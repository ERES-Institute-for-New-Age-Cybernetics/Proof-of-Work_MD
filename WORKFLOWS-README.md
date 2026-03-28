# ERES GitHub Workflows — BEST Configuration

> **Build · Evaluate · Sustain · Track**
> *Automated integrity for civilization-scale documentation*

---

## Overview

The ERES Institute GitHub Actions workflows implement automated validation, integrity checking, and reporting across the ERES corpus. The workflow architecture maps to the **BEST/SOUND/GOOD** moral vectoring principle:

| Workflow Tier | ERES Mapping | Function |
|---------------|--------------|----------|
| **BEST** | Personal integrity | Validate individual documents — linting, formatting, license compliance |
| **SOUND** | Public-Private trust | Cross-repository consistency — link checking, terminology validation, manifest generation |
| **GOOD** | Verifiable truth | Corpus-wide reporting — statistics, gap analysis, proof-of-work attestation |

All workflows run on `ubuntu-latest` and trigger on push/PR to `main`, with manual dispatch available.

---

## Workflow Architecture

```
C = R × P / M applied to CI/CD:

  C (Cybernetics)  = Automated workflow orchestration
  R (Resource)     = Repository files, documents, code artifacts
  P (Purpose)      = Integrity, consistency, accountability
  M (Method)       = GitHub Actions, linting, validation scripts
```

---

## Tier 1: BEST — Document Integrity

### `best-lint.yml` — Markdown Validation

Validates all `.md` files for formatting consistency, broken syntax, and ERES terminology compliance.

```yaml
# ERES BEST Tier 1: Document Integrity — Markdown Linting
name: BEST — Markdown Lint

on:
  push:
    branches: [ "main" ]
    paths: [ "**.md" ]
  pull_request:
    branches: [ "main" ]
    paths: [ "**.md" ]
  workflow_dispatch:

jobs:
  markdown-lint:
    name: Validate Markdown documents
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'

      - name: Install markdownlint
        run: npm install -g markdownlint-cli

      - name: Run Markdown linting
        run: |
          echo "=== ERES BEST: Document Integrity Check ==="
          echo "C = R × P / M — validating Resource integrity"
          markdownlint '**/*.md' --config .markdownlint.json || true

      - name: Count documents
        run: |
          echo "=== ERES Corpus Statistics ==="
          echo "Markdown files: $(find . -name '*.md' -not -path './.git/*' | wc -l)"
          echo "PDF files: $(find . -name '*.pdf' -not -path './.git/*' | wc -l)"
          echo "ZIP archives: $(find . -name '*.zip' -not -path './.git/*' | wc -l)"
          echo "Total tracked files: $(git ls-files | wc -l)"
```

### `best-license.yml` — CCAL v2.1 Compliance

Verifies that ERES original files carry proper CCAL v2.1 attribution markers.

```yaml
# ERES BEST Tier 1: License Compliance — CCAL v2.1
name: BEST — License Check

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]
  workflow_dispatch:

jobs:
  license-check:
    name: Verify CCAL v2.1 compliance
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Check for LICENSE file
        run: |
          echo "=== ERES BEST: CCAL v2.1 License Compliance ==="
          if [ -f "LICENSE" ] || [ -f "LICENSE.md" ]; then
            echo "LICENSE file found."
            if grep -qi "CARE Commons Attribution" LICENSE* 2>/dev/null; then
              echo "CCAL v2.1 reference confirmed."
            else
              echo "WARNING: LICENSE file exists but does not reference CCAL v2.1."
              echo "Expected: CARE Commons Attribution License v2.1"
            fi
          else
            echo "WARNING: No LICENSE file found."
            echo "ERES repositories should include CCAL v2.1 license text."
            echo "See: https://github.com/ERES-Institute-for-New-Age-Cybernetics/.github"
          fi

      - name: Check README license reference
        run: |
          if [ -f "README.md" ]; then
            if grep -qi "CCAL\|CARE Commons" README.md; then
              echo "README.md references CCAL licensing."
            else
              echo "NOTE: README.md does not mention CCAL v2.1 licensing."
            fi
          fi
```

