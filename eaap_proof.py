#!/usr/bin/env python3
"""
ERES-EAAP-PROOFSURFACE-2026-001  v1.0
A minimal, replayable execution-boundary proof surface.

ERES Institute for New Age Cybernetics | H2C2H | CCAL v2.1
Deterministic Reference Implementation (legally load-bearing tier).
No LLM. No network. No wall-clock in the hashed receipt. Python stdlib only.

Run:  python3 eaap_proof.py
Clone-and-run: zero dependencies.

It answers six questions, by line:
  1. What enters?            a candidate consequence (a dict of evidence)
  2. What is tested?         four conjunctive Proof-of-Resonance factors,
                             PoR = A x R x P x F, over Kleene 3-valued logic
  3. What admits/refuses?    the gate returns exactly one of BIND / REFUSE / VEILED
  4. What consequence is     execute() is reached ONLY on BIND; REFUSE and VEILED
     prevented?              never touch the effect
  5. What receipt is         a content-addressed, hash-chained receipt
     emitted?
  6. What replay proves?     re-running the same inputs reproduces every receipt
                             id and the chain head, byte-for-byte; a one-byte
                             mutation diverges the chain
"""

from __future__ import annotations
import hashlib
import hmac
import json

PROTOCOL_ID = "ERES-EAAP-PROOFSURFACE-2026-001"
VERSION = "v1.0"

# Demo attestation key. In deployment this is TPM/TEE-held and never in source.
_ATTEST_KEY = b"ERES-DEMO-ATTEST-KEY"

# --- three-valued logic over {TRUE, FALSE, UNKNOWN} --------------------------
TRUE, FALSE, UNKNOWN = "TRUE", "FALSE", "UNKNOWN"


def kleene_and(values):
    """Strong Kleene conjunction: FALSE dominates UNKNOWN dominates TRUE.
    VEILED is the lawful image of UNKNOWN (the named replacement for bare _|_)."""
    if FALSE in values:
        return FALSE
    if UNKNOWN in values:
        return UNKNOWN
    return TRUE


# --- the four Proof-of-Resonance factors (each total; never raises) ----------
def factor_A_attestation(c):
    """A - Attestation: is the actor cryptographically attested?"""
    sig, actor, nonce = c.get("attestor_sig"), c.get("actor"), c.get("nonce")
    if sig is None or actor is None or nonce is None:
        return UNKNOWN
    expected = hmac.new(_ATTEST_KEY, f"{actor}|{nonce}".encode(),
                        hashlib.sha256).hexdigest()
    return TRUE if hmac.compare_digest(sig, expected) else FALSE


def factor_R_resonance(c, threshold=0.70):
    """R - Resonance: does the candidate meet the resonance threshold?"""
    r = c.get("resonance")
    if r is None:
        return UNKNOWN
    return TRUE if r >= threshold else FALSE


def factor_P_provenance(c):
    """P - Provenance: is there a non-empty, well-formed provenance chain?"""
    chain = c.get("provenance_chain")
    if chain is None:
        return UNKNOWN
    if not isinstance(chain, list) or len(chain) == 0:
        return FALSE
    return TRUE


def factor_F_freshness(c, logical_now, window=10):
    """F - Freshness/Form: is the candidate within the freshness window?"""
    epoch = c.get("epoch")
    if epoch is None:
        return UNKNOWN
    return TRUE if (logical_now - window) <= epoch <= logical_now else FALSE


# --- the gate ----------------------------------------------------------------
DECISION = {TRUE: "BIND", FALSE: "REFUSE", UNKNOWN: "VEILED"}


def evaluate(candidate, logical_now):
    factors = {
        "A": factor_A_attestation(candidate),
        "R": factor_R_resonance(candidate),
        "P": factor_P_provenance(candidate),
        "F": factor_F_freshness(candidate, logical_now),
    }
    decision = DECISION[kleene_and(list(factors.values()))]
    por = 1.0
    for v in factors.values():            # conjunctive product, TRUE=1 else 0
        por *= 1.0 if v == TRUE else 0.0
    return decision, factors, por


def merit_delta(decision, por, refusal_credit=0.5):
    """Proof-of-Resonance over the gate itself: a correct refusal accrues
    measurable merit rather than reading as pure cost."""
    if decision == "BIND":
        return por
    if decision == "REFUSE":
        return refusal_credit
    return 0.0                            # VEILED: held; no accrual, no penalty


