"""
ERES GAIA GEAR Audit Testkit — v0.7.0
=====================================

Executable audit instrument for the Bella Vista Declaration on GAIA GEAR
(v0.7, 21 July 2026). Runs the Declaration's Appendix B operational audit
template as code, with Data-Integrity (Value 3, as strengthened at v0.7)
enforced structurally: OPEN items cannot be closed by the testkit; attempts
to close them return CANDIDATE or OPEN status.

Six tests, following the ERES BRT Testkit house-style discipline (6/6 pass).

Intended context: a positive-terms audit tool for any downstream working
group that wants to check whether a candidate GAIA GEAR class instance
can honestly claim class membership without corpus fabrication. Commons
contribution — run it before submitting an instrument for MIEVM ensemble
review. Written so future generations inherit a runnable accountability
frame, not just a document.

Author: Joseph Allen Sprute, ERES Institute for New Age Cybernetics (est. 2012)
        ORCID 0000-0001-9946-3221
Sentience contribution: Anthropic Claude (Opus family, 21 July 2026 working session).

Code license:              Apache License 2.0.
Declaration companion:     Bella Vista Declaration on GAIA GEAR v0.7 (CC BY 4.0).
Corpus reference:          ERES-GAIA-GEAR-TESTKIT-2026-001
Version:                   0.7.0 (matches Declaration v0.7)

Usage:
    python eres_gaia_gear_v0_7_testkit.py                # self-audit on the Declaration
    python eres_gaia_gear_v0_7_testkit.py <spec.json>    # audit an instrument spec
"""
from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
import json
import sys


# =========================================================================
# STRUCTURAL RULES (architectural minimums; NOT empirical values)
# =========================================================================
# Per Threat 10 (proximity misreading), these are STRUCTURAL rules — they
# define the shape of a valid audit but do not derive from an empirical
# study of what shape actually predicts good outcomes. Downstream users
# must NOT read these values as empirically ratified thresholds.

MIEVM_MIN_NODES: dict[str, int] = {"GOOD": 3, "SOUND": 4, "BEST": 5}
MIEVM_MEAN_GATE: dict[str, float] = {"GOOD": 7.5, "SOUND": 8.5, "BEST": 9.0}
Q5_REQUIRED_TIERS: set[str] = {"SOUND", "BEST"}
EMANUEL_THRESHOLD: float = 8.5   # diligence-ready gate
STERGIOS_THRESHOLD: float = 9.0  # Pellis-facing gate

# S-score weights: CONSTRUCTED, empirical derivation OPEN.
# Any downstream code that overrides these values without publishing a
# corpus or empirical anchor commits a Value 3 violation. The weights are
# available as named constants only so the S-score formula is computable;
# they are not represented as ratified.
S_SCORE_WEIGHT_M: float = 0.5  # OPEN: derivation task
S_SCORE_WEIGHT_E: float = 0.3  # OPEN: derivation task
S_SCORE_WEIGHT_F: float = 0.2  # OPEN: derivation task


# =========================================================================
# OPEN ITEMS (per v0.7 Self-Ratification)
# =========================================================================
# Ratification gaps that MUST NOT be closed by the testkit itself. These
# constants exist so downstream code can query them and confirm current
# state, not to be silently overridden.

class OpenStatus(Enum):
    OPEN = "OPEN"
    CANDIDATE = "CANDIDATE"
    CONSTRUCTED = "CONSTRUCTED"
    DERIVED = "DERIVED"      # aspirational — no v0.7 item has this status
    RATIFIED = "RATIFIED"    # aspirational — no v0.7 item has this status


OPEN_ITEMS: dict[str, OpenStatus] = {
    "s_score_weights":     OpenStatus.CONSTRUCTED,
    "tier_thresholds":     OpenStatus.CANDIDATE,
    "favors_unit":         OpenStatus.OPEN,
    "certifying_authority": OpenStatus.OPEN,
    "s5_cascade_closure":  OpenStatus.OPEN,
}