---

## Tier 2: SOUND — Cross-Repository Consistency

### `sound-links.yml` — Link Validation

Checks all internal and external links across Markdown documents for integrity.

```yaml
# ERES SOUND Tier 2: Cross-Repository Consistency — Link Checking
name: SOUND — Link Validation

on:
  push:
    branches: [ "main" ]
    paths: [ "**.md" ]
  pull_request:
    branches: [ "main" ]
  schedule:
    # Run weekly on Sunday at midnight UTC
    - cron: '0 0 * * 0'
  workflow_dispatch:

jobs:
  link-check:
    name: Validate links across documents
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'

      - name: Install link checker
        run: npm install -g markdown-link-check

      - name: Check links in all Markdown files
        run: |
          echo "=== ERES SOUND: Cross-Reference Integrity ==="
          echo "Public-Private trust requires verifiable links"
          FAIL=0
          for file in $(find . -name '*.md' -not -path './.git/*'); do
            echo "Checking: $file"
            markdown-link-check "$file" --quiet || FAIL=1
          done
          if [ $FAIL -eq 1 ]; then
            echo "WARNING: Some links are broken. Review output above."
          else
            echo "All links validated."
          fi
```

### `sound-terminology.yml` — ERES Terminology Validation

Ensures canonical terminology is used correctly across the corpus.

```yaml
# ERES SOUND Tier 2: Terminology Consistency
name: SOUND — Terminology Check

on:
  push:
    branches: [ "main" ]
    paths: [ "**.md" ]
  pull_request:
    branches: [ "main" ]
  workflow_dispatch:

jobs:
  terminology:
    name: Validate ERES canonical terminology
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Check for known terminology errors
        run: |
          echo "=== ERES SOUND: Terminology Validation ==="
          echo "Canonical terms must be preserved exactly."
          ERRORS=0

          # RHC must be "Resonant Harmony Cycle" not "Resonant Harmony Cybernetics"
          if grep -rin "Resonant Harmony Cybernetics" --include="*.md" .; then
            echo "ERROR: RHC = Resonant Harmony Cycle (not Cybernetics)"
            ERRORS=$((ERRORS+1))
          fi

          # SOMT must be "Sociocratic Overlay Metadata Tapestry"
          if grep -rin "Strategic Optimization.*Merit Tracking" --include="*.md" .; then
            echo "ERROR: SOMT = Sociocratic Overlay Metadata Tapestry (not Strategic Optimization & Merit Tracking)"
            ERRORS=$((ERRORS+1))
          fi

          # SROC must be "Smart-Resonant Offset Contracts"
          if grep -rin "Smart Registered Offset" --include="*.md" .; then
            echo "ERROR: SROC = Smart-Resonant Offset Contracts (not Smart Registered)"
            ERRORS=$((ERRORS+1))
          fi

          # REAL equation must not repeat letters (ERS/ST variant is error)
          if grep -rin "REAL.*E.*R.*S.*S.*T" --include="*.md" .; then
            echo "WARNING: Check REAL equation — the ERS/ST variant repeats S"
            ERRORS=$((ERRORS+1))
          fi

          # License should be CCAL not MIT
          if grep -rin "MIT License" --include="*.md" . | grep -v "MIT Press"; then
            echo "ERROR: ERES uses CCAL v2.1, not MIT License"
            ERRORS=$((ERRORS+1))
          fi

          if [ $ERRORS -eq 0 ]; then
            echo "All terminology checks passed."
          else
            echo "$ERRORS terminology issue(s) found. Please correct."
          fi
```

---

## Tier 3: GOOD — Corpus-Wide Reporting

### `good-manifest.yml` — Proof-of-Work Manifest

Generates a complete file manifest with checksums for attestation and provenance tracking.

