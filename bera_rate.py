#!/usr/bin/env python3
"""
ERES-BERA-2026-001  bera_rate  v1.2  (rating-tier reference implementation)
A minimal, replayable rating surface for the Bio-Ecologic Resonance Architecture.

This file corrects three faults found in the prior synthesis draft, against the
canonical specs (BERA v1 + v1.1 addendum):

  FIX 1  block-A / block-B baseline split (BERA v1.1 §1.3).
         C0 is the mean aggregate coherence over the RESTING block (block A of
         the ERES-PELLIS A-B-A-B-A-B design). It is established ONCE, before any
         stressed window is measured. The prior draft self-baselined on the same
         window it measured, which pinned D(t) to 0 on every single-shot call.
         Here D(t) is computed against a fixed block-A baseline and therefore
         rises on a block-B (stressed) window, as the architecture requires.

  FIX 2  integer-deterministic aggregate, RHC, and D(t) (BERA v1.1 §1.2, v1 §6).
         The determinism boundary is the QUANTIZED coherence vector. From that
         point forward every quantity is computed in integer fixed-point:
           - C(t)  : integer cross-multiplication, floor-normalized by W_sum
           - RHC   : integer fourth root (two math.isqrt calls), NOT float ** .25
           - D(t)  : integer cross-multiplication, floor division
         math.isqrt is exact and platform-independent, so the rating record is
         bit-identical across platforms. The per-channel metrics in PART 2 are
         the sensor front-end; they remain OPEN (§1.1) and are the ONLY float
         step, by design held strictly upstream of the quantization line.

  FIX 3  the rating tier has zero knowledge of the gate.
         This module never imports, calls, or constructs a Gate, and never
         emits a candidate 'resonance' field. The gate/rating split (v1 §2)
         is enforced by the absence of any path from a RATE value to an
         admit/refuse decision. Tuning of gate thresholds, if ever wired, is a
         separate instrument's job and is out of scope here.

STILL OPEN (require JAS canonical lock; NOT for external citation):
  - per-channel coherence metric sub-specs (§1.1)
  - integer weight vector w_k (§1.2)            -- carried verbatim from draft
  - ARI / ERI / RCI canonical expansions (§5)   -- PROVISIONAL below
  - R6 / R7 dimension map (§6)                  -- held VEILED-R

ERES Institute for New Age Cybernetics | H2C2H | CCAL v2.1
Run:  python3 bera_rate.py     Clone-and-run: Python stdlib only.
"""

from __future__ import annotations
import math
import statistics
from dataclasses import dataclass
from enum import Enum
from typing import Any, List, Sequence

INSTRUMENT_ID = "ERES-BERA-2026-001"
VERSION = "v1.2 (rating-tier)"

MILLI = 1_000          # coherence fixed-point scale: c in [0, 1000] == [0,1]
MICRO = 1_000_000      # output fixed-point scale for C(t), D(t), RHC


# =============================================================================
# PART 1 - deterministic integer primitives (the replayable core)
# =============================================================================

def quantize(x: float) -> int:
    """Map a [0,1] float to integer milli-units, half-even, clamped to [0,1000].
    This is the determinism boundary: everything downstream is pure integer."""
    return max(0, min(MILLI, int(round(x * MILLI))))


def integer_fourth_root(p: int) -> int:
    """Floor of p**(1/4) via two exact integer square roots. Deterministic on
    every platform (math.isqrt is exact integer arithmetic, no FP)."""
    return math.isqrt(math.isqrt(p))


def aggregate_coherence_milli(c: "ChannelsMilli", weights: dict, w_sum: int) -> int:
    """C(t) in milli-units. Integer cross-multiplication, floor-normalized.
    (BERA v1.1 §1.2 -- integer weights, integer cross-multiplication.)"""
    s = (weights["hrv"] * c.hrv + weights["eda"] * c.eda +
         weights["resp"] * c.resp + weights["voc"] * c.voc)
    return s // w_sum                       # floor; deterministic


