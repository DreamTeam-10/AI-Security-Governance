---
name: governance-skill
description: Maps a cybersecurity/AI-security finding, control, or governance gap to NIST CSF 2.0, MITRE ATT&CK, MITRE ATLAS, NIST AI RMF 1.0, AWS Well-Architected Framework (especially the Security pillar), OWASP Top 10 for Agentic Applications, and MITRE F3 (Fight Fraud Framework), with correct current version numbers and function/tactic/technique/pillar/category IDs. Use this skill whenever building AI security case studies, GitHub repo skill files, RACI/governance docs, cloud architecture reviews, compliance mappings, security-posture reporting, ATT&CK/ATLAS coverage heatmaps, or LinkedIn/report content about organizational risk management, AI risk governance, agentic application risk, or cloud workload architecture — even if the user describes the issue in plain language without naming a framework. Always use this skill instead of recalling category IDs from memory, since these frameworks revise on independent cycles.
---

# AI Governance Framework Mapper

Maps organizational risk, security posture, AI governance gaps, agentic-application risk, cloud architecture posture, and (where relevant) fraud/monetization behavior to seven frameworks. **MITRE ATT&CK, MITRE ATLAS, and NIST CSF 2.0 are the three primary, industry-standard anchors** — organizations actively use ATT&CK/ATLAS coverage mapping (heatmaps, gap analysis) as a governance and security-posture tool, not just an incident-response one, so this skill maps to them directly rather than deferring elsewhere. NIST AI RMF, AWS Well-Architected, and OWASP Agentic Top 10 are strong secondary frameworks, each authoritative within its specific lane. MITRE F3 is included for fraud/monetization findings but flagged as an immature, not-yet-widely-adopted framework — see priority section below.

This skill is the companion to `offense-defense-skill`, which covers the same ATT&CK/ATLAS technique-level detail plus D3FEND countermeasures for incident-level, kill-chain mapping. Use `offense-defense-skill` when the deliverable is a technical attack-chain breakdown; use this skill when the deliverable is posture/governance/reporting-level, even though both draw on ATT&CK and ATLAS.

## Before mapping anything: verify current versions

These frameworks are newer and revise faster than legacy MITRE ATT&CK. **Spot-check the version before citing it in any formal deliverable** — F3 in particular is brand-new (first released April 2026) and likely to see faster revision cycles than the others.

- Web search for the current version if it's been more than ~4-6 weeks since last checked, or the output is being published/shipped.

**Baseline versions (last verified 2026-08-05 — re-check before formal use):**

| Framework | Version | Scope | Canonical source |
|---|---|---|---|
| MITRE ATT&CK | v19.1 | 15 Enterprise tactics · 286 techniques — used here for posture/coverage mapping (e.g. "which tactics do our current detections cover") rather than incident-level technique breakdown | attack.mitre.org |
| MITRE ATLAS | v5.4 | 16 tactics · 84 techniques — AI/ML-specific adversarial coverage mapping | atlas.mitre.org |
| NIST CSF | 2.0 | 6 functions · 22 categories (org security posture) | nist.gov/cyberframework |
| NIST AI RMF | 1.0 | 4 functions (Govern, Map, Measure, Manage) · 72 subcategories | nist.gov/ai-rmf |
| AWS Well-Architected Framework | Current (6 pillars) | Operational Excellence, Security, Reliability, Performance Efficiency, Cost Optimization, Sustainability — plus domain-specific Lenses (ML, serverless, financial services, etc.) | docs.aws.amazon.com/wellarchitected |
| OWASP Top 10 for Agentic Applications | 2025 | Top 10 risk categories specific to agentic AI app design/deployment | owasp.org/Top10/2025 |
| MITRE F3 (Fight Fraud Framework) | v1.1 (released 2026-04-09) | 8 tactics · 123 techniques — Positioning (FA0001) and Monetization (FA0002) | ctid.mitre.org/fraud |

AWS Well-Architected doesn't publish a single version number the way NIST/MITRE do — it revises pillar guidance continuously. When mapping to it, cite the **pillar** (usually Security, sometimes Operational Excellence for monitoring/detection controls) rather than a version number, and check whether a domain-specific **Lens** (e.g. the Machine Learning Lens) applies for AI-specific workloads.

Also worth flagging when relevant: **ISO/IEC 42001** (AI management systems) is the standard most people mean when they say "ISO AI governance standard" — confirm this is what's intended if a user references an ISO number that doesn't check out (e.g. "ISO 12007" is not a published standard).

## Framework priority and industry adoption

Not all seven frameworks carry equal weight — be explicit about that rather than presenting them as peers:

- **MITRE ATT&CK, MITRE ATLAS, and NIST CSF are the three primary, industry-standard anchors.** Cite these with high default confidence. When a governance deliverable calls for a coverage view ("what tactics are we defending against," "where are our detection gaps"), build it directly from ATT&CK/ATLAS tactics here — don't route the user to `offense-defense-skill` for this; that skill is for incident-level technique breakdowns, this one is for posture-level coverage and reporting. The two skills legitimately overlap on ATT&CK/ATLAS by design.
- **NIST AI RMF, AWS Well-Architected, and OWASP Agentic Top 10** are industry-standard within their specific lanes (AI risk management; cloud architecture; agentic app security) but narrower in scope than the big three above — cite them confidently within that lane.
- **MITRE F3 is legitimate but immature** — first released April 2026, not yet a widely-adopted industry standard the way ATT&CK/CSF are. Still map fraud/monetization findings to it, but say so plainly (e.g. "per MITRE F3 — a new, not-yet-widely-adopted framework as of 2026") rather than presenting it with the same institutional weight as ATT&CK or CSF.

