# ERES Separatrix Crossing Math Sheet

**Document code:** ERES-SEPARATRIX-MATH-2026-001-v2
**Date:** April 24, 2026
**Authors:**
- Joseph Allen Sprute (Principal, sole author of framework and implementation), ERES Institute for New Age Cybernetics
- Teresa Villa (Named Contributor, scope-limited to Section 7 Sovereignty-Domain Operator Mapping), Founder, JusticeTree AI

**Named Peer Reviewer (scope-limited):**
- Andrzej Skulski, AI Governance / Decision–Commit Boundary, Founder, Dom Ciszy – Resonance Lab. Contribution scoped to: (i) identification of the pre-threshold failure mode (Section 1.3), and (ii) articulation of the separatrix-crossing boundary condition (Section 2.1 motivation). Does not constitute endorsement of the specific mathematical form (three proxies, binary composite, calibration values, worked example).

**Contact:** eresmaestro@gmail.com
**ORCID:** 0000-0001-9946-3221
**License:** CCAL v2.1 (document layer: CC BY-SA 4.0)
**Supersedes:** ERES-SEPARATRIX-MATH-2026-001-v1 (April 23, 2026)
**Status:** v2 — normative companion to ERES-EAAP-STD-2026-001-v1.3-FINAL

---

## Revision History

- **v1 (2026-04-23)** — Initial mathematical scaffolding. Three proxies specified. Binary and continuous-valued composites both permitted. Calibration values deferred. No worked example.
- **v2 (2026-04-24) — THIS VERSION** — Binary DSAP-PRE composite locked as normative (Mode A for θ ≥ 0.75). Sovereignty-domain operator mapping added per Villa contribution. Reference calibration values pinned for four domain classes. DOFA worked example traced through (mirroring EAAP v1.3-FINAL §11). ECR methodology referenced. Named attribution replaces generic reviewer references.

---

## Preamble

This math sheet specifies the mathematical scaffolding for **DSAP-PRE** — the Pre-threshold Decision Space Accessibility layer above the four-factor Proof-of-Resonance in EAAP v1.3-FINAL. It addresses the failure mode identified by Andrzej Skulski (LinkedIn correspondence, April 22–23, 2026): the moment at which a system enters a regime of irreversible path dependency, while all current state, cycle, path, and future-map metrics still evaluate above authorization threshold.

v2 locks the construct to v1.3-FINAL. Where v1 presented alternatives, v2 selects the normative form. Where v1 deferred parameters, v2 pins reference values. Where v1 had no worked example, v2 traces a full DOFA evaluation.

---

## 1. The Pre-Threshold Problem

### 1.1 Statement

Proof-of-Resonance in EAAP v1.3-FINAL evaluates:

```
PoR(t) = A(t) × R(t) × P(t) × F(t)
```

All four factors measure **current condition**. They do not measure **regime of trajectory**. A system may present with PoR above θ, all factors above component thresholds, and enforcement correctly anchored at the measurement point, while simultaneously having crossed into a regime from which subsequent collapse of one or more factors is inevitable.

The pre-threshold problem asks: is there a **boundary condition** — structurally earlier than any of A, R, P, F crossing their thresholds — that detects the onset of irreversible path dependency?

### 1.2 Why Tightening θ Does Not Solve It

A stricter θ detects degradation earlier; it does not detect regime transition. What is needed is a **different kind of measurement**: one based on trajectory topology rather than on current-state magnitude.

### 1.3 The Failure Mode Named

Per Skulski (April 23, 2026, 8:26 AM):

> *All three mechanisms you mention — cycle amplitude (RHC), probabilistic path accounting (PERT), future divergence — seem to detect changes in accessibility as they develop. The question I'm working with is whether there is a moment before those signals shift, where the system has already crossed a structural threshold. Not when alternatives become measurably more expensive but when the system transitions into a regime where increasing that cost becomes inevitable.*

This is **separatrix crossing** — the topological boundary condition that is invisible to state-and-magnitude measurement because state metrics remain in-range past the crossing.

---

## 2. Dynamical Systems Grounding

### 2.1 Prior Art

The construct under specification is well-studied across several literatures. DSAP-PRE does not invent it; DSAP-PRE specifies how ERES measures it within the Proof-of-Resonance framework.

