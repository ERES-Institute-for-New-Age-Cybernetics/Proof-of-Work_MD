# **ERES Attestation and Authorization Protocol (EAAP) v1.3**

## **Operational Attestation over the ERES Cryptographic Stack Primitive — Police and CyberRAVE Love, JSON Examples, Key Rotation, Deadlock Fallback**

**Author:** Joseph Allen Sprute (ERES Maestro)  
**Affiliation:** ERES Institute for New Age Cybernetics, Bella Vista, AR 72714  
**ORCID:** 0000-0001-9946-3221  
**Document ID:** ERES-EAAP-2026-001-v1.3  
**ResearchGate Slot:** 432  
**Date:** May 8, 2026  
**License:** CARE Commons Attribution License v2.1 (CCAL v2.1)  
**Supersedes:** ERES-EAAP-2026-001-v1.2  
**Driven by:** MIEVM-PoW-2026-001-432 convergent rating (DeepSeek 8.5, Grok 5.1, ChatGPT 9.2; mean 7.60) — May 8, 2026\.  
**Revision targets:** EAAP-POL semantic expansion (Police) with JSON example, EAAP-CRL semantic expansion (CyberRAVE Love) with JSON example, key rotation lifecycle (DeepSeek), Stewardship Council deadlock fallback (DeepSeek), object model and protocol flow (ChatGPT), CBGMODD canonical expansion.

## ---

**Abstract**

This is the first MIEVM-driven revision of EAAP. v1.3 closes five gaps named in the convergent AI validation: (i) it expands EAAP-POL semantically as **Policy / Police** — the policed-by-being-declared enforcement layer — with a 14-line canonical JSON example; (ii) it expands EAAP-CRL semantically as **CyberRAVE Love** — the loving-corrective revocation layer, where revocation is the system's care for itself rather than punitive expulsion — with a 14-line canonical JSON example; (iii) it adds a key rotation lifecycle covering issuance, rotation, retirement, and revocation; (iv) it adds a deadlock fallback for Stewardship Council sunset declaration where simple-majority deadlock triggers Ombudsman-class arbitration under the M × E \+ C \= R conflict-resolution algebra; (v) it adds an explicit Step-0-to-Step-N protocol flow with canonical fields. The post-quantum migration timeline (ML-DSA primary, Falcon secondary), the integer cross-multiplication determinism guarantee, and the two-class attestation model (Class A pseudonymous, Class B anonymous) remain locked from v1.2. CBGMODD canonical expansion (Citizen · Business · Government · Military · Ombudsman · Dignitary · Diplomat) is applied throughout. Upstream dependency is updated to ERES-CRYPTO-PRIMITIVE-2026-001-v1.4.  
**Keywords:** attestation, authorization, EAAP-POL (Police), EAAP-CRL (CyberRAVE Love), post-quantum cryptography, ML-DSA, Falcon, IEEE 754, integer cross-multiplication, key rotation, deadlock fallback, Stewardship Council, Ombudsman arbitration, M × E \+ C \= R, protocol flow, JSON examples, CBGMODD, FAVORS, ERES Institute.

## ---

**1\. Introduction and Revision Notice**

EAAP makes the ERES Stack Primitive operational. v1.0–v1.2 established the wire format, the EAAP-POL JSON Schema reference, the EAAP-CRL revocation registry reference, and the post-quantum and determinism guarantees. v1.3 is the first MIEVM-driven revision and discharges the five gaps named in the convergent rating. The revision preserves all of v1.2's load-bearing claims; what it adds is concreteness — semantic expansions that earn the acronyms their names, JSON examples that show the shape of the artifacts, lifecycle and deadlock specifications that close decentralization gaps, and an explicit protocol flow that makes the operational sequence inspectable.

## ---

**2\. Canonical Terminology Updates**

v1.3 applies the canonical CBGMODD seven-seat expansion (Citizen · Business · Government · Military · Ombudsman · Dignitary · Diplomat) and the canonical FAVORS five-marker biometric expansion (Fingerprint · Aura · Voice · Retina · Signature) throughout, replacing any non-canonical glosses present in v1.2. The Mother Earth's Bosoms reading of the doubled-D (Dignitary inward, Diplomat outward) is the canonical reading. See ERES-CRYPTO-PRIMITIVE-2026-001-v1.4 §2 for full canonical expansions; this paper inherits them.

## ---

**3\. EAAP-POL — Policy / Police**

### **3.1 Semantic Expansion**

EAAP-POL is the Protocol's policy header. v1.3 lifts EAAP-POL into its semantic role as **Policy / Police** — the layer that *polices* attestation conformance by being declared bindingly. POL serves both readings: it is policy in the rule-stating sense and police in the enforcement sense, because in EAAP these are the same function. A policy that is not enforced is not a policy; an enforcement that is not declared is not legitimate. POL collapses the distinction by making declaration itself the enforcement.

