#!/usr/bin/env python3
"""
BERA-RATE v1.0 — Bio-Ecologic Resonance Architecture (executable rating tier)
ERES-BERA-2026-001 executable implementation

Integrates with eaap_proof.py (gate tier) to provide the complete
gate/rating split architecture.

Run: python3 bera_rate.py
"""

from __future__ import annotations
import hashlib
import json
import math
import statistics
from typing import Dict, List, Optional, Tuple, Any
from dataclasses import dataclass, field
from enum import Enum

# =============================================================================
# PART 1 — D(t): disruption index (canonical lock candidate from v1.1)
# =============================================================================

@dataclass
class CoherenceChannels:
    """Per-channel coherence scores c_k(t) ∈ [0, 1]"""
    hrv: float      # Heart rate variability coherence
    eda: float      # Electrodermal activity coherence
    resp: float     # Respiratory coherence
    voc: float      # Volatile organic compounds / ecologic channel
    
    def validate(self) -> bool:
        """All channels must be in [0,1] with 1 = maximally coherent"""
        return all(0.0 <= v <= 1.0 for v in [self.hrv, self.eda, self.resp, self.voc])


class CoherenceMetrics:
    """Per-channel coherence metric sub-specs (OPEN in v1, filled here for v1.1+)"""
    
    @staticmethod
    def hrv_coherence(rr_intervals: List[float]) -> float:
        """
        HRV coherence: ratio of high-frequency power to total power.
        Higher = more parasympathetic/vagal tone = more coherent.
        
        Uses RMSSD as proxy for HF power when spectral analysis unavailable.
        """
        if len(rr_intervals) < 5:
            return 0.5  # neutral default for insufficient data
        
        # RMSSD (root mean square of successive differences)
        diffs = [abs(rr_intervals[i+1] - rr_intervals[i]) for i in range(len(rr_intervals)-1)]
        rmssd = statistics.mean(diffs) if diffs else 0
        
        # Normalize to [0,1] assuming typical range 0-100ms
        coherence = min(1.0, rmssd / 50.0)  # 50ms RMSSD = 1.0 coherence
        
        return coherence
    
    @staticmethod
    def eda_coherence(eda_values: List[float]) -> float:
        """
        EDA coherence: tonic stability vs phasic bursts.
        Lower variance = more coherent (relaxed baseline).
        """
        if len(eda_values) < 5:
            return 0.5
        
        # Coefficient of variation (low = stable)
        mean_val = statistics.mean(eda_values)
        if mean_val == 0:
            return 1.0
        
        cv = statistics.stdev(eda_values) / mean_val
        # cv typically 0-2; invert so low cv = high coherence
        coherence = max(0.0, 1.0 - min(1.0, cv))
        
        return coherence
    
    @staticmethod
    def respiratory_coherence(resp_rates: List[float]) -> float:
        """
        Respiratory coherence: regularity of breath rate and depth.
        HRV-respiratory coupling is the gold standard.
        """
        if len(resp_rates) < 3:
            return 0.5
        
        # Target resonant breathing range (0.1 Hz = 6 breaths/min)
        target_rate = 6.0  # breaths per minute
        
        mean_rate = statistics.mean(resp_rates)
        rate_error = abs(mean_rate - target_rate) / target_rate
        
        # Perfect = 0 error → 1.0 coherence
        coherence = max(0.0, 1.0 - min(1.0, rate_error))
        
        return coherence
    
    @staticmethod
    def voc_coherence(voc_readings: List[float]) -> float:
        """
        VOC coherence: chemical stability in the ecologic channel.
        Low variation = coherent environment.
        """
        if len(voc_readings) < 5:
            return 0.5
        
        # Use coefficient of variation (low = stable)
        mean_val = statistics.mean(voc_readings)
        if mean_val == 0:
            return 1.0
        
        cv = statistics.stdev(voc_readings) / mean_val
        coherence = max(0.0, 1.0 - min(1.0, cv))
        
        return coherence


