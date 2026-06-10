# ERES-CREDIT — Credit Division Under the Gate/Rating Split
## Reference & Maintenance Specification

| | |
|---|---|
| **Instrument ID** | ERES-CREDIT-2026-001 |
| **Spec version** | Credit Spec v0.1 (DRAFT) |
| **Reference implementation** | `credit_split.py` v0.1 |
| **Companion instruments** | BERA (`bera_rate.py`, ERES-BERA-2026-001) · EAAP (`eaap_proof.py`) |
| **License** | CCAL v2.1 (CARE Commons Attribution License) |
| **Author / Lock authority** | Joseph Allen Sprute, ERES Institute for New Age Cybernetics — ORCID 0000-0001-9946-3221 |
| **Method** | H2C2H · MIEVM |
| **Status** | DRAFT for MIEVM audit. **The weight vector is OPEN.** Not deposited. Not load-bearing for any payout decision. |

> **The asset, stated plainly.** Dividing credit fairly is the mechanism that lets contribution become an asset others will tend rather than fight over. This instrument supplies the *structure* of that division — a vector, a held-state for the unverifiable, an authorization step, an auditable ledger. It deliberately does **not** supply the *valuation* (how much each kind of contribution is worth). That single number is a human lock, not a derivation, and it is the headline OPEN item below.

> **How to read this document.**
> - **To *apply* it:** read §1 (the split), §3 (the dimensions), §4 (the worked example).
> - **To *understand* it:** add §2 (pipeline) and §5 (determinism).
> - **To *maintain or extend* it:** §6 (lock status) and §7 (the maintenance contract) are what keep it fair over time. Do not change §7 without the lock authority.

---

## 1. The axiom: measuring credit and awarding it are different functions

This is the same wall BERA puts between rating and gate, applied to credit.

- **Measuring a contribution is a RATING** — the **CREDIT vector** (§3): continuous, multi-dimensional, "how much resonance did this add." Tuning-tier commentary.
- **Awarding credit is a GATE** — a bounded decision (`BIND` / `REFUSE` / `VEILED`) about whether an attribution, share, or payout is recognized. Auditable.

Two prohibitions follow, and they are exactly the two failure modes that wreck credit systems:

1. **A contribution measure must never silently become a reward.** There is always a named, bounded authorization step between "you did good work" and "you receive X."
2. **A credit decision must never be derived by thresholding a scalar-collapsed contribution.** This is the h-index trap, the citation-count trap, the single "impact score" trap. Credit is a **vector**; averaging it into one figure destroys the structure that makes the division defensible.

The reference implementation enforces both by construction: the CREDIT vector is never collapsed unless a **locked** weight vector exists, and no award is reachable except through the gate.

---

## 2. The pipeline at a glance

```
 attested contributions            (per contributor, per dimension; magnitudes
            │                       are INPUTS confirmed at intake, not derived)
            ▼
   CREDIT vector  ⟨ ORIG · IMPL · AUDIT · LOCK · BRIDGE · STEW · C7 ⟩   7-D
            │
            ├──► per-dimension shares      ── integer largest-remainder,
            │    (normalize ONE column)       deterministic, Σ = 1000 milli   ✅ allowed
            │
            ├──► cross-dimension total     ── requires LOCKED weight vector
            │    (collapse the vector)        otherwise REFUSED                ⛔ gated
            │
            ▼
   AWARD GATE   A · V · D · L   (Kleene 3-valued)  →  BIND / REFUSE / VEILED
            │                                            │
            │                                            └─ correct REFUSE accrues
            ▼                                               merit to the verifier
   credit receipt  (content-addressed, hash-chained, tamper-evident, replayable)
```

A contribution that cannot be verified is held **VEILED-C** — never given a fabricated value.

---

## 3. The CREDIT vector (the eggs)

Per contributor, a seven-dimensional vector. Six named dimensions plus a reserved seventh (C7) held VEILED-C, mirroring BERA's RATE. **Magnitudes per dimension are inputs** — attested at intake by the contribution record — not invented by this instrument.

| Dim | Name | Credits | Status |
|---|---|---|---|
| **ORIG** | Origination | a novel construct or canonical form created | working |
| **IMPL** | Implementation | an executable realization | working |
| **AUDIT** | Audit | a fault found or corrected (the merit-for-refusal dimension) | working |
| **LOCK** | Canonical lock | an authority confirming a canonical form (a lock-authority act) | working |
| **BRIDGE** | Domain bridge | a cross-domain hypothesis or insight | working |
| **STEW** | Stewardship | maintenance, documentation, making it usable by others | working |
| **C7** | reserved | structural slot, held **VEILED-C** | dimension map OPEN |

