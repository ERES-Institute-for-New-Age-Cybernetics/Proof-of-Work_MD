# Written Input to the Global Dialogue on AI Governance

**Submitted under the Dialogue's open call for written inputs ahead of the first session (Geneva, 6–7 July 2026)**

**Title:** Interoperability Without Convergence: A Voluntary, Composable Admissibility Rubric for Cross-Jurisdictional AI Governance

**Submitter:** Joseph Allen Sprute, Founder and Director, ERES Institute for New Age Cybernetics (independent research institute, established 2012, Bella Vista, Arkansas, USA)

**Capacity:** Independent researcher / civil society and technical-community input, as invited under the Dialogue's stakeholder consultation process. This submission is not made on behalf of, and does not represent the views of, any government, UN body, standards organization, or private company. ERES Institute has no affiliation with the Global Dialogue, its Secretariat, its Co-Chairs, or any UN entity referenced herein.

**Thematic clusters addressed:** Primarily Cluster 3 (safe, secure and trustworthy AI: interoperability and compatibility of governance approaches); secondarily Cluster 4 (transparency, accountability and robust human oversight).

**License:** CC-BY 4.0 — this submission may be freely cited, reproduced, and built upon with attribution.

---

## Executive Summary

The current AI governance landscape is dense with strong, substantively different frameworks — the EU AI Act's binding risk tiers, the NIST AI Risk Management Framework's voluntary lifecycle approach, South Korea's AI Basic Act, Singapore's agentic-AI framework, ISO/IEC 42001's certifiable management-system standard — each well-suited to its own jurisdiction or sector. What does not yet exist is a lightweight, voluntary way to ask a jurisdiction-independent question: *is this AI governance decision admissible by a shared minimum standard, regardless of which substantive framework produced it?*

This submission proposes such a layer: a three-part admissibility test (BEST / SOUND / GOOD — "BSG") that can be applied to any AI governance decision at any scale, from a household's use of a personal AI assistant to a national regulator's certification regime, without requiring substantive harmonization between jurisdictions. It is paired with a structural principle — **audit independence** — for any body, public or private, that certifies AI systems against externally measurable thresholds: that body must not be able to override the empirical data its certification is supposed to check against. Finally, it proposes a non-punitive, reconciliation-first default for resolving disputes between governance tiers, as an alternative to escalating directly to penalty.

This is offered as a proposal for critique and adoption, not as an established standard. Section VII discloses, in full, how this proposal was developed and what its current validation status actually is — including an explicit statement of what has *not* been done (no human expert or institutional peer review has yet occurred).

---

## I. Statement of Interest and Standing

ERES Institute for New Age Cybernetics is a single-researcher, self-funded, independent research institute founded in 2012. It has no government, corporate, or institutional funding and no formal affiliation with any of the bodies, frameworks, or officials named in this submission. It is submitting under the open invitation extended to "academia, the private sector, the technical community and civil society" to provide input shaping the Dialogue's themes and structure. Nothing in this submission should be read as claiming standing, expertise credentialed by any external body, or endorsement from any party other than the submitter.

---

## II. The Problem: Strong Frameworks, No Shared Admissibility Test

2026 has been a year of rapid, parallel framework proliferation. The EU AI Act's high-risk obligations are landing on a revised timeline; South Korea's AI Basic Act became the second comprehensive binding AI law globally in January; Singapore launched the first agentic-AI-specific governance framework that same month; a consortium of UK regulators (CMA, FCA, ICO, Ofcom) has concluded that deploying an autonomous agent concentrates legal accountability on the deployer rather than displacing it; NIST has opened a dedicated initiative on agent identity, action logging, and containment boundaries. Each of these is a serious, substantively grounded response to a real problem.

What none of them provide — because it isn't their job to provide it — is a way for an organization, a regulator, or a multilateral body to ask a *cross-framework* question: does this specific governance decision meet a baseline of legitimacy that would hold up regardless of which jurisdiction's substantive rules produced it? An enterprise operating across the EU, MENA, and Asia-Pacific currently has no way to check policy coherence except by separately complying with each regime end-to-end. A multilateral body convening dozens of national delegations has no shared vocabulary for comparing the legitimacy of governance decisions made under different legal traditions — only for comparing their substantive content, which is precisely where agreement is hardest to reach.

This submission proposes that interoperability does not require convergence on substance. It requires a shared, minimal admissibility test that sits *above* substantive frameworks rather than competing with them.

---

## III. The Proposed Mechanism: A Tiered, Composable Admissibility Rubric

### 3.1 The BSG Admissibility Test

