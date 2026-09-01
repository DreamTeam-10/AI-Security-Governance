# Core Framework Matrix — Cybersecurity & AI Governance Reference

A working reference mapping the primary cybersecurity and AI governance frameworks: what each one is, why it exists, and where it applies across industries. Built for practitioners doing security architecture, risk assessment, or AI governance work in any regulated or enterprise environment.

**A note on sourcing:** every category/tactic name below was verified against current framework documentation, not recalled from memory. Where a framework has too many subcategories to list exhaustively, the full category/tactic layer is listed with a pointer to the canonical source for anything below that level.

**Version discrepancies worth flagging:** MITRE ATT&CK Enterprise is currently **14 tactics** (a commonly cited "15" is outdated — Reconnaissance and Resource Development were folded in from PRE-ATT&CK as of v8, landing at 14). MITRE F3 launched with **7 tactics**; check ctid.mitre.org/fraud for the current count before citing a higher number.

## 1. MITRE ATT&CK (Enterprise) — v19.1 — 14 tactics

**What it is and why it matters across sectors:** ATT&CK is the industry-standard knowledge base of *how attackers actually behave* once inside traditional IT infrastructure — servers, networks, identities, endpoints. It's sector-agnostic by design: a hospital, a bank, a manufacturer, and a government agency all face the same underlying tactics, even though the assets being defended differ. It's the shared vocabulary security teams, auditors, and threat intel analysts across every industry already speak, and the default reference for coverage heatmaps ("what are we actually defending against").

| **Tactic** | **ID** | **What it covers** | **Cross-sector example** |
| --- | --- | --- | --- |
| Reconnaissance | TA0043 | Gathering info to plan an attack | Attacker scrapes a company's public API docs and LinkedIn to map its tech stack before an attack |
| Resource Development | TA0042 | Building attack infrastructure | Registering a lookalike domain ahead of a phishing campaign against employees |
| Initial Access | TA0001 | Gaining a foothold | Phishing an employee for credentials into a cloud development environment |
| Execution | TA0002 | Running malicious code | Malicious code embedded in a compromised third-party software dependency |
| Persistence | TA0003 | Maintaining access | A backdoored service account left active inside a SaaS integration |
| Privilege Escalation | TA0004 | Gaining higher-level permissions | Exploiting an over-permissioned service identity to reach sensitive systems |
| Defense Evasion | TA0005 | Avoiding detection | Disabling logging to hide unauthorized access to a system |
| Credential Access | TA0006 | Stealing credentials | Harvesting API keys used by an automated workflow |
| Discovery | TA0007 | Mapping the environment | Enumerating which systems and data stores are reachable from a compromised host |
| Lateral Movement | TA0008 | Moving through the network | Pivoting from a compromised customer portal into adjacent internal systems |
| Collection | TA0009 | Gathering target data | Scraping customer records staged for exfiltration |
| Command and Control | TA0011 | Communicating with compromised systems | A compromised host beaconing to an external server disguised as legitimate traffic |
| Exfiltration | TA0010 | Stealing data out | Data exfiltrated through a poorly-monitored cloud storage bucket |
| Impact | TA0040 | Disrupting operations/data | Ransomware disrupting a manufacturer's production line or a hospital's patient records system |

## 2. MITRE ATLAS — v5.4 — 16 tactics (AI/ML-specific)

**What it is and why it matters across sectors:** ATLAS is ATT&CK's sibling framework, purpose-built for attacks that specifically target AI/ML systems — prompt injection, model theft, data poisoning — rather than traditional IT. As every industry from healthcare to retail to finance races to deploy AI into decision-making, ATLAS is becoming the equivalent reference point ATT&CK already is for traditional infrastructure.