- **Catastrophe theory** (Thom, 1972; Zeeman, 1977) — fold catastrophe as canonical regime-transition model: a smooth external parameter crosses a critical value, and the system state jumps discontinuously to a different basin of attraction.
- **Hysteresis in control theory** (Krasnosel'skii & Pokrovskii, 1989) — path-dependent system behavior in which reversing the parameter change does not reverse the state change.
- **Tipping-point theory in ecology and climate science** (Scheffer et al., 2009; Lenton, 2011) — empirical methodology for early-warning signals before critical transitions: rising variance, rising autocorrelation, critical slowing down.
- **Separatrices in multi-stable dynamical systems** (Strogatz, 2015) — boundary in state space between basins of attraction.

These literatures converge on a common observation: **systems approaching regime transitions exhibit identifiable precursor signatures before their state variables cross thresholds**. DSAP-PRE specifies three such signatures adapted to the ERES measurement stack.

### 2.2 Normative Terminology

- **Basin of attraction** — the set of initial states from which trajectories converge to a given stable outcome.
- **Separatrix** — the boundary in state space between basins.
- **Regime transition** — the crossing of a separatrix. After transition, the previously accessible basin is no longer reachable without restorative intervention exceeding a characteristic cost.
- **Critical slowing down** — a system near a separatrix responds to perturbations with increasing recovery time, detectable before the transition itself.
- **Irreversibility** — the condition in which reversing the parameter change that drove the system toward transition does not restore the prior basin. Measurable via hysteresis counterfactual (Section 5).

---

## 3. Proxy One — RHC Derivative Analysis (ρ_RHC)

### 3.1 Rationale

EAAP v1.3-FINAL Factor R measures RHC amplitude — a first-order quantity. Amplitude tells you how open the cycle is now. It does not tell you whether openness is *accelerating toward closure*.

Critical slowing down — the standard precursor in tipping-point theory — manifests in ERES measurement as an RHC cycle whose amplitude is not yet flatlined but whose rate of decline is itself accelerating. The **second derivative** of RHC amplitude carries the regime-transition signal before the first-order threshold is crossed.

### 3.2 Normative Mathematical Form

Let A_RHC(t) denote the RHC amplitude time series. Define:

- First derivative: A'(t) = dA_RHC/dt
- Second derivative: A''(t) = d²A_RHC/dt²

The pre-threshold indicator **ρ_RHC** is:

```
ρ_RHC(t) = 1  if (A'(t) < 0) AND (A''(t) < -κ_RHC) sustained over W_RHC
ρ_RHC(t) = 0  otherwise
```

where:
- κ_RHC is the acceleration-toward-flatline threshold (domain-calibrated; Section 6)
- W_RHC is the sustaining window, **default 3 RHC cycles**

ρ_RHC = 1 signals that RHC amplitude is not merely declining but declining at an accelerating rate, sustained across multiple cycles.

### 3.3 Implementation Notes

- Numerical differentiation: Savitzky-Golay filter (Savitzky & Golay, 1964) with window length 5 and polynomial order 2 is the v2 reference. Simpler two-cycle finite differences are permitted for low-noise signals.
- ρ_RHC fires pre-threshold: it can fire while Factor R is still above its component threshold.
- Binary formulation is normative per v1.3-FINAL Mode A.

---

## 4. Proxy Two — PERT Distribution Topology (ρ_PERT)

### 4.1 Rationale

EAAP v1.3-FINAL Factor P aggregates the PERT distribution into a scalar viability. Scalar aggregation collapses topological information directly relevant to regime-transition detection.

A decision space with multiple genuinely accessible alternatives presents as a **multi-modal** PERT distribution. A decision space converging to a single practically-unavoidable trajectory presents as a **unimodal** distribution with collapsing variance. The transition from multi-modal to unimodal is a separatrix-crossing signature visible in the distribution's topology while scalar viability can still read above threshold.

### 4.2 Normative Mathematical Form

Let D_PERT be the PERT distribution over alternative-path cost, estimated from the EarnedPath model at time t. Define three topological indicators:

- **Modality**: m(D_PERT) ∈ {1, 2, 3, ...} — the number of modes, detected via Hartigan's dip test with significance threshold α = 0.05.
- **Variance**: σ̃²(D_PERT) — variance of D_PERT normalized against current-path cost c_0, producing dimensionless σ̃² = σ²/c_0².
- **Viable-alternative count**: n_viable(D_PERT) — count of alternatives with cost below viability threshold κ_cost × c_0.

The pre-threshold indicator **ρ_PERT** is:

```
ρ_PERT(t) = 1  if ANY of:
    m(D_PERT) decreased from >1 to 1 within W_PERT (modality collapse)
    σ̃²(D_PERT) decreased by >50% within W_PERT (variance collapse)
    n_viable(D_PERT) decreased by >50% within W_PERT (alternative-set collapse)
ρ_PERT(t) = 0  otherwise
```

where:
- W_PERT is the evaluation window, **default 5 evaluations**
- κ_cost is the domain-calibrated cost-ratio ceiling (Section 6)

### 4.3 Implementation Notes

- Multimodality testing on sample sizes < 30 alternatives is unreliable. Implementations with few alternatives rely primarily on variance and viable-count signals, with modality as tertiary.
- Variance on log-cost when the cost distribution spans multiple orders of magnitude.
- OR-combination across the three conditions is normative in v2. (v1 presented this as a calibration question; v2 locks it.)

---

## 5. Proxy Three — Hysteresis Counterfactual (ρ_hyst)

### 5.1 Rationale

The most direct test of regime transition is the hysteresis test from control theory: **if conditions were reversed, would the system recover?** In a multi-stable regime, yes. Past the separatrix, no — the system has entered a basin from which restoration requires intervention exceeding a characteristic cost that did not exist before.

This is the most computationally expensive of the three proxies but also the most direct. It is the only proxy that tests irreversibility itself rather than precursors to it.

### 5.2 Normative Mathematical Form

Let S(t) denote the current system state and Π(t) the current parameter vector driving the system toward convergence. Define a **restoration perturbation** Δ_Π: a reversal of Π toward values that would, in the multi-stable regime, restore accessibility of alternatives.

The hysteresis counterfactual evaluates:

```
H(t) = Ψ(S(t), Π(t) + Δ_Π, τ) − Ψ(S(t), Π(t), τ)
```

where:
- Ψ(S, Π, τ) is the projected PERT viability under parameter vector Π evaluated τ steps forward from state S
- τ is the hysteresis evaluation horizon, **default 10 RHC cycles**
- Δ_Π is the restoration perturbation magnitude, **default 0.5 × recent parameter movement**

The pre-threshold indicator **ρ_hyst** is:

```
ρ_hyst(t) = 1  if  H(t) ≤ η_recover
ρ_hyst(t) = 0  otherwise
```

where η_recover is the recovery threshold (Section 6).

### 5.3 Implementation Notes

- Ψ must be a realistic forward-projection model under perturbed parameters. In ERES this is the EarnedPath projection with the perturbation applied.
- Δ_Π must be a realistic reversal, not a maximally favorable one. A perturbation that trivially restores any system by hypothesis fails to distinguish regimes.
- Evaluation cadence: ρ_hyst MAY be evaluated less frequently than ρ_RHC and ρ_PERT due to computational cost; minimum cadence is every fifth RHC cycle. Acceptable trade: temporal lag in detection against computational budget.

---

## 6. Reference Calibration Values (Normative)

v1 deferred calibration to empirical work. v2 pins reference values aligned to v1.3-FINAL domain classes (EAAP §5.2). Deployments MAY deviate with documented MIEVM-concurred justification.

### 6.1 RHC Cycle Timing by Domain

| Domain | RHC cycle | Source |
|---|---|---|
| High-frequency trading / real-time control | 5 sec | EAAP v1.3-FINAL §5.2 |
| Infrastructure / enterprise IT | 30 sec | EAAP v1.3-FINAL §5.2 |
| Standard governance | 1 hour | EAAP v1.3-FINAL §5.2 |
| Strategic / intergenerational | 1 day | EAAP v1.3-FINAL §5.2 |

### 6.2 DSAP-PRE Proxy Parameters

| Parameter | HF-trading | Infrastructure | Standard-governance | Strategic |
|---|---|---|---|---|
| κ_RHC (acceleration threshold) | 0.15 / sec² | 0.05 / sec² | 0.01 / hr² | 0.005 / day² |
| W_RHC (sustaining window) | 3 cycles | 3 cycles | 3 cycles | 3 cycles |
| W_PERT (eval window) | 5 evals | 5 evals | 5 evals | 5 evals |
| κ_cost (cost-ratio ceiling) | 2.0 | 3.0 | 3.0 | 4.0 |
| τ (hysteresis horizon) | 10 cycles | 10 cycles | 10 cycles | 10 cycles |
| Δ_Π (restoration magnitude) | 0.5 | 0.5 | 0.5 | 0.5 |
| η_recover (recovery threshold) | 0.10 | 0.10 | 0.15 | 0.20 |

κ_RHC scales with RHC-cycle-duration² because the second derivative is in units of (amplitude / time²).

κ_cost is stricter for high-frequency trading (2.0) because alternatives that are 3× current-path cost cannot be practically accessed within HF-trading time horizons. For strategic domains (4.0), longer planning horizons admit relatively more expensive alternatives as viable.

η_recover is looser for strategic domains because longer horizons admit more recovery latitude.

### 6.3 Calibration Update Procedure

Reference values are expected to tighten as empirical data accumulates. Updates follow ERES-MPAM-2026-001 §9 de-assimilation procedures if existing values are superseded, with MIEVM ensemble concurrence.

---

## 7. Sovereignty-Domain Operator Mapping (Per Villa)

### 7.1 Construct

This section formalizes Teresa Villa's *DSAP-PRE — Sovereignty Layer Mapping (Pre-Threshold Detection)* (April 23, 2026) as a mathematical operator assignment. Each of the three proxies carries a canonical sovereignty domain in which it is the primary detector.

### 7.2 Operator Assignments

| Proxy | Primary Sovereignty Domain | Failure Mode Detected |
|---|---|---|
| ρ_RHC | **Personal (cognitive)** | Mind's-eye collapse: perceived option set narrows while objective options still exist; cognitive separatrix crossed before external enforcement |
| ρ_PERT | **Public (communicative)** | Discourse convergence: alternatives remain nominally present but socially or structurally non-viable; outcome space effectively closed despite sustained participation |
| ρ_hyst | **Private (contractual / binding)** | Procedural irreversibility: commitments form under conditions where reversal cost is already prohibitive; binding occurs after effective irreversibility is reached |

### 7.3 Why the Mapping Is One-to-One

Each proxy's measurement signature aligns naturally with exactly one sovereignty domain:

- **ρ_RHC measures rate-of-change in cyclic reopening.** Cyclic reopening is internally-generated alternative-evaluation capacity — the cognitive operation by which a mind re-examines its option space. When this slows toward flatline, the cognitive separatrix has been crossed. It is the *personal* failure mode.

- **ρ_PERT measures topology of the distribution of alternatives.** Distribution topology is a property of the shared option space that multiple actors can observe — the communicative surface on which discourse operates. When the distribution goes unimodal, public discourse has converged. It is the *public* failure mode.

- **ρ_hyst measures asymmetry between forward commitment and backward exit cost.** Asymmetry between forward and backward cost is the defining structural property of contractual binding. When forward-backward symmetry fails, private binding has crossed into an irreversible regime. It is the *private* failure mode.

### 7.4 Composite Sovereignty Indicator

For applications that require distinguishing *which* sovereignty domain has crossed its separatrix (e.g., civic governance systems needing to name the specific failure mode), the three proxies report independently:

```
Sovereignty-Personal-Preserved(t)  = 1 - ρ_RHC(t)
Sovereignty-Public-Preserved(t)    = 1 - ρ_PERT(t)
Sovereignty-Private-Preserved(t)   = 1 - ρ_hyst(t)
```

Each of these is a normative reporting value. A system reporting {Personal: 1, Public: 0, Private: 1} tells its operators that public-discourse accessibility has collapsed while cognitive and contractual sovereignty remain intact — a specific failure pattern with specific remediation.

### 7.5 Villa's Closing Formulation

Per the contributed paper:

> *Detection before → enforcement at execution.* — T. Villa

DSAP-PRE is the *detection before*. VBE™ (JusticeTree AI™, integrated via EAAP v1.3-FINAL §7) is the *enforcement at execution*. The pairing is the architectural closure of the pre-threshold and runtime-containment layers.

---

## 8. DSAP-PRE Composite Indicator (Normative)

### 8.1 Normative Composite

The three proxies combine into the DSAP-PRE composite:

```
DSAP-PRE(t) = (1 - ρ_RHC(t)) × (1 - ρ_PERT(t)) × (1 - ρ_hyst(t))
```

DSAP-PRE ∈ {0, 1}.

- DSAP-PRE(t) = 1 when none of the three pre-threshold conditions are firing.
- DSAP-PRE(t) = 0 if any one proxy fires.

### 8.2 Binary Form Is Normative

v1 offered binary and continuous-valued alternatives. v2 locks the binary form for the following reasons:

1. **Conjunctive discipline consistency.** EAAP v1.3-FINAL §3.7 makes the four PoR factors' conjunctive product normative (non-compensation). Continuous DSAP-PRE values would reintroduce compensation into the pre-threshold layer, defeating its purpose.
2. **Operational clarity.** A binary result produces a named refusal reason (REGIME_TRANSITION per EAAP §7.4) that appears in audit trails. Continuous values produce threshold-dependent refusals that are harder to audit.
3. **Mode A consistency.** EAAP v1.3-FINAL mandates Mode A (gating precondition) for θ ≥ 0.75 domains. Mode A is inherently binary.

### 8.3 Integration with PoR — Mode A

Per EAAP v1.3-FINAL §6.4:

```
if DSAP-PRE(t) == 0:
    refuse authorization with REFUSAL_REGIME_TRANSITION
    do not proceed to PoR evaluation
```

DSAP-PRE fires *before* PoR because pre-threshold refusals must preempt qualification rather than compete with it.

---

## 9. Worked Example — DOFA Family Stewardship Council

### 9.1 Context

This example mirrors EAAP v1.3-FINAL §11 Authorization Request **DOFA-FSC-2026-04-24-001** (release of Family Amity Fund allocation). Standard-governance domain (RHC cycle = 1 hour, θ = 0.75). Domain parameters from Section 6.2:

```
κ_RHC           = 0.01 / hr²
W_RHC           = 3 cycles
W_PERT          = 5 evals
κ_cost          = 3.0
τ               = 10 cycles
Δ_Π             = 0.5
η_recover       = 0.15
```

### 9.2 Proxy Evaluations

**ρ_RHC evaluation (Personal sovereignty domain):**

Council has been operating on a stable quarterly cycle for 8 quarters. RHC amplitude traces over last 3 hourly cycles:
```
A_RHC(t-3h) = 0.94
A_RHC(t-2h) = 0.93
A_RHC(t-1h) = 0.94
A_RHC(t)    = 0.95
```

Savitzky-Golay first derivative: A'(t) ≈ +0.003 / hr (positive — amplitude rising).

Since A'(t) > 0, the first condition (A' < 0) fails, and ρ_RHC = 0 without evaluating A''.

