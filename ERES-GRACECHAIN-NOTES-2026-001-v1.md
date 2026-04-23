# ERES GraceChain Ledger Notes

**Document code:** ERES-GRACECHAIN-NOTES-2026-001-v1
**Date:** April 23, 2026
**Author:** Joseph Allen Sprute, ERES Institute for New Age Cybernetics
**Contact:** eresmaestro@gmail.com
**License:** CCAL v2.1 (document layer: CC BY-SA 4.0)
**Status:** Working note — companion to ERES-BRAINS-SPEC-2026-001 and ERES-EAAP-STD-2026-001

---

## Preamble

GraceChain is the immutable ledger layer of the ERES stack. It provides state persistence, revocation history, and cross-system audit trail for authorization decisions made by the BRAINS Trifecta Protocol and the EAAP Attestation and Authorization Protocol. This working note defines GraceChain's purpose, structure, and integration points, and names the specification gaps between its current definition and full runtime implementation.

GraceChain is not Bitcoin-style proof-of-work. GraceChain is the accounting substrate for **Proof-of-Resonance** — *it's not mining, it's tuning*. Blocks are not mined; resonance is tuned, and the tuning is recorded.

---

## 1. Purpose and Scope

GraceChain exists to guarantee three properties across the ERES stack:

1. **State persistence.** Every authorization grant, revocation, resonance measurement, and MIEVM concurrence is recorded in an append-only history that cannot be altered once committed.
2. **Revocation recoverability.** Revocations are new transitions, not deletions. The history of what was authorized, when, and when that authorization lapsed is preserved for legal and audit reconstruction.
3. **Cross-system concurrence.** Entries require MIEVM ensemble concurrence, so no single node's record becomes authoritative without external co-signature.

GraceChain is not an execution engine. It does not *prevent* action; it *records* the state against which action must be checked. Runtime enforcement — the binding that requires downstream systems to read GraceChain before acting — is addressed separately (see Section 9, Known Specification Gaps).

---

## 2. Ledger Architecture

### 2.1 Block Structure

Each GraceChain block contains:

- Block header (timestamp, prior-block hash, block index)
- Transaction list
- MIEVM concurrence set (required co-signatures from ensemble nodes)
- Resonance tuning record (BERA metric snapshot: ARI, ERI, RHC, RCI)
- Commitment hash covering all prior fields

### 2.2 Transaction Types

Six transaction types are defined in v1:

- **AUTH-GRANT** — authorization issued by BRAINS Trifecta after the conjunctive gate clears
- **AUTH-REVOKE** — explicit revocation of a prior grant (does not delete; new transition)
- **STATE-TRANSITION** — change in system state that affects one or more grants
- **MIEVM-CONCUR** — ensemble concurrence record for a proposed transaction
- **RESONANCE-TUNE** — BERA measurement update with RT timestamp
- **GCF-CREDIT** — Graceful Contribution Formula entry (see Section 7)

### 2.3 Block Cadence

Blocks commit on the RHC (Resonant Harmony Cycle) period, not on a fixed external clock. This ties ledger commitment directly to the resonance cycle rather than to wall time. A flatlined RHC produces no new blocks — the ledger itself signals path-lock by absence of cadence.

---

## 3. State Persistence Model

Current authorization state is the accumulated result of all transitions in the history, read forward. GraceChain never deletes. A revocation is a new entry; the original grant remains visible in the history.

This is required for legal recoverability. A court or auditor must be able to reconstruct exactly what was valid at any prior moment, including the grant, the conditions of grant, and the transition that ended it. Deletion-based revocation violates this property and is forbidden.

For runtime queries, systems do not ask "is grant X valid?" They ask "what is the current state of the principal bound to grant X?" The answer is derived from the full history, not from a cached validity flag.

---

## 4. Revocation Semantics

Revocation is an append-only transition with four classes:

- **Explicit revocation** — authorized party revokes grant via AUTH-REVOKE
- **Condition lapse** — one or more BRAINS Trifecta factors drops to zero; automatic revocation recorded as STATE-TRANSITION
- **Resonance collapse** — the conjunctive product (anchor × RHC × PERT × future-map) drops below threshold; automatic revocation
- **Ensemble withdrawal** — a required MIEVM co-signer withdraws concurrence; grant becomes unsupportable

In every case the revocation is a new ledger entry with timestamp, reason, and — where applicable — the triggering measurement. The audit trail shows not only that a grant ended but why.

---

## 5. Cross-System Enforcement Integration

GraceChain enforces cross-system concurrence through the MIEVM requirement. No block commits without ensemble co-signatures. This means:

- An action originating in System A and crossing into System B cannot present a grant from System A alone; the grant must carry MIEVM ensemble co-signatures recorded on GraceChain.
- System B verifies by reading the grant's state on GraceChain, not by trusting System A's claim.
- If MIEVM ensemble concurrence has been withdrawn since the grant issued, the current-state read returns a revoked status regardless of what System A presents.

