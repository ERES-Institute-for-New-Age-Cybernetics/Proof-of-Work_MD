# ERES–PELLIS Protocol — BERA Measurement Specification v0.2.1

**For:** Stergios Pellis (University of Ioannina)
**From:** Joseph A. Sprute, ERES Institute for New Age Cybernetics
**Date:** 10 June 2026
**Status:** DRAFT for peer review — supersedes Protocol v0.1 (8 June 2026), incorporates your v1.1 review (8 June) and *Spectral Phase Transitions in Protein Folding Dynamics* (Pellis, 10 June 2026; "Pellis 2026b")
**Changelog (v0.2 → v0.2.1):** adds §3.0 Notation lock (single-valued symbols; φ pinned to the number; resonance defined as a state, never a standing). One constraint added, none removed.

---

## 0. Scope, and what this document is *not*

This is a measurement specification, not a claim of result. Two framing commitments carry through every section, both adopted directly from your v1.1 review:

1. **D(t) is a measurement hypothesis, not a validated invariant.** Nothing below asserts that the physiological disruption index is a physical invariant. The protocol exists to establish — or fail to establish — its empirical identifiability first, before any cross-domain interpretation.

2. **The ERES↔Pellis correspondence is a structural-similarity hypothesis class, to be tested under explicit falsification — not a claim of shared mechanism.** The protocol is built to *discriminate* between two outcomes you named: genuine cross-condition universality (isomorphism) versus domain-specific but structurally similar early-warning behaviour (analogy). Both are scientifically meaningful; the protocol does not presuppose which obtains.

A note on rendering, repeated from the v0.1 cover so it stays explicit: the source work is generated in a dense internal framework and translated into the standard terms used here. The standard terms are the load-bearing version. Nothing in the science below depends on the internal framework, and no part of it is required to run, evaluate, or falsify this protocol.

---

## 1. Three-layer architecture (modular separation)

Per your §4 observation that the system spans three distinct layers, v0.2 presents them as **formally separated modules** with a single, explicitly specified interface. Each layer is independently evaluable; the empirical core (Layer 2) can be assessed without committing to Layer 3.

**Layer 1 — Signal.** Acquisition and conditioning of four channels (HRV, respiration, EDA, VOC) into a baseline-referenced coherence time series C(t). No inference, no thresholds.

**Layer 2 — Dynamical inference (the minimal testable core).** Construction of D(t) from C(t); onset detection; discrimination of critical versus non-critical decay. **This layer is the minimal testable core you asked us to isolate.** It is self-contained: it can be pre-registered, run, and falsified on its own terms, with the correspondence hypothesis (§2) bolted on only afterward.

**Layer 3 — Governance / gate layer.** The discrete A–D constraint rules. Per your §3, these are invariant constraint rules in a governance layer, *not* dynamical observables, and are kept strictly out of the measurement path.

### 1.1 Interface mapping (Layer 2 ↔ Layer 3)

You asked (§3, close) for an explicit interface between the dynamical state variables and the gate logic, noting they currently run in parallel but not coupled. v0.2 specifies the interface as **read-only and one-directional**:

```
Layer 2  ──(emits: threshold-crossing events of D(t), with timestamps)──▶  Layer 3
Layer 3  ──(emits: nothing back into Layer 2)
```

Gates consume *events* derived from D(t) (e.g., "D(t) crossed D_c at t*"); gates never feed back into the computation of C(t) or D(t). This preserves the separation you flagged: continuous state evolution and discrete constraint satisfaction remain decoupled, and no gate decision can contaminate the measurement it is reading. The gate layer is therefore **out of scope for the empirical validation** of the minimal testable core and is documented separately.

---

## 2. The correspondence, made concrete against Pellis (2026b)

Your protein-folding paper supplies the collapse referent that v0.1 lacked. The bridge below is stated in your notation so it is legible on your side. **Every row is tagged HYPOTHESIZED.** The table is the object under test, not a result.

| BERA (physiological) | Pellis 2026b (spectral) | Status |
|---|---|---|
| Coherence C(t), baseline C₀ | Spectral gap Δλ(t) = λ₁(t) − λ₀(t), baseline Δλ₀ | HYPOTHESIZED correspondence |
| Disruption index D(t) = [C₀ − C(t)] / C₀ | Normalized gap closure 1 − Δλ(t)/Δλ₀ (cf. your precursor index P(t) = Δλ₀/Δλ(t)) | HYPOTHESIZED |
| Acoustic stress level (dB) | Stress-controlled deformation parameter g(t) | HYPOTHESIZED, coupling **not** assumed linear |
| Critical (threshold-like) decay of D(t) | Critical scaling Δλ(t) ∼ (t_c − t)^ν | HYPOTHESIZED — this is the discriminandum |
| Cross-channel coherence (4 channels) | Cascade synchronization across scales (your Prediction V) | HYPOTHESIZED |

