**ERES UBIMIA**

**Manual and Operational Pilot Guide**

*Reference Architecture for Trilogy-Ready Deployment*

| WHO  ·  WHAT  ·  WHERE  ·  WHEN  ·  WHY  ·  HOW  ·  WITH *the seven-question architecture of a complete reference* |
| :---: |

**Joseph Allen Sprute**

Founder and Director

*ERES Institute for New Age Cybernetics*

Bella Vista, Arkansas  ·  April 25, 2026

**Document Metadata**

| Document ID | ERES-UBIMIA-MANUAL-2026-001-v1.0 |
| :---- | :---- |
| **Title** | ERES UBIMIA Manual and Operational Pilot Guide |
| **Author** | Joseph Allen Sprute, Founder & Director |
| **Institute** | ERES Institute for New Age Cybernetics |
| **ORCID** | 0000-0001-9946-3221 |
| **Date** | April 25, 2026 |
| **License** | CARE Commons Attribution License v2.1 (CCAL) |
| **Status** | v1.0 — Final |
| **Pilot jurisdiction** | First location adopted by ERES — TBD |
| **Companion documents** | BRIEF / SUM / FULL (architectural treatments — separate) |
| **Trilogy relationship** | Reference architecture preceding ONE GOOD / SECURITY-CLEARANCE / DATA-INTEGRITY |

This Manual is released under the CARE Commons Attribution License v2.1. It exists to make UBIMIA deployable by communities that have decided to deploy it, and to make UBIMIA writable about by communities that have decided to write about it. The architecture described is freely available to humanity, without restriction, for any community willing to operate it in good faith and any author willing to engage with it honestly.

This Manual is a companion, not a substitute. The architectural treatments — BRIEF (one page), SUM (three pages), FULL (thirteen pages) — describe what UBIMIA is. This Manual describes how a deploying community would actually do it. The Trilogy that follows — ONE GOOD, SECURITY-CLEARANCE, DATA-INTEGRITY — argues why it matters. Three genres, one architecture.

**FOREWORD**

**The Rooster**

There is a chicken-and-egg problem at the heart of any sufficiently large architecture. The architecture describes the world the implementation will create; the implementation makes the architecture real; neither can be evaluated until the other exists. The way out is not to begin with either the chicken or the egg. It is to begin with the rooster — the document whose only purpose is to make the others possible.

This Manual is the rooster. UBIMIA, taken whole, is large enough that no single trade book can contain it, no single technical specification can deploy it, and no single policy paper can defend it. The published architectural treatments — the one-page brief, the three-page summary, the thirteen-page full treatment — answer what UBIMIA is at the level a reader can finish in one sitting. They are the egg the chicken will hatch from. The Trilogy that follows — ONE GOOD on personal liberation, SECURITY-CLEARANCE on institutional trust, DATA-INTEGRITY on technical verification — will be the chicken: three trade-book volumes that argue, dramatize, and recruit. The chicken needs the egg to hatch from, and the egg needs the chicken to be born from. The rooster is what makes both happen.

Concretely: this Manual answers the seven questions that a complete reference architecture must answer before either the architectural treatments can stand on their own as policy documents or the Trilogy can be written without inventing as it goes. Who is involved. What instruments are deployed. Where the work happens. When the cycles run. Why the constraints are constitutional. How the procedures execute. With what tools, budget, and infrastructure. The seven questions are arranged as Parts I through VII. Each part is operational rather than argumentative — the Manual does not persuade, it specifies.

The architectural treatments will continue to evolve as ERES doctrine matures. The Trilogy will be written over the years that follow this publication. This Manual sits between them. It does not aspire to be the last word on UBIMIA; it aspires to be the word that makes the next words easier to write. AD\_ON-AI \== UuuuuU — the human-and-AI composer works downstream from a settled architecture, not upstream of one. The Manual is what settles the architecture far enough downstream that the writing can proceed.

*— Joseph Allen Sprute, Bella Vista, Arkansas*

**How to Use This Manual**

The Manual has three primary audiences, and each has a different reading path.

## **If you are a deploying community**

Read Part I (WHO) and Part V (WHY) before any other part — they together define the constitutional commitments your community is making by adopting UBIMIA. If those commitments are not ones you can endorse, the rest of the Manual is not yet useful to you. Once Part I and Part V are settled, read Part IV (WHEN) for the deployment sequence, then Part VII (WITH) for what you will need to acquire, then return to Parts II, III, and VI for instruments, sites, and procedures. The first 90 days of deployment use Parts I, IV, V, and VII most heavily.

## **If you are an engineering team building UBIMIA-compliant systems**

Read Part II (WHAT) and Part VI (HOW) first. Part II carries the schemas that your code must accept and emit; Part VI carries the procedures your code must implement. Cross-reference against the normative dependencies — EAAP v1.3-FINAL and Separatrix Math v2 — for byte-level specifications the Manual summarizes but does not duplicate. Parts III and VII give you the deployment context your systems must operate within. Part V gives you the constraints that no implementation choice may violate.

## **If you are an author writing about UBIMIA**

Read the front matter and the Glossary, then read whichever Part contains the answer to the question you are trying to answer. The Manual is structured so that any given operational question routes to exactly one Part. If you are writing the Trilogy, the mapping is: ONE GOOD (BEST) draws primarily from Parts I, IV, V; SECURITY-CLEARANCE (SOUND) draws primarily from Parts II, III, VI; DATA-INTEGRITY (GOOD) draws primarily from Parts II, VI, VII. The Manual provides the substrate; the Trilogy provides the argument.

## **If you are an auditor, reviewer, or adversarial reader**

Read Part V (WHY) to identify the constitutional commitments the architecture makes; then read Parts II, IV, and VI to identify whether the operational specification holds those commitments. Discrepancies between Part V and any other Part are bugs in the Manual, not features; they should be reported as errata. The six open gaps tracked in the FULL architectural treatment (Section 9.2) are noted at the end of each relevant Part as Open Specifications, with the Manual's interim guidance for pilots.

## **Conventions used throughout**

* Three-profile sidebars show how each rule applies at three pilot scales: COOPERATIVE (population approximately 200), MUNICIPAL (approximately 10,000), and REGIONAL (approximately 250,000).

* Runbook blocks (sage green border) describe sequenced procedures whose steps must execute in order.

* Schema blocks (purple border) define formal record formats. Field types follow standard JSON Schema conventions.

* Callout panels (amber border) carry constitutional constraints — non-negotiable commitments that no deployment may relax.

* References to EAAP §X.Y or Separatrix Math §X.Y point to the published normative dependencies; this Manual summarizes but does not duplicate them.

**Glossary of Operational Terms**

Terms defined in the architectural treatments (BRIEF / SUM / FULL) are not redefined here unless their operational meaning differs from their architectural meaning. This glossary covers terms specific to deployment.

**Adopting Community —** The cooperative, municipality, region, or other recognized governance body that has decided to deploy UBIMIA. Distinct from a Pilot Jurisdiction, which is the legal-administrative entity within which the Adopting Community operates.

**Attestation Booth —** A physical or digital site at which a participant can submit a Claim, witness another participant's Claim, or interact with the verification stack. May be located within a community center, a co-op office, or a participant's home device.

**Authority of Record —** The body designated by the Adopting Community as responsible for a particular operational function. Different functions may have different Authorities of Record (e.g., the Trustee Registry's Authority of Record need not be the GAIA Council's Authority of Record).

**Bond —** A Meritcoin or Credit balance held in escrow as a guarantee against false attestation, false certification, or other rule violations. Slashed (forfeited) on verified violation.

**Calibration Window —** The period during which initial parameter values (BaseCost, θ, δ\_max, CR) are adjusted from defaults toward jurisdiction-specific values based on observed pilot data. Default duration: first 12 months of Phase 1\.

**Claim Object —** The signed JSON record submitted by a participant asserting they performed a specific action contributing to a measured resonance gain. Schema specified in Part II.

**Compassion Override —** A manual procedure by which the GAIA Council can authorize emergency SCALULAR access for a participant with insufficient Credit balance. Tracks toward the Compassion Allowance specification (Open Gap 6 in the FULL).

**Custody Triad —** The three-party encryption-key custody arrangement protecting sensitive contribution data. Specified in Part III.

**Deployment Day —** Day 0 of the deployment runbook, defined by the Adopting Community as the first day on which UBI distributions begin flowing through Gracechain. All Phase 1 sequencing dates are relative to Deployment Day.

**ERES Recognition —** The act by which ERES Institute formally acknowledges an Adopting Community as a UBIMIA pilot site. Carries no enforcement authority; provides reputational acknowledgement and access to the ERES MIEVM ensemble.

**Freshness Window —** The maximum time between an authorization record's issuance and its use, beyond which the record is STALE. Default: one RHC cycle.

**GAIA Council —** The human council component of GAIA. Composition specified in Part I, Chapter 3\.

**Genesis Bill —** The first annual Bill issued to a participant on or after their enrollment. Pro-rated to remaining months in the calendar year of enrollment.

**Operational Bond —** A Bond posted by an institution applying for Type C Verification authority. Distinct from a participant Bond.

**Participant of Record —** A person who has been admitted to UBIMIA participation under the Adopting Community's Recognition Rule. Distinct from a Resident, which is a legal-administrative status.

**Phase Boundary —** A point in the three-phase transition model at which the Adopting Community formally graduates from one Phase to the next. Each boundary has graduation gates specified in Part IV.

**Pilot Jurisdiction —** The legal-administrative entity within which the Adopting Community operates. May be coextensive with the Adopting Community (in the case of a sovereign cooperative) or distinct from it (in the case of a community within a larger municipality).

**Recognition Rule —** The Adopting Community's adopted policy defining who is a Participant of Record. Templates supplied in Part I, Chapter 1\.

**Reference Calibration —** The default values for parameters such as θ, δ\_max, BaseCost, and CR. Used as starting points; replaced by jurisdiction-specific values during the Calibration Window.

**Sealed-Room Custody —** The physical security arrangement protecting hardware key-management modules. Specified in Part III, Chapter 11\.

**Trustee —** A person designated by a participant as a recovery agent for that participant's Gracechain identity. Minimum three trustees per participant. Specified in Part I, Chapter 4\.

**Verification Authority —** The status that permits an institution to issue Type C Verifications. Conferred by the GAIA Council subject to a posted Operational Bond. Revocable for verified violation.

**PART I**

**WHO**

*Participants and Bodies*

 

*WHO answers the first question of any reference architecture: which persons and which bodies have which roles, with which standing, under which selection rules, with which terms, and with which procedures for entry, departure, and recall. Until WHO is settled, no deployment can begin. Part I supplies the templates a deploying community can adopt rather than invent.*

**CHAPTER 1**

**Participants of Record**

A Participant of Record is a person admitted to UBIMIA participation under the Adopting Community's Recognition Rule. This is the only P0 gap in the architectural treatment — the Recognition Rule cannot be specified globally because no single rule is appropriate to all jurisdictions. The Manual's role is to supply templates the Adopting Community can choose among, adapt, or replace, with the architectural commitments that any rule must honor.

## **1.1 What any Recognition Rule must honor**

Six commitments are constitutional and apply to every Recognition Rule, whatever its specific terms:

* Birth eligibility. UBI flows from birth. No work requirement is permitted at any age. A guardian receives the floor on behalf of a minor.

* Compassion floor. Persons present in the jurisdiction who do not meet the Recognition Rule receive emergency SCALULAR access — not UBI — under the Compassion Override. This is non-negotiable.

* Stateless inclusion path. The Recognition Rule must include a path for stateless persons that does not require state-issued documentation.

* Re-entry. A former Participant who departed and returns must have a defined re-entry path. The default decay is 50% of prior ΔR\_contributor at re-entry, with a 90-day continuous-residency requirement before full restoration.

* No revocation for non-compliance. Recognition cannot be revoked because a Participant fails to behave as the regime prefers. Revocation paths exist only for the four reasons specified in Part V, Chapter 14\.

* Public criteria. The Recognition Rule must be public, written, and changeable only through the procedures specified in Part V, Chapter 13\.

## **1.2 Three template Recognition Rules**

Three templates are provided, calibrated to the three pilot scales. Each is a complete, adoptable rule. A deploying community may adopt one, blend two, or write its own — provided the adopted rule honors the six constitutional commitments above.

### **Template A — Cooperative (membership-based)**

A Participant of Record is any person who: (a) has been admitted to membership in the Cooperative under the Cooperative's bylaws; (b) is at least one day old (birth-from-membership); and (c) has not been expelled from membership through the procedure specified in the bylaws. The Cooperative is the Authority of Record. Stateless inclusion: the Cooperative may admit any person presented by three existing members in good standing as their sponsor.

### **Template B — Municipal (residency-based)**

A Participant of Record is any person who: (a) has been physically present in the Pilot Jurisdiction for at least 183 days in the preceding twelve months, OR holds citizenship of the jurisdiction, OR has been enrolled by the Municipal Authority via biometric anchoring with at least one community sponsor; AND (b) is at least one day old. The Municipal Authority is the Authority of Record. Stateless inclusion: the Municipal Authority must accept enrollment via three independent community sponsors regardless of state-issued documentation status.

### **Template C — Regional (citizenship \+ residency)**

A Participant of Record is any person who: (a) holds citizenship of the Pilot Jurisdiction, OR has held residency for at least 365 consecutive days, OR has been enrolled by the Regional Authority via biometric anchoring with at least three independent community sponsors; AND (b) is at least one day old. The Regional Authority is the Authority of Record. Stateless inclusion: the Regional Authority must publish a stateless-inclusion procedure within 180 days of Phase 1 commencement; until that procedure is published, the GAIA Council may enroll stateless persons by direct order.

| COOPERATIVE  ·  N≈200 Template A is the default. Membership and Recognition coextend; expulsion procedures are bylaws-governed; sponsors are existing members. | MUNICIPAL  ·  N≈10,000 Template B is the default. Residency, citizenship, and enrollment paths coexist; Municipal Authority is the Authority of Record. | REGIONAL  ·  N≈250,000 Template C is the default. Citizenship is primary; residency and sponsored enrollment provide alternative paths; stateless-inclusion procedure is mandatory. |
| :---- | :---- | :---- |

## **1.3 Re-entry, departure, and dual recognition**

Departure is voluntary. A Participant of Record may, at any time, notify the Authority of Record of departure. Upon departure, UBI flow ceases, Meritcoin balance is frozen for five years, Credits balance is drawable for two years (subject to RPA pricing for any SCALULAR services consumed during transit), and the Participant's record is marked Departed.

Re-entry follows the default rule unless the Adopting Community specifies otherwise: 90 days of continuous residency under the Recognition Rule, after which prior ΔR\_contributor is restored at 50% of its departure value. Frozen Meritcoin balance is restored fully on re-entry within five years; expired after.

Dual recognition — the case of a person recognized by two adopting communities — is permitted only if both adopting communities have signed a Dual Recognition Compact specifying which is the primary Authority of Record for which functions. In the absence of a Compact, recognition by a second community automatically triggers departure from the first.

## **1.4 Authority of Record responsibilities**

Every Recognition Rule designates an Authority of Record. The Authority's responsibilities are:

* Maintain the public Participant Register, including current status (Active / Departed / Suspended).

* Process enrollment applications under the published Recognition Rule.

* Process departure notifications and update the Register accordingly.

* Coordinate with the Trustee Registry for identity recovery (Chapter 4).

* Publish quarterly Recognition Reports including: number of new Participants, number of departures, number of Compassion Override events, and number of pending applications.

* Submit to annual audit by the GAIA Council per Part VI, Chapter 17\.

The Authority of Record is not a court. It does not adjudicate disputes between Participants; that is the GAIA Council's role. Its operational role is custodial: maintain the Register, process the events that change the Register, and submit the Register to audit.

**CHAPTER 2**

**The MIEVM Ensemble**