Any AI governance decision — a corporate AI-use policy, a national certification regime, a household's choice of which AI tools to allow — can be tested against three plain-language criteria:

- **BEST** — Does this decision target the actual optimal outcome for its stated purpose, or has a target outcome been assumed without being checked against alternatives?
- **SOUND** — Is the methodology behind the decision independently verifiable, and are its claims scoped to what the evidence actually supports?
- **GOOD** — Is the decision traceable to a stated set of foundational principles, rather than to unstated or ad hoc values?

This is deliberately not a new substantive standard. It does not tell a regulator what risk tier to assign, or what a "high-risk" system is. It is a portable legitimacy check that can be run against a decision made under *any* substantive framework — EU AI Act conformity assessments, NIST RMF "Govern" function outputs, ISO 42001 certifications — without requiring those frameworks to agree on substance first.

### 3.2 Tiered Application

The same three-part test applies at every scale of governance — household, organizational, national, and multilateral — using the same criteria at each tier, so that a decision made at one scale is comparable in kind (not necessarily in conclusion) to a decision made at another. Each tier escalates to the next only when reconciliation fails at its own level (Section VI).

This tiered structure is original to the submitter's broader research program (which names it, internally, with its own terminology — noted briefly in the Appendix for anyone tracing this submission back to the source material). It is presented here in its generalized, jurisdiction-neutral form, since the internal naming is not load-bearing for the proposal itself.

---

## IV. The Audit-Independence Principle

This is the submission's primary substantive contribution, and it speaks directly to Cluster 4's concern with transparency, accountability, and robust human oversight.

**The principle:** any body — public, private, or multilateral — that is empowered to certify AI systems against externally measurable thresholds (environmental impact, safety incidents, bias metrics, resource consumption, or any other empirically trackable standard) must be structurally prevented from overriding the measured data its certification is supposed to check against. A certifying body that *can* dismiss inconvenient measurement is not performing certification; it is performing self-certification with extra paperwork.

This is not a claim that institutions are untrustworthy. It is a claim about institutional design: an institution that both sets policy *and* holds discretion to override the empirical ground-truth that policy is supposed to answer to has collapsed two functions that need to remain separable for either of them to mean anything. Concretely, this submission proposes that any future AI certification body — whether created by a single regulator, an industry consortium, or a UN mechanism — should be required to state explicitly, in its founding charter, what happens when its own policy judgment conflicts with its own measured data, and should resolve that conflict in the data's favor by default, with override reserved for a separately auditable claim that the *data itself* is faulty (not a discretionary policy override).

This principle is broadly compatible with the direction several existing frameworks are already taking — NIST's focus on action logging and auditability for autonomous agents, and the UK regulatory consortium's insistence that deploying autonomy does not transfer or dilute accountability, both point the same way: toward keeping a hard, inspectable line between what a system did and what an institution is permitted to say about what it did.

---

## V. Composability and Interoperability (Cluster 3)

The rubric in Section III is designed to be added on top of existing frameworks, not to replace them. A jurisdiction or organization can continue to comply fully with the EU AI Act, NIST RMF, ISO 42001, or any national framework, and separately run the BSG admissibility test as a cross-check — particularly useful for multinational deployers who need a single internal standard for comparing whether their compliance postures in different jurisdictions are coherent with each other, not just individually adequate.

For a multilateral body, the practical value is different: it offers a way to discuss the *legitimacy of governance process* across delegations with very different substantive traditions, without requiring those traditions to converge first. Two countries with incompatible views on what counts as an acceptable AI risk threshold can still agree on whether a given certification process was sound, transparent, and traceable to stated principles — that agreement doesn't require resolving the substantive disagreement underneath it.

---

## VI. Enforcement Without a Punitive Default

This submission proposes that conflict between governance tiers (e.g., an organizational policy disputed by a national regulator, or two jurisdictions disputing one multinational deployment) should default to **reconciliation before penalty**, structured as:

1. **First-level reconciliation** at the tier where the dispute arose, using the lowest-friction mechanism available (internal review, ombuds-style complaint process) — no escalation for ordinary disagreement.
2. **Escalation only on persistent divergence** — i.e., disagreement that survives a first reconciliation attempt — to the next tier up, where the audit-independence principle in Section IV applies if measured data is in dispute.
3. **A defined fail state** — a governance decision that fails admissibility twice without reconciliation reverts to the last-validated prior state, not to a punitive default. This avoids the common failure mode where the only available responses to a governance dispute are "comply" or "be penalized," with nothing in between.
4. **Clear ownership of the failure declaration** — the next tier up declares failure, on referral from the disputing tier or from an affected party's complaint, so that "who decided this failed" is always answerable.