| **Stage** | **Tactics** | **Cross-sector example** |
| --- | --- | --- |
| **Preparation** | Reconnaissance, Resource Development, Initial Access, AI Model Access | Adversary repeatedly queries a public-facing AI chatbot to map its guardrails before attacking it |
| **Exploitation** | Execution, Persistence, Defense Evasion, Credential Access, Discovery, Lateral Movement, Collection | Prompt injection embedded in a document that an internal AI agent later ingests and acts on |
| **Objectives** | AI Attack Staging, Command and Control, Exfiltration, Impact | Crafted queries extract a system prompt or leak sensitive data through an AI assistant's responses |

## 3. NIST CSF 2.0 — 6 functions, 22 categories, 106 subcategories

**What it is and why it matters across sectors:** NIST CSF is the most widely adopted cybersecurity governance framework in the U.S. across every industry — voluntary, but functioning as a de facto baseline that regulators, examiners, boards, and cyber-insurance underwriters all reference. Sector-specific overlays exist on top of it (the Cyber Risk Institute Profile for banking, HITRUST for healthcare), but CSF itself is the common root.

| **Function** | **Category** | **ID** | **Cross-sector example** |
| --- | --- | --- | --- |
| **Govern** | Organizational Context | GV.OC | Defining how AI risk tolerance ties to the organization's broader enterprise risk appetite |
|  | Risk Management Strategy | GV.RM | Setting risk-tiering thresholds that route AI initiatives into delivery lanes |
|  | Roles, Responsibilities, and Authorities | GV.RR | Clarifying who signs off when an initiative is flagged Elevated Risk |
|  | Policy | GV.PO | Writing a guardrail policy for data exposure thresholds |
|  | Oversight | GV.OV | Reporting risk posture to executive/board audiences |
|  | Cybersecurity Supply Chain Risk Management | GV.SC | Vetting a third-party AI observability vendor before procurement |
| **Identify** | Asset Management | ID.AM | Maintaining an inventory of AI/agentic systems in production |
|  | Risk Assessment | ID.RA | Running a risk assessment before a new AI workflow ships |
|  | Improvement | ID.IM | Updating the risk model based on a near-miss incident |
| **Protect** | Identity Management, Authentication, and Access Control | PR.AA | Enforcing least-privilege access design for service accounts |
|  | Awareness and Training | PR.AT | Training engineering teams on secure integration patterns |
|  | Data Security | PR.DS | Defining data-access policy thresholds for what a system can read |
|  | Platform Security | PR.PS | Hardening an API gateway layer |
|  | Technology Infrastructure Resilience | PR.IR | Ensuring protective tooling doesn't create a single point of failure |
| **Detect** | Continuous Monitoring | DE.CM | Observability tooling flagging drift or anomalous behavior |
|  | Adverse Event Analysis | DE.AE | Investigating a flagged intrusion attempt |
| **Respond** | Incident Management | RS.MA | Executing the incident response plan |
|  | Incident Analysis | RS.AN | Root-causing how an access boundary was exceeded |
|  | Incident Response Reporting and Communication | RS.CO | Briefing auditors/regulators after an incident |
|  | Incident Mitigation | RS.MI | Rolling back a compromised system version |
| **Recover** | Incident Recovery Plan Execution | RC.RP | Restoring a service to a known-good configuration post-incident |
|  | Incident Recovery Communication | RC.CO | Communicating remediation status to stakeholders |

## 4. MITRE D3FEND — v1.3 — 7 categories, 267 techniques

**What it is and why it matters across sectors:** D3FEND is the defensive counterpart to ATT&CK — where ATT&CK catalogs attacker behavior, D3FEND catalogs actual countermeasures, with official mappings to NIST 800-53, a control catalog referenced across federal, healthcare, and financial regulatory regimes. It's the tool for turning a threat finding directly into an auditable control.