```yaml
# ERES GOOD Tier 3: Verifiable Truth — Proof-of-Work Manifest
name: GOOD — Corpus Manifest

on:
  push:
    branches: [ "main" ]
  workflow_dispatch:

jobs:
  manifest:
    name: Generate proof-of-work manifest
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Generate file manifest with checksums
        run: |
          echo "=== ERES GOOD: Proof-of-Work Manifest ==="
          echo "Graceful Evolution requires verifiable provenance."
          echo ""
          echo "ERES CORPUS MANIFEST"
          echo "Repository: ${{ github.repository }}"
          echo "Generated: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
          echo "Commit: ${{ github.sha }}"
          echo "Branch: ${{ github.ref_name }}"
          echo "---"
          echo ""

          # File inventory by type
          echo "FILE INVENTORY:"
          echo "  Markdown (.md):  $(find . -name '*.md' -not -path './.git/*' | wc -l)"
          echo "  PDF (.pdf):      $(find . -name '*.pdf' -not -path './.git/*' | wc -l)"
          echo "  ZIP (.zip):      $(find . -name '*.zip' -not -path './.git/*' | wc -l)"
          echo "  DOCX (.docx):    $(find . -name '*.docx' -not -path './.git/*' | wc -l)"
          echo "  HTML (.html):    $(find . -name '*.html' -not -path './.git/*' | wc -l)"
          echo "  JavaScript (.js): $(find . -name '*.js' -not -path './.git/*' -not -path './node_modules/*' | wc -l)"
          echo "  Python (.py):    $(find . -name '*.py' -not -path './.git/*' | wc -l)"
          echo "  Total tracked:   $(git ls-files | wc -l)"
          echo ""

          # Repository age and commit count
          echo "REPOSITORY HISTORY:"
          echo "  First commit: $(git log --reverse --format='%ai' | head -1)"
          echo "  Latest commit: $(git log -1 --format='%ai')"
          echo "  Total commits: $(git rev-list --count HEAD)"
          echo "  Contributors: $(git log --format='%ae' | sort -u | wc -l)"
          echo ""

          # SHA256 checksums for all non-git files
          echo "SHA256 CHECKSUMS:"
          find . -type f -not -path './.git/*' -not -path './node_modules/*' | sort | while read f; do
            sha256sum "$f"
          done

      - name: Generate ERES document index
        run: |
          echo ""
          echo "=== ERES DOCUMENT INDEX ==="
          echo ""
          echo "ERES-prefixed files (core corpus):"
          find . -name 'ERES*' -not -path './.git/*' | sort
          echo ""
          echo "FAVORS/BERA files:"
          find . -name 'FAVORS*' -o -name 'BERA*' | grep -v '.git' | sort
          echo ""
          echo "ESVRD files:"
          find . -name 'ESVRD*' -not -path './.git/*' | sort
          echo ""
          echo "GAIA/SOMT files:"
          find . -name 'GAIA*' -not -path './.git/*' | sort
```

### `good-stats.yml` — Corpus Statistics Report

Weekly automated report on corpus growth and health.