> The named set is a *working* taxonomy. Adding, renaming, or splitting a dimension is a lock-authority action (it changes the dimension map, §6), and must preserve no-collapse and VEILED-C discipline.

### 3.1 Per-dimension shares *(computable, deterministic)*

Within a single dimension, shares are the contributors' magnitudes normalized to milli-units summing to exactly 1000, by **integer largest-remainder apportionment** with ties broken by contributor name. Normalizing one column is *not* a collapse of the vector, so this is permitted and fully deterministic.

```
share_i(d) = floor( units_i(d) · 1000 / Σ units(d) ) , then largest remainders
             receive +1 until the column sums to exactly 1000
```

A contributor **VEILED-C in that dimension is held out of the denominator** — their share is VEILED-C, and they neither receive a fabricated share nor dilute the resolved contributors.

### 3.2 Cross-dimension total *(refused without a LOCKED weight vector)*

Converting a contributor's whole vector to one number requires a weight vector **w_credit** across the dimensions. That weight vector is **OPEN** (the headline lock item). The implementation:

- **No locked weights** → the collapse is **REFUSED** (a `PermissionError`, by design).
- **Provisional weights supplied** → returns a result explicitly tagged **`PROVISIONAL-PREVIEW (not for citation; weights OPEN)`** — usable for internal tuning, never authoritative.
- **Locked weights** → returns an **`AUTHORITATIVE`** total.

This is the same discipline as ARI/ERI/RCI in BERA: the structure runs today; the canonical valuation waits for the lock authority.

### 3.3 VEILED-C — the held state for unresolvable credit

A contribution whose contributor or provenance cannot be verified is held **VEILED-C**: never coerced to a number, never given a share, never used to dilute others. This generalizes the attribution discipline already in practice (an unconfirmable party cited as a correspondent, not assigned a fictional stake) and echoes CyberRAVE — *Cybernetic Ratings Abolishing Veiled Exchanges*. When the evidence resolves, the dimension can be un-veiled — but only through the gate and the lock authority, never silently.

---

## 4. Worked end-to-end example

From the reference implementation's own run. Contributors are **roles** that map to named parties via attestation.

**CREDIT vectors (inputs):**

| contributor | ORIG | IMPL | AUDIT | LOCK | BRIDGE | STEW | C7 |
|---|---|---|---|---|---|---|---|
| originator | 100 | 10 | 0 | 0 | 30 | 20 | VEILED-C |
| implementer | 5 | 80 | 40 | 0 | 0 | 25 | VEILED-C |
| auditor | 0 | 10 | 60 | 0 | 0 | 10 | VEILED-C |
| lock-authority | 0 | 0 | 0 | 100 | 0 | 5 | VEILED-C |
| unverified-correspondent | 0 | 0 | 0 | 0 | **VEILED-C** | 0 | VEILED-C |

**Per-dimension shares (milli, Σ = 1000):**

| dimension | shares |
|---|---|
| ORIG | originator 952 · implementer 48 |
| IMPL | originator 100 · implementer 800 · auditor 100 |
| AUDIT | implementer 400 · auditor 600 |
| LOCK | lock-authority 1000 |
| BRIDGE | originator 1000 · *unverified-correspondent VEILED-C* |
| STEW | originator 333 · implementer 417 · auditor 167 · lock-authority 83 |

Note BRIDGE: the unverified correspondent is **held VEILED-C** and the originator still receives the full resolved share — the veiled party does not dilute the resolved one.

**Cross-dimension collapse:**

- authoritative total → **REFUSED** (weight vector OPEN)
- provisional preview with illustrative weights → `370` `[PROVISIONAL-PREVIEW (not for citation; weights OPEN)]`

**Award gate (A · V · D · L):**

| case | A | V | D | L | decision |
|---|---|---|---|---|---|
| clean award | TRUE | TRUE | TRUE | TRUE | **BIND** |
| self-award | TRUE | TRUE | **FALSE** | TRUE | REFUSE |
| unverifiable provenance | TRUE | **UNKNOWN** | TRUE | TRUE | VEILED |
| no lock sign-off | TRUE | TRUE | TRUE | **UNKNOWN** | VEILED |
| forged attestation | **FALSE** | TRUE | TRUE | TRUE | REFUSE |

Only the clean award reaches an actual award. The two correct REFUSEs accrue **merit 0.5 each** to the verifier — catching a bad claim is itself credited. The full ledger is hash-chained: flipping a recorded REFUSE to BIND is detected at the exact index, and replaying the same claims reproduces the chain head byte-for-byte.

---

## 5. Determinism

Credit records must be reproducible by any party from the same inputs.

