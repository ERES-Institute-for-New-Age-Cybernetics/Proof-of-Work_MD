# Workflows

> *CI/CD architecture for the ERES Institute — BEST / SOUND / GOOD as a three-gate pipeline.*

[![License: CCAL v2.1](https://img.shields.io/badge/License-CCAL%20v2.1-blue.svg)](#license)
[![Pipeline](https://img.shields.io/badge/Pipeline-BEST%20%E2%86%92%20SOUND%20%E2%86%92%20GOOD-purple.svg)]()
[![Part of ERES](https://img.shields.io/badge/Part%20of-ERES%20Institute-green.svg)](https://github.com/ERES-Institute-for-New-Age-Cybernetics)

---

## Purpose

Shared **GitHub Actions workflows**, reusable composite actions, and pipeline contracts used across ERES Institute repositories. This repository is the single source of truth for how ERES code and documents are validated, released, and archived.

## Pipeline Model — BEST / SOUND / GOOD

The ERES Trilogy maps directly onto a three-gate CI/CD pipeline:

```
  commit ──▶  [ BEST ]  ──▶  [ SOUND ]  ──▶  [ GOOD ]  ──▶  release
             Personal      Public-Private    Graceful
             (Book 1)      (Book 2)          Evolution
                                             (Book 3)
```

| Gate | Trilogy | What It Checks |
|------|---------|----------------|
| **BEST** | Book 1 — ONE GOOD · Synthetic AI Constitution Through UBIMIA | Personal-grade hygiene: lint, format, type-check, secret-scan. |
| **SOUND** | Book 2 — SECURITY-CLEARANCE · IDIPITIS Framework for NBERS | Public-Private-grade integrity: unit + integration tests, SPT Triad checks, dependency audit. |
| **GOOD** | Book 3 — DATA-INTEGRITY · FAVORS for CBGMODD GAIA SOMT | Graceful-evolution-grade: MIEVM validation, Erasure Completeness Ratio (ECR), release-readiness. |

## Trifecta Protocol Gates

Production-bound changes must pass the **Trifecta Protocol**:

1. **ONE-GOOD** — ethical/moral vector check (Three Governing Principles).
2. **SECURITY-CLEARANCE** — SPT Triad (`ERES-SPT-2026-001`) enforcement.
3. **DATA-INTEGRITY** — provenance, versioning, and MIEVM corroboration.

## Reusable Actions

Typical contents of this repository:

- `.github/workflows/best.yml` — lint, format, secret-scan baseline.
- `.github/workflows/sound.yml` — test matrix, SPT Triad validators.
- `.github/workflows/good.yml` — MIEVM regression harness, release checklist.
- `actions/mievm-validate/` — composite action invoking the ensemble (Claude, Grok, DeepSeek, ChatGPT) against specification deltas.
- `actions/spt-check/` — SECUIR / VERTECA / FAVORS / CBGMODD static analysis.

## Using These Workflows From Another Repo

```yaml
# .github/workflows/ci.yml in a consumer repo
name: ERES CI
on: [push, pull_request]

jobs:
  best:
    uses: ERES-Institute-for-New-Age-Cybernetics/Workflows/.github/workflows/best.yml@main
  sound:
    needs: best
    uses: ERES-Institute-for-New-Age-Cybernetics/Workflows/.github/workflows/sound.yml@main
  good:
    needs: sound
    uses: ERES-Institute-for-New-Age-Cybernetics/Workflows/.github/workflows/good.yml@main
```

## Governing Formula

```
C = R × P / M
```

The pipeline is itself a Cybernetics instrument: each gate is a Method, each artifact is a Resource, each gate-promotion is a Purpose-check.

## Citation

```bibtex
@misc{sprute_eres_workflows_2026,
  author       = {Sprute, Joseph A.},
  title        = {{ERES Workflows: BEST / SOUND / GOOD CI/CD Pipeline}},
  year         = {2026},
  howpublished = {GitHub repository, ERES Institute for New Age Cybernetics},
  url          = {https://github.com/ERES-Institute-for-New-Age-Cybernetics/Workflows}
}
```

## License

**CARE Commons Attribution License v2.1 (CCAL v2.1).** See [`LICENSE`](./LICENSE).

## Contact

- **Joseph Allen Sprute** (ERES Maestro) — eresmaestro@gmail.com
- ORCID: [0000-0001-9946-3221](https://orcid.org/0000-0001-9946-3221)

---

> **Three Governing Principles** — Don't hurt yourself. Don't hurt others. Build for generations to come.

<sub>Document ID: `ERES-WORKFLOWS-README-2026-001` · Last updated: April 13, 2026</sub>