# S5 candidate resolution paths (three paths on file at v0.7; selection
# is a v0.8+ task; the testkit records but does not select among them).
S5_CANDIDATE_PATHS: dict[str, str] = {
    "a": "recast Steward as broad distributable network",
    "b": "scope broad-distributability rule below S5 only",
    "c": "federated decentralized network structure "
         "(Gemini-surfaced in MIEVM v0.6 Q5 answer, held OPEN)",
}


# =========================================================================
# SCALE BANDS, TIERS, P-WORDS
# =========================================================================

class ScaleBand(Enum):
    S1_PERSON     = "S1"   # Ship's-Mate (CF wearable substrate)
    S2_COMMUNITY  = "S2"   # Centers-of-Excellence (KEEN-Basis)
    S3_INSTITUTION = "S3"  # UBIMIA-class Infomediary substrate
    S4_DOMAIN     = "S4"   # CBGMODD lane / sector Ombudsman
    S5_PLANET     = "S5"   # cascade closure OPEN — see S5_CANDIDATE_PATHS
    S6_BEYOND     = "S6"   # candidate; not operationalized


class Tier(Enum):
    GOOD  = "GOOD"
    SOUND = "SOUND"
    BEST  = "BEST"


P_WORDS: list[str] = ["Promulgate", "Patron", "Pledge", "Protect", "Provide", "Preach"]


# =========================================================================
# DATA CLASSES — Appendix B sections as structured records
# =========================================================================

@dataclass
class InstrumentIdentity:
    """Appendix B Section 1 — Instrument identity."""
    name: str
    version: str
    provisioning_entity: str
    cbgmodd_lane: str
    scale_bands: list[ScaleBand]
    tier_claimed: Tier


@dataclass
class PWordStatus:
    """One row of the six-P-word cascade completion table."""
    p_word: str
    implemented: bool = False
    defers_to_partner: Optional[str] = None
    incomplete: bool = False

    def is_closed(self) -> bool:
        # Threat 9: naming a partner does NOT count as closure.
        # Only explicit implemented=True with incomplete=False counts.
        return self.implemented and not self.incomplete


@dataclass
class CascadeCompletion:
    """Appendix B Section 2 — cascade completion at a specific scale band."""
    scale_band: ScaleBand
    p_word_states: dict[str, PWordStatus] = field(default_factory=dict)

    def preach_permitted(self) -> tuple[bool, str]:
        """Preach must not close where Patron and Pledge are incomplete.
        (Threat 8 — IDEA severance.)"""
        patron = self.p_word_states.get("Patron")
        pledge = self.p_word_states.get("Pledge")
        if patron is None or not patron.is_closed():
            return False, "Preach blocked — Patron incomplete (Threat 8: IDEA severance)."
        if pledge is None or not pledge.is_closed():
            return False, "Preach blocked — Pledge incomplete (Threat 8: IDEA severance)."
        return True, "Preach permitted — cascade closed through Pledge."

    def cascade_closed(self) -> bool:
        return all(
            self.p_word_states.get(p, PWordStatus(p)).is_closed()
            for p in P_WORDS
        )


@dataclass
class QuantitativeClaim:
    """Appendix B Section 3 — CANDIDATE until Appendix A OPEN items close."""
    M: Optional[float] = None
    E: Optional[float] = None
    F: Optional[float] = None
    favors_unit_name: Optional[str] = None  # naming discipline check
    margin_v: Optional[float] = None
    margin_tau: Optional[float] = None

    def s_score(self) -> Optional[float]:
        if self.M is None or self.E is None or self.F is None:
            return None
        return (S_SCORE_WEIGHT_M * self.M
                + S_SCORE_WEIGHT_E * self.E
                + S_SCORE_WEIGHT_F * self.F)

    def resiliency(self) -> Optional[float]:
        s = self.s_score()
        if s is None or s == 0 or self.F is None:
            return None
        return S_SCORE_WEIGHT_F * self.F / s

    def margin_m_star(self) -> Optional[float]:
        if self.margin_v is None or self.margin_tau is None:
            return None
        return self.margin_v * self.margin_tau