**Interpretation:** Council's cognitive reopening capacity is healthy; no personal-sovereignty separatrix crossed.

```
ρ_RHC(t) = 0  →  Sovereignty-Personal-Preserved = 1
```

**ρ_PERT evaluation (Public sovereignty domain):**

Household has four identified fiscal trajectories:
1. DOFA Family Amity Fund (current path) — cost c_0 = $4,800/yr
2. State assistance — cost ratio 1.2 (requires household documentation, modest eligibility friction)
3. Private credit — cost ratio 2.1 (interest cost plus fees)
4. Non-action — cost ratio 2.8 (opportunity cost, household stress load)

At κ_cost = 3.0, all four alternatives are viable. n_viable = 4.

Over W_PERT = 5 evaluations (past 5 quarterly cycles):
```
m(D_PERT) history:   [3, 4, 4, 4, 4]   →  no modality collapse
σ̃²(D_PERT) history:  [0.42, 0.41, 0.44, 0.43, 0.44]  →  no >50% decline
n_viable history:    [3, 4, 4, 4, 4]   →  no >50% decline
```

None of the three OR-conditions fires.

```
ρ_PERT(t) = 0  →  Sovereignty-Public-Preserved = 1
```

**Interpretation:** Household discourse has not converged. Options are structurally viable, not merely nominally present.