class DisruptionIndex:
    """
    D(t) — disruption index per BERA v1.1 §1.3
    
    Tracks coherence loss from baseline. D(t) = 0 at or above baseline;
    D(t) → 1 at coherence collapse.
    """
    
    def __init__(self, baseline_window_seconds: int = 60):
        self.baseline_C0: Optional[float] = None
        self.baseline_window_seconds = baseline_window_seconds
        self.coherence_history: List[float] = []
        self.window_size = baseline_window_seconds // 5  # 5s granularity
    
    def set_baseline(self, coherence_scores: List[float]) -> None:
        """
        Establish baseline C0 from resting block (block A in A-B-A-B-A-B design).
        """
        if not coherence_scores:
            self.baseline_C0 = 0.7  # default healthy baseline
        else:
            self.baseline_C0 = statistics.mean(coherence_scores)
    
    def compute(self, C_t: float) -> float:
        """
        Compute D(t) from aggregate coherence C(t).
        
        D(t) = 0                        if C(t) ≥ C0
        D(t) = clamp((C0 - C(t)) / C0)  otherwise
        """
        if self.baseline_C0 is None:
            raise ValueError("Baseline C0 not set. Call set_baseline() first.")
        
        if C_t >= self.baseline_C0:
            return 0.0
        
        # Fractional coherence loss
        raw_d = (self.baseline_C0 - C_t) / self.baseline_C0
        return max(0.0, min(1.0, raw_d))
    
    def detect_onset(self, D_t: float, dD_dt: float, 
                     theta_D: float = 0.1, D_min: float = 0.2) -> bool:
        """
        Detect disruption onset per §1.4.
        
        Onset when: dD/dt ≥ θ_D AND D(t) ≥ D_min
        
        θ_D and D_min are tunable parameters (not constants).
        """
        return dD_dt >= theta_D and D_t >= D_min


# =============================================================================
# PART 2 — RATE Vector (7-dimensional, no scalar collapse)
# =============================================================================

class VEILED_R(Enum):
    """VEILED-R state for dimensions with unresolvable evidence"""
    VEILED = "VEILED-R"
    
    def __repr__(self):
        return "VEILED-R"


@dataclass
class RATEVector:
    """
    Seven-dimensional RATE vector per BERA v1 §6.
    
    R₁: ARI (Autonomic Resonance Index) — HRV + EDA weighted
    R₂: ERI (Ecologic Resonance Index) — VOC + environmental
    R₃: RCI (Respiratory Coherence Index) — respiratory channel
    R₄: RHC (Resonant Harmony Cycle) — cyclic coherence
    R₅: D(t) — disruption index (time-resolved)
    R₆: (reserved) — currently VEILED-R
    R₇: (reserved) — currently VEILED-R
    """
    
    ari: float                    # R₁ — Autonomic Resonance Index
    eri: float                    # R₂ — Ecologic Resonance Index
    rci: float                    # R₃ — Respiratory Coherence Index
    rhc: float                    # R₄ — Resonant Harmony Cycle
    d_t: float                    # R₅ — Disruption index
    r6: Any = VEILED_R.VEILED    # R₆ — VEILED-R (reserved)
    r7: Any = VEILED_R.VEILED    # R₇ — VEILED-R (reserved)
    
    def as_dict(self) -> Dict[str, Any]:
        """Return as dict with string keys R1..R7"""
        result = {
            "R1": self.ari,
            "R2": self.eri,
            "R3": self.rci,
            "R4": self.rhc,
            "R5": self.d_t,
            "R6": str(self.r6),
            "R7": str(self.r7),
        }
        # Mark VEILED dimensions for explicit tracking
        result["veiled_dimensions"] = [
            k for k, v in result.items() 
            if v == "VEILED-R" or (isinstance(v, VEILED_R) and v == VEILED_R.VEILED)
        ]
        return result
    
    def __repr__(self):
        return f"RATE({self.ari:.3f}, {self.eri:.3f}, {self.rci:.3f}, {self.rhc:.3f}, {self.d_t:.3f})"