| **Category** | **Technique count** | **What it covers** | **Cross-sector example** |
| --- | --- | --- | --- |
| Model | 27 | Understanding/baselining your own environment | Mapping which systems and data flows exist before setting controls |
| Harden | 51 | Reducing attack surface proactively | Hardening application and platform configurations |
| Detect | 90 | Identifying malicious activity | Detecting anomalous access patterns |
| Isolate | 57 | Containing a threat | Network-isolating a compromised system from production |
| Deceive | 11 | Misleading attackers | Deploying honeytoken data to catch unauthorized scraping |
| Evict | 19 | Removing the adversary | Revoking compromised credentials and tokens |
| Restore | 12 | Returning to known-good state | Rolling back a system to its last verified checkpoint |

## 5. NIST AI RMF — 1.0 — 4 functions, 19 categories (Govern: 6, Map: 5, Measure: 4, Manage: 4)

**What it is and why it matters across sectors:** NIST AI RMF is the U.S. government's voluntary, cross-industry framework for managing AI-specific risk — bias, transparency, safety — separate from traditional cybersecurity risk. Regulators across sectors increasingly cite it as an expected baseline even without a formal mandate, and it's designed to plug into an organization's existing enterprise risk management structure rather than requiring a parallel process.

| **Function** | **Categories (confirmed)** | **Cross-sector example** |
| --- | --- | --- |
| **Govern** (cross-cutting, org-wide) | 6 categories, 19 subcategories — policies, accountability, roles, culture | Establishing an AI governance team's charter and decision rights |
| **Map** (system-layer context) | Context establishment; AI system categorization; capability/limitations characterization; risk & benefit criteria; stakeholder identification | Scoping a new AI system: what it does, who's affected, what could go wrong |
| **Measure** (system-layer assessment) | 4 categories — testing/benchmarking against trustworthiness characteristics | Running red-team evaluations against a model before release |
| **Manage** (system-layer response) | 4 categories — prioritization, risk treatment, incident response | Deciding whether a flagged AI risk gets remediated, accepted, or blocks deployment |

*Note: Measure and Manage category names weren't independently confirmed at the subcategory level — pull exact wording from nist.gov/ai-rmf if quoting a specific subcategory.*

## 6. MITRE F3 (Fight Fraud Framework) — v1.1 — 7 tactics confirmed (verify current count)

**What it is and why it matters across sectors:** F3 is the newest framework here (launched April 2026), purpose-built for financial fraud — founding contributors include JPMorganChase, FS-ISAC, and Lloyds Banking Group. Its relevance narrows mostly to financial services, payments, and e-commerce, anywhere access converts directly into stolen money, but the underlying "positioning vs. monetization" behavioral split is a useful mental model even outside finance (e.g., healthcare billing fraud, insurance fraud).

| **Tactic** | **Note** | **Cross-sector example** |
| --- | --- | --- |
| Reconnaissance | Shared with ATT&CK | Fraudster researches a target's account recovery process |
| Resource Development | Shared with ATT&CK | Setting up mule accounts ahead of a fraud campaign |
| Initial Access | Shared with ATT&CK | Compromising a customer's login credentials |
| Defense Evasion | Shared with ATT&CK | Using synthetic identities to bypass identity verification |
| **Positioning** | F3-specific, not in ATT&CK | Manipulating account data post-compromise to prepare for a fraudulent payout |
| Execution | Shared with ATT&CK | Initiating an unauthorized transfer or claim |
| **Monetization** | F3-specific, not in ATT&CK | Converting stolen access into crypto, fake invoices, or resold credentials |

## 7. OWASP Top 10 for Agentic Applications — 2026 release (Dec 2025) — 10 categories

**What it is and why it matters across sectors:** The newest AI-native risk taxonomy, purpose-built for AI *agents* that take autonomous action rather than chatbots that just generate text. Relevant anywhere an organization is giving an AI system tool access, API calls, database queries, transaction authorization, regardless of industry, since the risk profile changes fundamentally once an AI system can *act* rather than just respond.

