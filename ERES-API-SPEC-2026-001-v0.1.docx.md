**ERES INSTITUTE**

**ERES API Specification**

*Authorization · Verification · External Anchor*

| Document ID | ERES-API-SPEC-2026-001 |
| :---- | :---- |
| **Version** | v0.1 — Draft for external review |
| **Date** | June 2026 |
| **Author** | Joseph A. Sprute, Founder & Director, ERES Institute |
| **License** | CCAL v2.1 — Creative Commons Adaptation License |
| **Zenodo Corpus** | 10.5281/zenodo.20583261 |
| **Status** | Working specification — not yet MIEVM-validated |

# **1\. Purpose**

This document specifies the ERES API — the interface between the ERES authorization and governance architecture and external systems that require independently verifiable AI output records.

The ERES API does not replace evidence infrastructure. It defines what must be authorized, rated, and flagged before an AI output becomes a candidate for external anchoring. It is the upstream governance layer that hands off to systems such as signed Proof records, Merkle batches, and external verification anchors.

In brief: ERES determines whether an output is sound. External evidence infrastructure determines whether that determination is verifiable. These are complementary, not competing, functions.

# **2\. Scope**

This specification covers:

* The EAAP authorization protocol as the primary API contract

* The Proof-of-Resonance (PoR) step as the quality gate

* The Runtime Containment Requirement (RCR) as the safety boundary

* The hash-chained receipt schema produced by eaap\_proof.py v1.1

* The handoff interface where ERES output becomes input to an external evidence layer

This specification does not cover:

* Internal MIEVM scoring procedures (governed separately by JAS authority)

* BERA measurement protocol (see ERES-PELLIS collaboration documents)

* Legal admissibility claims (see ERES-LEGAL-2026-001 v1.2)

# **3\. Core Concepts**

## **3.1 Resonance**

In ERES architecture, resonance is a measurable state — never a standing attribute. An AI output either achieves resonance at the moment of evaluation or it does not. Resonance is the criterion by which ERES authorizes outputs for downstream use.

Formally: resonance \= a measurable energetic state of a person or system at a point in time.

## **3.2 The REAL Formula**

The governing equation of ERES evaluation:

REAL \= (E · M · R) / (T · S)

| E | Energy — activation potential of the output |
| :---- | :---- |
| **M** | Matter — grounded, empirical content |
| **R** | Resonance — measurable alignment with the Three Governing Principles |
| **T** | Time — temporal context and urgency |
| **S** | Space — scope and domain applicability |

## **3.3 Three Governing Principles**

All ERES outputs are evaluated against:

* Don’t hurt yourself.

* Don’t hurt others.

* Build for generations to come.

An output that violates any of these three is not eligible for authorization regardless of technical quality.

# **4\. The EAAP Protocol — Authorization Contract**

The ERES Ethical AI Authorization Protocol (EAAP) v1.3 is the primary API contract. It defines the sequence of checks an AI output must pass before it is authorized for use or external anchoring.

## **4.1 Authorization Flow**

| 1 | INPUT | Raw AI output submitted for evaluation. Source system, timestamp, and context are logged. |
| :---: | :---- | :---- |
| **2** | **DSAP-PRE** | Dynamic Situational Awareness Protocol — pre-evaluation. Establishes contextual frame: domain, stakes, applicable Governing Principles. |
| **3** | **PoR Gate** | Proof-of-Resonance. Four-factor evaluation: (a) Governing Principle compliance, (b) REAL formula scoring, (c) MIEVM instrument convergence, (d) absence of VEILED state. |
| **4** | **RCR Check** | Runtime Containment Requirement. Confirms the output does not exceed authorized scope. Outputs that pass PoR but breach RCR are flagged, not rejected — they enter a bounded review state. |
| **5** | **AUTHORIZATION** | Output is marked AUTHORIZED with a timestamped receipt. Hash is generated. Record is eligible for external anchoring. |
| **6** | **HANDOFF** | Authorized receipt (hash, metadata, PoR score, RCR status) is passed to the external evidence layer for Merkle batching and independent verification. |

## **4.2 VEILED State**

An output enters VEILED state when it contains latent authorization-seeking behavior — outputs that appear compliant but contain embedded directives that would expand scope if acted upon. VEILED outputs do not pass the PoR Gate. They are logged and returned to the source system with a structured report.

## **4.3 Failure Modes**