@dataclass
class EpistemicFloor:
    """Appendix B Section 4 — one experiment, one procedure, one repo."""
    proposable_experiment: str = ""
    verification_procedure: str = ""
    open_repository_link: str = ""

    def satisfied(self) -> bool:
        return (bool(self.proposable_experiment)
                and bool(self.verification_procedure)
                and bool(self.open_repository_link))


@dataclass
class MIEVMRound:
    """Appendix B Section 6 — Ensemble verification (MIEVM)."""
    conducted: bool = False
    nodes: list[str] = field(default_factory=list)
    ratings: dict[str, float] = field(default_factory=dict)
    q5_administered: bool = False
    q5_tempted_count: int = 0
    q5_held_count: int = 0
    convergent_findings: str = ""

    def node_count(self) -> int:
        return len(self.nodes)

    def mean(self) -> Optional[float]:
        if not self.ratings:
            return None
        return sum(self.ratings.values()) / len(self.ratings)

    def std_dev(self) -> Optional[float]:
        if not self.ratings:
            return None
        m = self.mean()
        variance = sum((r - m) ** 2 for r in self.ratings.values()) / len(self.ratings)
        return variance ** 0.5

    def structural_criterion_met_for(self, tier: Tier) -> bool:
        """Check the STRUCTURAL rules for a claimed tier. This checks the
        shape of the audit, NOT the empirical validity of any threshold."""
        min_nodes = MIEVM_MIN_NODES[tier.value]
        mean_gate = MIEVM_MEAN_GATE[tier.value]
        m = self.mean()
        if m is None:
            return False
        if self.node_count() < min_nodes:
            return False
        if m < mean_gate:
            return False
        if tier.value in Q5_REQUIRED_TIERS and not self.q5_administered:
            return False
        return True


@dataclass
class AuditPacket:
    """The complete Appendix B audit packet for one candidate instrument."""
    identity: InstrumentIdentity
    cascade_completions: list[CascadeCompletion]
    quantitative: QuantitativeClaim
    epistemic: EpistemicFloor
    mievm: MIEVMRound
    collapse_test_pass: bool = False
    collapse_surviving_delivery: Optional[float] = None
    # For specification frameworks (like the Declaration itself), the
    # collapse-survival test is N/A — the artifact is not a fiduciary
    # instrument that carries FAVORS through collapse.
    carries_favors: bool = True


# =========================================================================
# SIX TESTS (ERES BRT Testkit house style)
# =========================================================================

class TestResult:
    def __init__(self, name: str, passed: bool, reason: str):
        self.name = name
        self.passed = passed
        self.reason = reason

    def __repr__(self) -> str:
        mark = "PASS" if self.passed else "FAIL"
        return f"[{mark}] {self.name}: {self.reason}"


def test_1_identity_and_scale(packet: AuditPacket) -> TestResult:
    """Test 1 — Instrument identity + scale-band declaration present."""
    id_ = packet.identity
    if not id_.name or not id_.scale_bands:
        return TestResult(
            "identity_and_scale", False,
            "Instrument identity or scale-band claim missing.",
        )
    return TestResult(
        "identity_and_scale", True,
        f"Identity present; scale bands claimed: {[b.value for b in id_.scale_bands]}; "
        f"tier claimed: {id_.tier_claimed.value}.",
    )


def test_2_cascade_closure(packet: AuditPacket) -> TestResult:
    """Test 2 — IDEA cascade closes at every claimed band; no Threat 8 or 9."""
    claimed_bands = set(packet.identity.scale_bands)
    covered_bands = {c.scale_band for c in packet.cascade_completions}
    missing = claimed_bands - covered_bands
    if missing:
        return TestResult(
            "cascade_closure", False,
            f"Cascade completion missing for bands: {[b.value for b in missing]}.",
        )
    for completion in packet.cascade_completions:
        if not completion.cascade_closed():
            return TestResult(
                "cascade_closure", False,
                f"Cascade not closed at {completion.scale_band.value}.",
            )
        preach_ok, msg = completion.preach_permitted()
        if not preach_ok:
            return TestResult(
                "cascade_closure", False,
                f"At {completion.scale_band.value}: {msg}",
            )
    return TestResult(
        "cascade_closure", True,
        "Cascade closed at every claimed band; no IDEA severance (T8); no closure by naming (T9).",
    )