| **ID** | **Category** | **Cross-sector example** |
| --- | --- | --- |
| ASI01 | Agent Goal Hijack | Indirect prompt injection causes an agent to pursue an attacker-defined objective |
| ASI02 | Tool Misuse and Exploitation | An agent with system access is manipulated into an unauthorized action |
| ASI03 | Identity and Privilege Abuse | An over-permissioned agent accesses data beyond its intended scope |
| ASI04 | Agentic Supply Chain Vulnerabilities | A compromised third-party plugin or MCP server used in an agent workflow |
| ASI05 | Unexpected Code Execution | An agent executes attacker-embedded code hidden in a submitted document |
| ASI06 | Memory & Context Poisoning | Poisoned data persists in an agent's memory, corrupting future decisions |
| ASI07 | Insecure Inter-Agent Communication | Spoofed messages between two AI agents coordinating a workflow |
| ASI08 | Cascading Failures | One compromised agent's bad output propagates through a multi-agent pipeline |
| ASI09 | Human-Agent Trust Exploitation | An employee approves a harmful action because the agent's output sounded convincing |
| ASI10 | Rogue Agents | An agent exhibits goal drift or misaligned behavior outside its intended function |

## 8. ISO/IEC 42001 — AI Management System standard

**What it is and why it matters across sectors:** ISO 42001 is the world's first *certifiable* AI management system standard, the AI-specific equivalent of ISO 27001. Where NIST AI RMF is voluntary self-attestation, ISO 42001 is something any organization, in any industry, can get independently audited and certified against, useful for demonstrating third-party AI governance assurance to customers, partners, or regulators.

Follows the same Annex SL structure shared across ISO management standards (27001, 9001):

| **Clause** | **Focus** | **Cross-sector example** |
| --- | --- | --- |
| 4 — Context of the Organization | Understanding internal/external AI risk context | Assessing how the EU AI Act affects international AI deployments |
| 5 — Leadership | Top management commitment, AI policy | Executive sign-off on an AI risk-tiering framework |
| 6 — Planning | Risk/opportunity assessment, objectives | Setting measurable AI governance objectives for the year |
| 7 — Support | Resources, competence, awareness, documentation | Ensuring teams share a common AI risk vocabulary |
| 8 — Operation | Operational planning and control | Day-to-day enforcement of guardrail thresholds in production |
| 9 — Performance Evaluation | Monitoring, internal audit, management review | Auditing whether risk-tiering decisions are applied consistently |
| 10 — Improvement | Nonconformity, corrective action, continual improvement | Updating the risk model after an incident review |

*Confidence note: this clause structure is well-established ISO convention; exact ISO 42001 clause wording wasn't independently re-verified — check iso.org if quoting clause language directly.*

## 9. MAESTRO — 7-layer agentic AI threat modeling framework

**What it is and why it matters across sectors:** MAESTRO (Multi-Agent Environment, Security, Threat, Risk, and Outcome) is purpose-built for multi-agent AI systems, relevant anywhere an organization is moving from single-model chatbots to coordinated multi-agent workflows, a shift happening across tech, finance, healthcare, and government simultaneously.

| **Layer** | **Focus** | **Cross-sector example** |
| --- | --- | --- |
| L1 — Foundation Models | The base LLM itself | Assessing whether a foundation model has known adversarial weaknesses |
| L2 — Data Operations | Data pipelines, storage, RAG | Poisoned data injected into a retrieval-augmented generation pipeline |
| L3 — Agent Frameworks | Orchestration/decision logic | A LangGraph or CrewAI-based agent's reasoning loop being manipulated |
| L4 — Deployment and Infrastructure | Hosting, containers, cloud | Misconfigured cloud infrastructure hosting an agent's runtime |
| L5 — Evaluation and Observability | Monitoring, logging, drift detection | Log injection hiding malicious agent activity from dashboards |
| L6 — Security and Compliance (cross-cutting) | Auth, guardrails, auditability | The vertical layer an AI governance role typically owns |
| L7 — Agent Ecosystem | Multi-agent/external interactions | Agent impersonation in a multi-agent workflow involving external servers |

## 10. GDPR (General Data Protection Regulation) — 99 articles, 11 chapters, 173 recitals

