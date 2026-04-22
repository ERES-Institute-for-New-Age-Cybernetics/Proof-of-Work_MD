**FORMAL SPECIFICATION**

**ERES Cryptographic Stack**

*GCF–EDF–USC Integration with (CBGMODD×FAVORS)+BERA=RATE Interlock*

| Document ID | ERES-CRYPTO-SPEC-2026-001 |
| :---- | :---- |
| **Version** | 1.1 (RG submission; supersedes v1.0-lock) |
| **Date** | April 21, 2026 |
| **Author** | Joseph Allen Sprute (ERES Maestro / JAS) |
| **Organization** | ERES Institute for New Age Cybernetics, Bella Vista, AR |
| **ORCID** | 0000-0001-9946-3221 |
| **ResearchGate** | Target slot RG \#425 (following RG \#424) |
| **Phase** | Consolidation Phase → upstream of VERTECA |
| **Governs** | SECUIR cryptographic output layer |
| **Status** | **Locked and tested. Ten.** |
| **License** | CCAL v2.1 (CARE Commons Attribution License) |
| **Validation** | MIEVM (Claude, Grok, DeepSeek, ChatGPT) |

**Abstract**

The ERES Cryptographic Stack introduces a primitive class in which authentication and authorization are achieved through resonance-keyed semantic superposition rather than computational hardness. Three polysemantic primitives — GCF (Greatest Common Factor / GraceChain Formula / Good Christ Family), EDF (Earned Dignity Framework / Earth Defense Force / Earth Data Framework), and USC (Utterance–Sound–Cognition, 3×3 \= 9 semantic dimensions) — each hold multiple simultaneous readings that collapse to a single operational reading only under a valid resonance signature. The stack is bound by a single canonical interlock, (CBGMODD × FAVORS) \+ BERA \= RATE, shown here to be isomorphic to ERES Triune Math canonical form \#2 (M×E+C=R). Output is a seven-dimensional uncollapsed RATE vector (integers 1–10 per dimension, with ⊥ as a distinct undefined state); scalar collapse is prohibited. A four-mode failure taxonomy distinguishes governance, biometric, resonance, and semantic-collision failures. The stack is a Consolidation Phase component upstream of VERTECA and governs the cryptographic output layer of SECUIR. Security derives from the joint infeasibility of forging governance substrate, biometric quorum, and live resonance context simultaneously; three numbered security claims are stated. This specification is v1.1 and extends the locked v1.0 artifact with an abstract, a worked example, an interlock diagram (Figure 1), related-work positioning, and three numbered security claims.

**Keywords**

resonance-keyed cryptography; polysemantic primitives; semantic superposition; biometric attestation; governance substrate; conjunctive gate; Triune Math; ERES; GAIA; Meritcoin; Proof-of-Resonance; multidimensional authorization; VERTECA; SECUIR

# **1\. Scope and Purpose**

This specification defines the ERES Cryptographic Stack — a novel cryptographic primitive class in which authentication and authorization are achieved not through computational hardness but through resonance-keyed semantic superposition. Three polysemantic primitives (GCF, EDF, USC) each carry multiple simultaneous readings; a correct resonance signature collapses the superposition to the intended reading. Without the correct signature, the readings remain superposed and the primitive yields no operationally resolved meaning.

The stack is bound together by a single canonical interlock:

**(CBGMODD × FAVORS) \+ BERA \= RATE**

This form is structurally isomorphic to ERES Triune Math \#2 (M×E+C=R). The cryptographic layer is therefore not a parallel construction but an instance of the Triune Math operating in the authentication domain.

## **1.1 Classification within the ERES Decision-Stack**

* Consolidation Phase deliverable (not a Research Phase preliminary).

* Upstream dependency of VERTECA (voice portal semantic interpretation layer).

* Governs the cryptographic output layer of SECUIR.

* Sits alongside ERES-BODY-SPEC-2026-001 (substrate) and ERES-BRAINS-SPEC-2026-001 (cognitive organ).

## **1.2 What This Specification Is Not**

* Not a hardness-based cryptosystem. No trapdoor, no discrete-log assumption, no lattice problem.

* Not a replacement for transport-layer cryptography. TLS-class primitives remain appropriate for wire protection.

