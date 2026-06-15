# ERES–PELLIS Corpus: Version Definition
## Define Before Publishing

**Author:** Joseph A. Sprute (ERES Maestro)
**ORCID:** 0000-0001-9946-3221
**Date:** June 14, 2026
**Document ID:** ERES-VERSION-2026-001
**Status:** DEFINITION — to be locked before Zenodo deposit
**License:** CCAL v2.1

---

## What This Document Does

This document defines, precisely and in advance, what **v1.0** of the ERES–PELLIS corpus contains, what it does NOT contain, and what gates must be passed before any subsequent version may be published. It is a pre-publication version contract — the equivalent of a pre-registration, but for the corpus itself.

Nothing in this corpus is published until this definition is signed off by the author (JAS).

---

## Version: v1.0 — Q3 2026

### Version label
**ERES–PELLIS Corpus v1.0 — Protocol + Artifacts (June 14, 2026)**

### Zenodo DOI structure
- **Concept DOI (permanent, always points to latest):** 10.5281/zenodo.20010116
- **This version DOI (v1.0):** to be assigned at time of deposit
- **Living Archive DOI (superseding draft):** 10.5281/zenodo.20583261

---

## What v1.0 CONTAINS

The following artifacts are locked into v1.0. No artifact in this list may be modified after deposit.

### Tier 1 — Protocol documents (external-facing, Pellis-ready)

| Document | Version | Status |
|---|---|---|
| ERES-PELLIS Protocol | v0.2.1 | FINAL for this corpus version |
| ERES-BERA-2026-001 Indices Spec | v1.1 (D(t) gates + D(t) locked) | FINAL |
| ERES-RESONANCE-PROTOCOL-2026-001 | v1.0 | FINAL |
| Technical Simulation Specification for Pellis/UoI | v1.0 (June 14, 2026) | FINAL |
| ERES–PELLIS As-Is/Bridge/To-Be Analysis | v0.3 (Pellis-facing, stripped of ERES-JAS internal layer) | FINAL |

### Tier 2 — Analysis instruments (executable)

| Artifact | Version | Status |
|---|---|---|
| ERES_PELLIS_Q0_Q1_Q2_analysis_stub.py | v1.1 (filled stubs: coherence, bootstrap CI, surrogate test) | FINAL |
| PSCI-hat specification | v1.0 (Use.ai Pellis-aligned variant; weights w = (0.25, 0.35, 0.15, 0.25)) | FINAL |
| Q1 preregistration text (critical vs. linear, WAIC ≥ 4 decision rule) | v1.0 | FINAL |
| Q2 preregistration text (ε_eq = 0.10, blind equivalence test) | v1.0 | FINAL |

### Tier 3 — Governance and transparency artifacts

| Artifact | Version | Status |
|---|---|---|
| ERES Advance Danger Notice (ADN_LLM_2.md) | June 14, 2026 | FINAL (MIEVM record complete: Claude + DeepSeek + Grok + Use.ai) |
| Science_FAIR Assessment and Draft | June 14, 2026 | FINAL |
| Negative result paper template | v1.0 | FINAL (pre-written; fill brackets only if H2 fails) |
| Pre-registration template (OSF/AsPredicted format) | v1.0 | FINAL |

### Tier 4 — Correspondence templates (outbound, not yet sent)

| Artifact | Status |
|---|---|
| Cover email to Stergios Pellis (sterpellis@gmail.com) re: simulation request | READY — not sent until simulation specification confirmed |
| Q2 evaluation request email | READY — not sent until H1/H2/H4 pass |
| 30-day follow-up email | READY |

---

## What v1.0 does NOT CONTAIN

The following are explicitly excluded from v1.0. Their absence is deliberate, not accidental.

| Excluded item | Reason |
|---|---|
| Human physiological data (D(t), C(t) time series) | Not yet collected. Inclusion would require Q0 to have passed. |
| Simulation output (gap closure → coherence monotonicity) | Not yet run. Requires Pellis/UoI or Google Colab execution. |
| ν_phys estimate | Not yet computed. Requires human data + analysis stub execution. |
| ν_Pellis reference value | Must be extracted from Pellis 2026 §16, Table 2 — not yet inserted. |
| OSF/AsPredicted registration ID | Not yet registered. Must be obtained before data collection. |
| Q2 verdict (PASS/FAIL) | Not yet issued. Cannot be self-issued per Protocol §12. |
| MIEVM Refusal Record (formal deposited artifact) | Not yet created as a standalone deposited document. Exists implicitly in ADN_LLM_2 but must be extracted and deposited formally before any isomorphism claim. |
| MyWay_Final / ERES-JAS internal framework materials | Intentionally excluded from external-facing deposit. Internal use only. |

---

## What Must Happen Before v2.0 (Q4 2026)

v2.0 is the RESULTS version. It is published only when:

| Gate | Criterion | Authority |
|---|---|---|
| Simulation pre-test | S1 (ρ > 0.90), S2 (ν_est within ε_eq), S3 (surrogate p < 0.01) all pass | Pellis/UoI or independent physicist — NOT the author |
| OSF pre-registration | Registered with ID, before data collection | OSF/AsPredicted |
| Q0 identifiability | CV < 10% across 3 baselines | Analysis stub output |
| Q1 critical decay | ΔWAIC ≥ 4, surrogate firewall clear | Analysis stub output |
| Q2 exponent correspondence | ε_eq = 0.10; issued by Pellis or independent analyst | NOT self-issued |

If simulation pre-test FAILS → v2.0 contains the negative simulation result + proxy revision plan. Human data is NOT collected until simulation passes.

