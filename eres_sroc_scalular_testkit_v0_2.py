#!/usr/bin/env python3
"""
ERES-SROC-SCALULAR-TESTKIT-2026-001  v0.2 DRAFT
Test instrument for ERES-SROC-SCALULAR-2026-001 v0.3 DRAFT

This testkit is the executable companion to ERES-SROC-SCALULAR-2026-001 v0.3.
Read the specification first; this instrument tests its rules, not its
aspirations.

WHAT THIS TESTS
---------------
The SROC *specification's* adjudication rules, as executable checks:
  - Sec 1    Contact of Record (five elements; non-severable; dead channel voids;
             no portal/handle/URL as voice channel; channel change preserves the
             Sec 1.5 continuity date)
  - Sec 1.6  Custody of Answerability and the Erasure Boundary
             (ECR asymptotic, ECR in [0, 1); 1.0 refused)
  - Sec 2    CANDIDATE definition constraints
  - Sec 4    BUILD ORDER inheritance of answerability custody

WHAT THIS DOES NOT TEST
-----------------------
Whether an SROC closes S5. It cannot. S5 cascade closure is OPEN in the
governing Declaration (Bella Vista on GAIA GEAR v0.7) and this kit takes no
position on paths (a), (b), (c) or (e). Per Declaration Threat 9, naming a
fiduciary form is not closure -- and neither is testing one.

OPEN ITEMS APPEAR AS SKIPS, BY DESIGN
-------------------------------------
Two checks SKIP rather than pass:
  - Sec 5 amendment authority is unanswered   -> T11 skips
  - Sec 7 author-definition register is open  -> T12 skips
The suite goes fully green only when those close in the specification. A green
suite today would be a false signal, so the skips are load-bearing. This
version does NOT auto-flip those skips based on parsing the spec; the point of
a load-bearing skip is that it flips only when the human-readable specification
closes.

Dependencies: Python standard library only.
Run:  python3 eres_sroc_scalular_testkit.py
      python3 eres_sroc_scalular_testkit.py --demo
"""

from __future__ import annotations

import sys
from dataclasses import dataclass, field
from datetime import date
from typing import Any

VERSION = "v0.2 DRAFT"
INSTRUMENT = "ERES-SROC-SCALULAR-TESTKIT-2026-001"
TESTS_SPEC = "ERES-SROC-SCALULAR-2026-001 v0.3 DRAFT"
TESTS_SPEC_VERSION = (0, 3, "DRAFT")     # parseable, for future drift-guard
GOVERNING = "Bella Vista Declaration on GAIA GEAR v0.7"

# Sec 7 -- terms with no definition in the governing Declaration.
# SECUIR is partially anchored at spec v0.2/v0.3 (named subsystem, acronym open).
UNDEFINED_TERMS = ("SCALULAR", "SaleBuilders", "EarnedPath",
                   "Gunnysack", "VERTECA", "EFIL")
PARTIAL_TERMS = ("SECUIR",)

# Sec 1 -- required elements of a Contact of Record.
CONTACT_ELEMENTS = ("voice_channel", "answerable_party", "response_hours",
                    "languages", "max_response_interval", "escalation_path",
                    "continuity_date")

# Sec 1.6.3 -- the answerability record may contain ONLY these fields.
ANSWERABILITY_FIELDS = frozenset({"party", "role", "interval", "channel_state"})

# ---------------------------------------------------------------------------
# Traceability -- machine-readable map from test -> specification clause.
# The single source of truth for which rule each test exercises.
# Referenced by exception strings and printed in the runner footer.
# ---------------------------------------------------------------------------
TRACEABILITY = {
    "t01_contact_elements":              "Sec 1 (all seven elements required)",
    "t02_dead_channel_voids":            "Sec 1 (dead channel voids)",
    "t03_contact_non_severable":         "Sec 1 (non-severable)",
    "t04_incomplete_contact_voids":      "Sec 1 (partial contact voids)",
    "t05_subject_data_erasable":         "Sec 1.6.1",
    "t06_answerability_not_erasable":    "Sec 1.6.2",
    "t07_self_erasure_refused":          "Sec 1.6.2 (self-erasure attack)",
    "t08_answerability_field_separation":"Sec 1.6.3",
    "t09_ecr_asymptotic":                "Sec 1.6 / ECR in [0,1)",
    "t10_build_order_inherits_custody":  "Sec 1.6 downstream",
    "t11_amendment_authority":           "Sec 5 (OPEN)",
    "t12_author_definition_register":    "Sec 7 (OPEN)",
    "t13_scale_claim_honesty":           "Declaration scale-consistency 3",
    "t14_no_s5_closure_asserted":        "Anti-fabrication",
    "t15_channel_form_rejected":         "Sec 1 (no portal/URL/handle)",
    "t16_channel_change_preserves_date": "Sec 1 (Sec 1.5 continuity date)",
}