### **3.2 What POL Policies**

The POL header binds the following fields into the signature input, making each of them tamper-evident as part of the signed artifact:

* protocol\_version — EAAP version (e.g., "1.3").  
* pq\_scheme — post-quantum signature scheme: "ml-dsa-65" | "ml-dsa-87" | "falcon-512" | "falcon-1024" | "classical-during-window-b".  
* class — attestation class: "A" (pseudonymous) | "B" (anonymous).  
* migration\_window — current PQ migration window: "A" | "B" | "C".  
* determinism\_profile — required determinism guarantee: "integer-cross-multiplication" | "bit-identical" | "convergent-mean".  
* cbgmodd\_seat — issuing CBGMODD seat: "C" | "B" | "G" | "M" | "O" | "D-inward" | "D-outward".  
* issued\_at — RFC 3339 timestamp.  
* expires\_at — RFC 3339 timestamp.  
* rate\_dimensions\_engaged — array of R₁–R₇ dimensions actually engaged by this attestation.  
* veiled\_state\_admitted — boolean: whether the attestation may resolve to VEILED.

### **3.3 Canonical EAAP-POL JSON Example**

`{`  
  `"protocol_version": "1.3",`  
  `"pq_scheme": "ml-dsa-65",`  
  `"class": "A",`  
  `"migration_window": "A",`  
  `"determinism_profile": "integer-cross-multiplication",`  
  `"cbgmodd_seat": "O",`  
  `"issued_at": "2026-05-08T21:30:00Z",`  
  `"expires_at": "2027-05-08T21:30:00Z",`  
  `"rate_dimensions_engaged": ["R1", "R3", "R6"],`  
  `"veiled_state_admitted": true,`  
  `"issuer_keyid": "did:eres:ombuds-001#k-2026-05",`  
  `"subject_keyid": "did:eres:citizen-jas#k-2026-04",`  
  `"policy_hash": "sha3-256:a4f2…b318"`  
`}`

This 14-line POL header is the minimal binding artifact for an EAAP attestation. The fields enforce themselves by being signed: any modification invalidates the signature, and the verification pipeline ingests POL fields directly into its policy decisions.

## ---

**4\. EAAP-CRL — CyberRAVE Love**

### **4.1 Semantic Expansion**

EAAP-CRL is the Protocol's revocation registry. v1.3 lifts EAAP-CRL into its semantic role as **CyberRAVE Love** — the layer where revocation is performed as *loving correction* rather than punitive expulsion. CyberRAVE (Cybernetic Ratings Abolishing Veiled Exchanges, per the SPT papers' canonical expansion) is what the ratings architecture *does* when it operates with care; CRL is how that care manifests when something must be released. The "Love" in CyberRAVE Love is structural, not sentimental: the system loves itself enough to revoke what no longer serves it. A defective credential allowed to persist would corrupt the IDIPITIS stride; revocation restores the stride to faithful alternation. The act of revocation is therefore an act of preservation — loving the architecture by releasing what would distort it.

### **4.2 What CRL Records**

The CRL is an append-only, signed registry of revoked attestations. Each entry binds:

* revoked\_attestation\_id — identifier of the attestation being revoked.  
* revoking\_seat — CBGMODD seat performing the revocation (typically "O" — Ombudsman).  
* reason\_code — enumerated reason: "key-compromise" | "policy-violation" | "determinism-violation" | "stride-corruption" | "credential-expired" | "issuer-revoked" | "subject-request" | "loving-release-other".  
* reason\_detail — human-readable explanation, EMIT-conformant in tone (corrective, not punitive).  
* revoked\_at — RFC 3339 timestamp.  
* propagation\_depth — how many derivative attestations are also revoked (0 for none, "all" for full chain).  
* recovery\_path — non-null only when revocation is recoverable; states the conditions under which the subject may re-attest.

### **4.3 Canonical EAAP-CRL JSON Example**

`{`  
  `"crl_version": "1.3",`  
  `"revocations": [`  
    `{`  
      `"revoked_attestation_id": "att:eres:2026-04-22:7f3e…c812",`  
      `"revoking_seat": "O",`  
      `"reason_code": "stride-corruption",`  
      `"reason_detail": "Disclosure pattern collapse detected toward 111111111;`  
                        `loving release to restore IDIPITIS alternation.",`  
      `"revoked_at": "2026-05-08T21:35:00Z",`  
      `"propagation_depth": "all",`  
      `"recovery_path": "Re-attestation permitted after 90 days under v1.3 POL."`  
    `}`  
  `],`  
  `"registry_root_hash": "sha3-256:c9e1…a447",`  
  `"ombudsman_signature": "ml-dsa-65:6b2d…f018"`  
