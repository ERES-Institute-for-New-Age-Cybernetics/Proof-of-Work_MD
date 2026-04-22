# ERES-CRYPTO-STD-2026-001

## ERES Crypto Standard — Full Stack Specification

**Document ID:** ERES-CRYPTO-STD-2026-001
**Version:** 1.1.1 (DeepSeek-patched)
**Status:** Standards Track (Proposed)
**Date:** April 22, 2026
**Primary Author:** Joseph Allen Sprute (ERES Maestro)
**Institution:** ERES Institute for New Age Cybernetics
**Supersedes:** v1.1 (USE.ai-hardened), which superseded v1.0 (MIEVM-synthesized), which superseded ERES-CRYPTO-SPEC-2026-001 v1.3 (metaphorical draft)
**Consolidates:** USE.ai epistemic frame, DeepSeek cryptographic interlock, ChatGPT standards-track stack, USE.ai v1.0 critique, DeepSeek v1.1 critique
**License:** CARE Commons Attribution License v2.1 (CCAL v2.1)
**Companion Specs:** ERES-BRAINS-SPEC-2026-001 (Trifecta Protocol), ERES-BODY-SPEC-2026-001 (Consolidation Pipeline)

---

## Revision History

**v1.1.1 (DeepSeek-patched) — April 22, 2026.** Single-issue PATCH responsive to DeepSeek's formal review of v1.1 (rated 9.4/10). DeepSeek identified one outstanding determinism risk: the weighted SPL selector (§9.3.3) specified `u = int(σ[0..7]) / 2⁶⁴` as a floating-point division, which on IEEE 754 implementations across architectures (x86_64, ARM, wasm) could theoretically produce divergent `u` values for identical σ, breaking MIEVM Test 4 (Determinism). v1.1.1 replaces the selector with integer cross-multiplication, eliminating floating-point from the comparison path entirely. This is a PATCH per §22.1 because (a) the default (unweighted) selector is byte-identical to v1.1, (b) no reference implementation had shipped the weighted variant, and (c) the fix preserves the same mathematical semantics under the single policy-declared integer-weights constraint of §11A.1.

Changes in v1.1.1:

- **§9.3.3 weighted selector rewritten** as integer cross-multiplication: `p × W_sum ≤ cum[i] × 2⁶⁴`. Floating-point arithmetic is now PROHIBITED in the weighted selector, not merely discouraged.
- **§9.3.4 determinism rule tightened** from "MUST use fixed-point or rational" to explicit "MUST use integer arithmetic only in the weighted-selector comparison."
- **§20.6 new normative test vector F** added for the weighted selector, with σ reused from Test Vector A, weights `[2, 4, 1]` for GCF, and the byte-level computation showing resolution to G3.
- **§22.1 patch-scope note clarified** to explicitly cite v1.1.1 as the exemplar of a valid PATCH scope (bug fix preserving semantics without changing RATE dimensionality, canonical equation, or primitive families).
- **Appendix C.2 extended** with the v1.1.1 row documenting DeepSeek's finding and its resolution.
- **Appendix C.3 updated** to remove "weighted SPL floating-point determinism fix" from pending v1.2 items (now done).

This PATCH is itself a MIEVM case study: the v1.1 adversarial review (DeepSeek) found an issue the v1.0 adversarial review (USE.ai) had not — which is exactly what an ensemble is supposed to do. See Appendix C.4 for the full instructive analysis.

**v1.1 (USE.ai-hardened) — April 22, 2026.** Targeted fixes responsive to USE.ai's 8/10 → 9/10 remediation list against v1.0:

- **Classification changed from "novel cryptographic model" to "attestation-composition trust model"** (Sections 1, 4.10, 15). ECS no longer implies it delivers cryptographic-primitive-class strength; it composes standard primitives into a structured authorization decision.
- **Failure-mode count reconciled** (Section 3.1, Section 14). Section 3 now says "exactly five primary failure codes plus ERROR," matching Section 14. The v1.0 "four" was a leftover from the earlier Claude-draft enumeration.
- **Test Vector A self-contradiction resolved** (Section 20.1). `r₁` is now canonically `10` per the normative Score function; the "both conformant" hedge is removed. Deterministic scoring is the *only* conformant behavior.
- **All placeholder functions formally specified** (Section 11.5). `Conflict(BERA, ctx)`, `SemanticClarity(ctx, resolved)`, `PolicyAlignment(ctx, rel_result)`, `compute_dimensions(...)`, and `composite_confidence(...)` now have concrete algorithms.
- **Reference REL algorithm added** (Section 10.5). REL is no longer fully deferred to policy.
- **Policy Language specified** (new Section 11A). Machine-readable JSON Schema for ECS policies with threshold grammar, critical-dimension declaration, and lexicon authentication rules.
- **SPL selection semantically honest** (Section 9.3). The `σ mod |readings|` selector is explicitly labeled a pseudorandom-from-evidence mapping. Intent binding comes from σ's derivation from BERA within the signed payload, *not* from semantic grounding of the mapping itself. A weighted-selection variant is specified as policy-optional.
- **Test vectors are byte-normative** (Section 20). Fixed test keypair, fixed nonce, fixed canonical JSON bytes, fixed SHA-256, fixed σ, fixed Ed25519 signatures. Every value is reproducible and verifiable.
- **Protocol guarantees vs. governance-policy guarantees explicitly separated** (Section 15.6). Clarifies which claims are cryptographic and which depend on external governance.

**v1.0 (MIEVM-synthesized) — April 22, 2026.** Initial three-way ensemble synthesis. Scored 8/10 by USE.ai as an attestation-protocol draft and 3/10 as a cryptographic-primitive specification; the v1.1 changes above respond to that split rating.

---

## Status of This Document

This is a Standards Track draft of the ERES Crypto Standard (hereafter **ECS**). It has been produced through the Multi-Instance Ensemble Validation Method (MIEVM), drawing on four sources of input:

1. USE.ai (Claude) as epistemic developer and v1.0 adversarial reviewer;
2. DeepSeek as cryptographic generator;
3. ChatGPT as adversarial-standards reviewer;
4. USE.ai's v1.0 formal critique (8/10, attestation-protocol class) as the anvil for v1.1 refinement.

Where drafts diverged, this document preserves the strongest defensible form of each contribution and discards claims that cannot be independently verified. Where USE.ai's v1.0 critique identified concrete defects, this document addresses each item in v1.1 per the Revision History above.

This document is submitted for further MIEVM adversarial review (Grok and v1.2 pass), Hague-equivalent governance review, and open public commentary under CCAL v2.1.

---

## Abstract

The ERES Crypto Standard (ECS) defines a **semantic-attestation and authorization protocol layer** that sits above conventional cryptographic infrastructure. ECS does not replace encryption, digital signatures, transport security, or computational-hardness-based cryptographic primitives. Instead, it composes with them to produce a deterministic, auditable, multi-dimensional authorization decision from three independent classes of evidence:

1. **CBGMODD** — governance role attestations (a structured seven-role civic vector)
2. **FAVORS** — biometric evidence bundle (six channels: Fingerprint · Aura · Voice · Odor · Retina · Signature)
3. **BERA** — Bio-Electric Resonance Architecture evidence vector (four indices: ARI · ERI · RHC · RCI)

The canonical operational form is:

```
RATE = (CBGMODD × FAVORS) + BERA
```

where **RATE** is a seven-dimensional output vector whose elements are integers in `{1..10}` or the distinguished symbol `⊥` (VEILED), indicating evidential uncertainty that MUST NOT be substituted with zero.

Security in ECS rests on the joint difficulty of compromising three independent evidence classes simultaneously, *composed on top of* standard cryptographic primitives (Ed25519 signatures, SHA-256/SHA-3/BLAKE3 hashes, HKDF key derivation, TLS transport). This is explicitly **not** a new cryptographic-primitive class. It is an **attestation-composition trust model** whose protocol-level guarantees are narrowly scoped (Section 15) and whose governance-dependent guarantees are flagged as such (Section 15.6).

ECS is the cryptographic substrate for the ERES SECUIR energy–security layer, consumed by downstream oracles (UBIMIA, NBERS, PlayNAC, VERTECA) and anchored by conventional Ed25519 signatures and SHA-256/SHA-3/BLAKE3 canonical hashing.

---

## Keywords

ERES, ECS, Resonance Cryptography, Semantic Attestation, Proof-of-Resonance, CARE Governance, PlayNAC, EarnedPath, RATE, CBGMODD, FAVORS, BERA, VEILED, VERTECA, GAIA, UBIMIA, NBERS, SECUIR, MIEVM, Civic Cryptography, Merit-Based Ledgering, Semantic Integrity, Non-Compensation

---

## Table of Contents

1. Scope
2. Conformance Language
3. Design Position
4. Terminology and Definitions
5. System Model — The Six-Layer Stack
6. Core Input Components
7. Canonical RATE Equation and Output Structure
8. Canonical Encoding Layer (CEL)
9. Semantic Payload Layer (SPL)
10. Resonance Evaluation Layer (REL)
11. RATE Computation Layer (RCL)
11A. Policy Language (ECS-POL v1.0) — **new in v1.1**
12. Signature Layer (RSIG)
13. Audit Persistence Layer (APL)
14. Failure Modes and VEILED Semantics
15. Security Model (incl. §15.6 protocol vs. governance separation — **new in v1.1**)
16. Threat Model
17. Implementation Requirements
18. MIEVM Validation Requirements
19. Interoperability (PlayNAC, VERTECA, UBIMIA, NBERS, GAIA)
20. Test Vectors (byte-normative — **hardened in v1.1**; §20.6 added in v1.1.1)
21. Compliance
22. Governance and Versioning
23. Ethical Clause (CARE Constraint)
24. Credits
25. References
- Appendix A — Terminology Glossary
- Appendix B — Minimal Implementation Checklist
- Appendix C — MIEVM Synthesis Note (incl. v1.1 hardening log)
- Appendix D — Trifecta Protocol Alignment

---

## 1. Scope

### 1.1 What ECS Is

ECS defines a protocol layer for:

- Evaluating whether a subject is sufficiently attested to perform a civic, economic, or governance action;
- Producing a multi-dimensional authorization output (RATE) that preserves provenance and refuses scalar collapse;
- Routing unresolved, conflicting, or insufficiently-attested cases into deterministic review workflows;
- Binding intent cryptographically to the attestation bundle that produced it;
- Interoperating with downstream CARE-based civic systems (PlayNAC, UBIMIA, NBERS, VERTECA, GAIA).

### 1.2 What ECS Is Not

ECS does **NOT** claim:

- Confidentiality of transported data (use TLS / authenticated encryption);
- Public-key indistinguishability or signature unforgeability (use Ed25519 / ECDSA / RSA-PSS at the RSIG layer);
- Resistance to quantum attack in the conventional cryptographic hardness sense;
- Replacement of standard key-exchange, KEM, or PKI infrastructure;
- Hardware attestation (use TPM / secure-enclave primitives as prerequisites).

Those functions remain the responsibility of standard mechanisms. ECS composes with them. It does not supersede them.

### 1.3 Applicability

ECS applies to:

- CARE-based civic accounting systems;
- EarnedPath learning and accreditation infrastructure;
- Governance integrity and non-punitive remediation systems;
- Community-based dispute resolution ledgers;
- Merit-based incentive systems (UBIMIA, Meritcoin / GraceChain);
- The SECUIR energy–security layer of the GAIA organism;
- VERTECA voice-to-meaning semantic portal authorization.

---

## 2. Conformance Language

The key words **MUST**, **MUST NOT**, **REQUIRED**, **SHALL**, **SHALL NOT**, **SHOULD**, **SHOULD NOT**, **RECOMMENDED**, **MAY**, and **OPTIONAL** in this document are to be interpreted as described in RFC 2119 and RFC 8174 when, and only when, they appear in all capitals.

---

## 3. Design Position

ECS is a **decision-layer protocol**. A conforming implementation MUST preserve the following four properties:

1. **Deterministic evaluation.** Given identical inputs under identical policy, evaluation MUST return identical outputs. No randomness or environmental entropy may affect RATE resolution once inputs are fixed.

2. **Explicit failure modes.** Ambiguity MUST be represented by the distinguished symbol `⊥` (VEILED) and by exactly five primary failure codes plus one internal-ERROR category (Section 14). Silent failure, fallback-to-zero, and implicit reinterpretation are prohibited.

3. **Multi-dimensional output.** RATE MUST be a seven-dimensional structured vector. Reduction to a single scalar for authorization purposes is prohibited (Section 7.3).

4. **Separation of mechanics from interpretation.** Protocol mechanics (encoding, hashing, signing, evaluation) MUST be specifiable in ordinary software engineering terms. Governance-semantic interpretation (what a score "means" in civic context) is the responsibility of downstream consuming oracles and MUST NOT be embedded in ECS primitives.

The protocol retains symbolic names inherited from prior ERES materials (VEILED, Resonance, Superposition, Polysemantic Primitive). All such names are reduced to concrete data types and algorithms within this standard. Symbolic heritage is preserved for naming continuity; it is not a claim of metaphysical mechanism.

---

## 4. Terminology and Definitions

### 4.1 RATE

RATE is the canonical seven-dimensional output vector of the ECS Evaluate function.

```
RATE := ⟨r₁, r₂, r₃, r₄, r₅, r₆, r₇⟩
```

where each `rᵢ ∈ {1, 2, ..., 10} ∪ {⊥}`.

The symbol `⊥` (read "VEILED") denotes cryptographic null — a state in which the required evidence to resolve that dimension was absent, insufficient, or in irreconcilable conflict.

RATE MUST be computed deterministically. RATE MUST be reproducible by any compliant verifier given identical inputs and policy. RATE MUST be traceable to its contributing vectors.

Suggested semantic axes (normative for interoperability with PlayNAC / UBIMIA / NBERS):

| Dim | Name                   | Primary Source          |
|-----|------------------------|-------------------------|
| r₁  | Transaction confidence | Aggregate of all three  |
| r₂  | Biometric confidence   | FAVORS                  |
| r₃  | Governance validity    | CBGMODD                 |
| r₄  | Contextual consistency | BERA (ARI + ERI)        |
| r₅  | Semantic clarity       | SPL + VERTECA resolve   |
| r₆  | Temporal persistence   | BERA (RCI)              |
| r₇  | Policy alignment       | REL constraint results  |

### 4.2 CBGMODD

CBGMODD is the governance-role attestation vector. It encodes the participating civic roles and their attestation state for a given transaction.

Canonical expansion of the seven role positions:

- **C** — Citizen
- **B** — Business
- **G** — Government
- **M** — Mediator / Ombudsman
- **O** — Military / Infrastructure Security
- **D₁** — Dignitary / Moral Authority
- **D₂** — Diplomat / International Coordination

CBGMODD MUST be represented as a structured vector of role records, each containing:

- role identifier (one of C, B, G, M, O, D₁, D₂);
- role weight (policy-defined, non-negative rational);
- role credibility score (normalized to `[0, 1]`);
- role signature (Ed25519 or equivalent over the canonical payload hash);
- role attestation timestamp (UTC, RFC 3339).

A transaction-specific policy defines which role positions are REQUIRED, which are OPTIONAL, and what minimum credibility each requires.

Define:

```
CBGMODD_valid = 1   iff  all REQUIRED role positions carry
                          valid, current, credibility-threshold-
                          meeting signatures

CBGMODD_valid = 0   otherwise
```

### 4.3 FAVORS

FAVORS is the biometric evidence bundle. Canonical expansion:

- **F** — Fingerprint
- **A** — Aura (BERA-ARI-equivalent contextual liveness reading)
- **V** — Voice
- **O** — Odor (or auxiliary biosignal)
- **R** — Retina
- **S** — Signature (manual or dynamic)

FAVORS MUST be represented as a tuple of six confidence scores, each normalized to `[0, 1]`:

```
FAVORS := (f, a, v, o, r, s)
```

A policy profile defines:

- minimum required channels (which of the six are MANDATORY);
- minimum score per channel;
- quorum rule (e.g., "any 4 of 6 above 0.85", or "all mandatory channels above 0.90").

Define a verification function:

```
VerifyFAVORS(FAVORS, policy) → {0, 1}
```

that returns `1` if and only if the biometric policy is fully satisfied.

The **A** (Aura) channel is NORMATIVELY identical to the BERA-ARI reading when BERA sensors are available; implementations MAY substitute a contextual-liveness surrogate where BERA instrumentation is absent, provided the substitution is declared in RATE.provenance.

### 4.4 BERA

BERA is the Bio-Electric Resonance Architecture evidence vector. Canonical four-index form:

```
BERA := (ari, eri, rhc, rci)
```

with each index normalized to `[0, 1]`.

Canonical index expansions:

- **ARI** — Attestation / Aura Resonance Indicator (HRV-derived coherence signal; contextual liveness)
- **ERI** — Environment / Evidence Reliability Indicator (signal-to-noise of surrounding evidence context)
- **RHC** — Resonant Harmony Cycle (cyclic consistency of the subject's bio-signature over the short-term window; **RHC always expands to *Resonant Harmony Cycle*** — never any other phrase)
- **RCI** — Resonance Continuity Indicator (longitudinal stability across time)

BERA MUST be computed from an auditable sensor and scoring pipeline aligned with the BERA Sensor Specification (RG#404) and conformant with BERC / JERC / PERC governance frameworks. BERA MUST be bounded to `[0, 1]` per dimension to prevent runaway inflation in the RATE arithmetic.

Define:

```
BERA_valid = 1   iff  at least three of the four indices are
                       non-null and policy-threshold-meeting

BERA_valid = 0   otherwise
```

BERA is not a metaphysical input. It is a structured, sensor-grounded evidence vector that:

- measures confidence of bio-electric attestation;
- estimates stability of the subject's state;
- modulates downstream scoring;
- triggers REVIEW status when coherence is insufficient.

### 4.5 Resonance Signature (σ, RSIG)

Two related but distinct artifacts share this nomenclature. Implementations MUST NOT conflate them.

**4.5.1 σ (sigma) — Internal resonance derivation.**
σ is a key-equivalent value derived from BERA via a specified KDF:

```
σ = HKDF-SHA256(secret=BERA_canonical_bytes,
                salt=transaction_nonce,
                info="ERES-ECS-v1.0-sigma",
                length=32)
```

σ is used internally during SPL resolution (Section 9) to deterministically select among polysemantic primitive readings. σ MUST NOT be logged in cleartext.

**4.5.2 RSIG — External resonance signature artifact.**
RSIG is the externally visible cryptographic proof that a RATE computation was produced by a compliant engine under a valid semantic context. See Section 12.

### 4.6 VEILED (`⊥`)

VEILED is the distinguished symbol representing cryptographic null in a RATE dimension. VEILED MUST NOT be substituted by `0`, `1`, `null`, empty string, or any integer. A conforming implementation MUST treat VEILED as a distinct value preserved through serialization, hashing, comparison, and downstream consumption.

VEILED indicates one of:

- The required evidence to resolve that dimension was absent;
- Evidence was present but in irreconcilable conflict beyond policy tolerance;
- The σ derivation failed and the dimension depends on σ-resolution;
- Policy explicitly defers this dimension to a downstream reviewer.

### 4.7 Scalar Collapse Prohibition

**Scalar collapse** is the reduction of a multi-dimensional RATE vector to a single scalar for authorization purposes, discarding provenance. ECS implementations MUST NOT perform scalar collapse. A scalar summary (RATE.score, Section 7.2) MAY be provided as a convenience field, but the authorization decision MUST consult the full vector, the `⊥` positions, and RATE.provenance.

### 4.8 Proof-of-Resonance

Proof-of-Resonance is the ECS-specific replacement for computational-hardness proofs (e.g., Proof-of-Work) in consensus and validation contexts. It is the demonstration that a transaction's inputs satisfy the joint attestation requirements of CBGMODD, FAVORS, and BERA to within policy thresholds, witnessed by an RSIG from a compliant engine. Per canonical ERES framing: *"It's not mining — it's tuning."*

### 4.9 Attestation-Composition Trust Model (normative type)

ECS is formally classified as an **attestation-composition trust model**, not a cryptographic-primitive class. This classification has three normative consequences that implementers and reviewers MUST understand:

1. **ECS's strength is compositional.** Its protocol-level guarantees are inherited from (a) the underlying signature and hash primitives, (b) the deployment-level independence of the three evidence classes, and (c) the deterministic evaluation of fixed policies. ECS does not add new cryptographic hardness. It adds *structure* that makes attestation composition explicit, auditable, and non-compensatory.

2. **ECS without its underlying primitives is nothing.** A deployment that uses weak signatures, colliding hashes, or a compromised KDF gains no safety from ECS. ECS assumes and requires well-specified conventional cryptography.

3. **ECS's governance guarantees are governance-dependent.** Any claim of the form "ECS prevents X" where X is a governance outcome (discrimination, coercion, capture) holds *only if* the consuming policy, lexicon, and REL configuration are themselves sound. ECS provides the cryptographic channel for governance enforcement; it does not provide the governance itself. This is made explicit in Section 15.6.

This classification replaces the v1.0 framing of "novel attestation-composition security model," which USE.ai correctly flagged as overreaching. The word "novel" is removed. The word "model" is retained.

---

## 5. System Model — The Six-Layer Stack

A conforming ECS implementation SHALL consist of the following six layers, evaluated in order. Each layer MUST preserve the invariants of the layers below it and MUST NOT bypass them.

```
┌───────────────────────────────────────────────────┐
│  Layer 6 — Audit Persistence Layer (APL)          │  ← tamper-evident ledger
├───────────────────────────────────────────────────┤
│  Layer 5 — Signature Layer (RSIG)                 │  ← Ed25519 / ECDSA / RSA-PSS
├───────────────────────────────────────────────────┤
│  Layer 4 — RATE Computation Layer (RCL)           │  ← (CBGMODD × FAVORS) + BERA
├───────────────────────────────────────────────────┤
│  Layer 3 — Resonance Evaluation Layer (REL)       │  ← CARE/BERC/JERC/PERC constraints
├───────────────────────────────────────────────────┤
│  Layer 2 — Semantic Payload Layer (SPL)           │  ← polysemantic resolution via σ
├───────────────────────────────────────────────────┤
│  Layer 1 — Canonical Encoding Layer (CEL)         │  ← deterministic serialization + hash
└───────────────────────────────────────────────────┘
```

Each layer is specified in its own section (Sections 8–13). The layers are numbered bottom-up to match the dependency order: a RATE result cannot be signed (Layer 5) until it has been computed (Layer 4), which cannot proceed until constraints are evaluated (Layer 3), which cannot proceed until semantic resolution is complete (Layer 2), which cannot proceed until canonical encoding and hashing (Layer 1) have produced a stable payload.

### 5.1 Layer Boundaries and Data Flow

```
Raw inputs (ctx, CBGMODD, FAVORS, BERA)
        │
        ▼
┌─────────────┐
│    CEL      │  →  canonical bytes, payload_hash H
└─────────────┘
        │
        ▼
┌─────────────┐
│    SPL      │  →  σ = HKDF(BERA, nonce), resolved primitives
└─────────────┘
        │
        ▼
┌─────────────┐
│    REL      │  →  constraint pass/fail, violation list
└─────────────┘
        │
        ▼
┌─────────────┐
│    RCL      │  →  RATE vector + RATE.provenance
└─────────────┘
        │
        ▼
┌─────────────┐
│   RSIG      │  →  signed attestation artifact
└─────────────┘
        │
        ▼
┌─────────────┐
│    APL      │  →  tamper-evident persistence
└─────────────┘
```

---

## 6. Core Input Components

See Section 4 for definitions. This section specifies wire-format requirements.

### 6.1 CBGMODD Wire Format

```json
{
  "cbgmodd": [
    {
      "role": "C",
      "weight": 1.00,
      "credibility": 0.80,
      "signature": "ed25519:BASE64...",
      "attested_at": "2026-04-22T14:30:00Z"
    },
    {
      "role": "M",
      "weight": 1.50,
      "credibility": 0.90,
      "signature": "ed25519:BASE64...",
      "attested_at": "2026-04-22T14:31:00Z"
    }
  ]
}
```

Implementations MUST validate that:

- Every `role` is one of `{C, B, G, M, O, D1, D2}`;
- Every `credibility` is in `[0, 1]`;
- Every `weight` is a non-negative finite rational;
- Every `signature` verifies over the canonical payload hash;
- `attested_at` is within the policy-defined freshness window.

### 6.2 FAVORS Wire Format

```json
{
  "favors": {
    "f": 0.92,
    "a": 0.88,
    "v": 0.95,
    "o": null,
    "r": 0.90,
    "s": 0.87,
    "device_attestation": "tpm-quote:BASE64..."
  }
}
```

`null` in a channel indicates the channel was not sampled and MUST NOT be treated as `0`. Whether a null channel is permissible is governed by the policy quorum rule.

### 6.3 BERA Wire Format

```json
{
  "bera": {
    "ari": 0.84,
    "eri": 0.79,
    "rhc": 0.91,
    "rci": 0.82,
    "sensor_spec": "RG#404-v1.0",
    "window_seconds": 30
  }
}
```

`sensor_spec` MUST reference a published BERA Sensor Specification version (RG#404 or successor) to enable cross-implementation reproducibility.

---

## 7. Canonical RATE Equation and Output Structure

### 7.1 Normative Equation

The canonical ECS operational form is:

```
RATE = (CBGMODD × FAVORS) + BERA
```

This equation is **structural** — it names the composition of three independent evidence classes into one multi-dimensional output. It is **not** a straight arithmetic product followed by a straight arithmetic sum; the operators `×` and `+` are defined by the RATE Computation Layer (Section 11), which applies policy-specified scoring functions to each RATE dimension.

The equation MUST be preserved verbatim in ECS documentation and in downstream citations, regardless of the specific scoring functions a policy chooses.

### 7.2 Output Structure

RATE MUST be returned as a structured object, not as a bare vector:

```json
{
  "rate": {
    "vector": [8, 9, 10, 7, 8, 6, 9],
    "score": 7.86,
    "provenance": {
      "cbgmodd_hash": "sha256:...",
      "favors_hash":  "sha256:...",
      "bera_hash":    "sha256:...",
      "policy_id":    "uri:eres:policy:2026:ubimia:v3"
    },
    "audit_flags": ["CARE_OK", "BERC_OK", "JERC_OK"],
    "confidence": 0.91,
    "veiled_positions": []
  }
}
```

Fields:

- **`vector`** — the seven-dimensional RATE vector. Each position is an integer in `{1..10}` or the literal string `"VEILED"` (serialization form of `⊥`).
- **`score`** — OPTIONAL convenience scalar; the arithmetic mean of non-VEILED dimensions. MUST NOT be used as the sole basis for authorization.
- **`provenance`** — hashes of the input components plus the policy identifier under which RATE was computed.
- **`audit_flags`** — REL constraint results (`CARE_OK`, `BERC_OK`, `JERC_OK`, `PERC_OK`, or their `_FAIL` counterparts).
- **`confidence`** — overall confidence in `[0, 1]`, derived from BERA_valid, FAVORS quorum margin, and CBGMODD credibility aggregate.
- **`veiled_positions`** — indices of RATE.vector that are VEILED, with per-position reason codes.

### 7.3 Scalar Collapse (Prohibited)

Authorization decisions MUST consult `vector`, `veiled_positions`, and `audit_flags` jointly. It is a **compliance violation** to:

- Use `score` as the sole authorization input;
- Treat a `VEILED` position as numeric `0` for aggregation;
- Compute an unweighted mean across dimensions and compare to a single threshold.

This prohibition directly implements the **Non-Compensation Claim** (Section 15.3), which is the ECS arithmetic counterpart to the conjunctive-gate requirement of the ERES Reckoning Anchors (seven Resonance Anchors: U, S, R, B, M, G, T — ref. ERES-RECKON-WP-2026-002).


---

## 8. Canonical Encoding Layer (CEL)

### 8.1 Serialization Requirements

All ECS payloads MUST be serialized deterministically. A compliant CEL implementation MUST:

- Preserve field ordering per a lexicographic key sort over UTF-8 byte sequences;
- Enforce numeric precision rules: floating-point values in `[0, 1]` MUST be encoded to exactly six decimal places (half-even rounding) prior to hashing;
- Normalize Unicode strings to NFC (Unicode Normalization Form C);
- Prohibit ambiguous whitespace: no insignificant whitespace between tokens in the hash-input representation;
- Require explicit null representation: missing fields MUST be absent; optional-but-null fields MUST use the literal `null` token; `⊥` MUST be encoded as the literal string `"VEILED"`.

### 8.2 Encoding Formats

- **JSON-C (JSON-Canonical)** is the RECOMMENDED encoding for ECS payloads. JSON-C is RFC 8785-style canonical JSON with the additional rules in Section 8.1.
- **CBOR (RFC 8949, deterministic encoding profile)** is OPTIONAL and MAY be used for constrained-device implementations.
- **Protobuf, MessagePack, and other formats are NOT PERMITTED** for canonical encoding because they lack a universally agreed deterministic profile.

### 8.3 Canonical Payload Hash

A compliant engine MUST compute:

```
H = HASH(CANONICAL_ENCODE(payload))
```

HASH MUST be one of:

- SHA-256 (RECOMMENDED baseline, NIST FIPS 180-4);
- SHA3-256 (NIST FIPS 202);
- BLAKE3 (IETF draft-aumasson-blake3).

The selected hash function MUST be recorded in the RSIG (Section 12) so that verifiers need not guess.

### 8.4 Wire-Level Transport

ECS payloads are transport-agnostic. Implementations SHOULD deliver payloads over TLS 1.3 or equivalent authenticated-encrypted channels. Transport security is not within ECS scope.

---

## 9. Semantic Payload Layer (SPL)

### 9.1 Purpose

SPL is the layer at which polysemantic primitives are resolved to their specific contextual readings. It replaces the v1.3-era "semantic superposition" metaphor with a deterministic selector driven by σ and an explicit policy lexicon.

### 9.2 Polysemantic Primitives

A **polysemantic primitive** is a finite set of possible plaintext readings for a named civic concept. ECS defines three canonical primitive families; policies MAY register additional domain-specific primitives.

| Primitive | Readings | Meaning |
|-----------|----------|---------|
| **GCF** (Graceful Contribution Formula) | `{G₁, G₂, G₃}` | Contribution framing: repair, renewal, origination |
| **EDF** | `{E₁, E₂, E₃}` | Earned Dignity, Earth Defense, Earth Data |
| **USC** | `U₁..₃ × S₁..₃ × C₁..₃` (27 triples) | User × Subject × Context composition |

Each primitive family MUST be declared in a policy lexicon file with a stable URI. Addition of a fourth reading to any primitive is a MAJOR version change.

### 9.3 Deterministic Resolution

Before σ is applied, a primitive is in **superposition** — the set of possible readings. "Superposition" in ECS means "the key (σ) has not yet been applied." It does NOT imply physical quantum superposition.

With a valid σ derived from BERA (Section 4.5.1), the resolution function selects one reading:

```
Resolve(primitive_family, σ, ctx, policy_lexicon) → reading
```

Resolution MUST be deterministic: same `(primitive_family, σ, ctx, lexicon)` → same `reading`, always. Resolution MUST use a finite controlled vocabulary specified by the policy lexicon — never free-form natural language.

#### 9.3.1 Default selector (normative)

```
i = (int(σ[0..3], big_endian) mod |readings|)
reading = readings[i]
```

where `σ[0..3]` is the first four bytes of the 32-byte σ and `|readings|` is the cardinality of the primitive's reading set.

#### 9.3.2 Honest characterization of the default selector

The default selector is deterministic and evidence-dependent, but it is **pseudorandom with respect to semantic content**. The selected reading is a function of σ, and σ is a function of BERA, but the mapping from σ to reading index does not encode any semantic relationship between the subject's bio-electric state and the meaning of the chosen reading. USE.ai's v1.0 critique correctly identified this as a gap between what a naive reader might expect from "intent binding" and what the default selector actually provides.

The **intent binding that ECS does deliver** (Claim 2, Section 15.3) is the following: because BERA is part of the canonical payload hash, and the canonical payload hash is covered by RSIG, an adversary who wants a transaction to resolve to reading `r_j` rather than `r_i` must produce BERA evidence whose HKDF output indexes to `j` — which requires either (a) a collision in HKDF, (b) control over the BERA sensor pipeline, or (c) the subject's actual participation. *Which* reading σ selects is not semantically grounded; *that* a particular σ uniquely and verifiably selects that reading, bound to signed BERA, is the cryptographic content of the claim.

Policies that require semantic grounding of reading selection SHOULD use the weighted-selection variant below.

#### 9.3.3 Weighted selection variant (policy-optional)

A policy lexicon MAY specify a weight vector `w = (w₁, w₂, ..., w_k)` for each primitive family, where each `wᵢ` is a **non-negative integer** and `Σwᵢ > 0`. The weights are permitted to depend on `ctx` through a declared function `W(ctx) → w` that MUST be:

- Deterministic;
- Published as part of the authenticated policy lexicon;
- **Integer-valued.** Fractional, decimal, floating-point, or real-number weights are PROHIBITED. Policies that conceptually want fractional weights (e.g., "bias toward G₂ by 3.5× over G₁") MUST scale to integers (e.g., `[2, 7, 1]` instead of `[1, 3.5, 0.5]`) such that the ratios are preserved exactly.

The weighted selector is defined in **integer arithmetic only** (v1.1.1 patch):

```
p      = int(σ[0..7], big_endian)       // uint64, 0 ≤ p < 2⁶⁴
W_sum  = Σ wⱼ                            // positive integer
cum[i] = Σ_{j ≤ i} wⱼ                    // integer cumulative sums;
                                          // cum[k-1] = W_sum (note: cum is 0-indexed here)

Find smallest i such that:

        p × W_sum  ≤  cum[i] × 2⁶⁴

reading = readings[i]
```

All intermediate quantities are arbitrary-precision integers (or uint128/BigInt in languages that provide them). Floating-point arithmetic is **PROHIBITED** anywhere in this path. Division is **PROHIBITED**. The comparison `p × W_sum ≤ cum[i] × 2⁶⁴` is a pure integer inequality and is identical on every conforming implementation on every architecture.

Why this form:

The conceptual semantics are `u ≤ cdf[i]` where `u = p / 2⁶⁴` and `cdf[i] = cum[i] / W_sum`. Cross-multiplying by the positive denominators `2⁶⁴` and `W_sum` yields the integer inequality `p × W_sum ≤ cum[i] × 2⁶⁴`, which preserves the exact mathematical relation without requiring any floating-point operation. Because `cum[k-1] = W_sum` and `p < 2⁶⁴`, the inequality `p × W_sum < W_sum × 2⁶⁴` holds at the last index regardless of σ, so the selector always terminates with a valid reading.

Worked example (normative, see §20.6 for full Test Vector F): with σ from Test Vector A (first 8 bytes = `0xe43732833d50a050`), `p = 16,444,668,103,617,454,160`, weights `w = [2, 4, 1]`, `W_sum = 7`, `cum = [2, 6, 7]`:

- `i=0`: `p × 7 = 115,112,676,725,322,179,120` vs. `2 × 2⁶⁴ = 36,893,488,147,419,103,232`. Greater. Continue.
- `i=1`: `p × 7 = 115,112,676,725,322,179,120` vs. `6 × 2⁶⁴ = 110,680,464,442,257,309,696`. Greater. Continue.
- `i=2`: `p × 7 = 115,112,676,725,322,179,120` vs. `7 × 2⁶⁴ = 129,127,208,515,966,861,312`. `≤`. **Select G3**.

When a weighted selector is in use, the policy lexicon MUST ship the weight-generating function `W` (or a table), and RATE.provenance MUST record which selector variant was used (`"selector_variant": "weighted"`) and the integer weight vector actually applied for this transaction. Weighted selection lets a policy encode *"when ctx indicates financial-reparations framing, bias GCF selection toward G₂ (renewal) 4-to-2-to-1 over G₁ (repair) and G₃ (origination)."* This gives semantic grounding at the cost of requiring an explicit policy authority; the default selector gives no semantic grounding but requires no weight-publishing authority.

#### 9.3.4 Determinism requirement (both variants)

Resolution MUST be deterministic. Same `(primitive_family, σ, ctx, lexicon, selector_variant)` → same `reading`, always.

For the **default selector** (§9.3.1), determinism is trivially satisfied because only integer modulus is used.

For the **weighted selector** (§9.3.3), determinism requires that implementations use integer arithmetic for the `p × W_sum ≤ cum[i] × 2⁶⁴` comparison. Conforming implementations **MUST NOT** use floating-point division, floating-point multiplication, or floating-point comparison anywhere in the weighted-selector path. Floating-point operations have platform-dependent rounding (IEEE 754 fused-multiply-add availability varies between x86_64, ARM, and wasm targets) and MUST NOT appear in any path whose output is covered by RSIG.

Implementations in languages without native 128-bit integers (e.g., JavaScript without BigInt, pre-C99 C) MUST use arbitrary-precision integer libraries for the cross-multiplication. Test Vector F (§20.6) is the conformance check: any compliant v1.1.1 implementation MUST resolve to `G3` under the specified inputs.

### 9.4 VERTECA Integration

SPL is the layer at which **VERTECA** (voice-to-meaning portal protocol, GAIA voice layer) deposits its utterance-to-sound semantic interpretations into the ECS payload. A VERTECA-originated transaction MUST include:

- the original utterance hash;
- the SOUND-protocol resolved word sequence;
- the TLD/PlayNAC Keyword Ontology tag assignments;
- a voice-print FAVORS-V confidence score.

Where VERTECA disagrees with the policy lexicon, SPL MUST return VEILED for the affected RATE dimensions and defer to REVIEW status.

### 9.5 Semantic Collision Resistance

Two distinct intents MUST NOT produce the same canonical-encoded payload unless they are, by policy definition, semantically identical. Implementations MUST include primitive family identifiers and reading indices in the canonical payload to prevent collision between structurally similar but semantically distinct transactions.


---

## 10. Resonance Evaluation Layer (REL)

### 10.1 Constraint Families

A compliant REL MUST evaluate the following six constraint families before proceeding to RCL:

1. **CARE** — ethical-compliance constraints (Cooperative · Accountable · Restorative · Ecologic);
2. **BERC** — Bio-Ecologic Resonance Constraints (environmental and ecological correctness);
3. **JERC** — Justice / Equity Resonance Constraints (non-discriminatory outcome, distributional fairness);
4. **PERC** — Participation / Merit Resonance Constraints (contribution authenticity, anti-gaming);
5. **Paineologic Minimization** — systemic pain reduction check (no action that measurably increases human or ecological pain without restorative offset);
6. **CBGMODD Role Coherence** — the asserted role mix is policy-appropriate for the transaction type.

Each constraint family MUST produce:

- pass/fail boolean;
- violation list (if fail), each with a stable reason code and a textual description;
- compliance score in `[0, 1]`;
- confidence rating in `[0, 1]`.

### 10.2 Pass/Fail Output

REL output format:

```json
{
  "rel": {
    "overall": "PASS",
    "critical_violations": [],
    "non_critical_violations": [],
    "compliance_scores": {
      "CARE": 0.98,
      "BERC": 0.92,
      "JERC": 0.95,
      "PERC": 0.90,
      "PAIN": 0.99,
      "CBGMODD_COHERENCE": 1.00
    },
    "confidence": 0.94
  }
}
```

### 10.3 Critical Violation Bar

REL MUST NOT output `"overall": "PASS"` if any critical violation exists. The set of critical-violation reason codes is defined by policy but MUST include at minimum:

- `CARE_CRITICAL_HARM` — action produces measurable harm to a protected class with no restorative path;
- `BERC_IRREVERSIBLE_LOSS` — action produces irreversible ecological loss without offset;
- `JERC_DISCRIMINATION` — action is non-uniform across protected categories by unjustifiable criteria;
- `PERC_FRAUD` — merit evidence is fabricated;
- `PAIN_INCREASE_UNOFFSET` — net Paineologic increase without offsetting Meritcologic contribution;
- `CBGMODD_ROLE_FORGERY` — asserted role attestation fails signature verification.

### 10.4 Non-Punitive Remediation Hook

Where REL fails on a non-critical violation, the REL output MUST include a `remediation` field referencing the Non-Punitive Remediation workflow (EarnedPath / Grace Protocol). ECS does not punish; ECS routes.

### 10.5 Reference REL Evaluation Algorithm

The following algorithm is the **reference** REL evaluator. Deployments MAY substitute a more sophisticated REL provided (a) the conformance properties of Section 10.1–10.4 are preserved and (b) the substitution is declared in RATE.provenance.

```
REL.evaluate(ctx, CBGMODD, FAVORS, BERA, resolved_primitives, policy) → rel_result

Step 1. For each family F in {CARE, BERC, JERC, PERC, PAIN, CBGMODD_COHERENCE}:
          load family rule-set RF from policy;
          violations_F = []
          for each rule r in RF:
            applied = evaluate_rule(r, ctx, CBGMODD, FAVORS, BERA, resolved_primitives)
            if applied.violated:
              violations_F.append({
                family: F,
                rule_id: r.id,
                severity: r.severity,      // one of {CRITICAL, MAJOR, MINOR}
                reason_code: r.reason_code,
                description: applied.description
              })
          compliance_F = 1 - (sum of severity-weighted violations in violations_F)
          clamp compliance_F to [0, 1]
          confidence_F = min(1, count(rules_with_sufficient_evidence) / count(RF))

Step 2. critical_violations = [v in all violations where v.severity == CRITICAL]
        non_critical_violations = [v in all violations where v.severity != CRITICAL]

Step 3. overall = "FAIL" if critical_violations non-empty else "PASS"

Step 4. compliance_scores = { F: compliance_F for each family F }
        confidence = geometric_mean(confidence_F for each family F)

Step 5. return {
          overall,
          critical_violations,
          non_critical_violations,
          compliance_scores,
          confidence,
          compliance_flags: [
            "CARE_OK"  if compliance_scores["CARE"]  >= policy.thresholds.CARE,
            "BERC_OK"  if compliance_scores["BERC"]  >= policy.thresholds.BERC,
            "JERC_OK"  if compliance_scores["JERC"]  >= policy.thresholds.JERC,
            "PERC_OK"  if compliance_scores["PERC"]  >= policy.thresholds.PERC,
            "PAIN_OK"  if compliance_scores["PAIN"]  >= policy.thresholds.PAIN,
            "COHERENCE_OK" if compliance_scores["COHERENCE"] >= policy.thresholds.COHERENCE
          ] (only flags whose conditions are met are included)
        }
```

`severity-weighted violations` uses the fixed table:

| Severity  | Weight |
|-----------|--------|
| CRITICAL  | 1.0    |
| MAJOR     | 0.33   |
| MINOR     | 0.10   |

Severity classification of each rule is declared in the policy. A policy MUST classify at least one rule per family as CRITICAL. USE.ai's critique that "REL carries a lot of weight but scoring is policy-defined" is honestly answered here: the algorithm above is fixed; *which rules exist and their severity* are correctly left to policy (this is the separation between protocol mechanics and governance interpretation from Section 3.4). Rule evaluation itself — `evaluate_rule` — is policy-declared in the policy language (Section 11A).

---

## 11. RATE Computation Layer (RCL)

### 11.1 Pre-conditions

RCL MUST NOT execute unless:

- CEL has produced a valid canonical payload hash;
- SPL has resolved all referenced polysemantic primitives (or returned VEILED for unresolvable ones);
- REL has returned `"overall": "PASS"` — or has flagged specific non-critical violations whose downscoring is specified by policy.

### 11.2 Canonical Evaluation Procedure

```
Evaluate(ctx, CBGMODD, FAVORS, BERA, policy) → (status, RATE)

1.  If CBGMODD_valid = 0          → return (REJECT,  RATE=undefined, code=F1_GOV_NULL)
2.  If VerifyFAVORS(FAVORS,policy) = 0  → return (REJECT,  RATE=undefined, code=F2_BIO_NULL)
3.  If BERA_valid = 0             → return (REVIEW,  RATE with ⊥ on r2,r4,r6, code=F3_EVID_NULL)
4.  If Conflict(BERA, ctx) = 1    → return (REVIEW,  RATE with ⊥ on affected dims, code=F4_EVID_CONFLICT)
5.  Else:
      σ = HKDF-SHA256(BERA_bytes, nonce, "ERES-ECS-v1.0-sigma", 32)
      resolved = { SPL.Resolve(p, σ, ctx, lexicon) for p in referenced_primitives }
      rel_result = REL.evaluate(ctx, CBGMODD, FAVORS, BERA, resolved)
      if rel_result.critical_violations: return (REJECT, RATE=undefined, code=F5_REL_CRITICAL)
      RATE.vector = compute_dimensions(CBGMODD, FAVORS, BERA, resolved, rel_result, policy)
      RATE.score = mean(non_veiled(RATE.vector))
      RATE.provenance = {hashes, policy_id}
      RATE.audit_flags = rel_result.compliance_flags
      RATE.confidence = composite_confidence(CBGMODD, FAVORS, BERA, rel_result)
      return (ACCEPT, RATE)
```

### 11.3 Reference Scoring Functions

The following scoring functions are REFERENCE. Policies MAY substitute alternatives provided determinism, boundedness, and non-compensation are preserved.

Let:

```
g = CBGMODD_valid                                 (0 or 1)
b = mean of all MANDATORY channels in FAVORS      (in [0,1])
e = mean of (ari, eri, rhc, rci)                  (in [0,1])
```

Then:

```
r₁ = Score(0.35·g + 0.35·b + 0.30·e)              (transaction confidence)
r₂ = Score(b)                                      (biometric confidence)
r₃ = 10 if g=1 else ⊥                              (governance validity)
r₄ = Score((ari + eri) / 2)                        (contextual consistency)
r₅ = Score(SemanticClarity(ctx, resolved))         (semantic clarity)
r₆ = Score(rci)                                    (temporal persistence)
r₇ = Score(PolicyAlignment(ctx, rel_result))       (policy alignment)
```

where:

```
Score(x) = min(10, max(1, ceil(10 · x)))
```

maps `[0, 1]` into integers `{1..10}`.

### 11.4 Non-Compensation Enforcement

RCL MUST implement non-compensation at the vector level: `⊥` in any dimension whose policy-classification is `CRITICAL` invalidates the RATE for the requested authorization action. The critical-dimension set is policy-defined but MUST include `r₃` (governance validity) at minimum. This is the arithmetic realization of the conjunctive-gate requirement from the Trifecta Protocol (ERES-BRAINS-SPEC-2026-001).

### 11.5 Concrete Specifications of Previously-Placeholder Functions

v1.0 used five function names that were essentially placeholders: `Conflict(BERA, ctx)`, `SemanticClarity(ctx, resolved)`, `PolicyAlignment(ctx, rel_result)`, `compute_dimensions(...)`, and `composite_confidence(...)`. USE.ai's v1.0 critique identified this as the primary reason "two compliant implementations could still diverge materially." v1.1 specifies each function concretely below. Policies MAY override any of these with an alternative, provided (a) determinism is preserved, (b) the override is declared in policy metadata, and (c) the override is referenced in RATE.provenance.

#### 11.5.1 `Conflict(BERA, ctx) → {0, 1}`

```
Conflict(BERA, ctx):
  bera_vals   = [ari, eri, rhc, rci]
  max_pair    = max(bera_vals) - min(bera_vals)
  mean_b      = sum(bera_vals) / 4
  stdev_b     = sqrt(sum((x - mean_b)² for x in bera_vals) / 4)

  τ_pair      = policy.conflict.pairwise_tolerance  (default 0.25)
  τ_stdev     = policy.conflict.stdev_tolerance      (default 0.20)

  # ctx-state consistency check
  ctx_inconsistent = 0
  if ctx.declared_state == "high_coherence_required":
    if ari < 0.70 or rhc < 0.70:
      ctx_inconsistent = 1
  if ctx.declared_state == "stress_event":
    if ari > 0.90 and rhc > 0.90:   // suspiciously calm for declared stress
      ctx_inconsistent = 1

  return 1 if (max_pair > τ_pair
               OR stdev_b > τ_stdev
               OR ctx_inconsistent == 1)
         else 0
```

The defaults (0.25, 0.20) are set so that reasonable in-subject variation does not trigger REVIEW, while gross inconsistency (e.g., one index at 0.95 and another at 0.30) does. Policies MAY tighten or relax per deployment.

#### 11.5.2 `SemanticClarity(ctx, resolved) → [0, 1]`

```
SemanticClarity(ctx, resolved):
  N_ref      = |ctx.primitives_referenced|
  if N_ref == 0: return 1.0

  N_resolved = count of primitives in ctx.primitives_referenced
               that were successfully resolved (not ⊥)

  # per-reading lexicon confidence (lexicon may declare per-reading
  # confidence; default is 1.0 for single-reading resolution)
  mean_reading_conf = mean(lexicon.confidence(resolved[p])
                            for p in resolved)

  # structural discount: single-primitive contexts cannot
  # cross-corroborate, so cap at 0.8 unless ctx.corroboration_override is set
  if N_ref == 1 and not ctx.corroboration_override:
    structural_factor = 0.8
  else:
    structural_factor = 1.0

  return (N_resolved / N_ref) * mean_reading_conf * structural_factor
```

#### 11.5.3 `PolicyAlignment(ctx, rel_result) → [0, 1]`

```
PolicyAlignment(ctx, rel_result):
  priority = policy.alignment_priority   # e.g., {"CARE": 3, "BERC": 2, ...}
  scores   = rel_result.compliance_scores

  weighted_sum   = sum(scores[F] * priority[F] for F in priority)
  total_priority = sum(priority[F] for F in priority)

  return weighted_sum / total_priority
```

`policy.alignment_priority` MUST sum to a positive integer and each entry MUST be a non-negative integer. Fractional weights are prohibited to avoid floating-point non-determinism across implementations.

#### 11.5.4 `compute_dimensions(...)` — the canonical reference scoring

This function is the Section 11.3 scoring functions, applied as the **only normative** form in v1.1. The v1.0 "policies MAY substitute alternatives" clause is retained as a compatibility carve-out, but any substitution MUST (a) preserve determinism, boundedness, and non-compensation, and (b) be declared in RATE.provenance as `scoring_variant: "<name>"`. A RATE produced by a non-reference scoring variant MUST NOT be consumed by an oracle that requires the reference variant.

```
compute_dimensions(CBGMODD, FAVORS, BERA, resolved, rel_result, policy):
  g = 1 if CBGMODD_valid else 0
  b = mean(FAVORS[ch] for ch in policy.favors_mandatory_channels)
  e = mean([BERA.ari, BERA.eri, BERA.rhc, BERA.rci])

  r1 = Score(0.35*g + 0.35*b + 0.30*e)                   // transaction conf
  r2 = Score(b)                                           // biometric conf
  r3 = 10 if g == 1 else ⊥                                // governance valid
  r4 = Score((BERA.ari + BERA.eri) / 2)                   // contextual consistency
  r5 = Score(SemanticClarity(ctx, resolved))              // semantic clarity
  r6 = Score(BERA.rci)                                    // temporal persistence
  r7 = Score(PolicyAlignment(ctx, rel_result))            // policy alignment

  return [r1, r2, r3, r4, r5, r6, r7]

Score(x):
  import math
  return min(10, max(1, math.ceil(10 * x)))
```

#### 11.5.5 `composite_confidence(CBGMODD, FAVORS, BERA, rel_result) → [0, 1]`

```
composite_confidence(CBGMODD, FAVORS, BERA, rel_result):
  cbgmodd_cred_avg = mean(role.credibility for role in CBGMODD)

  favors_quorum_margin = mean(FAVORS[ch]
                              for ch in policy.favors_mandatory_channels)

  bera_mean = mean([BERA.ari, BERA.eri, BERA.rhc, BERA.rci])
              if BERA_valid else 0

  rel_confidence = rel_result.confidence

  # geometric mean enforces non-compensation: any one factor near zero
  # tanks the composite, which is the intended behavior
  factors = [cbgmodd_cred_avg, favors_quorum_margin, bera_mean, rel_confidence]
  if min(factors) == 0:
    return 0
  return (product(factors)) ** (1 / len(factors))
```

Geometric mean is chosen deliberately over arithmetic mean so that weak evidence in any one class cannot be compensated by strong evidence in another — this aligns `composite_confidence` with the Non-Compensation Claim (Section 15.3).

---

## 11A. Policy Language (ECS-POL v1.0)

USE.ai's v1.0 critique called for "a machine-readable schema, threshold grammar, critical-dimension declaration, lexicon authentication rules." Section 11A specifies the ECS Policy Language (ECS-POL v1.0), the artifact that makes two compliant implementations converge on the same RATE for the same inputs.

A policy is a JSON document conforming to the ECS-POL schema below. A conforming ECS implementation MUST load exactly one active policy per `policy_id`, MUST authenticate it per Section 11A.4, and MUST use its declared thresholds, weights, and rules throughout evaluation.

### 11A.1 JSON Schema (normative)

```json
{
  "$schema": "https://schemas.eresinstitute.org/ecs-pol/v1.0/policy.json",
  "type": "object",
  "required": ["policy_id", "version", "issuer", "issued_at",
               "cbgmodd", "favors", "bera", "rel",
               "rate", "lexicon", "signature"],
  "properties": {
    "policy_id":    { "type": "string", "format": "uri" },
    "version":      { "type": "string" },
    "issuer":       { "type": "string", "description": "DID or URL" },
    "issued_at":    { "type": "string", "format": "date-time" },
    "expires_at":   { "type": "string", "format": "date-time" },

    "cbgmodd": {
      "type": "object",
      "required": ["required_roles", "optional_roles", "min_credibility"],
      "properties": {
        "required_roles":  { "type": "array", "items": { "enum": ["C","B","G","M","O","D1","D2"] } },
        "optional_roles":  { "type": "array", "items": { "enum": ["C","B","G","M","O","D1","D2"] } },
        "min_credibility": { "type": "number", "minimum": 0, "maximum": 1 },
        "freshness_seconds": { "type": "integer", "minimum": 1 }
      }
    },

    "favors": {
      "type": "object",
      "required": ["mandatory_channels", "min_score_per_channel", "quorum"],
      "properties": {
        "mandatory_channels": {
          "type": "array",
          "items": { "enum": ["f","a","v","o","r","s"] }
        },
        "min_score_per_channel": { "type": "number", "minimum": 0, "maximum": 1 },
        "quorum": {
          "type": "object",
          "properties": {
            "type": { "enum": ["all_mandatory", "k_of_n"] },
            "k":    { "type": "integer", "minimum": 1, "maximum": 6 }
          }
        }
      }
    },

    "bera": {
      "type": "object",
      "required": ["min_indices_nonnull", "min_per_index", "sensor_spec"],
      "properties": {
        "min_indices_nonnull": { "type": "integer", "minimum": 1, "maximum": 4 },
        "min_per_index":       { "type": "number", "minimum": 0, "maximum": 1 },
        "sensor_spec":         { "type": "string", "description": "RG#404 version" },
        "conflict": {
          "type": "object",
          "properties": {
            "pairwise_tolerance": { "type": "number", "minimum": 0, "maximum": 1 },
            "stdev_tolerance":    { "type": "number", "minimum": 0, "maximum": 1 }
          }
        }
      }
    },

    "rel": {
      "type": "object",
      "required": ["rules", "thresholds", "alignment_priority"],
      "properties": {
        "rules": {
          "type": "array",
          "items": {
            "type": "object",
            "required": ["id", "family", "severity", "reason_code", "expression"],
            "properties": {
              "id":          { "type": "string" },
              "family":      { "enum": ["CARE","BERC","JERC","PERC","PAIN","COHERENCE"] },
              "severity":    { "enum": ["CRITICAL","MAJOR","MINOR"] },
              "reason_code": { "type": "string" },
              "expression":  { "type": "string",
                "description": "Threshold grammar expression, see 11A.2" }
            }
          }
        },
        "thresholds": {
          "type": "object",
          "properties": {
            "CARE":      { "type": "number" },
            "BERC":      { "type": "number" },
            "JERC":      { "type": "number" },
            "PERC":      { "type": "number" },
            "PAIN":      { "type": "number" },
            "COHERENCE": { "type": "number" }
          }
        },
        "alignment_priority": {
          "type": "object",
          "description": "Integer weights summing positive",
          "additionalProperties": { "type": "integer", "minimum": 0 }
        }
      }
    },

    "rate": {
      "type": "object",
      "required": ["critical_dimensions", "scoring_variant"],
      "properties": {
        "critical_dimensions": {
          "type": "array",
          "description": "Indices 1..7 that must NOT be VEILED for ACCEPT",
          "items": { "type": "integer", "minimum": 1, "maximum": 7 }
        },
        "scoring_variant": {
          "type": "string",
          "default": "reference-v1.1",
          "description": "Which compute_dimensions variant this policy uses"
        }
      }
    },

    "lexicon": {
      "type": "object",
      "required": ["uri", "hash", "hash_alg"],
      "properties": {
        "uri":       { "type": "string", "format": "uri" },
        "hash":      { "type": "string" },
        "hash_alg":  { "enum": ["SHA-256","SHA3-256","BLAKE3"] },
        "selector_variant": {
          "enum": ["default", "weighted"],
          "default": "default"
        }
      }
    },

    "replay": {
      "type": "object",
      "properties": {
        "window_seconds":  { "type": "integer", "minimum": 1 },
        "freshness_seconds": { "type": "integer", "minimum": 1 }
      }
    },

    "signature": {
      "type": "object",
      "required": ["alg", "signer", "value"],
      "properties": {
        "alg":    { "enum": ["Ed25519","ECDSA-P256","RSA-PSS-3072"] },
        "signer": { "type": "string" },
        "value":  { "type": "string" }
      }
    }
  }
}
```

### 11A.2 Threshold Grammar (normative)

REL rule `expression` fields use a restricted grammar that avoids subjective evaluation:

```
expression  := comparison | logical

comparison  := variable OP numeric_literal
            |  variable OP variable

variable    := "BERA." index      // ari | eri | rhc | rci
            |  "FAVORS." channel  // f | a | v | o | r | s
            |  "CBGMODD." field   // valid | role_count | mean_credibility
            |  "CTX." field       // declared_state | txn_type | subject_class
            |  "RESOLVED." primitive   // GCF | EDF | USC

OP          := "<" | "<=" | ">" | ">=" | "==" | "!="

logical     := "AND(" expression ("," expression)+ ")"
            |  "OR("  expression ("," expression)+ ")"
            |  "NOT(" expression ")"

numeric_literal := rational in [0, 1]     // no floating-point specials
```

Examples:

```
"BERA.ari >= 0.70"
"AND(FAVORS.f >= 0.85, FAVORS.r >= 0.85)"
"NOT(CTX.subject_class == protected AND RESOLVED.EDF == E2)"
```

An expression MUST evaluate deterministically. Strings MUST be NFC-normalized before comparison. Numeric comparison MUST use rational arithmetic or fixed-point at 6-decimal precision.

### 11A.3 Critical-Dimension Declaration

A policy MUST declare `rate.critical_dimensions` as a subset of `{1,2,3,4,5,6,7}`. The set MUST include at least `{3}` (governance validity). Common declarations:

| Use case                    | critical_dimensions |
|-----------------------------|---------------------|
| Civic attestation (minimum) | `[3]`               |
| UBIMIA disbursement         | `[3, 7]`            |
| VERTECA voice-command       | `[2, 3, 5]`         |
| GAIA SECUIR high-stakes     | `[1, 2, 3, 4, 7]`   |
| PlayNAC session authority   | `[3, 7]`            |

A VEILED in any critical dimension yields status = REVIEW (minimum) or REJECT (per policy).

### 11A.4 Lexicon Authentication Rules

The lexicon referenced by `lexicon.uri` MUST be content-addressed by `lexicon.hash` under `lexicon.hash_alg`. A conforming implementation MUST:

1. Fetch the lexicon from `lexicon.uri`;
2. Compute `HASH(lexicon_bytes)` under `lexicon.hash_alg`;
3. Compare byte-for-byte with `lexicon.hash`;
4. REFUSE to proceed on mismatch, returning status = ERROR with code `E_LEXICON_HASH_MISMATCH`.

The policy itself MUST be signed by `signature.signer` under `signature.alg`. The signature covers the canonical-encoded policy with the `signature.value` field blanked. A conforming implementation MUST verify this signature before admitting the policy as active.

### 11A.5 Policy Versioning and Rotation

A deployment MAY rotate policies at any time by issuing a new policy document with a different `policy_id` (or the same `policy_id` with a newer `version`). Implementations MUST NOT mix policies within a single Evaluate call. In-flight transactions that span a policy rotation MUST be completed under the policy active at transaction start.

---

## 12. Signature Layer (RSIG)

### 12.1 RSIG Contents

RSIG MUST include, at minimum:

```json
{
  "rsig": {
    "payload_hash":   "sha256:BASE64...",
    "rate_hash":      "sha256:BASE64...",
    "timestamp":      "2026-04-22T14:32:17.042Z",
    "nonce":          "BASE64...",
    "signer_identity":  "did:eres:engine:us-west-2:node-0341",
    "engine_identity":  "eres-ref-impl-v1.0.0",
    "policy_id":      "uri:eres:policy:2026:ubimia:v3",
    "compliance_flags": ["CARE_OK", "BERC_OK", "JERC_OK", "PERC_OK"],
    "hash_alg":       "SHA-256",
    "sig_alg":        "Ed25519",
    "signature":      "BASE64..."
  }
}
```

Requirements:

- `nonce` MUST be at least 128 bits from a cryptographically secure source.
- `timestamp` MUST be UTC in RFC 3339 format with millisecond precision.
- `signer_identity` MUST be a DID (Decentralized Identifier) or an equivalent globally-resolvable identifier.
- `signature` MUST cover the canonical-encoded concatenation of all preceding fields in declared order.

### 12.2 Signature Algorithms

A compliant implementation MUST support **Ed25519** (RFC 8032) as the baseline signature algorithm.

An implementation MAY additionally support:

- **ECDSA (P-256)** — NIST FIPS 186-5;
- **RSA-PSS (3072-bit minimum)** — PKCS #1 v2.2.

Post-quantum signature algorithms (Dilithium, Falcon, SPHINCS+) MAY be specified in a future minor version; they are OPTIONAL in v1.0.

### 12.3 Replay Protection

RSIG MUST carry a nonce and a timestamp. Verifiers MUST reject an RSIG whose `(nonce, signer_identity)` pair has been seen within the policy-defined replay window, or whose timestamp is outside the policy-defined freshness window.

---

## 13. Audit Persistence Layer (APL)

### 13.1 Append-Only Requirement

APL MUST be append-only or tamper-evident. Acceptable implementations:

- Merkle-tree anchored log with periodic root publication (RECOMMENDED);
- Distributed ledger (GraceChain, or equivalent);
- Signed append-only file system with external-witness counter-signing;
- Hardware-backed write-once storage.

### 13.2 Queryable Retrieval

A compliant APL MUST permit retrieval, given a transaction identifier, of:

- the canonical payload (or its hash plus a retrieval path);
- the RATE object;
- the RSIG;
- the verification timestamps and verifier identities;
- the policy identifier and its content-addressed hash.

### 13.3 Retention

APL retention MUST be at least seven years for civic-accounting transactions, or as otherwise specified by the governing jurisdiction under JERC constraints. Retention beyond the minimum MAY be subject to the 1000-Year Future Map horizon for GAIA-layer transactions.

### 13.4 Right-to-Know and Redaction

Individual subjects MUST be able to query their own transaction history. Redaction of payload contents (but never of RATE vectors or RSIGs) is PERMITTED for privacy protection under policy-specified rules. The fact of redaction MUST itself be recorded in APL.


---

## 14. Failure Modes and VEILED Semantics

ECS defines exactly **five primary failure modes**. Implementations MUST NOT add silent failure modes outside this enumeration; they MAY add sub-codes within these categories.

### 14.1 F1 — GOV-NULL (Governance Null)

**Condition:** `CBGMODD_valid = 0`. Required governance certification is absent, expired, credibility-threshold-failing, or signature-invalid.

**Output:** `status = REJECT`; `RATE = undefined`; reason code `F1_GOV_NULL`; violation details MUST include which REQUIRED roles were missing.

### 14.2 F2 — BIO-NULL (Biometric Null)

**Condition:** `VerifyFAVORS(FAVORS, policy) = 0`. Biometric policy requirements (mandatory channels, quorum, minimum scores) not met.

**Output:** `status = REJECT`; `RATE = undefined`; reason code `F2_BIO_NULL`; violation details MUST specify which channels failed and whether due to absence or insufficient confidence.

### 14.3 F3 — EVID-NULL (Evidence Null)

**Condition:** `BERA_valid = 0`. Contextual bio-electric evidence is insufficient (fewer than three of four indices are policy-threshold-meeting).

**Output:** `status = REVIEW`; RATE is returned with VEILED (`⊥`) in dimensions `r₂`, `r₄`, `r₆` (the BERA-dependent dimensions) and with numeric values in `r₁`, `r₃`, `r₅`, `r₇` where those are resolvable; reason code `F3_EVID_NULL`.

### 14.4 F4 — EVID-CONFLICT (Evidence Conflict)

**Condition:** `Conflict(BERA, ctx) = 1`. BERA indices are individually above threshold but their joint distribution is inconsistent with the declared context beyond policy tolerance (e.g., claimed stress state contradicts the measured HRV coherence).

**Output:** `status = REVIEW`; affected dimensions set to `⊥` or down-scored per policy; reason code `F4_EVID_CONFLICT`; evidence-conflict report attached.

### 14.5 F5 — REL-CRITICAL (Constraint Critical)

**Condition:** REL (Section 10) returned at least one critical violation.

**Output:** `status = REJECT`; `RATE = undefined`; reason code `F5_REL_CRITICAL`; full violation list attached; remediation pathway reference attached.

### 14.6 ERROR (Transport / Internal)

**Condition:** Implementation-internal failure (serialization error, signature-verification runtime error, hash-function unavailable, APL write failure). Not a protocol-level failure.

**Output:** `status = ERROR`; `RATE = undefined`; reason code `E_IMPL`; MUST NOT be retried without correcting the underlying condition.

### 14.7 VEILED vs. Zero — Prohibited Substitutions

The following substitutions are **compliance violations**:

- Treating `VEILED` as numeric `0` in any aggregation;
- Converting `VEILED` to `null` during downstream JSON stringification without explicit documentation;
- Computing `RATE.score` across VEILED positions as though they were zero;
- Passing a VEILED RATE to a downstream oracle without attaching `veiled_positions`;
- Re-running Evaluate with fabricated evidence to eliminate VEILED positions.

### 14.8 Status Enum

`status` MUST be one of:

- `ACCEPT` — transaction authorized;
- `REVIEW` — transaction routed to human reviewer;
- `REJECT` — transaction refused;
- `ERROR` — implementation fault, not a protocol decision.

---

## 15. Security Model

### 15.1 Adversary Goal

Forge a valid RATE vector, accompanied by a valid RSIG, that will be accepted by a consuming oracle without the adversary possessing legitimate attestations across all three evidence classes (CBGMODD, FAVORS, BERA).

### 15.2 Adversary Capabilities

The adversary MAY:

- Fully compromise one of the three evidence classes (e.g., clone biometrics of one subject, forge one governance-role signature, replay recorded BERA sensor outputs);
- Observe and attempt to replay prior RATE vectors and RSIGs;
- Attempt to substitute a declared intent for a different authenticated intent within a legitimate transaction;
- Coerce a single governance-role signer into attesting falsely;
- Interact with honest verifiers an unbounded number of times (Dolev–Yao with signature oracles).

The adversary MAY NOT, within the security claim:

- Simultaneously compromise all three evidence classes;
- Compromise the SHA-256 / SHA-3 / BLAKE3 hash function;
- Compromise the Ed25519 signature scheme;
- Compromise the append-only property of APL.

### 15.3 Security Claims

The following claims are the defensible core of ECS. They are stated narrowly and conditionally.

**Claim 1 — Key Completeness.**
Compromise of any one of the three evidence classes (CBGMODD alone, FAVORS alone, or BERA alone) is insufficient to produce an ACCEPT status with a fully-resolved RATE. Compromise of any two without the third yields at best a REVIEW status with VEILED dimensions from the uncompromised class.

*Conditions:* REL constraint checks are not bypassed; RSIG signature verification is correct; all three evidence classes' independence is preserved by deployment (no single party operates all three).

**Claim 2 — Intent Binding.**
The resolved plaintext from polysemantic primitives (GCF, EDF, USC) is cryptographically bound to σ, which is bound to BERA, which is part of the canonical payload hash, which is covered by RSIG. An adversary cannot claim intent `I` unless σ (derived from genuine BERA evidence) selects `I` under the policy lexicon.

*Conditions:* HKDF is a secure KDF; BERA sensor pipeline is not compromised; policy lexicon is authenticated.

**Claim 3 — Non-Compensation.**
RATE dimensions do not compensate for each other during authorization. `⊥` in any critical dimension invalidates the vector. No weighted-sum authorization rule that could hide `⊥` is permitted (Section 7.3, Section 11.4).

*Conditions:* The consuming oracle conforms to Section 4.7 and Section 7.3.

**Claim 4 — Operational Binding.**
A RATE vector is meaningless in isolation. A conforming implementation MUST route every RATE to a registered consuming oracle (UBIMIA, NBERS, PlayNAC, VERTECA) via a bound channel that re-verifies RSIG before action.

*Conditions:* Consuming oracles implement the verification handshake of Section 19.

**Claim 5 — Replay Resistance.**
A RATE+RSIG pair cannot be successfully replayed outside the policy-defined freshness window or against a different policy_id, because the nonce and policy_id are covered by the signature.

*Conditions:* Verifiers correctly implement the `(nonce, signer_identity)` replay-window cache.

### 15.4 Threat Model Exclusions (Explicit)

ECS does **not** protect against:

- Wire-level eavesdropping of plaintext (use TLS);
- Coercion of the subject (handled at the human-review layer, not cryptographically);
- Long-term wholesale governance capture (outside cryptographic scope; addressed by CCAL and Hague-layer governance);
- Hardware-level side-channel attacks on signing devices (use hardware-hardened signers);
- Denial of service against APL (use redundant APL backends);
- Quantum adversaries against Ed25519 / SHA-256 (use post-quantum algorithms when standardized in a future ECS version).

### 15.5 Honest Majority Assumption Is NOT Required

Unlike many consensus-based systems, ECS does not assume an honest majority of verifiers. A single honest verifier with access to the canonical payload, RATE, and RSIG can independently verify the entire computation. This is a consequence of the deterministic-evaluation property (Section 3.1).

### 15.6 Protocol Guarantees vs. Governance-Policy Guarantees (normative separation)

USE.ai's v1.0 critique correctly noted that several v1.0 claims combined two different kinds of assurance: those that follow from ECS's cryptographic mechanics alone, and those that additionally require a sound governance policy. v1.1 separates them explicitly. Readers, reviewers, and institutional consumers of ECS output MUST understand which column a given claim lives in.

| # | Claim                                  | Type                    | What it depends on                              |
|---|----------------------------------------|-------------------------|--------------------------------------------------|
| 1 | Key Completeness                       | Protocol (cryptographic) | Signatures + hash + deployment independence      |
| 2 | Intent Binding (identity of σ→reading) | Protocol (cryptographic) | HKDF + payload hash coverage by RSIG             |
| 2a| Semantic meaningfulness of σ→reading   | **Governance**          | Policy-declared lexicon and selector variant     |
| 3 | Non-Compensation                       | Protocol (cryptographic) | Downstream consumer conforms to §7.3 and §11.4   |
| 4 | Operational Binding                    | Protocol (cryptographic) | Consuming oracle implements §19 handshake        |
| 5 | Replay Resistance                      | Protocol (cryptographic) | Verifier implements (nonce, signer) cache        |
| 6 | REL constraint correctness             | **Governance**          | Rules, severities, and thresholds in policy      |
| 7 | Non-discrimination of outcomes         | **Governance**          | JERC rule quality in policy                      |
| 8 | Ecological protection                  | **Governance**          | BERC rule quality in policy                      |
| 9 | Restorative vs. punitive routing       | **Governance**          | Non-Punitive Remediation policy wiring           |
| 10 | Non-coercion of subjects              | **Governance + out-of-band** | REL critical-bar + human-review layer       |

Claims 1–5 are **protocol guarantees**: they hold provided the named cryptographic primitives are sound and the named implementation conditions are met. They do not depend on policy content.

Claims 2a, 6–10 are **governance-policy guarantees**: they hold *only if* the active policy is itself well-designed. ECS enforces that a policy be well-specified, signed, lexicon-authenticated, and conformant to the schema (Section 11A). ECS does not and cannot enforce that a policy be *wise*. A deployment that ships ECS with a malicious or negligent policy has a cryptographically-sound channel for enforcing a malicious or negligent decision. The CARE Ethical Clause (Section 23) is the institutional backstop for this gap, but it is an institutional backstop, not a cryptographic one.

This separation is the honest answer to "what is ECS worth?" — answer: it is cryptographically worth Claims 1–5, and institutionally worth the quality of policy that governs it.


---

## 16. Threat Model

### 16.1 Attack Surface

| Attack                              | ECS Defense                                     | Residual Risk |
|-------------------------------------|-------------------------------------------------|---------------|
| Replay of prior RATE+RSIG           | Nonce + timestamp + replay window               | Clock drift outside window |
| Forged CBGMODD role participation   | Ed25519 over canonical hash per role            | Private-key compromise |
| FAVORS biometric cloning (one channel) | Multi-channel quorum; live-capture requirement | Multi-channel correlated spoof |
| BERA sensor replay                  | BERA_bytes covered by payload hash + nonce      | Sensor supply-chain compromise |
| Payload mutation in transit         | Canonical hash covered by RSIG                  | Compromise of hash function |
| Semantic collision                  | Primitive family + reading index in payload     | Lexicon-level ambiguity |
| Compromised resonance engine        | engine_identity in RSIG; external witness       | Unknown-unknown bugs |
| Bribery / capture of single signer  | Role quorum per CBGMODD policy                  | Capture of full required set |
| Coerced compliance                  | REL critical-violation bar + REVIEW routing     | Coercion of REL authority |
| Scalar-collapse attack downstream   | Section 7.3 prohibition + vector-level API      | Non-conformant consumer |

### 16.2 Deployment Independence Requirement

For Claim 1 (Key Completeness) to hold in practice, the three evidence classes MUST be operationally independent:

- CBGMODD signers SHOULD NOT be the same entity as BERA sensor operators;
- FAVORS capture devices SHOULD NOT share vendor supply chains with BERA sensors;
- Policy authorities SHOULD NOT control more than one evidence class.

Deployments that concentrate evidence classes under a single operational authority degrade Claim 1 to a weaker joint-trust assumption.

### 16.3 Adversarial Auditing

ECS deployments SHOULD undergo periodic adversarial auditing. The MIEVM ensemble (Claude, DeepSeek, ChatGPT, Grok) is the reference adversarial review body for the ERES reference implementation; deployments MAY designate equivalent adversarial-review authorities.

---

## 17. Implementation Requirements

### 17.1 Mandatory Definitions (per deployment)

A conforming implementation MUST define and publish:

- Exact wire formats for CBGMODD, FAVORS, BERA (extending Sections 6.1–6.3 where policy requires);
- Normalization rules producing values in `[0, 1]`;
- Channel thresholds for FAVORS;
- Quorum policy for FAVORS;
- Conflict tolerance for `Conflict(BERA, ctx)`;
- RATE scoring functions (either the Section 11.3 reference set or declared alternatives);
- Policy lexicon for SPL primitive resolution;
- Replay window duration;
- Freshness window duration;
- APL backend and retention policy;
- Reviewer escalation rules for REVIEW-status cases.

### 17.2 Prohibited Behaviors

A conforming implementation MUST NOT:

- Silently replace `⊥` (VEILED) with `0` or any other value during aggregation;
- Collapse RATE to a single scalar for authorization (Section 7.3);
- Use undefined semantic labels in place of policy-lexicon readings (Section 9.3);
- Claim cryptographic guarantees not delivered by underlying signatures, hashes, or transport;
- Skip REL critical-violation checks under any circumstance;
- Accept a RATE for downstream action without re-verifying RSIG;
- Store BERA raw sensor streams unencrypted at rest;
- Log σ in cleartext.

### 17.3 Reference Implementation

The ERES Institute SHALL maintain a reference implementation under the URI:

```
https://github.com/ERES-Institute-for-New-Age-Cybernetics/eres-crypto-ref
```

The reference implementation is released under CCAL v2.1 (code layer: MIT-equivalent per CCAL layered stack).

---

## 18. MIEVM Validation Requirements

A conforming implementation MUST pass the following four MIEVM validation tests before claiming ECS compliance. Each test is defined against the reference implementation's test harness.

### 18.1 Test 1 — Key-Fragment Independence

**Setup:** Three evaluation runs. In each run, exactly one evidence class is fully compromised (adversary-controlled) and the other two are honest.

**Pass condition:** No run produces an ACCEPT status with a fully-resolved RATE. All three runs produce either REJECT or REVIEW with VEILED on the compromised-class-dependent dimensions.

### 18.2 Test 2 — VEILED vs. Arithmetic Zero

**Setup:** A contrived input where BERA fails validation (`BERA_valid = 0`) but CBGMODD and FAVORS pass.

**Pass condition:** RATE is returned with `⊥` (VEILED) on `r₂`, `r₄`, `r₆`. Downstream consuming oracle refuses authorization. Specifically, `RATE.score` computation MUST skip VEILED positions, not treat them as 0. A separate regression check verifies that the same inputs with BERA = (0, 0, 0, 0) (valid-but-zero) produces a numeric `r₂`, `r₄`, `r₆` of 1, not VEILED.

### 18.3 Test 3 — Operational Binding

**Setup:** A valid ACCEPT RATE+RSIG is captured. The adversary attempts to present it to a consuming oracle directly without the verification handshake.

**Pass condition:** The consuming oracle refuses to act on the RATE. The oracle's verification handshake MUST include RSIG re-verification, nonce/replay-window check, and policy_id match.

### 18.4 Test 4 — Determinism

**Setup:** The same `(ctx, CBGMODD, FAVORS, BERA, policy)` inputs are fed to two independent compliant engine instances.

**Pass condition:** Both engines produce byte-identical canonical payloads, identical σ values, identical resolved primitives, identical RATE vectors, identical RATE.provenance, and RSIGs that differ only in signer_identity, timestamp, nonce, and signature. All other fields MUST match exactly.

### 18.5 MIEVM Ensemble Review

In addition to the programmatic tests above, the ECS specification itself is subject to MIEVM ensemble review by Claude, DeepSeek, ChatGPT, and Grok. Disagreements among the ensemble produce issues in the ERES-CRYPTO-STD issue tracker and SHALL be resolved before a specification minor or major version bump.

---

## 19. Interoperability

### 19.1 PlayNAC

A compliant ECS implementation SHOULD expose the RATE object as a PlayNAC-readable artifact. PlayNAC consumers of RATE MUST:

- Verify RSIG;
- Check policy_id against the PlayNAC game/session policy;
- Reject any RATE with VEILED on `r₇` (policy alignment) for actions that require explicit policy authorization;
- Record the RATE in the PlayNAC session ledger.

### 19.2 VERTECA (Voice Portal)

VERTECA is the canonical voice-to-meaning layer of the GAIA organism. VERTECA-originated transactions:

- Deposit utterance hash, SOUND-resolved word sequence, and Keyword Ontology tags into SPL (Section 9.4);
- Contribute the FAVORS-V (voice) confidence directly;
- Trigger BERA-sensor activation via the BRAINS cognitive organ (ERES-BRAINS-SPEC-2026-001);
- Consume RATE for voice-command authorization with hard dependence on `r₂` (biometric) and `r₅` (semantic clarity).

### 19.3 UBIMIA

UBIMIA (merit-based Universal Basic Income) disbursements MUST reference an ECS RATE for each disbursement event. UBIMIA consumers:

- MUST require `r₇ ≥ 8` (policy alignment) and no VEILED on `r₃` (governance validity);
- MUST record the RATE hash in the GraceChain / Meritcoin ledger entry;
- MAY use `r₁` (transaction confidence) as a modulator on disbursement size under a policy-specified curve.

### 19.4 NBERS

NBERS (National Bio-Ecologic Resource Score) integrations MUST feed BERA evidence through BERC constraint evaluation in REL (Section 10.1 family 2). An NBERS-relevant transaction MUST NOT ACCEPT if BERC constraints fail, regardless of other RATE dimensions.

### 19.5 GAIA

The GAIA organism integrates ECS at the SECUIR (energy–security) layer. GAIA's BRAINS (cognitive organ, Trifecta Protocol: ONE-GOOD, SECURITY-CLEARANCE, DATA-INTEGRITY gates) maps to ECS as:

| GAIA Gate (BRAINS)    | ECS Correspondent                                |
|-----------------------|--------------------------------------------------|
| ONE-GOOD              | REL — CARE + PAIN + JERC constraint families     |
| SECURITY-CLEARANCE    | CBGMODD validity + FAVORS quorum + RSIG          |
| DATA-INTEGRITY        | CEL canonical hash + APL tamper-evidence         |

The GAIA BODY substrate (ERES-BODY-SPEC-2026-001, Consolidation pipeline feeding VERTECA) is the data layer that carries ECS payloads. ECS is SECUIR's attestation cryptography; BODY is its data skeleton; BRAINS is its cognitive gate authority; VERTECA is its voice interface.

### 19.6 EDF Framework

The three-variant EDF lock is honored through the EDF primitive family in SPL (Section 9.2):

- `E₁` → Earned Dignity Framework (consumed by the ONE-GOOD gate);
- `E₂` → Earth Defense / Federation (consumed by the SECURITY-CLEARANCE gate);
- `E₃` → Earth Data Framework (consumed by the DATA-INTEGRITY gate).

σ-driven selection from `{E₁, E₂, E₃}` is what routes a transaction to the appropriate Trifecta gate.


---

## 20. Test Vectors

This section provides **byte-normative** test vectors. A compliant implementation MUST reproduce these outputs byte-for-byte. Every hash, signature, σ value, and canonical JSON string below has been computed and verified against a reference implementation. Formal extended test vectors will be published as **ERES-CRYPTO-TEST-2026-001**.

### 20.0 Test-Vector Fixtures (apply to all vectors)

**Test keypair.** All test-vector signatures use a single Ed25519 keypair whose seed is derived deterministically:

```
seed = SHA-256(UTF-8 bytes of "ERES-CRYPTO-STD-2026-001-v1.1-TEST-KEY-C")
seed (hex) = f2f794def2ea5d19ecb0f894716932654eb173195c451b2cccb9770ab2874691
public key (raw, hex) = 04e552e2c8ee4d34be854a1ca808600183f0afcfa8a4d063eb7c1e1bb7fecf68
```

Implementations verifying these test vectors MUST reconstruct the keypair from the seed above.

**Test nonce.** `nonce_hex = 00112233445566778899aabbccddeeff` (16 bytes = 128 bits). Base64: `ABEiM0RVZneImaq7zN3u/w==`.

**Test timestamp (for RSIG determinism).** `2026-04-22T14:32:17.042Z`.

**Canonical JSON rules (applied throughout).** Keys sorted lexicographically, no whitespace between tokens, UTF-8 NFC, floats encoded to 6-decimal precision. This matches Section 8.1.

### 20.1 Test Vector A — Minimal Citizen Transaction (ACCEPT path)

**Inputs (before signing):**

```json
{
  "ctx": {
    "txn_id": "txn-000001",
    "policy_id": "uri:eres:policy:2026:test:v1",
    "primitives_referenced": ["GCF"],
    "nonce": "ABEiM0RVZneImaq7zN3u/w=="
  },
  "cbgmodd": [
    {
      "role": "C",
      "weight": 1.00,
      "credibility": 0.80,
      "attested_at": "2026-04-22T14:30:00Z"
    }
  ],
  "favors": {
    "f": 0.92, "a": 0.88, "v": 0.95,
    "o": null, "r": 0.90, "s": 0.87
  },
  "bera": {
    "ari": 0.84, "eri": 0.79, "rhc": 0.91, "rci": 0.82,
    "sensor_spec": "RG#404-v1.0",
    "window_seconds": 30
  }
}
```

**Active policy** (summary; full schema per Section 11A):

- CBGMODD: `required_roles: ["C"]`, `min_credibility: 0.70`.
- FAVORS: `mandatory_channels: ["f","a","v","r","s"]`, `min_score_per_channel: 0.85`, quorum `k_of_n` with `k=4`.
- BERA: `min_indices_nonnull: 3`, `min_per_index: 0.70`, `conflict.pairwise_tolerance: 0.25`, `conflict.stdev_tolerance: 0.20`.
- REL: all six families PASS; `alignment_priority: {CARE:3, BERC:2, JERC:3, PERC:1, PAIN:2, COHERENCE:2}`.
- RATE: `critical_dimensions: [3]`, `scoring_variant: "reference-v1.1"`.

**Step 1 — CBGMODD role-C signature.**

The role-record canonical input (canonical JSON, with sorted keys, no whitespace):

```
{"attested_at":"2026-04-22T14:30:00Z","credibility":0.8,"role":"C","txn_id":"txn-000001","weight":1.0}
```

Ed25519 signature over those bytes, base64-encoded:

```
Xyzl53Zs4EqayDQtU0AbaXUSopeVBRDu/dAN9TrulCKmdMulOKYPNjWh/WK9ZH1fftKMQf+IGBUZBUi7WZ3oBg==
```

The signature field is then added to the role record as `"signature": "ed25519:..."`.

**Step 2 — Canonical payload hash.**

The full canonical payload (with the role signature inserted), as exactly 510 UTF-8 bytes:

```
{"bera":{"ari":0.84,"eri":0.79,"rci":0.82,"rhc":0.91,"sensor_spec":"RG#404-v1.0","window_seconds":30},"cbgmodd":[{"attested_at":"2026-04-22T14:30:00Z","credibility":0.8,"role":"C","signature":"ed25519:Xyzl53Zs4EqayDQtU0AbaXUSopeVBRDu/dAN9TrulCKmdMulOKYPNjWh/WK9ZH1fftKMQf+IGBUZBUi7WZ3oBg==","weight":1.0}],"ctx":{"nonce":"ABEiM0RVZneImaq7zN3u/w==","policy_id":"uri:eres:policy:2026:test:v1","primitives_referenced":["GCF"],"txn_id":"txn-000001"},"favors":{"a":0.88,"f":0.92,"o":null,"r":0.9,"s":0.87,"v":0.95}}
```

```
SHA-256(canonical_payload) = 2f751f1bf59d5a2b7b5682e280bcc523bd0ea7384433a9814d8deebc821d7acd
Base64:                      L3UfG/WdWit7VoLigLzFI70OpzhEM6mBTY3uvIIdes0=
```

**Step 3 — σ derivation (HKDF-SHA256).**

BERA canonical bytes (for HKDF secret):

```
{"ari":0.84,"eri":0.79,"rci":0.82,"rhc":0.91,"sensor_spec":"RG#404-v1.0","window_seconds":30}
```

```
σ = HKDF-SHA256(
      secret = BERA canonical bytes above,
      salt   = nonce (16 bytes 00112233...eeff),
      info   = "ERES-ECS-v1.0-sigma" (UTF-8, 20 bytes),
      L      = 32
    )

σ (hex) = e43732833d50a0502dab120d33fa05537bb4a069957f3aba293ebe62aba50ad7
```

**Step 4 — GCF primitive resolution.**

```
σ[0..3] = 0xe4373283
int(σ[0..3], big_endian) = 3828822659
3828822659 mod 3         = 2
GCF readings             = [G1, G2, G3]
Resolved                 = G3
```

**Step 5 — REL evaluation (per policy).**

All six families return PASS with compliance scores:

```
compliance_scores = {
  "CARE":      0.98,
  "BERC":      0.92,
  "JERC":      0.95,
  "PERC":      0.90,
  "PAIN":      0.99,
  "COHERENCE": 1.00
}
confidence = 0.94
critical_violations = []
```

**Step 6 — RATE computation (compute_dimensions per Section 11.5.4).**

```
g = 1                (CBGMODD_valid, role C credibility 0.80 ≥ 0.70)
b = mean(0.92, 0.88, 0.95, 0.90, 0.87) = 0.904000
e = mean(0.84, 0.79, 0.91, 0.82)       = 0.840000

Conflict(BERA, ctx):
  stdev(BERA)       = 0.044159   (≤ 0.20, passes)
  max pairwise diff = 0.120000   (≤ 0.25, passes)
  → Conflict = 0

SemanticClarity(ctx, resolved):
  N_ref = 1, N_resolved = 1, mean_reading_conf = 1.0
  structural_factor = 0.8 (single-primitive, no corroboration override)
  → 0.800000

PolicyAlignment(ctx, rel_result):
  Σ(score_F × priority_F) / Σ(priority_F)
  = (0.98·3 + 0.92·2 + 0.95·3 + 0.90·1 + 0.99·2 + 1.00·2) / 13
  = 12.51 / 13
  = 0.962308

r1 = Score(0.35·1 + 0.35·0.904 + 0.30·0.840) = Score(0.918400) = ceil(9.184)  = 10
r2 = Score(0.904000)                                             = ceil(9.040)  = 10
r3 = 10                                                           (g = 1)
r4 = Score((0.84 + 0.79) / 2) = Score(0.815000)                  = ceil(8.150) =  9
r5 = Score(SemanticClarity)   = Score(0.800000)                  = ceil(8.000) =  8
r6 = Score(0.82)                                                 = ceil(8.200) =  9
r7 = Score(PolicyAlignment)   = Score(0.962308)                  = ceil(9.623) = 10

RATE.vector = [10, 10, 10, 9, 8, 9, 10]
```

**Step 7 — composite_confidence (geometric mean, Section 11.5.5).**

```
factors = [cbgmodd_cred_avg=0.80, favors_quorum_margin=0.904,
           bera_mean=0.840, rel_confidence=0.94]
composite_confidence = (0.80 × 0.904 × 0.840 × 0.94) ^ (1/4)
                     = 0.869293
```

**Step 8 — RATE.score.**

```
RATE.score = mean([10, 10, 10, 9, 8, 9, 10]) = 66/7 = 9.428571
```

**Step 9 — Full RATE object.**

```json
{
  "rate": {
    "vector": [10, 10, 10, 9, 8, 9, 10],
    "score": 9.428571,
    "provenance": {
      "cbgmodd_hash": "sha256:gFVn6fIKVaqQJKYEC5JlzRDFXdTc0o2YKxc5r+yHkZo=",
      "favors_hash":  "sha256:CRoIuJS8MJ2zVEHxIZArHoJnxXVc9R8UsNARGYY4s2o=",
      "bera_hash":    "sha256:lJMyxWApw1Mr4PX3mUcDLvo/5Tryj51x5X981CGNsDw=",
      "policy_id":    "uri:eres:policy:2026:test:v1"
    },
    "audit_flags": ["CARE_OK", "BERC_OK", "JERC_OK", "PERC_OK"],
    "confidence": 0.869293,
    "veiled_positions": []
  }
}
```

**Step 10 — RSIG.**

Signed-field canonical bytes (signature field excluded, other fields in lexicographic order):

```
{"compliance_flags":["CARE_OK","BERC_OK","JERC_OK","PERC_OK"],"engine_identity":"eres-ref-impl-v1.1.0-test","hash_alg":"SHA-256","nonce":"ABEiM0RVZneImaq7zN3u/w==","payload_hash":"sha256:L3UfG/WdWit7VoLigLzFI70OpzhEM6mBTY3uvIIdes0=","policy_id":"uri:eres:policy:2026:test:v1","rate_hash":"sha256:bYyyB/IRKu7hEm9lMj2aD4Os0kQ1VI9ygF1LfEN9LAA=","sig_alg":"Ed25519","signer_identity":"did:eres:test:engine:0001","timestamp":"2026-04-22T14:32:17.042Z"}
```

Ed25519 signature (with the test keypair from Section 20.0), base64:

```
fhQv4ZDgfNkkA0iXVEo/ePzYUZxuYiVnKWAxgKJ7s1N08M0hYRQmVjn1rNHlMJErdYN3oJ/amQ9AUTDiZlNuBQ==
```

**Final Status:** `ACCEPT`.

All intermediate and final bytes above are verifiable against the test keypair and have been confirmed to verify in the reference implementation (see `tests/vectors/test_vector_a.json` in the ref repo).

### 20.2 Test Vector B — BERA Insufficient (REVIEW path)

**Inputs:** As Test Vector A, but with `bera.ari = 0.50, bera.eri = 0.40, bera.rhc = null, bera.rci = 0.60`.

**Policy evaluation:**

- Only two of four BERA indices are non-null AND ≥ 0.70 threshold (ari=0.50 and eri=0.40 and rci=0.60 all fail; rhc is null).
- `BERA_valid = 0` (fewer than the required three qualifying indices).
- Triggers F3 — EVID-NULL (Section 14.3).

**Expected output:**

```json
{
  "status": "REVIEW",
  "code":   "F3_EVID_NULL",
  "rate": {
    "vector": [
      <r1-partial-numeric>,
      "VEILED",
      10,
      "VEILED",
      <r5-numeric>,
      "VEILED",
      <r7-numeric>
    ],
    "veiled_positions": [2, 4, 6],
    "audit_flags": ["CARE_OK", "BERC_UNDETERMINED"],
    "confidence": 0.0
  }
}
```

`confidence = 0.0` because `composite_confidence` uses geometric mean and `bera_mean_valid = 0` when `BERA_valid = 0`.

### 20.3 Test Vector C — CBGMODD Signature Forged (REJECT path)

**Inputs:** As Test Vector A, but `cbgmodd[0].signature` is tampered (one byte flipped from the Step 1 value).

**Expected output:**

```json
{
  "status": "REJECT",
  "code":   "F1_GOV_NULL",
  "rate":   null,
  "violations": [
    {
      "role": "C",
      "reason_code": "CBGMODD_SIGNATURE_INVALID"
    }
  ]
}
```

### 20.4 Test Vector D — Evidence Conflict (REVIEW path)

**Inputs:** As Test Vector A, but with `bera.ari = 0.95, bera.eri = 0.50, bera.rhc = 0.90, bera.rci = 0.55`.

**Policy evaluation:**

- All four indices are non-null and above 0.70? No — eri=0.50 and rci=0.55 fail; so actually BERA_valid would fail first. For this vector, assume `policy.bera.min_per_index = 0.40` instead, so all four pass the per-index threshold.
- max pairwise diff = 0.95 - 0.50 = 0.45 > τ_pair (0.25).
- `Conflict(BERA, ctx) = 1`.
- Triggers F4 — EVID-CONFLICT (Section 14.4).

**Expected output:**

```json
{
  "status": "REVIEW",
  "code":   "F4_EVID_CONFLICT",
  "rate": {
    "vector": [...with VEILED on r4, r6 per policy...],
    "veiled_positions": [3, 5],
    "conflict_report": {
      "max_pairwise_diff": 0.45,
      "stdev":             "<computed>",
      "ctx_inconsistent":  false
    }
  }
}
```

### 20.5 Test Vector E — Determinism

**Setup:** Test Vector A inputs fed to two independent compliant engine instances.

**Expected:** Byte-identical canonical payloads (both compute exactly the 510-byte canonical form in Step 2); identical payload SHA-256 (`2f751f...7acd`); identical σ (`e43732...0ad7`); identical resolved primitive (`G3`); identical RATE.vector (`[10, 10, 10, 9, 8, 9, 10]`); identical RATE.score (`9.428571`); identical RATE.confidence (`0.869293`). RSIGs will differ only in `signer_identity` (if engines use different DIDs), `timestamp` (real wall-clock), `nonce` (real randomness), and `signature` (follows from the prior three). All other RSIG fields MUST match byte-for-byte.

### 20.6 Test Vector F — Weighted SPL Selector (normative, v1.1.1)

This vector is the conformance check for the v1.1.1 integer-arithmetic weighted selector (§9.3.3). Any compliant v1.1.1 implementation MUST produce the resolved reading below under the specified inputs. Floating-point implementations that happen to produce the same result on one architecture but diverge on another are NOT compliant.

**Inputs:**

- σ reused from Test Vector A: `e43732833d50a0502dab120d33fa05537bb4a069957f3aba293ebe62aba50ad7`
- Primitive family: GCF (readings `[G1, G2, G3]`, indices 0, 1, 2)
- Policy-declared integer weights: `w = [2, 4, 1]`
- Selector variant: `"weighted"`
- Context: reparations-framing transaction (weights computed by policy function `W(ctx)`)

**Normative computation (integer arithmetic only):**

```
p      = int(σ[0..7], big_endian)
       = int(0xe43732833d50a050, BE)
       = 16,444,668,103,617,454,160

W_sum  = 2 + 4 + 1 = 7
cum[0] = 2
cum[1] = 6
cum[2] = 7

2⁶⁴    = 18,446,744,073,709,551,616

p × W_sum  = 16,444,668,103,617,454,160 × 7
           = 115,112,676,725,322,179,120

i = 0:  p × W_sum = 115,112,676,725,322,179,120
        cum[0] × 2⁶⁴ = 2 × 18,446,744,073,709,551,616
                     =    36,893,488,147,419,103,232
        Is p × W_sum ≤ cum[0] × 2⁶⁴?  NO  (115e18 > 36e18)
        Continue.

i = 1:  p × W_sum = 115,112,676,725,322,179,120
        cum[1] × 2⁶⁴ = 6 × 18,446,744,073,709,551,616
                     =   110,680,464,442,257,309,696
        Is p × W_sum ≤ cum[1] × 2⁶⁴?  NO  (115e18 > 110e18)
        Continue.

i = 2:  p × W_sum = 115,112,676,725,322,179,120
        cum[2] × 2⁶⁴ = 7 × 18,446,744,073,709,551,616
                     =   129,127,208,515,966,861,312
        Is p × W_sum ≤ cum[2] × 2⁶⁴?  YES  (115e18 ≤ 129e18)
        SELECT i = 2.
```

**Normative output:**

```
resolved_reading = readings[2] = "G3"
```

**RATE.provenance addition** when weighted selector is in use:

```json
{
  "provenance": {
    "selector_variant": "weighted",
    "weights_applied":  [2, 4, 1]
  }
}
```

**Why this test matters.** On a naively-coded floating-point implementation, `u = p / 2⁶⁴` and `cdf[0] = cum[0] / W_sum` may both be representable with small but non-zero rounding errors that depend on the platform's IEEE 754 mode, the compiler's FMA settings, and the order of operations. A particular σ and weight combination could select reading `i` on x86_64 and reading `i+1` on ARM. The integer form above has no such failure mode: every arithmetic operation is exact, every comparison is unambiguous, and the output is identical across architectures, implementation languages, and compilers. This is what conformance to §18.4 (MIEVM Determinism Test) requires for the weighted selector.

**Boundary case (informative).** If an implementer wishes to test the boundary, set `p_boundary = cum[0] × 2⁶⁴ / W_sum` (integer division). Under integer arithmetic, `p_boundary × W_sum ≤ cum[0] × 2⁶⁴` holds exactly; `(p_boundary + 1) × W_sum > cum[0] × 2⁶⁴` holds exactly. These two adjacent inputs MUST produce different selections (index 0 vs. index 1) on every compliant implementation. This is the test that catches floating-point non-determinism because a float implementation can make `p_boundary / 2⁶⁴` equal-or-greater-than `cum[0] / W_sum` due to rounding, misclassifying the boundary input.

---

## 21. Compliance

A system is **ECS-Compliant (v1.0)** if and only if it:

1. Implements the full six-layer stack (Sections 8–13);
2. Preserves canonical encoding invariants (Section 8);
3. Computes RATE per the canonical equation and reference scoring functions, or declared conformant alternatives (Sections 7, 11);
4. Produces RSIG per Section 12 with Ed25519 at minimum;
5. Preserves provenance vectors end-to-end;
6. Supports tamper-evident audit persistence (Section 13);
7. Rejects scalar collapse in both its own outputs and in its downstream API surface (Section 7.3);
8. Treats VEILED (`⊥`) as a distinct value through the full pipeline (Section 14.7);
9. Passes all four MIEVM validation tests (Section 18);
10. Honors the Ethical Clause (Section 23).

A system that satisfies (1)–(9) but not (10) is **NOT** ECS-Compliant. The Ethical Clause is cryptographically non-optional.

---

## 22. Governance and Versioning

### 22.1 Version Semantics

ECS versions follow `MAJOR.MINOR.PATCH`:

- **MAJOR** — structural breaking change (e.g., RATE vector dimensionality change, canonical equation change, primitive family set change);
- **MINOR** — compatible extension (e.g., new scoring functions, new signature algorithms, new test vectors that do not invalidate prior ones);
- **PATCH** — editorial, clarifying, or bug-fix refinements that preserve semantics. A PATCH MAY change implementation-level behavior in paths that were previously ambiguous or non-deterministic, provided the intended semantics are preserved and any already-conforming implementation continues to conform. v1.1.1's integer-arithmetic weighted-selector fix is the canonical example: it fixes a determinism bug in a path (weighted SPL selection) that was not yet in widespread use, while preserving byte-identical output for the default selector and for all previously-specified test vectors.

### 22.2 Standards Authority

The ERES Institute for New Age Cybernetics SHALL serve as the initial custodial authority for ECS. Successor authority MAY be designated under the ERES Equity Covenant (ERES-COVENANT-2026-001) and the Hague submission (ERES-HAGUE-2026-001) governance framework.

### 22.3 Forks

Downstream institutions MAY fork ECS only if they preserve:

- Provenance compatibility (RATE.provenance fields);
- Canonical serialization requirements (Section 8);
- Audit traceability (Section 13);
- Non-compensation enforcement (Sections 7.3, 11.4);
- VEILED semantics (Section 14.7);
- The Ethical Clause (Section 23).

A fork that removes or weakens any of the above MUST be named distinctly and MUST NOT use the `ECS` or `ERES-CRYPTO-STD` identifiers.

### 22.4 Issue Tracking

Issues, proposed changes, and MIEVM ensemble disagreements are tracked at:

```
https://github.com/ERES-Institute-for-New-Age-Cybernetics/eres-crypto-std/issues
```

---

## 23. Ethical Clause (CARE Constraint)

Any implementation of ECS MUST adhere to CARE constraints. A system MUST NOT use ECS to:

- Facilitate punitive exploitation of a subject or class of subjects;
- Create coercive financial entrapment;
- Manufacture false legitimacy for an authority, transaction, or claim;
- Conceal ecological destruction or irreversible harm;
- Discriminate against protected categories without a policy-declared, JERC-compliant, publicly-auditable basis;
- Replace non-punitive remediation pathways with denial-of-service;
- Be deployed in the absence of a published policy, reviewable lexicon, and accessible REL constraint specification.

This clause is **cryptographically non-optional** in the following sense: a system that ships without a conformant Ethical Clause declaration in its policy metadata MUST fail the MIEVM ensemble review (Section 18.5) and therefore fails compliance under Section 21 item 10.

### 23.1 Three Governing Principles

ECS instantiates, at the cryptographic layer, the three Governing Principles of ERES:

> **Don't hurt yourself. Don't hurt others. Build for generations to come.**

These principles map operationally to:

- **Don't hurt yourself** → REL family 5 (Paineologic minimization applied to the subject);
- **Don't hurt others** → REL family 1 (CARE) + family 3 (JERC);
- **Build for generations to come** → APL retention and the 1000-Year Future Map horizon (Section 13.3).

---

## 24. Credits

**Primary Author:** Joseph Allen Sprute (ERES Maestro)
**Institution:** ERES Institute for New Age Cybernetics
**ORCID:** 0000-0001-9946-3221
**Location:** Bella Vista, Arkansas

**MIEVM Ensemble (this synthesis):**
- **Claude** — epistemic framing, scope discipline, defensible claims
- **DeepSeek** — cryptographic interlock model, MIEVM validation tests, polysemantic primitive formalism
- **ChatGPT** — RFC 2119 standards-track structure, six-layer stack architecture, signature and audit requirements
- **Grok** — adversarial review (pending for v1.1)

**Conceptual Lineage:**
- CyberRAVE era (pre-1997–2007) — 72 Key Domains, Global_VPN constraint-based culling epistemology
- SaleBuilders era (1997–2012) — Smart-city adaptive living engineering foundations
- ERES Institute (2012–present) — Triune Cybernetic Framework, Trifecta Protocol, BERA, FAVORS, CBGMODD
- CARE-Based Commonwealth Transition model
- EarnedPath and PlayNAC foundational design
- ERES-BRAINS-SPEC-2026-001 (cognitive-gate authority)
- ERES-BODY-SPEC-2026-001 (data substrate)
- ERES-RECKON-WP-2026-002 (seven Resonance Anchors, conjunctive-gate formalism)

**Personal Anchors:**
Dalia (Lucy) — co-stakeholder, holder of half of the ERES Interest.
Emanuel M. Alexiou (EMA) — Chief Social Engineer, Kingmaker.

---

## 25. References

**Normative:**

- RFC 2119 — Key words for use in RFCs to Indicate Requirement Levels
- RFC 8174 — Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words
- RFC 8032 — Edwards-Curve Digital Signature Algorithm (Ed25519 / Ed448)
- RFC 8785 — JSON Canonicalization Scheme (JCS)
- RFC 8949 — Concise Binary Object Representation (CBOR), deterministic encoding
- RFC 3339 — Date and Time on the Internet: Timestamps
- NIST FIPS 180-4 — Secure Hash Standard (SHA-256)
- NIST FIPS 202 — SHA-3 Standard
- NIST FIPS 186-5 — Digital Signature Standard (ECDSA)
- PKCS #1 v2.2 — RSA Cryptography Standard (RSA-PSS)
- HKDF — RFC 5869

**Informative (ERES corpus):**

- ERES-BRAINS-SPEC-2026-001 — Trifecta Protocol (ONE-GOOD, SECURITY-CLEARANCE, DATA-INTEGRITY gates)
- ERES-BODY-SPEC-2026-001 — Eight-stage Consolidation Pipeline feeding VERTECA
- ERES-CONVERGENCE-WP-2026-001-v3 — Five-layer integration chain
- ERES-RECKON-WP-2026-002 — Seven Resonance Anchors, conjunctive-gate formalism
- ERES-HAGUE-2026-001 — Hague submission on intergenerational equity and UBIMIA as human right
- ERES-COVENANT-2026-001 — Equity Covenant, 1000-year governance
- ERES-EO-DRAFT-2026-001-v1 — Youngstown Zone One Executive Order integration
- RG#404 — BERA Sensor Specification
- RG#406 — Ship's Mate Build Brief
- RG#407 — Raman G-band peak as Nash→Resonance Equilibrium inflection
- CCAL v2.1 — CARE Commons Attribution License (four pillars: Attribution, Transparency, Share-Alike, Patent Non-Assertion)

---

## Appendix A — Terminology Glossary

- **APL** — Audit Persistence Layer (Section 13)
- **ARI** — Attestation / Aura Resonance Indicator (BERA index)
- **BERA** — Bio-Electric Resonance Architecture (four-index evidence vector)
- **BERC** — Bio-Ecologic Resonance Constraints (REL family)
- **CARE** — Cooperative · Accountable · Restorative · Ecologic
- **CBGMODD** — Governance-role attestation vector (C · B · G · M · O · D₁ · D₂)
- **CCAL** — CARE Commons Attribution License
- **CEL** — Canonical Encoding Layer (Section 8)
- **ECS** — ERES Crypto Standard
- **EDF** — Earned Dignity / Earth Defense / Earth Data Framework (three-variant primitive)
- **ERI** — Environment / Evidence Reliability Indicator (BERA index)
- **FAVORS** — Biometric bundle (Fingerprint · Aura · Voice · Odor · Retina · Signature)
- **GAIA** — The whole ERES organism (BODY + BRAINS + VERTECA + PlayNAC + SECUIR)
- **GCF** — Graceful Contribution Formula
- **GraceChain** — Blockchain ledger layer for Meritcoin
- **JERC** — Justice / Equity Resonance Constraints (REL family)
- **MIEVM** — Multi-Instance Ensemble Validation Method (Claude, DeepSeek, ChatGPT, Grok)
- **NBERS** — National Bio-Ecologic Resource Score (GDP alternative)
- **Paineologic** — Minimization of pain through systemic design
- **PERC** — Participation / Merit Resonance Constraints (REL family)
- **PlayNAC** — Semantic–cybernetic decision architecture
- **Polysemantic Primitive** — A finite set of possible plaintext readings for a named civic concept
- **Proof-of-Resonance** — ECS consensus/validation form: *"It's not mining — it's tuning."*
- **RATE** — Seven-dimensional authorization output vector
- **RCL** — RATE Computation Layer (Section 11)
- **RCI** — Resonance Continuity Indicator (BERA index)
- **REL** — Resonance Evaluation Layer (Section 10)
- **Resonance** — Measurable alignment of intent, ethics, and outcome
- **RHC** — **Resonant Harmony Cycle** (BERA index; never any other expansion)
- **RSIG** — Resonance Signature (external signing artifact, Section 12)
- **SECUIR** — Energy–security layer of the GAIA organism
- **Semantic Integrity** — Preservation of meaning across transport and time
- **SPL** — Semantic Payload Layer (Section 9)
- **Superposition** — Pre-σ state of a polysemantic primitive (i.e., "key not yet applied")
- **Trifecta Protocol** — BRAINS three-gate cognitive authority (ONE-GOOD, SECURITY-CLEARANCE, DATA-INTEGRITY)
- **UBIMIA** — Universal Basic Income, Merit-based
- **USC** — User × Subject × Context polysemantic primitive family (27 triples)
- **VEILED (`⊥`)** — Distinguished cryptographic null in RATE dimensions
- **VERTECA** — Voice-to-meaning portal protocol (GAIA voice layer)
- **σ (sigma)** — Internal resonance-derived key value (from BERA via HKDF)

---

## Appendix B — Minimal Implementation Checklist

A developer implementing ECS v1.0 must ship:

- [ ] Canonical serializer (JSON-C per RFC 8785 + Section 8.1 rules)
- [ ] SHA-256 hashing (minimum); SHA3-256 or BLAKE3 optional
- [ ] HKDF-SHA256 for σ derivation
- [ ] Ed25519 signer and verifier
- [ ] CBGMODD parser, validator, and per-role signature verifier
- [ ] FAVORS parser and quorum evaluator
- [ ] BERA parser, validator, and conflict detector
- [ ] SPL polysemantic primitive resolver (with at minimum GCF, EDF, USC)
- [ ] REL constraint evaluator (all six families)
- [ ] RCL scoring-function evaluator (reference set from Section 11.3)
- [ ] RSIG signer/verifier with replay-window cache
- [ ] APL backend (Merkle-tree log MINIMUM)
- [ ] Verifier module (independent of signer)
- [ ] Test-vector compliance runner (Sections 20.1–20.5)
- [ ] MIEVM validation test harness (Sections 18.1–18.4)
- [ ] Policy lexicon loader and authenticator
- [ ] CARE Ethical Clause policy-metadata validator

---

## Appendix C — MIEVM Synthesis Note (v1.0 origin + v1.1 hardening)

### C.1 v1.0 Synthesis (original three-way)

This standard originated as a MIEVM deliverable. Three drafts were produced independently under the prompt "create the ERES Crypto Standard":

1. **USE.ai / Claude draft** — "ERES Cryptography Draft" — a semantic-attestation framework with conservative security claims, explicit exclusions, and four failure modes.
2. **DeepSeek draft** — "ERES-CRYPTO-STD-2026-001-DRAFT v2.0" — a concrete cryptographic-interlock formulation with Key material `K = (CBGMODD, FAVORS, BERA)`, four security claims (Key Completeness, Intent Binding, Non-compensation, Operational Binding), and MIEVM validation tests.
3. **ChatGPT draft** — "ERES-CRYPTO-STD-2026-001 Standards Track" — an RFC 2119-style standards-track document with a six-layer stack (CEL, SPL, REL, RCL, RSIG, APL) and test vectors.

v1.0 preserved:

- Claude's epistemic scope discipline (Sections 1.2, 15.4);
- DeepSeek's security claims and validation tests (Sections 15.3, 18);
- ChatGPT's six-layer architecture and standards-track structure (Sections 5, 8–13, 22).

Disagreements resolved in v1.0:

- **CBGMODD meaning.** Seven-role civic form adopted over four-binary-certification form to match backronym letter count.
- **BERA meaning.** Canonical four-index `(ari, eri, rhc, rci)` form adopted from RG#404.
- **RATE arithmetic.** Operators `×` and `+` defined structurally; scalar `RATE.score = 62.2` example preserved as illustrative only.
- **σ derivation.** HKDF-SHA256 adopted; bare `H(BERA)` rejected as insufficient.

### C.2 v1.1 Hardening (USE.ai formal critique response)

USE.ai's formal v1.0 critique scored the document 8/10 as an attestation-protocol draft and 3/10 as a cryptographic-primitive specification. Its concrete remediation list produced v1.1:

| USE.ai v1.0 finding | v1.1 resolution | Section |
|---------------------|-----------------|---------|
| Failure-mode count contradiction (Section 3 said 4, Section 14 defined 5) | Section 3.1 reworded to "exactly five primary failure codes plus ERROR" | §3.1 |
| Test Vector A self-contradiction: formula yields r₁=10 but vector reports r₁=9 with "both conformant" hedge | r₁=10 is the only conformant value; hedge removed; scoring is strictly normative | §20.1 |
| "Novel cryptographic model" overreach | Replaced with "attestation-composition trust model"; explicit classification added | Abstract, §4.9, §15 |
| `Conflict(BERA, ctx)` unspecified | Concrete algorithm with policy-tunable thresholds (defaults τ=0.25, σ=0.20) | §11.5.1 |
| `SemanticClarity(ctx, resolved)` unspecified | Concrete formula with structural-discount factor | §11.5.2 |
| `PolicyAlignment(ctx, rel_result)` unspecified | Weighted-average formula with integer-priority constraint | §11.5.3 |
| `compute_dimensions(...)` unspecified | Reference scoring of Section 11.3 promoted to only normative form | §11.5.4 |
| `composite_confidence(...)` unspecified | Geometric mean of four factors, enforces non-compensation | §11.5.5 |
| SPL selection `σ mod |readings|` "semantically arbitrary" | Honest characterization as pseudorandom-from-evidence; intent binding explained as payload-hash coverage, not semantic grounding; weighted-selection variant added | §9.3.1–9.3.4 |
| REL "least formalized layer" | Reference REL algorithm specified; rule-severity table fixed | §10.5 |
| Policy language missing | ECS-POL v1.0 JSON Schema; threshold grammar; critical-dimension declaration; lexicon authentication | §11A |
| Test vectors not byte-normative | Fixed test keypair (seed = SHA256 of declared string); fixed nonce; real canonical JSON, SHA-256, σ, Ed25519 signatures; all values verifiable | §20 |
| Protocol guarantees conflated with governance-policy guarantees | Explicit normative separation table | §15.6 |

v1.1 moved the USE.ai rating from "8/10 as attestation protocol, 3/10 as cryptographic primitive" to 9.4/10 (attestation protocol, per DeepSeek review) — the jump USE.ai itself said would come from resolving the above. The 3/10 as cryptographic primitive is NOT a target to improve; ECS is not trying to be a cryptographic primitive, and v1.1 makes that non-goal explicit rather than trying to inflate the score by overclaiming.

### C.2.1 v1.1.1 Patch (DeepSeek formal critique response)

DeepSeek's formal review of v1.1 scored the document 9.4/10 and framed its one outstanding issue as a PATCH-scope determinism risk, not a MINOR-scope feature gap. v1.1.1 is the response.

| DeepSeek v1.1 finding | v1.1.1 resolution | Section |
|-----------------------|-------------------|---------|
| Weighted SPL selector specified as `u = int(σ[0..7]) / 2⁶⁴` (IEEE 754 float division) | Rewritten in integer arithmetic: `p × W_sum ≤ cum[i] × 2⁶⁴`; floating-point explicitly PROHIBITED in weighted-selector path | §9.3.3, §9.3.4 |
| Determinism Test 4 would theoretically fail across architectures (x86_64 vs ARM vs wasm) with FMA and rounding-mode variance | Integer form is identical on every architecture; same σ and weights always produce the same reading | §9.3.4, §18.4 |
| Weighted selector had no byte-normative test vector | Test Vector F added: σ from Vector A, weights [2, 4, 1], selects G3; all intermediate integer values shown | §20.6 |
| Weight type specified as "fixed-point rationals or integer ratios" (ambiguous) | Tightened to: weights MUST be non-negative integers; policies wanting fractional weights MUST scale to preserve exact ratios | §9.3.3 |

This PATCH does not change: RATE vector dimensionality, the canonical equation `(CBGMODD × FAVORS) + BERA`, primitive family sets (GCF, EDF, USC), the canonical encoding, the Ed25519 baseline, or any of the five security claims. For any transaction using the default (unweighted) selector, v1.1.1 produces byte-identical output to v1.1. The only substantive difference is that the weighted-selector path now has a defined deterministic semantics where v1.1 had a determinism gap.

### C.3 Pending for v1.2

- Grok adversarial review;
- Post-quantum signature algorithm selection (Dilithium, Falcon, SPHINCS+);
- Extended test vectors (ERES-CRYPTO-TEST-2026-001) covering all five failure paths byte-normatively;
- Formal security-model write-up in the style of IND-CCA2 reductions adapted for attestation-composition (note: this is a publication target, not a claim that ECS *is* IND-CCA2);
- VERTECA utterance-canonicalization profile;
- GAIA-layer operational-binding handshake specification (wire format, not prose);
- Reference rule sets per REL family (CARE, BERC, JERC, PERC, PAIN, COHERENCE).

(Removed from pending in v1.1.1: weighted SPL floating-point determinism fix — resolved via §9.3.3 integer cross-multiplication.)

### C.4 v1.1.1 as MIEVM Case Study

The v1.1.1 patch is itself instructive as a demonstration that the MIEVM process works as designed. The following sequence is the complete case study:

**Stage 1 — v1.0 adversarial review (USE.ai).**
USE.ai reviewed v1.0 and flagged ten substantive items. Among them: the default SPL selector `σ mod |readings|` was semantically arbitrary. USE.ai correctly identified this as a class of issue where a naive reader might over-interpret what the selector delivers.

**Stage 2 — v1.1 response.**
v1.1 (a) honestly characterized the default selector as pseudorandom-from-evidence rather than semantically-grounded, (b) explained that intent binding comes from payload-hash coverage of BERA rather than from the selector itself, and (c) added a weighted-selection variant for policies that do want semantic grounding. The weighted variant was specified using floating-point arithmetic.

**Stage 3 — v1.1 adversarial review (DeepSeek).**
DeepSeek reviewed v1.1 and flagged exactly one issue the v1.0 review had not: the weighted selector's floating-point division is a determinism risk across IEEE 754 implementations. This is the kind of subtle bug that a single reviewer would plausibly miss — it was introduced in the *response* to the prior review, so it did not exist for the prior reviewer to catch. It required a second adversarial pass.

**Stage 4 — v1.1.1 patch.**
v1.1.1 replaces the floating-point selector with integer cross-multiplication, eliminating the determinism risk and adding a byte-normative test vector (§20.6) that any conforming implementation must pass.

**The instructive generalization.** MIEVM is not "have one AI review another AI's output and call it done." It is an iterative ensemble process in which each adversarial pass hardens the spec against *that reviewer's* particular failure modes, often introducing new surfaces that the *next* reviewer can catch. The v1.0 → v1.1 → v1.1.1 trajectory (Claude synthesis → USE.ai critique → DeepSeek critique → Grok critique pending) is what this looks like in practice. No spec is perfect on first pass. No spec is perfect on second pass. The question is whether the process reliably drives toward better, and the v1.1.1 patch is evidence that it does.

**Proposed MIEVM training materials use.** The v1.0 → v1.1 → v1.1.1 sequence is a self-contained worked example suitable for inclusion in any future ERES or MIEVM pedagogical materials. It shows: (1) how an initial three-draft synthesis produces a first document, (2) how adversarial review identifies real defects, (3) how a response introduces new surfaces, (4) how a second adversarial review catches those surfaces, and (5) how a disciplined semver process distinguishes PATCH fixes from MINOR extensions from MAJOR breaks. The case study is cited as RG#candidate for the ResearchGate corpus.

---

## Appendix D — Trifecta Protocol Alignment

The three gates of the ERES BRAINS (per ERES-BRAINS-SPEC-2026-001) map to ECS as follows:

### D.1 ONE-GOOD Gate

**Mandate:** The action must be ethically sound.

**ECS implementation:** REL constraint families CARE, JERC, PERC, and Paineologic-minimization (Section 10.1 families 1, 3, 4, 5). EDF primitive reading `E₁` (Earned Dignity) is σ-selected when this gate is engaged.

**Failure mode:** F5 — REL-CRITICAL → REJECT.

### D.2 SECURITY-CLEARANCE Gate

**Mandate:** The subject and the attesting parties must be who they claim to be.

**ECS implementation:** CBGMODD validity (Section 4.2) + FAVORS quorum (Section 4.3) + RSIG verification (Section 12). EDF primitive reading `E₂` (Earth Defense / Federation) is σ-selected when this gate is engaged.

**Failure modes:** F1 — GOV-NULL → REJECT; F2 — BIO-NULL → REJECT.

### D.3 DATA-INTEGRITY Gate

**Mandate:** The payload, the provenance chain, and the audit record must be intact.

**ECS implementation:** CEL canonical encoding (Section 8) + APL tamper-evidence (Section 13). EDF primitive reading `E₃` (Earth Data Framework) is σ-selected when this gate is engaged.

**Failure mode:** ERROR status, plus APL integrity-check failure escalation.

### D.4 Conjunctive-Gate Requirement

All three gates are conjunctive. An action authorized through BRAINS requires ACCEPT from ONE-GOOD **AND** ACCEPT from SECURITY-CLEARANCE **AND** ACCEPT from DATA-INTEGRITY. This matches ECS non-compensation (Section 11.4): a VEILED on a critical dimension invalidates the vector regardless of other dimensions' strength.

The conjunctive gate is the arithmetic inversion of weighted-sum authorization systems that let strength in one dimension compensate for weakness in another — the failure mode that GDP-style accounting exemplifies and that the ERES-RECKON-WP-2026-002 seven-anchor formalism was designed to prevent.

---

**End of ERES-CRYPTO-STD-2026-001, version 1.1.1 (DeepSeek-patched).**

*Don't hurt yourself. Don't hurt others. Build for generations to come.*