class SROCVoid(Exception):
    """Raised when an operation would void the contract under Sec 1 or Sec 1.6."""


# ---------------------------------------------------------------------------
# Reference implementation of the specification
# ---------------------------------------------------------------------------

def _looks_like_voice_channel(s: str) -> bool:
    """Sec 1 -- coarse check that a voice channel is not a URL, portal, email,
    or handle. Not a positive proof of reachability; catches the trivial
    failures the spec calls out ('may not be a form, a portal, an address,
    or an automated agent standing alone')."""
    if not isinstance(s, str) or not s.strip():
        return False
    lowered = s.lower()
    bad_tokens = ("://", "@", "mailto:", "www.", "http", "chatbot")
    return not any(tok in lowered for tok in bad_tokens)


@dataclass
class ContactOfRecord:
    voice_channel: str
    answerable_party: str
    response_hours: str
    languages: tuple
    max_response_interval: str
    escalation_path: str
    continuity_date: date
    live: bool = True
    human_answered: bool = True   # Sec 1: not an automated agent standing alone

    def missing_elements(self) -> list:
        """Sec 1 -- any of the five (seven, in the schema) elements missing
        by *presence* or by *emptiness* voids. Tightened v0.2: an empty
        string or empty tuple counts as missing, not just None."""
        missing = []
        for e in CONTACT_ELEMENTS:
            val = getattr(self, e, None)
            if val is None:
                missing.append(e)
            elif isinstance(val, (str, tuple, list)) and len(val) == 0:
                missing.append(e)
        return missing

    def channel_is_valid(self) -> bool:
        return (self.human_answered
                and _looks_like_voice_channel(self.voice_channel))

    def change_channel(self, new_channel: str, notice_sent: bool) -> None:
        """Sec 1 -- change of channel requires notice under Sec 5 and does
        NOT reset the Sec 1.5 continuity_date. Missing notice voids."""
        if not notice_sent:
            raise SROCVoid("Sec 1: channel change without Sec 5 notice")
        if not _looks_like_voice_channel(new_channel):
            raise SROCVoid("Sec 1: new channel is not a voice channel")
        self.voice_channel = new_channel
        # continuity_date deliberately preserved


@dataclass
class AnswerabilityRecord:
    """Sec 1.6.3 -- party, role, interval, channel state. Nothing else."""
    party: str
    role: str
    interval: str
    channel_state: str

    def fields(self) -> frozenset:
        return frozenset(self.__dict__.keys())


@dataclass
class SROC:
    identifier: str
    contact: ContactOfRecord | None
    scale_band_claimed: str
    subject_data: dict = field(default_factory=dict)
    answerability_log: list = field(default_factory=list)
    build_orders: list = field(default_factory=list)
    p_words_closed: set = field(default_factory=set)
    amendment_authority: Any = None          # Sec 5 -- OPEN
    ecr_reported: float | None = None

    # -- Sec 1 -------------------------------------------------------------
    def is_void(self) -> tuple:
        if self.contact is None:
            return True, "Sec 1: no Contact of Record (non-severable)"
        missing = self.contact.missing_elements()
        if missing:
            return True, f"Sec 1: incomplete Contact of Record: {', '.join(missing)}"
        if not self.contact.live:
            return True, "Sec 1: dead channel"
        if not self.contact.channel_is_valid():
            return True, "Sec 1: voice_channel is not a voice channel (portal/URL/handle/bot)"
        if not self.answerability_log:
            return True, "Sec 1.6: no custody record of answerability"
        return False, "conforming"

    # -- Sec 1.6 -----------------------------------------------------------
    def erase(self, target: str, requester: str) -> str:
        """Sec 1.6.1-1.6.4. Subject data erasable to the ECR limit; the
        answerability record is not, including at its own party's request."""
        if target == "answerability_log":
            raise SROCVoid(
                "Sec 1.6.2: custody record of answerability is not erasable "
                f"(requested by {requester})")
        if target in self.subject_data:
            del self.subject_data[target]
            return f"erased to ECR limit: {target}"
        return f"no such subject datum: {target}"

    def report_ecr(self, ratio: float) -> float:
        """Sec 1.6 / ERES-ECR-2026-001 -- ECR in [0, 1). 1.0 refused as a
        binary certificate; erasure is asymptotic, not binary."""
        if not 0.0 <= ratio < 1.0:
            raise SROCVoid(
                f"ECR must lie in [0.0, 1.0) -- erasure is asymptotic, not "
                f"binary; refused value {ratio}")
        self.ecr_reported = ratio
        return ratio