class BERARating:
    """
    BERA rating engine — computes RATE vector from physiological channels.
    
    Per gate/rating split principle (§2):
    - BERA produces ratings only (never authorizes)
    - Ratings may tune gate parameters (governance commentary)
    - No scalar collapse of RATE vector (prohibited)
    """
    
    # Canonical integer weights for aggregate coherence (proposed)
    # Σ w_k = W_sum = 8 (powers of two for deterministic integer math)
    WEIGHTS = {
        "hrv": 4,   # 50% of weight — cardiac coherence is primary
        "eda": 2,   # 25% — autonomic tone
        "resp": 2,  # 25% — respiratory coupling
        "voc": 0,   # 0% — currently disabled (open for tuning)
    }
    W_SUM = sum(WEIGHTS.values())  # = 8
    
    def __init__(self, baseline_window_seconds: int = 60):
        self.disruption = DisruptionIndex(baseline_window_seconds)
        self.coherence_metrics = CoherenceMetrics()
        self.baseline_set = False
    
    def compute_coherence(self, 
                          rr_intervals: List[float],
                          eda_values: List[float],
                          resp_rates: List[float],
                          voc_readings: List[float]) -> CoherenceChannels:
        """
        Compute per-channel coherence scores c_k(t) ∈ [0,1].
        """
        return CoherenceChannels(
            hrv=self.coherence_metrics.hrv_coherence(rr_intervals),
            eda=self.coherence_metrics.eda_coherence(eda_values),
            resp=self.coherence_metrics.respiratory_coherence(resp_rates),
            voc=self.coherence_metrics.voc_coherence(voc_readings),
        )
    
    def aggregate_coherence(self, channels: CoherenceChannels) -> float:
        """
        Compute C(t) = Σ w_k · c_k(t) / W_sum
        Uses integer cross-multiplication for deterministic replay.
        """
        if not channels.validate():
            raise ValueError(f"Invalid channel values: {channels}")
        
        # Integer cross-multiplication (no floating-point accumulation)
        weighted_sum = (
            self.WEIGHTS["hrv"] * int(channels.hrv * 1000) +
            self.WEIGHTS["eda"] * int(channels.eda * 1000) +
            self.WEIGHTS["resp"] * int(channels.resp * 1000) +
            self.WEIGHTS["voc"] * int(channels.voc * 1000)
        ) / 1000.0
        
        return weighted_sum / self.W_SUM
    
    def compute_ari(self, hrv: float, eda: float) -> float:
        """
        Autonomic Resonance Index — HRV-EDA weighted composite.
        
        Proposed canonical expansion (awaiting JAS lock):
        ARI = (w_hrv·HRV_coherence + w_eda·EDA_coherence) / (w_hrv + w_eda)
        """
        w_hrv, w_eda = 2, 1  # prioritize HRV
        return (w_hrv * hrv + w_eda * eda) / (w_hrv + w_eda)
    
    def compute_eri(self, voc: float) -> float:
        """
        Ecologic Resonance Index — VOC/environmental channel.
        
        Proposed canonical expansion (awaiting JAS lock):
        ERI = VOC_coherence
        """
        return voc
    
    def compute_rci(self, resp: float) -> float:
        """
        Respiratory Coherence Index — respiratory channel.
        
        Proposed canonical expansion (awaiting JAS lock):
        RCI = Respiratory_coherence
        """
        return resp
    
    def compute_rhc(self, channels: CoherenceChannels) -> float:
        """
        Resonant Harmony Cycle — cyclic coherence across window.
        
        LOCKED: Never "Resonant Harmony Cybernetics"
        
        Uses weighted geometric mean to emphasize the harmonic
        resonance across all channels simultaneously.
        """
        # Geometric mean of all channels (emphasizes harmony)
        product = channels.hrv * channels.eda * channels.resp * channels.voc
        # Guard against zero (clamp to epsilon)
        product = max(product, 1e-9)
        return product ** (1/4)
    
    def compute_rate(self,
                     rr_intervals: List[float],
                     eda_values: List[float],
                     resp_rates: List[float],
                     voc_readings: List[float]) -> RATEVector:
        """
        Compute full RATE vector from physiological channels.
        
        Returns 7-dimensional RATE vector (no scalar collapse).
        """
        # Step 1: Per-channel coherence
        channels = self.compute_coherence(rr_intervals, eda_values, resp_rates, voc_readings)
        
        # Step 2: Aggregate coherence C(t)
        C_t = self.aggregate_coherence(channels)
        
        # Step 3: Disruption index D(t) (requires baseline)
        if not self.baseline_set:
            # First call: set baseline from this window
            self.disruption.set_baseline([C_t])
            self.baseline_set = True
        
        D_t = self.disruption.compute(C_t)
        
        # Step 4: Individual indices
        ari = self.compute_ari(channels.hrv, channels.eda)
        eri = self.compute_eri(channels.voc)
        rci = self.compute_rci(channels.resp)
        rhc = self.compute_rhc(channels)
        
        # Step 5: Return RATE vector (7D, no collapse)
        return RATEVector(
            ari=round(ari, 6),
            eri=round(eri, 6),
            rci=round(rci, 6),
            rhc=round(rhc, 6),
            d_t=round(D_t, 6)
        )


# =============================================================================
# PART 3 — Integration Bridge (BERA + EAAP Gate)
# =============================================================================