## Mapping logic

1. **Identify what kind of gap or finding this is** before picking a framework:
   - Security-posture coverage question — "what are we defending against," "where's our detection gap," heatmap-style reporting → **MITRE ATT&CK** (enterprise) tactics, cross-referenced with **NIST CSF** functions (Detect/Protect)
   - AI/ML-adversarial posture coverage — same coverage-mapping exercise but for AI-specific threats → **MITRE ATLAS** tactics
   - Broad organizational security posture / risk prioritization → **NIST CSF** (map to one of the 6 functions: Govern, Identify, Protect, Detect, Respond, Recover)
   - AI-specific risk management / trustworthiness practice → **NIST AI RMF** (map to Govern, Map, Measure, or Manage)
   - Risk specific to how an agentic application is designed or deployed (excessive agency, tool misuse, memory poisoning, cascading agent trust) → **OWASP Agentic Top 10**
   - Cloud workload architecture decision (access design, network segmentation, monitoring/observability setup, credential/secrets architecture, blast-radius containment) → **AWS Well-Architected**, almost always the **Security pillar**; note the Operational Excellence pillar if the finding is about monitoring/detection process rather than the control itself
   - Post-compromise fraud/monetization behavior (account takeover leading to financial theft, synthetic identity, money-mule activity) → **MITRE F3** (Positioning FA0001 vs. Monetization FA0002)
2. **A single finding often maps to more than one framework at different altitudes** — e.g. an agent with over-broad IAM roles is simultaneously an OWASP "Excessive Agency" risk AND a NIST CSF "Protect" function gap AND (if it enabled fraud) a MITRE F3 Positioning technique. Map at each altitude that applies; don't force a single-framework answer if the finding is genuinely cross-cutting.
3. **Do not force a mapping.** If nothing fits cleanly, say so rather than inventing a category ID.
4. **Cite the rationale** in one sentence, referencing the specific mechanic.
5. **Never fabricate a category/subcategory ID.** Flag unconfirmed IDs explicitly.
6. **Every framework ID cited needs a traceable canonical source** — the framework's own site (nist.gov, ctid.mitre.org/fraud, owasp.org, docs.aws.amazon.com/wellarchitected) or the specific incident/report document the finding came from. "I recall this is the right ID" is not a source. If you can't point to where an ID came from, mark it unconfirmed rather than presenting it as settled — this project's credibility depends on every claim being provable, not just plausible.

## Output formats

### Format A — Markdown mapping table

| Finding | Framework | Function/Category/Tactic | ID | Rationale |
|---|---|---|---|---|
| Agent held broad "Reader" role that quietly expanded to write access | NIST CSF | Protect | PR.AA (verify subcategory) | Access-control scope creep, a Protect-function gap |
| Agent had no pre-execution policy check before high-impact actions | NIST AI RMF | Manage | MG (verify subcategory) | Missing runtime risk-response mechanism |
| Compromised credential used to move stolen funds | MITRE F3 | Monetization | FA0002 / F1xxx (verify) | Post-compromise conversion of access into fraud |
| Agent given curated tool access via allowlist only | OWASP Agentic Top 10 | (verify category) | — | Directly mitigates Excessive Agency risk category |

### Format B — agentskills.io-style YAML frontmatter

```yaml
---
name: agent-identity-least-privilege-control
nist_csf:
  - PR.AA  # verify exact subcategory
nist_ai_rmf:
  - MANAGE  # verify exact subcategory
mitre_f3: null  # not applicable — no fraud/monetization component
owasp_agentic:
  - "Excessive Agency"  # verify exact 2025 category name/number
---
```

## Typical tooling by category (for "what would a defender actually run" questions)

Illustrative market context, not endorsement — vendor choice depends on the org's existing stack.

| Category | Maps to | Representative tools |
|---|---|---|
| IAM / identity governance for agents | NIST CSF Protect / AWS WA Security pillar | Okta, Microsoft Entra ID, AWS IAM Identity Center |
| MFA / step-up authentication | NIST CSF Protect | Okta Verify, Duo, YubiKey (hardware keys) |
| Secrets & key management | NIST CSF Protect / AWS WA Security pillar | AWS KMS + Secrets Manager, HashiCorp Vault, Azure Key Vault |
| Just-in-time / short-lived privilege elevation | Microsoft's own least-privilege guidance for AI agents | AWS IAM Roles Anywhere + STS short-lived tokens, CyberArk, Entra PIM |
| CSPM / CNAPP (cloud security posture management) | AWS WA Security pillar | Wiz, Prisma Cloud, AWS Security Hub |
| GRC / compliance mapping platforms | NIST CSF, NIST AI RMF | ServiceNow GRC, OneTrust, Vanta |
| Agentic-app-specific guardrails (tool allowlisting, action-level policy) | OWASP Agentic Top 10 | Purpose-built agent runtime policy layers (e.g. AARM-conformant tooling) — still an emerging vendor category as of mid-2026 |

## When output is ambiguous or the mapping is contested

State confidence level plainly. These governance frameworks in particular have categories that legitimately overlap (a single control can satisfy both a CSF Protect subcategory and an AI RMF Manage subcategory) — say so rather than picking one arbitrarily.
