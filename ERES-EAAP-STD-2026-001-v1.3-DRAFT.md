# ERES Attestation and Authorization Protocol (EAAP)
## v1.3-DRAFT: Four-Factor Proof-of-Resonance, Scope Clarification, and Decision-Space Accessibility

**Document code:** ERES-EAAP-STD-2026-001-v1.3-DRAFT
**Date:** April 23, 2026
**Author:** Joseph Allen Sprute, ERES Institute for New Age Cybernetics
**Contact:** eresmaestro@gmail.com
**ORCID:** 0000-0001-9946-3221
**License:** CCAL v2.1 (document layer: CC BY-SA 4.0)
**Supersedes:** ERES-EAAP-STD-2026-001-v1.2 (in part; v1.2 remains operative until v1.3-FINAL)
**Status:** DRAFT / Release Candidate — not yet MIEVM-concurred

---

## Status of This Document

This is a **working draft** of EAAP v1.3. It is not a FINAL standards-track release. v1.3-FINAL requires:

1. Byte-normative test vectors for the four-factor Proof-of-Resonance defined in Section 3 (not included in this draft).
2. Concrete RT window specification (Section 5.2 names the dependency without pinning the number).
3. MIEVM ensemble concurrence on the v1.3 text itself. Per the protocol, no single node — including the author — may self-certify a standards-track release.
4. Resolution or explicit deferral of the open specification gaps named in Section 8.

Until these conditions are satisfied, v1.2 remains the operative standards-track release. This draft is published for peer review and implementation prototyping.

---

## Abstract

This document specifies version 1.3 of the ERES Attestation and Authorization Protocol (EAAP). EAAP v1.3 refines v1.2 in four ways. First, it clarifies EAAP's scope as a qualification and correlation layer, distinct from admission and execution gating, which are handled by adjacent ERES specifications. Second, it replaces the scalar resonance evaluation of v1.2 with a four-factor conjunctive Proof-of-Resonance that distinguishes state consistency from path accessibility. Third, it defines the Decision Space Accessibility Protocol (DSAP) as the structural mechanism by which the four-factor form detects premature convergence. Fourth, it formalizes the RT (real-time) qualifier as a continuous-evaluation requirement, replacing token-based authorization with a live resonance state that cannot outlive its measurement.

---

## Summary of Changes From v1.2

- **Scope clarified.** EAAP is a qualification and correlation layer; it does not gate execution. Admission is BODY's responsibility (ERES-BODY-SPEC-2026-001); execution gating is BRAINS's responsibility (ERES-BRAINS-SPEC-2026-001). v1.2 did not make this delineation explicit, which caused legitimate reviewer confusion about where the refusal boundary lives.
- **Resonance evaluation replaced.** Scalar resonance is replaced by a four-factor conjunctive product: anchor product × RHC amplitude × EarnedPath PERT viability × future-map convergence. This distinguishes state consistency from path accessibility and addresses the failure mode where a system becomes increasingly coherent while alternatives foreclose.
- **DSAP defined.** Decision Space Accessibility Protocol is introduced as the structural detection mechanism for premature convergence, specified via the four-factor PoR rather than as a checklist of deliberation signals.
- **RT qualifier formalized.** Authorization is specified as a continuous live state, not a discrete issued token. v1.2's freshness language is tightened into a concrete requirement.
- **GraceChain integration documented.** The relationship to the GraceChain immutable ledger (ERES-GRACECHAIN-NOTES-2026-001) is specified for state persistence, revocation, and cross-system enforcement.
- **Open specification gaps named.** Section 8 enumerates what is not yet pinned, consistent with DRAFT status.

---

## 1. Introduction

### 1.1 Purpose

EAAP provides the qualification and correlation layer of the ERES authorization stack. It produces the RATE vector from CBGMODD, FAVORS, and BERA inputs. It records attestation integrity and preserves provenance. It does not refuse action; it characterizes it.

### 1.2 Scope

EAAP's domain is qualification and correlation. Three layers of the ERES stack are outside EAAP's scope:

