# Tools & Resources

Working list of tools and standards bodies referenced across this repo's projects and reports.

## Testing & Red-Teaming

**[Garak](https://garak.ai/)**
An open-source LLM vulnerability scanner. A "Policy Advisor" agent is only as good as its ability to resist being talked out of its own guardrails via prompt injection — Garak acts as a compliance auditor, running an agent through 100+ known attack vectors to check whether its guardrails actually hold.

*Sector application:* useful for a public-sector "Trust & Oversight" model — running Garak against an agent produces a quantitative safety report that can support alignment claims against standards like FedRAMP or ISO/IEC 27017.

## Defensive & Governance Tooling

Categories referenced in this repo's case studies and Claude Skills ([`claude-skills/offense-defense-skill.md`](../claude-skills/offense-defense-skill.md), [`claude-skills/governance-skill.md`](../claude-skills/governance-skill.md)). Illustrative market context, not endorsement — vendor choice depends on the org's existing stack.

| Category | Representative tools |
|---|---|
| SIEM (log aggregation + correlation) | Splunk, Microsoft Sentinel, IBM QRadar, Elastic Security |
| EDR/XDR (endpoint & extended detection/response) | CrowdStrike Falcon, Microsoft Defender for Endpoint, SentinelOne |
| Execution isolation / sandboxing | gVisor, Firecracker microVMs, Kata Containers |
| Secrets & key management | AWS KMS + Secrets Manager, HashiCorp Vault, Azure Key Vault |
| Just-in-time / short-lived privilege elevation | AWS IAM Roles Anywhere + STS, CyberArk, Entra PIM |
| Cloud posture / metadata protection | IMDSv2 enforcement, AWS GuardDuty, Wiz, Prisma Cloud |
| Agentic-app-specific guardrails | Purpose-built agent runtime policy layers (e.g. AARM-conformant tooling) — still an emerging vendor category as of mid-2026 |
| GRC / compliance mapping platforms | ServiceNow GRC, OneTrust, Vanta |

## Standards & Frameworks

**[OWASP](https://owasp.org)** — Top 10 for Agentic Applications and related application security guidance. Core to the framework stack used throughout this repo (see [`framework-reference/framework-reference.md`](../framework-reference/framework-reference.md)).

## Career / Transition Resources

**[DoD SkillBridge](https://www.skillbridge.mil/locations)** — DoD program for service members transitioning into civilian roles, including cybersecurity and AI security career paths.

## Repository

**GitHub:** [DreamTeam-10/READ.ME](https://github.com/DreamTeam-10/READ.ME) — this repo.