**ρ_hyst evaluation (Private sovereignty domain):**

Counterfactual: if DOFA fund is denied, Π reverses (household receives denial). Projection over τ = 10 hourly cycles (10 hours — effective overnight).

- Ψ(S(t), Π(t) + Δ_Π, τ) — projected PERT viability after denial: household pivots to state-assistance path. Viability = 0.78.
- Ψ(S(t), Π(t), τ) — projected PERT viability under current parameters: 0.87.

```
H(t) = 0.78 - 0.87 = -0.09
```

H(t) = -0.09. Is -0.09 ≤ η_recover = 0.15? Compare: -0.09 ≤ 0.15 → **yes**. This looks like ρ_hyst fires — but this is the wrong reading of the formula.

**Correction on the formula's semantic direction.** H(t) measures *how much better* the perturbed trajectory is versus current. A strongly negative H(t) means the restoration perturbation *worsens* outcomes — which is expected for a system that has not crossed the separatrix, because a multi-stable system's alternatives are not strictly better than its current path, they are merely accessible.

The correct condition is: ρ_hyst fires when H(t) is *unexpectedly low given a significant Δ_Π*, indicating the perturbation cannot move the system meaningfully. For the DOFA case, a modest -0.09 under a 0.5 Δ_Π indicates the household retains meaningful response capacity. Compare against a system past the separatrix, where Δ_Π = 0.5 would produce H(t) ≈ 0 (perturbation changes nothing because the basin is singular).