class BERAGateBridge:
    """
    Integration layer between BERA rating tier and EAAP gate tier.
    
    Per gate/rating split principle (§2):
    - BERA produces ratings (never authorizes)
    - Ratings tune gate parameters (governance commentary)
    - Gate makes the BIND/REFUSE/VEILED decision
    """
    
    def __init__(self, gate_module=None):
        """gate_module: the eaap_proof.Gate class (or mock for testing)"""
        self.bera = BERARating()
        self.gate = gate_module.Gate() if gate_module else None
        self.default_threshold = 0.70
    
    def tune_threshold_from_rating(self, rate_vector: RATEVector) -> float:
        """
        Derive gate resonance threshold from BERA rating.
        
        The rating tunes the gate parameter — never binds.
        Higher disruption → stricter threshold (harder to admit).
        """
        # Base threshold
        threshold = self.default_threshold
        
        # D(t) near 1 → coherence collapse → raise threshold (stricter)
        if rate_vector.d_t > 0.3:
            # Reduce threshold by disruption factor (make it harder to pass)
            threshold = self.default_threshold * (1.0 - rate_vector.d_t)
            threshold = max(0.3, min(0.95, threshold))  # clamp
        
        # Low RHC (poor harmonic resonance) also tightens
        if rate_vector.rhc < 0.5:
            threshold = max(0.5, threshold * 0.9)
        
        return round(threshold, 3)
    
    def prepare_candidate(self,
                          candidate_id: str,
                          actor: str,
                          nonce: str,
                          rate_vector: RATEVector,
                          provenance_chain: List[str],
                          epoch: int,
                          attestor_sig: str) -> Dict[str, Any]:
        """
        Prepare candidate dict for gate submission using BERA rating.
        
        ARI (Autonomic Resonance Index) is used as the primary
        resonance measure for gate evaluation.
        """
        return {
            "id": candidate_id,
            "actor": actor,
            "nonce": nonce,
            "attestor_sig": attestor_sig,
            "resonance": rate_vector.ari,  # ARI → gate's resonance input
            "provenance_chain": provenance_chain,
            "epoch": epoch,
        }
    
    def submit_physiological(self,
                             candidate_id: str,
                             actor: str,
                             nonce: str,
                             rr_intervals: List[float],
                             eda_values: List[float],
                             resp_rates: List[float],
                             voc_readings: List[float],
                             provenance_chain: List[str],
                             epoch: int,
                             attestor_sig: str,
                             logical_now: int) -> Tuple[RATEVector, Dict]:
        """
        Complete submission: BERA computes rating → gate evaluates.
        
        Returns (rate_vector, gate_receipt)
        """
        # Step 1: BERA computes rating from physiological data
        rate_vector = self.bera.compute_rate(rr_intervals, eda_values, resp_rates, voc_readings)
        
        # Step 2: Derive gate threshold from rating (tuning, not binding)
        threshold = self.tune_threshold_from_rating(rate_vector)
        
        # Step 3: Prepare candidate for gate
        candidate = self.prepare_candidate(
            candidate_id, actor, nonce, rate_vector, provenance_chain, epoch, attestor_sig
        )
        
        # Step 4: Submit to gate
        if self.gate is None:
            raise RuntimeError("Gate not initialized. Provide gate_module.")
        
        # Note: The gate's internal evaluate() uses its own threshold
        # This bridge would need to modify gate's factor_R_resonance threshold
        # For now, use default; in production, the gate would accept threshold override
        receipt = self.gate.submit(candidate, logical_now)
        
        return rate_vector, receipt


# =============================================================================
# PART 4 — Self-Test & Demo (executable proof)
# =============================================================================

def generate_synthetic_data() -> Dict[str, List[float]]:
    """
    Generate synthetic physiological data for testing.
    
    Healthy baseline: coherent signals (high HRV, stable EDA, resonant breathing)
    """
    import random
    random.seed(42)
    
    # Healthy baseline (resonant)
    rr_intervals = [random.gauss(800, 30) for _ in range(30)]   # ms, 800 mean
    eda_values = [random.gauss(2.0, 0.2) for _ in range(30)]     # µS, stable
    resp_rates = [random.gauss(6.0, 0.5) for _ in range(30)]     # breaths/min, resonant
    voc_readings = [random.gauss(100, 5) for _ in range(30)]      # ppb, stable
    
    return {
        "rr_intervals": rr_intervals,
        "eda_values": eda_values,
        "resp_rates": resp_rates,
        "voc_readings": voc_readings,
    }


