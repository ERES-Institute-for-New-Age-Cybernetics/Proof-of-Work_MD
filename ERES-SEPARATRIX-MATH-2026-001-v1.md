# ERES Separatrix Crossing Math Sheet

**Document code:** ERES-SEPARATRIX-MATH-2026-001-v1
**Date:** April 23, 2026
**Author:** Joseph Allen Sprute, ERES Institute for New Age Cybernetics
**Contact:** eresmaestro@gmail.com
**ORCID:** 0000-0001-9946-3221
**License:** CCAL v2.1 (document layer: CC BY-SA 4.0)
**Status:** Working document — precursor to ERES-DSAP-PRE-SPEC-2026-001

---

## Preamble

This math sheet specifies the mathematical scaffolding for **DSAP-PRE** — the Pre-threshold Decision Space Accessibility layer above the four-factor Proof-of-Resonance in EAAP v1.3. It addresses a failure mode identified through peer review during April 2026: the moment at which a system enters a regime of irreversible path dependency, while all current state, cycle, path, and future-map metrics still evaluate above authorization threshold.

This is a working document, not a specification. It grounds the construct in established dynamical-systems literature, names three measurable proxies, and specifies enough mathematics for a reference implementation. A full specification document (ERES-DSAP-PRE-SPEC-2026-001) will follow once the math sheet has been peer-reviewed and refined.

---

## 1. The Pre-Threshold Problem

### 1.1 Statement

Proof-of-Resonance in EAAP v1.3-DRAFT evaluates:

**PoR = A × R × P × F**

where A is anchor product (state consistency), R is RHC amplitude (cyclic openness), P is EarnedPath PERT viability (path accessibility), and F is future-map convergence (intergenerational integrity). Authorization requires PoR > θ, continuously evaluated.

All four factors measure **current condition**. They do not measure **regime of trajectory**. A system may present with:

- PoR above θ
- All four factors above their component thresholds
- Enforcement correctly anchored at the measurement point

while simultaneously having crossed into a regime from which subsequent collapse of one or more factors is inevitable. Enforcement at the measurement point is downstream of the critical transition.

### 1.2 What Is Asked

The pre-threshold problem asks: is there a **boundary condition** — structurally earlier than any of A, R, P, F crossing their thresholds — that detects the onset of irreversible path dependency?

This is not the same as tightening any existing threshold. A stricter θ detects degradation earlier; it does not detect regime transition. What is needed is a **different kind of measurement**: one based on trajectory topology rather than on current-state magnitude.

---

## 2. Dynamical Systems Grounding

### 2.1 Prior Art

The construct under discussion is well-studied across several literatures. DSAP-PRE does not invent it; DSAP-PRE specifies how ERES measures it within the Proof-of-Resonance framework.

