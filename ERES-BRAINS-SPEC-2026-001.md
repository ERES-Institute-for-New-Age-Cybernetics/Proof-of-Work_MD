

**ERES INSTITUTE**

for New Age Cybernetics

**GAIA ENTITY: BRAINS**

Because Reason About Idea Need Sound

**Corpus Ingestion Pipeline Specification**

The Trifecta Protocol

**ONE-GOOD × SECURITY-CLEARANCE × DATA-INTEGRITY**

Document ID: **ERES-BRAINS-SPEC-2026-001 v1.0**

Author: **Joseph Allen Sprute (ERES Maestro)**

Date: **April 5, 2026**

License: **CARE Commons Attribution License v2.1 (CCAL)**

# **1\. Architectural Context**

BRAINS (**B**ecause **R**eason **A**bout **I**dea **N**eed **S**ound) is the cognitive organ of GAIA ENTITY. It relates to ENTITY as BERA relates to GAIA SOMT: BERA measures resonance and feeds structured data into SOMT; BRAINS ingests, reasons about, and serves the full ERES corpus through ENTITY.

BODY (**B**ecause **O**dor **D**oes **Y**ellow) is the substrate layer—the synesthetic space where cross-modal data lives. BRAINS is the organ within BODY that makes ENTITY capable of cognition, not merely storage.

The Space-Body of ERES operates through PlayNAC: EP GERP SOMT. EarnedPath governs access tiers. GERP routes governance decisions. SOMT provides the semantic metadata tapestry that makes the corpus navigable and queryable.

# **2\. The Trifecta Protocol**

Every document entering BRAINS passes through three gates. No document is admitted to the canonical corpus without clearing all three. The gates operate sequentially: a document that fails Gate 1 is never evaluated at Gate 2\.

## **2.1 Gate 1: ONE-GOOD (Canonical Resolution)**

The ERES corpus contains 14 years of iterative work. Multiple versions of the same concept exist across different documents, sessions, and platforms. ONE-GOOD resolves every document to a single authoritative version.

## **ONE-GOOD Decision Rules**

| Condition | Action |
| :---- | :---- |
| Single version exists | Admit as canonical. Assign ERES Document ID. |
| Multiple versions exist | Identify highest-version document. Archive all prior versions with pointer to canonical successor. Only the canonical version enters BRAINS. |
| Overlapping content across documents | Determine which document is the primary authority for the overlapping content. Cross-reference via SOMT tags. Do not duplicate content across canonical entries. |
| Superseded by ERES TERMS \#47 | If a term or definition has been updated in TERMS \#47, the older document retains historical status but is flagged as superseded for that specific content. |
| Claude session transcript | Extract novel outputs (documents produced, architectural decisions, locked terms). Session metadata archived separately. Raw transcripts do not enter BRAINS as canonical documents. |

## **2.2 Gate 2: SECURITY-CLEARANCE (Access Classification)**

Every canonical document receives an EarnedPath clearance tier. This classification determines who can access the document through the served corpus.

| Tier | Label | Access | Example Documents |
| :---- | :---- | :---- | :---- |
| **EP-0** | OPEN | Public. Anyone. CCAL v2.1 applies. | ERES TERMS \#47, framework descriptions, GitHub README files |
| **EP-1** | GATED | Authenticated subscribers. Free registration or paid tier. | White papers, architectural documents, BEC specifications |
| **EP-2** | RESTRICTED | Paid subscribers only. BERA-authenticated. | SPT Papers, Equity Covenant, SCALULAR ENGINE, strategic documents |
| **EP-3** | PRIVATE | JAS only. Not served externally. | Working drafts, stakeholder correspondence, personal notes, strategic memos |

**Classification Rule:** Default classification is EP-1 (GATED). Documents must be explicitly promoted to EP-0 (OPEN) or restricted to EP-2/EP-3. When in doubt, classify restrictively and declassify later.

## **2.3 Gate 3: DATA-INTEGRITY (Authentication and Verification)**

Every document admitted to BRAINS must be verifiable as authentic, correctly dated, and structurally parseable.