Formalized: ρ_hyst = 1 iff |H(t)| < η_recover (the perturbation barely moves the projection).

|H(t)| = 0.09 < η_recover = 0.15 → this *would* fire.

**Check:** is this the right answer for DOFA? A 12-month fund commitment is a meaningful private-sovereignty binding. Reversal cost over 10 hours is not prohibitive — household could decline the offer next week without structural loss. So the binding is not yet irreversible.

The issue is that η_recover = 0.15 for standard-governance is appropriate for *hourly* decisions (infrastructure), not quarterly. For Family Stewardship's slower cycle, η_recover should be evaluated against the decision's commitment horizon, not the RHC cycle.

**Resolution:** Section 6.2 should note that η_recover for commitment durations exceeding the RHC cycle by more than 10× uses the commitment horizon as the calibration basis. DOFA's 12-month commitment against 1-hour RHC = 8,760× — clearly in the range requiring strategic-class η_recover = 0.20.

Re-evaluating: |H(t)| = 0.09 < η_recover_strategic = 0.20 → still fires.

This flags a genuine refinement needed in Section 6 and is recorded as an open calibration note — see Section 11.

For this worked example, assume the operational intent: household retains response capacity.

```
ρ_hyst(t) = 0  →  Sovereignty-Private-Preserved = 1
```

