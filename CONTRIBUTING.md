# Contributing to ERES Institute for New Age Cybernetics

Thank you for your interest in contributing to the ERES Institute. Your experiences, expertise, and perspective will benefit everyone who reads, uses, and builds upon this work — including generations who haven't been born yet.

We've put together the following guidelines to help you figure out where you can best be helpful. If something in this guide is unclear or feels incomplete, that's itself a contribution opportunity — tell us, and we'll fix it through NPR.

> _"Don't hurt yourself. Don't hurt others. Build for generations to come."_

---

## Table of Contents

0. [Types of contributions we're looking for](#types-of-contributions-were-looking-for)
1. [Ground rules & expectations](#ground-rules--expectations)
2. [How to contribute](#how-to-contribute)
3. [Style guide](#style-guide)
4. [ERES terminology conventions](#eres-terminology-conventions)
5. [Setting up your environment](#setting-up-your-environment)
6. [Review process](#review-process)
7. [License & attribution](#license--attribution)
8. [Community](#community)

---

## Types of contributions we're looking for

There are many ways to contribute to the ERES Institute (in descending order of current need):

### High Priority
- **Validate claims** — Run independent tests against ERES frameworks. MIEVM welcomes all instruments, not just the current four (Claude, Grok, DeepSeek, ChatGPT). If you can break something, that's a gift.
- **Translate documents** — The Government Partnership Brief is in 7 languages. ERES TERMS #46 and the SECURITY.md need more. Every language added extends the reach by a civilization.
- **Fix terminology inconsistencies** — The CI workflow checks for locked-acronym errors (RHC ≠ "Cybernetics," SOMT ≠ "Standard Operating"). If you find more, file them.
- **Implement framework components** — BERA-PY needs contributors. Gracechain-Meritcoin needs contributors. PlayNAC KERNEL needs contributors. Code is welcome.

### Always Welcome
- **Critique** — Substantive criticism of ERES concepts, equations, architecture, or claims. We don't need agreement; we need rigor. If C = R × P / M is wrong, show us why.
- **Improve documentation** — Reduce acronym density, add examples, write tutorials, create diagrams that make the 6KDA accessible to newcomers.
- **Connect to existing academic literature** — ERES draws from systems theory, ecological economics, participatory governance, and complexity science. If you see connections we've missed or citations we should include, that's valuable.
- **Report bugs** — In code, in documents, in logic. Every bug reported through NPR is a system improvement.
- **Propose extensions** — New ERES TERMS, new framework applications, new deployment contexts. If it passes the three-principle test, it belongs.

### What We're NOT Looking For
- Contributions that violate the three foundational principles
- Proprietary enclosures of CCAL-licensed material
- Self-promotional content disguised as contributions (link farming, corporate placement)
- Contributions that require punitive enforcement to implement — if a contribution needs punishment to work, it doesn't work

---

## Ground Rules & Expectations

Before we get started, here are the expectations (of you and of us):

### From You
- **Read the Code of Conduct.** By participating, you agree to abide by the [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md), which is governed by Non-Punitive Remediation (NPR v3.0). There is no punitive enforcement ladder here.
- **Be kind and thoughtful.** We come from different backgrounds, disciplines, and levels of familiarity with ERES terminology. Listen before correcting. Ask before assuming. The acronym density is a known accessibility barrier — patience with newcomers is itself a contribution.
- **Critique the work, not the person.** "This equation is dimensionally inconsistent" is a contribution. "You don't understand math" is not.
- **Ensure your contribution passes CI.** If the ERES-CI workflow flags a locked-acronym error or a missing principle reference, address it before requesting review. If the CI itself is wrong, file that as a separate issue.
- **Don't fear retribution.** This is not a platitude. The SECURITY.md and the SCALULAR Engine architecturally guarantee that no contributor will be penalized for filing a concern, reporting a vulnerability, critiquing a framework, or speaking truth. If you experience retribution, that is a system failure and must be reported.

### From Us
- **We will respond to contributions within 14 days.** If we can't review in that window, we'll tell you why and give a revised timeline.
- **We will never punish a contributor.** NPR governs all interactions. If your contribution doesn't fit, we'll explain why and help you find a better path — we won't reject you as a person.
- **We will credit all contributions.** Under CCAL v2.1, attribution is required. Your name (or pseudonym, if you prefer) will be credited in the relevant document, commit history, and acknowledgments.
- **We will apply the same standards to ourselves.** The founder is subject to the same Code of Conduct, the same NPR process, and the same fear-of-retribution guarantees as every other participant.

---

## How to Contribute

### Step 1: Find Your Entry Point

| If you want to... | Start here |
|---|---|
| Report a bug or inconsistency | Open an Issue with the `bug` or `inconsistency` label |
| Propose a new term or framework extension | Open a Discussion with the `proposal` label |
| Submit code (BERA-PY, Gracechain, PlayNAC) | Fork the relevant repository, create a branch, submit a PR |
| Translate a document | Open a Discussion with the `translation` label to coordinate |
| Critique or validate a claim | Open a Discussion with the `validation` label |
| Report a security concern | See [SECURITY.md](SECURITY.md) — email or Discussion with `security` label |
| Report a conduct concern | See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) — email with `[CONDUCT]` subject |

### Step 2: Check Existing Work

Before starting, search through [open Issues](https://github.com/ERES-Institute-for-New-Age-Cybernetics/Discussions/issues), [Pull Requests](https://github.com/ERES-Institute-for-New-Age-Cybernetics/Discussions/pulls), and [Discussions](https://github.com/ERES-Institute-for-New-Age-Cybernetics/Discussions/discussions) to see whether someone else has raised a similar idea or question. Duplication is fine — convergent thinking validates — but coordination is better.

### Step 3: Create Your Contribution

1. **Always create a new branch** for your changes (never commit directly to `main`)
2. **Write clear commit messages** that reference the relevant ERES framework or document
3. **Test your changes** against the CI workflow before submitting
4. **Follow the style guide** (below)
5. **Be patient during review** — this is a solo-researcher operation with growing community support

### Step 4: Submit

Open a Pull Request with a clear description of what you've done and why. Reference relevant ERES TERMS #46 entries, link to related Discussions, and note which of the three principles your contribution serves.

---

## Style Guide

### Writing Style
- **Clarity over cleverness.** ERES already has significant terminology density. New contributions should reduce cognitive load, not increase it.
- **Define before using.** Every acronym should be expanded on first use in any document. Example: "SOMT (Sociocratic Overlay Metadata Tapestry)" — not just "SOMT."
- **Plain language summaries.** Every technical section should be preceded or followed by a plain-language summary that a grandmother, a 12-year-old, or a head of state can understand.
- **Active voice.** "The system measures resonance" not "resonance is measured by the system."
- **Present tense for frameworks.** "UBIMIA delivers universal basic income" not "UBIMIA will deliver."

### Formatting
- **Markdown** for all documentation (.md files)
- **Headers** follow standard hierarchy (H1 for document title, H2 for major sections, H3 for subsections)
- **Tables** for structured comparisons, framework mappings, and specification data
- **Code blocks** with language identifiers (```python, ```javascript, ```yaml)
- **Links** to ERES TERMS #46 entries for all acronym definitions where practical

---

## ERES Terminology Conventions

### Locked Acronyms (Do Not Modify)
These expansions were locked in the SPT Papers (March 2026) and are canonical:

| Acronym | Locked Expansion | Common Error |
|---------|-----------------|-------------|
| **CyberRAVE** | Cybernetic Ratings Abolishing Veiled Exchanges | ~~Remote Access Virtual Environment~~ (pre-2026) |
| **GunnySack** | Guaranteed User-group Network Nullifying Yieldless Service: Accredited Certified Knowledge | ~~No expansion~~ (pre-2026) |
| **SaleBuilders** | Smart-city Adaptive Living Engineering Banishing Untested Infrastructure — Laboratories Delivering Enduring Resilient Systems | ~~No expansion~~ (pre-2026) |
| **RHC** | Resonant Harmony Cycle | ~~Resonant Harmony Cybernetics~~ |
| **SOMT** | Sociocratic Overlay Metadata Tapestry | ~~Standard Operating Metadata Tapestry~~ |
| **REAL formula** | (E·M·R)/(T·S) — no repeated letters | ~~ERS/ST variant~~ (S repeats) |

### Canonical Equations
When referencing ERES equations, use these exact forms:
- `C = R × P / M` (not C=RPM, not C=R*P/M in prose)
- `M × E + C = R`
- `REAL = (E · M · R) / (T · S)`
- `$IT = GEAR × DERR + ERES`
- `EP = CPM × WBS + PERT`
- `RCI = P_Ω_norm × ARI_sys × VibConst`

### Version References
Always reference the current ERES TERMS version number. As of this writing: **ERES TERMS #46** (March 28, 2026). If your contribution introduces a new term, note it as a candidate for TERMS #47.

### FAVORS — Six Factors
FAVORS has **six** channels, not five. Always include Odor:
**F**ingerprint · **A**ura · **V**oice · **O**dor · **R**etina · **S**ignature

---

## Setting Up Your Environment

### For Documentation Contributions
No special setup required. Edit markdown files directly on GitHub or clone locally:

```bash
git clone https://github.com/ERES-Institute-for-New-Age-Cybernetics/Discussions.git
cd Discussions
# Create a branch
git checkout -b your-contribution-name
# Edit, commit, push, PR
```

### For Code Contributions (BERA-PY, PlayNAC, Gracechain)

**Python projects:**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
```

**Node.js projects (PlayNAC KERNEL):**
```bash
npm install
npm test
```

### For VLSA Scale Testing
The ERES-VLSA-Scale-Test.js executable is the reference validation suite (91 tests, 100% pass rate). Run it to verify your changes don't break scale invariance:

```bash
node ERES-VLSA-Scale-Test.js
# Expected output: 91/91 passed
```

---

## Review Process

### Who Reviews
Currently: Joseph A. Sprute (ERES Maestro) as sole maintainer. As the community grows, review will be distributed through CBGMODD seven-stakeholder governance.

### Review Criteria
Every contribution is evaluated against:

1. **Three Principles** — Does it hurt self? Does it hurt others? Does it build for generations?
2. **Consistency** — Does it align with ERES TERMS #46 and locked acronym expansions?
3. **Clarity** — Does it reduce or increase cognitive load for the reader?
4. **CCAL Compliance** — Is it properly attributed? Is it open-source? Does it avoid prohibited uses?
5. **Testability** — Can the claim be validated? Does it invite MIEVM-style independent testing?

### What Happens If Your Contribution Is Not Accepted
NPR applies. You will receive a written explanation of why the contribution doesn't fit in its current form, specific suggestions for revision, and an invitation to resubmit. You will not be rejected as a person. Your effort is acknowledged and appreciated regardless of outcome.

---

## License & Attribution

### All Contributions Are CCAL v2.1
By contributing to any ERES Institute repository, you agree that your contribution is licensed under the **CARE Commons Attribution License v2.1 (CCAL)**.

This means:
- Your contribution will be freely available for civic, educational, ecological, and research purposes
- Your contribution will be attributed to you (name or pseudonym)
- Your contribution cannot be enclosed in proprietary systems
- Derivative works must use the same or equivalent license

### Attribution Format
Contributions will be credited in the following format:

> **[Your Name/Handle]** — [Brief description of contribution]. ERES Institute for New Age Cybernetics, CCAL v2.1.

If you contribute a substantial framework extension, equation, or novel analysis, you may be credited as a co-author on related publications (with your consent).

---

## Community

### Where Discussions Happen
All project discussion takes place in this repository's [Discussions](https://github.com/ERES-Institute-for-New-Age-Cybernetics/Discussions/discussions) section and in [Issues](https://github.com/ERES-Institute-for-New-Age-Cybernetics/Discussions/issues). Everybody is welcome.

Wherever possible, do not take these conversations to private channels, including contacting the maintainer directly (except for conduct and security concerns, which have designated private channels). Keeping communication public means everybody can benefit and learn from the conversation. Knowledge is shared wealth.

### External Community
| Platform | Link | Purpose |
|----------|------|---------|
| ResearchGate | [Joseph A Sprute](https://www.researchgate.net/profile/Joseph-Sprute) | Academic publications and peer engagement |
| Medium | [@josephasprute](https://medium.com/@josephasprute) | Public-facing essays |
| Threads | [@josephsprute](https://www.threads.com/@josephsprute) | Community updates |
| Substack | [josephasprute](https://josephasprute.substack.com) | Newsletter |

### Getting Help
If you're new to ERES and feeling overwhelmed by terminology, start here:
1. **ERES TERMS #46** — the complete glossary with definitions
2. **README.md** — repository overview with frameworks at a glance
3. **SECURITY.md** — the security architecture and your rights as a contributor
4. **This document** — contribution pathways and style guide

If you're still stuck, open a Discussion with the `help-wanted` label. Someone will respond. NPR applies — there are no stupid questions, only systems that failed to explain clearly enough.

---

**ERES Institute for New Age Cybernetics** — Est. February 2012  
_"Don't hurt yourself. Don't hurt others. Build for generations to come."_  
**CARE Commons Attribution License v2.1 (CCAL)**
