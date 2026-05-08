# **ERES Attestation and Authorization Protocol (EAAP) v1.2**

## **Operational Attestation over the ERES Cryptographic Stack Primitive — Post-Quantum Migration and Determinism Guarantees**

**Author:** Joseph Allen Sprute (ERES Maestro)  
**Affiliation:** ERES Institute for New Age Cybernetics, Bella Vista, AR 72714  
**ORCID:** 0000-0001-9946-3221  
**Document ID:** ERES-EAAP-2026-001-v1.2  
**ResearchGate Slot:** 432  
**Date:** May 8, 2026  
**License:** CARE Commons Attribution License v2.1 (CCAL v2.1)

## ---

**Abstract**

The ERES Attestation and Authorization Protocol (EAAP) is the operational attestation layer that sits directly above the ERES Cryptographic Stack Primitive (v1.3, slot 431). EAAP v1.2 closes three lifecycle items deferred from earlier versions: (i) the post-quantum migration timeline with concrete ML-DSA and Falcon milestones; (ii) integer cross-multiplication as the determinism guarantee that eliminates IEEE 754 floating-point non-determinism in attestation comparison; (iii) a confirmed two-class attestation model (Class A pseudonymous, Class B anonymous). v1.2 is the version at which EAAP is locked as the attestation substrate for SCALULAR. The EAAP-POL JSON Schema and EAAP-CRL revocation registry are referenced as normative companions.  
**Keywords:** attestation, authorization, post-quantum cryptography, ML-DSA, Falcon, IEEE 754, integer cross-multiplication, SCALULAR, ERES Institute.

## **1\. Introduction**

EAAP makes the ERES Stack Primitive operational. Where the Primitive defines the *form* of attestable claims, EAAP defines the *protocol* by which those claims are issued, exchanged, verified, revoked, and re-validated under credential rotation. Versions 1.0 and 1.1 established the wire format, the EAAP-POL JSON Schema, and the EAAP-CRL revocation registry. Version 1.2 hardens the protocol against two adversaries: a quantum adversary in the medium term, and a determinism adversary in the immediate term.

## **2\. Post-Quantum Migration Timeline**

**2.1 Threat model.** EAAP assumes the eventual deployment of cryptographically relevant quantum computers (CRQC). The protocol must remain valid under transition without invalidating attestations issued under classical signature schemes during the migration window.  
**2.2 Primary migration target — ML-DSA.** The protocol's primary post-quantum signature target is ML-DSA (FIPS 204, Module-Lattice-Based Digital Signature Algorithm). ML-DSA is mandated for new EAAP deployments at version 1.2 and above; pre-1.2 deployments retain classical signatures under a sunset window.  
**2.3 Secondary target — Falcon.** Falcon (FIPS 206, draft) is supported as a secondary post-quantum signature scheme where signature size or verification cost is the constraining factor. Falcon attestations are interoperable with ML-DSA attestations under a joint verification policy declared in the EAAP-POL header.  
**2.4 Migration windows.** Three windows are defined:

* **Window A (immediate):** new attestations under v1.2+ deployments shall use ML-DSA or Falcon.  
* **Window B (parallel):** existing classical attestations remain valid under their original schemes; verifiers shall accept both classical and PQ schemes during this window.  
* **Window C (sunset):** classical attestations are accepted only with explicit verifier-side override and a logged provenance note. Window C closes when the Stewardship Council declares a CRQC threat threshold satisfied.

## **3\. Determinism Guarantee — Integer Cross-Multiplication**

**3.1 The IEEE 754 problem.** Attestation comparison frequently requires verifying that two BERA-derived scalars are equal, ordered, or proportionally related. If those scalars are represented as IEEE 754 floating-point values, the verification result becomes platform-dependent: ARM, x86, and GPU implementations of equivalent floating-point pipelines do not always produce bit-identical outputs.  
**3.2 The fix.** EAAP v1.2 forbids floating-point comparison in attestation verification. Where two ratios a/b and c/d must be compared, the comparison is performed via integer cross-multiplication (a · d vs. b · c) over arbitrary-precision integers. This is bit-deterministic on every platform and eliminates the floating-point non-determinism class entirely.  
**3.3 Implementation guidance.** Reference implementations shall use a vetted big-integer library; implementations are forbidden from silently downgrading to fixed-width integer arithmetic where overflow is possible.

## **4\. Two-Class Attestation Model**

EAAP v1.2 confirms the two-class model first proposed in MIEVM-PATCH-2026-001:

* **Class A — Pseudonymous attestation.** The attesting party is identified by a stable pseudonym bound to a CBGMODD seat. The pseudonym is unlinkable to legal identity without an out-of-band disclosure protocol, but is linkable across attestations.  
* **Class B — Anonymous attestation.** The attesting party is identified only by a freshly generated key, unlinkable across attestations. Class B attestations are admissible for receipts and acknowledgments but not for normative claims requiring R₇ (Right) under the Stack Primitive.

The class is declared in the EAAP-POL header and is bound into the signature input.

## **5\. EAAP-POL and EAAP-CRL**

**5.1 EAAP-POL JSON Schema.** The protocol policy header is a JSON object validated against the EAAP-POL JSON Schema. v1.2 adds fields for pq\_scheme, class, migration\_window, and determinism\_profile.  
**5.2 EAAP-CRL.** The revocation list is append-only, signed by the issuing CBGMODD seat, and verifiable independently of the attestation it revokes. Revocation under v1.2 may cite a determinism-class reason code where a pre-v1.2 attestation is found to depend on floating-point comparison.

## **6\. Position in the ERES Stack**

EAAP v1.2 sits:

* **Above:** ERES Cryptographic Stack Primitive v1.3 (slot 431).  
* **Below:** SCALULAR (HEALTH/SSHP, LAW/SSLA, PROTECTION/SSPS, SKILLS\_TRADE/SSST), Meritcoin Proof-of-Resonance, and the DOFA closed-loop receipts pipeline.

## **7\. Conclusion**

EAAP v1.2 is the version at which the protocol is locked for SCALULAR. The post-quantum migration is sequenced, the determinism class is closed, and the two-class attestation model is confirmed. Subsequent versions are expected to focus on cross-stack composition (interop with non-ERES attestation substrates) and on multi-Talonic attestations spanning more than one of the 126 governance states concurrently.

## **References**

1. Sprute, J. A. (2026). *ERES Cryptographic Stack Primitive v1.3.* ERES-CRYPTO-PRIMITIVE-2026-001-v1.3 (slot 431).  
2. NIST (2024). *FIPS 204: Module-Lattice-Based Digital Signature Standard.*  
3. NIST (2024). *FIPS 206 (draft): Falcon Digital Signature Algorithm.*  
4. Sprute, J. A. (2026). *MIEVM-PATCH-2026-001.* ERES Institute.  
5. Sprute, J. A. (2026). *ERES UBIMIA Manual v1.1.* ERES Institute.

---

*© 2026 Joseph Allen Sprute / ERES Institute. Released under CARE Commons Attribution License v2.1 (CCAL v2.1). Attribution required; derivatives must propagate the license.*