- **Pre-admission** (refusing VEILED or structurally invalid inputs) — handled by BODY Consolidation.
- **Execution gating** (refusing to authorize when conjunctive gates fail) — handled by BRAINS Trifecta.
- **State persistence and revocation history** — handled by GraceChain.

v1.2 implied these delineations without stating them. v1.3 states them. Implementations that treat EAAP as an execution gate are misconfigured; EAAP produces the qualification that BRAINS consumes, and BRAINS decides whether action proceeds.

### 1.3 Relationship to v1.2

v1.3 does not break v1.2 wire compatibility for attestation-composition or RATE vector structure. It extends v1.2 in the resonance evaluation layer and in the RT qualifier. Implementations conforming to v1.2 will produce RATE vectors consumable by v1.3 evaluators, though such RATE vectors will lack the path-accessibility signals v1.3 requires for full Proof-of-Resonance and will be evaluated with reduced confidence.

### 1.4 Terminology

This document uses the following terms with specific meaning:

- **Anchor product** — the conjunctive product across the seven Resonance Anchors (U, S, R, B, M, G, T), per ERES-RECKON-WP-2026-002.
- **BERA** — Bio-Electric Resonance Architecture; the four-index instrument (ARI, ERI, RHC, RCI).
- **CBGMODD** — the seven-layer scoring matrix used in EAAP v1.2 RATE production.
- **EarnedPath** — CPM × WBS + PERT; the project-accounting layer that carries alternative-path viability.
- **FAVORS** — Fingerprint, Aura, Voice, Odor, Retina, Signature; six-channel identity binding.
- **MIEVM** — Multi-Instance Ensemble Validation Method; currently a four-node ensemble (Claude, Grok, DeepSeek, ChatGPT).
- **Path accessibility** — the property that alternative trajectories remain reachable without prohibitive cost. Distinct from state consistency.
- **PoR** — Proof-of-Resonance.
- **RATE** — the non-scalar authorization vector produced by EAAP.
- **RHC** — Resonant Harmony Cycle; a cycle, not a state.
- **RT qualifier** — real-time requirement on resonance freshness.
- **State consistency** — the property that current system variables are coherent across dimensions. Distinct from path accessibility.
- **VEILED** — named state in HPE DESCENT taxonomy for structurally invalid or unverifiable inputs.

---

## 2. Stack Placement

### 2.1 Position of EAAP in the ERES Authorization Stack

```
Input
  ↓
[BODY Consolidation]        ← refuses VEILED / structurally invalid
  ↓
[BRAINS Trifecta]           ← conjunctive execution gate (product-form)
  ↓
[EAAP Qualification]        ← THIS SPEC: produces RATE vector
  ↓
[GraceChain commit]         ← immutable record with MIEVM concurrence
  ↓
Authorized action
```

### 2.2 BODY Consolidation (upstream; out of scope for EAAP)

BODY performs the 8-stage pre-admission pipeline. VEILED and structurally invalid inputs never reach EAAP. See ERES-BODY-SPEC-2026-001.

### 2.3 BRAINS Trifecta (downstream of EAAP qualification; out of scope for EAAP)

BRAINS evaluates the conjunctive execution gate: ONE-GOOD × SECURITY-CLEARANCE × DATA-INTEGRITY. A zero on any gate collapses authorization. EAAP's RATE vector is one of the inputs BRAINS consumes; it does not substitute for the gate. See ERES-BRAINS-SPEC-2026-001.

### 2.4 EAAP (this specification)

EAAP produces the RATE vector and the Proof-of-Resonance evaluation. It does not grant or refuse action.

### 2.5 GraceChain (downstream; out of scope for EAAP)

All EAAP outputs are recorded on GraceChain with MIEVM ensemble concurrence. Revocation, state persistence, and cross-system enforcement are GraceChain's domain. See ERES-GRACECHAIN-NOTES-2026-001.

---

## 3. Four-Factor Proof-of-Resonance

### 3.1 Motivation