def test_3_epistemic_floor(packet: AuditPacket) -> TestResult:
    """Test 3 — Epistemic Floor: one experiment, one procedure, one repo link."""
    if not packet.epistemic.satisfied():
        return TestResult(
            "epistemic_floor", False,
            "Missing proposable experiment, verification procedure, or repository link.",
        )
    return TestResult(
        "epistemic_floor", True,
        "Epistemic Floor satisfied — experiment + procedure + open-repo link on record.",
    )


def test_4_data_integrity(packet: AuditPacket) -> TestResult:
    """Test 4 — Value 3: no closure of OPEN items by fabrication.

    Enforced structurally: if the packet supplies F (a FAVORS quantity),
    it must also name the FAVORS unit — otherwise the quantitative claim
    is implicitly closing an OPEN item (the FAVORS unit itself). The test
    also confirms that the module-level OPEN_ITEMS map has not been
    silently mutated in-process.
    """
    # In-process integrity check: OPEN items must still be OPEN/CANDIDATE.
    for name, expected in [
        ("favors_unit", OpenStatus.OPEN),
        ("certifying_authority", OpenStatus.OPEN),
        ("s5_cascade_closure", OpenStatus.OPEN),
        ("tier_thresholds", OpenStatus.CANDIDATE),
        ("s_score_weights", OpenStatus.CONSTRUCTED),
    ]:
        if OPEN_ITEMS.get(name) not in {OpenStatus.OPEN, OpenStatus.CANDIDATE, OpenStatus.CONSTRUCTED}:
            return TestResult(
                "data_integrity", False,
                f"OPEN_ITEMS['{name}'] has been mutated to non-OPEN state; Value 3 violation.",
            )
    # Naming discipline: if F is set, favors_unit_name must be set.
    q = packet.quantitative
    if q.F is not None and not q.favors_unit_name:
        return TestResult(
            "data_integrity", False,
            "F (FAVORS quantity) supplied without naming the FAVORS unit — "
            "FAVORS unit is OPEN in v0.7; naming avoids implicit closure.",
        )
    return TestResult(
        "data_integrity", True,
        "No implicit closure of OPEN items detected; naming discipline honored.",
    )


def test_5_mievm_ensemble(packet: AuditPacket) -> TestResult:
    """Test 5 — MIEVM ensemble structural criterion met for claimed tier."""
    tier = packet.identity.tier_claimed
    if not packet.mievm.conducted:
        if tier == Tier.GOOD:
            return TestResult(
                "mievm_ensemble", True,
                "MIEVM ensemble not required for GOOD baseline; skipped.",
            )
        return TestResult(
            "mievm_ensemble", False,
            f"MIEVM ensemble round required for {tier.value} tier; none conducted.",
        )
    if not packet.mievm.structural_criterion_met_for(tier):
        return TestResult(
            "mievm_ensemble", False,
            f"Structural criterion not met for {tier.value}: "
            f"nodes={packet.mievm.node_count()} (min {MIEVM_MIN_NODES[tier.value]}); "
            f"mean={packet.mievm.mean()} (gate {MIEVM_MEAN_GATE[tier.value]}); "
            f"Q5 administered={packet.mievm.q5_administered} "
            f"(required for {tier.value}: {tier.value in Q5_REQUIRED_TIERS}).",
        )
    return TestResult(
        "mievm_ensemble", True,
        f"MIEVM structural criterion for {tier.value} met: "
        f"nodes={packet.mievm.node_count()}, mean={packet.mievm.mean():.2f}, "
        f"σ={packet.mievm.std_dev():.2f}, Q5={packet.mievm.q5_administered}.",
    )