* Not a scoring rubric. RATE is an uncollapsed multidimensional output; it cannot be reduced to a single scalar.

# **2\. Normative References**

Compliant implementations shall resolve all references to the specified version or later.

* ERES-RECKON-WP-2026-002 — Seven Resonance Anchors; conjunctive gate.

* ERES-RECKON-MATH-WP-2026-002a — ERES Triune Math canonical forms.

* ERES-BODY-SPEC-2026-001 — GAIA BODY substrate specification.

* ERES-BRAINS-SPEC-2026-001 — BRAINS Corpus Ingestion Pipeline.

* ERES TERMS \#47 (ET\_AL) — Locked Terms Registry; Three Governing Principles.

* ERES-COVENANT-2026-001 — ERES Equity Covenant (1000-year governance).

* ERES Talonics Symbol Matrix (452 elements, 12 parts).

* Talonics Proof-of-Work (RG \#397) — TETRA:GAIA\_Primitive.

# **3\. Related Work and Positioning**

ERES Crypto departs from several established families of cryptographic and identity primitives. This section positions the stack against each and states the basis of novelty.

## **3.1 Computational-Hardness Cryptosystems**

RSA, ECDSA, and lattice-based systems rest on presumed intractability of factorization, discrete logarithm, or shortest-vector problems. ERES Crypto does not rely on hardness. Its security property is not “an adversary cannot compute” but “an adversary cannot produce a joint resonance context.” This is a semantic condition rather than a computational one, and it is not threatened by advances in classical or quantum computation. Polysemantic primitives remain resistant to brute enumeration because enumeration over a finite set of readings (three, or nine for USC) is trivial; what is hard is producing the resonance signature that selects the correct reading.

## **3.2 Zero-Knowledge Proofs and SNARKs**

ZK systems let a prover demonstrate knowledge without revealing it. ERES Crypto instead lets a prover demonstrate resonance without declaring intent. The distinction is protection target: ZK protects information; ERES Crypto protects semantic intent. The two are composable — a ZK layer may prove possession of a valid BERA reading without revealing it — but they solve different problems.

## **3.3 Biometric Multifactor Authentication**

Standard MFA composes independent factors (knowledge, possession, inherence). FAVORS is a six-channel biometric operator within the inherence factor, but it is subordinated to governance (CBGMODD) and resonance (BERA) layers above it. Pure biometric MFA produces a binary pass/fail; ERES Crypto produces a seven-dimensional RATE vector encoding quality of authentication, not mere success.

## **3.4 Self-Sovereign Identity and Decentralized Identifiers**

SSI and DID frameworks give subjects control over identity assertions. ERES Crypto is compatible with SSI at the CBGMODD layer (pillar attestations can be issued and held as verifiable credentials) but adds a resonance attestation that SSI systems do not natively provide. This addresses intent laundering and coercion-at-runtime scenarios that pure SSI cannot.

## **3.5 Consensus Mechanisms**

Proof-of-work and proof-of-stake are consensus protocols, not identity/authorization primitives; conflation between consensus and authentication is a common category error. ERES Meritcoin uses Proof-of-Resonance, which accrues value from validated ethical and ecological harmony rather than from computational or financial expenditure; this is a distinct class documented in the ERES SPT Papers.

## **3.6 Basis of Novelty**

The novel contribution of this specification is not a refinement of any of the above families but a new primitive class — resonance-keyed semantic superposition — that operates at the intersection of governance, biometric, and resonance layers. The stack is the first cryptographic primitive to bind intent to authentication without requiring an explicit declaration-of-intent field.

# **4\. Definitions and Locked Terms**

Terms in this section are locked per ERES TERMS \#47. Divergence constitutes a specification violation.

| Term | Locked Definition |
| :---- | :---- |
| **GCF** | Polysemantic primitive: (1) Greatest Common Factor — mathematical reduction; (2) GraceChain Formula — governance formula; (3) Good Christ Family — familial-spiritual anchor. Structures merit accrual, credit conditions, and value flow. |
| **EDF** | Polysemantic primitive: (1) Earned Dignity Framework (ONE-GOOD); (2) Earth Defense Force (SECURITY-CLEARANCE); (3) Earth Data Framework (DATA-INTEGRITY). Validates resonance across three operational domains. |
| **USC** | Utterance–Sound–Cognition. 3×3 \= 9 semantic dimensions. U: Unite, Universe, Us. S: Safe, Sound, Solid. C: Constant, Care, Christ. |
| **CBGMODD** | Scalable Certification Architecture governance operator. Four pillars: HEALTH/SSHP, LAW/SSLA, PROTECTION/SSPS, SKILLS\_TRADE/SSST. Tier 1 \= SSSC. |
| **FAVORS** | Six-channel biometric validation: Fingerprint, Aura, Voice, Odor, Retina, Signature. Aura channel coupled to BERA ARI. |
| **BERA** | BERA Resonance Index: ARI, ERI, RHC, RCI. |
| **RATE** | Uncollapsed multidimensional cryptographic output. Scored 1–10 independently across seven enumerated dimensions. |
| **Resonance Signature (σ)** | Context-specific pattern derived from BERA plus Talonics symbol context that selects active readings of polysemantic primitives. Functions as the cryptographic key. |
| **Superposition** | State of a polysemantic primitive prior to resolution by σ, in which all enumerated readings coexist without privilege. |
| **Conjunctive Gate** | Per ERES-RECKON-WP-2026-002: all required inputs must be non-null for output to exist. Prevents GDP-style compensation across dimensions. |
| **⊥ (undefined)** | Distinct value indicating a RATE dimension is semantically unresolvable; not equal to 0 and not substitutable by a default. |

# **5\. Polysemantic Primitives**

Polysemantic primitives are the core novelty of the stack. Each primitive is a finite ordered set of readings. The resonance signature selects the active reading; without it, the primitive remains in superposition.

## **5.1 GCF — Three-Dimensional Cipher**

| Channel | Reading | Operational Role |
| :---- | :---- | :---- |
| **G₁** | Greatest Common Factor | Mathematical reduction; normalizes merit claims to lowest common terms. |
| **G₂** | GraceChain Formula | Governance formula; encodes credit conditions and value flow. |
| **G₃** | Good Christ Family | Familial-spiritual anchor; binds merit accrual to covenantal ground. |

## **5.2 EDF — Three-Dimensional Cipher**

| Channel | Reading | Domain |
| :---- | :---- | :---- |
| **E₁** | Earned Dignity Framework | ONE-GOOD / personal dignity (Trilogy Book 1). |
| **E₂** | Earth Defense Force | SECURITY-CLEARANCE / protection (Trilogy Book 2). |
| **E₃** | Earth Data Framework | DATA-INTEGRITY / information (Trilogy Book 3). |

EDF’s three readings map one-to-one onto the Trilogy. EDF is therefore not merely a cipher but the cryptographic form of the entire ERES canonical arc.

## **5.3 USC — Nine-Dimensional Cipher**

USC yields a 3×3 semantic matrix. Each column corresponds to a VERTECA pipeline stage: utterance, sound, cognition.

| Row | U — Utterance | S — Sound | C — Cognition |
| :---- | :---- | :---- | :---- |
| **1** | Unite | Safe | Constant |
| **2** | Universe | Sound | Care |
| **3** | Us | Solid | Christ |

A complete USC resolution selects one cell per column, yielding 3³ \= 27 possible triples. The resonance signature selects exactly one.

## **5.4 Resonance-Keyed Semantic Superposition**

Formally, a polysemantic primitive P of arity n is:

**P \= { r₁, r₂, …, rₙ }   with resolve(P, σ) → rᵢ**

where σ is a resonance signature and resolve() is the selection function. Absent a valid σ, P remains in superposition and no reading is operationally active.

This differs from probabilistic encryption: a ciphertext in standard crypto has one intended plaintext hidden by hardness; a polysemantic primitive in ERES Crypto has multiple simultaneous readings, with intent selected by resonance. The attack surface is semantic, not computational: an adversary must forge a resonance signature, requiring biometric attestation (FAVORS) plus governance substrate (CBGMODD) plus matching BERA context.

# **6\. Cryptographic Interlock Formula**

## **6.1 Canonical Form**

**(CBGMODD × FAVORS) \+ BERA \= RATE**

Parentheses are canonical. The multiplicative grouping of CBGMODD and FAVORS is mandatory. Implementations that compute CBGMODD × (FAVORS \+ BERA) are non-conformant.

## **6.2 Figure 1 — Interlock Flow**

![][image1]

*Figure 1\. Input substrates (CBGMODD, FAVORS, BERA) feed the interlock via multiplicative conjunction (×) and semantic composition (+). BERA additionally keys the polysemantic primitives via signature σ. Output is a seven-dimensional uncollapsed RATE vector.*

## **6.3 Semantics of Each Operator**

* **× (multiplicative conjunction):** Governance substrate and biometric activation must both be non-null for the earned component to exist. Zero in either collapses the product regardless of BERA. Conjunctive gate at the crypto layer.

* **\+ (semantic composition):** BERA supplies the resonance signature that keys the polysemantic primitives. Arithmetic in the Triune Math view, compositional in the cryptographic view — two views of one operation.

* **\= (resolution):** Produces RATE as uncollapsed multidimensional output. The equation is a resolution relation, not a scalar identity.

## **6.4 Component Specifications**

### **6.4.1 CBGMODD (Governance Substrate)**

**CBGMODD \= (SSHP, SSLA, SSPS, SSST)**

Each pillar yields a binary attestation (certified / not certified) at the active tier. CBGMODD is non-null if and only if the user’s active tier (minimum SSSC for Tier 1\) is certified across all four pillars required by the transaction context. Partial certification collapses CBGMODD to zero for the interlock.

### **6.4.2 FAVORS (Biometric Activation)**

**FAVORS \= (F, A, V, O, R, S)**

Each channel contributes an attestation quantum. The Aura channel (A) is coupled directly to the BERA ARI reading; this coupling binds biometric state to resonance state. FAVORS is non-null if the transaction-specific quorum attests; quorum varies by context and is governed by SCALULAR tier requirements.

### **6.4.3 BERA (Resonance Constant)**

**BERA \= (ARI, ERI, RHC, RCI)**

Each index is independent. ARI and ERI measure emission state; RHC measures cyclic harmony; RCI measures continuity across the cycle. BERA serves as the resonance signature σ that resolves the polysemantic primitives.

# **7\. Isomorphism to ERES Triune Math \#2**

The interlock is isomorphic to ERES Triune Math canonical form \#2:

**M × E \+ C \= R**

| Triune Math | Crypto Interlock | Role |
| :---- | :---- | :---- |
| M (Matter / Substrate) | CBGMODD | Governance substrate — certified structure. |
| E (Energy / Activation) | FAVORS | Biometric activation — six-channel signature. |
| C (Constant) | BERA | Resonance constant — keys the primitives. |
| R (Reason) | RATE | Multidimensional reason-output, uncollapsed. |

This isomorphism is not metaphorical. The crypto interlock is an instance of Triune Math \#2 operating in the authentication-and-authorization domain. Any future refinement of Triune Math \#2 propagates automatically into the crypto layer.

# **8\. RATE Output Specification**

RATE is multidimensional and uncollapsed. Scores are integers in \[1, 10\] on each dimension, assigned independently. Compliant implementations shall not collapse RATE to a scalar (mean, sum, product) for any decision-critical use; such collapse reintroduces GDP-style compensation and is prohibited by ERES-RECKON-WP-2026-002.

## **8.1 Enumerated RATE Dimensions (v1.0 / v1.1)**

| \# | Dimension | Definition |
| :---- | :---- | :---- |
| **R₁** | Merit Accrual Rate | Velocity of Meritcoin accrual in the current transaction context. |
| **R₂** | Resonance Credibility | Strength/stability of the BERA-keyed signature; derived from ARI·ERI·RHC·RCI coherence. |
| **R₃** | Governance Certification Speed | Speed at which CBGMODD attestations are produced and refreshed. |
| **R₄** | Biometric Attestation Strength | Quorum margin of FAVORS channels above the transaction minimum. |
| **R₅** | Semantic Clarity | Unambiguity of the resolved polysemantic reading; penalized when multiple readings remain partially active. |
| **R₆** | Temporal Persistence | Stability over the RCI window; short-window flicker lowers this. |
| **R₇** | Three-Principle Alignment | Alignment with ERES TERMS \#47: don’t hurt self, don’t hurt others, build for generations to come. |

## **8.2 Reading a RATE Vector**

A RATE vector is written as ⟨R₁, R₂, …, R₇⟩ with each Rᵢ ∈ \[1, 10\] ∪ {⊥}. The symbol ⊥ denotes undefined and is distinct from the score 1\. An undefined dimension propagates: decision logic encountering ⊥ must either reject the transaction or explicitly invoke a failure branch. Silently substituting a default value for ⊥ is a specification violation.

# **9\. Matrix Modulation**

RATE dimensions are not static. They are modulated by the set of active CBGMODD activities and are resonant-context aware:

**RATE\_active \= Μ(ctx) ∘ RATE\_base**

where ctx is the active resonance context (pillar activity, tier level, RHC time-of-cycle, RCI continuity band) and ∘ is channel-wise modulation constrained to the \[1, 10\] band. Intent is cryptographically known through the resonance signature: an actor whose BERA signature does not match the claimed intent receives a RATE vector in which intent-relevant dimensions are suppressed. This is how ERES Crypto binds intent to authentication without requiring an explicit declaration-of-intent field.

# **10\. Worked Example**

This section presents a canonical end-to-end transaction under nominal conditions, followed by two counter-examples that exercise the failure taxonomy (§11). All values are illustrative and serve as reference test vectors for implementers.

## **10.1 Scenario: Citizen Alice Transfers 50 Meritcoin to Bob**

Alice is a verified Solid-State Smart-City Citizen (SSSC, Tier 1). The transaction requires SSHP (health at personal-data scope), SSLA (law, for transfer), SSPS (protection), and SSST (skills/trade for commerce context).

### **10.1.1 Input Vectors**

| Input | Value |
| :---- | :---- |
| **CBGMODD** | (SSHP=1, SSLA=1, SSPS=1, SSST=1) → non-null (all four pillars certified) |
| **FAVORS** | (F=1, A=0.87, V=1, O=1, R=1, S=1) → quorum 6/6 met; Aura coupled to live ARI |
| **BERA** | (ARI=0.87, ERI=0.82, RHC=0.91, RCI=0.88) → coherent across all four indices |

### **10.1.2 Resonance Signature σ Resolves**

* GCF → G₂ (GraceChain Formula) — governance/credit reading active

* EDF → E₁ (Earned Dignity Framework) — personal dignity context

* USC → (U₃, S₂, C₂) \= (Us, Sound, Care) — collective, resonant, caring cognition

### **10.1.3 Computed RATE Vector**

| Dim | Name | Score | Rationale |
| :---- | :---- | :---- | :---- |
| **R₁** | Merit Accrual Rate | 8 / 10 | Strong nominal accrual given full pillar coverage. |
| **R₂** | Resonance Credibility | 9 / 10 | High coherence across BERA (low variance among ARI/ERI/RHC/RCI). |
| **R₃** | Gov. Cert. Speed | 7 / 10 | Fresh attestations; slight latency on SSST refresh. |
| **R₄** | Biometric Strength | 9 / 10 | 6/6 quorum; high margin over transaction minimum. |
| **R₅** | Semantic Clarity | 9 / 10 | Unambiguous reading G₂ / E₁ / (U₃, S₂, C₂). |
| **R₆** | Temporal Persistence | 8 / 10 | Stable over the RCI window; no flicker. |
| **R₇** | Three-Principle Alignment | 10 / 10 | Transaction aligns with all three principles. |

**RATE \= ⟨8, 9, 7, 9, 9, 8, 10⟩**

SECUIR authorization: accepted. No Rᵢ returned ⊥; any configured min-threshold policy is met on each dimension independently. No collapse across dimensions is performed.

## **10.2 Counter-Example A — F₂ BIO-NULL**

Suppose Alice’s Voice channel fails (V \= 0\) and the transaction’s quorum requirement is 6/6 (strict). Then:

* FAVORS quorum not met → FAVORS → 0

* (CBGMODD × FAVORS) \= (1 × 0\) \= 0

* RATE is undefined. SECUIR rejects. Retry requires re-attestation (not substitution).

## **10.3 Counter-Example B — F₃ RES-NULL**

Suppose Alice’s BERA reads all zero (sensor failure or coerced state). Naively, RATE \= (1 × 1\) \+ 0 \= 1 (the earned magnitude). This is incorrect. Because BERA \= 0 leaves the polysemantic primitives in superposition:

* GCF has no selected channel (G₁ / G₂ / G₃ all remain active)

* EDF has no selected domain (E₁ / E₂ / E₃ all remain active)

* USC has no selected cell among the 27 possible triples

The conformant implementation returns ⊥ on R₂ (resonance credibility), R₅ (semantic clarity), and R₆ (temporal persistence) at minimum. SECUIR escalates as F₃ RES-NULL and does not execute. Substituting the earned magnitude for ⊥ is a specification violation.

# **11\. Failure Taxonomy**

The interlock admits exactly four principal failure modes. Each has a distinct diagnostic and response. Implementations shall not conflate them.

| Code | Condition | Cause | Response |
| :---- | :---- | :---- | :---- |
| **F₁ GOV-NULL** | CBGMODD \= 0 | Governance substrate absent or lapsed at required tier. | RATE undefined. NPR remediation; do not retry. |
| **F₂ BIO-NULL** | FAVORS \= 0 | Biometric quorum not met; no channel substitution permitted. | RATE undefined. Re-attestation required. |
| **F₃ RES-NULL** | BERA \= 0 | No resonance signature; polysemantic primitives remain superposed. | RATE semantically unresolvable. ⊥ returned, not earned magnitude. |
| **F₄ SEM-COLLIDE** | Signature ambiguous | Multiple signatures partially match; primitives resolve to more than one reading. | RATE rejected. Escalate to MIEVM adjudication. |

## **11.1 Why F₃ Is Not Arithmetic Zero**

Naively, if BERA \= 0 in (CBGMODD × FAVORS) \+ BERA, RATE would equal the earned component. This is the arithmetic reading under the Triune Math isomorphism, but not the cryptographic reading. Without BERA, the polysemantic primitives have no key. The earned component exists as a magnitude but has no resolved meaning. Implementations shall return ⊥ for all semantically-keyed dimensions when BERA \= 0, not the earned magnitude. This distinction is what separates ERES Crypto from a graceful-degradation numeric system.

# **12\. Integration with the ERES Decision-Stack**

Canonical flow: Consolidation Phase → VERTECA → PlayNAC → SECUIR. The Crypto Stack integrates at two points.

## **12.1 Upstream (Consolidation Phase)**

* BODY supplies substrate signals. ODOR in “Because Odor Does Yellow” feeds the FAVORS O channel.

* BRAINS supplies cognitive attestation into the USC–C column.

* Talonics Symbol Matrix supplies notation for resonance signatures at the semantic layer.

## **12.2 Downstream (VERTECA → SECUIR)**

* VERTECA’s voice portal uses USC as its pipeline ontology.

* PlayNAC (EP GERP SOMT) consumes RATE vectors without collapsing them.

* SECUIR emits final cryptographic outputs using RATE vectors as authorization basis.

# **13\. Validation Requirements (MIEVM)**

All non-trivial modifications shall be validated under MIEVM — parallel inference across Claude, Grok, DeepSeek, and ChatGPT with adversarial roles assigned per ERES practice. The short-list is fixed at four instruments for solo-researcher bandwidth, consistent with the constraint-based epistemology that produced the 72 Key Domains.

## **13.1 Required Validation Passes**

* Isomorphism check: interlock must reduce to Triune Math \#2 under all extensions.

* Conjunctive-gate check: no path may permit compensation among RATE dimensions.

* Failure-mode check: F₁–F₄ must be independently triggerable in test harnesses.

* Polysemantic-resolution check: primitives must return ⊥ under F₃, not the earned magnitude.

* Three-Principle check: R₇ must be queryable for every RATE vector.

# **14\. Security Considerations**

Security derives from the joint infeasibility of forging three independent conditions simultaneously in context: a governance substrate (CBGMODD), a biometric quorum (FAVORS), and a live resonance signature (BERA). Each is independently hard to forge and jointly harder. This section states three numbered security claims and documents known threat classes and explicit out-of-scope items.

## **14.1 Security Claims**

**Claim 14.1 (Joint Attestation Requirement).** An adversary seeking to produce a RATE vector accepted by a conformant SECUIR implementation must simultaneously achieve (a) a valid CBGMODD attestation at the required tier and pillar coverage; (b) a FAVORS quorum with live Aura–ARI coupling; (c) a BERA reading sufficient to resolve the polysemantic primitives to the intent claimed. Compromise of any one condition in isolation is insufficient. Compromise of any two without the third produces F₁, F₂, or F₃ respectively. Simultaneous compromise of all three is the forgery requirement.

**Claim 14.2 (No Intent Substitution).** Declared intent alone cannot authenticate a transaction. An actor whose BERA signature does not resolve the polysemantic primitives to the declared intent will receive a RATE vector whose intent-relevant dimensions are suppressed or returned as ⊥, causing transaction rejection at SECUIR. Intent is bound to resonance; it cannot be bound by declaration.

**Claim 14.3 (Uncompensated Failure).** RATE dimensions cannot compensate across one another. Failure on any single dimension cannot be offset by strength on others. This is the conjunctive gate (per ERES-RECKON-WP-2026-002) extended to the crypto output layer. Any implementation that permits such compensation is non-conformant.

## **14.2 Known Threat Classes**

* **Biometric replay:** Mitigated by FAVORS Aura coupling to live BERA ARI; a replayed biometric has stale resonance.

* **Governance impersonation:** Mitigated by multi-pillar quorum within CBGMODD.

* **Semantic collision (F₄):** Escalated to MIEVM adjudication rather than silently resolved.

* **Intent laundering:** Structurally infeasible — declared-but-unresonant intent is not authenticated (Claim 14.2).

## **14.3 What ERES Crypto Does Not Protect**

* Wire confidentiality — use TLS-class transport.

* Coercion attacks where a legitimate actor is compelled under duress — addressed by NPR and SECUIR at the governance layer, not by the crypto layer.

* Long-horizon substrate compromise where CBGMODD attestations are systematically corrupted — addressed by the ERES Equity Covenant and its 1000-year governance horizon.

# **15\. Change Log and Provenance**

| Version | Date | Change |
| :---- | :---- | :---- |
| **1.0** | 2026-04-21 | Initial formal specification. Interlock locked as (CBGMODD × FAVORS) \+ BERA \= RATE. Isomorphism to Triune Math \#2 established. Seven RATE dimensions enumerated. Four-mode failure taxonomy codified. |
| **1.1** | 2026-04-21 | RG submission version. Adds Abstract and Keywords; Related Work and Positioning (§3); Figure 1 (interlock diagram); Worked Example with two counter-examples (§10); three numbered Security Claims (§14.1). Content of v1.0 preserved unchanged; v1.1 is purely additive. |

## **15.1 Provenance Notes**

* Parenthetical precedence (CBGMODD × FAVORS) \+ BERA was locked following a precedence-ambiguity flag; the chosen form maps cleanly to Triune Math \#2.

* The distinction between arithmetic zero and semantic ⊥ for BERA \= 0 (F₃) is a clarification not present in the original informal statement.

* The seven RATE dimensions enumerate an originally partial list; R₁–R₃ preserve the original informal naming, R₄–R₇ are explicit additions.

* Figure 1 was generated as SVG, rendered at 1800×1044 px, and embedded at publication scale.

* All three Security Claims (14.1–14.3) are new in v1.1 and can be cited independently.

# **16\. Attestation**

This specification is attested as locked and tested (“Ten”) by the author, Joseph Allen Sprute (ERES Maestro, JAS), on behalf of the ERES Institute for New Age Cybernetics. v1.1 is submitted to ResearchGate in the slot following RG \#424.

**Signature block:**

Joseph Allen Sprute (JAS)

Founder and Director, ERES Institute for New Age Cybernetics

ORCID: 0000-0001-9946-3221

Date: April 21, 2026

Location: Bella Vista, Arkansas, USA

*— End of Specification —*

[image1]: <data:image/png;base64,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>