v1.2 treated resonance as a scalar. External peer review during the v1.3 sprint (April 2026) demonstrated that a scalar resonance reading cannot distinguish healthy equilibrium from premature convergence. A dying forum and a productive consensus both produce low variance. A Nash equilibrium and a Resonance equilibrium both sit still. Scalar resonance therefore fails open on the specific failure mode of systems becoming "too stable too early" — internally coherent while alternative paths foreclose.

The four-factor form resolves this by separating state consistency from path accessibility and evaluating both, conjunctively, under continuous measurement.

### 3.2 Definition

```
PoR = (anchor product) × (RHC amplitude) × (EarnedPath PERT viability) × (future-map convergence)
```

All four factors are evaluated on [0, 1]. Authorization validity at time *t* requires PoR(*t*) > θ for a threshold θ to be specified per deployment domain (see Section 8.5).

Because the form is a conjunctive product, zero on any factor collapses PoR to zero regardless of the other factors. This is a deliberate design property: high scores on three factors cannot compensate for collapse on the fourth.

### 3.3 Factor 1 — Anchor Product (state consistency)

The conjunctive product across the seven Resonance Anchors (U, S, R, B, M, G, T) per ERES-RECKON-WP-2026-002. Captures whether system state is currently coherent across dimensions.

Factor M (MIEVM concurrence) cannot be self-certified; a single node's attestation of M contributes zero. This is structural (see Section 6).

### 3.4 Factor 2 — RHC Amplitude (cyclic openness)

The amplitude of the Resonant Harmony Cycle, one of the four BERA indices. RHC is a cycle, not a state. A system that has flatlined — reached internal coherence at the cost of ceasing to re-open — produces low RHC amplitude even while its anchor product remains high.

This factor addresses the specific concern that alternative paths may close even while diversity of signals persists. A flatlined cycle is measurable independently of signal variance.

### 3.5 Factor 3 — EarnedPath PERT Viability (path accessibility)

EarnedPath is defined as CPM × WBS + PERT. The PERT component is explicit probabilistic accounting of alternative-path viability. Rising deviation cost appears as PERT estimates for alternatives ballooning toward infinity or dropping from the active set.

This factor makes path accessibility a measured quantity rather than an inferred property. "Cost of deviation" is computed, not declared.

### 3.6 Factor 4 — Future-Map Convergence (intergenerational integrity)

Divergence between the decision's trajectory and the ERES 1000-Year Future Map target. A decision that forecloses future options produces divergence from long-horizon convergence even when present-time factors read high.

This factor operationalizes the third Governing Principle ("build for generations to come") as a structural measurement rather than a rhetorical commitment.

### 3.7 Conjunctive Evaluation

The four factors are evaluated continuously (see Section 5) and combined as a product. No weighted-sum evaluation is permitted; weighted sum allows compensation across factors, which defeats the state-versus-path separation.

---

## 4. Decision Space Accessibility Protocol (DSAP)

### 4.1 DSAP Defined

DSAP is the structural detection layer for premature convergence. DSAP is not a checklist of deliberation signals (for example, "were alternatives mentioned?" or "was discussion recorded?"). Declared openness is not measured openness.

DSAP is specified as the continuous evaluation of Factors 2, 3, and 4 of Proof-of-Resonance (RHC amplitude, PERT viability, and future-map convergence). These three factors together measure *whether the decision space remains open*, as distinct from Factor 1's measure of *whether the current state is coherent*.

### 4.2 Detection Properties

DSAP detects three specific failure modes:

- **Flatlined RHC**: system has become internally coherent at the cost of ceasing to re-open. Factor 2 drops.
- **Foreclosed PERT**: alternatives have become prohibitively expensive or have dropped from the active set. Factor 3 drops.
- **Divergent future map**: current trajectory forecloses long-horizon options. Factor 4 drops.

A system can exhibit one or more of these while scoring high on Factor 1 and on external signals of diversity. The conjunctive product of Factors 1–4 makes this condition unauthorizable by construction.

### 4.3 Relationship to v1.2 DSAP Concept