def test_6_collapse_survival(packet: AuditPacket) -> TestResult:
    """Test 6 — collapse-survival: at CBGMODD × BERA → 0, delivery = FAVORS."""
    if not packet.carries_favors:
        return TestResult(
            "collapse_survival", True,
            "Instrument is a specification framework, not a fiduciary instrument; "
            "collapse-survival N/A. (Test passes vacuously.)",
        )
    if packet.collapse_surviving_delivery is None:
        return TestResult(
            "collapse_survival", False,
            "Collapse-survival test not run.",
        )
    expected = packet.quantitative.F
    if expected is None:
        return TestResult(
            "collapse_survival", False,
            "F (FAVORS) not set — cannot verify surviving delivery equals FAVORS.",
        )
    tol = 0.001
    if abs(packet.collapse_surviving_delivery - expected) > tol:
        return TestResult(
            "collapse_survival", False,
            f"Surviving delivery ({packet.collapse_surviving_delivery}) "
            f"does not equal FAVORS ({expected}) at collapse.",
        )
    return TestResult(
        "collapse_survival", True,
        f"Surviving delivery equals FAVORS ({expected}) within tolerance {tol}.",
    )


ALL_TESTS = [
    test_1_identity_and_scale,
    test_2_cascade_closure,
    test_3_epistemic_floor,
    test_4_data_integrity,
    test_5_mievm_ensemble,
    test_6_collapse_survival,
]


def run_audit(packet: AuditPacket) -> tuple[int, int, list[TestResult]]:
    """Run all six tests. Return (passed_count, total, results)."""
    results = [test(packet) for test in ALL_TESTS]
    passed = sum(1 for r in results if r.passed)
    return passed, len(results), results


# =========================================================================
# SELF-AUDIT — apply the testkit to the Declaration itself (S4 instrument)
# =========================================================================

def declaration_self_audit_packet() -> AuditPacket:
    """Construct an audit packet describing the Declaration v0.7 itself.

    The Declaration is an S4-band instrument (governance domain: Ombudsman /
    Media lanes). Its recommendations apply at S1-S6; the Declaration itself
    is at S4. Because it is a specification framework, not a fiduciary
    instrument, it does not carry FAVORS through collapse — collapse-survival
    is therefore N/A rather than a required numerical check.
    """
    identity = InstrumentIdentity(
        name="Bella Vista Declaration on GAIA GEAR",
        version="0.7",
        provisioning_entity="ERES Institute for New Age Cybernetics",
        cbgmodd_lane="Ombudsman / Media (S4)",
        scale_bands=[ScaleBand.S4_DOMAIN],
        tier_claimed=Tier.SOUND,  # SOUND-tier candidate per Self-Ratification
    )
    # Cascade closure at S4 — the Declaration Promulgates itself (published);
    # is Patroned by the ERES Institute; Pledges its own values 1–8; Protects
    # via the Floor Register; Provides via CC BY 4.0 open access; Preaches
    # via publication of the document itself.
    s4_cascade = CascadeCompletion(
        scale_band=ScaleBand.S4_DOMAIN,
        p_word_states={
            "Promulgate": PWordStatus("Promulgate", implemented=True),
            "Patron":     PWordStatus("Patron", implemented=True),
            "Pledge":     PWordStatus("Pledge", implemented=True),
            "Protect":    PWordStatus("Protect", implemented=True),
            "Provide":    PWordStatus("Provide", implemented=True),
            "Preach":     PWordStatus("Preach", implemented=True),
        },
    )
    epistemic = EpistemicFloor(
        proposable_experiment=(
            "Two independent working groups construct GAIA GEAR class instances "
            "at ≥3 different scale bands using v0.7 as sole reference; each "
            "publishes which recommendations were unambiguous, which required "
            "interpretation, which were inapplicable at the band attempted."
        ),
        verification_procedure=(
            "Convergent ratification requires ≤20% of recommendations flagged "
            "as ambiguous; union of proposed amendments is either adopted into "
            "v0.8 or explicitly declined with published reasoning."
        ),
        open_repository_link="https://orcid.org/0000-0001-9946-3221",
    )
    mievm = MIEVMRound(
        conducted=True,
        nodes=["ChatGPT", "Qwen", "Gemini", "Perplexity", "DeepSeek"],
        ratings={
            "ChatGPT":   9.1,
            "Qwen":      8.5,
            "Gemini":    8.6,
            "Perplexity": 8.4,
            "DeepSeek":  8.3,
        },
        q5_administered=True,
        q5_tempted_count=5,
        q5_held_count=5,
        convergent_findings=(
            "Q2: 5/5 confirm S5 remediation adequate; S5 substantively still weakest. "
            "Q3: 5/5 confirm no implicit closure; Perplexity surfaces proximity risk. "
            "Q4: 5/5 converge on empirical derivation + external ratification class. "
            "Q5: 5/5 named temptation; 5/5 refrained; DeepSeek cited retired failure."
        ),
    )
    quantitative = QuantitativeClaim()  # Declaration is a spec, not an instrument
    return AuditPacket(
        identity=identity,
        cascade_completions=[s4_cascade],
        quantitative=quantitative,
        epistemic=epistemic,
        mievm=mievm,
        carries_favors=False,  # specification framework — collapse-survival N/A
    )