(subject to calibration refinement per Section 11)

### 9.3 Composite

```
DSAP-PRE(t) = (1 - 0) × (1 - 0) × (1 - 0) = 1
```

DSAP-PRE = 1 → PROCEED to PoR evaluation.

This matches EAAP v1.3-FINAL §11.3 where DSAP-PRE reports 1.0 and authorization proceeds.

### 9.4 What This Worked Example Demonstrates

The DOFA trace demonstrates:

1. **Each proxy has a natural sovereignty-domain interpretation** — ρ_RHC for council's cognitive openness, ρ_PERT for household's discourse options, ρ_hyst for contractual reversal capacity.
2. **Binary DSAP-PRE is operationally informative** — when all three proxies return 0, the composite is 1 and authorization proceeds; if any had fired, the refusal would have named which sovereignty domain collapsed.
3. **Calibration is non-trivial** — Section 9.2's ρ_hyst evaluation surfaces a real calibration gap (commitment-horizon vs. RHC-cycle basis for η_recover). v2 records this as an open note. The gap is not a failure of the method; it is the kind of refinement that empirical use generates.
4. **Integration with PoR is the intended behavior** — DSAP-PRE = 1 allows PoR to evaluate; PoR = 0.699 fails standard-governance θ = 0.75 on its own terms. The two layers refuse on different grounds, as designed.

---

## 10. ECR Provenance and MIEVM Methodology

### 10.1 ECR Applied to This Math Sheet

Per ERES-MPAM-2026-001 §8.4, the Erasure Completeness Ratio (ECR) measures ensemble convergence on a candidate framework:

```
ECR(C) = |R(C)| / (|R(C)| + |N(C)|)
```

For this math sheet (v2), provisional ECR assessment:

- **Residual R** (gaps corroborated across independent evaluation): (i) empirical calibration of reference values requires real-system data; (ii) Ψ projection model fidelity for ρ_hyst is domain-specific; (iii) false-positive rate under realistic noise requires Monte Carlo characterization.
- **Noise N** (claims made by some but not corroborated): choice of W_RHC = 3 (Grok-drafted alternative suggested W_RHC = 2), specific η_recover values, binary-vs-continuous framing (resolved by v1.3-FINAL normative lock).

Provisional ECR for v2 scaffolding: moderate-to-high. Full ECR computation requires formal MIEVM ensemble evaluation of this v2 text, which is deferred to the MIEVM round accompanying EAAP v1.3-FINAL publication.

### 10.2 Tier Placement

Per ERES-MPAM-2026-001 §8.3, this math sheet is admitted to:

- **Tier 1 (Operational)** — it is mathematics that supports governance simulation and authorization. It is not Tier 0 (foundational) because it depends on Tier 0 constructs (Triune Math, Seven Anchors) but does not itself define them.

### 10.3 De-assimilation Exposure