If human protocol H2 FAILS → v2.0 contains the pre-written negative result paper (fill brackets only). No H3/Q2 evaluation is requested.

---

## Controlled Vocabulary (binding in all v1.0 documents)

The following single-valued term assignments apply across all artifacts in this corpus. No term may carry dual meanings.

| Symbol | Canonical term | Retired aliases |
|---|---|---|
| L̂(t) | Operator | generator, flow-operator |
| ψ(t) | State trajectory | signal-state, wavefunction |
| σ(L̂) | Spectrum | eigen-structure, modal set |
| V(ψ) = inf Re(λ) | Stability functional | least-mode real-part, spectral floor |
| M_c = {ψ \| V(ψ)=0} | Critical manifold | collapse boundary, tipping surface |
| C(t) | Cross-channel coherence | synchrony, coupling |
| D(t) = [C0−C(t)]/C0 | Disruption index | normalized coherence loss, gap proxy |
| PSCI-hat | Spectral collapse index (surrogate) | PSCI surrogate, collapse score |
| Q0 | Identifiability gate | reproducibility check |
| Q1 | Decay-form gate | scaling test |
| Q2 | Exponent correspondence gate | universality check |
| ε_eq | Equivalence margin | tolerance band |
| HYPOTHESIZED / PASSED / FAILED / INCONCLUSIVE | Status tiers | provisional, tentative, mixed |

**Resonance** = measurable energetic state (never a standing)
**D(t)** ≠ "gap proxy" in external prose (it is the disruption index; the gap is Δλ)
**φ firewall** = maintained per Protocol §2.1; φ-specificity excluded from minimal testable core

---

## MIEVM Rating Summary (v1.0 basis)

The following ratings form the consensus basis for the five identified gaps:

| LLM | Document rated | Score | Key finding |
|---|---|---|---|
| Claude | As-Is/Bridge/To-Be | — | Bridge asserted not argued; Q2 undefined; confound firebreak missing |
| DeepSeek | As-Is/Bridge/To-Be | B+ | Architecturally complete, empirically unbuilt; bridge not yet crossable |
| Grok | As-Is/Bridge/To-Be | 7.8/10 | Esoteric overlays risk external credibility; strong internally |
| Use.ai | As-Is/Bridge/To-Be | 8/10 → 10/10 definition | Toy simulation + pinned PSCI-hat + locked Q1/Q2 rules = path to 10 |
| Grok | Science_FAIR draft | 7.9/10 | Storm Party framing risks undermining scientific core for external audiences |
| Claude | ADN + Science_FAIR draft | 7.8/10 | Strong self-diagnostic; rigor uneven on ε_eq and simulation spec |

**Consensus:** Architecture sound. Five specific gaps must close before any external submission or claim of isomorphism.

---

## MIEVM Share Links (v1.0 record)

- Claude: https://claude.ai/share/f2c5903f-8954-4768-9760-269040b69ee3
- DeepSeek: https://chat.deepseek.com/share/nwerfbmwymvsw3oczs
- Grok: https://grok.com/share/bGVnYWN5_41b8c4c8-1013-430c-985e-0f7cec0e80d3
- Use.ai: https://use.ai/share/c8be2843-66b9-4be0-8172-14b22a7f5dae

---

## Five Gaps Requiring Resolution Before v2.0

These are the load-bearing items from the ADN. All five must be resolved or formally acknowledged before v2.0 is published.

| # | Gap | Resolution path | Target version |
|---|---|---|---|
| E1 | Coherence→gap bridge asserted, not argued | Pellis/UoI simulation (S1–S3 criteria) | Before v2.0 |
| E2 | Q2 equivalence margin undefined | Pre-registered: ε_eq = 0.10, CI intersection criterion | v1.0 ✓ RESOLVED HERE |
| O1 | No confound firebreak | Pre-registration block: SNR_min, artifact-rejection %, respiration handling | Before human data collection |
| O2 | No MIEVM Refusal Record as standalone deposit | Extract from ADN_LLM_2, create formal record, deposit to Zenodo | Before any isomorphism claim |
| O3 | Terminology dual-use risk | Controlled vocabulary table (above) adopted as binding exhibit | v1.0 ✓ RESOLVED HERE |

**Note on E2:** The equivalence margin ε_eq = 0.10 is now pre-registered in this document. Q2 passes if the 95% bootstrap CI of ν_phys intersects [ν_Pellis − 0.10, ν_Pellis + 0.10]. This resolves E2 in v1.0.

**Note on O3:** The controlled vocabulary table above is the binding exhibit. All v1.0 documents adopt it. This resolves O3 in v1.0.

---

## Version Signature

This version definition is complete and locked when signed below.

**Version:** 1.0
**Date of definition:** June 14, 2026
**Author:** Joseph A. Sprute (ERES Maestro)
**ORCID:** 0000-0001-9946-3221
**Signature:** _______________________ (date of Zenodo deposit)

**What this signature means:**
- The contents listed above are complete and correct as of the date signed
- Nothing in the "Does NOT Contain" list is being concealed — it is genuinely absent
- The five gaps are acknowledged; E2 and O3 are resolved in this version
- E1, O1, and O2 remain open and are documented as open
- No isomorphism claim is made in v1.0
- v2.0 will not be published until the simulation pre-test and Q0–Q2 gates are passed or formally failed

---

*ERES Institute for New Age Cybernetics · est. February 2012 · Bella Vista, Arkansas*
*Three Governing Principles: Don't hurt yourself. Don't hurt others. Build for generations to come.*
*License: CCAL v2.1*