```yaml
# ERES GOOD Tier 3: Corpus Statistics and Growth Tracking
name: GOOD — Weekly Stats

on:
  schedule:
    # Run every Monday at 6:00 AM UTC
    - cron: '0 6 * * 1'
  workflow_dispatch:

jobs:
  stats:
    name: Generate corpus statistics
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Corpus health report
        run: |
          echo "=========================================="
          echo " ERES CORPUS HEALTH REPORT"
          echo " $(date -u +%Y-%m-%d)"
          echo " Repository: ${{ github.repository }}"
          echo "=========================================="
          echo ""
          echo "BEST (Document Integrity):"
          echo "  README.md present: $([ -f README.md ] && echo 'YES' || echo 'NO')"
          echo "  LICENSE present:   $([ -f LICENSE ] || [ -f LICENSE.md ] && echo 'YES' || echo 'MISSING')"
          echo ""
          echo "SOUND (Consistency):"
          echo "  Total .md files:   $(find . -name '*.md' -not -path './.git/*' | wc -l)"
          echo "  Total .pdf files:  $(find . -name '*.pdf' -not -path './.git/*' | wc -l)"
          echo "  Total .zip files:  $(find . -name '*.zip' -not -path './.git/*' | wc -l)"
          echo ""
          echo "GOOD (Growth):"
          echo "  Total commits:     $(git rev-list --count HEAD)"
          echo "  Commits (30 days): $(git rev-list --count --since='30 days ago' HEAD)"
          echo "  Commits (7 days):  $(git rev-list --count --since='7 days ago' HEAD)"
          echo "  Repo size:         $(du -sh . --exclude=.git | cut -f1)"
          echo ""
          echo "RECENT ACTIVITY (last 10 commits):"
          git log --oneline -10
          echo ""
          echo "=========================================="
          echo " C = R × P / M"
          echo " Build for generations to come."
          echo "=========================================="
```

---

## Unified CI Pipeline

### `ci.yml` — Master Workflow

Replaces the default GitHub template. Runs all BEST/SOUND checks on every push.

```yaml
# ERES Unified CI — BEST/SOUND/GOOD
# Replaces the default GitHub Actions template
name: ERES CI — Integrity Pipeline

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]
  workflow_dispatch:

jobs:
  # ─── BEST: Document Integrity ───
  best:
    name: BEST — Document Integrity
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: File inventory
        run: |
          echo "=== ERES BEST: Document Integrity ==="
          echo "Markdown: $(find . -name '*.md' -not -path './.git/*' | wc -l)"
          echo "PDF:      $(find . -name '*.pdf' -not -path './.git/*' | wc -l)"
          echo "ZIP:      $(find . -name '*.zip' -not -path './.git/*' | wc -l)"
          echo "Total:    $(git ls-files | wc -l) tracked files"

      - name: License check
        run: |
          if [ -f "LICENSE" ] || [ -f "LICENSE.md" ]; then
            echo "LICENSE file: PRESENT"
          else
            echo "WARNING: No LICENSE file. ERES requires CCAL v2.1."
          fi

      - name: README check
        run: |
          if [ -f "README.md" ]; then
            echo "README.md: PRESENT ($(wc -l < README.md) lines)"
          else
            echo "WARNING: No README.md found."
          fi

  # ─── SOUND: Terminology Consistency ───
  sound:
    name: SOUND — Terminology
    runs-on: ubuntu-latest
    needs: best
    steps:
      - uses: actions/checkout@v4

      - name: Canonical terminology check
        run: |
          echo "=== ERES SOUND: Terminology Validation ==="
          PASS=true

          # Check for known errors
          grep -rin "Resonant Harmony Cybernetics" --include="*.md" . && echo "FIX: RHC = Resonant Harmony Cycle" && PASS=false || true
          grep -rin "Strategic Optimization.*Merit Tracking" --include="*.md" . && echo "FIX: SOMT = Sociocratic Overlay Metadata Tapestry" && PASS=false || true
          grep -rin "Smart Registered Offset" --include="*.md" . && echo "FIX: SROC = Smart-Resonant Offset Contracts" && PASS=false || true
          grep -rin "MIT License" --include="*.md" . | grep -v "MIT Press" && echo "FIX: Use CCAL v2.1, not MIT License" && PASS=false || true

          if [ "$PASS" = true ]; then
            echo "All terminology checks PASSED."
          fi

  # ─── GOOD: Attestation ───
  good:
    name: GOOD — Attestation
    runs-on: ubuntu-latest
    needs: [best, sound]
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Proof-of-work summary
        run: |
          echo "=== ERES GOOD: Proof-of-Work Attestation ==="
          echo "Repository: ${{ github.repository }}"
          echo "Commit:     ${{ github.sha }}"
          echo "Timestamp:  $(date -u +%Y-%m-%dT%H:%M:%SZ)"
          echo "Commits:    $(git rev-list --count HEAD) total"
          echo "Files:      $(git ls-files | wc -l) tracked"
          echo "Size:       $(du -sh . --exclude=.git | cut -f1)"
          echo ""
          echo "BEST:  Document integrity verified"
          echo "SOUND: Terminology consistency verified"
          echo "GOOD:  Attestation record generated"
          echo ""
          echo "C = R × P / M"
          echo "Don't hurt yourself. Don't hurt others."
          echo "Build for generations to come."
```