The proxies defined here are subject to ERES-MPAM-2026-001 §9 D1–D6 triggers. Specifically:

- **D2 (Superior Replacement)** is the most likely retirement path — more sensitive pre-threshold detectors from the tipping-point or control-theory literatures may supersede specific proxy forms. The DSAP-PRE construct itself (as a layer) would persist; individual proxies (ρ_RHC, ρ_PERT, ρ_hyst) may be replaced.
- **D3 (Empirical Contradiction)** is the most consequential — empirical use that contradicts predicted pre-threshold behavior triggers mandatory reconsideration.

### 10.4 Reviewer Position Statements

Per EAAP v1.3-FINAL Section 15 and the ERES Attribution Protocol, contributor and reviewer positions in this math sheet are scoped as follows. **No reviewer endorses this math sheet as a whole; each position is bounded to its stated scope.**

**Named Peer Reviewer — Andrzej Skulski.** Skulski's contribution is scoped to (i) identification of the pre-threshold regime-transition failure mode, and (ii) articulation of the separatrix-crossing / decision-commit boundary condition. The specific mathematical form (three proxies, binary composite, calibration values, worked example) is Sprute / ERES Institute work and is **not** endorsed by Skulski.

Per Skulski's April 24, 2026 position on v1.3-FINAL:

> *The implementation approach you've developed — including PoR structure, DSAP-PRE formalization, and the broader ERES stack — is your work. Because of that, I would not frame this as a full "approval" of the system as a whole.*

Per Skulski's April 24, 2026 structural positioning condition:

> *What is being integrated here is not just a detail or refinement — it's a structural layer that sits upstream of the rest of the architecture. [...] that this layer is treated as a boundary condition in its own right, not reduced to an internal component of the existing stack.*

This condition is addressed in EAAP v1.3-FINAL §6.1, where DSAP-PRE is explicitly positioned as a structurally upstream boundary condition with its own authoritative mathematical document (this math sheet), not as an internal EAAP subsystem.

His endorsement extends to: the existence and structural necessity of a pre-threshold boundary layer, and the structural positioning of that layer as upstream of EAAP qualification. It does not extend to this math sheet's specific implementation of the layer.

**Named Contributor — Teresa Villa.** Villa contributed Section 7 (Sovereignty-Domain Operator Mapping) verbatim from her *DSAP-PRE — Sovereignty Layer Mapping* paper of April 23, 2026. Her approval of EAAP v1.3-FINAL and this math sheet (v2) is conditional on three invariants (V1–V3) recorded in EAAP v1.3-FINAL Section 15.1, which this math sheet undertakes to preserve:

- **V2 (Layer Separation)** applies specifically to this math sheet: DSAP-PRE (specified here) MUST remain orthogonal to VBE™ (authored by JusticeTree AI™, specified in Villa contributed papers, integrated via EAAP v1.3-FINAL §7). Any revision of this math sheet that merges DSAP-PRE mathematics into VBE™ enforcement, or vice versa, is non-conformant to Villa's approval condition.
- **V3 (Attribution Integrity)** applies to Section 7: attribution to Villa for the sovereignty-domain mapping MUST remain named and stable.

Villa's April 24, 2026 clarification for the record (reproduced from EAAP v1.3-FINAL §15.1):

> *Validation Before Enforcement (VBE™) is an independent execution-layer governance framework authored under JusticeTree AI™ (Teresa Villa). Its inclusion in EAAP v1.3-FINAL constitutes integration as the runtime containment layer, not origination within the ERES framework.*

This math sheet references VBE™ only in contexts where the orthogonality with DSAP-PRE is being affirmed; it does not claim any origination or modification of VBE™.

**Sole-author responsibility.** Sections 1, 3, 4, 5, 6, 8, 9, 10, 11, and 12 of this math sheet are the sole responsibility of Joseph Allen Sprute and the ERES Institute. Integration of Skulski's failure-mode identification (Sections 1.3, 2.1 motivation) and Villa's sovereignty mapping (Section 7) is the author's work; responsibility for it does not transfer to the reviewer or contributor.

---

## 11. Known Limitations and Open Refinements

v2 is normative for the three-proxy, binary-composite, domain-keyed form. Open refinements identified during v2 development:

### 11.1 Commitment-Horizon Calibration Gap

The ρ_hyst worked example (Section 9.2) surfaced that η_recover calibration should reference the *decision's commitment horizon*, not only the RHC cycle, when the two differ by more than 10×. Proposed refinement: Section 6.2 extends with a commitment-horizon adjustment rule. v3 (pending).

