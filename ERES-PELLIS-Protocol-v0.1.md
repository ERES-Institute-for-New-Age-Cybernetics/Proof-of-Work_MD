# ERES–PELLIS Protocol v0.1

**A cross-domain test of collapse dynamics: physiological coherence breakdown vs. spectral collapse**

Joseph A. Sprute — ERES Institute for New Age Cybernetics
In correspondence with Stergios Pellis, University of Ioannina
Date: 2026-06-08 · Status: Draft for review (pre-registration to follow)

---

## Purpose

This protocol tests whether physiological coherence breakdown under increasing parametric stress shares the same *functional form* of an approach-to-threshold disruption index, D(t), as spectral collapse in magnetically confined fusion plasmas. Whether the correspondence is **shared functional form** (analogy) or **shared structure** (isomorphism) is precisely what the protocol is designed to discriminate — it is not assumed in advance.

The design is deliberately written in standard psychophysiology and time-series terms so that it can be read, criticized, and run by any working researcher without adopting any framework-specific vocabulary.

---

## Hypothesis (under test, not asserted)

As parametric stress increases, cross-channel physiological coherence will approach a critical threshold whose approach curve, D(t) → D_c, resembles the functional form of spectral collapse in the fusion framework. The protocol discriminates between two readings of any such resemblance:

- **Analogy** — shared functional form across domains (a hypothesis class).
- **Isomorphism** — the same mathematical structure instantiated in a different substrate (a stronger identity claim).

The protocol does not presume which holds; it is built to tell them apart.

---

## Observables

- **Cross-channel coherence:** magnitude-squared coherence, gamma-squared(f), computed across four channels — HRV, respiration, EDA, and VOC. Bounded [0, 1], dimensionless.
- **Discriminability measure:** A/B classification accuracy (silence vs. pink noise) from the coherence pattern. Chance = 50%.
- **Channel-independence measure:** cross-channel mutual information. Rises as channels lose independence (mode coalescence); floor is statistical independence.

### Channel notes

- **HRV** (heart rate variability) — cardiac, beat-to-beat timing variation; ECG or PPG.
- **Respiration** — respiratory rate and depth; respiration belt. Coupled to HRV via respiratory sinus arrhythmia.
- **EDA** (electrodermal activity) — sudomotor; skin conductance, a direct sympathetic-arousal readout.
- **VOC** (volatile organic compounds) — metabolic; gas-phase emissions. *Treated as exploratory:* slower and less standardized than the other three. The core falsification rests on HRV + respiration + EDA; VOC is added as a fourth channel once the three-channel version is established.

---

## Pre-specified falsification

The hypothesis fails if **either** of the following holds:

1. **Joint coherence does not beat the best single channel.** The joint-channel coherence classifier must outperform the best-performing single channel in predicting condition (p < 0.05). If a single channel does as well or better, cross-channel coherence carries no additional information and the resonance claim is falsified.
2. **The decay is linear, not critical.** If A/B classification accuracy declines smoothly and linearly as stress rises — rather than showing a threshold-like (critical) drop — the result is consistent with ordinary physiological saturation, not a critical transition, and the specific universality claim fails.

Both conditions are committed to before any data are collected.

---

## Null model

Phase-randomized surrogate data preserving marginal statistics (standard surrogates). The full classification is re-run on surrogate data; the real result counts only if it beats the surrogate. Additional baselines (e.g., standard nonlinear stochastic models without critical transitions) follow after the first n=1 run.

---

## Grounding of the measures

Every reported number bottoms out in something that requires no interpretation:

- **Logged labels** — the stimulus condition (silence vs. pink noise) is known and recorded at all times; this is the ground truth.
- **Chance baseline** — 50% for two conditions = the zero-information reference for classification accuracy.
- **Held-out testing** — the classifier is trained on one portion of data and tested on a held-out portion; same-data testing is excluded.
- **Surrogate nulls** — phase-randomized comparison separates real structure from artifact.
- **Single-channel benchmark** — the joint classifier must beat the best individual channel.

For mutual information, the zero point is statistical independence (a mathematical floor, not an assigned value); rising MI is measured against that floor.

---

## Measurement vs. rating (a note on interpretation)

The classification gate measures one thing only: whether two states remain distinguishable, and how fast that is changing. It is **valence-free** — it does not encode whether a closing gap is good or bad. Any such meaning belongs to a separate rating layer and is set by direction of travel:

- Approaching a collapse threshold → a closing gap is an **alarm**.
- Approaching a target condition → the same closing gap is **progress**.

The same notation and the same measured number serve both readings without conflict, because the gate measures and the rating interprets. This separation is deliberate and is part of what keeps the measurement trustworthy independent of any goal.

---

## Design

- **Subject:** n=1 intensive (repeated-measures), then replicate.
- **Stressor:** pink noise, 40 → 90 dB in 5 dB steps.
- **Blocks:** 5-minute blocks per step.
- **Per-step computation:** coherence entropy, A/B classification accuracy, cross-channel mutual information.
- **Threshold:** identify D_c, the step at which classification accuracy drops abruptly toward chance.
- **Pre-registration:** OSF or AsPredicted, before any data collection.

---

## Sequence

pre-register → run n=1 → compare observed decay to predicted form → refine or reject → replicate

---

## Methodological points carried from review

- **Stimulus ≠ driver.** Acoustic stress is treated as a stimulus whose coupling to the internal stress parameter is itself an open question — not assumed to scale linearly with the relevant internal variable.
- **Saturation vs. collapse.** The surrogate comparison and the linear-decay failure condition exist precisely to separate ordinary physiological saturation from a genuine critical transition.

---

## What this protocol does not claim

- It does not claim coherence indexes a feeling, emotion, personality type, or compatibility.
- It does not claim the fusion operator is literally the physiological coherence operator.
- It does not claim validation. This is a hypothesis to be tested, not a finding.

---

*Terms here map to an internal ERES lexicon; the mapping is available on request but nothing in the science depends on it. No data collected. No claims made. Protocol available for pre-registration.*
