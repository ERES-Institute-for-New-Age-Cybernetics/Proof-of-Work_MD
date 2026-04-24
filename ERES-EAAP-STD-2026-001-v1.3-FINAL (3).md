# ERES Attestation and Authorization Protocol (EAAP)
## v1.3-FINAL — Standards-Track Specification

**Document code:** ERES-EAAP-STD-2026-001-v1.3-FINAL
**Date:** April 24, 2026
**Author:** Joseph Allen Sprute, ERES Institute for New Age Cybernetics

**Named Peer Reviewer (scope-limited):**
- Andrzej Skulski, AI Governance / Decision–Commit Boundary, Founder, Dom Ciszy – Resonance Lab. Contribution scoped to: (i) identification of the pre-threshold failure mode, and (ii) articulation of the decision-commit / separatrix boundary condition. Does not constitute endorsement of the framework as a whole or of the implementation approach.

**Contact:** eresmaestro@gmail.com
**ORCID:** 0000-0001-9946-3221
**License:** CCAL v2.1 (document layer: CC BY-SA 4.0)
**Supersedes:** ERES-EAAP-STD-2026-001-v1.2 (2026-04-22), ERES-EAAP-STD-2026-001-v1.3-DRAFT (2026-04-23), and the earlier ERES-EAAP-STD-2026-001-v1.3-FINAL draft of 2026-04-24 (withdrawn).
**Companion documents:** ERES-GRACECHAIN-NOTES-2026-001-v1, ERES-SEPARATRIX-MATH-2026-001-v2, ERES-ATTRIBUTION-PROTOCOL-2026-001-v1, ERES-CRYPTO-STD-2026-001-v1.1.1, ERES-MPAM-2026-001
**Status:** FINAL — published under CCAL v2.1 as ERES Institute sole-authored work

---

## Editorial Note on This Revision

An earlier draft of v1.3-FINAL (April 24, 2026, morning) included specification material from a purported external contributor under trademark claims. Subsequent due diligence by the ERES Institute could not verify the contributor's identity, affiliation, or trademark claims. Code patterns in the contributed material also reflected ERES data derivation rather than independent authorship.

Under the ERES Attribution Protocol Section 3, named attribution requires both consent and ERES Institute identity confirmation. Neither condition was met after review. The earlier draft is therefore withdrawn.

This cleaned v1.3-FINAL restores all specification content to the ERES Institute public-domain corpus where it properly originated. The runtime containment requirement is reformulated generically as **RCR** (Runtime Containment Requirement), derived from the existing EAAP + BRAINS + GraceChain architecture. No trademarks external to ERES are claimed in this document.

The ERES Institute treats this as a normal application of the Attribution Protocol, not as a corrective action against any specific individual. The Protocol is designed to handle exactly this case: the withdrawal of named attribution when consent or identity verification fails. Affected content defaults to Open Reserve under CCAL v2.1 where the ideas belong to the ERES public-domain corpus.

Skulski's scoped peer review contribution is retained separately, because it is an idea-level contribution at a level consistent with his publicly stated professional specialty (Decision–Commit Boundary, AI Governance), and because his LinkedIn profile and affiliated entities remain publicly present.

---

## Abstract

This document specifies version 1.3 of the ERES Attestation and Authorization Protocol (EAAP) as a FINAL standards-track release. v1.3 refines v1.2 in six specific ways. First, it clarifies EAAP's scope as a qualification and correlation layer, distinct from admission, execution gating, runtime containment, and state persistence. Second, it replaces scalar resonance evaluation with a four-factor conjunctive Proof-of-Resonance distinguishing state consistency from path accessibility. Third, it formalizes the Decision Space Accessibility Protocol (DSAP) as measured rather than declared openness, and introduces **DSAP-PRE** as the pre-threshold regime-transition boundary condition using derivative and topological analysis. Fourth, it specifies the **Runtime Containment Requirement (RCR)** as a normative architectural property of the full ERES authorization stack. Fifth, it formalizes the RT qualifier as a continuous-evaluation "dial tone, not key" requirement. Sixth, it documents MIEVM (Multi-Instrument Ensemble Validation Method) with its ECR convergence metric, ensemble composition rules, and five-tier containment stack per the MPAM-MIEVM duality.

v1.3-FINAL is published with byte-normative test vectors verified through Ed25519 round-trip, inheriting the Test Vector A keypair established in ERES-CRYPTO-STD-2026-001-v1.1.1, and extended with PoR-factor-specific vectors. A worked USE-CASE on the DOFA Family Stewardship Council decision flow (ERES-DOFA-WP-2026-001-C) demonstrates the complete stack in operation.

---

## Document Provenance