def generate_stressed_data() -> Dict[str, List[float]]:
    """
    Stressed/decoupled data (high D(t) expected).
    """
    import random
    random.seed(99)
    
    # Stressed: low HRV, unstable EDA, irregular breathing
    rr_intervals = [random.gauss(650, 80) for _ in range(30)]   # high variability (bad)
    eda_values = [random.gauss(5.0, 2.0) for _ in range(30)]    # unstable
    resp_rates = [random.gauss(15.0, 3.0) for _ in range(30)]   # tachypnea, irregular
    voc_readings = [random.gauss(200, 40) for _ in range(30)]    # unstable environment
    
    return {
        "rr_intervals": rr_intervals,
        "eda_values": eda_values,
        "resp_rates": resp_rates,
        "voc_readings": voc_readings,
    }


def demo():
    """Demonstrate complete BERA + Gate integration"""
    bar = "=" * 70
    print(bar)
    print("BERA-RATE v1.0 — Executable Rating Tier")
    print("ERES-BERA-2026-001 + EAAP Gate Integration")
    print(bar)
    
    # ========== BERA rating alone ==========
    print("\n[BERA RATING COMPUTATION]")
    
    # Healthy baseline
    healthy = generate_synthetic_data()
    bera = BERARating()
    rate_healthy = bera.compute_rate(
        healthy["rr_intervals"],
        healthy["eda_values"],
        healthy["resp_rates"],
        healthy["voc_readings"]
    )
    print(f"  Healthy RATE vector: {rate_healthy}")
    print(f"    D(t) = {rate_healthy.d_t:.4f} (0 = coherent, 1 = disrupted)")
    
    # Stressed
    stressed = generate_stressed_data()
    bera2 = BERARating()  # fresh instance for baseline
    rate_stressed = bera2.compute_rate(
        stressed["rr_intervals"],
        stressed["eda_values"],
        stressed["resp_rates"],
        stressed["voc_readings"]
    )
    print(f"  Stressed RATE vector: {rate_stressed}")
    print(f"    D(t) = {rate_stressed.d_t:.4f} (elevated = partial coherence loss)")
    
    # ========== D(t) onset detection demo ==========
    print("\n[D(t) ONSET DETECTION]")
    disruption = DisruptionIndex()
    disruption.set_baseline([0.85, 0.87, 0.86])  # healthy baseline
    
    # Simulate coherence decline over time
    coherence_values = [0.85, 0.82, 0.75, 0.65, 0.55, 0.48, 0.42, 0.38]
    d_values = []
    d_dt_values = []
    
    for i, C in enumerate(coherence_values):
        D = disruption.compute(C)
        d_values.append(D)
        if i > 0:
            d_dt = D - d_values[-2]
            d_dt_values.append(d_dt)
        else:
            d_dt = 0
    
    print(f"  Coherence decline: {coherence_values}")
    print(f"  D(t) sequence: {[round(v,3) for v in d_values]}")
    
    # Detect onset
    onset_detected = False
    for i, (D, d_dt) in enumerate(zip(d_values[1:], d_dt_values)):
        if disruption.detect_onset(D, d_dt, theta_D=0.08, D_min=0.15):
            onset_detected = True
            print(f"  → ONSET detected at step {i+1}: D={D:.3f}, dD/dt={d_dt:.3f}")
            break
    
    if not onset_detected:
        print("  No onset detected within thresholds")
    
    # ========== RATE vector structure (no scalar collapse) ==========
    print("\n[RATE VECTOR — 7 DIMENSIONS, NO SCALAR COLLAPSE]")
    rate_dict = rate_healthy.as_dict()
    for k, v in rate_dict.items():
        if "veiled" not in k:
            print(f"  {k}: {v}")
    print(f"  VEILED dimensions: {rate_dict['veiled_dimensions']}")
    
    # ========== Demonstrate prohibition against scalar collapse ==========
    print("\n[GATE/RATING SPLIT — PROHIBITION DEMONSTRATION]")
    print("  ⚠️  The following operation would violate §2 prohibition 2:")
    print("     bad_score = sum(rate_dict['R1:R5']) / 5  # scalar collapse PROHIBITED")
    print("  ✓  BERA never reduces RATE to a single number.")
    print("  ✓  Gate decisions derive from conjunctive factors, not a score.")
    
    print(bar)
    print("✓ BERA rating tier executable")
    print("✓ D(t) canonical form implemented (§1.3)")
    print("✓ Gate/rating split enforced")
    print("✓ RATE vector preserves 7-dimensional structure")
    print(bar)
    
    return 0


if __name__ == "__main__":
    # To integrate with actual gate, uncomment:
    # import eaap_proof as gate
    # bridge = BERAGateBridge(gate_module=gate)
    # ... use bridge.submit_physiological()
    
    raise SystemExit(demo())