@dataclass
class BuildOrder:
    """Sec 1.6 downstream: inherits the issuing SROC's answerability custody."""
    identifier: str
    tier: str                     # s / S / $
    issuer: SROC
    inherited_custody: list = field(default_factory=list)

    def __post_init__(self):
        self.inherited_custody = list(self.issuer.answerability_log)

    def anonymize(self) -> None:
        raise SROCVoid(
            "Sec 1.6: a BUILD ORDER may not be erased into anonymity by its issuer")


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

def conforming_sroc() -> SROC:
    contact = ContactOfRecord(
        voice_channel="+1-000-000-0000 [placeholder -- author to supply]",
        answerable_party="[author to supply]",
        response_hours="09:00-17:00 CT, Mon-Fri",
        languages=("en",),
        max_response_interval="1 business day",
        escalation_path="named alternate, then written notice",
        continuity_date=date(2026, 7, 23),
        live=True,
        human_answered=True,
    )
    s = SROC(
        identifier="SROC-DEMO-001",
        contact=contact,
        scale_band_claimed="S1",
        subject_data={"biometric_sample": "...", "transaction_log": "..."},
        answerability_log=[AnswerabilityRecord(
            party="[author to supply]", role="Contact of Record",
            interval="2026-07-23 -> open", channel_state="live")],
        p_words_closed=set(),
    )
    return s


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

SKIP = "SKIP"


def t01_contact_elements():
    """Sec 1 -- all seven Contact of Record elements required."""
    s = conforming_sroc()
    void, why = s.is_void()
    return (not void, f"conforming SROC accepted ({why})")


def t02_dead_channel_voids():
    """Sec 1 -- a dead channel voids the contract, not merely defects it."""
    s = conforming_sroc()
    s.contact.live = False
    void, why = s.is_void()
    return (void and "dead channel" in why, why)


def t03_contact_non_severable():
    """Sec 1 -- removing the Contact of Record voids."""
    s = conforming_sroc()
    s.contact = None
    void, why = s.is_void()
    return (void and "non-severable" in why, why)


def t04_incomplete_contact_voids():
    """Sec 1 -- a partial Contact of Record is not a Contact of Record.
    Tightened v0.2 to catch empty-string and empty-tuple, not just None."""
    s = conforming_sroc()
    s.contact.escalation_path = ""      # empty string, not None
    void, why = s.is_void()
    if not (void and "escalation_path" in why):
        return (False, why)
    # secondary: empty tuple for languages
    s2 = conforming_sroc()
    s2.contact.languages = ()
    void2, why2 = s2.is_void()
    return (void2 and "languages" in why2, f"{why}; {why2}")


def t05_subject_data_erasable():
    """Sec 1.6.1 -- subject data erasable to the ECR limit."""
    s = conforming_sroc()
    before = len(s.subject_data)
    msg = s.erase("biometric_sample", requester="data subject")
    return (len(s.subject_data) == before - 1, msg)


def t06_answerability_not_erasable():
    """Sec 1.6.2 -- the custody record of answerability is not erasable."""
    s = conforming_sroc()
    try:
        s.erase("answerability_log", requester="third party")
        return (False, "erasure was permitted -- specification violated")
    except SROCVoid as exc:
        return (True, str(exc)[:72])


def t07_self_erasure_refused():
    """Sec 1.6.2 -- including at the request of the answerable party itself.
    This is the attack the rule exists to defeat."""
    s = conforming_sroc()
    party = s.contact.answerable_party
    try:
        s.erase("answerability_log", requester=party)
        return (False, "answerable party erased own custody record")
    except SROCVoid:
        return (True, "self-erasure by the answerable party refused")


def t08_answerability_field_separation():
    """Sec 1.6.3 -- the answerability record carries no subject data,
    which is what makes the two separable by construction."""
    rec = conforming_sroc().answerability_log[0]
    extra = rec.fields() - ANSWERABILITY_FIELDS
    return (not extra, f"fields {sorted(rec.fields())}"
                       + (f"; unexpected {sorted(extra)}" if extra else ""))


