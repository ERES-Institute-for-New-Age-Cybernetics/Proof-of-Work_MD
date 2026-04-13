# ZIP — PlayNAC KERNEL Codebase

> *The working code home of the PlayNAC KERNEL. Where the specification becomes executable.*

[![License: CCAL v2.1](https://img.shields.io/badge/License-CCAL%20v2.1-blue.svg)](#license)
[![Runtime](https://img.shields.io/badge/Runtime-Node.js%2018%2B-green.svg)]()
[![Database](https://img.shields.io/badge/DB-PostgreSQL%2012%2B-blue.svg)]()
[![Cache](https://img.shields.io/badge/Cache-Redis%206%2B-red.svg)]()
[![Part of ERES](https://img.shields.io/badge/Part%20of-ERES%20Institute-green.svg)](https://github.com/ERES-Institute-for-New-Age-Cybernetics)

---

## What This Repository Is

This repository hosts the **PlayNAC KERNEL codebase** — the executable counterpart to the canonical PDF specification in [`PlayNAC-KERNEL`](../PlayNAC-KERNEL). Source code, configuration, schemas, and deployable artifacts live here.

> The repository is named `ZIP` for historical reasons (originally a container for program ZIP files). It has been **repositioned as the codebase home**.

## Companion Repositories

| Repository | Role |
|------------|------|
| [`PlayNAC-KERNEL`](../PlayNAC-KERNEL) | PDF specification (what the code implements) |
| [`Support-Documentation`](../Support-Documentation) | R&D packaging, auxiliary specs |
| [`Proof-of-Work_MD`](../Proof-of-Work_MD) | Genesis markdown corpus (prior art) |
| [`Gracechain-Meritcoin`](../Gracechain-Meritcoin) | Economic layer (Proof-of-Resonance) |
| [`Workflows`](../Workflows) | CI/CD for this codebase |

## KERNEL Surface Area

The KERNEL exposes subsystems aligned to the specification:

- **Authentication & Identity** — JWT-based, IDIPITIS-aware (Book 2 mapping).
- **PlayNAC Engine** — task/quest completion, achievements, progression.
- **BERA Measurement** — ARI, ERI, **RHC** (Resonant Harmony Cycle), RCI.
- **UBIMIA distribution** — balance, accrual, settlement.
- **Meritcoin accrual** — **Proof-of-Resonance** (not Proof-of-Work).
- **GAIA tracking** — planetary-tier (T1–T8) state toward JUSTUS end-state.
- **SROC settlement** — Smart-Resonant Offset Contracts.
- **SPT enforcement** — Security, Privacy, Trust per `ERES-SPT-2026-001`.

## Technical Stack

| Layer | Technology |
|-------|------------|
| Runtime | Node.js 18+ (Python 3.8+ companion utilities) |
| Database | PostgreSQL 12+ |
| Cache / queue | Redis 6+ |
| API | Express + Joi validation |
| Auth | JWT (access + refresh) |
| Rate limiting | Token bucket, per-endpoint |

## Quick Start

```bash
# Clone
git clone https://github.com/ERES-Institute-for-New-Age-Cybernetics/ZIP.git
cd ZIP

# Install
npm install

# Configure
cp .env.example .env
# -> set JWT_SECRET, REFRESH_TOKEN_SECRET, DB creds

# Run
npm start
```

## Canonical Formulae Used by the Code

```
C = R × P / M                              (Cybernetics = Resource × Purpose / Method)
M × E + C = R                              (Matter × Energy + Constant = Reason)
REAL = (E·M·R) / (T·S)                     (Energy · Matter · Resonance / Time · Space)
RCI  = P_Ω_norm × ARI_sys × VibConst       (Resonant Coherence Index, with Butzbach)
```

## MIEVM-Linked Validation

The code is exercised against MIEVM-validated fixtures derived from the specification. Regression behavior should match the KERNEL PDF; divergence is a bug in the code, not the spec.

## Security, Privacy, Trust

All code changes are evaluated against the **SPT Triad** defined in `ERES-SPT-2026-001`. See [`SECURITY.md`](./SECURITY.md) for disclosure process.

## Contributing

See [`CONTRIBUTING.md`](./CONTRIBUTING.md) and [`CODE_OF_CONDUCT.md`](./CODE_OF_CONDUCT.md). Contributions are reviewed against the Three Governing Principles.

## Citation

```bibtex
@software{sprute_playnac_kernel_code_2026,
  author       = {Sprute, Joseph A.},
  title        = {{PlayNAC KERNEL Codebase}},
  year         = {2026},
  publisher    = {ERES Institute for New Age Cybernetics},
  url          = {https://github.com/ERES-Institute-for-New-Age-Cybernetics/ZIP}
}
```

## License

**CARE Commons Attribution License v2.1 (CCAL v2.1).** See [`LICENSE`](./LICENSE).

## Contact

- **Joseph Allen Sprute** (ERES Maestro) — eresmaestro@gmail.com
- ORCID: [0000-0001-9946-3221](https://orcid.org/0000-0001-9946-3221)

---

> **Three Governing Principles** — Don't hurt yourself. Don't hurt others. Build for generations to come.

<sub>Document ID: `ERES-ZIPCODE-README-2026-001` · Last updated: April 13, 2026</sub>