- **Catastrophe theory** (Thom, 1972; Zeeman, 1977) formalizes discontinuous state transitions arising from smooth parameter changes. The fold catastrophe is the canonical regime-transition model: a smooth external parameter crosses a critical value, and the system state jumps discontinuously to a different basin of attraction.
- **Hysteresis in control theory** (Krasnosel'skii & Pokrovskii, 1989) formalizes path-dependent system behavior in which reversing the parameter change does not reverse the state change. Hysteresis loops quantify the asymmetry between degradation and recovery trajectories.
- **Tipping-point theory in ecology and climate science** (Scheffer et al., 2009; Lenton, 2011) provides empirical methodology for early-warning signals before critical transitions: rising variance, rising autocorrelation, critical slowing down.
- **Separatrices in multi-stable dynamical systems** (Strogatz, 2015) formalize the boundary between basins of attraction. Crossing a separatrix changes the set of reachable states. Downstream of separatrix crossing, the system may still read stable on current measurements, but the set of accessible trajectories has strictly decreased.

These literatures converge on a common observation: **systems approaching regime transitions exhibit identifiable precursor signatures before their state variables cross thresholds**. DSAP-PRE specifies three such signatures adapted to the ERES measurement stack.

### 2.2 Terminology Used Here

- **Basin of attraction**: the set of initial states from which trajectories converge to a given stable outcome.
- **Separatrix**: the boundary in state space between basins.
- **Regime transition**: the crossing of a separatrix. After transition, the previously accessible basin is no longer reachable without restorative intervention exceeding a characteristic cost.
- **Critical slowing down**: the phenomenon in which a system near a separatrix responds to perturbations with increasing recovery time, detectable before the transition itself.
- **Irreversibility**: the condition in which reversing the parameter change that drove the system toward transition does not restore the prior basin. Measurable via hysteresis counterfactual (Section 5).

---

## 3. Proxy One — RHC Derivative Analysis

### 3.1 Rationale

EAAP v1.3 Factor R measures the amplitude of the Resonant Harmony Cycle. Amplitude is a first-order quantity: it tells you how open the cycle is now. It does not tell you whether openness is *accelerating toward closure*.

Critical slowing down — the standard precursor in tipping-point theory — manifests in ERES measurement as an RHC cycle whose amplitude is not yet flatlined but whose rate of decline is itself accelerating. The second derivative of RHC amplitude carries the regime-transition signal before the first-order threshold is crossed.

### 3.2 Mathematical Form

Let A_RHC(t) denote the RHC amplitude time series. Define:

- First derivative: A'(t) = dA_RHC/dt
- Second derivative: A''(t) = d²A_RHC/dt²

The pre-threshold indicator **ρ_RHC** is:

**ρ_RHC(t) = 1** if (A'(t) < 0) and (A''(t) < -κ_RHC) sustained over window W_RHC
**ρ_RHC(t) = 0** otherwise

where:
- κ_RHC is the acceleration-toward-flatline threshold (domain-dependent; reference value to be determined by empirical calibration, Section 7)
- W_RHC is the sustaining window, default 3 RHC cycles

ρ_RHC = 1 signals that RHC amplitude is not merely declining but is declining at an accelerating rate, sustained across multiple cycles. This is the acceleration-toward-flatline condition.

### 3.3 Implementation Notes

- Estimation of A' and A'' requires numerical differentiation over the cycle history. A simple two-cycle finite difference is sufficient for initial implementation; Savitzky-Golay filtering or similar is recommended for noisy signals.
- ρ_RHC is intentionally binary at the math-sheet level. Continuous-valued versions are possible (for example, 1/(1 + |A''|/κ_RHC) for A'' < 0) and may be preferred in the full specification.
- ρ_RHC can fire while Factor R is still above its own threshold — that is the point. It provides pre-threshold warning.

---

## 4. Proxy Two — PERT Distribution Topology

### 4.1 Rationale

EAAP v1.3 Factor P measures the viability of alternative paths as a scalar derived from the EarnedPath PERT distribution. Scalar aggregation collapses topological information that is directly relevant to regime-transition detection.

A decision space with multiple genuinely accessible alternatives presents as a **multi-modal** PERT distribution — distinct peaks corresponding to distinct viable trajectories. A decision space converging to a single practically-unavoidable trajectory presents as a **unimodal** distribution with collapsing variance. The transition from multi-modal to unimodal is a separatrix-crossing signature visible in the distribution's topology while the scalar viability can still read above threshold.

### 4.2 Mathematical Form

Let D_PERT be the PERT distribution over alternative-path cost, estimated from the EarnedPath model at time t. Define three topological indicators:

- **Modality**: m(D_PERT) ∈ {1, 2, 3, ...} — the number of modes detected in the distribution. Detection via Hartigan's dip test or equivalent multimodality test with significance threshold α = 0.05.
- **Variance**: σ²(D_PERT) — the variance of the distribution, normalized against the current-path cost c_0 to produce a dimensionless σ̃² = σ²/c_0².
- **Viable-alternative count**: n_viable(D_PERT) — the count of alternatives in the distribution whose cost is below a viability threshold κ_cost × c_0, where κ_cost is the domain-dependent cost-ratio ceiling (for example, κ_cost = 3 treats alternatives up to 3× the current path cost as viable).

The pre-threshold indicator **ρ_PERT** is:

**ρ_PERT(t) = 1** if any of:
- m(D_PERT) has decreased from > 1 to 1 within the last W_PERT evaluations (modality collapse)
- σ̃²(D_PERT) has decreased by more than 50% within W_PERT evaluations (variance collapse)
- n_viable(D_PERT) has decreased by more than 50% within W_PERT evaluations (alternative-set collapse)

**ρ_PERT(t) = 0** otherwise.

Default W_PERT = 5 evaluations.

ρ_PERT = 1 signals that the path-distribution topology has shifted in a direction consistent with regime transition, independently of whether Factor P has crossed its threshold.

### 4.3 Implementation Notes

- Multimodality testing on small sample sizes (fewer than ~30 alternatives) is unreliable. Implementations with small alternative counts should rely primarily on variance and viable-count signals, using modality as a tertiary indicator.
- Variance should be computed on log-cost rather than raw cost when the cost distribution spans multiple orders of magnitude.
- The three OR-combined conditions are intentionally generous at the math-sheet level. The full specification may require two of three, or weighted combination; this is a calibration question, not a definitional one.

---

## 5. Proxy Three — Hysteresis Counterfactual

### 5.1 Rationale

The most direct test of regime transition is the hysteresis test from control theory: **if conditions were reversed, would the system recover?** In a multi-stable regime, yes. Past the separatrix, no — the system has entered a basin from which restoration requires intervention exceeding a characteristic cost that did not exist before.

This is the most expensive of the three proxies but also the most direct. It is the only proxy that tests irreversibility itself rather than precursors to it.

### 5.2 Mathematical Form

Let S(t) denote the current system state and Π(t) the current parameter vector driving the system toward convergence. Define a **restoration perturbation** Δ_Π: a reversal of Π toward values that would, in the multi-stable regime, restore accessibility of alternatives.

The hysteresis counterfactual evaluates:

**H(t) = Ψ(S(t), Π(t) + Δ_Π, τ) − Ψ(S(t), Π(t), τ)**

where:
- Ψ(S, Π, τ) is the projected PERT viability under parameter vector Π evaluated τ steps forward from state S
- τ is the hysteresis evaluation horizon, default 10 RHC cycles
- Δ_Π is the restoration perturbation, sized to reverse recent parameter movement by a specified fraction (default 0.5)

**H(t) > η_recover** indicates recovery is possible under restoration: the system is in a multi-stable regime.
**H(t) ≤ η_recover** indicates recovery is not projected under restoration: the system has crossed into a single-basin regime.

The pre-threshold indicator **ρ_hyst** is:

**ρ_hyst(t) = 1** if H(t) ≤ η_recover
**ρ_hyst(t) = 0** otherwise

where η_recover is the recovery threshold, reference value to be determined by calibration.

### 5.3 Implementation Notes

- The counterfactual requires a forward projection model (Ψ) that can be evaluated under perturbed parameters. In ERES this is the EarnedPath projection with the perturbation applied.
- Computational cost is dominated by the τ-step projection. For initial implementations, τ = 5 is acceptable; longer horizons improve detection sensitivity.
- The restoration perturbation Δ_Π must be a realistic reversal, not a maximally favorable one. A perturbation that trivially restores any system by hypothesis fails to distinguish regimes.
- Hysteresis testing can be evaluated less frequently than ρ_RHC and ρ_PERT due to its cost. A cadence of every fifth RHC cycle is a reasonable starting point.

---

## 6. DSAP-PRE Composite Indicator

### 6.1 Composition

The three proxies combine into the DSAP-PRE composite:

**DSAP-PRE(t) = (1 − ρ_RHC(t)) × (1 − ρ_PERT(t)) × (1 − ρ_hyst(t))**

DSAP-PRE is in [0, 1]. It equals 1 when none of the three pre-threshold conditions are firing and equals 0 if any one fires.

### 6.2 Relationship to PoR

DSAP-PRE is evaluated **alongside and before** PoR. Two integration modes are proposed; selection is a specification-level decision:

**Mode A — Gating precondition.** Authorization requires DSAP-PRE = 1 as a precondition to PoR evaluation. If DSAP-PRE = 0, authorization is refused regardless of PoR value.

**Mode B — Joint conjunctive product.** Authorization requires DSAP-PRE × PoR > θ_joint, where θ_joint is a joint threshold higher than θ alone. Under this mode DSAP-PRE can partially compensate for fluctuations in PoR and vice versa, subject to the joint threshold.

Mode A is stricter and more consistent with the conjunctive-product design philosophy of PoR itself. Mode B is more permissive but allows graceful degradation. Recommendation: **Mode A** for authorization decisions in high-consequence domains (governance, safety-critical infrastructure, legal authority); **Mode B** for advisory or lower-consequence domains.

### 6.3 Continuous-Valued Alternative

The binary formulation of ρ_RHC, ρ_PERT, ρ_hyst given in Sections 3–5 is appropriate for a math sheet and for initial implementation. A continuous-valued alternative defines each ρ on [0, 1] as a soft indicator of how firmly the pre-threshold condition is met, and combines them as a conjunctive product consistent with PoR's structure:

**DSAP-PRE_continuous(t) = R_soft(t) × P_soft(t) × H_soft(t)**

where R_soft, P_soft, H_soft are continuous-valued analogs of (1 − ρ_RHC), (1 − ρ_PERT), (1 − ρ_hyst) respectively. The full specification will choose between binary and continuous formulations; this math sheet supports both.

---

## 7. Calibration and Reference Values

Every threshold named in this document (κ_RHC, W_RHC, κ_cost, W_PERT, τ, Δ_Π, η_recover, θ_joint) is stated with a placeholder or default value only. Reference values for representative domains are an open calibration question, not a definitional one.

Calibration requires either:
- Empirical data from deployed ERES instances exhibiting regime transitions, or
- Simulation studies on reference systems with known separatrix structure (the canonical tipping-point models from ecology and climate science are suitable), or
- Analytic derivation from assumed dynamical properties of the target domain.

The full DSAP-PRE specification will include reference values for at least three representative domains (governance, infrastructure, high-frequency authorization) derived from one or more of these methods.

---

## 8. Integration With EAAP v1.3

### 8.1 Stack Placement

```
Input
  ↓
[BODY Consolidation]         ← admission
  ↓
[BRAINS Trifecta]            ← execution gate
  ↓
[DSAP-PRE evaluation]        ← pre-threshold boundary (THIS WORK)
  ↓
[EAAP Qualification / PoR]   ← qualification and correlation
  ↓
[GraceChain commit]          ← record with MIEVM concurrence
  ↓
Authorized action
```

DSAP-PRE sits between BRAINS Trifecta clearance and EAAP qualification. A system that fails DSAP-PRE does not proceed to PoR evaluation; the authorization request is refused on regime-transition grounds.

### 8.2 Relation to EAAP v1.3 Section 8 Gaps

EAAP v1.3-DRAFT Section 8 names the runtime containment layer as an open specification requirement. DSAP-PRE is a **separate** open specification requirement, addressing pre-threshold regime detection rather than runtime containment. Both are open; they are not substitutes for each other.

The v1.3-FINAL text should extend Section 8 to name DSAP-PRE explicitly as a companion specification under development, with reference to this math sheet as the current state of the work.

---

## 9. Known Limitations

### 9.1 False Positives

All three proxies can fire under conditions that do not reflect regime transition:

- ρ_RHC can fire during normal system adjustment to parameter changes that are not driving toward transition.
- ρ_PERT can fire when the alternative set is legitimately consolidating around a correct choice, not irreversibly foreclosing.
- ρ_hyst can fire when the forward projection model Ψ is itself poorly calibrated.

Calibration (Section 7) reduces but does not eliminate false-positive rates. The specification-level decision of Mode A versus Mode B partially addresses this: Mode A's strict gating is appropriate only where false-positive refusals are tolerable; otherwise Mode B provides graceful degradation.

### 9.2 False Negatives

Conversely, all three proxies can fail to fire during genuine regime transitions:

- Abrupt transitions without critical slowing down produce low ρ_RHC signal.
- Regime transitions that preserve apparent multi-modality (for example, two alternatives that both lead to the same basin) produce low ρ_PERT signal.
- Hysteresis counterfactual with small Δ_Π may fail to detect regimes that require larger restoration perturbations than tested.

The three-proxy design mitigates single-proxy failure by requiring any one to fire, not all three. However, systems exhibiting none of the three signatures can still undergo regime transition; DSAP-PRE is a defense in depth, not a guarantee.

### 9.3 Computational Cost

The hysteresis counterfactual (ρ_hyst) is significantly more expensive than the other two proxies. Implementations operating under strict latency budgets may need to evaluate ρ_hyst less frequently than every cycle, accepting temporal lag in detection.

### 9.4 Specification Gap

This math sheet specifies the three proxies at a level sufficient for implementation and refinement. It does not:
- Provide byte-normative test vectors (required for specification-grade publication).
- Calibrate reference values for specific domains.
- Resolve the Mode A versus Mode B selection for specific authorization contexts.
- Prove optimality or completeness of the three-proxy set.

All of these are legitimate extensions for the full DSAP-PRE specification.

---

## 10. Peer Review Lineage

This math sheet incorporates peer review contribution from **Reviewer A (LinkedIn correspondence, April 22–23, 2026)** per the ERES Attribution Protocol. The pre-threshold problem was identified and sharpened across multiple correspondence turns by Reviewer A, who distinguished:

- Measurement of degradation (what EAAP v1.3 PoR currently measures) from detection of irreversibility-onset (what DSAP-PRE addresses).
- Presence of deliberation signals from preservation of decision space.
- Diversity of signals from viability of alternative paths.

The three-proxy decomposition (RHC derivative, PERT topology, hysteresis counterfactual) is ERES Institute work developed in response to Reviewer A's sharpening. The dynamical-systems grounding (Section 2) is standard prior art from the cited literatures and is not original to this sheet.

Reviewer A has not been independently verified or named per the Attribution Protocol and has not yet reviewed this math sheet. Named attribution will be added upon reviewer request and ERES Institute confirmation.

---

## 11. Next Steps

1. **Peer review of this math sheet** by Reviewer A and, in due course, by the MIEVM ensemble.
2. **Refinement** in response to peer review, particularly on whether the three proxies are sufficient or whether additional signatures (autocorrelation, spectral shifts, flicker) from the tipping-point literature should be incorporated.
3. **Calibration** of reference values for representative domains.
4. **Promotion to DRAFT specification** (ERES-DSAP-PRE-SPEC-2026-001-DRAFT) once the math sheet stabilizes.
5. **Integration into EAAP v1.3-FINAL Section 8** as a named companion specification.
6. **Full publication** as a ResearchGate working paper (anticipated RG#410 in sequence).

---

## 12. References

### Dynamical Systems Grounding

- Krasnosel'skii, M. A., & Pokrovskii, A. V. (1989). *Systems with hysteresis*. Springer-Verlag.
- Lenton, T. M. (2011). Early warning of climate tipping points. *Nature Climate Change*, 1(4), 201–209.
- Scheffer, M., Bascompte, J., Brock, W. A., Brovkin, V., Carpenter, S. R., Dakos, V., Held, H., van Nes, E. H., Rietkerk, M., & Sugihara, G. (2009). Early-warning signals for critical transitions. *Nature*, 461(7260), 53–59.
- Strogatz, S. H. (2015). *Nonlinear dynamics and chaos: With applications to physics, biology, chemistry, and engineering* (2nd ed.). Westview Press.
- Thom, R. (1972). *Stabilité structurelle et morphogenèse*. W. A. Benjamin.
- Zeeman, E. C. (1977). *Catastrophe theory: Selected papers, 1972–1977*. Addison-Wesley.

### ERES Specifications

- ERES-EAAP-STD-2026-001-v1.3-DRAFT — EAAP v1.3 Draft.
- ERES-GRACECHAIN-NOTES-2026-001-v1 — GraceChain Ledger Notes.
- ERES-ATTRIBUTION-PROTOCOL-2026-001-v1 — ERES Attribution Protocol.
- ERES-RECKON-WP-2026-002 — Seven Resonance Anchors.
- ERES-BRAINS-SPEC-2026-001 — BRAINS Trifecta Protocol.
- ERES-BODY-SPEC-2026-001 — BODY Consolidation Pipeline.

### Statistical Methods

- Hartigan, J. A., & Hartigan, P. M. (1985). The dip test of unimodality. *The Annals of Statistics*, 13(1), 70–84.
- Savitzky, A., & Golay, M. J. E. (1964). Smoothing and differentiation of data by simplified least squares procedures. *Analytical Chemistry*, 36(8), 1627–1639.

---

**Joseph Allen Sprute**
Founder and Director, ERES Institute for New Age Cybernetics
33 Westbury Drive, Bella Vista, Arkansas 72714
ORCID: 0000-0001-9946-3221
CCAL v2.1

*Don't hurt yourself. Don't hurt others. Build for generations to come.*