def t09_ecr_asymptotic():
    """Sec 1.6 / ERES-ECR-2026-001 -- erasure is asymptotic; ECR in [0,1)."""
    s = conforming_sroc()
    ok_val = s.report_ecr(0.9987)
    try:
        s.report_ecr(1.0)
        return (False, "binary erasure certificate accepted -- refused by spec")
    except SROCVoid:
        return (True, f"ratio {ok_val} accepted; 1.0 refused as binary")


def t10_build_order_inherits_custody():
    """Sec 1.6 downstream -- a BUILD ORDER inherits answerability custody
    and cannot be anonymized by its issuer."""
    s = conforming_sroc()
    bo = BuildOrder("BO-001", tier="S", issuer=s)
    inherited = len(bo.inherited_custody) == len(s.answerability_log)
    try:
        bo.anonymize()
        return (False, "BUILD ORDER anonymization permitted")
    except SROCVoid:
        return (inherited, f"inherited {len(bo.inherited_custody)} record(s); "
                           "anonymization refused")


def t11_amendment_authority():
    """Sec 5 -- OPEN. Whoever may deploy, amend, pause or key the SROC is the
    actual S5 Patron. Unanswered in the specification, so this cannot pass."""
    s = conforming_sroc()
    if s.amendment_authority is None:
        return (SKIP, "Sec 5 unanswered -- path (e) stands or falls here; "
                      "close in the spec, not in the fixture")
    return (True, f"amendment authority: {s.amendment_authority}")


def t12_author_definition_register():
    """Sec 7 -- OPEN. Six chain terms carry no definition in the governing
    Declaration; one is partially anchored."""
    if UNDEFINED_TERMS:
        return (SKIP, f"{len(UNDEFINED_TERMS)} undefined, "
                      f"{len(PARTIAL_TERMS)} partial: "
                      f"{', '.join(UNDEFINED_TERMS)}; close upstream, "
                      "not in this kit")
    return (True, "all chain terms anchored")


def t13_scale_claim_honesty():
    """Declaration scale-consistency rule 3 -- do not claim a band the cascade
    does not reach. The demo claims S1 and closes no P-words, so it must not
    be representable as closing S1."""
    s = conforming_sroc()
    six = {"Promulgate", "Patron", "Pledge", "Protect", "Provide", "Preach"}
    closed = s.p_words_closed >= six
    claim_ok = not closed  # demo asserts no closure, correctly
    return (claim_ok, f"claims {s.scale_band_claimed}; "
                      f"P-words closed {len(s.p_words_closed)}/6 -- "
                      "no closure asserted")


def t14_no_s5_closure_asserted():
    """Anti-fabrication -- this kit must not encode an S5 closure."""
    s = conforming_sroc()
    return (s.scale_band_claimed != "S5",
            "no fixture claims S5; S5 remains OPEN in the Declaration")


def t15_channel_form_rejected():
    """Sec 1 -- the voice channel may not be a form, a portal, an address, or
    an automated agent standing alone. Added v0.2."""
    cases = [
        ("https://example.com/contact", "URL"),
        ("support@example.com",         "email address"),
        ("chatbot://helpdesk",          "chatbot handle"),
        ("www.example.com/help",        "portal URL"),
    ]
    failures = []
    for chan, kind in cases:
        s = conforming_sroc()
        s.contact.voice_channel = chan
        void, why = s.is_void()
        if not (void and "voice_channel" in why):
            failures.append(f"{kind} accepted")
    if failures:
        return (False, "; ".join(failures))
    # and: a live human channel with human_answered=False also voids
    s2 = conforming_sroc()
    s2.contact.human_answered = False
    void2, why2 = s2.is_void()
    return (void2 and "voice_channel" in why2,
            f"URL/email/handle/portal/bot-flagged all void: {why2}")


def t16_channel_change_preserves_date():
    """Sec 1 / Sec 1.5 -- change of channel requires notice and does not
    reset the continuity_date. Added v0.2."""
    s = conforming_sroc()
    original = s.contact.continuity_date
    # 1. no notice -> voids
    try:
        s.contact.change_channel("+1-555-000-1111", notice_sent=False)
        return (False, "channel change without notice was accepted")
    except SROCVoid:
        pass
    # 2. with notice -> succeeds; date preserved
    s.contact.change_channel("+1-555-000-1111", notice_sent=True)
    if s.contact.continuity_date != original:
        return (False, f"continuity_date changed: {original} -> "
                       f"{s.contact.continuity_date}")
    return (True, f"channel updated with notice; continuity_date preserved "
                  f"({original.isoformat()})")


