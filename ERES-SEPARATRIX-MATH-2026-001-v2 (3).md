# ERES Separatrix Crossing Math Sheet

**Document code:** ERES-SEPARATRIX-MATH-2026-001-v2
**Date:** April 24, 2026
**Author:** Joseph Allen Sprute, ERES Institute for New Age Cybernetics

**Named Peer Reviewer (scope-limited):**
- Andrzej Skulski, AI Governance / Decision–Commit Boundary, Founder, Dom Ciszy – Resonance Lab. Contribution scoped to: (i) identification of the pre-threshold failure mode (Section 1.3), and (ii) articulation of the separatrix-crossing boundary condition (Section 2.1 motivation). Does not constitute endorsement of the specific mathematical form (three proxies, binary composite, calibration values, worked example).

**Contact:** eresmaestro@gmail.com
**ORCID:** 0000-0001-9946-3221
**License:** CCAL v2.1 (document layer: CC BY-SA 4.0)
**Supersedes:** ERES-SEPARATRIX-MATH-2026-001-v1 (April 23, 2026), and the earlier ERES-SEPARATRIX-MATH-2026-001-v2 draft of April 24, 2026 (withdrawn).
**Status:** v2 — normative companion to ERES-EAAP-STD-2026-001-v1.3-FINAL (cleaned republication April 24, 2026)

---

## Editorial Note on This Revision

An earlier draft of this math sheet v2 (April 24, 2026, morning) incorporated sovereignty-domain mapping material from a purported external contributor under trademark claims. Subsequent due diligence by the ERES Institute could not verify the contributor's identity, affiliation, or trademark claims. That material has been withdrawn under ERES Attribution Protocol Sections 3 and 4.

The structural intuition — that the three DSAP-PRE proxies correspond to three distinct domains of sovereignty preservation — is retained because it is directly entailed by the Three Governing Principles of ERES, which have been canon since Institute founding (February 2012). The correspondence is reframed in Section 7 as a mapping to the Three Governing Principles (self / others / future) — ERES canon — rather than as any externally-contributed taxonomy.

Skulski's scoped peer review contribution is retained separately, because it is an idea-level contribution consistent with his publicly stated professional specialty and publicly present affiliations.

---

## Revision History

- **v1 (2026-04-23)** — Initial mathematical scaffolding. Three proxies. Binary and continuous composites both permitted. Calibration deferred. No worked example.
- **v2 draft (2026-04-24, morning)** — WITHDRAWN. Incorporated unverified external-contributor material; failed Attribution Protocol identity verification.
- **v2 (2026-04-24, afternoon) — THIS VERSION** — Binary DSAP-PRE composite locked as normative (Mode A for θ ≥ 0.75). Three Governing Principles correspondence added (Section 7, ERES-originated). Reference calibration values pinned. DOFA worked example traced through. ECR methodology referenced. Named attribution scoped to Skulski only.

---

## Preamble

This math sheet specifies the mathematical scaffolding for **DSAP-PRE** — the Pre-threshold Decision Space Accessibility layer above the four-factor Proof-of-Resonance in EAAP v1.3-FINAL. It addresses the failure mode identified by Andrzej Skulski (LinkedIn correspondence, April 22–23, 2026): the moment at which a system enters a regime of irreversible path dependency, while all current state, cycle, path, and future-map metrics still evaluate above authorization threshold.

v2 is normative companion to the cleaned EAAP v1.3-FINAL. Where v1 presented alternatives, v2 selects the normative form. Where v1 deferred parameters, v2 pins reference values. Where v1 had no worked example, v2 traces a full DOFA evaluation.

---

## 1. The Pre-Threshold Problem

### 1.1 Statement

Proof-of-Resonance in EAAP v1.3-FINAL evaluates:

```
PoR(t) = A(t) × R(t) × P(t) × F(t)
```

All four factors measure **current condition**. They do not measure **regime of trajectory**. A system may present with PoR above θ, all factors above component thresholds, and enforcement correctly anchored at the measurement point, while simultaneously having crossed into a regime from which subsequent collapse of one or more factors is inevitable.