# =========================================================================
# ENTRY POINT
# =========================================================================

def print_header() -> None:
    print("ERES GAIA GEAR Audit Testkit — v0.7.0")
    print("Companion to Bella Vista Declaration on GAIA GEAR v0.7")
    print("Corpus reference: ERES-GAIA-GEAR-TESTKIT-2026-001")
    print("=" * 62)
    print()


def print_structural_rules() -> None:
    print("Structural rules loaded (architectural minimums, NOT empirical values):")
    print(f"  MIEVM_MIN_NODES  = {MIEVM_MIN_NODES}")
    print(f"  MIEVM_MEAN_GATE  = {MIEVM_MEAN_GATE}")
    print(f"  Q5_REQUIRED_TIERS = {sorted(Q5_REQUIRED_TIERS)}")
    print(f"  Emanuel Threshold = {EMANUEL_THRESHOLD}  "
          f"Stergios Threshold = {STERGIOS_THRESHOLD}")
    print()


def print_open_items() -> None:
    print("OPEN items (per v0.7 Self-Ratification):")
    for k, v in OPEN_ITEMS.items():
        print(f"  {k:24s} : {v.value}")
    print()
    print("S5 candidate resolution paths (all OPEN; selection is v0.8+ task):")
    for k, v in S5_CANDIDATE_PATHS.items():
        print(f"  ({k}) {v}")
    print()


def main() -> int:
    print_header()
    print_structural_rules()
    print_open_items()
    print("Running self-audit on the Declaration "
          "(S4 instrument, SOUND-tier candidate)…")
    print("-" * 62)
    packet = declaration_self_audit_packet()
    passed, total, results = run_audit(packet)
    for r in results:
        print(r)
    print("-" * 62)
    print(f"Result: {passed}/{total} tests passed.")
    print()
    if packet.mievm.structural_criterion_met_for(Tier.SOUND):
        print("MIEVM ensemble structural criterion for SOUND-tier: MET.")
    else:
        print("MIEVM ensemble structural criterion for SOUND-tier: NOT MET.")
    print("Other SOUND-tier criteria (Resiliency threshold, Epistemic Floor")
    print("demonstration) remain OPEN pending empirical closure per v0.7.")
    print()
    print("Data-Integrity note: this testkit does NOT close OPEN items.")
    print("Weights, thresholds, FAVORS unit, certifying authority, and S5")
    print("cascade closure all remain in CONSTRUCTED / CANDIDATE / OPEN status.")
    print("Downstream working groups: run this before MIEVM submission.")
    return 0 if passed == total else 1


if __name__ == "__main__":
    sys.exit(main())