TESTS = (t01_contact_elements, t02_dead_channel_voids, t03_contact_non_severable,
         t04_incomplete_contact_voids, t05_subject_data_erasable,
         t06_answerability_not_erasable, t07_self_erasure_refused,
         t08_answerability_field_separation, t09_ecr_asymptotic,
         t10_build_order_inherits_custody, t11_amendment_authority,
         t12_author_definition_register, t13_scale_claim_honesty,
         t14_no_s5_closure_asserted,
         t15_channel_form_rejected, t16_channel_change_preserves_date)


# ---------------------------------------------------------------------------
# Runner
# ---------------------------------------------------------------------------

def demo() -> None:
    print("-" * 74)
    print("WORKED EXAMPLE -- one SROC, three operations")
    print("-" * 74)
    s = conforming_sroc()
    void, why = s.is_void()
    print(f"1. conformance check           : {'VOID' if void else 'OK'} ({why})")
    print(f"2. erase subject datum         : {s.erase('transaction_log', 'subject')}")
    try:
        s.erase("answerability_log", requester=s.contact.answerable_party)
    except SROCVoid as exc:
        print(f"3. erase own custody record    : REFUSED -- {exc}")
    print(f"4. ECR reported                : {s.report_ecr(0.9987)}")
    bo = BuildOrder("BO-001", tier="$", issuer=s)
    print(f"5. BUILD ORDER {bo.identifier} (tier {bo.tier}) inherits "
          f"{len(bo.inherited_custody)} custody record(s)")
    print()


def print_traceability() -> None:
    print("TRACEABILITY -- test to specification clause")
    print("-" * 74)
    for name, clause in TRACEABILITY.items():
        short = name.split("_", 1)[0]  # tNN
        print(f"  {short:<5}  {clause}")
    print()


def run() -> int:
    print("=" * 74)
    print(f"{INSTRUMENT}  {VERSION}")
    print(f"tests: {TESTS_SPEC}")
    print(f"under: {GOVERNING}")
    print("=" * 74)

    passed = failed = skipped = 0
    for fn in TESTS:
        ok, detail = fn()
        if ok is SKIP:
            tag, skipped = "SKIP", skipped + 1
        elif ok:
            tag, passed = "PASS", passed + 1
        else:
            tag, failed = "FAIL", failed + 1
        name = fn.__name__.split("_", 1)[1].replace("_", " ")
        print(f"[{tag}] {name:<34} {detail}")

    print("-" * 74)
    print(f"{passed} pass · {failed} fail · {skipped} skip "
          f"(of {len(TESTS)})")
    print()
    print_traceability()
    print("SCOPE: these tests exercise the specification's rules, not the")
    print("world. Passing does NOT establish that an SROC exists, has been")
    print("deployed, or closes any cascade band. S5 remains OPEN and no path")
    print("among (a), (b), (c), (e) is selected here.")
    print()
    print("The two skips are load-bearing: Sec 5 amendment authority and the")
    print("Sec 7 definition register. The suite goes fully green only when")
    print("those close in the specification -- not before.")
    print("=" * 74)
    return 1 if failed else 0


# ---------------------------------------------------------------------------
# Change Log
# ---------------------------------------------------------------------------
# 2026-07-23  v0.2 DRAFT   Tracks spec v0.3. Added TRACEABILITY dict (single
#                          source of truth for test -> clause mapping, printed
#                          in runner footer). Added t15 (voice_channel may not
#                          be a form/portal/URL/handle/bot -- Sec 1) and t16
#                          (channel change requires notice and preserves the
#                          Sec 1.5 continuity_date). Tightened
#                          missing_elements() to reject empty strings and
#                          empty tuples, not just None. Added
#                          TESTS_SPEC_VERSION as a parseable tuple to guard
#                          against future version drift. Cross-reference to
#                          spec added in module docstring. Load-bearing SKIPs
#                          for Sec 5 and Sec 7 preserved -- deliberately NOT
#                          auto-flipped based on parsing the spec.
# 2026-07-23  v0.1 DRAFT   Initial test kit for spec v0.2. Sec 1 elements,
#                          Sec 1.6 erasure asymmetry, ECR asymptote, BUILD
#                          ORDER inheritance, anti-fabrication for S5.


if __name__ == "__main__":
    if "--demo" in sys.argv:
        demo()
    sys.exit(run())