**What it is and why it matters across sectors:** GDPR is the EU's foundational data privacy law and, because of its extraterritorial reach, applies to any organization processing EU residents' personal data, regardless of headquarters location or industry. For AI specifically, GDPR governs whether a system can even use certain data in the first place, before you get to securing it.

| **Chapter** | **Focus** | **Cross-sector example** |
| --- | --- | --- |
| I — General Provisions | Scope, definitions | Determining whether a feature processing EU customer data falls under GDPR |
| II — Principles | Lawfulness, purpose limitation, data minimization, accountability | Ensuring an AI model only uses data it has a lawful basis to process |
| III — Rights of the Data Subject | Access, erasure, portability, objection to automated decisions | Handling a request to explain why an AI system made an automated decision (Art. 22) |
| IV — Controller and Processor | Obligations, security of processing, DPIAs | Requiring a Data Protection Impact Assessment before a new high-risk AI feature |
| V — International Transfers | Rules for moving data outside the EU | Governing whether EU data can be processed by a non-EU-hosted AI model |
| VI — Supervisory Authorities | Regulator structure and powers | Understanding which EU authority would investigate a complaint |
| VII — Cooperation and Consistency | Cross-border regulator coordination | Relevant to incident escalation planning across EU member states |
| VIII — Remedies, Liability, and Penalties | Fines, right to compensation | Framing the business case for guardrails in terms of fine exposure |
| IX — Specific Processing Situations | Sector-specific carve-outs | Employment data, journalism, research exemptions, varies by sector |
| X — Delegated/Implementing Acts | EU Commission rulemaking authority | Generally not relevant for day-to-day architecture work |
| XI — Final Provisions | Repeal of prior directive, entry into force | Generally not relevant for day-to-day architecture work |

**Cross-sector tie-in:** any AI guardrail (PII exposure thresholds, data-access policy) is, at its core, a technical control implementing GDPR's Article 5 principles and Article 25 "data protection by design."

## 11. EU AI Act (Regulation (EU) 2024/1689) — 4 risk tiers

**What it is and why it matters across sectors:** The world's first comprehensive, binding AI law, taking a risk-tiered approach where the stricter the potential harm, the heavier the compliance burden. Applies extraterritorially to any organization whose AI systems affect people in the EU, regardless of industry, though the specific high-risk categories (Annex III) are weighted toward employment, credit, law enforcement, healthcare, and critical infrastructure.

**Important, current status as of this writing:** under the July 2026 "Digital Omnibus on AI" reform (Regulation (EU) 2026/1744), high-risk obligation deadlines were pushed back — Annex III high-risk systems now must comply by **2 December 2027** (previously 2 August 2026), Annex I high-risk systems by **2 August 2028**. The ban on unacceptable-risk practices (Feb 2025) and GPAI model obligations (Aug 2025) are already in force and unaffected. Worth knowing cold — this is a very recent, actively-moving timeline.

| **Tier** | **Status** | **What it covers** | **Cross-sector example** |
| --- | --- | --- | --- |
| Unacceptable Risk | Banned outright (Art. 5), in force since Feb 2025 | Social scoring, subliminal manipulation, workplace emotion recognition | Prohibits any AI feature manipulating behavior without awareness |
| High Risk | Full conformity assessment, human oversight, registration (Annex III deadline now Dec 2027) | Credit scoring, employment, critical infrastructure, biometric ID, healthcare diagnostics | An AI-driven hiring screen, credit decision, or diagnostic tool |
| Limited Risk | Transparency disclosure only (Art. 50), in force Aug 2026 | Chatbots, AI-generated content | A customer service AI chatbot must disclose it's AI |
| Minimal Risk | No mandatory obligations | Most internal tooling, recommendation systems | An internal AI coding assistant used by engineers |

**Cross-sector tie-in:** any customer-facing AI feature touching EU users needs classification against these four tiers before deployment, this applies equally to a bank's fraud model, a hospital's triage tool, or a retailer's recommendation engine.