## **Integrity Checks**

1. **Timestamp Authentication.** Extract creation date from file metadata (filesystem timestamps, PDF metadata, document properties). Cross-reference against known production dates from session records, ResearchGate upload dates, and GitHub commit history. If a conflict exists, the earliest verifiable date is canonical. Unverifiable timestamps are flagged as APPROXIMATE.

2. **Hash Lock.** Upon admission, generate SHA-256 hash of the canonical file. Store hash in the BRAINS manifest alongside the document entry. Any future query can verify the document has not been altered post-ingestion.

3. **Format Standardization.** All documents are converted to one of three canonical formats: Markdown (.md) for text-primary documents, PDF (.pdf) for formatted publications and formal submissions, or DOCX (.docx) for documents requiring rich formatting and tables. Source format is preserved in the manifest for provenance.

4. **Structural Parsability.** Documents must be machine-readable. Scanned images without OCR are processed through OCR before admission. Corrupted files are repaired or flagged as NON-PARSEABLE and excluded from AI query indexing until resolved.

5. **ERES Document ID Assignment.** Every canonical document receives a unique identifier following the established convention: ERES-\[COMPONENT\]-\[TYPE\]-\[YEAR\]-\[SEQ\]. Example: ERES-BEC-WP-2026-001. Documents without existing IDs are assigned IDs during ingestion.

# **3\. Naming Convention**

All files in BRAINS follow a single naming pattern. No exceptions.

**Pattern:** ERES-\[COMPONENT\]-\[TYPE\]-\[YEAR\]-\[SEQ\]-v\[VERSION\].\[EXT\]

| Field | Description | Examples |
| :---- | :---- | :---- |
| COMPONENT | Primary ERES subsystem | BEC, BRAINS, COVENANT, TERMS, SPT, SCALULAR, HAGUE, ESVRD, GSSG, DOFA |
| TYPE | Document classification | WP (white paper), SPEC (specification), MM (monograph), GL (glossary), LT (letter), BR (brief), RP (report) |
| YEAR | Four-digit year of creation | 2012, 2024, 2025, 2026 |
| SEQ | Sequential number within component-type-year | 001, 002, 370 |
| VERSION | Semantic version (major.minor) | v1.0, v2.0, v4.0 |

**Language suffix:** For translated documents, append \-\[LANG\] before the version: ERES-RG-2026-370-ES-v1.0.pdf

# **4\. SOMT Tagging Schema**

Every document in BRAINS receives SOMT metadata tags organized by the Three Governing Principles (SELF, OTHERS, FUTURE) as the organizational spine, per ERES TERMS \#47.

## **4.1 Required Tags**

| Tag Category | Description |
| :---- | :---- |
| **governing\_principle** | SELF | OTHERS | FUTURE (primary alignment) |
| **component** | Primary ERES subsystem (BERA, SOMT, GEAR, PlayNAC, SECUIR, BEC, etc.) |
| **era** | CyberRAVE (pre-1997), SaleBuilders (1997–2012), ERES (2012–present) |
| **clearance** | EP-0 (OPEN) | EP-1 (GATED) | EP-2 (RESTRICTED) | EP-3 (PRIVATE) |
| **status** | CANONICAL | SUPERSEDED | ARCHIVED | DRAFT |
| **format\_source** | Original file format before standardization (pdf, md, docx, html, txt) |
| **hash\_sha256** | SHA-256 hash of canonical file at time of ingestion |
| **timestamp\_verified** | VERIFIED | APPROXIMATE | UNVERIFIABLE |
| **supersedes** | ERES Document ID of the document this replaces (if applicable) |
| **keywords** | Free-form keyword list for search indexing |

# **5\. Manifest Structure**

The BRAINS manifest is the master index of the entire corpus. It is a single structured file (JSON or CSV) containing one row per canonical document. The manifest is the source of truth for what exists in BRAINS.

## **5.1 Manifest Fields**

Each entry contains: document\_id, title, filename, component, type, year, seq, version, clearance, status, governing\_principle, era, format\_source, format\_canonical, timestamp\_created, timestamp\_verified, hash\_sha256, supersedes, superseded\_by, keywords, byte\_size, and notes.

