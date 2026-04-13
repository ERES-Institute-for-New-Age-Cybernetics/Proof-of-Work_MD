# ERES GitHub README Refresh — April 13, 2026

Full-refresh of all 10 repository READMEs in the ERES Institute organization.

## Scope applied to every file

- **Markdown hygiene** — consistent heading hierarchy (H1 → H2 → H3), fenced code blocks with language hints, clean tables, consistent badge grammar, blockquote footer pattern.
- **Terminology pass** — canonical forms enforced throughout:
  - **SOMT** — Sociocratic Overlay Metadata Tapestry
  - **SROC** — Smart-Resonant Offset Contracts
  - **RHC** — Resonant Harmony **Cycle** (not *Cybernetics*)
  - **Meritcoin** — Proof-of-**Resonance** (not Proof-of-Work)
  - **CCAL v2.1** — CARE Commons Attribution License v2.1
  - **Three Governing Principles** as the closing blockquote
- **Standard sections added to every README**:
  - About / Overview
  - Governing Formula (at minimum `C = R × P / M`; Triune Math where relevant)
  - Repository role in the ERES ecosystem
  - Citation (BibTeX)
  - License
  - Contact
  - Three Governing Principles footer
  - Document ID + last-updated stamp
- **MIEVM badge** added where validation is relevant (7 of 10 repos).

## File inventory

| # | File | Target repo | Notes |
|---|------|-------------|-------|
| 1 | `01_dotgithub_profile_README.md` | `.github` → `profile/README.md` | Org landing page |
| 2 | `02_Support-Documentation_README.md` | `Support-Documentation` | R&D packaging |
| 3 | `03_Gracechain-Meritcoin_README.md` | `Gracechain-Meritcoin` | Proof-of-Resonance economics |
| 4 | `04_PlayNAC-KERNEL_README.md` | `PlayNAC-KERNEL` | PDF specification archive |
| 5 | `05_Proof-of-Work_MD_README.md` | `Proof-of-Work_MD` | Genesis corpus |
| 6 | `06_NAC_Images_README.md` | `NAC_Images` | CC0-1.0 exception (visual assets) |
| 7 | `07_ZIP_README.md` | `ZIP` | Repositioned as KERNEL codebase home |
| 8 | `08_Discussions_README.md` | `Discussions` | Community forum |
| 9 | `09_Workflows_README.md` | `Workflows` | BEST/SOUND/GOOD CI/CD |
| 10 | `10_ERES-Relativity-Equation_README.md` | `ERES-Relativity-Equation` | Triune Math Key #3 |

## Commit message template

```
docs(readme): full refresh — markdown hygiene + canonical terminology + standard sections

- Apply CCAL v2.1 license block, citation (BibTeX), contact, and
  Three Governing Principles footer to all 10 org repos.
- Correct terminology: SOMT, SROC, RHC (Cycle), Meritcoin = Proof-of-Resonance.
- Add MIEVM validation badge where applicable.
- Stamp Document IDs (ERES-*-README-2026-001) and last-updated date.

Ref: ERES-ORG-README-REFRESH-2026-04-13
```

## Deployment (recommended order)

1. `.github` (profile README) — sets the org landing page first.
2. `Proof-of-Work_MD` and `PlayNAC-KERNEL` — the archival anchors.
3. `Support-Documentation` and `ZIP` — working R&D + code home.
4. `Gracechain-Meritcoin` and `ERES-Relativity-Equation` — framework specifics.
5. `NAC_Images` — note the CC0 exception (confirm `LICENSE` file in repo matches).
6. `Workflows` — CI/CD.
7. `Discussions` — community-facing, last.

## Notes and caveats

- Each file is a **drop-in replacement** for the repo's `README.md`. File naming (`NN_RepoName_README.md`) is for sorting in this delivery bundle only; rename to `README.md` at the target.
- The `NAC_Images` repo uses **CC0-1.0** by exception; confirm the in-repo `LICENSE` file reflects that before committing.
- The `Workflows` README assumes the BEST/SOUND/GOOD pipeline files exist or will be added; if not yet present, the README still serves as architectural intent.
- All BibTeX entries use a consistent key pattern `sprute_<repo>_2026`.
- I did not fetch the live READMEs this session (fetch tool blocked non-prior URLs); the refresh is built from the established corpus context. **Spot-check each** against any content that may have been in the current README that you want preserved (recent release notes, specific file catalogs, etc.) before committing.