def rhc_milli(c: "ChannelsMilli") -> int:
    """Resonant Harmony Cycle (LOCKED name) as integer geometric mean of the
    four channels, in micro-units. RHC = (h*e*r*v)^(1/4) computed in fixed point:
      P = h*e*r*v               with each in [0,1000]  -> P in [0,1e12]
      rhc_micro = isqrt(isqrt(P * 1e12)) = P^(1/4) * 1e3 = RHC * 1e6
    No float exponentiation -- this is the §1.2 determinism fix for RHC."""
    p = c.hrv * c.eda * c.resp * c.voc      # 0 .. 1e12
    return integer_fourth_root(p * (MICRO * MICRO))   # 0 .. 1e6


def disruption_milli(c0_milli: int, c_t_milli: int) -> int:
    """D(t) in micro-units (BERA v1.1 §1.3):
       D = 0                              if C(t) >= C0
       D = clamp_[0,1]((C0 - C(t)) / C0)  otherwise
    Integer cross-multiplication + floor division; bounded [0, 1e6]."""
    if c0_milli <= 0:
        return 0
    if c_t_milli >= c0_milli:
        return 0
    return min(MICRO, (c0_milli - c_t_milli) * MICRO // c0_milli)


# =============================================================================
# PART 2 - coherence front-end (sensor sub-specs; §1.1 OPEN; ONLY float step)
# =============================================================================
# These are provisional metric proposals carried from the draft. They are the
# single floating-point stage and are held strictly UPSTREAM of quantize().
# Replacing them is a JAS lock item and does not affect the integer core.

class CoherenceMetrics:
    @staticmethod
    def hrv(rr: Sequence[float]) -> float:
        if len(rr) < 5:
            return 0.5
        diffs = [abs(rr[i + 1] - rr[i]) for i in range(len(rr) - 1)]
        rmssd = statistics.mean(diffs) if diffs else 0.0
        return min(1.0, rmssd / 50.0)       # PROVISIONAL: direction OPEN (§1.1)

    @staticmethod
    def eda(v: Sequence[float]) -> float:
        if len(v) < 5:
            return 0.5
        m = statistics.mean(v)
        if m == 0:
            return 1.0
        return max(0.0, 1.0 - min(1.0, statistics.stdev(v) / m))

    @staticmethod
    def resp(v: Sequence[float]) -> float:
        if len(v) < 3:
            return 0.5
        return max(0.0, 1.0 - min(1.0, abs(statistics.mean(v) - 6.0) / 6.0))

    @staticmethod
    def voc(v: Sequence[float]) -> float:
        if len(v) < 5:
            return 0.5
        m = statistics.mean(v)
        if m == 0:
            return 1.0
        return max(0.0, 1.0 - min(1.0, statistics.stdev(v) / m))


@dataclass(frozen=True)
class ChannelsMilli:
    """Quantized per-channel coherence, integer milli-units [0,1000]."""
    hrv: int
    eda: int
    resp: int
    voc: int

    @classmethod
    def from_window(cls, rr, eda, resp, voc) -> "ChannelsMilli":
        m = CoherenceMetrics
        return cls(quantize(m.hrv(rr)), quantize(m.eda(eda)),
                   quantize(m.resp(resp)), quantize(m.voc(voc)))


# =============================================================================
# PART 3 - RATE vector (7 dimensions, no scalar collapse; §6)
# =============================================================================

class VEILED_R(Enum):
    VEILED = "VEILED-R"
    def __repr__(self):
        return "VEILED-R"


@dataclass(frozen=True)
class RATEVector:
    # values stored as integer micro-units; floats are display-only
    ari: int
    eri: int
    rci: int
    rhc: int
    d_t: int
    r6: Any = VEILED_R.VEILED       # reserved; dimension map OPEN (§6)
    r7: Any = VEILED_R.VEILED

    def as_tuple(self) -> tuple:
        return (self.ari, self.eri, self.rci, self.rhc, self.d_t,
                repr(self.r6), repr(self.r7))   # always length 7

    def dimensions(self) -> int:
        return len(self.as_tuple())

    def __repr__(self):
        f = lambda u: u / MICRO
        return (f"RATE(ari={f(self.ari):.6f}, eri={f(self.eri):.6f}, "
                f"rci={f(self.rci):.6f}, rhc={f(self.rhc):.6f}, "
                f"d_t={f(self.d_t):.6f}, r6=VEILED-R, r7=VEILED-R)")


# =============================================================================
# PART 4 - rating engine with block-A baseline / block-B measurement split
# =============================================================================

class BERARating:
    # integer weights carried verbatim from the draft; w_k is a v2 lock item.
    WEIGHTS = {"hrv": 4, "eda": 2, "resp": 2, "voc": 0}
    W_SUM = sum(WEIGHTS.values())           # = 8

    # PROVISIONAL index expansions -- NOT locked, NOT for external citation.
    @staticmethod
    def _ari(c: ChannelsMilli) -> int:      # autonomic: 2*HRV + 1*EDA
        return (2 * c.hrv + 1 * c.eda) * MICRO // (3 * MILLI)

    @staticmethod
    def _eri(c: ChannelsMilli) -> int:      # ecologic: VOC
        return c.voc * MICRO // MILLI

    @staticmethod
    def _rci(c: ChannelsMilli) -> int:      # respiratory: RESP
        return c.resp * MICRO // MILLI

    def __init__(self):
        self._c0_milli: int | None = None   # block-A baseline; set once

    # ---- block A: establish baseline from one or more resting windows -------
    def establish_baseline(self, resting_windows: List[dict]) -> int:
        """Set C0 = integer mean of C(t) over the resting block (block A).
        Each window is {'rr':..., 'eda':..., 'resp':..., 'voc':...}.
        Returns C0 in milli-units. Must be called before rate()."""
        if not resting_windows:
            raise ValueError("block A is empty; cannot establish baseline")
        cs = []
        for w in resting_windows:
            ch = ChannelsMilli.from_window(w["rr"], w["eda"], w["resp"], w["voc"])
            cs.append(aggregate_coherence_milli(ch, self.WEIGHTS, self.W_SUM))
        self._c0_milli = sum(cs) // len(cs)         # integer mean
        return self._c0_milli

    # ---- block B: rate a (possibly stressed) measurement window -------------
    def rate(self, rr, eda, resp, voc) -> RATEVector:
        if self._c0_milli is None:
            raise RuntimeError("baseline not established; call establish_baseline() "
                               "on the resting block (A) first")
        ch = ChannelsMilli.from_window(rr, eda, resp, voc)
        c_t = aggregate_coherence_milli(ch, self.WEIGHTS, self.W_SUM)
        d_t = disruption_milli(self._c0_milli, c_t)
        return RATEVector(
            ari=self._ari(ch), eri=self._eri(ch), rci=self._rci(ch),
            rhc=rhc_milli(ch), d_t=d_t,
        )

    @property
    def baseline_milli(self) -> int | None:
        return self._c0_milli


# =============================================================================
# PART 5 - self-proving demo (the file proves its own claims, cf. eaap_proof)
# =============================================================================

def _gauss_window(seed, rr, eda, resp, voc, n=30):
    import random
    g = random.Random(seed)
    return {
        "rr":   [g.gauss(*rr)   for _ in range(n)],
        "eda":  [g.gauss(*eda)  for _ in range(n)],
        "resp": [g.gauss(*resp) for _ in range(n)],
        "voc":  [g.gauss(*voc)  for _ in range(n)],
    }


def main() -> int:
    bar = "=" * 70
    print(bar)
    print(f"{INSTRUMENT_ID}  {VERSION}")
    print("BERA rating-tier reference implementation (no gate; integer-deterministic)")
    print(bar)

    # Resting block A: coherent physiology (the baseline)
    block_A = [_gauss_window(10 + i, (800, 30), (2.0, 0.2), (6.0, 0.5), (100, 5))
               for i in range(3)]
    # Stressed block B: same generators as the audited draft (seed 99 family)
    block_B = _gauss_window(99, (650, 80), (5.0, 2.0), (15.0, 3.0), (200, 40))
    # A second resting window, to show D(t) returns toward 0 on recovery
    block_A2 = _gauss_window(7, (800, 30), (2.0, 0.2), (6.0, 0.5), (100, 5))

    bera = BERARating()
    c0 = bera.establish_baseline(block_A)
    print("\n[FIX 1] block-A baseline / block-B measurement")
    print(f"    C0 (block A mean, milli)   : {c0}   ( = {c0/MILLI:.3f} )")

    r_rest = bera.rate(**block_A2)
    r_stress = bera.rate(**block_B)
    print(f"    resting window  D(t)       : {r_rest.d_t/MICRO:.6f}"
          f"   (fresh resting window sits near baseline)")
    print(f"    STRESSED window D(t)       : {r_stress.d_t/MICRO:.6f}"
          f"   (RISES off baseline -- the fix)")
    ratio = r_stress.d_t / r_rest.d_t if r_rest.d_t else float('inf')
    print(f"    stress / rest disruption   : {ratio:.2f}x")
    print(f"    prior draft on same data   : 0.000000  (self-baselined -> pinned)")

    print("\n[D(t) RANGE CHECK]  feed descending coherence directly (pure D(t) law)")
    seq = [c0, int(c0 * 0.9), int(c0 * 0.7), int(c0 * 0.5),
           int(c0 * 0.3), int(c0 * 0.1), 0]
    d_seq = [disruption_milli(c0, c) / MICRO for c in seq]
    print(f"    C(t)/C0 : {[round(c / c0, 2) for c in seq]}")
    print(f"    D(t)    : {[round(d, 4) for d in d_seq]}")
    mono = all(d_seq[i] <= d_seq[i + 1] + 1e-12 for i in range(len(d_seq) - 1))
    bounded = all(0.0 <= d <= 1.0 for d in d_seq)
    print(f"    monotone non-decreasing    : {mono}")
    print(f"    bounded in [0,1]           : {bounded}")
    print(f"    collapse -> D(t)=1         : {d_seq[-1] == 1.0}")

    print("\n[FIX 2] integer-deterministic RHC (no float ** .25)")
    ref = ChannelsMilli(800, 700, 600, 500)        # known case: (.8*.7*.6*.5)^.25
    rhc = rhc_milli(ref) / MICRO
    float_ref = (0.8 * 0.7 * 0.6 * 0.5) ** 0.25
    print(f"    channels (.8,.7,.6,.5) RHC : {rhc:.6f}")
    print(f"    float reference            : {float_ref:.6f}")
    print(f"    integer == float to 4 dp   : {abs(rhc - float_ref) < 5e-5}"
          f"   (integer is floor-rooted, platform-identical)")

    print("\n[REPLAY]  same inputs -> identical RATE tuple, byte-for-byte")
    b1 = BERARating(); b1.establish_baseline(block_A)
    b2 = BERARating(); b2.establish_baseline(block_A)
    t1, t2 = b1.rate(**block_B).as_tuple(), b2.rate(**block_B).as_tuple()
    print(f"    run 1 : {t1}")
    print(f"    run 2 : {t2}")
    print(f"    identical                  : {t1 == t2}")

    print("\n[FIX 3] gate/rating split (structural, not textual)")
    import sys
    ns = vars(sys.modules[__name__])
    gate_imported = any("eaap" in m.lower() for m in list(sys.modules))
    gate_symbols = [k for k in ns if k in ("Gate", "evaluate", "emit_receipt")]
    rate_fields = set(RATEVector.__dataclass_fields__)
    leaks_resonance = "resonance" in rate_fields
    clean_split = (not gate_imported) and (not gate_symbols) and (not leaks_resonance)
    print(f"    imports a gate module      : {gate_imported}")
    print(f"    defines gate symbols       : {bool(gate_symbols)}")
    print(f"    RATE leaks 'resonance'     : {leaks_resonance}")
    print(f"    clean split                : {clean_split}   (True = rating cannot reach a decision)")

    print("\n[RATE VECTOR -- 7 dims, no scalar collapse]")
    print(f"    {r_stress}")
    print(f"    dimensions                 : {r_stress.dimensions()}")

    print(f"\n{bar}")
    holds = (d_seq[0] == 0.0 and r_stress.d_t > r_rest.d_t and mono and bounded
             and d_seq[-1] == 1.0 and abs(rhc - float_ref) < 5e-5
             and t1 == t2 and clean_split and r_stress.dimensions() == 7)
    print(f"RATING SURFACE HOLDS: {holds}")
    print(bar)
    return 0 if holds else 1


if __name__ == "__main__":
    raise SystemExit(main())