The Multi-Instrument Ensemble Validation Method is the methodology that prevents EAAP Factor A\_M (the Anchor Product's MIEVM component) from being self-certified. It is also the methodology by which the architectural treatments and this Manual were produced. The ensemble is not a single tool; it is a constitution of multiple tools, with composition rules, rotation rules, and dissent procedures.

## **2.1 Why ensemble validation is required**

A single model lineage operating alone is vulnerable to four failure modes: training-data bias, alignment-objective drift, corporate-incentive capture, and silent compromise. Ensemble validation defeats all four because the failure of any one lineage does not propagate to the others — they were not trained on the same data, aligned for the same objectives, owned by the same corporate parent, or compromised by the same path.

DeepSeek's review of the architectural treatments specifically asked for the defense of the canonical four (Claude, ChatGPT, Grok, DeepSeek). The defense is: independence of training lineage, diversity of optimization objective, availability of API provenance, and capacity for adversarial review. No one of these properties is sufficient by itself; together, they describe a constitution rather than a vendor list.

## **2.2 The four properties an ensemble member must satisfy**

* **Independence of training lineage.** The lineage was trained on a substantively different corpus from at least two other ensemble members. A manipulation injected into one corpus does not propagate to the others.

* **Diversity of optimization objective.** The lineage was aligned toward a substantively different optimization target — different reward model, different constitutional document, different RLHF protocol. A drift in one alignment objective does not pull the others.

* **Availability of API provenance.** The lineage's outputs are obtainable through a public API with a documented version string, so that an attestation made today is reproducible by any auditor with API access. Closed-weight models without version-stable APIs cannot serve as ensemble members.

* **Capacity for adversarial review.** The lineage is operated by an organization willing to receive and process adversarial feedback — to acknowledge when its outputs are wrong, retract attestations under public scrutiny, and update its alignment in response. A lineage whose operator dismisses adversarial review cannot serve.

## **2.3 The canonical ensemble (April 2026\)**

As of April 2026, the canonical ensemble for ERES MIEVM operations consists of:

| Lineage | Operator | Training Independence | Alignment Objective | API Provenance | Adversarial Review |
| :---- | :---- | :---- | :---- | :---- | :---- |
| Claude | Anthropic | Distinct corpus | Constitutional AI | Stable, versioned | Active |
| ChatGPT | OpenAI | Distinct corpus | RLHF \+ spec | Stable, versioned | Active |
| Grok | xAI | Distinct corpus | Truth-seeking objective | Stable, versioned | Active |
| DeepSeek | DeepSeek AI | Distinct corpus | Open-weights base | Stable, versioned | Active |

The ensemble composition is not constitutional; the four properties are. As the model ecosystem evolves, lineages may join the ensemble (after demonstrating the four properties) or be retired from it (if they cease to satisfy any property). Concentration of the ensemble in a single corporate group is constitutionally forbidden — at least three of the four ensemble members must be operated by distinct organizations.

## **2.4 Erasure Completeness Ratio**

ECR is the metric by which ensemble convergence is measured. It is computed as the proportion of ensemble members concurring on a given attestation, weighted by depth of agreement (full text concurrence vs. surface concurrence). Production deployments require ECR ≥ 0.75 for high-confidence authorization. Pilot deployments may operate at ECR ≥ 0.60 during the Calibration Window, with the requirement rising to 0.75 at Phase 1 graduation.

## **2.5 Dissent procedure**

When the ensemble fails to converge — when ECR falls below the required threshold for an attestation — the attestation is held pending dissent review. Three outcomes are possible:

* Resolution by data. Additional input data resolves the disagreement; the dissenting lineage updates its attestation; ECR rises above threshold; the attestation proceeds.

* Resolution by escalation. The attestation is escalated to the GAIA Council for human-judgment resolution. The Council may either ratify a majority view, request further data, or refer the underlying procedure to the Open Specifications register.

* Documented standoff. No resolution is reached within the dissent review window (default: 30 days). The attestation is rejected; the procedure is flagged for revision; the underlying parameter or rule is reviewed by the Council in the next regular session.

Documented standoffs are not failures. They are the architecture working as designed: the ensemble has identified a question that single-lineage attestation would have answered incorrectly, and the question is now visible for the Council to address rather than buried in the attestation log.

**CHAPTER 3**

**GAIA Composition and the Council**

GAIA — the Governance and Amortization body — is the most important specification this Manual must close. The architectural treatments referred to GAIA throughout but did not define its composition; DeepSeek flagged this as the largest unclosed specification in the FULL. This Chapter supplies the definition.

| GAIA in one sentence GAIA is a hybrid governance body — an algorithmic core that executes deterministic rules, supervised by a human council selected by weighted lottery from active contributors, with strictly bounded override authority and full public logging on Gracechain. |
| :---- |

## **3.1 The algorithmic core**

The algorithmic core executes the deterministic rules of UBIMIA. Specifically, it computes:

* BaseCost(T) annual adjustments under the Section 14 formula in the FULL, with the 25% volatility cap and 0.95 deflationary bias.

* CR (the Meritcoin → Credits conversion rate) under the Section 15 formula in the FULL, with the 90-day publication requirement and 25% volatility cap.

* 60/40 carryforward and COI amortization at year-end, with the resulting BaseCost reductions for the following year.

* Freshness window enforcement for authorization records (Part VI, Chapter 18).

* Calibration parameter updates under the procedure specified in Part VI, Chapter 19\.

The algorithmic core has no discretion. Its outputs are reproducible: any auditor running the same input data through the same rule set produces identical outputs. The core's function is to remove parameter-setting from human discretion, exactly so that human discretion can be reserved for the questions that require it.

## **3.2 The Council**

The Council is the human supervisory body. Its size and selection method scale with the Adopting Community:

| Pilot Scale | Council Size | Term Length | Recall Threshold (Petition) |
| :---- | :---- | :---- | :---- |
| Cooperative (N≈200) | 5 members | 1 year | 20% of Participants |
| Municipal (N≈10,000) | 9 members | 2 years | 10% of Participants |
| Regional (N≈250,000) | 15 members | 2 years | 5% of Participants |

Council members are selected by weighted lottery from the pool of Participants whose ΔR\_contributor exceeds 0.1. The lottery weight is proportional to ΔR\_contributor; this preserves the architectural commitment that contribution dominates governance weight. A Participant can decline selection without penalty; selection passes to the next candidate in the lottery order. A Participant can be selected at most once per six-year period (preventing entrenchment).

## **3.3 What the Council can and cannot do**

### **Within authority**

* Override an algorithmic-core output, by 2/3 majority and with 30-day public notice, when the override is justified by a documented failure of the rule under specific circumstances. Override decisions are recorded on Gracechain with the rationale attached.

* Resolve dissent in MIEVM ensemble standoffs (Chapter 2.5).

* Adjudicate disputes between Participants under Part VI, Chapter 20\.

* Approve or reject Compassion Override applications (Part VI, Chapter 21).

* Confer or revoke Verification Authority on institutions applying for Type C status (Part II, Chapter 7).

* Convene constitutional review under the procedure specified in Part V, Chapter 13\.

### **Outside authority**

* Revise the deterministic rules executed by the algorithmic core. Rule revision requires constitutional review under Part V, not Council action.

* Revoke any Participant's UBI for any reason. The survival floor is non-revocable.

* Revise the Recognition Rule. That is the Adopting Community's authority, not the Council's.

* Revise the Three Governing Principles or the Eight Immutable Ethical Principles. Those are constitutional.

* Operate in secret. All Council decisions are public, with attributed votes and published rationales.

## **3.4 Recall by petition**

Any Council member can be recalled mid-term by a petition signed by the threshold percentage of Participants specified in Section 3.2. Recall procedure:

| RUNBOOK  ·  Council Recall Procedure 1\.  A Participant or group of Participants drafts a recall petition stating the Council member's name and the rationale for recall. 2\.  The petition is published on Gracechain and circulates for signatures for a period of 30 days. 3\.  Signatures are tallied by the Authority of Record. Each signature carries the signing Participant's governance weight at the time of signing. 4\.  If the threshold percentage is met or exceeded by the end of the 30-day window, the recall is successful; the Council member's term ends immediately. 5\.  A successor is selected by weighted lottery from the next candidate in the original selection order, serving the remainder of the original term. 6\.  A recalled Council member is ineligible for re-selection for a period equal to twice the original term length. |
| :---- |

## **3.5 Council compensation**

Council service is itself a contribution. Council members earn Meritcoin at a rate calibrated to reflect the time commitment without rewarding entrenchment: the rate is sufficient to compensate the average member for their service hours, no more. Specifically:

* Meeting attendance: 10 Meritcoin per scheduled meeting attended (typically 12–24 meetings per year, depending on Council size and pilot scale).

* Override decisions: 25 Meritcoin per documented override authored, regardless of vote outcome.

* Adjudication decisions: 15 Meritcoin per dispute adjudicated.

Compensation is paid from the COI pool, not from any deployment-specific budget; this ensures Council compensation does not become a target for budget reduction by hostile administrations.

**CHAPTER 4**

**Trustees and the Recovery Triad**

Gracechain identity recovery is one of the open gaps in the architectural treatment. The Manual specifies the operational procedure that an Adopting Community can implement during Phase 1 to honor the architectural commitment that loss of credentials does not strand a Participant from the floor.

## **4.1 The trustee triad**

Every Participant designates a minimum of three Trustees at enrollment. Trustees are independent — they cannot all be members of the same household, the same employer, or the same organization. The recommended triad composition is:

* One personal trustee — typically a family member, close friend, or partner.

* One community trustee — typically a representative of a community organization, mutual-aid network, or cooperative.

* One legal-aid trustee — typically a representative of a legal-aid clinic, bar-association referral service, or community-law organization.

The triad composition is recommended, not constitutional. The constitutional requirement is independence: no two Trustees may be members of the same household, employer, or organization, and at least one Trustee must be unaffiliated with any state agency.

## **4.2 Recovery procedure**

| RUNBOOK  ·  Gracechain Identity Recovery 1\.  The Participant (or, if incapacitated, a Trustee on the Participant's behalf) notifies any one Trustee that recovery is needed. The notifying party provides whatever identification is available — biometric, photographic, testimonial. 2\.  The notified Trustee contacts a second Trustee. The two Trustees verify the Participant's identity through whatever means they consider sufficient (visual recognition, knowledge of shared history, biometric verification by a community institution). 3\.  Once two Trustees concur on identity, they jointly file a Recovery Request with the Authority of Record. The Request includes both Trustees' signatures and the verification method used. 4\.  The Authority of Record posts the Recovery Request to a 30-day public notice period on Gracechain. During this period, any party — including a person claiming the original credentials — may contest. 5\.  If no valid contest is filed within 30 days, the Authority of Record issues replacement credentials to the Participant, marks the prior credentials as superseded, and updates the Trustee Registry to reflect the recovery event. 6\.  If a contest is filed, the Recovery Request is escalated to the GAIA Council for adjudication. The Council resolves the contest within 60 days, with both the Participant and the contestant given the opportunity to be heard. |
| :---- |

## **4.3 Rate limiting**

Recovery is rate-limited to once per Participant per two years. This prevents abuse of the procedure as a way to evade verification penalties or to harass other Participants through repeated false-recovery claims. A Participant in genuine need of more frequent recovery — for example, due to a pattern of credential theft — may petition the GAIA Council for a rate-limit exception, with the petition documented and the exception time-bounded.

## **4.4 If all three Trustees are unreachable**

The architectural commitment that recovery must be possible without state-issued ID requires a fallback path for the case in which all three Trustees are unreachable. The fallback is:

| RUNBOOK  ·  Trustee-Unreachable Fallback 1\.  The Participant notifies the Authority of Record that all three Trustees are unreachable, providing whatever identification is available. 2\.  The Authority of Record schedules an in-person Recovery Hearing within 30 days. The Hearing is conducted before three randomly selected Participants drawn from the GAIA Council's jury pool. 3\.  At the Hearing, the Participant presents their identification. The three jurors interview the Participant, examine any available evidence, and may consult community institutions familiar with the Participant. 4\.  The three jurors deliberate privately and issue a unanimous determination of identity. Anything short of unanimity refers the case to the full GAIA Council for further proceedings. 5\.  On unanimous identity confirmation, the Authority of Record issues replacement credentials and the Participant designates new Trustees within 90 days. |
| :---- |

## **4.5 Trustee responsibilities and protections**

Trustees are not legally accountable for the Participant's actions or balances. Their responsibility is identity recovery only. Specifically:

* A Trustee is obligated to respond to recovery notifications within a reasonable time (default: 14 days). A Trustee who consistently fails to respond may be replaced by the Participant at any time.

* A Trustee who knowingly participates in a false-recovery claim — vouching for a person they know is not the Participant — is subject to the same penalties as a false witness in a verification dispute (Part VI, Chapter 20).

* A Trustee who declines to act in good faith — refusing to respond out of personal animosity, attempting to extract concessions in exchange for cooperation — may be replaced by the Participant and reported to the Authority of Record. A pattern of bad-faith trusteeship may result in the Trustee being barred from future Trustee designation.

* A Trustee receives no compensation for ordinary trusteeship. Recovery hearings, if convened, compensate the Trustee 10 Meritcoin per hearing attended (similar to Council compensation), to recognize the time commitment.

**CHAPTER 5**

**Verification Authorities**

Type C Verifications — institutional verifications, used as evidence in Meritcoin minting decisions — are issued only by institutions holding Verification Authority. This Chapter specifies how an institution acquires, maintains, and (if necessary) loses Verification Authority.

## **5.1 Eligible institutions**

An institution is eligible to apply for Verification Authority if it satisfies all of:

* It is a recognized organization in the Pilot Jurisdiction (cooperative, clinic, school, land trust, mutual-aid society, religious organization, public agency, or other body recognized by the Adopting Community).

* It maintains records of activities relevant to UBIMIA contribution domains. The records need not be currently in machine-readable form, but must be auditable.

* It is willing to post an Operational Bond (Section 5.2) and to submit to quarterly attestation logging and annual audit.

* It has not had Verification Authority revoked within the preceding three years.

## **5.2 The Operational Bond**

Verification Authority requires the posting of an Operational Bond. The Bond is held in escrow by the Authority of Record and is forfeited (slashed) on verified violation. Bond size scales with pilot scale:

| Pilot Scale | Operational Bond (Meritcoin equivalent) | Replenishment Period |
| :---- | :---- | :---- |
| Cooperative (N≈200) | 500 Mc | 30 days from slashing |
| Municipal (N≈10,000) | 2,500 Mc | 60 days from slashing |
| Regional (N≈250,000) | 10,000 Mc | 90 days from slashing |

The Bond may be posted in Meritcoin, in Credits at the prevailing CR, or in fiat at a published exchange rate. Institutions that cannot post the full Bond at application may request a graduated entry: half-Bond at application, full Bond at six months, with reduced verification volume during the half-Bond period.

## **5.3 Application procedure**

| RUNBOOK  ·  Verification Authority Application 1\.  The institution submits an Application to the GAIA Council, including: legal status documentation, description of activities relevant to UBIMIA contribution domains, names of authorized representatives who will sign attestations, and the proposed Operational Bond amount. 2\.  The Council publishes the Application on Gracechain for a 30-day public comment period. Any Participant may submit comments, objections, or supporting attestations. 3\.  The Council reviews the Application and any comments at its next regular meeting. Approval requires a simple majority. Rejection or deferral must include written rationale. 4\.  On approval, the institution posts the Operational Bond. The Bond is acknowledged on Gracechain. Verification Authority becomes effective on the date of Bond acknowledgement. 5\.  The institution receives a published Verification Authority record listing its authorized representatives, the activity domains for which it can issue verifications, and the Bond amount. 6\.  The institution begins quarterly attestation logging within 90 days of authority commencement. |
| :---- |

## **5.4 Quarterly attestation logging and annual audit**

Every institution holding Verification Authority must publish a quarterly attestation log on Gracechain. The log lists every Type C Verification issued during the quarter, with: claim ID verified, date of verification, authorized representative who signed, and a summary of the verification basis (without disclosing private contribution details that would violate the privacy commitment in Part V).

The annual audit, conducted by the GAIA Council under Part VI, Chapter 17, examines the institution's verification records and compares them against random samples of underlying activity data. The audit may identify three categories of finding:

* Concordant — verification records match underlying data; no action required.

* Discrepant — verification records show errors that are explainable as ordinary administrative mistakes; the institution corrects records and is given a notice. Three notices in five years results in Bond reduction.

* Fraudulent — verification records show evidence of intentional false certification; the Operational Bond is fully slashed and Verification Authority is revoked for a minimum of three years, with possible permanent revocation depending on severity.

## **5.5 Loss of Verification Authority**

Verification Authority can be lost in three ways:

* Voluntary surrender. The institution notifies the Council that it is withdrawing from Verification Authority. The Bond is returned after a 90-day audit period during which all outstanding verifications are reviewed.

* Bond forfeiture without replenishment. If the Bond is slashed and the institution does not replenish within the period specified in Section 5.2, Verification Authority lapses automatically. Reinstatement requires a new Application.

* Council revocation. The Council may revoke Authority by 2/3 majority for verified violation of the audit findings or for systematic deviation from the standards specified in Part VI. Revocation includes Bond forfeiture and a minimum three-year exclusion from re-application.

**PART II**

**WHAT**

*Instruments and Schemas*

 

*WHAT answers the second question: which instruments does UBIMIA deploy, with which formal schemas, with which interfaces, and with which behavioral guarantees. Until WHAT is settled in formal terms, no two implementations can talk to each other and no audit can verify that an implementation is UBIMIA-compliant. Part II is the engineering canon.*

**CHAPTER 6**

**The Two Ledgers**

UBIMIA settles across two ledgers — Gracechain (the unconditional, gift-economy floor) and Meritcoin (the contribution-recognized, Proof-of-Resonance augmentation). The architectural separation is established in the FULL; this Chapter specifies the operational properties an implementation must honor.

## **6.1 Gracechain operational properties**

Gracechain is the persistence layer of last resort. Any Manual operation that produces a record is anchored to Gracechain; loss of any other system component must not result in loss of Gracechain state. Specifically:

* Append-only. Records are written and never modified. Corrections are issued as new records that supersede prior records, with the prior records retained for audit.

* Recipient-anchored. Identity is bound to the Participant of Record, not to a wallet, key, or device. Loss of credentials triggers the recovery procedure (Part I, Chapter 4); the underlying identity does not change.

* Aggregate-public. The total flow of UBI distributions, FAVORS rebalancing, IDIPITIS adjustments, and Patriot Dividend payments is publicly verifiable in aggregate.

* Detail-private. Individual receipt amounts and timing are private to the Participant; sensitive contribution details (mental health work, intimate caregiving, learning) are private with zero-knowledge attestation defaults.

* Non-collateralized. Gracechain balances cannot be pledged as collateral, used to secure loans, or financialized in any way. The ledger refuses any transaction attempting collateralization.

## **6.2 Meritcoin operational properties**

Meritcoin is the contribution-recognized currency. Its operational properties enforce the architectural commitments that no fiat exchange occurs and that hoarding is irrational:

* Earned only. Meritcoin is minted only by the EAAP-authorized minting procedure (Part VI, Chapter 16). No other minting path exists.

* Spent only. Meritcoin is spendable only on SCALULAR services (priced via the Resonance-Priced Access formula in Chapter 8\) and governance-weight participation (Part I, Chapter 3.5 Council compensation accrual).

* No exchange. The ledger refuses any transaction that would convert Meritcoin into fiat, into another cryptocurrency, or into a transferable claim that could be subsequently exchanged. The single exception is the gift allowance (10% of annual minting per Participant).

* Annual conversion. Once per year, unspent Meritcoin converts to Credits at the published CR. The conversion is automatic and non-reversible.

* Extinction at death. Meritcoin balance is extinguished at Participant death, returning to the system as a deflationary adjustment. Credits, which are the converted form, can be inherited subject to caps (Part VI, Chapter 17).

## **6.3 The schema layer**

Both ledgers operate against a schema layer specifying the exact format of every record type. The schemas are JSON Schema-conformant; this Manual carries the human-readable summaries, with the formal schemas published separately as ERES-UBIMIA-SCHEMAS-2026-001.

| SCHEMA  ·  ParticipantRecord (Gracechain) {   participant\_id: string (DID format, immutable),   authority\_of\_record: string (issuing Authority's DID),   recognition\_rule: enum (cooperative | municipal | regional | custom),   enrolled\_date: ISO8601 timestamp,   status: enum (active | departed | suspended),   trustees: \[string, string, string, ...\],  // minimum 3 DIDs   delta\_R\_contributor: float \[0, 1\],         // 12-month flow   meritcoin\_balance: integer ≥ 0,   credits\_balance: integer ≥ 0,   governance\_weight: float \[0, 1\] (computed) } |
| :---- |

## **6.4 Audit invariants**

Three invariants must hold at all times in any UBIMIA-compliant implementation. An audit verifies these by sampling; a violation is grounds for the implementation to be flagged non-compliant until the violation is corrected.

* Conservation. The sum of all Meritcoin balances plus all Meritcoin in transit equals the cumulative net minting (lifetime mints minus lifetime extinctions and gift transfers out). No Meritcoin appears or disappears outside the specified procedures.

* Authorization closure. Every minting record references a fresh EAAP authorization record. No minting exists without an authorization, and no authorization exists without DSAP-PRE clearance and the four-factor PoR product computation.

* Identity continuity. Every active Participant has at least three Trustees on file. No active Participant lacks the recovery triad. A Participant whose Trustee count drops below three is given 90 days to designate replacements; failure flags the Participant for Council review.

**CHAPTER 7**

**Claim, Verification, Authorization, Minting**

The four record types involved in turning a real-world contribution into Meritcoin form a chain. Each record references the prior record. The chain is what makes attribution, verification, and audit possible. This Chapter specifies the four record types in detail.

## **7.1 The Claim Object**

A Claim is the Participant's assertion that they performed a specific action contributing to a measured resonance gain. The Claim is signed by the claimant, time-bounded by submission rules, and constrained by overlap rules.

| SCHEMA  ·  Claim {   claim\_id: string (UUIDv7 recommended for time-orderability),   claimant: string (Participant DID),   domain: enum (ecological | social | healthcare | economic | cultural),   system\_boundary: string (named system identifier),   action\_description: string (human-readable; private by default),   time\_start: ISO8601 timestamp,   time\_end: ISO8601 timestamp,   total\_person\_hours: float \> 0,   witnesses: \[string, ...\] (Participant DIDs of witnesses, optional),   submission\_timestamp: ISO8601 timestamp,   signature: cryptographic signature by claimant } Constraints:   submission\_timestamp ≤ time\_end \+ 7 days,   no overlap with claimant's other Claims on same system\_boundary,   claimant.status \= active and not under verification suspension |
| :---- |

## **7.2 The Verification Object**

A Verification is an independent attestation that a Claim is factually correct. There are three types: Type A (sensory/biometric), Type B (witness), Type C (institutional). A Claim may receive multiple Verifications of different types; the highest-weight Verification governs.

| SCHEMA  ·  Verification {   verification\_id: string,   claim\_id: string (references Claim),   verification\_type: enum (A | B | C),   verifier: string (DID of verifier — sensor, witness, or institution),   evidence\_hash: string (cryptographic hash of evidence;                           evidence stored encrypted off-chain),   verification\_timestamp: ISO8601 timestamp,   weight: float (1.0 for Type A, 0.8 for Type B, 0.6 for Type C),   signature: cryptographic signature by verifier } Type A: signed by the device or sensor system; oracle-attested. Type B: minimum two non-collusive witnesses required;         each witness submits an independent Verification. Type C: signed by an authorized representative of an institution         holding Verification Authority (Part I, Chapter 5). |
| :---- |

## **7.3 The Authorization Record**

An Authorization is the EAAP record certifying that a Claim has cleared the authorization stack. Authorization is required before Meritcoin can be minted. The record references the Claim, the Verification(s), the DSAP-PRE clearance, and the four-factor PoR computation.

| SCHEMA  ·  Authorization {   authorization\_id: string,   claim\_id: string (references Claim),   verifications: \[string, ...\] (references Verification IDs),   dsap\_pre\_clearance: {     rho\_RHC: float \[0, 1\],     rho\_PERT: float \[0, 1\],     rho\_hyst: float \[0, 1\],     composite: int (0 or 1\)   },   por\_factors: {     A: float \[0, 1\] (Anchor Product),     R: float \[0, 1\] (RHC Amplitude),     P: float \[0, 1\] (EarnedPath Viability),     F: float \[0, 1\] (Future-Map Convergence)   },   por\_value: float (= A \* R \* P \* F),   threshold: float (theta for the domain),   outcome: enum (authorized | refused),   refusal\_reason: enum (REGIME\_TRANSITION | INSUFFICIENT\_POR | null),   mievm\_ecr: float \[0, 1\] (ensemble convergence ratio),   authorization\_timestamp: ISO8601 timestamp,   freshness\_window\_seconds: integer,   signature: cryptographic signature by authorization service } |
| :---- |

## **7.4 The Minting Record**

A Minting Record is the final link in the chain — the record that creates new Meritcoin. The record references the Authorization, the magnitude calculation, and the Participant receiving the Meritcoin.

| SCHEMA  ·  MintingRecord {   minting\_id: string,   authorization\_id: string (references Authorization),   claimant: string (Participant DID),   base\_reward: integer (governance parameter, Part VI Ch 19),   delta\_R\_net: float \[0, 1\] (weighted sum across BERA indices),   quality\_weight: float (1.0 / 0.8 / 0.6 by verification type),   meritcoin\_minted: integer (= base\_reward \* delta\_R\_net \* quality\_weight),   ledger\_position: integer (Meritcoin ledger sequence),   rcr\_record: string (Runtime Containment record reference),   minting\_timestamp: ISO8601 timestamp,   signature: cryptographic signature by minting service } Invariant: meritcoin\_minted \= floor(base\_reward × delta\_R\_net × quality\_weight) |
| :---- |

## **7.5 Chain integrity**

The four records form a linear chain: Claim → Verification(s) → Authorization → MintingRecord. An audit walks the chain backward from any MintingRecord to verify that:

* The Authorization references a Claim that exists and was submitted within the 7-day window.

* The Authorization references at least one Verification with weight ≥ 0.6.

* The Authorization's PoR computation, when re-executed against the same input data, produces the same value.

* The DSAP-PRE clearance, when re-executed, produces the same composite output.

* The MintingRecord's meritcoin\_minted equals the formula applied to the Authorization's outputs.

* The MintingRecord references a fresh RCR record (Part VI, Chapter 18\) within the freshness window.

Any break in the chain — a missing record, a signature failure, a recomputation mismatch — is grounds to reject the MintingRecord and reverse the mint. Reversal does not require a court; it is an audit invariant. The slashing penalties for the Participant or institution responsible follow from Part VI, Chapter 20\.

**CHAPTER 8**

**Resonance-Priced Access: The Formula**

The conversion of Meritcoin into SCALULAR service access is the most operationally consequential formula in UBIMIA. The architectural treatment carried the prose statement of the rule; this Manual carries the formula in its operationally correct form, with the floor explicitly written rather than buried in the text.

## **8.1 The corrected formula**

The Resonance-Priced Access cost for any SCALULAR service S in tier T is:

**Cost(S) \= BaseCost(T) × Complexity(S) × max(0.5, 1 / (1 \+ ΔR\_contributor))**

The max(0.5, ...) form expresses the 50% floor explicitly. At ΔR\_contributor \= 1.0, the discount factor is 1/(1+1.0) \= 0.5, which equals the floor; for any ΔR\_contributor \> 1.0 (hypothetically possible if normalization were imperfect), the discount factor would still be 0.5 by the max operation. The floor is non-negotiable: no Participant pays less than 50% of base, however contribution-rich.

## **8.2 The single-domain cap**

ΔR\_contributor is normalized within domain to the interval \[0, 1\]. To prevent gaming by concentrating in a single domain, the architectural treatment specified that no Participant can have ΔR\_contributor \> 0.6 from a single domain. The Manual makes this rule explicit in operational form:

**ΔR\_contributor \= min(0.6, ΔR\_domain\_primary) \+ sum(ΔR\_domain\_secondary, ...)**

The primary domain (the domain in which the Participant has the highest unweighted ΔR) is capped at 0.6. Contributions in secondary domains add without cap, until the global ΔR\_contributor reaches its ceiling at 1.0. The effect is that reaching the maximum 50% discount requires meaningful contribution in at least two domains. Single-domain specialists can earn substantial Meritcoin and substantial discount, but the architecturally privileged top tier is reserved for multi-domain contributors.

## **8.3 BaseCost calibration**

BaseCost(T) is set annually by the GAIA algorithmic core under the formula in the FULL §15. The Manual supplies the initial calibration table that an Adopting Community can use as a starting point for the Calibration Window:

| SCALULAR Tier | Initial BaseCost (Mc per service-hour) | Notes |
| :---- | :---- | :---- |
| HEALTH (SSHP) | 10 Mc | Calibrated to median primary-care visit cost |
| LAW (SSLA) | 8 Mc | Lower than HEALTH; reflects shorter service durations |
| PROTECTION (SSPS) | 6 Mc | Lowest; reflects standing capacity rather than per-incident service |
| SKILLS\_TRADE (SSST) | 12 Mc | Highest; reflects per-hour instructor cost premium |

The initial values are starting points only. The Adopting Community runs the GAIA algorithmic core against the first year's pilot data; the formula adjusts BaseCost by the actual minting-to-demand ratio observed. By the end of the Calibration Window (year 1), BaseCost values reflect the jurisdiction-specific economy. The 25% volatility cap prevents large jumps; the 0.95 deflationary bias rewards continued participation.

## **8.4 Complexity factors**

Complexity(S) is the per-service multiplier reflecting resource intensity. Initial calibration table for the most common SCALULAR services:

| Service | Tier | Complexity Factor | Typical Duration |
| :---- | :---- | :---- | :---- |
| Primary care visit | HEALTH | 1.0 | 30 min |
| Routine vaccination | HEALTH | 0.5 | 15 min |
| Mental health session | HEALTH | 1.5 | 50 min |
| Major surgery | HEALTH | 4.0 | varies |
| Organ transplant | HEALTH | 8.0 | varies |
| Civil mediation | LAW | 1.0 | 2 hr |
| Document review | LAW | 0.7 | 1 hr |
| Court representation | LAW | 3.0 | varies |
| Personal security consult | PROTECTION | 1.0 | 1 hr |
| Disaster response | PROTECTION | 5.0 | varies |
| Standard course | SKILLS | 1.0 | per credit hour |
| Apprenticeship stipend | SKILLS | 2.5 | per quarter |
| Specialized credentialing | SKILLS | 3.0 | per certification |

The Adopting Community publishes its full Complexity Factor table at the start of Phase 1\. Additions, corrections, or jurisdiction-specific entries are submitted through the procedure in Part VI, Chapter 19\. The table itself is part of the constitutional layer — changes require 30-day public notice and Council review.

## **8.5 Worked examples across the three pilot scales**

| COOPERATIVE  ·  N≈200 Cooperative pilot, BaseCost(HEALTH) \= 8 Mc/hr (reduced from 10 to reflect smaller-scale costs). Participant with ΔR\_contributor \= 0.5 (achieved across two domains) pays for primary care: 8 × 1.0 × max(0.5, 1/1.5) \= 8 × 0.667 \= 5.33 Mc. | MUNICIPAL  ·  N≈10,000 Municipal pilot, BaseCost(HEALTH) \= 10 Mc/hr (reference). Same Participant pays for primary care: 10 × 1.0 × max(0.5, 1/1.5) \= 6.67 Mc. For major surgery: 10 × 4.0 × 0.667 \= 26.67 Mc. | REGIONAL  ·  N≈250,000 Regional pilot, BaseCost(HEALTH) \= 12 Mc/hr (elevated to reflect regional cost variation). Same Participant pays for primary care: 12 × 1.0 × 0.667 \= 8.00 Mc. The discount applies identically regardless of scale; only BaseCost varies. |
| :---- | :---- | :---- |

**CHAPTER 9**

**BERA Indices: ARI, ERI, RHC, RCI**

The four BERA indices are the measurement frame against which contributions are evaluated. The architectural treatment named them and gave their roles. This Chapter supplies the operational interface specifications — what an oracle for each index must accept, must compute, and must emit.

## **9.1 ARI — Adaptive Resonance Index**

ARI measures the fit of a system to its changing conditions. An ARI oracle accepts a system identifier and a time window; it emits the system's ARI value over that window.

| SCHEMA  ·  ARI Oracle Interface Input:   system\_id: string (named system, e.g., 'forest\_patch\_alpha'),   time\_window\_start: ISO8601,   time\_window\_end: ISO8601,   domain: enum Computation:   ARI \= inverse\_normalized\_response\_variance(system\_id, window) ×         absorbed\_perturbation\_magnitude(system\_id, window) Output:   {     system\_id: string,     window: { start: ISO8601, end: ISO8601 },     ari\_value: float \[0, 1\],     confidence\_interval: \[float, float\],     data\_sources: \[string, ...\],     oracle\_signature: cryptographic signature   } |
| :---- |

## **9.2 ERI — Ethical Resonance Index**

ERI measures alignment with the Eight Immutable Ethical Principles. An ERI oracle is the most consequential of the four because it explicitly encodes ethical content in measurable form. The constitutional defense is that the Principles are fixed; ERI measures consistency with fixed Principles, not conformity to a regime's preferences.

| SCHEMA  ·  ERI Oracle Interface Input:   system\_id: string,   time\_window\_start: ISO8601,   time\_window\_end: ISO8601 Computation: weighted product across eight sub-indices,   one per Immutable Principle:     sustainability\_sub\_index from waste-stream reduction,     transparency\_sub\_index from data-publication completeness,     harm\_reduction\_sub\_index from documented harm reduction,     welfare\_sub\_index from measured welfare metrics,     dignity\_sub\_index from documented dignity indicators,     recognition\_sub\_index from contribution acknowledgement,     reversibility\_sub\_index from preserved-option count,     pluralism\_sub\_index from governance diversity Output: { ..., eri\_value, confidence\_interval, ... } |
| :---- |

## **9.3 RHC — Resonant Harmony Cycle**

RHC measures sustained periodic coherence over time. The naming is canonical: RHC is Resonant Harmony Cycle, never 'Resonant Harmony Cybernetics.' An RHC oracle returns zero if variation falls below 0.05 — the flatline detection rule that prevents gaming by stillness.

| SCHEMA  ·  RHC Oracle Interface Input:   system\_id: string,   time\_window\_start: ISO8601,   time\_window\_end: ISO8601 Computation:   amplitude \= normalized\_amplitude(periodic\_component(system, window))   variation \= stddev(amplitude) / mean(amplitude)   if variation \< 0.05: rhc\_value \= 0  // flatline rule   else: rhc\_value \= max(0, amplitude \- 0.05) / (1 \- 0.05) Output: { ..., rhc\_value, variation\_observed, ... } |
| :---- |

## **9.4 RCI — Resonance Continuity Index**

RCI is the most operationalizable of the four indices because it has an explicit formula derived from Butzbach Continuity Theory. An RCI oracle implementation can use sliding-window autocorrelation as the persistence proxy, with the ARI\_sys input drawn from the ARI oracle, and VibConst supplied from the domain table.

| SCHEMA  ·  RCI Oracle Interface Input:   system\_id: string,   time\_window\_start: ISO8601,   time\_window\_end: ISO8601,   domain: enum (ecological | social | economic) Computation:   P\_omega\_norm \= normalized\_persistence(system, window)                   // sliding-window autocorrelation                   // lag \= 1 day, window \= 30 days   ari\_sys \= ARI\_oracle(system, window).ari\_value   vib\_const \= vibconst\_table\[domain\]   rci\_value \= P\_omega\_norm × ari\_sys × vib\_const VibConst table (initial calibration):   ecological: 1.0,   social: 0.85,   economic: 0.92 Output: { ..., rci\_value, p\_omega\_norm, ari\_sys, vib\_const, ... } |
| :---- |

## **9.5 Composition into ΔR\_net**

For Meritcoin minting, the four indices compose into ΔR\_net via weighted sum:

**ΔR\_net \= w\_ARI × ΔARI \+ w\_ERI × ΔERI \+ w\_RHC × ΔRHC \+ w\_RCI × ΔRCI**

Domain-calibrated weights summing to 1.0. Initial calibration:

| Index | Default Weight | Rationale |
| :---- | :---- | :---- |
| w\_ARI | 0.25 | Adaptation matters but is not exclusive |
| w\_ERI | 0.30 | Ethics is primary; highest weight |
| w\_RHC | 0.25 | Harmony prevents collapse |
| w\_RCI | 0.20 | Continuity is important but can be traded |

Note: the weighted-sum composition is normative for reward magnitude (Section 7.4 minting). Authorization (the EAAP gate, Chapter 11\) uses the conjunctive product, in which a weak factor cannot be compensated by a strong one. The two layers operate at different points in the chain.

**CHAPTER 10**

**Credits, Bills, and the COI Pool**

The annual settlement cycle converts Meritcoin to Credits, Credits to Bill payments, and unspent balance to carryforward and the Community Opportunity Investment pool. This Chapter specifies the operational records and the year-end procedure.

## **10.1 Credit operational properties**

* Credits are denominated in a unit comparable to the local cost of SCALULAR services.

* Credits are produced by two paths: annual conversion from Meritcoin (via the GAIA-set CR), and Patriot Dividend distributions (which arrive directly as Credits, not Meritcoin).

* Credits are spendable on SCALULAR Bills under the RPA pricing formula.

* Credits are inheritable subject to caps; unspent Credits at year-end follow the 60/40 rule.

* Credits cannot be exchanged for fiat; like Meritcoin, they are use-only within UBIMIA.

## **10.2 The Bill record**

| SCHEMA  ·  Bill {   bill\_id: string,   participant: string (DID),   tier: enum (HEALTH | LAW | PROTECTION | SKILLS),   service: string (references service in Complexity table),   service\_provider: string (DID of provider institution),   service\_date: ISO8601 timestamp,   cost\_credits: integer (computed via RPA),   delta\_R\_at\_billing: float (Participant's ΔR\_contributor at billing time),   rcr\_record: string (Runtime Containment record reference),   status: enum (pending | paid | disputed | refunded),   payment\_timestamp: ISO8601 timestamp (null until paid),   signature: cryptographic signature by service\_provider } |
| :---- |

## **10.3 Year-end procedure**

| RUNBOOK  ·  Annual Settlement Year-End Procedure 1\.  On day 90 before year-end, GAIA publishes the next year's CR and the next year's BaseCost(T) for each tier, computed by the algorithmic core formulas. Participants have 90 days to plan whether to spend Meritcoin before conversion or to convert. 2\.  On day 1 of the new year, all unspent Meritcoin in each Participant's account converts to Credits at the published CR. The conversion is recorded on Gracechain. 3\.  Throughout the year, Participants pay Bills using their Credit balance. Each Bill payment produces a Bill record with status 'paid' and an RCR reference. 4\.  On day 365, GAIA computes each Participant's unspent Credit balance. The balance is split: 60% added to the Participant's Credit account for the new year (as a starting balance independent of newly converted Meritcoin); 40% transferred to the COI pool. 5\.  GAIA computes the BaseCost adjustment for the new year using the COI pool magnitude and the prior-year minting-to-demand ratio. The adjustment is published; Participants see the new BaseCost values and can plan accordingly. 6\.  Audit logs for the year are sealed and posted to Gracechain. Any Participant or auditor may verify the computation by re-running the formulas against the published input data. |
| :---- |

## **10.4 Patriot Dividend integration**

Patriot Dividend distributions, specified separately in ERES-PD-2026-001 v4.0, arrive on Gracechain as direct Credit deposits to all Participants of Record. They do not pass through Meritcoin minting. The integration with the year-end procedure is straightforward: Patriot Dividend Credits accumulate during the year, are spendable on Bills like any other Credits, and follow the 60/40 split at year-end.

The Adopting Community decides whether to fund Patriot Dividend distributions, in what amount, and on what schedule (monthly, quarterly, annually). The architectural commitment is that Patriot Dividend, where deployed, supplements rather than substitutes for Meritcoin-derived Credits — both flow into the same Participant account, both are spendable on the same Bills, and both follow the same year-end split.

**CHAPTER 11**

**The Three Anchors: Identity, Authorization, and Persistence**

UBIMIA-compliant implementations rely on three anchor systems: an Identity anchor (binding Participants to their records), an Authorization anchor (binding actions to fresh authorization), and a Persistence anchor (binding all of the above to immutable storage). This Chapter specifies the interface contracts an implementation must honor.

## **11.1 Identity anchor**

The Identity anchor implements the recipient-anchored identity property of Gracechain. An implementation can use any underlying identifier scheme — DIDs, biometric hashes, sealed enclaves — provided the implementation honors the contract:

* Resolve(participant\_id) → ParticipantRecord. The identifier resolves to the current participant record.

* Recover(claim\_evidence, trustees) → new\_credentials. Given evidence and trustee approvals (Part I, Chapter 4), produces new credentials for the same identity.

* UpdateTrustees(participant\_id, new\_trustees) → success/failure. The Participant can change their trustee triad, subject to rate limits.

* MarkDeparted(participant\_id, departure\_timestamp) → success. Sets status to departed and triggers the asset-handling rules.

Implementations should resist key-loss attacks: a participant who loses their device must remain recoverable through the trustee triad, and a participant whose device is stolen must be able to invalidate the prior credentials without losing identity continuity.

## **11.2 Authorization anchor**

The Authorization anchor implements the EAAP runtime stack. The contract:

* Authorize(claim, verifications) → AuthorizationRecord. Performs DSAP-PRE check and four-factor PoR computation; returns an authorization record with outcome and freshness window.

* CheckFresh(authorization\_id, current\_time) → fresh/stale. Returns true if the authorization is within its freshness window; false otherwise.

* Bind(authorization\_id, action) → RCR record. Binds the authorization to a specific action; returns the runtime containment record. Required before action execution.

The contract requires the authorization service to refuse to issue authorization when DSAP-PRE returns zero, when any PoR factor falls below the implicit minimum (typically the cube root of θ to ensure conjunctive product reaches threshold), or when the MIEVM ECR falls below the minimum (0.60 pilot, 0.75 production).

## **11.3 Persistence anchor**

The Persistence anchor implements Gracechain. The contract:

* Append(record) → ledger\_position. Appends a record to Gracechain; returns the position. Append-only; no overwrite.

* Read(query) → records. Returns records matching the query, with privacy filters applied based on the requester's authorization.

* Verify(record, ledger\_position) → valid/invalid. Verifies that the record at the given position matches the supplied record (for audit).

* Audit(time\_range) → audit\_proof. Produces a cryptographic audit proof over the records in the time range, suitable for independent verification.

The persistence anchor is the system whose loss would be most damaging to UBIMIA. Implementations should be conservative: prefer redundant persistence (multiple geographically distributed replicas), prefer cryptographically auditable structures (Merkle trees, signed checkpoints), prefer simplicity over performance optimization. Gracechain is the system of record; performance is secondary to integrity.

**PART III**

**WHERE**

*Sites and Infrastructure*

 

*WHERE answers the third question: which physical and digital sites host which functions, with which security perimeters, with which jurisdictional boundaries, and with which custody arrangements for the most sensitive material. Until WHERE is settled, the operational specification has no place to live.*

**CHAPTER 12**

**Physical Sites**

UBIMIA needs physical sites for three functions: enrollment and recovery, attestation and verification, and Council operations. Each function has different security and accessibility requirements, and a single site may serve multiple functions if the site can satisfy the strictest requirement among them.

## **12.1 Enrollment sites**

Enrollment is the process by which a person becomes a Participant of Record. The site must be accessible — no Participant should face a barrier of distance, cost, or formality at enrollment — and it must be capable of biometric anchoring without leaking biometric data outside the Participant's control.

Recommended siting: a community center, a co-op office, a public library, a clinic, or any other space with regular hours and a published address. The site is staffed by trained Authority of Record representatives during enrollment hours; outside enrollment hours, the site continues its ordinary function. Cooperative pilots can use a single shared space; municipal pilots typically need three to five geographically distributed sites; regional pilots need one site per population center plus a mobile capability.

## **12.2 Attestation booths**

Attestation booths are the sites at which Participants submit Claims, witness other Participants' Claims, and view their own ledger records. A booth is not a building — it is a software interface accessible from any participating Participant's device, supplemented by physical kiosks for Participants without personal devices.

| COOPERATIVE  ·  N≈200 Single shared booth at the co-op space. Hours match the co-op's regular hours. Members access from personal devices when not in the booth. | MUNICIPAL  ·  N≈10,000 One physical booth per population center, plus an open-source mobile app available for personal-device use. App accessibility audit required quarterly. | REGIONAL  ·  N≈250,000 One physical booth per population center, plus a regional app meeting the regional jurisdiction's accessibility requirements. Multilingual support is mandatory. |
| :---- | :---- | :---- |

The booth's job is to be a low-friction, low-fear site for entering Claims. Participants should be able to enter a Claim in five minutes or less for routine contributions, with the system pre-populating system\_boundary and time\_window fields when it can infer them from prior activity. The booth should not require users to understand the underlying schema; the schema is the implementation's concern, not the user's.

## **12.3 Council chambers**

The Council needs a place to meet — for regular sessions, for override decisions, for adjudication, and for recall hearings. The Council chamber must satisfy three properties:

* Public access. Council sessions are public; the chamber must accommodate observers.

* Recording capacity. All sessions are recorded and posted to Gracechain. The chamber must support reliable audio and video capture.

* Deliberation privacy. Some Council decisions (jury deliberations, identity recovery hearings, dispute adjudications involving sensitive personal information) require private deliberation. The chamber must include a private deliberation room, distinct from but adjacent to the public session space.

The chamber may also serve as the Council's compensation point: Council members earning Meritcoin per Section I.3.5 attend chamber sessions in person or by verified telepresence, with attendance verified by the Authority of Record.

## **12.4 Recovery hearing sites**

When the Trustee-unreachable fallback procedure is invoked (Part I, Chapter 4.4), the recovery hearing requires three randomly selected Participants from the GAIA Council's jury pool to convene in person with the Participant whose identity is being recovered. Recovery hearings are by appointment, infrequent, and conducted at the Council chamber or — at the requesting Participant's option — at a community center within reasonable distance.

The site must be accessible; a Participant who has lost credentials may also lack transportation, mobility, or social-support resources. The Authority of Record is responsible for providing transportation assistance and accessibility accommodations on request, drawn from the COI pool when necessary.

**CHAPTER 13**

**Digital Sites**

Digital sites are the network locations at which UBIMIA's persistent state lives. The architectural commitment to recipient-anchored identity, to public auditability of aggregate flows, and to private custody of sensitive contribution detail dictates a multi-tier digital topology.

## **13.1 Gracechain anchor**

Gracechain is the immutable, append-only persistence layer. The anchor — the primary system of record for Gracechain — must be:

* Geographically distributed. At minimum three replicas in distinct legal jurisdictions, so that a single jurisdiction's adversarial action cannot destroy the record.

* Cryptographically auditable. A Merkle-tree-or-equivalent structure, with periodic signed checkpoints published openly, so that any third party can verify state without trusting any single anchor operator.

* Operationally simple. Append-only with verified signatures on every record; no smart-contract complexity for the persistence layer (smart-contract logic, where used, runs in subsidiary services that themselves anchor to Gracechain).

The Adopting Community designates the primary anchor operator. Most pilots will use an existing public infrastructure — an Ethereum-compatible chain, a Filecoin-anchored data store, or a sovereign-operated public ledger — rather than building from scratch. The choice is local; the contract (Section 11.3) is universal.

## **13.2 Meritcoin ledger**

The Meritcoin ledger is operationally distinct from Gracechain even when both share the same underlying persistence technology. The distinction is functional: Gracechain holds the unconditional and constitutional records (Participant register, UBI flow, FAVORS rebalancing, recovery proceedings); Meritcoin ledger holds the contribution-recognized records (mints, transfers, conversions). The two-ledger separation is what prevents the merit ledger from being weaponized against the floor.

In a pilot deployment, the two ledgers may be implemented as two distinct logical zones within a single underlying persistence system, with cryptographic boundaries that prevent cross-zone state corruption. In a production deployment, the two ledgers may be implemented as fully distinct persistence systems with cryptographic anchoring between them. The architectural commitment is the same regardless of implementation: failures of the merit ledger do not propagate into Gracechain.

## **13.3 RCR audit log**

The Runtime Containment audit log is the record of every authorization-bound action. Every UBIMIA operation that consumes or transfers value produces an RCR record; every RCR record is anchored to Gracechain. The log is queryable for audit but its records are never modified.

Pilot deployments may implement the RCR log as an append-only file system with periodic Gracechain anchoring, rather than as inline Gracechain writes for every action. The trade-off is latency vs. instantaneous immutability; for pilots, latency-tolerant batch anchoring is acceptable. Production deployments should anchor each RCR record at the time of issuance.

## **13.4 Encryption-key custody**

| The Custody Triad Sensitive contribution data (mental health work, intimate caregiving, learning that the Participant prefers private) is encrypted with keys held in a three-party custody triad: the Participant, the Trustee Registry, and an independent Custody Authority. No single party can decrypt. Decryption requires either Participant consent or two-of-three concurrence under specified circumstances (audit, dispute adjudication, recovery). |
| :---- |

The Custody Authority is a separate body from the Authority of Record and from the GAIA Council. It exists to hold one of the three encryption-key shares, to refuse decryption requests that lack proper authorization, and to publish quarterly transparency reports on the number of decryption requests received and granted. The Adopting Community designates the Custody Authority — typically a community institution unrelated to the governance bodies, with a documented track record of refusing improper data requests.

## **13.5 Sealed-room hardware custody**

Hardware key-management modules — the physical devices that hold cryptographic keys for ledger signing, MIEVM ensemble attestation, and the Custody Authority's share — must be housed in sealed-room conditions. The room is a physical space with:

* Tamper-evident seals on entry points. Any unauthorized entry produces visible evidence.

* Two-person concurrence for entry. No single individual can enter alone; any access requires two designated key-bearers acting together.

* Environmental monitoring. Temperature, humidity, and motion are logged continuously, with the log streamed to Gracechain.

* Air-gapped operation. The hardware modules do not connect to general-purpose networks. Communication occurs through audited intermediary systems with one-way data diodes for outbound state; inbound configuration changes require physical media handed in via the two-person procedure.

The sealed-room standard is high but not exotic; commercial hardware security modules and existing data-center practices already meet most requirements. The Adopting Community typically does not need to build a sealed room from scratch; it leases capacity from an established secure-facility operator that meets the requirements.

**CHAPTER 14**

**Jurisdictional Boundaries and Cross-Border Behavior**

UBIMIA pilots operate within a Pilot Jurisdiction — the legal-administrative entity that gives the Adopting Community its standing. Pilot Jurisdictions have boundaries; UBIMIA's behavior at and across those boundaries is operationally important and merits its own Chapter.

## **14.1 Within-jurisdiction operation**

Within the Pilot Jurisdiction, UBIMIA operates as specified throughout the Manual. Participants of Record receive UBI, earn Meritcoin, pay Bills, participate in governance. The Authority of Record maintains the register. The Council convenes and operates. SCALULAR providers accept Credits.

## **14.2 Cross-border travel**

A Participant of Record traveling outside the Pilot Jurisdiction temporarily retains their status. UBI flow continues during travel, deposited as Credits to the Participant's account. SCALULAR access is limited to providers who have signed cross-border acceptance agreements with the Adopting Community; in jurisdictions without such agreements, the Participant pays for services in fiat (using their own resources) and is reimbursed at the published cross-border reimbursement rate on return.

Meritcoin earning during cross-border travel is permitted only for contributions made within the home Pilot Jurisdiction (via remote work, telecommuting, or coordination with home-jurisdiction systems) or for contributions in the visited jurisdiction that are formally recognized via inter-jurisdiction Compact. In the absence of a Compact, contributions in the visited jurisdiction earn no Meritcoin.

## **14.3 Permanent emigration**

Permanent emigration triggers the departure procedure (Part I, Chapter 1.3). The Participant notifies the Authority of Record, status changes to Departed, UBI flow ceases, Meritcoin balance is frozen for five years, Credits balance is drawable for two years.

If the Participant relocates to a jurisdiction with its own UBIMIA pilot, a Dual Recognition Compact between the two Adopting Communities can simplify the transition: the Participant transfers their record from the prior community to the new community, with prior ΔR\_contributor restored at 50% (the standard re-entry decay). Without a Compact, the Participant departs the prior community fully and enrolls in the new community as a new Participant.

## **14.4 Immigration into the Pilot Jurisdiction**

A person entering the Pilot Jurisdiction with intent to remain becomes eligible for enrollment under the Adopting Community's Recognition Rule. The Recognition Rule's specific waiting periods (183 days residency, 365 days residency, etc.) determine when the person can enroll. During the waiting period, the person receives Compassion Override emergency SCALULAR access only — not UBI.

Immigrants from jurisdictions with their own UBIMIA pilots can transfer under a Dual Recognition Compact (Section 14.3 reciprocal direction). Without a Compact, they enroll fresh, with no transferred ΔR\_contributor.

## **14.5 Cross-border Meritcoin and Credits**

Meritcoin and Credits do not cross borders. They are use-only currencies within their issuing UBIMIA deployment. A Participant who relocates does not carry Meritcoin or Credits to the new jurisdiction. The asset rules (frozen Meritcoin, drawable Credits, eventual extinction) handle the transition.

Inter-deployment trade — a SCALULAR provider in one Adopting Community serving a Participant from another — is handled through the Dual Recognition Compact's settlement provisions. Typically, the home jurisdiction's COI pool reimburses the visited jurisdiction's provider in the visited jurisdiction's Credits, with the rate set by mutual agreement. The Participant pays in their home jurisdiction's Credits at home rates; the cross-jurisdiction rate adjustment is invisible to the Participant.

**PART IV**

**WHEN**

*Cycles and Sequencing*

 

*WHEN answers the fourth question: at which times do the operations execute, in which order, with which dependencies, and with which graduation gates between phases. Without sequencing, an Adopting Community knows what to do but not when; without graduation gates, a pilot cannot end and become production. Part IV is the calendar.*

**CHAPTER 15**

**Phase 1 Deployment: Day 0 through Day 365**

Phase 1 is the pilot phase: UBIMIA running in parallel with existing systems, in one Adopting Community, for one or two years. This Chapter is the day-by-day runbook for the first year. Specific dates are relative to Deployment Day, the day on which UBI distributions begin flowing.

## **15.1 The pre-deployment period (Day \-180 to Day 0\)**

| RUNBOOK  ·  Pre-Deployment Sequence 1\.  Day \-180: The Adopting Community announces intent to pilot UBIMIA. Recognition Rule template selection begins. Initial Trustee Registry recruitment opens. 2\.  Day \-150: Recognition Rule is finalized and published. Authority of Record is designated. Custody Authority is designated. 3\.  Day \-120: Initial Council selection lottery is conducted. Council members serve a transitional first term (six months) before the regular two-year term cycle begins. 4\.  Day \-90: GAIA algorithmic core implementation is configured with initial calibration values from Part II Chapter 8\. MIEVM ensemble membership is established with the canonical four lineages (Claude, ChatGPT, Grok, DeepSeek) under documented pilot simplification. 5\.  Day \-60: Sealed-room infrastructure is commissioned. Hardware key-management modules are installed and verified. Three-party custody triad is operational. 6\.  Day \-30: Trial Claim submissions begin with simulated contributions. The full chain (Claim → Verification → Authorization → Minting) is exercised end-to-end. Audit invariants are verified. 7\.  Day \-14: Participant enrollment opens. The Authority of Record begins processing applications under the Recognition Rule. 8\.  Day \-7: First Bills are issued (pro-rated Genesis Bills) to enrolled Participants. Participants verify their initial Bill records. 9\.  Day 0: Deployment Day. UBI distributions begin flowing on Gracechain. Phase 1 is in operation. |
| :---- |

## **15.2 The first quarter (Day 0 to Day 90\)**

The first quarter is the most fragile period of the pilot. Mistakes are most costly here, because Participants are forming their initial impressions of the system. The runbook prioritizes stability over completeness:

| RUNBOOK  ·  First Quarter Operations 1\.  Day 1-30: UBI flows begin. The Authority of Record processes ongoing enrollments. The Council holds its first regular meeting and reviews the first 30 days of operation. No Bill payments yet — Genesis Bills accrue but are not paid. 2\.  Day 31-60: Bill payment begins. Participants pay their first SCALULAR service Bills using Patriot Dividend Credits (if deployed) or pro-rated initial Credit allocations. The Council reviews the first month of Bill payments and the first month of any disputes. 3\.  Day 61-90: Initial Claim submissions begin. The first contributions are submitted, verified, and (if authorized) result in Meritcoin minting. The Council reviews the first month of Claim activity. The first MIEVM ensemble attestations are recorded; ECR is monitored for early warning of ensemble drift. 4\.  Day 90: First Quarter Review. The Council publishes a public report on operations to date, including: enrollment counts, UBI distribution totals, Bill payment volumes, Claim submission counts, Authorization outcomes (authorized vs. refused), Meritcoin mint totals, and any audit findings. |
| :---- |

## **15.3 The Calibration Window (Day 90 to Day 365\)**

From Day 90 onward, the system runs on real data with monthly parameter calibration. The Calibration Window is the period during which initial reference parameters are adjusted to jurisdiction-specific values:

* BaseCost(T) is recalibrated monthly using the running ratio of mint volume to demand volume, with the 25% volatility cap and 0.95 deflationary bias.

* CR is published 90 days before year-end (Day 275\) and locked at that publication for the upcoming year-end conversion.

* Domain weights (w\_ARI, w\_ERI, w\_RHC, w\_RCI) are reviewed quarterly by the Council and may be adjusted based on observed mint patterns and Council priorities.

* DSAP-PRE calibration (κ\_RHC, η\_recover, τ) is reviewed at Day 180 and Day 365 by the Council. Adjustments require justification documented in Council records.

## **15.4 Year-End (Day 365\)**

| RUNBOOK  ·  Year-End Procedure 1\.  Day 275: GAIA publishes the next year's CR and BaseCost values. Participants have 90 days to plan whether to spend Meritcoin before conversion or convert. 2\.  Day 365: Conversion of all unspent Meritcoin to Credits at the published CR. Conversion records anchored to Gracechain. 3\.  Day 365: Computation of unspent Credit balances. 60% added to next year's starting balance; 40% to COI pool. 4\.  Day 365: COI pool computation and publication. BaseCost adjustment for the new year published. 5\.  Day 365: Year-end audit log sealed and posted. Public verification of computations begins. 6\.  Day 366: Phase 1 enters its second year (if a 24-month pilot) or the Council reviews graduation criteria for Phase 2 (if a 12-month pilot). |
| :---- |

**CHAPTER 16**

**Annual Cycles and Recurring Operations**

After the first year, UBIMIA operates on a steady annual cycle. This Chapter specifies the recurring operations that occur every year, regardless of pilot phase.

## **16.1 The annual calendar**

| Day of Year | Operation |
| :---- | :---- |
| 1 | Conversion of unspent Meritcoin to Credits at published CR |
| 1 | Application of carryforward Credits (60% of prior year unspent) |
| 1 | Application of new BaseCost values (after COI amortization adjustment) |
| 30 | First quarterly Council session of the year |
| 90 | First quarter audit log published |
| 120 | Second quarterly Council session |
| 180 | Mid-year DSAP-PRE calibration review |
| 210 | Third quarterly Council session |
| 270 | Fourth quarterly Council session |
| 275 | Publication of next year's CR and BaseCost values |
| 300 | Trustee Registry quarterly review (any Participants below 3 Trustees flagged) |
| 365 | Year-end conversion, settlement, and audit-log sealing |

## **16.2 Freshness windows**

Authorization records are issued with freshness windows that scale to the operation's risk and cadence:

| Operation Type | Freshness Window | Rationale |
| :---- | :---- | :---- |
| Bill payment (routine SCALULAR) | 1 day | Cadence matches daily life |
| Meritcoin minting | 1 day | Aligned with claim and verification cadence |
| Council vote on Override | 1 hour | Real-time deliberative cadence |
| Verification Authority decisions | 1 hour | Council session cadence |
| Sealed-room access | 5 minutes | Highest-stakes cadence |
| DSAP-PRE evaluation | matches RHC cycle | Domain-calibrated |

## **16.3 Decay schedules**

Several quantities decay over time, by design:

* ΔR\_contributor decays with a 12-month rolling window. Only contributions in the past 365 days count toward the discount factor in RPA pricing.

* Verification weight is fixed at the moment of verification but contributes to ΔR\_contributor for only 12 months. After 12 months, the contribution is acknowledged in the Participant's history but no longer affects pricing.

* Meritcoin balance does not decay actively, but converts annually. A Participant who never spends sees their Meritcoin become Credits over time, which flow into year-end balance and eventually into either carryforward (60%) or COI (40%).

* Frozen Meritcoin (post-departure) is retained for five years. After five years without re-entry, the balance is extinguished.

* Credits are drawable for two years post-departure. After two years, unspent Credits flow to COI.

## **16.4 Governance cycles**

Governance operates on overlapping cycles:

* Council session cycle: quarterly regular sessions, with extraordinary sessions called as needed for override decisions, recall hearings, or constitutional review.

* Council member term cycle: 1 year (cooperative), 2 years (municipal, regional). Half the Council rotates each year (in 2-year terms) to preserve institutional memory.

* Constitutional review cycle: every 5 years, the Adopting Community conducts a public review of the Recognition Rule, the BaseCost calibration history, the Council's override decisions, and the audit findings. The review is publicly published; participation is open to all Participants of Record.

* Trilogy correspondence cycle: as the Trilogy is written and updated, this Manual will be revised to maintain consistency. Manual revisions are versioned (v1.1, v1.2, etc.) and published with change logs.

**CHAPTER 17**

**Phase Graduation Gates**

Phases are not time-bound; they are gate-bound. An Adopting Community advances from Phase 1 to Phase 2 only when the graduation gates are satisfied. This prevents premature scaling — a pilot that has not yet demonstrated stability does not graduate, however long it has run.

## **17.1 Phase 1 → Phase 2 graduation gates**

Phase 1 (pilot, parallel operation with existing systems) graduates to Phase 2 (integration) when all of the following are satisfied:

* Operational stability. At least 24 consecutive months of operation with no Council-flagged audit failures and no MIEVM ensemble standoffs left undocumented.

* Recognition Rule maturity. The Recognition Rule has been applied to at least 90% of the Pilot Jurisdiction's eligible population. Edge cases (stateless persons, dual-recognition cases, complex residency situations) have documented resolutions.

* SCALULAR provider acceptance. At least 75% of SCALULAR services available in the Pilot Jurisdiction accept Credits, with documented service-level agreements.

* Council functionality. The Council has held at least 8 quarterly sessions, has executed at least one recall procedure (or has documented why none have occurred), and has resolved at least 95% of submitted disputes within their target windows.

* Audit clean record. Three consecutive quarterly audits with no non-correctable findings.

* Constitutional alignment. The Adopting Community has formally affirmed adherence to the Three Governing Principles, the Eight Immutable Ethical Principles, and the constitutional commitments in Part V of this Manual.

## **17.2 Phase 2 → Phase 3 graduation gates**

Phase 2 (integration) graduates to Phase 3 (full settlement) when all of the following are satisfied:

* Welfare program integration. Existing welfare programs have folded into Gracechain UBI as a single transfer, with the prior administering agencies either decommissioned or repurposed.

* Tax acceptance. The Pilot Jurisdiction's tax authority has formally accepted Meritcoin (via Credits) for tax payments, with documented procedures.

* Cross-border infrastructure. Dual Recognition Compacts with at least three other UBIMIA-deployed jurisdictions are signed and operational.

* Population coverage. At least 95% of the Pilot Jurisdiction's eligible population is enrolled as Participants of Record.

* Audit clean record. Six consecutive quarterly audits with no non-correctable findings.

* External validation. At least one independent third-party auditor (academic, civil society, or governmental) has reviewed the deployment and published a positive evaluation.

## **17.3 Failure paths**

Not every pilot graduates. The Manual specifies what happens when a pilot does not advance:

* Graduation gate not satisfied within 36 months. The Adopting Community publishes a formal review explaining why the gates were not met and what remediation is planned. The pilot continues; another graduation review occurs in 12 months.

* Persistent audit failures. If three consecutive quarterly audits show non-correctable findings, the pilot enters Remediation Status. Operations continue but no graduation review occurs until the findings are corrected.

* Constitutional drift. If the Adopting Community has revised practices that violate the Eight Immutable Ethical Principles or the Three Governing Principles, the pilot loses ERES Recognition. Operations may continue under the Adopting Community's authority, but the deployment is no longer a UBIMIA-recognized pilot. The community may re-apply for Recognition after demonstrating constitutional alignment.

* Adopting Community withdrawal. The Adopting Community may withdraw from the pilot at any time. Withdrawal triggers the migration procedures in Part I, Chapter 1 for affected Participants. Withdrawal does not prevent re-engagement in the future under a new Adopting Community.

**PART V**

**WHY**

*Constitutional Constraints*

 

*WHY answers the fifth question: which commitments are non-negotiable, which principles bind every operation, and which constraints no deployment may relax. WHY is the layer that distinguishes a UBIMIA deployment from a UBIMIA-flavored deployment that has quietly abandoned UBIMIA's core. Part V is the constitution.*

**CHAPTER 18**

**The Three Governing Principles, Operationalized**

The Three Governing Principles — SELF: don't hurt yourself; OTHERS: don't hurt others; FUTURE: build for generations to come — are not aspirational. They are operationally encoded in the architecture, with each principle mapped to a specific authorization-stack mechanism. This Chapter shows the mapping.

## **18.1 SELF — Don't hurt yourself**

The SELF principle is operationally encoded in DSAP-PRE's ρ\_RHC proxy. ρ\_RHC fires when the system in question is accelerating toward flatline — when its Resonant Harmony Cycle amplitude is decaying faster than κ\_RHC over a sustained window. A system in this state is hurting itself, in the sense that it is losing the structural variation that keeps it alive as a system.

Operationally, every authorization-bound action is checked against ρ\_RHC for the affected system. If ρ\_RHC fires, authorization is refused with REFUSAL\_REGIME\_TRANSITION. The action does not execute. The principle is enforced not by aspiration but by code: the system literally cannot complete the action that would hurt the affected substrate.

## **18.2 OTHERS — Don't hurt others**

The OTHERS principle is operationally encoded in DSAP-PRE's ρ\_PERT proxy. ρ\_PERT fires when the PERT distribution topology shows modality collapse, variance collapse beyond 50%, or viable-alternative collapse beyond 50%. These are signals that the system is foreclosing options for parties not represented at the negotiating table — that it is hurting others, in the sense that it is consuming the option space that other parties would need to maintain their own well-being.

As with ρ\_RHC, the encoding is operational. ρ\_PERT firing refuses authorization. The action does not execute. Adversarial actors who attempt to drive a system into collapse — by, for example, monopolizing decision modalities or by foreclosing alternatives that competitors would need — find that their authorizations are refused not by appeal to ethics but by the architecture's response to the topology of the system they are operating on.

## **18.3 FUTURE — Build for generations to come**

The FUTURE principle is operationally encoded in DSAP-PRE's ρ\_hyst proxy. ρ\_hyst fires when a hysteresis counterfactual shows that a reversal perturbation would not produce recovery within the η\_recover threshold over horizon τ. In plainer language: ρ\_hyst fires when an action is about to make the system irreversibly different — when the change cannot be undone within the recovery horizon.

Irreversibility is the defining concern of the FUTURE principle. A reversible change is, in principle, manageable: future generations can choose differently. An irreversible change forecloses their choice. The architecture refuses authorization for irreversible changes that have not been deliberately authorized at the constitutional level — meaning that ordinary operational actions cannot incidentally lock in irreversibility. Constitutional review is the only path to deliberate irreversibility.

**CHAPTER 19**

**The Eight Immutable Ethical Principles**

Beneath the Three Governing Principles sit eight more specific ethical commitments. They are immutable in the sense that no UBIMIA deployment may revise them; they are encoded in the ERES TERMS \#47 (ET\_AL) Locked Terms Registry. The Manual restates them here in operational form, with the sub-indices that contribute to the Ethical Resonance Index.

## **19.1 The eight**

| Principle | Operational Sub-Index |
| :---- | :---- |
| Sustainability — closed-loop self-correction | Waste-stream reduction over baseline |
| Transparency — public, written, auditable | Data-publication completeness ratio |
| Harm reduction — first do no damage | Documented adverse-event reduction |
| Measurable welfare — empirical, not asserted | Welfare metric trend over baseline |
| Dignity — survival not conditional | Dignity-indicator composite |
| Recognition — contribution acknowledged | Acknowledgement-coverage ratio |
| Reversibility — irreversibility requires highest authorization | Preserved-option-count metric |
| Pluralism — no single authority sets merit | Governance-diversity composite |

The eight sub-indices compose into the Ethical Resonance Index (ERI) under the weighted product specified in Part II Chapter 9.2. ERI feeds into the EAAP four-factor PoR computation; insufficient ERI refuses authorization. The principles are thereby operationally enforced, not merely asserted.

## **19.2 What 'immutable' means**

An immutable principle, in this Manual's usage, is one that cannot be revised by any deployment without breaking compatibility with UBIMIA. A deployment that revised any of the eight would, by definition, no longer be a UBIMIA deployment. It would be free to operate under a different name; the broader ERES community is not in a position to enforce naming rights. But the Manual's contract — and the contract that the Trilogy will articulate in book form — is that the eight are constitutional. Compliance is binary: a deployment honors all eight or it is not UBIMIA.

## **19.3 The right to fork as defense against capture**

Constitutional immutability is enforced not by a central authority but by the right to fork. UBIMIA is licensed under CCAL v2.1; the document layer is CC BY-SA 4.0; the code layer is MIT. Any community can fork the architecture and operate its own version. The original ERES community retains no veto over forks.

When a regime captures a local UBIMIA deployment and revises practices in directions that violate the Eight Principles, the Participants can — and should — fork. The fork inherits the architecture intact; the captured deployment is left to its own diminished membership. The right to walk away with the architecture is the ultimate guarantee that no single authority controls the system.

**CHAPTER 20**

**Civil Liberties as Constitutional Constraint**

UBIMIA must never function as a coercive social-credit regime. This is the constitutional commitment that distinguishes the architecture from every system that has used merit-tracking for behavior control. The Manual restates the commitment, then specifies its operational consequences.

| The Constitutional Constraint No rating system is valid under UBIMIA unless it protects the individual from exploitation and protects the commons from deception. The system measures externalities and institutional performance, not private life. Participation is voluntary and consent-based. Public auditability applies to aggregate flows; sensitive contribution detail is private by default. |
| :---- |

## **20.1 Voluntary participation**

No person may be compelled to participate in UBIMIA. The Recognition Rule may make UBI available to all eligible persons in the Pilot Jurisdiction, but acceptance is voluntary. A person who declines to enroll continues to live in the jurisdiction under whatever other arrangements obtain (existing welfare, market employment, family support, mutual aid). The decision is theirs.

Operationally, this means the Authority of Record has no enrollment quotas, no consequences for non-enrollment, and no surveillance of non-enrolled persons. The Participant Register lists only those who have voluntarily enrolled.

## **20.2 Privacy by default**

Sensitive contribution detail is private by default. A Participant who contributes through mental-health work, intimate caregiving, learning that touches private subjects, or any activity the Participant prefers private, has their contribution detail encrypted under the Custody Triad. The aggregate flow is public; the detail is not.

Selective disclosure is opt-in. A Participant may choose to disclose specific contributions for social recognition, or to receive a quality-weight bonus when the disclosure permits richer verification. The choice is the Participant's; declining to disclose carries no penalty.

## **20.3 Audit court protocol**

Encrypted contribution detail can be decrypted only under specified circumstances. The Audit Court protocol governs decryption requests:

| RUNBOOK  ·  Audit Court Decryption Procedure 1\.  An authorized requester (the GAIA Council, a court-of-law in a fraud investigation, or the Participant themselves) submits a decryption request to the Custody Authority. 2\.  The Custody Authority reviews the request against the published criteria. Non-conforming requests are refused with documented rationale. 3\.  Conforming requests are escalated to a Decryption Hearing before three Custody Authority members. The hearing is public unless the Participant requests privacy. 4\.  If the hearing approves decryption, two of the three custody-key shares are combined; the third (the Participant's) is required only if the Participant has consented. In non-Participant-consent cases (fraud investigation), the Custody Authority's share and the Trustee Registry's share suffice; the Participant is notified of the decryption. 5\.  Decrypted material is provided to the requester for the limited purpose specified. Custody Authority retains a record of the decryption event, posted to Gracechain (with the contents not posted). |
| :---- |

## **20.4 The right to fork, again**

Civil-liberties violations — surveillance creep, behavior-control drift, ideological capture — find their ultimate remedy in the right to fork. A community that experiences such violations does not need to win a political battle to restore the architecture; it can copy the architecture and start again, leaving the captured deployment to its diminished operators.

This is why the architecture is licensed under CCAL v2.1 with CC BY-SA 4.0 for documents and MIT for code. The licenses are themselves civil-liberties safeguards: they cannot be revoked, they cannot be refused, and they ensure that no community is ever locked into a deployment that has lost its way.

**PART VI**

**HOW**

*Procedures and Runbooks*

 

*HOW answers the sixth question: through which step-by-step procedures do the operations of UBIMIA actually run. This is the longest Part of the Manual, by design — procedures must be specified at step-level detail or they will be invented, inconsistently, by every implementer who needs them. Part VI removes that need.*

**CHAPTER 21**

**Contribution Verification, Step-by-Step**

This Chapter walks through a single contribution end-to-end, from the moment a Participant decides to claim credit for an action through the moment the resulting Meritcoin appears in the Participant's balance. Every step is specified; every record produced is referenced to its schema in Part II.

## **21.1 The full flow**

| RUNBOOK  ·  End-to-End Contribution Procedure 1\.  Participant performs the action. The action occurs in the real world: invasive species removal, mental health peer support, code review for an open-source project, anything within an authorized contribution domain. 2\.  Within 7 days of action completion, Participant submits a Claim via attestation booth. Schema in Part II §7.1. The Claim is signed by the Participant; submission timestamp is recorded; overlap rules are checked automatically. 3\.  Verifier(s) submit Verification(s). Each verifier independently submits a Verification record (Type A sensory, Type B witness, Type C institutional). Multiple verifications on the same Claim are permitted; the highest-weight Verification governs. Schema in Part II §7.2. 4\.  Authorization service runs DSAP-PRE check. The system\_boundary's three regime-transition proxies (ρ\_RHC, ρ\_PERT, ρ\_hyst) are evaluated. If composite returns 0, authorization refused with REFUSAL\_REGIME\_TRANSITION. The chain ends here. 5\.  Authorization service runs PoR computation. The four factors (A: Anchor Product, R: RHC Amplitude, P: EarnedPath Viability, F: Future-Map Convergence) are computed. The conjunctive product PoR \= A × R × P × F is compared against θ for the domain. If PoR \< θ, authorization refused with INSUFFICIENT\_POR. 6\.  MIEVM ensemble validates Factor A\_M. The Anchor Product's MIEVM concurrence factor is verified across the ensemble (Claude, ChatGPT, Grok, DeepSeek). ECR is computed; if below threshold (0.60 pilot, 0.75 production), authorization refused. 7\.  Authorization record produced. If all gates passed, an AuthorizationRecord (Part II §7.3) is signed and posted to Gracechain. The record includes all factor values, the DSAP-PRE clearance, the MIEVM ECR, and the freshness window. 8\.  Minting service computes magnitude. ΔR\_net is computed via weighted sum across the four BERA indices. quality\_weight is read from the verification type (1.0 / 0.8 / 0.6). Meritcoin minted \= floor(BaseReward × ΔR\_net × quality\_weight). 9\.  RCR record produced. The minting action is bound to a fresh RCR record (Part VI §29). The RCR record references the AuthorizationRecord and produces a unique audit anchor for the mint. 10\.  MintingRecord posted to Meritcoin ledger. Schema in Part II §7.4. The Participant's Meritcoin balance increases by the minted amount. 11\.  Participant notified. The attestation booth shows the new mint in the Participant's record. The Participant can verify the chain (Claim → Verification → Authorization → Minting) end-to-end through the booth interface. |
| :---- |

## **21.2 Worked example: ecological contribution**

To illustrate, consider a Participant who spends 18 hours over three days removing invasive species from a named forest patch. The forest patch has an active RCI oracle (Part II §9.4). The Participant's home jurisdiction is operating under Template A (cooperative) with BaseReward \= 10,000 Mc per 1.0 ΔR.

* Action: 18 person-hours of invasive removal in Forest Patch Alpha, May 10-12.

* Claim submitted May 13: claimant Alice (DID), domain ecological, system\_boundary 'Forest\_Patch\_Alpha', total\_person\_hours 18, witnesses Bob and Carol.

* Verifications: Bob and Carol each submit Type B witness verifications on May 14 (weight 0.8 each). The cooperative also submits Type C institutional verification on May 15 (weight 0.6, citing crew log entries).

* DSAP-PRE check on May 20: ρ\_RHC \= 0.05 (forest patch RHC is healthy), ρ\_PERT \= 0.10, ρ\_hyst \= 0.08. Composite \= (0.95 × 0.90 × 0.92) ≈ 0.79. DSAP-PRE returns 1 (no regime transition).

* PoR computation: A \= 0.85 (Anchor Product including MIEVM concurrence), R \= 0.78 (RHC amplitude healthy), P \= 0.82 (alternative paths exist), F \= 0.79 (Future-Map convergence good). PoR \= 0.85 × 0.78 × 0.82 × 0.79 \= 0.43. Domain threshold θ \= 0.40 (ecological standard). PoR ≥ θ. Authorized.

* MIEVM ECR \= 0.81 (above the 0.75 production threshold; this is a real ensemble attestation, not a pilot simplification). Authorization confirmed.

* Magnitude: ΔRCI measured by oracle \= \+0.041 over the 30-day window; ΔARI \= \+0.018; ΔERI \= \+0.012; ΔRHC \= \+0.008. Weighted sum with default weights: ΔR\_net \= 0.25 × 0.018 \+ 0.30 × 0.012 \+ 0.25 × 0.008 \+ 0.20 × 0.041 \= 0.0185. Quality weight 0.8 (highest verification type was Type B). Meritcoin minted \= floor(10,000 × 0.0185 × 0.8) \= 148 Mc.

* Distribution among Alice, Bob, Carol: weighted by hours × verification quality. Alice (18 × 0.8) \= 14.4; Bob (12 × 0.8) \= 9.6; Carol (6 × 0.6) \= 3.6. Total weighted: 27.6. Alice receives 148 × (14.4/27.6) ≈ 77 Mc; Bob ≈ 51 Mc; Carol ≈ 19 Mc.

The chain is auditable end-to-end. Any third-party auditor can re-run the oracle measurements, re-compute the PoR, re-verify the MIEVM ECR, and confirm that the mint amount equals the formula applied to the verified inputs.

**CHAPTER 22**

**Dispute Adjudication**

Disputes arise. A Participant claims a contribution that another Participant believes was theirs; a witness contradicts a Claim; an institution's verification is challenged as fraudulent. The Manual specifies how disputes are handled, with the goal of resolving them without conferring discretionary power on any single body.

## **22.1 Filing a dispute**

Any Participant in good standing may file a dispute against any Claim, Verification, Authorization, or MintingRecord within 14 days of the record being posted to Gracechain. The dispute filing schema:

| SCHEMA  ·  Dispute {   dispute\_id: string,   filer: string (Participant DID),   target\_record\_id: string (Claim, Verification, Authorization, or MintingRecord ID),   category: enum (false\_claim | false\_verification | computation\_error |                    eligibility\_violation | other),   evidence: string or evidence\_hash (private; encrypted via Custody Triad),   rationale: string (public summary, no sensitive detail),   filing\_timestamp: ISO8601,   signature: cryptographic signature by filer } Constraints:   filing\_timestamp ≤ target\_record posted\_timestamp \+ 14 days,   filer.status \= active and not under sanction |
| :---- |

## **22.2 Initial review**

Within 7 days of filing, the Authority of Record performs initial review:

* Standing check. Is the filer in good standing? If not, the dispute is dismissed with notice.

* Timeliness check. Was the dispute filed within the 14-day window? If not, dismissed.

* Substance check. Does the rationale articulate a coherent dispute category? If not, the filer is given 7 days to amend; if not amended, dismissed.

* Frivolousness check. Has the filer filed more than three disputes in the past 90 days that were determined frivolous? If so, the dispute requires 5 Mc Bond posted by the filer; if the dispute is determined frivolous, the Bond is forfeited.

Disputes that pass initial review proceed to the adjudication procedure.

## **22.3 Adjudication procedure**

| RUNBOOK  ·  Dispute Adjudication 1\.  The Authority of Record selects three jurors by weighted lottery from the GAIA Council jury pool. Jurors must have ΔR\_contributor \> 0.2 and no conflict of interest (not the filer, not the target Participant, not an institution involved). 2\.  Jurors are notified. They have 30 days to convene; jurors who decline are replaced by the next candidates in lottery order. 3\.  The hearing is convened. Both filer and target are notified at least 14 days before hearing. Each may submit written statements and may attend the hearing in person or via verified telepresence. 4\.  Evidence is presented. If sensitive evidence is involved, the Custody Triad decryption procedure (Part V §20.3) is invoked, with the jurors as authorized recipients of the decrypted material. 5\.  Jurors deliberate privately. Deliberation is confidential; no transcript is produced. Outcomes are decided by simple majority (2 of 3). 6\.  Outcome is published. Possible outcomes: Mint As Claimed (target record stands); Mint Reduced (50% of original); Reject (record reversed; if MintingRecord, Meritcoin clawed back); Fraud Found (record reversed plus 2× Meritcoin clawback or equivalent penalty plus 180-day suspension of minting rights for the offender). 7\.  Appeal window opens. Either party may appeal within 14 days to a 7-member GAIA Council panel (different members from the original three jurors). Appeal decision is final. 8\.  Implementation. The Authority of Record updates Gracechain to reflect the outcome. Affected ledger states are corrected. Compensation flows (juror compensation: 5 Mc per juror per hearing; appeal panel: 10 Mc per member if convened) are paid from COI. |
| :---- |

## **22.4 What jurors are deciding**

Jurors are not deciding what is true in some absolute sense; they are deciding whether the architecture's rules were applied correctly to the specific facts of the case. The questions before them are operational:

* Was the Claim submitted within the 7-day window?

* Did the Verification(s) come from non-collusive sources?

* Were the system\_boundary and time\_window correctly identified?

* Does the evidence support the claimant's role in the action?

* Were the PoR computation and ΔR\_net calculation correct?

This narrowing of the juror role — from truth-finding to rule-application — is what makes adjudication scalable. Jurors are not philosophers or judges; they are rule-checkers, drawing on their own contribution-rich background to identify whether a rule was honored.

**CHAPTER 23**

**Council Procedures**

The GAIA Council holds limited authority within UBIMIA. This Chapter specifies the procedures by which the Council exercises that authority — convening sessions, voting on overrides, conferring Verification Authority, and conducting recall hearings.

## **23.1 Regular session procedure**

| RUNBOOK  ·  Quarterly Council Session 1\.  Agenda published 14 days before session. Agenda includes: review of past quarter operations, override decisions on the docket, Verification Authority applications received, recall petitions in process, audit findings to date, and new business. 2\.  Public attendance opens at session start. The session is recorded; the recording is posted to Gracechain after the session. 3\.  Operations review: the Authority of Record presents quarterly metrics (enrollment, UBI distribution, Bill volumes, mint counts, refusal counts, disputes resolved). 4\.  Override decisions: each agenda override is presented with rationale, public comment is received (each speaker limited to 3 minutes), the Council deliberates publicly, votes are recorded by name. 2/3 majority required for override; otherwise the algorithmic core's output stands. 5\.  Verification Authority decisions: applications for new Authority and revocations are voted on by simple majority. 6\.  Recall petitions: any recall petition that reached threshold is processed, with the affected member recused from the vote. 7\.  New business: motions from Council members or from Participants (presented through a member sponsor). Motions follow standard parliamentary procedure. 8\.  Compensation accrual: each member's session attendance is recorded, contributing to Meritcoin compensation per Part I §3.5. |
| :---- |

## **23.2 Override procedure in detail**

The override authority is the most consequential power the Council holds. It allows the Council, by 2/3 majority and with 30-day public notice, to override an algorithmic-core output when the override is justified by documented failure of the rule under specific circumstances. The procedure requires care:

| RUNBOOK  ·  Algorithmic Core Override 1\.  A Council member or a Participant (through a member sponsor) files an Override Proposal stating: the specific algorithmic-core output to override, the proposed alternative output, the documented failure justifying override, and the limit of the override (one-time, time-bounded, or rule-revising). 2\.  The Override Proposal is published on Gracechain for 30 days of public notice. During this period, comments are received from any Participant. 3\.  At the next regular Council session (or an extraordinary session if the override is time-sensitive), the Proposal is debated. The Council member sponsoring the Proposal speaks first; a designated dissent speaker (if any) speaks next; public comment follows. 4\.  Vote occurs by name. 2/3 majority of the full Council (not 2/3 of those present) is required for the Override to pass. Abstentions count as no. 5\.  If passed: the alternative output is applied; the override record is posted to Gracechain with the rationale, vote tally, and limit; affected operations are recomputed. 6\.  If failed: the algorithmic-core output stands; the failed Proposal is recorded with the vote tally; the proposer may re-file after 90 days with revised rationale. 7\.  Annual review: at the end of each year, the Council publishes an Override Review summarizing all overrides issued, their stated limits, and whether the limits were honored. Patterns of override that resemble rule-revision (rather than rule-application failure) are flagged for constitutional review. |
| :---- |

**CHAPTER 24**

**Verification Authority Procedures**

The procedures for conferring, maintaining, and revoking Verification Authority were sketched in Part I, Chapter 5\. This Chapter supplies the operational detail.

## **24.1 Application processing**

The Authority of Record processes Verification Authority applications:

| RUNBOOK  ·  Verification Authority Application Processing 1\.  Application received with required materials: legal status documentation, activity description, authorized representatives, proposed Operational Bond. 2\.  Authority of Record performs initial completeness check. Incomplete applications are returned with specific deficiencies identified; applicant has 30 days to amend. 3\.  Complete applications are published on Gracechain for 30-day public comment. The Authority of Record solicits comments through standard channels (community announcements, online posting). 4\.  Public comments are summarized in a comment report attached to the Application packet. No comment is suppressed; comments are summarized for the Council's consideration. 5\.  At the next regular Council session, the Application is presented. Council deliberates, votes by simple majority (with rationale for negative votes recorded). 6\.  On approval: the applicant posts the Operational Bond. The Bond posting is recorded on Gracechain. Verification Authority becomes effective 14 days after Bond posting (allowing time for any outstanding objections to be filed). 7\.  On rejection or deferral: the Council's rationale is delivered to the applicant in writing. The applicant may re-apply after 180 days with revised materials, or appeal the rejection through the standard appeal procedure. |
| :---- |

## **24.2 Quarterly attestation logging**

Every institution holding Verification Authority must publish a quarterly attestation log. The schema:

| SCHEMA  ·  AttestationLog {   log\_id: string,   institution: string (DID),   quarter: string (e.g., '2026-Q3'),   verifications\_issued: integer (count),   verifications\_by\_domain: { domain\_name: count, ... },   authorized\_representatives\_active: \[string, ...\] (DIDs),   bond\_balance: integer (current Operational Bond size),   publication\_timestamp: ISO8601,   signature: cryptographic signature by institution } Constraints:   publication\_timestamp ≤ quarter\_end \+ 30 days,   verifications\_issued \= sum(verifications\_by\_domain.values()) |
| :---- |

## **24.3 Annual audit procedure**

| RUNBOOK  ·  Verification Authority Annual Audit 1\.  On the institution's audit anniversary, the Council assigns an audit team of three members. Audit team members may not be affiliated with the audited institution. 2\.  Audit team requests a sample of verifications from the past year. The sample is randomly selected from the institution's quarterly logs, sized at minimum 5% of total verifications or 10 verifications, whichever is greater. 3\.  Audit team examines each sampled verification: the Verification record on Gracechain, the underlying activity record (provided by the institution), and any cross-references with other ledger state. 4\.  Findings are categorized: Concordant (record matches), Discrepant (administrative error, correctable), or Fraudulent (intentional false certification). 5\.  Audit Report is drafted with findings and recommendations. The institution receives a draft for response within 30 days. 6\.  Final Audit Report is published on Gracechain. Concordant findings produce a Clean Audit Status. Discrepant findings produce a Notice; three Notices in five years reduce the institution's Operational Bond by 25%. Fraudulent findings produce immediate Bond slashing and Verification Authority revocation. |
| :---- |

**CHAPTER 25**

**Recall by Petition**

Recall is the procedure by which Participants remove a Council member, an Authority of Record, or another body from their position before the end of their term. This Chapter specifies the operational detail.

## **25.1 What is recallable**

Three positions are recallable through this procedure:

* Council member, by petition signed by the threshold percentage of Participants (Part I §3.2).

* Authority of Record representative (a specific person, not the office itself), by petition signed by the threshold percentage.

* Custody Authority member, by petition signed by the threshold percentage with additional requirement of ΔR\_contributor \> 0.3 for all signatories.

The Authority of Record office itself is not recallable through this procedure; replacement of the office (e.g., from a cooperative to a municipal authority) requires the Recognition Rule revision procedure.

## **25.2 Recall procedure**

| RUNBOOK  ·  Recall by Petition 1\.  A Participant or group drafts a recall petition stating the target's name, role, and the rationale for recall. Rationale must include specific actions or omissions; vague rationales (general dissatisfaction) are insufficient. 2\.  Petition is published on Gracechain. Signature collection begins immediately and runs for 30 days. 3\.  Each signature includes the signer's DID, signature timestamp, and (for Custody Authority recalls) the signer's verified ΔR\_contributor. 4\.  The Authority of Record tallies signatures continuously. The current count is published on Gracechain daily. If the threshold is reached before 30 days, signature collection continues until the deadline (additional signatures are recorded but do not affect outcome). 5\.  At the 30-day deadline, the Authority of Record certifies the result. If the threshold was met or exceeded, the recall is successful and the target's term ends immediately. 6\.  Successor selection: for Council members, the next candidate in the original lottery order serves the remainder of the original term. For Authority of Record representatives, the Authority designates a replacement subject to Council confirmation. For Custody Authority members, the Custody Authority designates a replacement subject to Council confirmation. 7\.  The recalled person is ineligible for re-selection to the same role for a period equal to twice the original term length. They retain Participant status and may run for other roles after a 90-day cooling period. |
| :---- |

## **25.3 Frivolous-recall protection**

Recall procedures can be weaponized — flooded with frivolous petitions to harass office-holders. The architecture protects against this:

* Each recall petition requires 5 Mc Bond posted by the petition drafter. The Bond is refunded if the recall succeeds; forfeited (returned to COI) if the recall fails to reach threshold.

* A Participant who has filed three failed recall petitions in 12 months loses recall-petition standing for 24 months.

* Patterns of recall-petition abuse (multiple petitions targeting the same office-holder for the same alleged action, after the first fails) are flagged by the Authority of Record for Council review and may trigger recall-petitioner sanction.

* Recall petitions cannot be filed against an office-holder within 90 days of their assumption of office (a grace period) or within 90 days of a prior failed recall petition against the same office-holder (a cooling period).

**CHAPTER 26**

**Calibration Procedures**

UBIMIA's parameters are not free constants — they are calibrated against observed pilot data through documented procedures. This Chapter specifies the calibration procedures for each parameter.

## **26.1 BaseCost(T) calibration**

BaseCost is recalibrated monthly by the algorithmic core, using the formula in the FULL §15:

**BaseCost(T)\_new \= BaseCost(T)\_old × (TotalMintedMc\_window / TotalDemand\_window) × 0.95**

Where the window is the trailing 30 days for monthly recalibration, the 0.95 factor is the deflationary bias, and the 25% volatility cap is applied if the new value differs from the old by more than 25%. The calibration runs deterministically; no human discretion is exercised at this layer.

## **26.2 CR (Conversion Rate) calibration**

CR is set annually, published 90 days before year-end (Day 275). The formula:

**CR \= TotalMintedMc\_year / TotalCreditsIssued\_target**

Where TotalMintedMc\_year is the accumulated Meritcoin minted during the year ending at recalibration, and TotalCreditsIssued\_target is the GAIA-set target for total Credits to be issued in the upcoming year (calibrated to projected SCALULAR demand). The 25% volatility cap applies to the year-over-year change in CR.

## **26.3 θ (authorization threshold) calibration**

θ is the domain-specific authorization threshold for the EAAP four-factor PoR. Initial values are calibrated by domain and pilot scale; revisions follow the procedure:

| RUNBOOK  ·  θ Calibration Revision 1\.  Council member or audit team identifies a pattern in PoR refusals or authorizations that suggests miscalibration (too many authorizations resulting in disputes, or too many refusals that retrospectively appear correct). 2\.  A θ Revision Proposal is drafted citing the specific data, the proposed new θ value, and the rationale. 3\.  The Proposal is published for 30 days of public comment. 4\.  At the next regular Council session, the Proposal is debated. Revision requires 2/3 majority (treated as an Override Proposal, since θ is part of the algorithmic core). 5\.  If passed, the new θ takes effect after a 30-day transition window. During the transition, both the old and new θ are computed; authorizations are made using the old θ; the new θ is used only for monitoring. 6\.  After the transition, the new θ is applied. Six months after the change, the Council reviews the impact and either confirms the revision or proposes further adjustment. |
| :---- |

## **26.4 DSAP-PRE proxy calibration**

The DSAP-PRE proxy parameters (κ\_RHC, η\_recover, τ, W\_RHC, W\_PERT, κ\_cost) are reviewed semi-annually (Day 180 and Day 365). The reference calibration values from the architectural FULL §6:

| Parameter | Standard Governance | Strategic |
| :---- | :---- | :---- |
| κ\_RHC | 0.01/hr² | 0.005/day² |
| W\_RHC | 3 cycles | 3 cycles |
| W\_PERT | 5 evaluations | 5 evaluations |
| κ\_cost | 3.0 | 4.0 |
| τ | 10 cycles | 10 cycles |
| η\_recover | 0.15 | 0.20 |

Revisions follow the same procedure as θ revisions: documented rationale, 30-day public comment, Council 2/3 majority, 30-day transition window, 6-month post-revision review.

## **26.5 Domain weights**

The BERA index weights (w\_ARI, w\_ERI, w\_RHC, w\_RCI) are reviewed quarterly by the Council. Revisions require simple majority (not 2/3, since these are reward-magnitude parameters rather than authorization parameters). The constraint that weights sum to 1.0 is invariant; a revision adjusts the proportional balance among the four indices.

Domain weight revisions are reflected in the next annual BaseReward setting, not retroactively. A Participant whose contributions were minted under prior weights retains the prior values; new contributions are minted under the new weights.

**CHAPTER 27**

**Audit and Reporting**

Audit is the activity by which the architecture's integrity is verified by parties not part of its operation. UBIMIA's design assumes hostile audit — that auditors will look hard for violations — and is structured so that violations cannot hide. This Chapter specifies the audit procedures.

## **27.1 Continuous audit invariants**

Three invariants from Part II §6.4 are checked continuously by the algorithmic core. Any violation triggers an immediate flag and notifies the Authority of Record and the Council. These are:

* Conservation. Sum of Meritcoin balances \+ in-transit equals cumulative net minting. Computed at every state transition; logged at every block.

* Authorization closure. Every minting record references a fresh, valid authorization. Verified at minting time and re-verified during quarterly audits.

* Identity continuity. Every active Participant has at least three Trustees on file. Verified at enrollment, at each Trustee change, and at quarterly audits.

## **27.2 Quarterly audit**

Every quarter, the Authority of Record conducts a quarterly audit. The audit covers:

* All MintingRecords in the quarter: chain integrity (Claim → Verification → Authorization → Minting), formula correctness, oracle measurements re-verifiable from public data.

* All Bill payments in the quarter: RPA pricing applied correctly, RCR records present and fresh.

* All COI flows in the quarter: 60/40 split correctly applied, COI pool magnitude correctly computed, BaseCost adjustments correctly derived.

* All Verification Authority operations in the quarter: institutional logs published on time, sampled verifications concord with underlying activity records.

* All Council decisions in the quarter: vote tallies correctly recorded, Override rationales documented, recall petitions correctly tallied.

The quarterly audit produces a public Audit Report posted to Gracechain. Findings are categorized as Concordant, Discrepant, or Fraudulent (parallel to Verification Authority audits). Three consecutive quarters of non-Concordant findings trigger Remediation Status.

## **27.3 Annual external audit**

In addition to quarterly internal audits, an annual external audit is conducted by an independent third party. The external auditor is selected by the Council from a published roster of qualified auditors (academic institutions, civil-society organizations, or independent professional auditors). The same auditor cannot be selected for more than two consecutive annual audits.

The external audit produces an Annual Audit Report that is publicly published. The Report is required for graduation gate satisfaction (Part IV §17): a Phase 2 graduation requires three consecutive years of clean external audits; a Phase 3 graduation requires six.

## **27.4 Whistleblower protections**

Any Participant who identifies a potential audit failure may file a Whistleblower Notice. The protections:

* The whistleblower's identity is held in confidence by the Authority of Record. Confidentiality is breached only if the whistleblower consents.

* Whistleblowers are immune from sanctions for filing in good faith, even if the alleged violation is not substantiated.

* Whistleblowers who filed substantiated notices receive a Recognition Reward — 50 Mc plus public acknowledgment (with consent), drawn from the COI pool.

* Frivolous or malicious whistleblower filings (more than three unsubstantiated filings in 12 months) trigger sanction review by the Council.

These protections are constitutional. They cannot be revised by deployment-specific decisions; the architecture's defense against capture depends on the integrity of the whistleblower channel.

**PART VII**

**WITH**

*Tools, Budget, Procurement*

 

*WITH answers the seventh question — the question that completes the AD\_ON-AI \== UuuuuU principle. With which tools, with which budget envelope, with which procurement guidance, does the deploying community actually acquire what UBIMIA needs. Without WITH, the other six questions describe a thing nobody can actually build.*

**CHAPTER 28**

**Software Stack**

UBIMIA-compliant deployments do not require novel cryptographic research, novel consensus algorithms, or novel programming languages. The architectural commitments can be honored using existing open-source components composed in specific ways. This Chapter specifies what an Adopting Community needs to acquire and configure.

## **28.1 Persistence layer (Gracechain anchor)**

Recommended options for the persistence layer, in order of typical Adopting Community fit:

| Option | Best fit | Pros | Trade-offs |
| :---- | :---- | :---- | :---- |
| Ethereum L2 (Optimism, Arbitrum) | Municipal, Regional | Mature, low cost per anchor | Public chain; some governance through L1 |
| Filecoin \+ IPFS | Cooperative, Municipal | Decentralized storage, content-addressed | Higher complexity; retrieval latency |
| Sovereign-operated public ledger | Regional | Full jurisdictional control | Setup cost; ongoing operations |
| Tendermint-based custom chain | Municipal, Regional | Mature BFT consensus | Validator-set governance overhead |
| Append-only signed log \+ periodic checkpoint | Cooperative pilot | Simplest possible | Less robust against operator compromise |

The choice is local. The contract (Part II §11.3) is universal: append-only writes, geographic distribution of state, cryptographic auditability through Merkle structures or equivalents, signed checkpoints published openly. Any of the options above can satisfy the contract; choosing among them is a matter of operational fit, regulatory environment, and cost tolerance.

## **28.2 Authorization service**

The authorization service implements EAAP. The recommended architecture is a stateless service with the following components:

* DSAP-PRE evaluator. Implements the three regime-transition proxies. Pure computation; no external state required beyond the system\_boundary's measurement window.

* PoR computer. Computes Factor A (Anchor Product, including MIEVM concurrence call), Factor R (RHC oracle call), Factor P (EarnedPath service call), Factor F (Future-Map convergence service call). Each factor source is an independent service; the PoR computer aggregates.

* MIEVM ensemble client. Calls the canonical four lineages (Claude, ChatGPT, Grok, DeepSeek) in parallel, computes ECR, returns the concurrence result. Pilot deployments may use a single-lineage client with the ensemble call mocked to a constant high-confidence value, with the deviation documented.

* Authorization writer. Composes the AuthorizationRecord schema and posts to Gracechain. Returns the record ID and freshness window.

Each component can be implemented as a small service in any modern language. Reference implementations in Rust, Python, and TypeScript are available in the ERES Institute GitHub organization, under MIT license.

## **28.3 BERA oracle implementations**

The four BERA index oracles (ARI, ERI, RHC, RCI) are domain-specific and require integration with the data sources the Adopting Community has access to:

* **ARI oracle:** Computes inverse-normalized response variance times absorbed perturbation magnitude. Data sources depend on domain — for ecological systems, NDVI satellite imagery, soil moisture sensors; for social systems, response-time analytics from civic processes; for healthcare, patient-flow analytics.

* **ERI oracle:** Computes weighted product across eight sub-indices. Each sub-index has its own data sources — sustainability sub-index from waste-stream measurements, transparency sub-index from data-publication completeness ratios, and so on.

* **RHC oracle:** Computes normalized periodic amplitude with flatline detection. Data sources depend on domain; for ecological systems, time-series sensor data; for social systems, civic engagement cycles.

* **RCI oracle:** Computes P\_Ω\_norm × ARI\_sys × VibConst, with sliding-window autocorrelation as the persistence proxy. The most directly implementable of the four oracles; reference implementation in 200 lines of Python with pandas time-series support.

The Adopting Community can deploy oracle implementations from the ERES Institute reference suite or develop jurisdiction-specific implementations. The contract is the schema (Part II §9); the implementation choice is local.

## **28.4 Identity layer (DIDs and recovery)**

Recipient-anchored identity uses Decentralized Identifiers (DIDs) as the underlying identifier scheme. The choice of DID method is local — did:web for centralized-but-portable identifiers, did:key for cryptographic minimalism, did:ion for Sidetree-anchored ledger-independence. Each method has trade-offs documented in W3C DID Method Registry.

Trustee recovery is implemented above the DID layer. The Trustee Registry maintains, for each Participant DID, the list of designated Trustees. Recovery procedure (Part I §4) operates on the Registry, not on the underlying DID method. This means the Adopting Community can change DID methods without breaking trustee recovery, and conversely.

## **28.5 Encryption-key custody**

Custody Triad implementation:

* Participant share. Held in the Participant's personal device (mobile wallet, hardware security key, paper backup). Implementation uses standard wallet libraries (e.g., libsodium, BIP-39 seed phrases for paper backup).

* Trustee Registry share. Held in the Authority of Record's hardware security module. Single key distributed across the three Trustees using Shamir Secret Sharing (3-of-3 reconstruction required).

* Custody Authority share. Held in the Custody Authority's hardware security module, in a sealed-room facility (Part III §13.5).

Decryption requires concurrence: Participant alone if the Participant initiates; two of three (Custody Authority \+ Trustee Registry, or Participant \+ Custody Authority, or Participant \+ Trustee Registry) for authorized non-Participant requests. The cryptographic primitives are standard; threshold cryptography libraries (e.g., FROST, threshold-Ed25519) provide the underlying mechanics.

## **28.6 Booth and front-end software**

The attestation booth front-end is the Participant-facing interface to UBIMIA. Recommended properties:

* Open-source. Source code published; community can audit, fork, modify.

* Accessibility-compliant. Meets WCAG 2.1 Level AA at minimum; supports screen readers, keyboard navigation, multiple languages.

* Offline-capable. Booth functions in disconnected mode with batched sync to Gracechain when connectivity is restored.

* Verifiable. Booth software builds reproducibly from source; release artifacts are signed and verifiable.

Reference implementations are available in the ERES Institute GitHub organization. Adopting Communities are encouraged to fork and customize for jurisdiction-specific needs (language, regional accessibility standards, integration with local civic systems).

**CHAPTER 29**

**Hardware and Infrastructure**

UBIMIA does not require exotic hardware. The most demanding requirements are at the sealed-room custody perimeter; the rest of the deployment uses commodity hardware in standard configurations.

## **29.1 Sealed-room hardware**

The sealed-room facility houses hardware security modules holding the most sensitive cryptographic material. Specifications:

* HSMs. Commercial hardware security modules (Thales, Yubico, AWS CloudHSM, or equivalent) with FIPS 140-2 Level 3 or higher certification. Two HSMs in active-passive configuration; failover tested quarterly.

* Air-gap perimeter. The HSMs do not connect to general-purpose networks. Communication with the broader system uses one-way data diodes for outbound state, with inbound configuration changes requiring physical media handed in via the two-person procedure.

* Environmental monitoring. Temperature, humidity, motion, and door-status sensors; logs streamed to Gracechain via the diode.

* Physical access control. Two-person concurrence required for entry; both parties' identities are biometrically verified; entry logs include both parties' identities and the duration of access.

* Backup HSMs. A backup pair is held in a geographically distinct facility with the same specifications. The backup is updated through documented synchronization runs (typically quarterly) using the two-person procedure.

## **29.2 Booth hardware**

| COOPERATIVE  ·  N≈200 Single shared kiosk plus members' personal devices. Kiosk: $2,000 one-time \+ $200/year. Personal device app: free. | MUNICIPAL  ·  N≈10,000 5-10 distributed kiosks (one per population center) plus app. Kiosk total: $20,000-40,000 one-time \+ $4,000/year maintenance. | REGIONAL  ·  N≈250,000 30-100 kiosks across the region plus app. Kiosk total: $120,000-400,000 one-time \+ $30,000-80,000/year maintenance. |
| :---- | :---- | :---- |

Kiosks are touchscreen tablets in tamper-resistant enclosures, networked over standard cellular or wired connections. The hardware is commodity; the security is in the software stack and the back-end attestation procedures.

## **29.3 Sensor and oracle infrastructure**

Where BERA oracles depend on physical sensor data (ecological monitoring, healthcare flow analytics), the Adopting Community can either:

* Use existing public sensor networks (NOAA, USGS, public-health surveillance) that publish data in machine-readable format with cryptographic provenance.

* Deploy jurisdiction-specific sensors where existing networks are insufficient. Costs vary widely; a single ecological-monitoring sensor (water quality, soil moisture) costs $200-2,000 plus connectivity.

* Contract with a third-party sensor-data provider for specific domains. The Adopting Community must verify that the provider's data is auditable and that the provider does not gain undue influence over MintingRecord outcomes.

For pilots, the recommended approach is to start with existing public sensor networks where available, supplemented by carefully selected jurisdiction-specific sensors for domains the public networks don't cover. Building a comprehensive sensor infrastructure from scratch is not required and would likely delay deployment unnecessarily.

**CHAPTER 30**

**Budget Envelopes**

This Chapter specifies the all-in budget envelopes for the three pilot scales, including software, hardware, personnel, and operations. Numbers are 2026 USD-equivalent; Adopting Communities should adjust for local cost of living and labor markets.

## **30.1 Cooperative pilot (N≈200)**

| Cost category | One-time (Year 0\) | Annual (Year 1+) |
| :---- | :---- | :---- |
| Software setup (config, integration, testing) | $15,000 | — |
| Hardware (kiosk \+ HSM minimum) | $8,000 | $1,500 |
| Sealed-room (shared lease in existing facility) | $5,000 | $3,000 |
| Authority of Record staffing (0.25 FTE) | — | $15,000 |
| Council compensation (5 members in Mc, valued) | — | $3,000 |
| External audit (annual) | — | $5,000 |
| Misc. operations | $3,000 | $3,000 |
| TOTAL | $31,000 | $30,500 |

## **30.2 Municipal pilot (N≈10,000)**

| Cost category | One-time (Year 0\) | Annual (Year 1+) |
| :---- | :---- | :---- |
| Software setup | $60,000 | — |
| Hardware (5-10 kiosks \+ dedicated HSM pair) | $80,000 | $8,000 |
| Sealed-room (dedicated lease) | $30,000 | $24,000 |
| Authority of Record staffing (2 FTE) | — | $140,000 |
| Council compensation (9 members in Mc, valued) | — | $15,000 |
| External audit (annual) | — | $25,000 |
| Sensor infrastructure (jurisdiction-specific) | $40,000 | $8,000 |
| Misc. operations | $15,000 | $15,000 |
| TOTAL | $225,000 | $235,000 |

## **30.3 Regional pilot (N≈250,000)**

| Cost category | One-time (Year 0\) | Annual (Year 1+) |
| :---- | :---- | :---- |
| Software setup | $300,000 | — |
| Hardware (50-100 kiosks \+ redundant HSM clusters) | $600,000 | $60,000 |
| Sealed-room (dedicated facility, two sites) | $200,000 | $120,000 |
| Authority of Record staffing (15 FTE) | — | $1,200,000 |
| Council compensation (15 members in Mc, valued) | — | $50,000 |
| External audit (annual) | — | $120,000 |
| Sensor infrastructure | $300,000 | $60,000 |
| Misc. operations \+ community engagement | $100,000 | $80,000 |
| TOTAL | $1,500,000 | $1,690,000 |

## **30.4 What is not in the budget**

Three categories are deliberately excluded from these envelopes, because they vary too widely to estimate at this Manual's level:

* UBI distributions themselves. The cost of UBI is the cost of UBI; it is the policy choice the Adopting Community is making, not an infrastructure overhead.

* Patriot Dividend funding. If the Adopting Community deploys Patriot Dividend, the funding source (sovereign wealth, public revenues, natural-resource royalties) is jurisdiction-specific.

* SCALULAR provider reimbursements during Phase 1 transition. In Phase 1, existing SCALULAR providers (clinics, legal aid, schools) accept Credits but receive fiat reimbursement from a transition fund. The size of this fund depends on the Adopting Community's existing service infrastructure.

These costs should be evaluated separately by the Adopting Community as part of policy planning, not as infrastructure procurement.

**CHAPTER 31**

**Procurement Guidance**

UBIMIA's architectural commitment to civil liberties and to the right to fork has procurement consequences. A deployment that depends on a single proprietary vendor for any constitutional component is at risk of capture by that vendor. This Chapter specifies the procurement principles and the practical guidance for honoring them.

## **31.1 Vendor-neutrality requirements**

For every constitutional component, the Adopting Community must:

* Use software with source code available for audit. Closed-source components are permitted only at the periphery (e.g., a commercial accessibility tool used by the booth front-end), never at the core.

* Use open standards where standards exist. JSON Schema for record formats, DID methods for identity, signed Merkle structures for ledger anchoring.

* Avoid single-vendor lock-in. No single vendor should be in a position where withdrawing their service would prevent the Adopting Community from operating UBIMIA.

* Maintain exit paths. For every commercial relationship, document how the Adopting Community would migrate away from the vendor if necessary, including data export procedures and operational substitutes.

## **31.2 Recommended procurement procedure**

| RUNBOOK  ·  UBIMIA Component Procurement 1\.  Identify the component need. State the contract (the schema, interface, and behavioral guarantees the component must honor). Reference the Part II Chapter that specifies the contract. 2\.  Survey available implementations. Open-source first (ERES Institute references, community projects); commercial options second. 3\.  Evaluate against the four vendor-neutrality criteria. Filter out options that fail any criterion. 4\.  Solicit competing proposals. At least two distinct vendors or two distinct deployment architectures (e.g., self-host vs. managed) must be evaluated. 5\.  Conduct a security review. The proposed solution is reviewed by an independent security professional or community audit team. Findings are public. 6\.  Make selection. Document the selection rationale on Gracechain, including why alternative options were not chosen. 7\.  Implement with a published migration plan. The migration-away path is documented at deployment time, not deferred. This document is part of the procurement record. 8\.  Annual review. Each procurement is reviewed annually for continued vendor neutrality. If the vendor landscape has shifted (e.g., the chosen vendor has been acquired by an incompatible parent), the migration plan is exercised. |
| :---- |

## **31.3 The MIEVM ensemble as procurement test case**

The MIEVM ensemble is the most consequential procurement decision an Adopting Community makes, because it determines who can self-certify Factor A\_M. The Manual's guidance:

* Adopt the canonical four lineages (Claude, ChatGPT, Grok, DeepSeek) as the starting ensemble, unless the Adopting Community has specific reasons to prefer alternatives.

* Document the four-property defense (Part I §2.2) as the rationale. Each lineage is justified against independence of training, diversity of optimization, API provenance, and adversarial review.

* Maintain rotation eligibility. Establish a procedure for adding new lineages (after they demonstrate the four properties) and retiring lineages that fail (after demonstrated failure of any property).

* Avoid corporate concentration. At least three of four ensemble members must be operated by distinct organizations. If consolidation in the AI industry reduces this diversity, the Adopting Community must adjust the ensemble or document the deviation.

## **31.4 What an Adopting Community should not procure**

Three categories are inappropriate for procurement and should be developed in-house, contributed back to the open-source commons, or done without:

* Constitutional language. The Recognition Rule, the constitutional commitments, the relationship with the Three Governing Principles — these are constitutional acts of the Adopting Community, not products to be purchased from a vendor.

* MIEVM ensemble selection. The choice of which lineages constitute the ensemble is constitutional; outsourcing it to a vendor would violate the architectural commitment to plurality.

* Audit body. The annual external auditor must be selected by the Council from a published roster, not contracted from a single vendor. The procurement here is for audit services from a specific qualified auditor, not for an audit-vendor relationship.

**BACK MATTER**

*Appendices and References*

**APPENDIX A**

**Schema Reference**

This Appendix consolidates the schemas defined throughout the Manual into a single reference. Implementers should refer to the formal JSON Schema definitions published as ERES-UBIMIA-SCHEMAS-2026-001 for byte-level specifications.

| SCHEMA  ·  ParticipantRecord (Part II §6.3) { participant\_id, authority\_of\_record, recognition\_rule,   enrolled\_date, status, trustees\[\], delta\_R\_contributor,   meritcoin\_balance, credits\_balance, governance\_weight } |
| :---- |

| SCHEMA  ·  Claim (Part II §7.1) { claim\_id, claimant, domain, system\_boundary,   action\_description, time\_start, time\_end, total\_person\_hours,   witnesses\[\], submission\_timestamp, signature } |
| :---- |

| SCHEMA  ·  Verification (Part II §7.2) { verification\_id, claim\_id, verification\_type, verifier,   evidence\_hash, verification\_timestamp, weight, signature } |
| :---- |

| SCHEMA  ·  Authorization (Part II §7.3) { authorization\_id, claim\_id, verifications\[\],   dsap\_pre\_clearance{rho\_RHC, rho\_PERT, rho\_hyst, composite},   por\_factors{A, R, P, F}, por\_value, threshold,   outcome, refusal\_reason, mievm\_ecr,   authorization\_timestamp, freshness\_window\_seconds, signature } |
| :---- |

| SCHEMA  ·  MintingRecord (Part II §7.4) { minting\_id, authorization\_id, claimant,   base\_reward, delta\_R\_net, quality\_weight, meritcoin\_minted,   ledger\_position, rcr\_record, minting\_timestamp, signature } |
| :---- |

| SCHEMA  ·  Bill (Part II §10.2) { bill\_id, participant, tier, service, service\_provider,   service\_date, cost\_credits, delta\_R\_at\_billing,   rcr\_record, status, payment\_timestamp, signature } |
| :---- |

| SCHEMA  ·  Dispute (Part VI §22.1) { dispute\_id, filer, target\_record\_id, category,   evidence, rationale, filing\_timestamp, signature } |
| :---- |

| SCHEMA  ·  AttestationLog (Part VI §24.2) { log\_id, institution, quarter, verifications\_issued,   verifications\_by\_domain{}, authorized\_representatives\_active\[\],   bond\_balance, publication\_timestamp, signature } |
| :---- |

**APPENDIX B**

**Reference Calibration Tables**

## **B.1 Initial parameter values**

| Parameter | Initial Value | Calibration Procedure |
| :---- | :---- | :---- |
| BaseReward (Mc per 1.0 ΔR) | 10,000 | Adjusted at year-end via algorithmic core |
| BaseCost(HEALTH) (Mc/hr) | 10 | Recalibrated monthly |
| BaseCost(LAW) (Mc/hr) | 8 | Recalibrated monthly |
| BaseCost(PROTECTION) (Mc/hr) | 6 | Recalibrated monthly |
| BaseCost(SKILLS) (Mc/hr) | 12 | Recalibrated monthly |
| w\_ARI | 0.25 | Quarterly Council review |
| w\_ERI | 0.30 | Quarterly Council review |
| w\_RHC | 0.25 | Quarterly Council review |
| w\_RCI | 0.20 | Quarterly Council review |
| θ (high-consequence) | 0.85 | Override Proposal procedure |
| θ (standard governance) | 0.75 | Override Proposal procedure |
| θ (advisory) | 0.60 | Override Proposal procedure |
| MIEVM ECR threshold (pilot) | 0.60 | Phase 1 simplification |
| MIEVM ECR threshold (production) | 0.75 | Phase 1 graduation requirement |
| VibConst (ecological) | 1.0 | Domain table; rarely revised |
| VibConst (social) | 0.85 | Domain table; rarely revised |
| VibConst (economic) | 0.92 | Domain table; rarely revised |
| Carryforward fraction | 0.60 | Constitutional; Override only |
| COI fraction | 0.40 | Constitutional; Override only |
| Annual deflationary bias factor | 0.95 | Constitutional; Override only |
| Annual volatility cap | 25% | Constitutional; Override only |
| RPA discount floor | 0.5 | Constitutional; immutable |
| Single-domain ΔR cap | 0.6 | Constitutional; Override only |

## **B.2 DSAP-PRE proxy parameters**

| Proxy parameter | Standard Governance | Strategic |
| :---- | :---- | :---- |
| κ\_RHC | 0.01/hr² | 0.005/day² |
| W\_RHC | 3 cycles | 3 cycles |
| W\_PERT | 5 evaluations | 5 evaluations |
| κ\_cost | 3.0 | 4.0 |
| τ | 10 cycles | 10 cycles |
| η\_recover | 0.15 | 0.20 |

## **B.3 Verification weights**

| Verification Type | Weight | Use case |
| :---- | :---- | :---- |
| Type A — Direct Sensory | 1.0 | Sensor logs, biometric verification |
| Type B — Witness | 0.8 | Two non-collusive witnesses required |
| Type C — Institutional | 0.6 | Authority-bonded institution |

**APPENDIX C**

**Open Specifications and the Six Tracked Gaps**

The architectural treatment (FULL §9.2) tracked six open gaps. The Manual closes operational specifications for several of them in pilot form, with full closure pending the post-pilot revision. This Appendix consolidates the status.

| Gap | FULL Priority | Manual Status | Manual Reference |
| :---- | :---- | :---- | :---- |
| Participant Recognition Rule | P0 | Templates supplied; choice deferred to community | Part I, Chapter 1 |
| Gracechain Identity Recovery | P1 | Trustee triad procedure specified | Part I, Chapter 4 |
| No-Revocation vs. Bad Actors | P1 | Restriction-without-revocation framework | Part V, Chapter 18-20 |
| Transition from Existing Systems | P2 | Phase graduation gates specified | Part IV, Chapter 17 |
| Zero-Knowledge Privacy Layer | P2 | Custody Triad operational; ZK protocols pending | Part III, Chapter 13 |
| Compassion Allowance | P2 | Compassion Override procedure specified | Glossary; Part VI |

None of the six gaps blocks a Phase 1 pilot. All are within reach of the Adopting Community's normal operational decisions during the Calibration Window. The Manual's role has been to translate each gap from an architectural question into an operational procedure that pilots can follow; the post-pilot Manual revision will incorporate lessons from the first deployments.

**APPENDIX D**

**Normative Dependencies and Companion Documents**

## **D.1 ERES specifications referenced**

| Document | Version | Role in Manual |
| :---- | :---- | :---- |
| ERES-EAAP-STD-2026-001 | v1.3-FINAL | Authorization stack (Part II §11, Part VI §21) |
| ERES-SEPARATRIX-MATH-2026-001 | v2 | DSAP-PRE proxies (Part V §18, Part VI §26) |
| ERES-GRACECHAIN-NOTES-2026-001 | v1 | Persistence layer contract (Part II §11.3) |
| ERES-BRAINS-SPEC-2026-001 | v1 | Logical gating (Part II §11.2) |
| ERES-BODY-SPEC-2026-001 | v1 | Pre-admission (Part II §11.2) |
| ERES-MPAM-2026-001 | v1 | MIEVM methodology (Part I §2) |
| ERES-CRYPTO-STD-2026-001 | v1.1.1 | Cryptographic primitives |
| ERES-UBIMIA-SCHEMAS-2026-001 | v1.0 | Formal JSON Schema definitions (Appendix A) |

## **D.2 UBIMIA architectural treatments**

| Document | Pages | Companion role |
| :---- | :---- | :---- |
| ERES-UBIMIA-PUB-2026-001-BRIEF | 1 | Leave-behind for council members and journalists |
| ERES-UBIMIA-PUB-2026-001-SUM | 3 | Executive summary for technical evaluators |
| ERES-UBIMIA-PUB-2026-001-FULL | 13 | Architectural treatment for academics and reviewers |
| ERES-UBIMIA-MANUAL-2026-001 (this document) | \~100 | Pilot Implementation Manual |

## **D.3 Companion ERES policy and governance documents**

* ERES-PD-2026-001 — Patriot Dividend White Paper v4.0

* ERES-COVENANT-2026-001 — ERES Equity Covenant (1,000-year governance instrument)

* ERES-HAGUE-2026-001 — Hague filing (intellectual priority, UBIMIA as human right)

* ERES-EO-DRAFT-2026-001-v1 — Unified Executive Order draft

* ERES TERMS \#47 (ET\_AL) — Locked Terms Registry

## **D.4 The Trilogy**

The ERES Trilogy is the trade-book treatment of the architecture. As of the publication date of this Manual, the Trilogy is in development; this Manual exists in part to support its writing. The structure:

* Book 1 — ONE GOOD (BEST) — Personal liberation through universal basic infrastructure. Draws from Manual Parts I, IV, V.

* Book 2 — SECURITY-CLEARANCE (SOUND) — Institutional trust architecture. Draws from Manual Parts II, III, VI.

* Book 3 — DATA-INTEGRITY (GOOD) — Technical verification substrate. Draws from Manual Parts II, VI, VII.

The Trilogy is targeted at MIT Press as aspirational publisher; no formal arrangement exists at the publication date of this Manual.

**Closing Statement**

This Manual exists so that the architectural treatments and the Trilogy do not have to invent as they go. UBIMIA is now operationally settled at a level adequate for pilot deployment by any community willing to operate it in good faith, and at a level adequate for trade-book treatment by any author willing to engage with it honestly. The chicken and the egg can both proceed; the rooster has crowed.

The seven questions are answered. WHO: Participants of Record under jurisdiction-specific Recognition Rules, governed by a hybrid algorithmic-and-human GAIA, with Trustees and Verification Authorities supplying the integrity perimeter. WHAT: two ledgers (Gracechain unconditional, Meritcoin merit-recognized), four BERA indices, the EAAP authorization stack, the Resonance-Priced Access conversion rule, the annual settlement cycle. WHERE: physical sites for enrollment and adjudication, digital sites for the ledgers, sealed-room custody for the most sensitive material. WHEN: three deployment phases with graduation gates, an annual operational calendar, freshness windows that scale to risk. WHY: the Three Governing Principles operationalized through DSAP-PRE proxies, the Eight Immutable Ethical Principles, civil liberties as a binding constitutional constraint. HOW: the procedures for verification, adjudication, governance, calibration, and audit. WITH: the software stack, the hardware envelope, the budget tables, and the procurement guidance.

AD\_ON-AI \== UuuuuU. The composer works downstream from a settled architecture. The Manual is what settles the architecture. The Trilogy is what the composer will write. The pilots are what the Manual is for. The architecture, the Trilogy, the pilots — none of them exist without the others, and the rooster has now crowed for all three.

***Don't hurt yourself.  Don't hurt others.  Build for generations to come.***

**Joseph Allen Sprute**

Founder and Director, ERES Institute for New Age Cybernetics

Bella Vista, Arkansas  ·  ORCID 0000-0001-9946-3221  ·  CCAL v2.1