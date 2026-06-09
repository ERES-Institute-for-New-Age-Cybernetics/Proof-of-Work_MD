# EAAP → Secure User-Group Communications: Build Path

**Instrument ID:** ERES-EAAP-COMMS-BUILDPATH-2026-001
**Version:** v0.1 — DRAFT
**License:** CCAL v2.1
**Author:** Joseph Allen Sprute, ERES Institute for New Age Cybernetics
**ORCID:** 0000-0001-9946-3221
**Status:** Intent map. Distinguishes what runs today (`eaap_proof.py`) from what must be added.

---

## Intent

> An attestation and authorization protocol enabling secure, private communication among user-groups in smart-ID environments.

## What runs today (the gate)

`eaap_proof.py` is the **admission boundary**: a candidate action is submitted, four conjunctive Proof-of-Resonance factors are evaluated over strong Kleene three-valued logic, and the gate returns BIND / REFUSE / VEILED. Only BIND reaches the effect; every decision emits a tamper-evident, hash-chained receipt. This already provides **authorization, attestation logic, and audit** — three of the pieces a secure-comms system needs. It does **not** provide confidentiality (it does not encrypt or transport a message). That is the seam this document closes.

## The build path

Each layer states what it adds, what gate element it builds on, and its honest status.

### 1. Smart-ID key custody  *(builds on: factor A — attestation)*
- **Adds:** real cryptographic identities per actor and per user-group, with private keys held in TPM/TEE, never in source.
- **Today:** the demo attestation key is in-source (disclosed limit). The gate's factor-A logic is correct; the *custody* is the deployment piece.
- **Path:** Ed25519 attestation now → ML-DSA / Falcon post-quantum migration on the EAAP 2026–2032 timeline. Endpoint attestation binds an identity to an attested smart-ID environment, so a message is admissible only from an attested endpoint.
- **Status:** TO BUILD (gate-side logic BUILT).

### 2. Confidentiality layer  *(new — the "private" in private comms)*
- **Adds:** authenticated encryption of message payloads so content is readable only by intended recipients.
- **Path:** session-key agreement (e.g. X25519 ECDH) → AEAD payload encryption (e.g. ChaCha20-Poly1305 or AES-GCM) with forward secrecy. These are standard, defensible primitives offered as deployment candidates, **not** ERES canonical locks.
- **Relationship to the gate:** orthogonal and complementary. The gate decides *whether* a message may pass; the AEAD layer makes its *content* private. Per the gate/rating split discipline, neither substitutes for the other.
- **Status:** TO BUILD (not present in `eaap_proof.py` by design).

### 3. User-group membership & access policy  *(builds on: Lock C — pre-qualification inversion)*
- **Adds:** group definitions, membership pre-qualified *before* access (never granted post-hoc), and revocation.
- **Today:** Lock C already enforces "any requested cell not in the accessible set is REFUSED, not negotiated" — the exact shape of group-scoped access.
- **Path:** group-key / sender-key management so membership changes re-key the group; revocation removes decrypt capability.
- **Status:** TO BUILD (membership-gate pattern BUILT).

### 4. Per-message admission  *(builds on: the gate itself)*
- **Adds:** every outbound/inbound message is submitted to the gate as a candidate consequence before it is delivered. Delivery is the "effect" that fires only on BIND.
- **Path:** wrap the transport so the gate is consulted per message; REFUSE/VEILED messages never reach the channel.
- **Status:** TO BUILD (admission semantics BUILT).

### 5. Anti-replay & freshness  *(builds on: factor F — freshness)*
- **Adds:** per-message nonces and a freshness window so a captured message cannot be re-injected.
- **Today:** factor F already evaluates freshness against a logical clock.
- **Status:** mostly BUILT (extend nonces to the message layer).

### 6. Communications audit trail  *(builds on: hash-chained receipts)*
- **Adds:** the existing receipt chain becomes the per-message audit log — who sent, admitted/refused/held, in what order, verifiable after the fact via `verify_chain()`.
- **Status:** BUILT (reuse directly).

### 7. Runtime containment  *(builds on: RCR — Runtime Containment Requirement)*
- **Adds:** the guarantee that an unadmitted message cannot reach a recipient by any path — the containment that makes "only BIND is delivered" enforceable, not merely conventional.
- **Status:** TO SPECIFY for the comms boundary (gate-local RCR BUILT).

## The honest boundary

```
BUILT today  :  authorization · attestation logic · admission · freshness · audit
TO BUILD     :  smart-ID key custody · confidentiality (encryption) ·
                group key management · per-message transport · comms-layer RCR
```

The gate is the load-bearing brick. Secure user-group communication is the wall built on it. Layers 2 and 3 (confidentiality + group key management) are the largest pieces of net-new work; everything else extends a gate element that already runs.

---

*Three Governing Principles (operationally binding): Don't hurt yourself. Don't hurt others. Build for generations to come.*