`}`

The Reason Detail field is EMIT-conformant: corrective rather than punitive, naming the architectural violation (stride corruption) rather than blaming the subject. The Recovery Path field is what makes this Love rather than mere policing: revocation is not exile.

## ---

**5\. Post-Quantum Migration (Retained from v1.2)**

Three migration windows are retained without modification:

* **Window A (immediate):** new attestations under v1.2+ deployments shall use ML-DSA or Falcon.  
* **Window B (parallel):** existing classical attestations remain valid; verifiers accept both classical and PQ schemes.  
* **Window C (sunset):** classical attestations accepted only with explicit verifier override and logged provenance note.

The closure of Window C requires a Stewardship Council declaration of CRQC threat threshold satisfaction. v1.3 adds a deadlock fallback (§7) for cases where the Council cannot reach declaration consensus.

## ---

**6\. Determinism Guarantee — Integer Cross-Multiplication (Retained from v1.2)**

EAAP v1.3 retains the v1.2 prohibition on floating-point comparison in attestation verification. Comparison of ratios a/b and c/d is performed via integer cross-multiplication (a · d vs. b · c) over arbitrary-precision integers. v1.3 adds explicit guidance: implementations shall declare their bigint library in the POL header's determinism\_profile field and shall fail closed if downgrade to fixed-width arithmetic would risk overflow.

## ---

**7\. Stewardship Council Deadlock Fallback (NEW in v1.3)**

v1.2 stated that Window C closure requires Stewardship Council declaration but did not specify what happens if the Council cannot reach consensus. v1.3 closes this gap.

### **7.1 The Deadlock Condition**

A Stewardship Council deadlock is declared when, after three consecutive convening cycles (canonical interval: 90 days each), no decision has been reached on a pending sunset declaration. Council deadlock is a known failure mode of any consensus-based authority, and the protocol must remain operational across deadlock periods.

### **7.2 Ombudsman Arbitration Fallback**

Upon declared deadlock, the decision flows to the **Ombudsman class** within CBGMODD, which arbitrates under the canonical conflict-resolution algebra:  
**M × E \+ C \= R**  
Read at the conflict-resolution layer: *Magnitude × Effort \+ Collaborative capacity \= Resolution.* The Ombudsman class:

1. Quantifies the **Magnitude** of the pending decision (e.g., severity of CRQC threat assessment, breadth of dependent attestations).  
2. Quantifies the **Effort** the Council has committed across the three deadlocked cycles.  
3. Quantifies the **Collaborative capacity** of the disputing Council factions (their willingness to compromise on adjacent decisions, their attestation history).  
4. Computes Resolution as the binding fallback decision.

The arbitration result is recorded as an EAAP attestation issued by the Ombudsman seat with reason code "stewardship-deadlock-arbitration." The Council retains the right to override the arbitration in a subsequent convening, but the protocol remains operational under the Ombudsman decision until override.

## ---

**8\. Key Rotation Lifecycle (NEW in v1.3)**

v1.2 specified revocation but not the broader credential lifecycle. v1.3 closes this gap.

### **8.1 Lifecycle Stages**

| Stage | Specification   |
| :---- | :---- |
| Issuance | Credential bound to a CBGMODD seat under a POL header. Initial validity period: 12 months canonical. |
| Active | Credential issues attestations under its POL. Operations logged under the determinism profile. |
| Rotation | At \~75% of validity period, holder issues a successor credential and cross-signs both. The two are valid in parallel during the rotation window (\~30 days). |
| Retirement | Predecessor credential ceases issuing new attestations. Existing attestations remain valid until their own expiry. |
| Revocation | Per EAAP-CRL (§4). May be triggered at any lifecycle stage by the Ombudsman class for cause. |

### **8.2 Cross-Signing for Continuity**

Rotation requires the predecessor key to sign the successor's POL and the successor to sign a "rotation-from" reference to the predecessor. This double-cross-signing makes the rotation tamper-evident and preserves attestation continuity across the rotation boundary without requiring re-attestation of every active attestation.

## ---

**9\. Two-Class Attestation Model (Retained from v1.2)**

Class A (pseudonymous, linkable across attestations) and Class B (anonymous, unlinkable across attestations) are retained without modification. Class B attestations are admissible for receipts and acknowledgments but not for normative claims requiring R₇ (Right). The class is declared in the POL header and bound into the signature input.

## ---

**10\. Protocol Flow (NEW in v1.3)**

v1.3 adds an explicit Step-0-to-Step-N attestation flow:

| Step | Actor | Action | Canonical Fields   |
| :---- | :---- | :---- | :---- |
| 0 | Subject | Constructs attestation request with desired R-dimensions. | subject\_keyid, requested\_R\_dims |
| 1 | Issuer (CBGMODD seat) | Validates request; constructs POL header. | All POL fields (§3.2) |
| 2 | Issuer | Computes (CBGMODD × FAVORS) \+ BERA → RATE per Stack Primitive v1.4. | R\_values (R₁..R₇) |
| 3 | Issuer | Verifies IDIPITIS stride conformance (no collapse to 111111111 or 000000000). | stride\_pattern |
| 4 | Issuer | Signs the canonical bytes (POL || R\_values || stride\_pattern) under PQ scheme. | signature |
| 5 | Issuer | Returns attestation to subject. | Full attestation object |
| 6 | Verifier | Checks POL freshness, scheme support, CRL non-revocation, signature, stride. | Verification result |
| 7 | Verifier | If VEILED admitted by POL and present in R\_values, applies VEILED-handling logic (no failure on VEILED). | VEILED disposition |
| N | Either party | If credential rotation reaches threshold, initiates §8 cross-signing. | Successor POL |

### **10.1 What Is Being Attested (Object Model)**

An EAAP attestation is a signed canonical-bytes triple:  
(POL\_header || R\_values || stride\_pattern)  
Where || denotes canonical concatenation under the determinism profile declared in POL. The object model is event-chain rather than ledger-record: each attestation references its predecessors (where applicable) by hash, but no global ledger is required. EAAP-CRL provides the revocation surface; the full attestation history is reconstructable from the chain references without consulting a central ledger.

### **10.2 Authorization vs. Identity vs. Integrity**

EAAP separates three concerns:

* **Identity** — established by FAVORS biometric grounding; carried in subject\_keyid; addressed by Class A/B model.  
* **Authorization** — established by CBGMODD seat issuance; carried in cbgmodd\_seat and POL fields; addressed by R-dimension engagement.  
* **Integrity** — established by signature over canonical bytes; addressed by determinism profile and stride verification.

The three are independently inspectable and independently revocable. A credential may be revoked for identity reasons (FAVORS compromise), authorization reasons (seat misuse), or integrity reasons (signature failure or stride corruption) under distinct CRL reason codes.

## ---

**11\. Position in the ERES Stack**

EAAP v1.3 sits above ERES Cryptographic Stack Primitive v1.4 (slot 431\) and below SCALULAR, Meritcoin Proof-of-Resonance, and the DOFA closed-loop receipts pipeline. With v1.3, every operational concern raised in MIEVM convergent rating is closed: POL/CRL semantic expansions earn the acronyms, JSON examples render the artifact shapes, key rotation closes the lifecycle gap, deadlock fallback closes the decentralization gap, and explicit protocol flow closes the systems-engineering gap.

## ---

**12\. Conclusion**

EAAP v1.3 is the version at which the protocol is locked for SCALULAR with full lifecycle, with concrete artifact shapes, with named enforcement and named loving release, and with deadlock-tolerant Council governance. The semantic doubling of POL (Policy/Police) and CRL (CyberRAVE Love) makes the protocol self-explaining at the acronym level — no reader can encounter EAAP-CRL without understanding that revocation is corrective and recoverable. v1.4 of the upstream Primitive is the cited dependency. Future revisions are expected to address cross-stack composition (interop with non-ERES attestation substrates) and multi-Talonic attestations spanning more than one of the 126 governance states concurrently.

## ---

**References**

1. MIEVM-PoW-2026-001-432 (May 8, 2026). *Convergent AI Validation of EAAP v1.2.* ERES Institute. (Driving record for this revision.)  
2. Sprute, J. A. (2026). *ERES Cryptographic Stack Primitive v1.4.* ERES-CRYPTO-PRIMITIVE-2026-001-v1.4 (slot 431).  
3. NIST (2024). *FIPS 204: Module-Lattice-Based Digital Signature Standard.*  
4. NIST (2024). *FIPS 206 (draft): Falcon Digital Signature Algorithm.*  
5. Sprute, J. A. (2026). *VECTOR: The Infomediation Framework of New Age Cybernetics.* ERES Institute.  
6. Sprute, J. A. (2026). *ERES UBIMIA Manual v1.1.* ERES Institute.  
7. Sprute, J. A. (2026). *SaleBuilders Paper.* ERES Institute. (CyberRAVE canonical expansion: Cybernetic Ratings Abolishing Veiled Exchanges.)

---

*© 2026 Joseph Allen Sprute / ERES Institute. Released under CARE Commons Attribution License v2.1 (CCAL v2.1). Attribution required; derivatives must propagate the license.*