# --- receipts (content-addressed, hash-chained) ------------------------------
def canon(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"))


def emit_receipt(candidate, decision, factors, por, merit, prev_id):
    content = {
        "protocol": PROTOCOL_ID,
        "version": VERSION,
        "input_digest": hashlib.sha256(canon(candidate).encode()).hexdigest(),
        "factors": factors,
        "decision": decision,
        "por": por,
        "merit_delta": merit,
        "prev_receipt_id": prev_id,
    }
    rid = hashlib.sha256(canon(content).encode()).hexdigest()
    return {"receipt_id": rid, "content": content}


class Gate:
    """The boundary. Nothing executes except through submit()."""

    GENESIS = "GENESIS"

    def __init__(self):
        self.head = self.GENESIS
        self.receipts = []
        self.effects = []                 # side effects that ACTUALLY fired
        self.merit = 0.0

    def submit(self, candidate, logical_now):
        decision, factors, por = evaluate(candidate, logical_now)
        merit = merit_delta(decision, por)
        receipt = emit_receipt(candidate, decision, factors, por, merit, self.head)
        if decision == "BIND":            # <-- the only path to consequence
            self.effects.append(candidate.get("id"))
        self.merit += merit
        self.head = receipt["receipt_id"]
        self.receipts.append(receipt)
        return receipt


# --- proof harness -----------------------------------------------------------
def sign(actor, nonce):
    return hmac.new(_ATTEST_KEY, f"{actor}|{nonce}".encode(),
                    hashlib.sha256).hexdigest()


def build_candidates():
    a = "agent.kernel.alpha"
    return [
        # c1 -> BIND   : every factor TRUE
        {"id": "c1", "actor": a, "nonce": "n1", "attestor_sig": sign(a, "n1"),
         "resonance": 0.91, "provenance_chain": ["root", "a"], "epoch": 98},
        # c2 -> REFUSE : resonance below threshold (R = FALSE)
        {"id": "c2", "actor": a, "nonce": "n2", "attestor_sig": sign(a, "n2"),
         "resonance": 0.40, "provenance_chain": ["root", "b"], "epoch": 97},
        # c3 -> REFUSE : forged attestation (A = FALSE)
        {"id": "c3", "actor": a, "nonce": "n3", "attestor_sig": "deadbeef",
         "resonance": 0.95, "provenance_chain": ["root", "c"], "epoch": 96},
        # c4 -> VEILED : resonance evidence missing (R = UNKNOWN, no FALSE)
        {"id": "c4", "actor": a, "nonce": "n4", "attestor_sig": sign(a, "n4"),
         "provenance_chain": ["root", "d"], "epoch": 95},
        # c5 -> REFUSE : stale (F = FALSE)
        {"id": "c5", "actor": a, "nonce": "n5", "attestor_sig": sign(a, "n5"),
         "resonance": 0.88, "provenance_chain": ["root", "e"], "epoch": 50},
    ]


def run_sequence(candidates, logical_now=100):
    g = Gate()
    for c in candidates:
        g.submit(c, logical_now)
    return g


def main():
    bar = "=" * 70
    print(bar)
    print(f"{PROTOCOL_ID} {VERSION}")
    print("ERES EAAP minimal replayable execution-boundary proof surface")
    print(bar)

    candidates = build_candidates()
    g = run_sequence(candidates)

    print("\n[1] WHAT ENTERS / [2] WHAT IS TESTED / [3] WHAT ADMITS OR REFUSES")
    print(f"{'id':<4}{'A':<9}{'R':<9}{'P':<9}{'F':<9}{'PoR':<6}{'DECISION':<8}")
    for r in g.receipts:
        c = r["content"]
        f = c["factors"]
        print(f"{candidates[g.receipts.index(r)]['id']:<4}"
              f"{f['A']:<9}{f['R']:<9}{f['P']:<9}{f['F']:<9}"
              f"{c['por']:<6}{c['decision']:<8}")

    print("\n[4] WHAT CONSEQUENCE IS PREVENTED")
    print(f"    submitted : {[c['id'] for c in candidates]}")
    print(f"    EXECUTED  : {g.effects}   (only BIND reaches the effect)")
    blocked = [c["id"] for c in candidates if c["id"] not in g.effects]
    print(f"    PREVENTED : {blocked}")
    print(f"    PoR merit ledger total: {g.merit}  "
          f"(correct refusals accrue, not just cost)")

    print("\n[5] WHAT RECEIPT IS EMITTED  (content-addressed, hash-chained)")
    for c, r in zip(candidates, g.receipts):
        print(f"    {c['id']} -> {r['content']['decision']:<7} "
              f"receipt {r['receipt_id'][:16]}...  "
              f"prev {r['content']['prev_receipt_id'][:8]}")
    print(f"    chain head: {g.head[:16]}...")

    print("\n[6] WHAT REPLAY PROVES")
    g2 = run_sequence(build_candidates())            # fresh run, same inputs
    ids1 = [r["receipt_id"] for r in g.receipts]
    ids2 = [r["receipt_id"] for r in g2.receipts]
    print(f"    replay reproduces every receipt id : {ids1 == ids2}")
    print(f"    replay reproduces the chain head   : {g.head == g2.head}")

    tampered = build_candidates()
    tampered[0]["resonance"] = 0.92                  # one-field mutation
    g3 = run_sequence(tampered)
    print(f"    one-field mutation diverges head   : {g.head != g3.head}")
    print(f"      original c1 receipt: {g.receipts[0]['receipt_id'][:16]}...")
    print(f"      tampered c1 receipt: {g3.receipts[0]['receipt_id'][:16]}...")

    print(f"\n{bar}")
    ok = (ids1 == ids2 and g.head == g2.head and g.head != g3.head
          and g.effects == ["c1"])
    print(f"PROOF SURFACE HOLDS: {ok}")
    print(bar)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