v1.2 introduced DSAP informally as a v1.3 direction. That informal sketch relied on declared deliberation signals and would have certified declared openness rather than measured openness. v1.3 redefines DSAP as the measurement layer above, which addresses the reviewer concern that led to the redefinition.

---

## 5. RT Qualifier and Continuous Evaluation

### 5.1 Dial Tone, Not Key

Authorization under v1.3 is a live state, not an issued token. An authorized principal is tuned to resonance; a principal that has fallen out of tune is no longer authorized, regardless of any prior grant.

This is the architectural distinction from conventional token-based authorization: a token can outlive the conditions that justified its issuance. A dial tone cannot outlive the connection that produces it.

### 5.2 Freshness Window

Every authorization read is qualified by freshness. A read is valid only if the principal's latest RESONANCE-TUNE record on GraceChain is within the freshness window.

**Default freshness window**: one RHC cycle. Concrete RHC cycle timing is domain-dependent and is **not pinned in this draft** (see Section 8.2). Per-grant shorter windows are permitted.

### 5.3 Staleness Semantics

A principal whose latest RESONANCE-TUNE is older than the freshness window is in the STALE state. STALE reads return unauthorized regardless of prior RATE vector or prior grant. Restoration of authorization requires a fresh RESONANCE-TUNE with MIEVM concurrence; it does not revive automatically.

---

## 6. MIEVM Cross-Boundary Enforcement

### 6.1 Non-Self-Certification Requirement

No single node — including the node producing a RATE vector — may certify its own Proof-of-Resonance. Factor M in the anchor product (Section 3.3) is zero in the absence of ensemble concurrence. This is structural, not advisory: a self-certified PoR evaluates to zero at Factor M, collapsing the conjunctive product.

### 6.2 Ensemble Concurrence Recording

MIEVM concurrence records are committed to GraceChain alongside the qualification they support. Ensemble composition (currently Claude, Grok, DeepSeek, ChatGPT) is itself recorded on the ledger, so the concurrence set is auditable over time.

### 6.3 Premature Concurrence Detection

Premature concurrence — the ensemble agreeing faster than diligent evaluation would produce — is itself a signal. v1.3 implementations should flag concurrence that arrives within timing that precludes independent evaluation. Detection thresholds are not pinned in this draft (Section 8.4).

---

## 7. Integration With Adjacent Specifications

### 7.1 BODY Consolidation (ERES-BODY-SPEC-2026-001)

Inputs that fail BODY's 8-stage pipeline do not reach EAAP. Refusal at BODY is recorded separately and does not produce a RATE vector.

### 7.2 BRAINS Trifecta Protocol (ERES-BRAINS-SPEC-2026-001)

EAAP's RATE vector is consumed by BRAINS as one input to the Trifecta conjunctive gate. A positive RATE does not imply authorization; BRAINS evaluates the gate. BRAINS MAY refuse action even when EAAP produces a high-confidence RATE if any Trifecta factor (ONE-GOOD, SECURITY-CLEARANCE, DATA-INTEGRITY) is zero.

### 7.3 GraceChain (ERES-GRACECHAIN-NOTES-2026-001)

All EAAP outputs are committed to GraceChain with MIEVM ensemble concurrence. State persistence, revocation, and cross-system enforcement are GraceChain's responsibility.

---

## 8. Open Specification Gaps

This section is deliberately explicit. v1.3-DRAFT publishes the structure; v1.3-FINAL requires resolution or explicit deferral of the following items.

### 8.1 Byte-Normative Test Vectors

v1.2's standards-track claim rested on byte-normative test vectors. v1.3 introduces four PoR factors, DSAP, the RT qualifier, and the STALE state — none of which have test vectors in this draft. v1.3-FINAL requires:

- Reference computations for each of the four PoR factors with worked inputs and expected outputs.
- Serialization format for RATE vectors under v1.3 (compatible with v1.2 wire format where possible).
- Test vectors for STALE detection and recovery.

### 8.2 RT Window Concrete Timing