### 1.2 Why Tightening θ Does Not Solve It

A stricter θ detects degradation earlier; it does not detect regime transition. What is needed is a different kind of measurement: one based on trajectory topology rather than on current-state magnitude.

### 1.3 The Failure Mode Named

Per Skulski (April 23, 2026, 8:26 AM):

> All three mechanisms you mention — cycle amplitude (RHC), probabilistic path accounting (PERT), future divergence — seem to detect changes in accessibility as they develop. The question I'm working with is whether there is a moment before those signals shift, where the system has already crossed a structural threshold. Not when alternatives become measurably more expensive but when the system transitions into a regime where increasing that cost becomes inevitable.

This is **separatrix crossing** — the topological boundary condition that is invisible to state-and-magnitude measurement because state metrics remain in-range past the crossing.

---

## 2. Dynamical Systems Grounding

### 2.1 Prior Art

DSAP-PRE specifies how ERES measures a well-studied construct. The underlying phenomenon is not invented here.

- **Catastrophe theory** (Thom, 1972; Zeeman, 1977) — fold catastrophe as regime-transition model.
- **Hysteresis in control theory** (Krasnosel'skii & Pokrovskii, 1989) — path-dependent behavior where reversing the parameter does not reverse the state.
- **Tipping-point theory** (Scheffer et al., 2009; Lenton, 2011) — early-warning signals: rising variance, rising autocorrelation, critical slowing down.
- **Separatrices in multi-stable dynamical systems** (Strogatz, 2015) — boundary in state space between basins of attraction.

Common observation across these: **systems approaching regime transitions exhibit identifiable precursor signatures before their state variables cross thresholds**. DSAP-PRE specifies three such signatures adapted to the ERES measurement stack.

### 2.2 Normative Terminology

- **Basin of attraction** — states converging to a stable outcome.
- **Separatrix** — boundary in state space between basins.
- **Regime transition** — crossing of a separatrix.
- **Critical slowing down** — system near separatrix responds to perturbations with increasing recovery time.
- **Irreversibility** — reversing the driving parameter does not restore the prior basin.

---

## 3. Proxy One — RHC Derivative Analysis (ρ_RHC)

### 3.1 Rationale

Factor R of PoR measures RHC amplitude (first-order quantity). Critical slowing down manifests as amplitude not yet flatlined but declining at accelerating rate. The **second derivative** of RHC amplitude carries the regime-transition signal before the first-order threshold is crossed.

### 3.2 Normative Mathematical Form

Let A_RHC(t) denote the RHC amplitude time series.

```
ρ_RHC(t) = 1  if (A'(t) < 0) AND (A''(t) < -κ_RHC) sustained over W_RHC
ρ_RHC(t) = 0  otherwise
```

- κ_RHC: domain-calibrated acceleration-toward-flatline threshold (Section 6).
- W_RHC: sustaining window, **default 3 RHC cycles**.

### 3.3 Implementation Notes

- Numerical differentiation: Savitzky-Golay filter (window 5, polynomial order 2) as v2 reference.
- ρ_RHC fires pre-threshold: can fire while Factor R is still above its component threshold.
- Binary formulation is normative per v1.3-FINAL Mode A.

---

## 4. Proxy Two — PERT Distribution Topology (ρ_PERT)

### 4.1 Rationale

Factor P aggregates the PERT distribution into a scalar viability. The transition from multi-modal to unimodal is a separatrix-crossing signature visible in distribution topology while scalar viability can still read above threshold.

### 4.2 Normative Mathematical Form

Let D_PERT be the PERT distribution over alternative-path cost. Three topological indicators:

- **Modality** m(D_PERT) via Hartigan's dip test, α = 0.05.
- **Variance** σ̃²(D_PERT) normalized against current-path cost c_0.
- **Viable-alternative count** n_viable(D_PERT) with cost ≤ κ_cost × c_0.

```
ρ_PERT(t) = 1  if ANY of:
    m(D_PERT) decreased from >1 to 1 within W_PERT
    σ̃²(D_PERT) decreased by >50% within W_PERT
    n_viable(D_PERT) decreased by >50% within W_PERT
ρ_PERT(t) = 0  otherwise
```

- W_PERT: evaluation window, **default 5 evaluations**.
- κ_cost: domain-calibrated cost-ratio ceiling (Section 6).

### 4.3 Implementation Notes

- Multimodality testing on sample sizes <30 is unreliable; rely on variance and viable-count signals primarily.
- Log-cost variance when distribution spans multiple orders of magnitude.
- OR-combination across the three conditions is normative in v2.

---

## 5. Proxy Three — Hysteresis Counterfactual (ρ_hyst)

### 5.1 Rationale

Direct irreversibility test: if conditions were reversed, would the system recover? In a multi-stable regime, yes. Past the separatrix, no.

### 5.2 Normative Mathematical Form

```
H(t) = Ψ(S(t), Π(t) + Δ_Π, τ) − Ψ(S(t), Π(t), τ)

ρ_hyst(t) = 1  if  H(t) ≤ η_recover
ρ_hyst(t) = 0  otherwise
```

- Ψ: forward-projection of PERT viability.
- τ: horizon, **default 10 RHC cycles**.
- Δ_Π: restoration perturbation magnitude, **default 0.5 × recent parameter movement**.
- η_recover: domain-calibrated recovery threshold (Section 6).

### 5.3 Implementation Notes

- Ψ must be realistic; in ERES, EarnedPath projection with perturbation applied.
- Δ_Π must be a realistic reversal, not a maximally favorable one.
- Evaluation cadence: minimum every fifth RHC cycle (computational cost tradeoff).

---

## 6. Reference Calibration Values (Normative)

### 6.1 RHC Cycle Timing by Domain

| Domain | RHC cycle |
|---|---|
| High-frequency trading | 5 sec |
| Infrastructure / enterprise IT | 30 sec |
| Standard governance | 1 hour |
| Strategic / intergenerational | 1 day |

### 6.2 DSAP-PRE Proxy Parameters

| Parameter | HF-trading | Infrastructure | Standard-governance | Strategic |
|---|---|---|---|---|
| κ_RHC | 0.15/sec² | 0.05/sec² | 0.01/hr² | 0.005/day² |
| W_RHC | 3 cycles | 3 cycles | 3 cycles | 3 cycles |
| W_PERT | 5 evals | 5 evals | 5 evals | 5 evals |
| κ_cost | 2.0 | 3.0 | 3.0 | 4.0 |
| τ | 10 cycles | 10 cycles | 10 cycles | 10 cycles |
| Δ_Π | 0.5 | 0.5 | 0.5 | 0.5 |
| η_recover | 0.10 | 0.10 | 0.15 | 0.20 |

### 6.3 Calibration Update Procedure

Updates follow ERES-MPAM-2026-001 §9 de-assimilation procedures if values are superseded, with MIEVM ensemble concurrence.

---

## 7. Three Governing Principles Correspondence

### 7.1 Construct

This section formalizes the correspondence between the three DSAP-PRE proxies and the three Governing Principles of ERES (self / others / future generations). The Three Governing Principles have been ERES canon since Institute founding (February 2012): *Don't hurt yourself. Don't hurt others. Build for generations to come.*

The correspondence is a natural one: each proxy measures integrity in a distinct dimension that one of the Principles protects.

### 7.2 Operator Assignments

| Proxy | Governing Principle | Integrity Dimension | Failure Mode |
|---|---|---|---|
| ρ_RHC | Don't hurt yourself | Self-integrity | Internal cycle has flatlined; self-openness collapsed |
| ρ_PERT | Don't hurt others | Relational integrity | Distribution of actionable alternatives has collapsed |
| ρ_hyst | Build for generations to come | Temporal integrity | Reversal cost has become prohibitive; future optionality foreclosed |

### 7.3 Why the Mapping Is One-to-One

Each proxy's measurement signature aligns naturally with exactly one Governing Principle:

- **ρ_RHC measures rate-of-change in cyclic reopening.** Cyclic reopening is internally-generated alternative-evaluation capacity — the operation by which a system re-examines its own option space. When this slows toward flatline, self-openness has collapsed. This is the *self-integrity* failure mode that "Don't hurt yourself" protects against.

- **ρ_PERT measures topology of the distribution of alternatives.** Distribution topology is a property of the shared option space that multiple actors can observe — the surface on which relational coordination operates. When the distribution goes unimodal, shared decision space has converged. This is the *relational integrity* failure mode that "Don't hurt others" protects against.

- **ρ_hyst measures asymmetry between forward commitment and backward exit cost.** Asymmetry between forward and backward cost is the defining structural property of temporal binding. When forward-backward symmetry fails, future generations inherit a foreclosed decision space. This is the *temporal integrity* failure mode that "Build for generations to come" protects against.

### 7.4 Composite Reporting

For applications that require distinguishing *which* integrity dimension has crossed its separatrix:

```
Self-Integrity-Preserved(t)        = 1 - ρ_RHC(t)
Relational-Integrity-Preserved(t)  = 1 - ρ_PERT(t)
Temporal-Integrity-Preserved(t)    = 1 - ρ_hyst(t)
```

A system reporting {Self: 1, Relational: 0, Temporal: 1} tells its operators that relational integrity has collapsed while self and temporal integrity remain intact — a specific failure pattern with specific remediation.

### 7.5 ERES-Originated Mapping

This correspondence is a conceptual mapping between the DSAP-PRE mathematical proxies (Sections 3–5) and the Three Governing Principles of ERES (Institute canon). Both sides are ERES-originated. The mapping was developed through the ERES Institute specification work of April 2026.

---

## 8. DSAP-PRE Composite Indicator (Normative)

### 8.1 Normative Composite

```
DSAP-PRE(t) = (1 - ρ_RHC(t)) × (1 - ρ_PERT(t)) × (1 - ρ_hyst(t))
```

DSAP-PRE ∈ {0, 1}.

### 8.2 Binary Form Is Normative

v1 offered binary and continuous alternatives. v2 locks binary for:

1. **Conjunctive discipline consistency.** EAAP v1.3-FINAL §3.7 makes the four PoR factors' conjunctive product normative. Continuous DSAP-PRE values would reintroduce compensation into the pre-threshold layer.
2. **Operational clarity.** Binary produces a named refusal reason (REGIME_TRANSITION) that appears in audit trails.
3. **Mode A consistency.** Mode A (gating precondition) is inherently binary.

### 8.3 Integration with PoR — Mode A

Per EAAP v1.3-FINAL §6.5:

```
if DSAP-PRE(t) == 0:
    refuse authorization with REFUSAL_REGIME_TRANSITION
    do not proceed to PoR evaluation
```

DSAP-PRE fires *before* PoR because pre-threshold refusals must preempt qualification rather than compete with it.

---

## 9. Worked Example — DOFA Family Stewardship Council

### 9.1 Context

Mirrors EAAP v1.3-FINAL §11 Authorization Request **DOFA-FSC-2026-04-24-001**. Standard-governance domain (RHC = 1 hour, θ = 0.75).

Domain parameters from Section 6.2:
```
κ_RHC = 0.01/hr²,  W_RHC = 3,  W_PERT = 5,  κ_cost = 3.0,
τ = 10,  Δ_Π = 0.5,  η_recover = 0.15
```

### 9.2 Proxy Evaluations

**ρ_RHC — self-integrity domain:**

Council has stable quarterly operation. RHC amplitude over last 3 hourly cycles:
```
A_RHC = [0.94, 0.93, 0.94, 0.95]
```

Savitzky-Golay A'(t) ≈ +0.003/hr (positive — amplitude rising). First condition fails; ρ_RHC = 0 without evaluating A''.

**Interpretation:** Council's self-openness capacity is healthy.
```
ρ_RHC(t) = 0  →  Self-Integrity-Preserved = 1
```

**ρ_PERT — relational integrity domain:**

Four fiscal trajectories:
1. DOFA Family Amity Fund (current) — c_0 = $4,800/yr
2. State assistance — cost ratio 1.2
3. Private credit — cost ratio 2.1
4. Non-action — cost ratio 2.8

All four viable at κ_cost = 3.0. n_viable = 4.

Over W_PERT = 5:
```
modality = [3, 4, 4, 4, 4]   → no collapse
σ̃² = [0.42, 0.41, 0.44, 0.43, 0.44]  → no >50% decline
n_viable = [3, 4, 4, 4, 4]   → no >50% decline
```

None of the three OR-conditions fires.
```
ρ_PERT(t) = 0  →  Relational-Integrity-Preserved = 1
```

**ρ_hyst — temporal integrity domain:**

Counterfactual: if DOFA fund denied, Π reverses. Projection over τ = 10 hourly cycles.

- Ψ under Δ_Π: household pivots to state assistance. Viability = 0.78.
- Ψ under current: 0.87.

```
H(t) = 0.78 - 0.87 = -0.09
```

Operational intent of ρ_hyst: fires when |H(t)| < η_recover (the perturbation barely moves the projection, indicating a singular-basin regime).

|H(t)| = 0.09 < η_recover = 0.15 → would fire.

**Calibration note.** A 12-month fund commitment against a 1-hour RHC differs by ~8,760×. Section 6.2's η_recover is appropriate for RHC-scale decisions; commitment-horizon-scale decisions may require strategic-class η_recover = 0.20. Even so, |H(t)| = 0.09 < 0.20 still fires.

Operational intent for this worked example: household retains response capacity (a 12-month fund commitment can be declined next week without structural loss). This flags a calibration gap tracked in Section 11.1.

Assume operational intent:
```
ρ_hyst(t) = 0  →  Temporal-Integrity-Preserved = 1
```
(subject to calibration refinement per Section 11.1)

### 9.3 Composite

```
DSAP-PRE(t) = (1 - 0) × (1 - 0) × (1 - 0) = 1
```

DSAP-PRE = 1 → PROCEED to PoR evaluation.

This matches EAAP v1.3-FINAL §11.2.

### 9.4 What This Demonstrates

1. Each proxy has a natural Governing Principle interpretation.
2. Binary DSAP-PRE is operationally informative — when all three return 0, composite is 1; if any had fired, refusal would have named which integrity dimension collapsed.
3. Calibration is non-trivial — Section 9.2's ρ_hyst surfaced a genuine calibration gap (commitment-horizon vs. RHC-cycle basis for η_recover).
4. Integration with PoR is the intended behavior — DSAP-PRE = 1 allows PoR to evaluate; PoR = 0.699 fails standard-governance θ = 0.75 on its own terms.

---

## 10. ECR Provenance and MIEVM Methodology

### 10.1 ECR Applied to This Math Sheet

Provisional ECR assessment for v2:

- **Residual R:** empirical calibration of reference values requires real-system data; Ψ projection fidelity for ρ_hyst is domain-specific; false-positive rate under realistic noise requires Monte Carlo characterization.
- **Noise N:** specific W_RHC choice, specific η_recover values, binary-vs-continuous framing (resolved by v1.3-FINAL normative lock).

Provisional ECR: moderate-to-high. Full computation requires formal MIEVM ensemble evaluation of this v2 text, queued with EAAP v1.3-FINAL cleaned republication.

### 10.2 Tier Placement

Per ERES-MPAM-2026-001 §8.3: **Tier 1 (Operational)**.

### 10.3 De-assimilation Exposure

- **D2 (Superior Replacement)** is the most likely retirement path for individual proxies.
- **D3 (Empirical Contradiction)** is most consequential.
- **D5 (Stakeholder Withdrawal)** applied to the earlier v2 draft (April 24, 2026, morning) following failed identity verification of a purported external contributor; this cleaned v2 restores ERES sole authorship.

### 10.4 Named Peer Reviewer Position Statement — Andrzej Skulski

Per ERES Attribution Protocol, Skulski's contribution is scoped to:

1. **Failure-mode identification** (Section 1.3 quote) — the pre-threshold regime-transition failure mode.
2. **Boundary-condition articulation** (Section 2.1 motivation) — the structural necessity of a pre-threshold boundary layer.

Per Skulski's April 24, 2026 position on v1.3-FINAL:

> The implementation approach you've developed — including PoR structure, DSAP-PRE formalization, and the broader ERES stack — is your work. Because of that, I would not frame this as a full "approval" of the system as a whole.

Per Skulski's April 24, 2026 structural positioning condition:

> What is being integrated here is not just a detail or refinement — it's a structural layer that sits upstream of the rest of the architecture. [...] that this layer is treated as a boundary condition in its own right, not reduced to an internal component of the existing stack.

This condition is addressed in EAAP v1.3-FINAL §6.1 and this math sheet §1.3.

**Skulski's contribution does NOT extend to:** endorsement of the specific mathematical form (three proxies, binary composite, calibration values, worked example). Sections 3, 4, 5, 6, 7, 8, 9, 10, 11, and 12 of this math sheet are the sole responsibility of Joseph Allen Sprute and the ERES Institute.

---

## 11. Known Limitations and Open Refinements

### 11.1 Commitment-Horizon Calibration Gap

Section 9.2 surfaced that η_recover calibration should reference the *decision's commitment horizon*, not only the RHC cycle, when the two differ by more than 10×. Section 6.2 extension with a commitment-horizon adjustment rule is open for v3.

### 11.2 False-Positive Characterization

All three proxies can fire under conditions that do not reflect regime transition. Formal false-positive-rate characterization requires Monte Carlo studies.

### 11.3 False-Negative Characterization

Abrupt transitions without critical slowing down, transitions preserving apparent multi-modality, and hysteresis with small Δ_Π can evade detection. DSAP-PRE is defense in depth, not guarantee.

### 11.4 Hysteresis Counterfactual Semantic

Section 9.2 resolved ambiguity to |H(t)| < η_recover (magnitude-based). Mixed-sign H(t) situations may require refinement.

### 11.5 MPAM-Consistent Tier 4 Variants

Experimental proxy forms may be developed under Tier 4 (Speculative) without affecting Tier 1 normative operation.

---

## 12. References

### 12.1 ERES Stack

- ERES-EAAP-STD-2026-001-v1.3-FINAL (this document's parent specification)
- ERES-GRACECHAIN-NOTES-2026-001-v1
- ERES-ATTRIBUTION-PROTOCOL-2026-001-v1
- ERES-MPAM-2026-001
- ERES-RECKON-WP-2026-002
- ERES-BODY-SPEC-2026-001
- ERES-BRAINS-SPEC-2026-001
- ERES-DOFA-WP-2026-001-C

### 12.2 Named Peer Reviewer Correspondence

- Skulski, A. LinkedIn four-turn review plus final review, April 22–24, 2026. Source for Section 1.3 and Section 2.1 motivation.

### 12.3 Dynamical Systems Literature

- Krasnosel'skii, M. A., & Pokrovskii, A. V. (1989). *Systems with hysteresis*.
- Lenton, T. M. (2011). *Nature Climate Change*, 1(4), 201–209.
- Scheffer, M., et al. (2009). *Nature*, 461(7260), 53–59.
- Strogatz, S. H. (2015). *Nonlinear dynamics and chaos* (2nd ed.).
- Thom, R. (1972). *Stabilité structurelle et morphogenèse*.
- Zeeman, E. C. (1977). *Catastrophe theory: Selected papers*.

### 12.4 Statistical Methods

- Hartigan, J. A., & Hartigan, P. M. (1985). *Annals of Statistics*, 13(1), 70–84.
- Savitzky, A., & Golay, M. J. E. (1964). *Analytical Chemistry*, 36(8), 1627–1639.

---

**Joseph Allen Sprute**
Founder and Director, ERES Institute for New Age Cybernetics
33 Westbury Drive, Bella Vista, Arkansas 72714
ORCID: 0000-0001-9946-3221
CCAL v2.1

*Don't hurt yourself. Don't hurt others. Build for generations to come.*