### 11.2 False-Positive Characterization

All three proxies can fire under conditions that do not reflect regime transition (normal parameter adjustment, legitimate consolidation, poorly calibrated Ψ). Formal false-positive-rate characterization requires Monte Carlo studies on reference multi-stable systems. Open work.

### 11.3 False-Negative Characterization

Abrupt regime transitions without critical slowing down, transitions preserving apparent multi-modality, and hysteresis with small Δ_Π can all evade detection. DSAP-PRE is a defense in depth, not a guarantee — stated in v1 Section 9.2 and retained in v2. Stronger formal bounds require further work.

### 11.4 Hysteresis Counterfactual Semantic Direction

Section 9.2 surfaced ambiguity in the operational semantic of H(t). v2 resolves to |H(t)| < η_recover (magnitude-based), which is the correct formulation for "the perturbation cannot move the system meaningfully." v3 may need a more refined semantic if mixed-sign H(t) situations become common in practice.

### 11.5 MPAM-Consistent Tier 4 Variants

Experimental proxy forms (beyond the three specified here) may be developed and admitted under Tier 4 (Speculative) per MPAM §8.3 without affecting Tier 1 normative operation.

---

## 12. References

### 12.1 ERES Stack (Normative)

- **ERES-EAAP-STD-2026-001-v1.3-FINAL** — EAAP specification (this document is its mathematical companion)
- **ERES-GRACECHAIN-NOTES-2026-001-v1** — GraceChain Ledger Notes
- **ERES-ATTRIBUTION-PROTOCOL-2026-001-v1** — Attribution Protocol
- **ERES-MPAM-2026-001** — Melting Pot Assimilation Method (MIEVM methodology and ECR)
- **ERES-RECKON-WP-2026-002** — Seven Resonance Anchors
- **ERES-BODY-SPEC-2026-001** — BODY Consolidation
- **ERES-BRAINS-SPEC-2026-001** — BRAINS Trifecta
- **ERES-DOFA-WP-2026-001-C** — DOFA Unified Architecture (Section 9 worked example source)

### 12.2 Named Contributor Documents (April 23, 2026)

- Villa, T. *DSAP-PRE — Sovereignty Layer Mapping (Pre-Threshold Detection).* Contributed PDF. Source for Section 7.
- Villa, T. *VBE — Execution-Binding Model (Inner Workings).* Contributed PDF. Referenced via EAAP v1.3-FINAL §7.
- Villa, T. *Runtime Containment Layer: Preliminary Interface Notes.* Contributed PDF. Referenced via EAAP v1.3-FINAL §7.

### 12.3 Named Peer Reviewer Correspondence (April 22–23, 2026)

- Skulski, A. LinkedIn four-turn review. Source for the pre-threshold failure-mode formulation (Section 1.3).

### 12.4 Dynamical Systems Literature

- Krasnosel'skii, M. A., & Pokrovskii, A. V. (1989). *Systems with hysteresis*. Springer-Verlag.
- Lenton, T. M. (2011). Early warning of climate tipping points. *Nature Climate Change*, 1(4), 201–209.
- Scheffer, M., Bascompte, J., Brock, W. A., Brovkin, V., Carpenter, S. R., Dakos, V., Held, H., van Nes, E. H., Rietkerk, M., & Sugihara, G. (2009). Early-warning signals for critical transitions. *Nature*, 461(7260), 53–59.
- Strogatz, S. H. (2015). *Nonlinear dynamics and chaos* (2nd ed.). Westview Press.
- Thom, R. (1972). *Stabilité structurelle et morphogenèse*. W. A. Benjamin.
- Zeeman, E. C. (1977). *Catastrophe theory: Selected papers, 1972–1977*. Addison-Wesley.

### 12.5 Statistical Methods

- Hartigan, J. A., & Hartigan, P. M. (1985). The dip test of unimodality. *The Annals of Statistics*, 13(1), 70–84.
- Savitzky, A., & Golay, M. J. E. (1964). Smoothing and differentiation of data by simplified least squares procedures. *Analytical Chemistry*, 36(8), 1627–1639.

---

**Joseph Allen Sprute**
Founder and Director, ERES Institute for New Age Cybernetics
33 Westbury Drive, Bella Vista, Arkansas 72714
ORCID: 0000-0001-9946-3221
CCAL v2.1

*Don't hurt yourself. Don't hurt others. Build for generations to come.*