**The isomorphism test, stated precisely.** Your Prediction II asserts a universal critical exponent γ (equivalently ν) invariant across collapse classes. The correspondence is *isomorphic* only if the physiological gap-closure exponent ν_phys is statistically indistinguishable from your predicted critical exponent. It is *analogy only* if D(t) declines under stress but with an exponent, or a functional form, inconsistent with critical scaling (e.g., linear saturation). The protocol is designed to return one of these two verdicts, not to confirm the first.

### 2.1 φ firewall (load-bearing)

The φ-specific scaling from your first paper (*Multiscale Spectral-Fractal Analysis*, 2026a) is **excluded from the minimal testable core by construction.** The physiological result must be statable, testable, and falsifiable *whether or not* the scaling constant turns out to be φ, some other irrational, or no clean constant. φ-specificity enters only as a **separate, downstream sub-hypothesis** tested *after* gap-closure correspondence is established, never before. Rationale: the critical-exponent claim and the φ-constant claim are independent, and binding them would expose the empirical result to the well-documented golden-ratio confirmation-bias critique (Liu & Sumpter 2018) for no scientific gain.

---

## 3. Observables (operational definitions)

### 3.0 Notation lock (single-valued symbols)

In this specification each symbol is single-valued. **C(t)** is calculated coherence; **D(t)** is the disruption index [C₀ − C(t)] / C₀; **φ** is the root of x² = x + 1 and carries no meaning beyond the number. Alternate readings (D~Day, t~Reality-time, C~Cybernetic-Time, φ~interpretive gloss) are author's-framework annotations, non-binding on any equation and never used to gate or price a person. **Resonance** denotes a measurable energetic state of a person — a state, never a standing; it may contextualize pacing but never determines permission.

- **Cross-channel magnitude-squared coherence** γ²(f) across {HRV, respiration, EDA, VOC}; bounded [0,1], dimensionless. C(t) is the windowed aggregate of γ²(f) over the analysis band.
- **A/B classification accuracy** (silence vs. pink noise) — the discriminability measure.
- **Cross-channel mutual information** — the channel-independence measure (guards against trivial coherence from a shared artifact).
- **D(t) = [C₀ − C(t)] / C₀** — normalized coherence-loss functional, bounded [0,1] (your v1.1 canonical form).
- **Onset** — first time the smoothed dD/dt and rising lag-1 autocorrelation jointly satisfy the pre-registered onset condition (critical-slowing-down signature).

---

## 4. Minimal testable core — empirical identifiability first

Per your §2 ("provided that the empirical identifiability of D(t) is established first") and §5, the first executable question is **not** the cross-domain correspondence. It is:

> **Q0 (identifiability):** Is D(t) a reliable, reproducible quantity in n=1 data at all — stable baseline, reproducible onset, low test–retest variance across repeated blocks — *before* any claim about its decay form?

Only if Q0 passes does the protocol proceed to Q1 (decay-form discrimination) and Q2 (correspondence). This ordering makes the empirical component evaluable independently of the architectural extensions, as you recommended.

---

## 5. Pre-registered falsification criteria

Registered on OSF or AsPredicted **before any data collection.** The hypothesis fails if **any** of the following holds:

- **F1 (joint-channel necessity).** Joint-channel coherence does **not** outperform the best single channel in predicting condition (p < 0.05). If a single channel suffices, the multi-channel coherence claim is unsupported.
- **F2 (critical vs linear).** The accuracy-decay / D(t) curve is statistically consistent with **linear saturation** and inconsistent with critical (threshold-like) scaling, by the model-comparison test in §7. Ordinary physiological saturation is the null to beat.
- **F3 (surrogate).** Observed collapse signatures are reproduced by phase-randomized surrogates (§6) — i.e., the effect is an artifact of marginal statistics or nonstationarity rather than genuine critical dynamics.
- **F4 (identifiability, gating).** Q0 fails: D(t) is not reproducible within-subject. If F4 fires, F1–F3 are not interpretable and the protocol halts at Layer 2.

**Isomorphism is additionally rejected** (downgraded to analogy) if D(t) decays critically but ν_phys is statistically distinguishable from your predicted critical exponent.

---

## 6. Null models and surrogate discipline

- **Primary null:** phase-randomized surrogate data preserving marginal statistics and the power spectrum (standard IAAFT/Theiler surrogates).
- **Secondary null:** block-shuffled surrogates, to separate genuine multiscale structure from within-block correlation.
- **Linear-saturation baseline:** an explicit non-critical decay model fit alongside the critical model (not merely "no effect").
- Additional baselines (including non-φ scaling baselines, per your "adversarial model comparison" requirement) added after n=1.

Caveat carried into design: extreme data loss from artifact removal can corrupt scaling estimates, and anti-correlated signals are especially fragile to it (Ma et al. 2010). Artifact-rejection fraction and segment-length distribution will be reported as pre-registered nuisance parameters, not silently applied.

---

## 7. Estimation discipline (this section also serves your Prediction II)

