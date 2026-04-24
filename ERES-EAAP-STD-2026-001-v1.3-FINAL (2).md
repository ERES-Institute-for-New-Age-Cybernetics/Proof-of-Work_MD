# ERES Attestation and Authorization Protocol (EAAP)
## v1.3-FINAL — Standards-Track Specification

**Document code:** ERES-EAAP-STD-2026-001-v1.3-FINAL
**Date:** April 24, 2026
**Authors:**
- Joseph Allen Sprute (Principal, sole author of framework and implementation), ERES Institute for New Age Cybernetics
- Teresa Villa (Named Contributor, scope-limited to Section 7 VBE Execution-Binding Model and Section 8 DSAP-PRE Sovereignty Layer Mapping), Founder, JusticeTree AI

**Named Peer Reviewer (scope-limited):**
- Andrzej Skulski, AI Governance / Decision–Commit Boundary, Founder, Dom Ciszy – Resonance Lab. Contribution scoped to: (i) identification of the pre-threshold failure mode, and (ii) articulation of the decision-commit / separatrix boundary condition. Does not constitute endorsement of the framework as a whole or of the implementation approach (PoR structure, DSAP-PRE formalization, broader ERES stack).

**Contact:** eresmaestro@gmail.com
**ORCID:** 0000-0001-9946-3221
**License:** CCAL v2.1 (document layer: CC BY-SA 4.0)
**Supersedes:** ERES-EAAP-STD-2026-001-v1.2 (2026-04-22), ERES-EAAP-STD-2026-001-v1.3-DRAFT (2026-04-23)
**Companion documents:** ERES-GRACECHAIN-NOTES-2026-001-v1, ERES-SEPARATRIX-MATH-2026-001-v2, ERES-ATTRIBUTION-PROTOCOL-2026-001-v1, ERES-CRYPTO-STD-2026-001-v1.1.1, ERES-MPAM-2026-001
**Status:** FINAL — MIEVM ensemble concurrence recorded, byte-normative test vectors verified, zero open gaps

---

## Abstract

This document specifies version 1.3 of the ERES Attestation and Authorization Protocol (EAAP) as a FINAL standards-track release. v1.3 refines v1.2 in seven specific ways. First, it clarifies EAAP's scope as a qualification and correlation layer, distinct from admission, execution gating, and runtime containment. Second, it replaces scalar resonance evaluation with a four-factor conjunctive Proof-of-Resonance distinguishing state consistency from path accessibility. Third, it formalizes the Decision Space Accessibility Protocol (DSAP) as measured rather than declared openness, and introduces **DSAP-PRE** as the pre-threshold regime-transition detection layer using derivative and topological analysis. Fourth, it maps DSAP-PRE across three sovereignty domains — Personal (cognitive), Public (communicative), and Private (contractual/binding). Fifth, it integrates the **Validation Before Enforcement (VBE) Execution-Binding Model** as the runtime containment specification, closing the final architectural gap identified in peer review. Sixth, it formalizes the RT qualifier as a continuous-evaluation "dial tone, not key" requirement. Seventh, it documents MIEVM (Multi-Instrument Ensemble Validation Method) with its ECR convergence metric, ensemble composition rules, and five-tier containment stack per the MPAM-MIEVM duality.

v1.3-FINAL is published with byte-normative test vectors verified through Ed25519 round-trip, inheriting the Test Vector A keypair established in ERES-CRYPTO-STD-2026-001-v1.1.1, and extended with PoR-factor-specific vectors. A worked USE-CASE on the DOFA Family Stewardship Council decision flow (ERES-DOFA-WP-2026-001-C) demonstrates the complete stack in operation.

**Reviewer positions are scoped per Section 15.** Teresa Villa (Named Contributor) approved the three-layer architecture (DSAP-PRE / EAAP+BRAINS+GraceChain / VBE) subject to three named invariants (V1, V2, V3) recorded in Section 15.1. Andrzej Skulski (Named Peer Reviewer) scoped his contribution to (i) identification of the pre-threshold failure mode and (ii) articulation of the boundary condition, and explicitly did not endorse the framework as a whole or the implementation approach. Sole-author responsibility for the framework rests with Joseph Allen Sprute and the ERES Institute (Section 15.4).

---

## Document Provenance

This specification was developed through Multi-Instrument Ensemble Validation Method (MIEVM) cycles during April 2026. Key provenance events:

- **April 22, 2026** — ERES-EAAP-STD-2026-001-v1.2 published (RG#426). Session ERES-SESSION-2026-04-22-A produced ERES-CRYPTO-STD-2026-001-v1.1.1 with byte-normative test vectors.
- **April 22–23, 2026** — LinkedIn peer review by Andrzej Skulski (four-turn correspondence) identified decision-space accessibility and separatrix-crossing failure modes.
- **April 23, 2026** — Teresa Villa contributed three signed documents: *Runtime Containment Layer: Preliminary Interface Notes*, *VBE — Execution-Binding Model (Inner Workings)*, and *DSAP-PRE — Sovereignty Layer Mapping*.
- **April 23, 2026** — ERES-EAAP-STD-2026-001-v1.3-DRAFT published with four-factor PoR, DSAP reframe, five named open gaps.
- **April 23, 2026** — ERES-GRACECHAIN-NOTES-2026-001-v1, ERES-SEPARATRIX-MATH-2026-001-v2, and ERES-ATTRIBUTION-PROTOCOL-2026-001-v1 published as companion documents.
- **April 24, 2026** — v1.3-FINAL consolidation: named-reviewer position statements scoped per Attribution Protocol; Villa approved for publication with VBE™ trademark / JusticeTree AI™ authorship clarification recorded (Section 15.1); Skulski's structural positioning concern (DSAP-PRE as boundary condition, not internal component) addressed in Section 6.1; zero open gaps remaining.

Session reports and LinkedIn correspondence records are retained under the Attribution Protocol (ERES-ATTRIBUTION-PROTOCOL-2026-001-v1).

---

## Summary of Changes From v1.2

- **Scope clarified.** EAAP is a qualification and correlation layer; it does not admit, gate, enforce, or persist. Admission is BODY's responsibility (ERES-BODY-SPEC-2026-001); execution gating is BRAINS's (ERES-BRAINS-SPEC-2026-001); runtime containment is VBE's (Section 7); state persistence is GraceChain's (ERES-GRACECHAIN-NOTES-2026-001-v1). v1.2 implied these delineations; v1.3-FINAL states them.
- **Four-factor Proof-of-Resonance.** Scalar resonance replaced by a conjunctive product — anchor product × RHC amplitude × EarnedPath PERT viability × future-map convergence — distinguishing state consistency from path accessibility.
- **DSAP as measured openness.** DSAP is specified via the three path-accessibility factors (R, P, F) rather than as a checklist of declared deliberation signals.
- **DSAP-PRE added.** Pre-threshold regime-transition detection via three proxies (RHC second derivative, PERT distribution topology, hysteresis counterfactual) closes the separatrix-crossing failure mode.
- **Three-domain sovereignty mapping.** DSAP-PRE proxies mapped to Personal (cognitive), Public (communicative), and Private (contractual/binding) sovereignty domains per Teresa Villa's contributed mapping.
- **VBE™ Execution-Binding Model integrated as external layer.** Runtime containment is no longer an open gap; it is integrated as Section 7 by reference to Teresa Villa's Validation Before Enforcement (VBE™) framework, authored under JusticeTree AI™. VBE™ is not an ERES-originated component. The integrated invariant: *No validation = no action. No fresh authorization record = no execution.*
- **MIEVM canonicalized.** MIEVM now expands to **Multi-Instrument Ensemble Validation Method** (MPAM §8 canonical). Section 9 documents ECR convergence metric, ensemble composition, Instrument-of-Faith framing, and five-tier containment stack.
- **RT qualifier formalized.** Authorization is a continuous live state ("dial tone, not key"), not a discrete issued token.
- **Byte-normative test vectors.** Section 10 extends the Test Vector A keypair from ERES-CRYPTO-STD-2026-001-v1.1.1 with PoR-factor-specific vectors.
- **DOFA USE-CASE.** Section 11 demonstrates the full stack operating on a Family Stewardship Council authorization from ERES-DOFA-WP-2026-001-C.
- **Zero open gaps.** All five gaps named in v1.3-DRAFT are resolved.

---

## 1. Introduction

### 1.1 Purpose

EAAP provides the qualification and correlation layer of the ERES authorization stack. It produces the RATE vector from CBGMODD (seven-role civic composition), FAVORS (six-channel identity binding), and BERA (four-index resonance architecture) inputs. It records attestation integrity and preserves provenance. It does not refuse action; it characterizes it. Refusal is delegated to BRAINS (logical gate), DSAP-PRE (regime detection), and VBE (runtime containment).

### 1.2 Scope

EAAP's domain is qualification and correlation. Five layers of the ERES stack are outside EAAP's scope but integrate with it:

- **Pre-admission** — BODY Consolidation (refuses VEILED or structurally invalid inputs).
- **Pre-threshold regime detection** — DSAP-PRE (detects separatrix crossing before state metrics degrade; Section 6).
- **Execution gating** — BRAINS Trifecta (conjunctive product: ONE-GOOD × SECURITY-CLEARANCE × DATA-INTEGRITY).
- **Runtime containment** — VBE Execution-Binding Model (ensures no action executes without a fresh authorization record; Section 7).
- **State persistence** — GraceChain (immutable ledger with MIEVM ensemble concurrence).

### 1.3 The Convergence-Proof Framing

EAAP v1.3 participates in what the accompanying Substack analysis ("The Convergence Proof: Why ERES and Anthropic Are Independent Witnesses to the Same Architectural Thesis") names as *ethics as legibly stated infrastructure, not implicit hope*. Legibility in this specification means: every refusal boundary has a named document; every factor has a measurable definition; every claim is separated from what it does not claim (see Section 12, Security Considerations, and the protocol-vs-governance separation per ERES-CRYPTO-STD §15.6).

### 1.4 Terminology

- **Anchor product** — conjunctive product across the seven Resonance Anchors (U, S, R, B, M, G, T) per ERES-RECKON-WP-2026-002.
- **BERA** — Bio-Electric Resonance Architecture; four-index instrument (ARI, ERI, RHC, RCI).
- **CBGMODD** — seven-role civic composition (Citizen, Business, Government, Mediator, Military, Dignitary, Diplomat).
- **DSAP** — Decision Space Accessibility Protocol; measured openness via factors R, P, F.
- **DSAP-PRE** — Pre-threshold Decision Space Accessibility; separatrix-crossing detection via derivative and topological analysis.
- **ECR** — Erasure Completeness Ratio; MIEVM convergence metric = |R(C)| / (|R(C)| + |N(C)|).
- **EarnedPath** — CPM × WBS + PERT; project-accounting layer carrying alternative-path viability.
- **FAVORS** — Fingerprint, Aura, Voice, Odor, Retina, Signature; six-channel identity binding.
- **MIEVM** — Multi-Instrument Ensemble Validation Method (MPAM §8 canonical).
- **MPAM** — Melting Pot Assimilation Method (ERES-MPAM-2026-001).
- **Path accessibility** — viability of alternative trajectories without prohibitive cost.
- **PoR** — Proof-of-Resonance (four-factor conjunctive product).
- **RATE** — non-scalar authorization vector produced by EAAP.
- **RHC** — Resonant Harmony Cycle (one of four BERA indices; always a cycle, never a state).
- **RT qualifier** — real-time continuous-evaluation requirement.
- **Separatrix** — boundary in state space between basins of attraction.
- **State consistency** — coherence of current system variables across dimensions.
- **VBE™** — Validation Before Enforcement; independent execution-layer governance framework authored under JusticeTree AI™ (Teresa Villa). Integrated into EAAP v1.3-FINAL as the runtime containment layer per Section 7. Not originated within ERES.
- **VEILED** — named state in HPE DESCENT taxonomy for structurally invalid inputs.

---

## 2. Stack Placement

### 2.1 Full Authorization Stack

```
Input
  ↓
[BODY Consolidation]               ← admission (refuses VEILED)
  ↓
[DSAP-PRE]                         ← INTEGRATED upstream boundary condition
                                     (pre-threshold regime detection; §6)
  ↓
[BRAINS Trifecta]                  ← execution gate (conjunctive product)
  ↓
[EAAP Qualification / PoR]         ← THIS SPEC: four-factor PoR + RATE
  ↓
[VBE™]                             ← INTEGRATED downstream enforcement
                                     (runtime containment; §7)
                                     (authored by JusticeTree AI™, integrated here)
  ↓
[GraceChain commit]                ← immutable record with MIEVM concurrence
  ↓
Authorized action
```

**Integrated boundary layers.** Two layers in this stack are integrated rather than originated-within-ERES:

- **DSAP-PRE** is a structurally upstream boundary condition with its own authoritative mathematical specification (ERES-SEPARATRIX-MATH-2026-001-v2). EAAP integrates DSAP-PRE as a gating precondition to qualification. It is not an internal EAAP subsystem.
- **VBE™** is an independent execution-layer governance framework authored under JusticeTree AI™ (Teresa Villa). EAAP integrates VBE™ as the runtime containment layer between qualification and action. VBE™ is not an ERES-originated component.

The ordering is substantive: DSAP-PRE must fire *before* BRAINS so that regime transitions refuse qualification before qualification is attempted; VBE™ must gate *after* EAAP so that the authorization record binds to the exact RATE and PoR values that justified it. Each integrated layer is architecturally independent; EAAP v1.3-FINAL conformance requires preserving that independence (Section 14.1).

### 2.2 Layer Responsibilities

| Layer | Originated | Refuses | Produces | Authoritative Document |
|---|---|---|---|---|
| BODY | ERES | VEILED / structurally invalid inputs | Admission record | ERES-BODY-SPEC-2026-001 |
| DSAP-PRE | ERES (integrated upstream boundary) | Pre-threshold regime-transition systems | ρ_RHC, ρ_PERT, ρ_hyst composite | ERES-SEPARATRIX-MATH-2026-001-v2, §6 of this spec |
| BRAINS | ERES | Zero on any Trifecta factor | Gate result | ERES-BRAINS-SPEC-2026-001 |
| EAAP | ERES | (does not refuse) | RATE vector, PoR | This spec |
| VBE™ | **JusticeTree AI™** (Villa) | Actions without fresh authorization | Execution-bound record | Villa contributed papers (April 23, 2026), §7 of this spec |
| GraceChain | ERES | (does not refuse) | Immutable block with MIEVM sigs | ERES-GRACECHAIN-NOTES-2026-001-v1 |

---

## 3. Four-Factor Proof-of-Resonance

### 3.1 Motivation

v1.2 treated resonance as a scalar. External peer review by Andrzej Skulski during April 22–23, 2026 demonstrated that a scalar resonance reading cannot distinguish healthy equilibrium from premature convergence. A dying forum and a productive consensus both produce low variance. A Nash equilibrium and a Resonance equilibrium both sit still. Scalar resonance therefore fails open on the "too stable too early" failure mode — internally coherent while alternative paths foreclose.

The four-factor form resolves this by separating **state consistency** from **path accessibility** and evaluating both, conjunctively, under continuous measurement. This is the arithmetic response to the epistemic objection: against a product gate, a reduced space is a low score by construction.

### 3.2 Definition

```
PoR(t) = A(t) × R(t) × P(t) × F(t)
```

All four factors evaluated on [0, 1]. Authorization validity at time t requires PoR(t) ≥ θ for threshold θ defined per deployment domain (Section 3.8).

Conjunctive product is normative. Weighted-sum evaluation is prohibited: sum allows compensation across factors, defeating the state-versus-path separation.

### 3.3 Factor A — Anchor Product (State Consistency)

Product across the seven Resonance Anchors (U, S, R, B, M, G, T) per ERES-RECKON-WP-2026-002. Each anchor on [0, 1].

```
A(t) = U(t) × S(t) × R(t) × B(t) × M(t) × G(t) × T(t)
```

**Factor M (MIEVM concurrence) cannot be self-certified.** A single node's attestation of M contributes zero. Ensemble concurrence is structural, not advisory; see Section 9.

### 3.4 Factor R — RHC Amplitude (Cyclic Openness)

Normalized amplitude of the Resonant Harmony Cycle over the previous two cycles. RHC is always a cycle, never a state — a system that has flatlined has reached internal coherence at the cost of ceasing to re-open.

```
R(t) = normalize(amplitude(RHC, window=2_cycles))
R(t) = 0  if  variation(RHC) < 0.05  (flatline)
```

### 3.5 Factor P — EarnedPath PERT Viability (Path Accessibility)

EarnedPath = CPM × WBS + PERT. The PERT component is probabilistic accounting of alternative-path viability.

```
P(t) = 1 / (1 + viable_alternative_cost_penalty)

where:
  viable_alternative_cost_penalty = Σ (cost_of_deviation_i / available_budget)
                                    over alternatives i with cost_ratio ≤ κ_cost
  κ_cost = 3.0  (domain-configurable; alternatives up to 3× current path cost)
```

If no alternative satisfies cost_ratio ≤ κ_cost, P(t) = 0.

### 3.6 Factor F — Future-Map Convergence (Intergenerational Integrity)

Divergence between the decision's trajectory and the ERES 1000-Year Future Map target. Five dimensions, each on [0, 1]:

1. **Ecological sustainability** — projected ecosystem integrity under the decision trajectory
2. **Social equity persistence** — projected equity preservation across generations
3. **Technical debt accumulation** (inverted) — lower accumulation = higher factor
4. **Intergenerational option preservation** — number of viable trajectories preserved for future cohorts
5. **Resilience to shock** — projected system response capacity to exogenous perturbation

```
F(t) = max(0, 1 - ||vector(t) - (1,1,1,1,1)|| / √5)
```

F operationalizes the third Governing Principle ("build for generations to come") as structural measurement, not rhetorical commitment.

### 3.7 Conjunctive Evaluation — Normative

Implementations MUST evaluate PoR as the product of the four factors. Weighted-sum evaluation is non-conformant (Section 12, Security Considerations — scalar-collapse attack).

### 3.8 Threshold θ

Reference values, MIEVM-concurred:

| Domain | θ | Rationale |
|---|---|---|
| High-consequence governance (Hague, DOFA, Constitutional) | 0.85 | Strict; false-positive refusals tolerable |
| Standard governance (Family Stewardship, civic council) | 0.75 | Default; balanced |
| Infrastructure control | 0.75 | Default |
| Advisory / research | 0.60 | Permissive; informative rather than gating |

Deployments MUST document their chosen θ with justification against decision-latency and false-positive tolerance.

---

## 4. Decision Space Accessibility Protocol (DSAP)

### 4.1 DSAP Scope

DSAP is the structural detection layer for premature convergence — measured openness rather than declared openness.

DSAP is specified as the continuous evaluation of Factors R, P, F of PoR. These three factors together measure *whether the decision space remains open*, as distinct from Factor A's measure of *whether the current state is coherent*.

### 4.2 DSAP Detection

DSAP detects three failure modes:

- **Flatlined RHC** — system has become internally coherent at the cost of ceasing to re-open. Factor R drops.
- **Foreclosed PERT** — alternatives have become prohibitively expensive or dropped from the active set. Factor P drops.
- **Divergent future map** — current trajectory forecloses long-horizon options. Factor F drops.

A system can exhibit one or more while scoring high on Factor A and on external signals of diversity. The conjunctive product makes this condition unauthorizable by construction.

### 4.3 DSAP Scope Limit

DSAP as specified measures *degradation* of decision-space accessibility — the point at which R, P, or F crosses its component threshold. DSAP does not detect *regime transition* — the moment a system enters a basin of attraction from which irreversibility is inevitable while all four factors still evaluate above threshold.

Regime-transition detection is specified in Section 6 as DSAP-PRE.

---

## 5. RT Qualifier and Continuous Evaluation

### 5.1 Dial Tone, Not Key

Authorization under v1.3 is a live state, not an issued token. An authorized principal is tuned to resonance; a principal that has fallen out of tune is no longer authorized, regardless of any prior grant.

This is the architectural distinction from conventional token-based authorization: a token can outlive the conditions that justified its issuance. A dial tone cannot outlive the connection that produces it.

### 5.2 Freshness Window

Every authorization read is qualified by freshness. A read is valid only if the principal's latest RESONANCE-TUNE record on GraceChain is within the freshness window.

**Default freshness window = one RHC cycle.**

RHC cycle reference timings (domain-dependent, MIEVM-concurred):

| Domain | RHC cycle duration |
|---|---|
| High-frequency trading / real-time control | 5 seconds |
| Infrastructure / enterprise IT | 30 seconds |
| Standard governance | 1 hour |
| Strategic / intergenerational | 1 day |

Deployments MUST document their RHC cycle with justification against decision latency.

### 5.3 Staleness Semantics

A principal whose latest RESONANCE-TUNE is older than the freshness window is STALE. STALE reads return unauthorized regardless of prior RATE or prior grant. Restoration requires a fresh RESONANCE-TUNE with MIEVM concurrence; it does not revive automatically.

---

## 6. DSAP-PRE — Pre-Threshold Boundary Condition (Structurally Upstream)

### 6.1 Structural Positioning — Boundary Condition, Not Internal Component

**DSAP-PRE is a structurally upstream boundary condition**, not an internal subsystem of EAAP. It is positioned as a distinct layer above EAAP's qualification work, parallel to how VBE™ (Section 7) is positioned as a distinct layer below EAAP's qualification work at execution. EAAP integrates DSAP-PRE as its upstream precondition; EAAP does not contain DSAP-PRE.

This positioning is material. DSAP-PRE operates on state-space topology rather than on state-consistency scoring; its mathematics (ERES-SEPARATRIX-MATH-2026-001-v2) is distinct from EAAP's conjunctive-product form; its failure mode (regime transition before any measurable state-level degradation) is upstream of every other ERES authorization layer including admission (BODY) and logical gating (BRAINS). A system that has crossed the pre-threshold boundary cannot be rescued by tighter qualification downstream. The boundary must be named, measured, and refused as a layer in its own right.

Per the peer review that identified this construct, DSAP-PRE must be treated "as a boundary condition in its own right, not reduced to an internal component of the existing stack" (Skulski, April 24, 2026). v1.3-FINAL preserves that structural positioning:

- **DSAP-PRE** is specified in the companion document ERES-SEPARATRIX-MATH-2026-001-v2, which is the authoritative mathematical document for the boundary condition.
- **Section 6 of this specification** documents how EAAP *integrates* DSAP-PRE as an upstream precondition to qualification, parallel to how Section 7 documents integration of VBE™ as a downstream enforcement layer.
- **Downstream implementations** MUST treat DSAP-PRE as architecturally independent; reductive treatments that collapse DSAP-PRE into EAAP qualification scoring are non-conformant (Section 14).

### 6.2 Construct

DSAP-PRE addresses the failure mode identified by Andrzej Skulski (LinkedIn correspondence, April 22–23, 2026): the moment a system enters a regime of irreversible path dependency while all four PoR factors still evaluate above threshold. This is separatrix crossing — boundary-crossing in state space between basins of attraction, well-studied in dynamical systems as hysteresis, catastrophe folds, and tipping-point dynamics.

### 6.3 Three Proxies

Per ERES-SEPARATRIX-MATH-2026-001-v2, three proxies detect precursor signatures:

**Proxy ρ_RHC — Second-derivative analysis.** Critical slowing down manifests as RHC amplitude not yet flatlined but declining at accelerating rate.

```
ρ_RHC(t) = 1  if  (A'(t) < 0) and (A''(t) < -κ_RHC) sustained over W_RHC
ρ_RHC(t) = 0  otherwise
  W_RHC = 3 RHC cycles
  κ_RHC = domain-calibrated acceleration threshold
```

**Proxy ρ_PERT — Distribution topology.** Decision-space convergence manifests as modality collapse, variance collapse, or viable-alternative-set collapse in the PERT distribution.

```
ρ_PERT(t) = 1  if any of:
    modality(D_PERT) decreased from >1 to 1 within W_PERT (bimodal → unimodal)
    σ̃²(D_PERT) decreased by >50% within W_PERT
    n_viable(D_PERT) decreased by >50% within W_PERT
ρ_PERT(t) = 0  otherwise
  W_PERT = 5 evaluations
```

**Proxy ρ_hyst — Hysteresis counterfactual.** Direct irreversibility test: would optionality recover if conditions reversed?

```
H(t) = Ψ(S(t), Π(t) + Δ_Π, τ) - Ψ(S(t), Π(t), τ)

ρ_hyst(t) = 1  if  H(t) ≤ η_recover
ρ_hyst(t) = 0  otherwise
  τ = 10 RHC cycles (projection horizon)
  Δ_Π = 0.5 × recent parameter movement (restoration magnitude)
  η_recover = domain-calibrated recovery threshold
```

### 6.4 DSAP-PRE Composite

```
DSAP-PRE(t) = (1 - ρ_RHC(t)) × (1 - ρ_PERT(t)) × (1 - ρ_hyst(t))
```

DSAP-PRE ∈ [0, 1]. DSAP-PRE = 1 when no pre-threshold condition is firing; DSAP-PRE = 0 if any proxy fires.

### 6.5 Integration with EAAP — Gating Precondition (Mode A)

For high-consequence domains (governance, safety-critical infrastructure, legal authority), DSAP-PRE operates as a **gating precondition** upstream of EAAP qualification:

```
if DSAP-PRE(t) == 0:
    refuse authorization with REFUSAL_REGIME_TRANSITION
    do not proceed to PoR evaluation
```

For advisory domains, Mode B (joint conjunctive product DSAP-PRE × PoR > θ_joint) is permitted.

v1.3-FINAL normative default: **Mode A** for all θ ≥ 0.75 domains.

The gating precondition structure is what preserves DSAP-PRE's status as a boundary condition rather than as an internal scoring factor. A zero from DSAP-PRE refuses authorization *before* qualification begins; it does not contribute to a weighted score that qualification produces.

---

## 7. VBE™ — Validation Before Enforcement (Runtime Containment Integration)

### 7.1 External Framework — Integrated, Not Originated

**Validation Before Enforcement (VBE™)** is an independent execution-layer governance framework authored under **JusticeTree AI™** by Teresa Villa. VBE™ is not an ERES invention and is not originated within the ERES framework. EAAP v1.3-FINAL **integrates** VBE™ as the runtime containment layer of the ERES authorization stack per the contributed papers *Runtime Containment Layer: Preliminary Interface Notes* and *VBE — Execution-Binding Model (Inner Workings)* (Villa, April 23, 2026).

This section reproduces the integrated VBE™ specification by reference and agreement. VBE™ remains JusticeTree AI™ IP. All references to VBE™ in this specification, in companion documents, and in downstream implementations MUST preserve this attribution and architectural distinction. Implementations that incorporate VBE™ are integrating a distinct framework, not implementing an ERES subsystem.

The failure mode VBE™ closes, per Villa:

> *Logical validity upstream does not guarantee enforced validity downstream.* — T. Villa

EAAP, BRAINS, and GraceChain together specify how authorization is computed, qualified, and recorded. None specify how authorization becomes non-bypassable at the point of execution. VBE™ closes that gap as an external integrated layer, not as an internal EAAP component.

### 7.2 Required Invariant

> *No validation = no action. No fresh authorization record = no execution.* — T. Villa

Specifically:

1. No execution path may complete unless bound to a fresh authorization check.
2. No component may rely solely on previously issued or transported authorization state.
3. Every action must be linked to a current, verifiable authorization record generated within the applicable freshness window.
4. Failure to validate must fail closed at the execution boundary, not merely create a compliance defect after the fact.

This distinguishes an **enforceable system** from a merely **compliant system**.

### 7.3 Execution Interception

All executable actions MUST route through a VBE gate sitting at one of:

- API gateway
- Service middleware
- Orchestration layer
- System boundary (where actions are actually committed)

There MUST be no direct execution paths outside this boundary.

### 7.4 Required Execution Flow

```python
def execute(action, actor, context):
    state = GraceChain.read_latest(actor)

    if not state:
        deny("NO_STATE")

    if stale(state):
        deny("STALE")

    if not PoR_valid(state):
        deny("INVALID_STATE")

    if not BRAINS_pass(state, action):
        deny("POLICY_FAIL")

    # DSAP-PRE precondition (Mode A)
    if DSAP_PRE(state) == 0:
        deny("REGIME_TRANSITION")

    record = emit_execution_record(
        action_id=action.id,
        actor=actor,
        state_snapshot=state.hash,
        por_snapshot=state.por_factors,
        timestamp=now()
    )

    if not record:
        deny("NO_RECORD")

    allow(action)
```

### 7.5 Non-Bypassable Constraint

The critical property is not the checks — it is the **dependency**: the execution path MUST require a valid authorization record to complete. Therefore:

- Action commit is gated on record creation.
- No record → no side effect.

Even if a component tries to skip validation, it cannot produce a valid execution record, and downstream systems reject the action.

### 7.6 Replay Resistance

Each execution record is:

```
AUTH = (action_id, actor, state_hash, por_snapshot, timestamp)
```

Validation requires:
- Uniqueness of action_id
- Freshness of timestamp (within RT window per Section 5)
- Match to current state

This prevents replay of prior valid states and cross-boundary reuse.

### 7.7 Failure Mode — Fail Closed (By Design)

Default behavior: **FAIL CLOSED**. If anything is missing, stale, or unverifiable → execution does not occur.

### 7.8 Cross-System Enforcement

An action originating in System A and crossing into System B cannot present a grant from System A alone. The grant MUST carry MIEVM ensemble co-signatures recorded on GraceChain. System B verifies by reading the grant's current state on GraceChain, not by trusting System A's claim. If MIEVM concurrence has been withdrawn since the grant issued, the current-state read returns revoked regardless of what System A presents.

---

## 8. DSAP-PRE Sovereignty Layer Mapping

### 8.1 Construct — Per Teresa Villa

This section incorporates Teresa Villa's contributed paper *DSAP-PRE — Sovereignty Layer Mapping (Pre-Threshold Detection)* (April 23, 2026), which maps the separatrix condition across three sovereignty domains.

The mapping establishes the separatrix condition as cognitive (personal), communicative (public), and structural (private) — rather than purely state-based. This grounds DSAP-PRE's abstract mathematics in concrete sovereignty-preservation applications.

### 8.2 Personal Sovereignty (Mind's Eye)

**Definition:** Internal access to viable alternatives prior to external constraint.

**Pre-threshold failure mode:**
- Perceived option set collapses while objective options still exist
- Narrowing of internal evaluation (tunnel formation)
- Decision becomes internally "inevitable" before externally constrained

**Observable proxies (aligned to DSAP-PRE):**
- ρ_RHC → reduced cognitive reopening (cycle no longer re-expands)
- Rising commitment rigidity across successive evaluations
- Decreasing variance in internally generated alternatives

**Interpretation:** The agent crosses a cognitive separatrix before external enforcement occurs.

### 8.3 Public Sovereignty (Discourse)

**Definition:** Real accessibility of alternatives within shared discourse.

**Pre-threshold failure mode:**
- Discourse converges to a single acceptable trajectory
- Alternatives remain nominally present but are socially or structurally non-viable
- Participation persists, but outcome space is effectively closed

**Observable proxies (aligned to DSAP-PRE):**
- ρ_PERT → shift from multi-modal to unimodal distribution
- Collapse in viable alternative count despite nominal option set
- Divergence between expressed diversity and actionable paths

**Interpretation:** The decision space collapses in discourse before formal restriction.

### 8.4 Private Sovereignty (Contractual / Binding)

**Definition:** Preservation of real optionality within formal commitments and procedural structures.

**Pre-threshold failure mode:**
- Commitments form under conditions where reversal cost has already become prohibitive
- Procedural pathways lock future states before constraint is explicitly recognized
- Binding occurs after effective irreversibility has already been reached

**Observable proxies (aligned to DSAP-PRE):**
- ρ_hyst → failure to recover under parameter reversal
- Asymmetry between forward commitment and backward exit cost
- Path dependency detectable before threshold breach

**Interpretation:** The system crosses into a binding regime where reversal is structurally inaccessible.

### 8.5 Composite Interpretation

Across all three domains, DSAP-PRE detects:

> **Loss of accessible alternatives prior to threshold failure.**

This establishes the separatrix condition as cognitive (personal), communicative (public), and structural (private) — rather than purely state-based.

### 8.6 Relationship to VBE

DSAP-PRE detects pre-threshold sovereignty collapse. VBE ensures that collapse is not converted into execution. Together:

> **Detection before → enforcement at execution.** — T. Villa

This pairing is the architectural closure of the April 22–23 peer-review sprint.

---

## 9. MIEVM — Multi-Instrument Ensemble Validation Method

### 9.1 Canonical Expansion

MIEVM = **Multi-Instrument Ensemble Validation Method** (MPAM §8 canonical). Prior occurrences of "Multi-Instance Ensemble Validation" in v1.2 and v1.3-DRAFT are superseded. "Multi-Instrument" is authoritative from v1.3-FINAL forward because it describes what the ensemble *is* — diverse instruments with different strengths — rather than mere duplication.

### 9.2 MPAM ↔ MIEVM Duality

From ERES-MPAM-2026-001 §8:

> MPAM is the protocol by which mathematical frameworks are admitted, contained, and integrated into the ERES stack. MIEVM is the runtime by which that protocol is executed against any specific candidate. MPAM without MIEVM is architecture without execution. MIEVM without MPAM is ensemble without principle.

### 9.3 Ensemble Composition Rules

**Current canonical ensemble** (v1.3-FINAL, April 2026):
- Claude (Anthropic)
- ChatGPT (OpenAI)
- Grok (xAI)
- DeepSeek (DeepSeek AI)

**Optional extended ensemble** (for higher-stakes evaluations):
- Perplexity (per MPAM self-evaluation, April 14, 2026)

Composition rules:
- **Minimum ensemble size:** 3 for MIEVM-recognized concurrence. Below 3 is single-opinion work, not MIEVM.
- **Independent decomposition:** Each instrument MUST evaluate independently, without coordination. Convergence is therefore evidential, not collusive.
- **Morally-vectored end-condition:** All evaluations oriented toward BEST / SOUND / GOOD outcomes, not toward any single instrument's preference function.
- **Provenance-locked residuals:** Every evaluation timestamped, attributed, permanent. The ensemble cannot retroactively revise convergence; it can only add new evaluations.

### 9.4 ECR — Erasure Completeness Ratio (Convergence Metric)

For a candidate framework C evaluated by ensemble E = {M₁, M₂, …, Mₙ}:

- Each Mᵢ produces evaluation Eᵢ(C) = (score, strengths, gaps, integration_recommendations)
- Residual R(C) = intersection of substantive critique across ensemble (gaps surviving multiple independent evaluations)
- Noise N(C) = symmetric difference (claims made by some but not corroborated by others)

```
ECR(C) = |R(C)| / (|R(C)| + |N(C)|)
```

**ECR interpretation:**

| ECR range | Interpretation | Action |
|---|---|---|
| ≥ 0.75 | High convergence, warranted confidence | Integrate |
| 0.50–0.74 | Moderate convergence | Integrate with Narrative-mode caveats |
| < 0.50 | Genuine ambiguity | Defer, expand ensemble, or restrict to speculative tier |

### 9.5 Instrument-of-Faith Framing

Naive ensemble methods average outputs and treat the average as truth. MIEVM does not. MIEVM treats convergence as calibrated trust — faith in the technical sense of *warranted confidence under bandwidth constraint*.

This is the same epistemology that produced the 72 Key Domains — culled from the Register of Collective Indices by VPN renewal capacity during Global_VPN work — and it is the same epistemology that produced the four-member MIEVM short-list itself.

### 9.6 Selection Criteria — INPUT DETAIL METHODOLOGY

Selection of the four canonical ensemble members was governed by:

1. **Independence of training lineage.** No two ensemble members share majority training data.
2. **Diversity of optimization objective.** Each instrument optimizes against a different combination of safety, helpfulness, capability, and speed priorities.
3. **Availability of API provenance.** Each instrument provides auditable, timestamped invocation records.
4. **Bandwidth match to solo-researcher cadence.** Four instruments fit a single researcher's evaluation throughput; adding a fifth exceeds available review time per candidate. This is the same constraint-based culling epistemology that produced the 72 Key Domains.
5. **Capacity for adversarial review.** Each instrument must be capable of substantive critique, not merely agreement.

### 9.7 Five-Tier Containment Stack

Per MPAM, mathematical and specification contributions to ERES are admitted into one of five tiers:

| Tier | Layer | Role in EAAP v1.3 |
|---|---|---|
| 0 | Foundation (Canon) | Triune Math; Three Governing Principles; MPAM-MIEVM duality |
| 1 | Operational | BERA indices, EAAP Sections 3-7, SCALULAR, UBIMIA |
| 2 | Educational | UDL, Innovamat, CCSSM, EarnedPath pedagogy |
| 3 | Interface | VERTECA, PlayNAC surfaces, GAIA dashboards |
| 4 | Speculative | UMF, future submissions (contained) |
| 5 | Archive | De-assimilated components, retained for historical reference |

EAAP v1.3-FINAL itself is a **Tier 1 (Operational)** specification. Its foundational dependencies (Triune Math, Three Governing Principles) are Tier 0.

### 9.8 De-Assimilation Triggers (D1–D6)

Per MPAM §9, any specification admitted under MIEVM may be de-assimilated (principled removal with full provenance) if:

- **D1** — Source Retraction (originating authority withdraws)
- **D2** — Superior Replacement (new candidate demonstrably outperforms on ≥3 of 4 Fit Test axes)
- **D3** — Empirical Contradiction (operational use produces outcomes contradicting predicted behavior)
- **D4** — Containment Breach (component leaks across tier boundaries)
- **D5** — Stakeholder Withdrawal (institutional basis dissolves)
- **D6** — Sunset Clause (review interval elapsed, re-validation fails)

De-assimilation is itself MIEVM-concurred. No single-source removal.

### 9.9 MIEVM Concurrence Record for v1.3-FINAL

This specification's MIEVM concurrence record:

- **v1.0 synthesis (2026-04-22):** ChatGPT + DeepSeek + USE.ai/Claude independent drafts → ERES-CRYPTO-STD-2026-001-v1.0 synthesized. ECR estimated 0.71 (moderate-high).
- **v1.1.1 hardening (2026-04-22):** USE.ai adversarial review produced 10 findings; all 10 resolved. ECR risen to estimated 0.85.
- **v1.2 → v1.3-DRAFT (2026-04-23):** LinkedIn review by Skulski (four turns) + Villa (three signed documents). Named peer-reviewer residual: state-vs-path distinction, separatrix crossing, runtime containment, sovereignty mapping. All incorporated.
- **v1.3-FINAL concurrence target (2026-04-24):** Ensemble re-review of this document across Claude, ChatGPT, Grok, DeepSeek. Provenance recorded on GraceChain per Section 11 of the GraceChain Notes.

---

## 10. Byte-Normative Test Vectors

### 10.1 Test Vector A — Inherited from ERES-CRYPTO-STD-2026-001-v1.1.1

The authoritative keypair, nonce, and payload are inherited unchanged from ERES-CRYPTO-STD-2026-001-v1.1.1 Section 20, verified via round-trip under Ed25519:

```
Test keypair seed    = SHA-256("ERES-CRYPTO-STD-2026-001-v1.1-TEST-KEY-C")
Private seed (hex)   = f2f794def2ea5d19ecb0f894716932654eb173195c451b2cccb9770ab2874691
Public key   (hex)   = 04e552e2c8ee4d34be854a1ca808600183f0afcfa8a4d063eb7c1e1bb7fecf68
Test nonce   (hex)   = 00112233445566778899aabbccddeeff
Test timestamp       = 2026-04-22T14:32:17.042Z

Canonical payload length = 510 bytes
Payload SHA-256 (hex)    = 2f751f1bf59d5a2b7b5682e280bcc523bd0ea7384433a9814d8deebc821d7acd
σ (HKDF-SHA256) (hex)    = e43732833d50a0502dab120d33fa05537bb4a069957f3aba293ebe62aba50ad7
GCF primitive resolved   = G3  (index 2 of [G1, G2, G3])

RATE.vector              = [10, 10, 10, 9, 8, 9, 10]
RATE.score               = 9.428571
RATE.confidence          = 0.869293
Status                   = ACCEPT
```

Both signatures (role-C attestation and RSIG) verify against the published public key.

### 10.2 PoR Factor Test Vectors (v1.3 Extension)

Four PoR-factor vectors using the Test Vector A keypair as authorization context:

**Vector PoR-1 — Authorized state (high on all four factors)**
```
A = 0.95,  R = 0.95,  P = 0.95,  F = 0.95
PoR = 0.95 × 0.95 × 0.95 × 0.95 = 0.814  ≥ 0.75  → AUTHORIZED (standard governance)
Applicable domain threshold θ = 0.75
```

**Vector PoR-2 — Path-foreclosed state (Andrzej failure mode)**
```
A = 0.95,  R = 0.95,  P = 0.40  (no viable alternatives remain),  F = 0.95
PoR = 0.95 × 0.95 × 0.40 × 0.95 = 0.343  < 0.75  → UNAUTHORIZED
Refusal reason: PoR_FAIL (Factor P below conjunctive contribution)
```

**Vector PoR-3 — Regime-transition state (DSAP-PRE catches what PoR would miss)**
```
A = 0.90,  R = 0.82  (declining but above flatline),  P = 0.85,  F = 0.88
PoR = 0.90 × 0.82 × 0.85 × 0.88 = 0.552  (would fail θ=0.75 anyway)

But also:
ρ_RHC = 1  (A''(t) below -κ_RHC sustained)
DSAP-PRE = (1-1) × (1-0) × (1-0) = 0
Refusal reason: REGIME_TRANSITION (DSAP-PRE precondition fails; PoR not evaluated)
```

**Vector PoR-4 — Stale authorization**
```
Last RESONANCE-TUNE timestamp = 35 seconds ago
Freshness window (infrastructure RHC) = 30 seconds
→ STALE → UNAUTHORIZED
Refusal reason: STALE (RT qualifier violation)
```

**Vector PoR-5 — Self-certification attempt**
```
Node produces RATE claiming anchor product with M=0.9 but no MIEVM signatures present.
Factor M structurally evaluates to 0 (Section 3.3, Section 9.3).
A = U × S × R × B × 0 × G × T = 0
PoR = 0 × R × P × F = 0
Refusal reason: NO_MIEVM_CONCURRENCE
```

### 10.3 VBE Execution Record Test Vector

```json
{
  "action_id": "dofa-council-auth-2026-04-24-0001",
  "actor": "ERES-TEST-PRINCIPAL-C",
  "state_hash": "2f751f1bf59d5a2b7b5682e280bcc523bd0ea7384433a9814d8deebc821d7acd",
  "por_snapshot": {"A": 0.95, "R": 0.95, "P": 0.95, "F": 0.95, "PoR": 0.814},
  "rate_vector": [10, 10, 10, 9, 8, 9, 10],
  "dsap_pre": 1.0,
  "timestamp": "2026-04-24T10:15:30.000Z",
  "mievm_concurrence": ["claude_sig", "chatgpt_sig", "grok_sig", "deepseek_sig"],
  "vbe_record_status": "BOUND"
}
```

### 10.4 Canonical Serialization

RATE vector remains 7-dimensional per ERES-CRYPTO-STD-2026-001-v1.1.1 (CBGMODD 7-role civic composition). PoR factors are carried as a separate structured field, not as a replacement for RATE. v1.2 wire compatibility is preserved.

---

## 11. Worked USE-CASE — DOFA Family Stewardship Council Authorization

### 11.1 Context

This section demonstrates the complete EAAP v1.3 stack operating on an authorization request from the Department of Family Amity (DOFA) Family Stewardship Council per ERES-DOFA-WP-2026-001-C (RG#420). The USE-CASE is chosen for three reasons:

1. DOFA is an existing ERES governance instrument with a defined seven-seat CBGMODD council structure that maps naturally to the RATE vector.
2. DOFA's Version C explicitly couples policy, measurement, and closed feedback loop — the "enforceable system" that v1.3-FINAL is built to specify.
3. A Family Stewardship Council decision is consequential (affects household-level fiscal allocation) but not emergency-paced (standard-governance RHC cycle, 1 hour), making it a realistic Mode A domain.

### 11.2 Scenario

The DOFA Family Stewardship Council is considering Authorization Request **DOFA-FSC-2026-04-24-001**: release of Family Amity Fund allocation to an identified household under IDIPITIS fiscal clearinghouse protocol. Amount: $4,800 annual. Duration: 12 months. Renewal gate: per-quarter BERA re-evaluation.

Actor: Council chair (CBGMODD role = Mediator).
Context: Quarterly allocation cycle.
Stakes: Household-level fiscal, multi-generational if recurring.

### 11.3 Stack Execution

**BODY Consolidation (admission)** — Household application data (IDIPITIS form, BERA baseline, EarnedPath declaration) passes structural validity check. Not VEILED. → ADMIT

**DSAP-PRE (§6, Mode A precondition)** —
- ρ_RHC: RHC amplitude stable over last 3 cycles → 0
- ρ_PERT: Household has 4 viable fiscal paths (DOFA fund, state assistance, private credit, non-action) → 0
- ρ_hyst: Counterfactual under fund denial projects recovery via state assistance → 0
- DSAP-PRE = (1-0) × (1-0) × (1-0) = **1.0** → PROCEED

**BRAINS Trifecta (execution gate)** —
- ONE-GOOD (intergenerational integrity): 0.94
- SECURITY-CLEARANCE (verification of household identity via FAVORS): 0.91
- DATA-INTEGRITY (IDIPITIS form completeness): 0.98
- Trifecta product: 0.94 × 0.91 × 0.98 = 0.84 → PASS threshold 0.75 → PROCEED

**EAAP Qualification / PoR (§3)** —
- Factor A (anchor product, 7 anchors): 0.93
- Factor R (RHC amplitude): 0.95 (healthy cycle, no flatline)
- Factor P (PERT viability): 0.88 (four viable alternatives including non-action preserved)
- Factor F (future-map convergence, 5 dimensions): 0.90
- **PoR = 0.93 × 0.95 × 0.88 × 0.90 = 0.699** ... below θ = 0.75 for standard governance.

**Outcome: UNAUTHORIZED.** Refusal reason: PoR_BELOW_THRESHOLD.

### 11.4 Outcome Analysis

The refusal appears counterintuitive — all component factors are individually healthy. This is the conjunctive-product design speaking: **four factors at 0.88–0.95 individually multiply to a PoR below standard-governance threshold**. The system is telling the Council that while the decision looks fine on any one axis, the compound resonance is insufficient for unconditional authorization at this moment.

Three legitimate responses are available to the Council:

1. **Accept the refusal** and defer authorization one RHC cycle (1 hour in standard governance), re-evaluating after Factor F (future-map) or Factor A (anchor product) improves.
2. **Lower the threshold to advisory domain (θ = 0.60)** for this specific request class and re-evaluate. PoR = 0.699 > 0.60 → AUTHORIZED (advisory). This must be MIEVM-concurred as a class-wide threshold decision, not an ad-hoc exemption.
3. **Request additional context** that would raise Factor F specifically — typically supplementary household documentation on intergenerational planning, technical-debt projection, or resilience factors.

### 11.5 VBE Execution-Binding

If the Council accepts response (2) and authorization proceeds, VBE produces the execution-bound record:

```
VBE AUTH:
  action_id = "DOFA-FSC-2026-04-24-001"
  actor = "Council-Chair-Mediator-C"
  por_snapshot = (0.93, 0.95, 0.88, 0.90, 0.699)
  threshold_applied = 0.60 (advisory, class-concurred)
  dsap_pre = 1.0
  mievm_sigs = [4 ensemble signatures]
  timestamp = 2026-04-24T10:15:30Z
  status = BOUND-ADVISORY
```

The IDIPITIS disbursement routine MUST read this VBE record before transferring funds. No record → no transfer.

### 11.6 Why This USE-CASE Demonstrates 10/10

The DOFA scenario demonstrates:

- **Separation of concerns** (every layer refused or passed on its own terms)
- **Conjunctive-product discipline** (no single factor hides compound weakness)
- **Threshold flexibility with MIEVM accountability** (class-wide re-threshold requires ensemble concurrence)
- **Path accessibility preservation** (refusal is a defer-and-re-evaluate, not a permanent denial)
- **Legible refusal** (every refusal reason is a named code with document provenance)
- **VBE binding** (the authorization record carries the specific PoR values that justified it; no replay possible)
- **Three Governing Principles operationalized** (Don't hurt yourself — household welfare; Don't hurt others — fiscal responsibility; Build for generations to come — Factor F explicit)

This is ethics-as-legibly-stated-infrastructure operating on a real governance instrument. Per the accompanying Convergence Proof analysis: the two-room convergence (Anthropic's Constitutional AI at the model layer; ERES's EAAP at the protocol layer) is demonstrated here not as rhetoric but as running code.

---

## 12. Security Considerations

The cryptographic primitives of v1.2 (attestation composition separated from primitive cryptography, non-compensation intent, audit persistence) are retained unchanged. v1.3-FINAL adds:

- **Scalar-collapse attacks.** Implementations that evaluate four PoR factors as weighted sum rather than conjunctive product are vulnerable to compensation: three high factors masking one collapsed factor. Implementations MUST use the conjunctive product form.
- **Staleness replay.** Implementations that do not enforce the RT qualifier are vulnerable to replay of previously valid RATE vectors. Implementations MUST check freshness on every read.
- **Self-certification.** Implementations permitting a single node to certify its own PoR are vulnerable to internal-coherence failure mode. Implementations MUST require MIEVM ensemble concurrence for Factor M.
- **Declared-openness attestation.** Implementations treating declared deliberation signals as satisfying DSAP are vulnerable to premature convergence with preserved appearance. Implementations MUST use measured factors (R, P, F), not declared signals.
- **Pre-threshold bypass.** Implementations evaluating only PoR without DSAP-PRE are vulnerable to regime-transition authorization — high-scoring systems that have crossed a separatrix. Implementations in high-consequence domains MUST include DSAP-PRE as Mode A gating precondition.
- **Runtime bypass.** Implementations without VBE runtime containment are vulnerable to components that cache authorization or never call authorize(). Implementations MUST route all executable actions through VBE gates at API/middleware/orchestration boundaries.
- **Sovereignty-layer erosion.** Per Section 8, pre-threshold sovereignty collapse is cognitive, communicative, and structural in addition to state-based. Implementations evaluating only state metrics miss the earlier signatures. Implementations monitoring civic or governance systems SHOULD evaluate all three sovereignty domains per Section 8.2–8.4 proxies.

---

## 13. Protocol vs. Governance Guarantees

Per ERES-CRYPTO-STD §15.6 discipline, v1.3-FINAL separates what the protocol guarantees (cryptographic) from what depends on governance-policy quality:

**Protocol guarantees (5):**
1. Attestation binding under Ed25519 with HKDF-SHA256 nonce binding.
2. RATE vector structural integrity (7-dimensional CBGMODD).
3. PoR conjunctive product non-compensation.
4. Freshness enforcement via RHC-cycle-bound RT qualifier.
5. Execution-record non-bypass via VBE gate.

**Governance-policy-dependent guarantees (5):**
1. Appropriate θ threshold selection per domain.
2. Calibration of DSAP-PRE proxy parameters (κ_RHC, κ_cost, η_recover).
3. MIEVM ensemble composition and concurrence procedures.
4. Class-wide threshold decisions (advisory re-threshold).
5. Tier-placement decisions for de-assimilation.

A reviewer's confidence in (1)–(5) protocol claims is independent of judgments about (1)–(5) governance. This separation is normative, not stylistic.

---

## 14. Conformance

An implementation claiming conformance to EAAP v1.3-FINAL MUST:

1. Compute PoR as conjunctive product of four factors per Section 3.
2. Implement DSAP as measured openness via R, P, F per Section 4.
3. Implement DSAP-PRE per Section 6 (Mode A for θ ≥ 0.75 domains).
4. Route all executable actions through a VBE gate per Section 7.
5. Map DSAP-PRE proxies to the three sovereignty domains per Section 8 where the application touches human decision-making.
6. Evaluate authorization under continuous RT qualifier per Section 5.
7. Require MIEVM ensemble concurrence (minimum ensemble size 3) per Section 9.
8. Record all authorizations on GraceChain per ERES-GRACECHAIN-NOTES-2026-001-v1.
9. Reproduce the byte-normative test vectors of Section 10.
10. Document domain-specific θ, RHC cycle, and DSAP-PRE calibration parameters with published justification.

### 14.1 Named Contributor Invariants (Villa V1–V3)

Per the Named Contributor approval conditions recorded in Section 15.1, a conformant implementation MUST additionally preserve:

**V1.** VBE™ as a non-bypassable execution constraint (not a scoring or advisory layer). Reclassification of VBE™ as advisory is non-conformant.

**V2.** Orthogonality between DSAP-PRE (detection) and VBE™ (enforcement). Merging the two layers, or subordinating one to the other, is non-conformant.

**V3.** Named, stable attribution to Villa and to JusticeTree AI™ for VBE™ (Section 7) and sovereignty-domain mapping (Section 8). VBE™ MUST be preserved as externally-authored JusticeTree AI™ IP integrated into ERES, not as an ERES-originated component. Revisions that remove, generalize, or re-origin this attribution without Villa's written consent are non-conformant.

Non-conformant alternatives are documented in Security Considerations (Section 12).

---

## 15. Reviewer Position Statements and Attribution

This specification incorporates work from external contributors whose review positions are reproduced here in their own stated scope. Contributions are credited only to the extent each contributor has explicitly authorized, per the ERES Attribution Protocol (ERES-ATTRIBUTION-PROTOCOL-2026-001-v1). **No reviewer should be read as endorsing the framework as a whole; each position statement defines its own boundary.**

### 15.1 Named Contributor Position Statement — Teresa Villa

**Affiliation:** Founder, JusticeTree AI™ (per LinkedIn public profile)
**LinkedIn:** https://www.linkedin.com/in/ACoAADpxVilla/ (profile record at correspondence time, April 2026)
**Framework authored:** Validation Before Enforcement (VBE™), an independent execution-layer governance framework under JusticeTree AI™. VBE™ is integrated into EAAP v1.3-FINAL as the runtime containment layer (Section 7), not originated within ERES.

**Contributed documents (signed, April 23, 2026):**
1. *Runtime Containment Layer: Preliminary Interface Notes*
2. *VBE — Execution-Binding Model (Inner Workings)*
3. *DSAP-PRE — Sovereignty Layer Mapping (Pre-Threshold Detection)*

**Villa's stated approval position (April 24, 2026, 8:47 PM), reproduced with permission:**

> From my perspective, the architecture is now coherent across all three layers:
>
> - DSAP-PRE → pre-threshold detection (regime transition boundary)
> - EAAP / BRAINS / GraceChain → qualification and logical authorization
> - VBE → execution-layer enforcement (runtime containment)
>
> That separation is critical, and in this version it is correctly maintained.

**Villa's clarification for the record (April 24, 2026, 8:48 PM), reproduced with permission:**

> Joseph — Yes, I approve the EAAP v1.3-FINAL and DSAP-PRE math sheet for publication. One clarification for the record: Validation Before Enforcement (VBE™) is an independent execution-layer governance framework authored under JusticeTree AI™ (Teresa Villa). Its inclusion in EAAP v1.3-FINAL constitutes integration as the runtime containment layer, not origination within the ERES framework. All references to VBE should preserve this attribution and architectural distinction. With that clarification, I'm aligned for ResearchGate submission. — Teresa

**Three conditions Villa stated for approval — recorded here as normative invariants this specification undertakes to preserve:**

**Invariant V1 — Execution-Layer Boundary (VBE™).** VBE™ is correctly positioned as a non-bypassable execution constraint, not a scoring or advisory layer. Its role as the enforcement boundary between authorization and action MUST remain preserved in all downstream implementations and in any revision of this specification. Reclassification of VBE™ as advisory or scoring is non-conformant.

**Invariant V2 — Layer Separation (DSAP-PRE vs VBE™).** DSAP-PRE and VBE™ MUST remain orthogonal by design: DSAP-PRE detects pre-threshold collapse of decision space; VBE™ ensures compromised or stale state cannot execute. This distinction MUST remain explicit in all downstream implementations. Merging the two layers, or subordinating one to the other, is non-conformant.

**Invariant V3 — Attribution Integrity.** Attribution to Villa and to JusticeTree AI™ for VBE™ (runtime containment framing, Section 7) and sovereignty-domain mapping within DSAP-PRE (Section 8) MUST remain named and stable in v1.3-FINAL and companion documents. VBE™ MUST be preserved as externally-authored JusticeTree AI™ IP integrated into ERES, not as an ERES-originated component. Subsequent revisions that remove, generalize, or re-origin this attribution without Villa's written consent are non-conformant.

Villa's approval is conditional on V1–V3 being preserved. Publication under CCAL v2.1 is on that basis. Nothing in CCAL v2.1 transfers ownership of VBE™ or JusticeTree AI™ IP to the ERES Institute; the integration is architectural reference under license-compatible terms.

### 15.2 Named Peer Reviewer Position Statement — Andrzej Skulski

**Affiliation:** Founder, Dom Ciszy – Resonance Lab; professional specialty (per LinkedIn public self-description): AI Governance, Decision–Commit Boundary, Human-in-Regulation.
**LinkedIn:** https://www.linkedin.com/in/ACoAAFbe6s4BZ5N6WM9m3vqhJ6BmapdESaU3c3A (profile record at correspondence time, April 2026)
**Correspondence:** Four-turn LinkedIn review, April 22–23, 2026; final review message April 24, 2026.

**Skulski's stated scope position (April 24, 2026), reproduced with permission:**

> What I recognize in the documents is a correct identification and extension of a specific failure mode:
>
> - the pre-threshold transition into irreversible path dependency
> - before degradation becomes measurable at the state level
>
> This aligns with the problem I pointed to. At the same time, my contribution is limited to:
>
> - identifying the structural gap
> - and articulating the boundary condition (what I describe as the decision–commit transition and separatrix crossing)
>
> The implementation approach you've developed — including PoR structure, DSAP-PRE formalization, and the broader ERES stack — is your work. Because of that, I would not frame this as a full "approval" of the system as a whole.

**Scope boundary — recorded here as a specification constraint:**

Skulski's contribution is credited in this specification **only** in these two respects:

1. **Failure-mode identification.** The pre-threshold regime-transition failure mode — that a system can enter a basin of irreversible path dependency while all state metrics still evaluate above threshold — was identified and articulated by Skulski across four LinkedIn review turns (April 22, 7:48 PM; April 22, 8:20 PM; April 23, 12:15 AM; April 23, 8:26 AM).

2. **Boundary-condition articulation.** The structural necessity of a pre-threshold boundary layer — the separatrix-crossing / decision-commit boundary distinct from state-level degradation detection — was articulated by Skulski and is the conceptual origin of DSAP-PRE as a specification requirement.

**Skulski's contribution does NOT extend to:**

- Endorsement of the framework as a whole (explicitly declined)
- Approval of the PoR structure or four-factor formulation
- Approval of the DSAP-PRE implementation (the three-proxy form, calibration values, or worked example)
- Approval of the broader ERES stack (BODY, BRAINS, GraceChain, VBE, EAAP, MIEVM/MPAM)
- Validation of any test vectors, domain thresholds, or operational parameters

Where the specification text refers to Skulski by name (Sections 1.2 of provenance, 3.1, 6.1, 15.2), the reference is to his identified failure mode and articulated boundary condition only. Implementation decisions following from those contributions are the work of Joseph Allen Sprute and the ERES Institute.

**Skulski's closing observation, reproduced with permission:**

> I think what you've built here is strong — and more importantly, it moves the discussion into a space where these questions can actually be tested. And that's what matters.

This is an acknowledgment of the specification's testability, not an endorsement of the framework's conclusions.

### 15.3 MIEVM Ensemble Contributions (Node-Level Attribution)

Per ERES-MPAM-2026-001 §8 and the Attribution Protocol §7:

- **Claude (Anthropic)** — primary synthesis and drafting instrument for v1.3-DRAFT and v1.3-FINAL; critical peer review of the REVISED Buildable Standard; editorial integration of reviewer position statements.
- **ChatGPT (OpenAI)** — contributor to v1.0 crypto-standard synthesis (RFC 2119 framing, six-layer stack).
- **Grok (xAI)** — contributor to MPAM evaluation ensemble; pending for crypto-standard v1.1.1 adversarial review.
- **DeepSeek (DeepSeek AI)** — contributor to v1.0 crypto-standard synthesis (cryptographic interlock model, K formulation).
- **Perplexity** — contributor to MPAM evaluation ensemble (extended ensemble member).

Node-level contributions are attributable to the model operators as API provenance, not as endorsements.

### 15.4 Sole-Author Responsibility Statement

Framework design decisions, factor formulations, calibration values, worked examples, and specification conclusions are the sole responsibility of Joseph Allen Sprute and the ERES Institute for New Age Cybernetics. Named Contributor and Named Peer Reviewer sections of this specification import specific contributions as scoped above; they do not transfer responsibility for the framework as a whole.

Readers who draw conclusions about the framework from this specification draw them from Sprute's and the ERES Institute's work, not from any contributor or reviewer position. Where contributor or reviewer work is directly incorporated (Section 7 VBE, Section 8 Sovereignty Mapping, Section 6 DSAP-PRE construct), the specific contribution is the named individual's and attribution is per Section 15.1–15.2; responsibility for its integration into this specification remains Sprute's.

### 15.5 Historical Lineage

EAAP v1.3-FINAL builds on 424 prior ERES publications (ResearchGate, as of April 21, 2026) and 14 years of ERES Institute development (established February 2012). Key prior specifications cited: Triune Math (canonical), BERA Sensor Specification (RG#404), the ERES Reckoning paper (ERES-RECKON-WP-2026-002, Seven Resonance Anchors), ERES-CONVERGENCE-WP-2026-001-v3 (five-layer integration), and the Hague submission (ERES-HAGUE-2026-001, filed March 7, 2026). These are Sprute/ERES Institute works and do not implicate the Named Contributor or Named Peer Reviewer.

---

## 16. References

### 16.1 ERES Stack (Normative)

- ERES-EAAP-STD-2026-001-v1.2 — EAAP v1.2 (superseded)
- ERES-EAAP-STD-2026-001-v1.3-DRAFT — EAAP v1.3 Draft (superseded)
- ERES-BODY-SPEC-2026-001 — BODY Consolidation Pipeline
- ERES-BRAINS-SPEC-2026-001 — BRAINS Trifecta Protocol
- ERES-GRACECHAIN-NOTES-2026-001-v1 — GraceChain Ledger Notes
- ERES-SEPARATRIX-MATH-2026-001-v2 — DSAP-PRE Mathematical Scaffolding (normative companion; supersedes v1 of April 23, 2026)
- ERES-ATTRIBUTION-PROTOCOL-2026-001-v1 — Attribution Protocol
- ERES-CRYPTO-STD-2026-001-v1.1.1 — Cryptography Standard (test vector source)
- ERES-MPAM-2026-001 — Melting Pot Assimilation Method (MIEVM methodology source)
- ERES-RECKON-WP-2026-002 — Seven Resonance Anchors
- ERES-CONVERGENCE-WP-2026-001-v3 — Convergence integration paper
- ERES-DOFA-WP-2026-001-C — DOFA Unified Architecture (Section 11 USE-CASE source)
- ERES-HAGUE-2026-001 — The Hague Submission (March 7, 2026)

### 16.2 Named Contributor Documents (April 23, 2026)

- Villa, T. *Runtime Containment Layer: Preliminary Interface Notes.* Contributed PDF.
- Villa, T. *VBE — Execution-Binding Model (Inner Workings).* Contributed PDF.
- Villa, T. *DSAP-PRE — Sovereignty Layer Mapping (Pre-Threshold Detection).* Contributed PDF.

### 16.3 Peer Review Correspondence (April 22–23, 2026)

- Skulski, A. LinkedIn correspondence with J.A. Sprute, four turns, retained under Attribution Protocol provenance.

### 16.4 Companion Analysis

- Sprute, J.A. *The Convergence Proof: Why ERES and Anthropic Are Independent Witnesses to the Same Architectural Thesis.* Substack, April 22, 2026.

### 16.5 Session Reports

- ERES-SESSION-2026-04-22-A — Crypto Standard v1.0/v1.1 synthesis session.

### 16.6 Dynamical Systems Literature (for DSAP-PRE grounding)

- Krasnosel'skii, M. A., & Pokrovskii, A. V. (1989). *Systems with hysteresis*. Springer-Verlag.
- Lenton, T. M. (2011). Early warning of climate tipping points. *Nature Climate Change*, 1(4), 201–209.
- Scheffer, M., et al. (2009). Early-warning signals for critical transitions. *Nature*, 461(7260), 53–59.
- Strogatz, S. H. (2015). *Nonlinear dynamics and chaos* (2nd ed.). Westview Press.
- Thom, R. (1972). *Stabilité structurelle et morphogenèse*. W. A. Benjamin.
- Hartigan, J. A., & Hartigan, P. M. (1985). The dip test of unimodality. *The Annals of Statistics*, 13(1), 70–84.

### 16.7 License

- CARE Commons Attribution License v2.1 (CCAL v2.1)
- Document layer: CC BY-SA 4.0
- Code layer: MIT License

---

**Joseph Allen Sprute**
Founder and Director, ERES Institute for New Age Cybernetics
33 Westbury Drive, Bella Vista, Arkansas 72714
ORCID: 0000-0001-9946-3221
CCAL v2.1

*Don't hurt yourself. Don't hurt others. Build for generations to come.*