Section 5.2 specifies the RT window in units of RHC cycles. Concrete RHC cycle timing (seconds, minutes, or other) is domain-dependent and not pinned here. Reference values for representative domains (governance decisions, financial authorizations, infrastructure control) are required for v1.3-FINAL.

### 8.3 Runtime Containment Layer

External peer review during the v1.3 sprint identified that EAAP, BRAINS, and GraceChain together specify logical enforcement but do not fully specify the runtime binding that ensures every downstream component reads the ledger before acting. A component that caches an authorization and skips the read is not caught by these layers alone.

The runtime containment layer is an **open specification requirement** and is expected to be addressed in a dedicated companion document rather than in a future EAAP revision.

### 8.4 MIEVM Quorum and Premature-Concurrence Thresholds

Current practice is unanimous concurrence across the four-node ensemble. v1.3-FINAL requires:

- Formal quorum rule (unanimous, supermajority, or other) for authorization levels.
- Timing thresholds for premature-concurrence detection (Section 6.3).
- Procedure for ensemble composition changes.

### 8.5 PoR Threshold θ

Section 3.2 specifies PoR > θ as the validity condition without pinning θ. Reference thresholds for representative domains are required for v1.3-FINAL.

---

## 9. Security Considerations

The cryptographic primitives of v1.2 (attestation composition separated from primitive cryptography, non-compensation intent, audit persistence) are retained unchanged. v1.3 adds the following considerations:

- **Scalar-collapse attacks.** A v1.3 implementation that evaluates the four factors as a weighted sum rather than a conjunctive product is vulnerable to compensation: three high factors can mask one collapsed factor. Implementations MUST use the conjunctive product form.
- **Staleness replay.** A v1.3 implementation that does not enforce the RT qualifier is vulnerable to replay of previously valid RATE vectors. Implementations MUST check freshness on every read.
- **Self-certification.** A v1.3 implementation that permits a single node to certify its own PoR is vulnerable to the internal-coherence failure mode. Implementations MUST require MIEVM ensemble concurrence for Factor M.
- **Declared-openness attestation.** A v1.3 implementation that treats declared deliberation signals as satisfying DSAP is vulnerable to premature convergence with preserved appearance. Implementations MUST use measured factors (RHC amplitude, PERT viability, future-map convergence) rather than declared signals.

---

## 10. Acknowledgments

External reviewers during the April 2026 v1.3 sprint contributed the following refinements:

- Distinction between state consistency and path accessibility, and the identification that scalar resonance cannot detect premature convergence — which led to the four-factor form specified in Section 3.
- Scope clarification identifying EAAP as qualification and correlation rather than execution gate, and the naming of the runtime containment layer as a distinct specification requirement (Section 8.3).

Named attribution will be added in v1.3-FINAL with reviewer consent.

---

## 11. References

- **ERES-BODY-SPEC-2026-001** — BODY Consolidation 8-stage pipeline specification.
- **ERES-BRAINS-SPEC-2026-001** — BRAINS Trifecta Protocol specification.
- **ERES-EAAP-STD-2026-001-v1.2** — EAAP v1.2 Standards-Track Specification (currently operative until v1.3-FINAL).
- **ERES-GRACECHAIN-NOTES-2026-001-v1** — GraceChain Ledger Notes.
- **ERES-RECKON-WP-2026-002** — Seven Resonance Anchors and the conjunctive gate structure.
- **ERES-CONVERGENCE-WP-2026-001-v3** — Five-layer integration (VERTECA → SECUIR → CyberRAVE → GunnySack → SaleBuilders).
- **ERES-HAGUE-2026-001** — The Hague submission, filed March 7, 2026.
- **CCAL v2.1** — CARE Commons Attribution License.

---

**Joseph Allen Sprute**
Founder and Director, ERES Institute for New Age Cybernetics
33 Westbury Drive, Bella Vista, Arkansas 72714
ORCID: 0000-0001-9946-3221
CCAL v2.1

*Don't hurt yourself. Don't hurt others. Build for generations to come.*