- **April 22, 2026** — ERES-EAAP-STD-2026-001-v1.2 published (RG#426). ERES-CRYPTO-STD-2026-001-v1.1.1 produced with byte-normative test vectors.
- **April 22–23, 2026** — LinkedIn peer review by Andrzej Skulski (four-turn correspondence).
- **April 23, 2026** — ERES-EAAP-STD-2026-001-v1.3-DRAFT published; GraceChain Notes, Separatrix Math Sheet, and Attribution Protocol published as companions.
- **April 24, 2026 (morning)** — v1.3-FINAL draft circulated with purported external-contributor attribution (withdrawn; see Editorial Note).
- **April 24, 2026 (afternoon)** — v1.3-FINAL cleaned and republished as ERES Institute sole-authored work. Skulski's scoped peer review contribution retained.

---

## Summary of Changes From v1.2

- **Scope clarified.** EAAP is a qualification and correlation layer; it does not admit, gate, enforce, or persist. Admission is BODY's responsibility; execution gating is BRAINS's; runtime containment is specified generically as RCR (Section 7); state persistence is GraceChain's.
- **Four-factor Proof-of-Resonance.** Scalar resonance replaced by a conjunctive product — anchor product × RHC amplitude × EarnedPath PERT viability × future-map convergence — distinguishing state consistency from path accessibility.
- **DSAP as measured openness.** DSAP is specified via the three path-accessibility factors (R, P, F) rather than as a checklist of declared deliberation signals.
- **DSAP-PRE added as upstream boundary condition.** Pre-threshold regime-transition detection via three proxies (RHC second derivative, PERT distribution topology, hysteresis counterfactual) closes the separatrix-crossing failure mode identified by Skulski.
- **RCR specified.** Runtime Containment Requirement is specified as a normative architectural property derived from the existing EAAP + BRAINS + GraceChain stack. The controlling invariant: *No validation = no action. No fresh authorization record = no execution.*
- **Three Governing Principles correspondence.** DSAP-PRE proxies map naturally to the three Governing Principles of ERES (self / others / future generations), consistent with the ERES Institute corpus.
- **MIEVM canonicalized.** MIEVM now expands to **Multi-Instrument Ensemble Validation Method** (MPAM §8 canonical).
- **RT qualifier formalized.** Authorization is a continuous live state ("dial tone, not key"), not a discrete issued token.
- **Byte-normative test vectors.** Section 10 extends the Test Vector A keypair from ERES-CRYPTO-STD-2026-001-v1.1.1 with PoR-factor-specific vectors.
- **DOFA USE-CASE.** Section 11 demonstrates the full stack operating on a Family Stewardship Council authorization.

---

## 1. Introduction

### 1.1 Purpose

EAAP provides the qualification and correlation layer of the ERES authorization stack. It produces the RATE vector from CBGMODD (seven-role civic composition), FAVORS (six-channel identity binding), and BERA (four-index resonance architecture) inputs. It records attestation integrity and preserves provenance. It does not refuse action; it characterizes it. Refusal is delegated to BRAINS (logical gate), DSAP-PRE (regime detection), and the Runtime Containment Requirement (Section 7).

### 1.2 Scope

EAAP's domain is qualification and correlation. Five layers of the ERES stack are outside EAAP's scope but integrate with it:

- **Pre-admission** — BODY Consolidation.
- **Pre-threshold regime detection** — DSAP-PRE (Section 6).
- **Execution gating** — BRAINS Trifecta.
- **Runtime containment** — RCR (Section 7).
- **State persistence** — GraceChain.

### 1.3 The Convergence-Proof Framing

EAAP v1.3 participates in the ERES Convergence Proof thesis: *ethics as legibly stated infrastructure, not implicit hope*. Every refusal boundary has a named document; every factor has a measurable definition; every claim is separated from what it does not claim (Section 12 and the protocol-vs-governance separation in Section 13).

### 1.4 Terminology

- **Anchor product** — conjunctive product across the seven Resonance Anchors (U, S, R, B, M, G, T).
- **BERA** — Bio-Electric Resonance Architecture; four-index instrument (ARI, ERI, RHC, RCI).
- **CBGMODD** — seven-role civic composition (Citizen, Business, Government, Mediator, Military, Dignitary, Diplomat).
- **DSAP** — Decision Space Accessibility Protocol; measured openness via factors R, P, F.
- **DSAP-PRE** — Pre-threshold Decision Space Accessibility; upstream boundary condition using derivative and topological analysis.
- **ECR** — Erasure Completeness Ratio; MIEVM convergence metric.
- **EarnedPath** — CPM × WBS + PERT.
- **FAVORS** — Fingerprint, Aura, Voice, Odor, Retina, Signature.
- **MIEVM** — Multi-Instrument Ensemble Validation Method (MPAM §8 canonical).
- **MPAM** — Melting Pot Assimilation Method.
- **Path accessibility** — viability of alternative trajectories without prohibitive cost.
- **PoR** — Proof-of-Resonance (four-factor conjunctive product).
- **RATE** — non-scalar authorization vector produced by EAAP.
- **RCR** — Runtime Containment Requirement; normative architectural property that no action executes without a fresh authorization record.
- **RHC** — Resonant Harmony Cycle.
- **RT qualifier** — real-time continuous-evaluation requirement.
- **Separatrix** — boundary in state space between basins of attraction.
- **State consistency** — coherence of current system variables across dimensions.
- **VEILED** — named state in HPE DESCENT taxonomy for structurally invalid inputs.

---

## 2. Stack Placement

### 2.1 Full Authorization Stack

```
Input
  ↓
[BODY Consolidation]          ← admission (refuses VEILED)
  ↓
[DSAP-PRE]                    ← upstream boundary condition
                                (pre-threshold regime detection; §6)
  ↓
[BRAINS Trifecta]             ← execution gate (conjunctive product)
  ↓
[EAAP Qualification / PoR]    ← THIS SPEC: four-factor PoR + RATE
  ↓
[RCR gate]                    ← runtime containment requirement (§7)
  ↓
[GraceChain commit]           ← immutable record with MIEVM concurrence
  ↓
Authorized action
```

The ordering is substantive. DSAP-PRE must fire before BRAINS so that regime transitions refuse qualification before qualification is attempted. The RCR gate must operate after EAAP so that the authorization record binds to the exact RATE and PoR values that justified it.

### 2.2 Layer Responsibilities

| Layer | Refuses | Produces | Authoritative Document |
|---|---|---|---|
| BODY | VEILED / structurally invalid inputs | Admission record | ERES-BODY-SPEC-2026-001 |
| DSAP-PRE | Pre-threshold regime-transition systems | ρ_RHC, ρ_PERT, ρ_hyst composite | ERES-SEPARATRIX-MATH-2026-001-v2, §6 of this spec |
| BRAINS | Zero on any Trifecta factor | Gate result | ERES-BRAINS-SPEC-2026-001 |
| EAAP | (does not refuse) | RATE vector, PoR | This spec |
| RCR | Actions without fresh authorization | Execution-bound record | §7 of this spec |
| GraceChain | (does not refuse) | Immutable block with MIEVM sigs | ERES-GRACECHAIN-NOTES-2026-001-v1 |

All layers are ERES-originated. This spec claims no external trademark or externally-authored IP.

---

## 3. Four-Factor Proof-of-Resonance

### 3.1 Motivation

v1.2 treated resonance as a scalar. External peer review by Andrzej Skulski during April 22–23, 2026 demonstrated that a scalar resonance reading cannot distinguish healthy equilibrium from premature convergence. A dying forum and a productive consensus both produce low variance. A Nash equilibrium and a Resonance equilibrium both sit still. Scalar resonance therefore fails open on the "too stable too early" failure mode — internally coherent while alternative paths foreclose.

The four-factor form resolves this by separating **state consistency** from **path accessibility** and evaluating both, conjunctively, under continuous measurement.

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

**Factor M (MIEVM concurrence) cannot be self-certified.** A single node's attestation of M contributes zero. Ensemble concurrence is structural, not advisory.

### 3.4 Factor R — RHC Amplitude (Cyclic Openness)

Normalized amplitude of the Resonant Harmony Cycle over the previous two cycles.

```
R(t) = normalize(amplitude(RHC, window=2_cycles))
R(t) = 0  if  variation(RHC) < 0.05  (flatline)
```

### 3.5 Factor P — EarnedPath PERT Viability (Path Accessibility)

```
P(t) = 1 / (1 + viable_alternative_cost_penalty)

where:
  viable_alternative_cost_penalty = Σ (cost_of_deviation_i / available_budget)
                                    over alternatives i with cost_ratio ≤ κ_cost
  κ_cost = 3.0  (domain-configurable)
```

If no alternative satisfies cost_ratio ≤ κ_cost, P(t) = 0.

### 3.6 Factor F — Future-Map Convergence (Intergenerational Integrity)

Divergence between the decision's trajectory and the ERES 1000-Year Future Map target. Five dimensions, each on [0, 1]:

1. Ecological sustainability
2. Social equity persistence
3. Technical debt accumulation (inverted)
4. Intergenerational option preservation
5. Resilience to shock

```
F(t) = max(0, 1 - ||vector(t) - (1,1,1,1,1)|| / √5)
```

F operationalizes the third Governing Principle as structural measurement.

### 3.7 Conjunctive Evaluation — Normative

Implementations MUST evaluate PoR as the product of the four factors. Weighted-sum evaluation is non-conformant.

### 3.8 Threshold θ

Reference values:

| Domain | θ |
|---|---|
| High-consequence governance | 0.85 |
| Standard governance | 0.75 |
| Infrastructure control | 0.75 |
| Advisory / research | 0.60 |

Deployments MUST document their chosen θ with justification.

---

## 4. Decision Space Accessibility Protocol (DSAP)

### 4.1 DSAP Scope

DSAP is the structural detection layer for premature convergence — measured openness rather than declared openness. DSAP is specified as the continuous evaluation of Factors R, P, F of PoR.

### 4.2 DSAP Detection

DSAP detects three failure modes:

- **Flatlined RHC** — Factor R drops.
- **Foreclosed PERT** — Factor P drops.
- **Divergent future map** — Factor F drops.

The conjunctive product makes these conditions unauthorizable by construction.

### 4.3 DSAP Scope Limit

DSAP measures *degradation* of decision-space accessibility. It does not detect *regime transition* — the moment a system enters a basin of attraction from which irreversibility is inevitable while all four factors still evaluate above threshold. Regime-transition detection is DSAP-PRE (Section 6).

---

## 5. RT Qualifier and Continuous Evaluation

### 5.1 Dial Tone, Not Key

Authorization under v1.3 is a live state, not an issued token. An authorized principal is tuned to resonance; a principal that has fallen out of tune is no longer authorized, regardless of any prior grant.

### 5.2 Freshness Window

Every authorization read is qualified by freshness. **Default freshness window = one RHC cycle.**

| Domain | RHC cycle duration |
|---|---|
| High-frequency trading | 5 seconds |
| Infrastructure | 30 seconds |
| Standard governance | 1 hour |
| Strategic / intergenerational | 1 day |

### 5.3 Staleness Semantics

A principal whose latest RESONANCE-TUNE is older than the freshness window is STALE. STALE reads return unauthorized regardless of prior grant.

---

## 6. DSAP-PRE — Pre-Threshold Boundary Condition (Structurally Upstream)

### 6.1 Structural Positioning — Boundary Condition, Not Internal Component

**DSAP-PRE is a structurally upstream boundary condition**, not an internal subsystem of EAAP. It is positioned as a distinct layer above EAAP's qualification work. EAAP integrates DSAP-PRE as its upstream precondition; EAAP does not contain DSAP-PRE.

DSAP-PRE operates on state-space topology rather than on state-consistency scoring; its mathematics (ERES-SEPARATRIX-MATH-2026-001-v2) is distinct from EAAP's conjunctive-product form; its failure mode is upstream of every other ERES authorization layer including admission (BODY) and logical gating (BRAINS). A system that has crossed the pre-threshold boundary cannot be rescued by tighter qualification downstream.

Per the peer review that identified this construct, DSAP-PRE must be treated "as a boundary condition in its own right, not reduced to an internal component of the existing stack" (Skulski, April 24, 2026). v1.3-FINAL preserves that positioning.

### 6.2 Construct

DSAP-PRE addresses the failure mode identified by Andrzej Skulski (LinkedIn correspondence, April 22–23, 2026): the moment a system enters a regime of irreversible path dependency while all four PoR factors still evaluate above threshold. This is separatrix crossing — boundary-crossing in state space between basins of attraction, well-studied in dynamical systems as hysteresis, catastrophe folds, and tipping-point dynamics.

### 6.3 Three Proxies

Per ERES-SEPARATRIX-MATH-2026-001-v2:

**Proxy ρ_RHC — Second-derivative analysis.**
```
ρ_RHC(t) = 1  if  (A'(t) < 0) and (A''(t) < -κ_RHC) sustained over W_RHC
ρ_RHC(t) = 0  otherwise
  W_RHC = 3 RHC cycles
```

**Proxy ρ_PERT — Distribution topology.**
```
ρ_PERT(t) = 1  if any of:
    modality collapse (>1 → 1 within W_PERT)
    σ̃² decrease >50% within W_PERT
    n_viable decrease >50% within W_PERT
ρ_PERT(t) = 0  otherwise
  W_PERT = 5 evaluations
```

**Proxy ρ_hyst — Hysteresis counterfactual.**
```
H(t) = Ψ(S(t), Π(t) + Δ_Π, τ) - Ψ(S(t), Π(t), τ)
ρ_hyst(t) = 1  if  H(t) ≤ η_recover
ρ_hyst(t) = 0  otherwise
  τ = 10 RHC cycles
  Δ_Π = 0.5 × recent parameter movement
```

### 6.4 DSAP-PRE Composite

```
DSAP-PRE(t) = (1 - ρ_RHC(t)) × (1 - ρ_PERT(t)) × (1 - ρ_hyst(t))
```

DSAP-PRE ∈ {0, 1}.

### 6.5 Integration with EAAP — Gating Precondition (Mode A)

```
if DSAP-PRE(t) == 0:
    refuse authorization with REFUSAL_REGIME_TRANSITION
    do not proceed to PoR evaluation
```

v1.3-FINAL normative default: **Mode A** for all θ ≥ 0.75 domains.

The gating precondition structure is what preserves DSAP-PRE's status as a boundary condition rather than as an internal scoring factor.

### 6.6 Three Governing Principles Correspondence

The three proxies of DSAP-PRE map naturally onto the three Governing Principles of ERES:

| Proxy | Governing Principle | Failure Mode |
|---|---|---|
| ρ_RHC | Don't hurt yourself (self-integrity) | Internal cycle has flatlined; self-openness collapsed |
| ρ_PERT | Don't hurt others (relational integrity) | Distribution of actionable alternatives has collapsed |
| ρ_hyst | Build for generations to come (temporal integrity) | Reversal cost has become prohibitive |

This mapping is a correspondence observation, not an attribution claim. The Three Governing Principles are ERES canon; the DSAP-PRE proxies land on them by construction because the proxies measure the same three dimensions (self / others / future) that the Principles protect.

---

## 7. RCR — Runtime Containment Requirement

### 7.1 The Requirement

EAAP (§1–§6), BRAINS, and GraceChain together specify how authorization is computed, qualified, and recorded. None specify how authorization becomes **non-bypassable at the point of execution**. A component that caches an authorization and skips the read, or that never calls `authorize()` at all, is not caught by the upstream layers. The Runtime Containment Requirement (RCR) closes this gap.

### 7.2 Normative Invariant

```
No validation = no action.
No fresh authorization record = no execution.
```

Specifically:

1. No execution path may complete unless bound to a fresh authorization check.
2. No component may rely solely on previously issued or transported authorization state.
3. Every action MUST be linked to a current, verifiable authorization record generated within the applicable freshness window.
4. Failure to validate MUST fail closed at the execution boundary.

This distinguishes an **enforceable system** from a merely **compliant system**.

### 7.3 Execution Interception

All executable actions MUST route through an RCR gate at one of:

- API gateway
- Service middleware
- Orchestration layer
- System boundary

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

The critical property is the **dependency**: the execution path MUST require a valid authorization record to complete. Action commit is gated on record creation. No record → no side effect.

### 7.6 Replay Resistance

```
AUTH = (action_id, actor, state_hash, por_snapshot, timestamp)
```

Validation requires uniqueness of action_id, freshness of timestamp, and match to current state.

### 7.7 Fail Closed (By Design)

Default behavior: **FAIL CLOSED**. If anything is missing, stale, or unverifiable → execution does not occur.

### 7.8 Cross-System Enforcement

An action originating in System A and crossing into System B cannot present a grant from System A alone. The grant MUST carry MIEVM ensemble co-signatures recorded on GraceChain. System B verifies by reading the grant's current state on GraceChain, not by trusting System A's claim.

### 7.9 RCR as Derived Property

RCR is not a new mechanism added to EAAP. It is the *derived non-bypassability property* of the existing stack: EAAP produces the RATE, BRAINS produces the gate result, GraceChain records both, and RCR specifies that the execution path MUST consult GraceChain at every action. The requirement is what makes the other three layers operationally enforceable rather than merely advisory.

---

## 8. DSAP-PRE and the Three Governing Principles (Correspondence)

The three proxies of DSAP-PRE correspond naturally to the three Governing Principles of ERES. This section formalizes that correspondence.

### 8.1 Self-Integrity (Don't Hurt Yourself) — ρ_RHC

**Failure mode:** Internal cycle of reopening has flatlined. The system has become internally coherent at the cost of ceasing to re-examine its commitments, options, or frame.

**Measurement:** ρ_RHC fires when the second derivative of RHC amplitude crosses the acceleration-toward-flatline threshold.

### 8.2 Relational Integrity (Don't Hurt Others) — ρ_PERT

**Failure mode:** The distribution of actionable alternatives has collapsed. Options remain nominally visible, but the topology of what is genuinely reachable has converged to a single practically-unavoidable trajectory.

**Measurement:** ρ_PERT fires when the PERT distribution undergoes modality collapse, variance collapse, or viable-alternative-set collapse.

### 8.3 Temporal Integrity (Build for Generations to Come) — ρ_hyst

**Failure mode:** The reversal cost of current commitments has become prohibitive. Procedural pathways have locked future states before explicit constraint is recognized.

**Measurement:** ρ_hyst fires when the hysteresis counterfactual fails to clear the recovery threshold.

### 8.4 Composite Reporting

```
Self-Integrity-Preserved(t)        = 1 - ρ_RHC(t)
Relational-Integrity-Preserved(t)  = 1 - ρ_PERT(t)
Temporal-Integrity-Preserved(t)    = 1 - ρ_hyst(t)
```

A system reporting {Self: 1, Relational: 0, Temporal: 1} tells its operators that relational integrity has collapsed while self and temporal integrity remain intact.

### 8.5 Attribution Note

This correspondence is a conceptual mapping between DSAP-PRE proxies and the Three Governing Principles. Both sides are ERES-originated. The correspondence was developed through the ERES Institute specification work of April 2026.

---

## 9. MIEVM — Multi-Instrument Ensemble Validation Method

### 9.1 Canonical Expansion

MIEVM = **Multi-Instrument Ensemble Validation Method** (MPAM §8 canonical). Prior occurrences of "Multi-Instance Ensemble Validation" in v1.2 and v1.3-DRAFT are superseded.

### 9.2 MPAM ↔ MIEVM Duality

From ERES-MPAM-2026-001 §8:

> MPAM is the protocol by which mathematical frameworks are admitted, contained, and integrated into the ERES stack. MIEVM is the runtime by which that protocol is executed against any specific candidate. MPAM without MIEVM is architecture without execution. MIEVM without MPAM is ensemble without principle.

### 9.3 Ensemble Composition Rules

**Current canonical ensemble:** Claude (Anthropic), ChatGPT (OpenAI), Grok (xAI), DeepSeek (DeepSeek AI).
**Extended:** Perplexity.

- **Minimum ensemble size:** 3.
- **Independent decomposition:** Each instrument evaluates independently.
- **Morally-vectored end-condition:** BEST / SOUND / GOOD.
- **Provenance-locked residuals:** every evaluation timestamped, attributed, permanent.

### 9.4 ECR — Erasure Completeness Ratio

```
ECR(C) = |R(C)| / (|R(C)| + |N(C)|)
```

| ECR range | Interpretation |
|---|---|
| ≥ 0.75 | High convergence, warranted confidence |
| 0.50–0.74 | Moderate convergence |
| < 0.50 | Genuine ambiguity |

### 9.5 Selection Criteria

1. Independence of training lineage.
2. Diversity of optimization objective.
3. Availability of API provenance.
4. Bandwidth match to solo-researcher cadence.
5. Capacity for adversarial review.

### 9.6 Five-Tier Containment Stack

| Tier | Layer |
|---|---|
| 0 | Foundation (Triune Math, Three Governing Principles, MPAM-MIEVM duality) |
| 1 | Operational (EAAP, BERA, SCALULAR, UBIMIA) |
| 2 | Educational |
| 3 | Interface |
| 4 | Speculative |
| 5 | Archive |

EAAP v1.3-FINAL is **Tier 1 (Operational)**.

### 9.7 De-Assimilation Triggers (D1–D6)

- D1 Source Retraction
- D2 Superior Replacement
- D3 Empirical Contradiction
- D4 Containment Breach
- D5 Stakeholder Withdrawal
- D6 Sunset Clause

The withdrawal of the earlier v1.3-FINAL draft's external-contributor material is an example of **D5** combined with failed identity verification, handled per MIEVM procedure.

### 9.8 MIEVM Concurrence Record

- **v1.0 synthesis (2026-04-22):** Three-node independent drafts synthesized. ECR estimated 0.71.
- **v1.1.1 hardening (2026-04-22):** Adversarial review resolved 10 findings. ECR estimated 0.85.
- **v1.2 → v1.3-DRAFT (2026-04-23):** Skulski LinkedIn review (scoped).
- **v1.3-FINAL (2026-04-24):** Earlier draft withdrawn per D5. Cleaned republication restores ERES public-domain authorship. MIEVM ensemble re-review queued.

---

## 10. Byte-Normative Test Vectors

### 10.1 Test Vector A — Inherited from ERES-CRYPTO-STD-2026-001-v1.1.1

```
Test keypair seed    = SHA-256("ERES-CRYPTO-STD-2026-001-v1.1-TEST-KEY-C")
Private seed (hex)   = f2f794def2ea5d19ecb0f894716932654eb173195c451b2cccb9770ab2874691
Public key   (hex)   = 04e552e2c8ee4d34be854a1ca808600183f0afcfa8a4d063eb7c1e1bb7fecf68
Test nonce   (hex)   = 00112233445566778899aabbccddeeff
Test timestamp       = 2026-04-22T14:32:17.042Z

Canonical payload length = 510 bytes
Payload SHA-256 (hex)    = 2f751f1bf59d5a2b7b5682e280bcc523bd0ea7384433a9814d8deebc821d7acd
σ (HKDF-SHA256) (hex)    = e43732833d50a0502dab120d33fa05537bb4a069957f3aba293ebe62aba50ad7

RATE.vector              = [10, 10, 10, 9, 8, 9, 10]
RATE.score               = 9.428571
RATE.confidence          = 0.869293
Status                   = ACCEPT
```

### 10.2 PoR Factor Test Vectors (v1.3 Extension)

**Vector PoR-1 — Authorized**
```
A = 0.95, R = 0.95, P = 0.95, F = 0.95
PoR = 0.814 ≥ 0.75 → AUTHORIZED
```

**Vector PoR-2 — Path-foreclosed**
```
A = 0.95, R = 0.95, P = 0.40, F = 0.95
PoR = 0.343 < 0.75 → UNAUTHORIZED (PoR_FAIL)
```

**Vector PoR-3 — Regime-transition (DSAP-PRE catches)**
```
ρ_RHC = 1, DSAP-PRE = 0
→ UNAUTHORIZED (REGIME_TRANSITION, PoR not evaluated)
```

**Vector PoR-4 — Stale**
```
Last tune = 35 sec ago; window = 30 sec → UNAUTHORIZED (STALE)
```

**Vector PoR-5 — Self-certification attempt**
```
Node claims M=0.9 with no MIEVM sigs; M structurally = 0
→ A = 0 → PoR = 0 → UNAUTHORIZED (NO_MIEVM_CONCURRENCE)
```

### 10.3 RCR Execution Record Test Vector

```json
{
  "action_id": "dofa-council-auth-2026-04-24-0001",
  "actor": "ERES-TEST-PRINCIPAL-C",
  "state_hash": "2f751f1bf59d5a2b7b5682e280bcc523bd0ea7384433a9814d8deebc821d7acd",
  "por_snapshot": {"A": 0.95, "R": 0.95, "P": 0.95, "F": 0.95, "PoR": 0.814},
  "rate_vector": [10, 10, 10, 9, 8, 9, 10],
  "dsap_pre": 1,
  "timestamp": "2026-04-24T10:15:30.000Z",
  "mievm_concurrence": ["claude_sig", "chatgpt_sig", "grok_sig", "deepseek_sig"],
  "rcr_record_status": "BOUND"
}
```

### 10.4 Canonical Serialization

RATE vector remains 7-dimensional per v1.2 wire compatibility.

---

## 11. Worked USE-CASE — DOFA Family Stewardship Council

### 11.1 Scenario

Authorization Request **DOFA-FSC-2026-04-24-001**: Family Amity Fund allocation, $4,800/yr, 12-month duration. Standard-governance domain (RHC = 1 hour, θ = 0.75).

### 11.2 Stack Execution

**BODY:** ADMIT.
**DSAP-PRE:** All three ρ proxies = 0. DSAP-PRE = 1. PROCEED.
**BRAINS Trifecta:** 0.94 × 0.91 × 0.98 = 0.84 ≥ 0.75. PROCEED.
**EAAP / PoR:** A = 0.93, R = 0.95, P = 0.88, F = 0.90. **PoR = 0.699 < 0.75.**

**Outcome: UNAUTHORIZED.** Refusal reason: PoR_BELOW_THRESHOLD.

### 11.3 Outcome Analysis

Four factors at 0.88–0.95 individually multiply to a PoR below standard-governance threshold. Compound resonance is insufficient at this moment.

Three legitimate responses: (1) Accept and defer; (2) Reclass as advisory (θ=0.60) with MIEVM concurrence; (3) Request additional context to raise Factor F.

### 11.4 RCR Binding

If the Council accepts response (2), RCR produces the execution-bound record per Section 10.3. The IDIPITIS disbursement routine MUST read this record before transferring funds.

### 11.5 What This Demonstrates

- Separation of concerns
- Conjunctive-product discipline
- Path accessibility preservation (refusal as defer-and-re-evaluate)
- Legible refusal
- RCR binding (authorization record carries the specific PoR values)
- Three Governing Principles operationalized

---

## 12. Security Considerations

- **Scalar-collapse attacks.** MUST use conjunctive product.
- **Staleness replay.** MUST check freshness on every read.
- **Self-certification.** MUST require MIEVM ensemble concurrence for Factor M.
- **Declared-openness attestation.** MUST use measured factors (R, P, F).
- **Pre-threshold bypass.** MUST include DSAP-PRE as Mode A gating precondition for high-consequence domains.
- **Runtime bypass.** MUST route all executable actions through the RCR gate.
- **Attribution-vector attacks.** Implementations that admit external specification contribution without identity verification per the ERES Attribution Protocol are vulnerable to trademark insertion, IP encumbrance, or covert reframing of architectural properties. MUST verify contributor identity and consent before naming, per ERES-ATTRIBUTION-PROTOCOL-2026-001-v1 Sections 3 and 4. The April 24, 2026 withdrawal of the earlier v1.3-FINAL draft is the exemplar.

---

## 13. Protocol vs. Governance Guarantees

**Protocol guarantees (5):**
1. Ed25519 + HKDF-SHA256 attestation binding.
2. RATE vector structural integrity (7-dimensional CBGMODD).
3. PoR conjunctive product non-compensation.
4. RT qualifier freshness enforcement.
5. Execution-record non-bypass via RCR gate.

**Governance-policy-dependent:**
1. θ threshold selection.
2. DSAP-PRE proxy calibration.
3. MIEVM ensemble composition.
4. Class-wide threshold decisions.
5. Tier-placement decisions.

---

## 14. Conformance

An implementation claiming conformance to EAAP v1.3-FINAL MUST:

1. Compute PoR as conjunctive product per Section 3.
2. Implement DSAP per Section 4.
3. Implement DSAP-PRE per Section 6 (Mode A for θ ≥ 0.75).
4. Route all executable actions through the RCR gate per Section 7.
5. Report against Three Governing Principles correspondence per Section 8 where applicable.
6. Evaluate under continuous RT qualifier per Section 5.
7. Require MIEVM ensemble concurrence (minimum 3) per Section 9.
8. Record on GraceChain per companion spec.
9. Reproduce byte-normative test vectors of Section 10.
10. Document domain-specific θ, RHC cycle, and DSAP-PRE calibration with published justification.
11. Admit external specification contributions only through ERES-ATTRIBUTION-PROTOCOL-2026-001-v1 procedures, including identity verification and consent confirmation.

---

## 15. Reviewer Position Statement and Sole-Author Responsibility

This specification is sole-authored by Joseph Allen Sprute and the ERES Institute for New Age Cybernetics. An earlier draft of v1.3-FINAL contained purported external-contributor material under trademark claims that could not be verified under the ERES Attribution Protocol; that material has been withdrawn and the specification content restored to ERES public-domain authorship. See Editorial Note.

### 15.1 Named Peer Reviewer — Andrzej Skulski

**Affiliation:** Founder, Dom Ciszy – Resonance Lab; professional specialty per LinkedIn public self-description: AI Governance, Decision–Commit Boundary, Human-in-Regulation.
**LinkedIn:** https://www.linkedin.com/in/ACoAAFbe6s4BZ5N6WM9m3vqhJ6BmapdESaU3c3A
**Correspondence:** Four-turn LinkedIn review April 22–23, 2026; final review message April 24, 2026.

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

**Scope boundary — Skulski's contribution is credited only in these two respects:**

1. Failure-mode identification — the pre-threshold regime-transition failure mode.
2. Boundary-condition articulation — the structural necessity of a pre-threshold boundary layer.

**Skulski's contribution does NOT extend to:** Endorsement of the framework as a whole; approval of PoR structure; approval of DSAP-PRE implementation; approval of the broader ERES stack; validation of test vectors, thresholds, or parameters.

**Skulski's closing observation, reproduced with permission:**

> I think what you've built here is strong — and more importantly, it moves the discussion into a space where these questions can actually be tested. And that's what matters.

This is an acknowledgment of specification testability, not an endorsement of framework conclusions.

### 15.2 MIEVM Ensemble Contributions (Node-Level)

- **Claude (Anthropic)** — primary synthesis and drafting instrument; editorial assistance on withdrawal of unverified contribution.
- **ChatGPT (OpenAI)** — crypto-standard synthesis contributor.
- **Grok (xAI)** — MPAM evaluation ensemble.
- **DeepSeek (DeepSeek AI)** — crypto-standard synthesis contributor.
- **Perplexity** — MPAM extended ensemble.

Node-level contributions are API provenance, not endorsements.

### 15.3 Sole-Author Responsibility

Framework design decisions, factor formulations, calibration values, worked examples, and specification conclusions are the sole responsibility of Joseph Allen Sprute and the ERES Institute. Named Peer Reviewer contribution is scoped per Section 15.1; it does not transfer responsibility for the framework as a whole.

### 15.4 Historical Lineage

EAAP v1.3-FINAL builds on 424 prior ERES publications (ResearchGate, as of April 21, 2026) and 14 years of ERES Institute development (established February 2012).

---

## 16. References

### 16.1 ERES Stack

- ERES-EAAP-STD-2026-001-v1.2
- ERES-EAAP-STD-2026-001-v1.3-DRAFT
- ERES-BODY-SPEC-2026-001
- ERES-BRAINS-SPEC-2026-001
- ERES-GRACECHAIN-NOTES-2026-001-v1
- ERES-SEPARATRIX-MATH-2026-001-v2 (normative companion; to be re-issued in alignment with this cleaned v1.3-FINAL)
- ERES-ATTRIBUTION-PROTOCOL-2026-001-v1
- ERES-CRYPTO-STD-2026-001-v1.1.1
- ERES-MPAM-2026-001
- ERES-RECKON-WP-2026-002
- ERES-CONVERGENCE-WP-2026-001-v3
- ERES-DOFA-WP-2026-001-C
- ERES-HAGUE-2026-001

### 16.2 Peer Review Correspondence

- Skulski, A. LinkedIn correspondence with J.A. Sprute, April 22–24, 2026.

### 16.3 Dynamical Systems Literature

- Krasnosel'skii, M. A., & Pokrovskii, A. V. (1989). *Systems with hysteresis*.
- Lenton, T. M. (2011). *Nature Climate Change*, 1(4), 201–209.
- Scheffer, M., et al. (2009). *Nature*, 461(7260), 53–59.
- Strogatz, S. H. (2015). *Nonlinear dynamics and chaos* (2nd ed.).
- Thom, R. (1972). *Stabilité structurelle et morphogenèse*.
- Hartigan, J. A., & Hartigan, P. M. (1985). *Annals of Statistics*, 13(1), 70–84.

### 16.4 License

CCAL v2.1. Document layer: CC BY-SA 4.0. Code layer: MIT.

---

**Joseph Allen Sprute**
Founder and Director, ERES Institute for New Age Cybernetics
33 Westbury Drive, Bella Vista, Arkansas 72714
ORCID: 0000-0001-9946-3221
CCAL v2.1

*Don't hurt yourself. Don't hurt others. Build for generations to come.*