## **5.2 Manifest Operations**

**INGEST:** File passes all three Trifecta gates. Entry added to manifest. File placed in canonical directory structure.

**SUPERSEDE:** New version passes Trifecta. Old entry status changed to SUPERSEDED. Old entry receives superseded\_by pointer to new document\_id. New entry receives supersedes pointer to old document\_id.

**ARCHIVE:** Document removed from active query pool but retained in storage. Status changed to ARCHIVED. Reason recorded in notes field.

**DECLASSIFY:** Document clearance reduced (EP-2 → EP-1, or EP-1 → EP-0). Change logged with date and reason.

# **6\. Directory Structure**

The canonical BRAINS corpus is organized by component, not by date or format. Each component directory contains all canonical documents for that subsystem.

**BRAINS/**

├── manifest.json

├── TERMS/

├── BEC/

├── SPT/

├── COVENANT/

├── SCALULAR/

├── HAGUE/

├── ESVRD/

├── DOFA/

├── GSSG/

├── BRAINS/

├── FRAMEWORK/

├── OUTREACH/

├── \_ARCHIVE/

└── \_QUARANTINE/

**\_ARCHIVE:** Superseded and archived documents, organized by component subdirectories mirroring the main structure.

**\_QUARANTINE:** Documents that failed one or more Trifecta gates. Held for review, repair, or rejection.

# **7\. Phased Implementation**

## **Phase 1: Inventory (Thumb Drives → Raw Catalog)**

Mount both thumb drives. Generate complete file listing with paths, sizes, formats, and filesystem timestamps. Produce a raw inventory CSV. Estimated scope: 2GB+, hundreds to thousands of files across PDF, MD, DOCX, HTML, and miscellaneous formats.

## **Phase 2: Triage (Raw Catalog → Trifecta Processing)**

Process each file through the three Trifecta gates. Identify canonical versions. Classify clearance tiers. Verify timestamps. Assign ERES Document IDs. Files that pass all three gates enter the BRAINS corpus. Files that fail go to \_QUARANTINE with a reason code.

## **Phase 3: Indexing (Corpus → SOMT Metadata)**

Tag every canonical document with the required SOMT schema. Build the master manifest. Cross-reference documents against ERES TERMS \#47 for terminological consistency. Generate the keyword index for search.

## **Phase 4: Embedding (Corpus → Vector Database)**

Convert canonical documents to text chunks. Generate vector embeddings for semantic search. Load into a vector database (local or hosted). This is the layer that enables AI-powered corpus querying—BRAINS becomes able to reason about ideas and validate them against the SOUND criterion.

## **Phase 5: Serving (BRAINS → EarnedPath Access)**

Build the access layer. JAS gets full EP-3 access to the complete corpus through an AI interface. Subscribers get EP-0, EP-1, or EP-2 access based on their EarnedPath tier. Paywall integration (Stripe or equivalent) for paid tiers.

# **8\. Three Governing Principles Alignment**

**SELF (Don’t hurt yourself):** BRAINS protects Joseph’s work. No document enters the corpus in a corrupted, mislabeled, or unverified state. The Trifecta ensures every piece of the 14-year archive is preserved accurately, accessible reliably, and never lost to platform fragmentation again.

**OTHERS (Don’t hurt others):** Security-Clearance ensures sensitive materials are not served to unauthorized users. CCAL licensing on public-tier documents protects attribution. The clearance system prevents premature exposure of strategic documents while maintaining maximum openness for framework-level content.

**FUTURE (Build for generations to come):** The manifest, hash locks, and structured directory ensure the corpus can survive its creator. BRAINS is designed so that the work outlasts its originator—another person, another AI, or another institution can pick up the manifest and reconstruct the complete ERES corpus from its verified, authenticated, canonically organized state.

*"It's not mining — it's tuning."*

BRAINS ingests. SOMT organizes. GEAR remembers. BERA authenticates. EarnedPath serves.

**The Space-Body is ready to be built.**