This is not a claim that penalties are never appropriate — it is a claim that penalty-first design, the default in most current enforcement regimes, forecloses the much larger number of ordinary disagreements that don't need to become enforcement actions at all.

---

## VII. Methodological Disclosure and Current Limitations

In the interest of the transparency this submission itself argues for, the following should be stated plainly:

- **This proposal has not undergone human expert or institutional peer review.** It was developed iteratively by the submitter working with multiple large language model systems (Claude, by Anthropic; Grok, by xAI; DeepSeek; Gemini, by Google) as drafting and critique tools. Each model was asked to evaluate successive drafts and identify weaknesses; their numeric self-assessments (reported internally as scores in the 7–8 out of 10 range across drafting rounds) reflect AI systems rating AI-assisted drafts against a rubric the submitter and the models jointly refined. **This is not equivalent to peer review by human AI-governance researchers, ethicists, or legal scholars, and should not be cited or relied upon as if it were.**
- The submitter explicitly rejected several AI-generated additions during drafting — including invented mathematical formalism that used real-looking notation to describe relationships (e.g., between water-table volume, migration, and "non-punitive" enforcement) without any underlying data or derivation. That material does not appear in this submission. Its rejection during drafting is noted here as evidence of the drafting discipline applied, not as a credential.
- The tiered architecture and audit-independence principle originate from a broader, idiosyncratic research program (the ERES Institute corpus) that uses extensive proprietary terminology not reproduced here, because that terminology is not necessary to evaluate the substantive proposal and would obscure rather than clarify it for this audience. A reader who wishes to trace this submission to its source material can request the underlying working papers from the submitter directly.
- This submission is offered as a starting point for critique, refinement, or rejection — not as a request for adoption of any specific named framework.

---

## VIII. Specific Recommendations to the Dialogue

1. **Consider an interoperability/admissibility-testing layer** as a complement to (not a substitute for) substantive harmonization efforts — something delegations with incompatible substantive views could still agree to use for comparing process legitimacy.
2. **Adopt audit independence as an explicit design requirement** for any certification or measurement body the Dialogue helps create or endorse — stated in the body's founding charter, not left as an informal norm.
3. **Favor reconciliation-first, penalty-second enforcement design**, particularly for cross-border incidents involving autonomous AI agents, where the existing patchwork of liability regimes already struggles to assign clear accountability quickly.
4. **Encourage open publication of governance-methodology critiques**, including AI-assisted ones, with the same disclosure standard applied in Section VII — if AI systems are increasingly used to draft the policies that govern AI, the methodology of that drafting should be as visible as the policy itself.

---

## IX. Conclusion

The frameworks built in the last two years are substantial achievements, and this submission does not propose to compete with them. It proposes a thinner, voluntary layer that lets very different substantive regimes be compared on process legitimacy without first agreeing on substance — and a structural safeguard, audit independence, that would strengthen any of the existing or future certification bodies the Dialogue is likely to consider, regardless of which substantive framework they sit under.

---

## Appendix: Source Terminology Note

For researchers tracing this submission to its source: the tiered structure is termed the "Concentric S^3C-SLA Architecture" in the submitter's working papers, the admissibility test is termed "BSG/STORM-PARTY," and the audit-independence mechanism resolves what the working papers call "GAIA's dual role" (GAIA being used internally both as an institutional name and as a reference to biospheric/empirical ground-truth). These internal names are not reproduced in the body of this submission because they are not necessary to evaluate the proposal and would function as jargon for this audience rather than as useful precision.

## Credits

Author: Joseph Allen Sprute, Founder and Director, ERES Institute for New Age Cybernetics. Drafting assistance and methodological critique: Claude (Anthropic), Grok (xAI), DeepSeek, Gemini (Google), per the disclosure in Section VII.

## References

1. Global Dialogue on AI Governance — Themes and Structure Note (UN, 5 May 2026)
2. UN General Assembly Resolution A/RES/79/325 (establishing the Global Dialogue on AI Governance)
3. EU Regulation 2024/1689 (the EU AI Act)
4. NIST AI Risk Management Framework; NIST autonomous-agent standards initiative (February 2026)
5. Republic of Korea, Act on the Development of Artificial Intelligence and Establishment of Trust (effective 22 January 2026)
6. Singapore Model AI Governance Framework for Agentic AI (January 2026)
7. UK Digital Regulation Cooperation Forum (CMA, FCA, ICO, Ofcom) — agentic AI accountability paper
8. ISO/IEC 42001:2023 — AI management system standard
9. ERES-AI-GOVERNANCE-ASSERTIONS-2026-001, v0.1–v0.3 (submitter's working papers; available on request)