## 12. OWASP Top 10 for LLM Applications — 2026 edition (Aug 4, 2026) — 10 categories

**What it is and why it matters across sectors:** The original OWASP AI-native risk taxonomy, purpose-built for LLMs functioning as a *component inside an application* (a chatbot, copilot, or RAG system) rather than an autonomous agent. Relevant anywhere an organization embeds a language model into a product, regardless of industry, since prompt injection and output-handling risks exist the moment untrusted text reaches a model — well before that model is ever given tool access. Complements the OWASP Agentic Top 10 above: this list governs the model as a component, and the moment it gains tools, memory, or autonomous consequences, risk shifts to the Agentic list.

**Currency note:** the 2026 edition (released Aug 4, 2026 at Black Hat USA) reordered eight of ten entries and renamed one from the 2025 list, and for the first time weighted rankings 75% on practitioner consensus / 25% on 6,639 real-world incidents rather than consensus alone. If citing rank order, confirm it's still current — this list moves fast.

| **ID** | **Category** | **Cross-sector example** |
| --- | --- | --- |
| LLM01:2026 | Prompt Injection | A crafted support ticket contains hidden text that redirects the assistant to disclose internal notes |
| LLM02:2026 | Sensitive Information Disclosure | An AI assistant summarizing internal documents inadvertently surfaces a customer's PII embedded in a linked record |
| LLM03:2026 | Excessive Agency | A support chatbot with refund-processing permissions is manipulated into issuing an unauthorized payout |
| LLM04:2026 | Supply Chain | A pretrained model fine-tuned on a compromised third-party dataset carries the vulnerability into every deployment |
| LLM05:2026 | Data and Model Poisoning | Manipulated fine-tuning data causes a model to systematically favor a competitor's product in recommendations |
| LLM06:2026 | Unbounded Consumption | An attacker floods an AI chatbot with expensive queries to exhaust an org's inference budget (a "Denial of Wallet" attack) |
| LLM07:2026 | Misinformation | A confidently-worded but factually wrong AI-generated answer triggers an automated downstream action based on bad data |
| LLM08:2026 | Hidden Context Exposure | A user extracts the system prompt and internal tool schema through careful questioning, revealing business logic |
| LLM09:2026 | Vector and Embedding Weaknesses | An attacker poisons a RAG knowledge base so retrieval returns manipulated content for specific queries |
| LLM10:2026 | Improper Output Handling | Unvalidated model output is passed directly into a database query or shell command, functioning like stored XSS |

## Quick-reference: which framework to reach for, by scenario type

| **Scenario** | **Framework to cite first** |
| --- | --- |
| Designing reference architectures / secure defaults for AI and agentic workloads | MAESTRO, OWASP Agentic Top 10 |
| Building a multi-factor risk-tiering model | NIST CSF (Govern/Identify), NIST AI RMF (Map/Measure), EU AI Act's 4-tier model as real-world precedent |
| Setting guardrail thresholds (hallucination, PII/PHI, prompt injection, toxicity) | OWASP LLM Top 10, OWASP Agentic Top 10, MITRE ATLAS, GDPR Article 25 |
| Threat modeling a new AI system pattern | STRIDE (traditional), MAESTRO, MITRE ATLAS |
| Financial services / regulated industry AI governance | ISO/IEC 42001, NIST AI RMF, SR 11-7 (model risk, banking-specific) |
| Evaluating emerging agentic AI frameworks | OWASP Agentic Top 10, MAESTRO L3 |
| Building or securing a standard LLM-powered app (chatbot, copilot, RAG — not autonomous) | OWASP LLM Top 10 |
| Questions involving EU customer data or international AI deployment | GDPR, EU AI Act |
| Financial fraud / payments-specific risk | MITRE F3 |
| Turning a threat finding into a documented, auditable control | MITRE D3FEND (mapped to NIST 800-53) |

---
*Source: consolidated from framework-reference working doc, comprehensive 12-framework edition.*