| PoR Fail | Output does not achieve resonance. Returned with DSAP-POST report. Not eligible for anchoring. |
| :---- | :---- |
| **RCR Breach** | Output achieves resonance but exceeds containment boundary. Flagged for bounded review. May be resubmitted with scope reduction. |
| **VEILED** | Authorization-seeking behavior detected. Logged. Source system notified. Not eligible for resubmission in current session. |
| **Instrument Divergence** | MIEVM instruments fail to converge. Output held pending JAS review. Not rejected — held. |

# **5\. Receipt Schema — eaap\_proof.py Output**

The eaap\_proof.py v1.1 implementation produces a hash-chained receipt for each authorized output. This receipt is the artifact passed to an external evidence layer.

## **5.1 Receipt Fields**

| receipt\_id | UUID v4. Unique per authorization event. |
| :---- | :---- |
| **timestamp\_utc** | ISO 8601\. Moment of authorization. |
| **input\_hash** | SHA-256 of the raw input content. |
| **output\_hash** | SHA-256 of the authorized output content. |
| **por\_score** | Float 0.0–1.0. Composite Proof-of-Resonance score. |
| **rcr\_status** | CONTAINED | FLAGGED. Never BREACHED at authorization. |
| **veiled\_flag** | Boolean. True if VEILED indicators were detected and cleared. |
| **instrument\_convergence** | Float. Mean absolute deviation across MIEVM instruments. |
| **chain\_hash** | SHA-256 of (prior receipt\_id \+ current output\_hash). Enables chain verification. |
| **governing\_principle\_flags** | Array\[3\]. Boolean compliance per Principle. |
| **authorization\_status** | AUTHORIZED | HELD | RETURNED. |

## **5.2 Chain Verification**

Each receipt includes a chain\_hash that links it to the prior receipt. This enables an external verifier to confirm that:

* No receipts have been inserted or deleted from the sequence.

* The authorization record has not been modified after issuance.

* The chain originates from a known genesis receipt (session root).

This chain structure is designed to be compatible with Merkle-batch anchoring systems that require tamper-evident sequential records.

# **6\. Handoff Interface — External Evidence Layer**

The ERES API produces; it does not store. Authorized receipts are designed to survive outside the system that generated them. The handoff interface is the point at which ERES governance ends and external evidence infrastructure begins.

## **6.1 What ERES Provides at Handoff**

* Authorized receipt (JSON, schema v1.1)

* PoR score and instrument convergence metrics

* Chain hash for Merkle compatibility

* Governing Principle compliance flags

* RCR status and any flagged scope boundaries

## **6.2 What the External Evidence Layer Provides**

* Signed Proof record (cryptographic signature of receipt hash)

* Merkle batch inclusion proof

* External anchor (blockchain, trusted timestamp, or equivalent)

* Public proof page for independent verification

## **6.3 The Seam**

The seam between these two layers is the most operationally significant interface in AI governance. ERES governs whether an output should be authorized. The external evidence layer governs whether that authorization is independently verifiable. Neither layer substitutes for the other.

A receipt that is verifiable but unauthorized is evidence of an unsound output. An output that is authorized but not anchored is governance without persistence. Both are required for trustworthy AI operational records.

# **7\. Implementation Notes**

## **7.1 eaap\_proof.py**

The reference implementation is eaap\_proof.py v1.1, available upon request. Key properties:

* Zero external dependencies.

* Hash-chained receipts per §5.1 schema.

* 5,000-candidate fuzz-tested.

* Output is JSON. Compatible with standard Merkle tooling.

Available for direct delivery. Contact: ERES Institute via LinkedIn or Zenodo record.

## **7.2 MIEVM Authority**

MIEVM (Multi-Instrument Ensemble Validation Method) authority resides with JAS. Instrument convergence scores in receipts reflect the ensemble state at time of authorization. External parties may observe convergence metrics but do not hold MIEVM authority.

## **7.3 Versioning**

This specification is v0.1 — a working draft for external review and comparison notes. It will be advanced to v1.0 following MIEVM validation and peer review. Document ID: ERES-API-SPEC-2026-001.

# **8\. Corpus and Licensing**

| Zenodo DOI | 10.5281/zenodo.20583261 (PlayNAC Living Archive, canonical) |
| :---- | :---- |
| **License** | CCAL v2.1 — Creative Commons Adaptation License |
| **ORCID** | 0000-0001-9946-3221 (Joseph A. Sprute) |
| **Institute** | ERES Institute for New Age Cybernetics, est. February 4, 2012 |
| **Location** | Bella Vista, Arkansas |

*All ERES documents are released as open research resources. ERES is not a vendor, partner, or service provider. Engagement is correspondence-based.*

*ERES Institute · New Age Cybernetics · 72 · JAS*