- **Per-dimension apportionment** is integer largest-remainder with a deterministic tie-break (largest fractional part, then contributor name). No floating-point; shares sum to exactly 1000 on every platform.
- **Receipts** are content-addressed SHA-256 over a canonical (sorted-key) JSON encoding and hash-chained by `prev_receipt_id`. Replay of the same claim sequence reproduces every receipt id and the chain head.
- **The full 7-D vector is recorded in each receipt** — never a scalar.

---

## 6. Lock status — what is settled, what is open

| Item | Status | Authority |
|---|---|---|
| Gate/rating split + two prohibitions (§1) | **LOCKED** | canonical axiom |
| CREDIT = 7-D vector; scalar collapse prohibited without locked weights | **LOCKED** | canonical |
| VEILED-C held-state discipline (§3.3) | **LOCKED** | canonical |
| Distinctness / no self-award (gate factor D; mirrors BERA Gate A) | **LOCKED** | canonical |
| Merit-for-refusal (correct REFUSE accrues to verifier) | **LOCKED** | canonical |
| Per-dimension apportionment = integer largest-remainder | **LOCKED** (v0.1 impl) | JAS |
| Hash-chained, replayable credit receipts | **LOCKED** (v0.1 impl) | JAS |
| **Weight vector `w_credit` (cross-dimension valuation)** | **OPEN — the headline lock item** | **JAS** |
| Named dimension set (ORIG/IMPL/AUDIT/LOCK/BRIDGE/STEW) | **OPEN — working taxonomy** | JAS |
| Formal C1…C7 dimension map | **OPEN** | JAS |
| Refusal-credit magnitude (currently 0.5) | **OPEN** | JAS |
| Intake rule for contribution magnitudes (who attests, how) | **OPEN** | JAS |

> **The headline OPEN item is the weight vector.** Until JAS locks `w_credit`, the instrument refuses to produce an authoritative cross-dimension total. This is intentional: the moment credit becomes money, people optimize for whatever dimensions you weight, so the weighting is an incentive design — a governance decision the lock authority must own and defend, not a number the math hands you.

---

## 7. The maintenance contract — how the division stays fair

Changing any of these is a **lock-authority action**, not a maintainer action. A reviewer should reject a pull request that violates any of them.

- **CI1 — Split.** A CREDIT measure never authorizes an award. An award never derives from a thresholded, scalar-collapsed credit.
- **CI2 — No collapse without a lock.** A cross-dimension total is REFUSED unless `w_credit` is LOCKED. Provisional previews are tagged non-authoritative and are not citable.
- **CI3 — VEILED-C discipline.** Unresolvable credit is held VEILED-C: never numbered, never given a share, never used to dilute resolved contributors. Un-veiling happens only through the gate and the lock authority.
- **CI4 — Distinctness.** No self-award: a contributor may not be the awarding authority for their own credit.
- **CI5 — Determinism.** Apportionment is integer largest-remainder with a fixed tie-break; replay of the same claims reproduces the chain head byte-for-byte.
- **CI6 — Merit-for-refusal.** A correct REFUSE accrues to the verifier; audit and review are first-class credited acts, not unpaid overhead.
- **CI7 — Ledger integrity.** Every award decision emits a hash-chained receipt recording the full 7-D vector. No receipt stores a single "credit score."
- **CI8 — Provisional ≠ canonical.** The weight vector, the dimension taxonomy, and any preview total are not citable until JAS lock.

**Safe extension path.** The instrument separates what is open from what is locked so the open parts can change without touching the load-bearing core:
- Adjusting the dimension taxonomy or the intake rule affects only the front-end; the split, VEILED-C, gate, and ledger are untouched.
- Locking the weight vector is a JAS action: confirm `w_credit`, move its row in §6 from OPEN to LOCKED, set `CreditWeights.LOCKED`, and only then are authoritative cross-dimension totals citable.
- Every change should be replay-verified and, ideally, fuzz-checked against CI1–CI7 before merge.

---

## 8. Position in the ERES instrument stack

1. **Deterministic reference implementation (EAAP gate)** — legally load-bearing (Daubert-relevant).
2. **MIEVM-LLM ensemble** — governance commentary only.
3. **BERA / ERES-CREDIT** — governance tuning only. CREDIT describes and apportions; it does not, by itself, move money or confer authority. The award gate records a recognized award; any consequence-bearing transfer flows through tier 1 discipline.

Any claim placing ERES-CREDIT in a load-bearing payout role without a locked weight vector and a named authorization step is out of specification.

---

*Three Governing Principles (operationally binding): Don't hurt yourself. Don't hurt others. Build for generations to come.*

*ERES-CREDIT — Credit Division Under the Gate/Rating Split · ERES-CREDIT-2026-001 · CCAL v2.1*