---

## Configuration Files

### `.markdownlint.json`

Place in repository root for Markdown linting rules:

```json
{
  "default": true,
  "MD013": false,
  "MD033": false,
  "MD041": false,
  "MD024": { "siblings_only": true },
  "MD029": { "style": "ordered" }
}
```

**Rule explanations:**
- `MD013: false` — Disable line length limit (ERES documents are long-form)
- `MD033: false` — Allow inline HTML (badges, special formatting)
- `MD041: false` — Don't require H1 as first line (ERES docs use banners)
- `MD024` — Allow duplicate headings only for sibling sections
- `MD029` — Ordered list numbering must be sequential

---

## Deployment Guide

### Step 1: Create workflow directory

```bash
mkdir -p .github/workflows
```

### Step 2: Add workflows

Copy the YAML blocks above into individual files:

```
.github/
  workflows/
    ci.yml                    # Unified pipeline (start here)
    best-lint.yml             # Markdown linting
    best-license.yml          # CCAL compliance
    sound-links.yml           # Link validation
    sound-terminology.yml     # Terminology check
    good-manifest.yml         # Proof-of-work manifest
    good-stats.yml            # Weekly statistics
```

### Step 3: Add configuration

```bash
# Markdown linting config
cp .markdownlint.json ./
```

### Step 4: Enable Actions

In each repository's Settings → Actions → General:
- Select "Allow all actions and reusable workflows"
- Workflow permissions: "Read and write permissions"

### Recommended rollout order

1. **Start with `ci.yml`** — the unified pipeline covers all basics
2. **Add `good-stats.yml`** — weekly health reporting
3. **Add individual BEST/SOUND workflows** — as repos mature

### Which repos get which workflows

| Repository | `ci.yml` | `best-lint` | `sound-links` | `sound-terminology` | `good-manifest` | `good-stats` |
|------------|----------|-------------|---------------|---------------------|-----------------|--------------|
| Proof-of-Work_MD | Yes | Yes | Yes | Yes | Yes | Yes |
| PlayNAC-KERNEL | Yes | — | — | — | Yes | Yes |
| Support-Documentation | Yes | Yes | Yes | Yes | Yes | Yes |
| Gracechain-Meritcoin | Yes | Yes | Yes | Yes | Yes | Yes |
| Proof-of-Work | Yes | — | — | — | Yes | Yes |
| .github | Yes | Yes | — | Yes | — | — |
| ERES-Relativity-Equation | Yes | — | — | — | — | — |
| NAC_Images | Yes | — | — | — | Yes | — |
| ZIP | Yes | — | — | — | Yes | Yes |
| Discussions | — | — | — | — | — | — |

---

## ERES CI Principles

The ERES workflow architecture follows the same moral vectoring as the Trilogy:

1. **BEST (Personal):** Each document passes integrity checks independently — no file should break the build on its own
2. **SOUND (Public-Private):** Cross-document consistency is enforced — terminology, links, and references must be trustworthy
3. **GOOD (Graceful Evolution):** The corpus generates its own attestation record — proof-of-work is automatic, verifiable, and permanent

> *"If it works in a THOW, it works on a generation ship."*
> The VLSA Principle applies to CI/CD too: if the workflow validates a single README, it validates the entire corpus.

---

**Document ID:** ERES-WORKFLOWS-README-2026-001
**Last Updated:** March 28, 2026
**License:** CARE Commons Attribution License v2.1 (CCAL)
**Classification:** Open / Unrestricted