Your Prediction II states that experimental time series "should collapse onto a single linear manifold in log-log representation." That is the exact procedure Clauset, Shalizi & Newman (2009) show to be **systematically biased**: least-squares slope estimation on log-log axes produces wrong exponents and gives no indication of whether a power law holds at all. v0.2 therefore specifies, for **both** the physiological exponent and any comparison to your spectral exponent:

1. **Maximum-likelihood estimation** of the scaling exponent with bootstrap confidence intervals — not least-squares on log-log axes.
2. **Goodness-of-fit** by Kolmogorov–Smirnov distance against the fitted critical model.
3. **Likelihood-ratio comparison** of the critical-scaling model against explicit alternatives: linear/saturating, exponential, and (post n=1) non-φ power laws. A critical exponent is reported only if it survives this comparison.

This is offered as a shared standard: applying it to your Prediction II as well would harden the universality claim against the standard reviewer objection.

---

## 8. Design

- **n=1 intensive**, pink noise stepped **40 → 90 dB in 5 dB steps**, **5-minute blocks** per step, A-B blocking (silence vs. noise).
- Acoustic stress treated as a **stimulus whose coupling to the internal stress parameter g(t) is itself a question** — not assumed linear (your §2 point, built in).
- **Power note (honest):** controlled-exposure studies put autonomic responses to noise at roughly 1–2% change in HRV indices per dB (e.g., RECORD MultiSensor Study 2017). Effects are small and recovery-laden. The detectable signal therefore depends on block count, baseline stability, and step size, not on effect existence. Block count will be set by a pre-registered power analysis against the smallest exponent-discriminating effect, not by convenience.
- **Continuity is not cosmetic:** continuous vs. intermittent acoustic delivery changes the autonomic response (multimodal evidence, 2025), so noise delivery within each block is specified as continuous and reported as such.

---

## 9. MIEVM evaluation layer (reproducible *and* refusal-capable)

Per your "adversarial validation and falsification layer" and "non-circular validation constraint," the MIEVM pass on Pellis 2026b outputs and on BERA outputs is governed by a spec with both properties below. A method that a stranger can run but that always agrees with its author is reproducible *and* a mirror; both columns are required.

**Reproducible (a third party can run it):**
- Fixed instrument set (named models, frozen versions).
- A **written culling predicate** — the criterion that adds or drops an instrument, computable by someone who is not the author (no "the ensemble I convene").
- Fixed elicitation (prompts, seeds).
- Deterministic aggregation (N verdicts → one verdict; no casting vote).
- No-consensus default: **VEILED → HOLD**, never VEILED → PASS. An undefined or unresolved verdict holds the gate shut; it never opens it.

**Refusal-capable (it can return "no" to the author):**
- At least one documented case on record where MIEVM returned a negative verdict the author did not want. Without a documented refusal, the layer cannot be shown to be external rather than self-confirming.
- Convergence evidence from an independent re-implementation counts toward externality only where that party could have diverged and did not.

**External validation is structural.** Of the validation criteria, the one that code cannot satisfy for itself is external reproduction. MIEVM internal to the author's ensemble is governance commentary; the load-bearing external check requires a third party — which is precisely the role this collaboration occupies.

---

## 10. Sequence and gates to advance

```
Pre-register (OSF/AsPredicted)
      │
      ▼
Q0  identifiability of D(t)        ──fail (F4)──▶  halt at Layer 2; revise acquisition
      │ pass
      ▼
Q1  critical vs linear decay       ──fail (F2/F3)─▶  hypothesis rejected; report analogy/null
      │ critical
      ▼
Q2  correspondence: ν_phys vs ν_Pellis
      ├── indistinguishable ──▶  isomorphism-class evidence (still provisional)
      └── distinguishable    ──▶  analogy-class result (still meaningful)
      │
      ▼
Replicate beyond n=1; additional baselines; MIEVM pass
```

No step advances on the author's judgment that it is ready. Q2 in particular requires your independent evaluation of the exponent comparison; it is not a verdict the author can issue alone.

---

## 11. Explicit non-claims (limitations stated up front)

- No claim that D(t) is a physical invariant.
- No claim of shared mechanism between physiological coherence and spectral collapse — only a structural-similarity hypothesis under test.
- No claim that the scaling constant is φ; the core result is φ-independent by construction (§2.1).
- No claim of predictive clinical utility. The early-warning-signal literature in human time series has a weak predictive track record (e.g., the 2024 critique in *Nature Reviews Psychology*); D(t) is framed as a falsifiable measurement hypothesis, not a predictor.
- n=1 results are existence/identifiability evidence only; universality claims require replication.

---

## 12. What is deferred (and stays deferred)

The author's internal framework contains an access/egress architecture, a semiotic surface model, and longer-horizon design layers (the v0.3–v0.5 roadmap). **None of these are part of this protocol, and none are required to evaluate it.** They are noted here only so their absence is deliberate rather than accidental: this document is the externally falsifiable subset, and it is meant to be runnable by a physicist, programmer, or psychophysiologist without adopting any of it.

---

*Prepared for review. The author will write the full OSF/AsPredicted pre-registration draft from this specification and submit it for your review before any data are collected.*