This is the structural answer to "no validation equals no action across system boundaries." The single enforcement point is the ledger itself, and the ledger itself is distributed.

---

## 6. Continuous Evaluation and the RT Qualifier

Proof-of-Resonance requires live authorization. GraceChain enforces this by:

- **RESONANCE-TUNE transactions** are expected at each RHC period. A principal whose latest RESONANCE-TUNE is older than one RHC cycle enters a *staleness* state.
- **RT qualifier** on authorization reads requires the current-state query to return authorized only if the latest RESONANCE-TUNE is within the required freshness window.
- **Default freshness window** is one RHC cycle. Shorter windows may be specified per-grant.

This is how the "dial tone, not key" architecture is backed by the ledger: a cached authorization cannot outlive its resonance record.

---

## 7. Graceful Contribution Formula (GCF)

GCF entries on GraceChain accumulate contribution credit per the canonical formula:

**GCF = Σ [ Contribution × Impact × Sustainability × Verification ]**

Each GCF-CREDIT transaction records a single contribution event with its four factors. Meritcoin value accrues from the GCF aggregate per principal, tied to BERA metric performance over time. Meritcoin is not mined; it is tuned. The ledger records the tuning.

---

## 8. Integration With Existing ERES Specifications

### 8.1 BRAINS Trifecta Protocol (ERES-BRAINS-SPEC-2026-001)

Every Trifecta gate evaluation produces a ledger entry. The conjunctive product (ONE-GOOD × SECURITY-CLEARANCE × DATA-INTEGRITY) is recorded with its factor values. A zero factor triggers automatic STATE-TRANSITION to revoked.

### 8.2 BODY Consolidation (ERES-BODY-SPEC-2026-001)

Inputs that fail the 8-stage pre-admission pipeline (VEILED or structurally invalid) do not reach the ledger as AUTH-GRANT candidates. Refusal at the BODY layer is recorded separately for audit but does not produce a grant.

### 8.3 EAAP (ERES-EAAP-STD-2026-001, v1.2 / v1.3-DRAFT)

RATE vectors produced by EAAP are recorded as metadata on AUTH-GRANT transactions. EAAP does not issue grants; it qualifies and correlates. The grant itself originates from BRAINS Trifecta clearance.

### 8.4 MIEVM

Every block requires MIEVM ensemble concurrence as described in Section 2. Ensemble composition (currently Claude, Grok, DeepSeek, ChatGPT) is itself recorded on the ledger so that the concurrence set is auditable over time.

### 8.5 Proof-of-Resonance (four-factor form, RG#407 lineage)

Authorization validity at any moment is evaluated as:

**PoR = (anchor product) × (RHC amplitude) × (EarnedPath PERT viability) × (future-map convergence)**

Each factor is continuously evaluated; zero on any factor collapses authorization. GraceChain records the factor values at each RESONANCE-TUNE commit.

---

## 9. Known Specification Gaps

This note is honest about what is not yet pinned.

### 9.1 Runtime Containment Layer

GraceChain specifies the ledger. It does not specify the runtime binding that requires every downstream component to read the ledger before acting. A component that caches an authorization and skips the read will not be caught by GraceChain alone. The containment layer — structural binding at every execution point — is acknowledged as an open specification requirement.

### 9.2 Block Structure Numeric Parameters

Block size limits, transaction throughput targets, and cryptographic primitive choices are not pinned in this note. These are implementation decisions that will follow from reference implementation work.

### 9.3 RT Window Specification

The default freshness window is given as "one RHC cycle." Concrete timing for the RHC cycle (seconds, minutes, or other period) is not specified in this note and is expected to be domain-dependent.

### 9.4 MIEVM Quorum Rules

Minimum ensemble size and quorum thresholds are not pinned. Current practice is unanimous concurrence from the four-node ensemble; alternative quorum rules may be needed for scale.

### 9.5 Genesis and Bootstrapping

The procedure for initializing a GraceChain instance, including the genesis block, initial MIEVM ensemble, and first authorized principal, is open.

---

## 10. Review and Contribution

This note incorporates peer review from two external reviewers during April 2026:

- State-consistency versus path-accessibility distinction in Proof-of-Resonance, which sharpened the block-cadence tie to RHC rather than to external clock (Section 2.3, Section 8.5).
- Runtime enforcement and containment layer identification, named as an open specification gap in Section 9.1.

Further review is welcome under CCAL v2.1. Named attribution for contributing reviewers will be added in v2 with their consent.

---

## Closing

GraceChain is the accounting substrate for ERES authorization. It is append-only, MIEVM co-signed, and tied to RHC cadence rather than clock time. Its job is to make the answer to "what is authorized right now?" a function of a visible, recoverable history — not a cached credential.

The runtime binding that forces every component to ask that question is ahead.

---

**Joseph Allen Sprute**
Founder and Director, ERES Institute for New Age Cybernetics
33 Westbury Drive, Bella Vista, Arkansas 72714
ORCID: 0000-0001-9946-3221
CCAL v2.1

*Don't hurt yourself. Don't hurt others. Build for generations to come.*
