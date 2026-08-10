# READ.ME

### Cybersecurity × AI Security, cross-mapped to governance frameworks

This repository bridges traditional cybersecurity disciplines with AI safety and fraud-mitigation standards. Every artifact here — incident breakdowns, governance tooling, reference material — is cross-mapped against a consistent stack of recognized frameworks, so the analysis holds up whether the reader is a security engineer, a compliance lead, or a non-technical stakeholder.

## Why this repo exists

Most AI security commentary either stays abstract (principles with no mapping to real controls) or stays narrowly technical (a CVE writeup with no governance context). This repo tries to sit in between: take a real incident or policy development, run it through the framework stack below, and land on questions or controls a team could act on this week.

## Framework stack

| Framework | Version | Scope |
|---|---|---|
| 🧠 NIST AI RMF | 1.0 | Risk management guidance for trustworthy/secure AI governance (Govern, Map, Measure, Manage) |
| 🏛️ ISO/IEC 42001 | 2023 | AI management system certification standard |
| 🤖 MITRE ATLAS | v5.4 | Adversarial threat landscape targeting AI/ML systems |
| 📋 OWASP Top 10 for Agentic Applications | 2025/2026 | Top risks specific to agentic AI application design and deployment |
| 🛡️ MITRE ATT&CK | v19.1 | Adversary tactics, techniques, and procedures for traditional enterprise networks |
| 🧱 MITRE D3FEND | v1.3 | Engineering countermeasures to detect, isolate, and deceive adversaries |
| 💸 MITRE F3 (Fight Fraud Framework) | v1.1 | Post-compromise behaviors — how access converts into financial fraud |
| 🏦 NIST CSF | 2.0 | High-level organizational cybersecurity risk guidance |
| ☁️ AWS Well-Architected Framework | Current (6 pillars) | Cloud workload architecture, especially the Security pillar |
| 🎓 MIT AI Risk Repository | — | Living taxonomy of AI risks for prioritization work |
| 📡 CISA/NSA Joint Advisories | ongoing | Government-issued guidance and threat advisories |

Full detail on each framework's scope and canonical docs: [`framework-reference/framework-reference.md`](framework-reference/framework-reference.md).

## Repo structure

```
READ.ME/
├── framework-reference/  → framework reference & analytical methodology
├── governance-raci/      → AI Agent Governance RACI matrix + narrative guide
├── case-studies/         → incident/policy breakdowns, mapped to frameworks
├── claude-skills/        → Claude Skills that auto-apply the framework stack (offense-defense-skill, governance-skill)
└── tools-and-resources/  → tools, standards bodies, and training links used across this work
```

## How the analysis works

Every case study follows the same structure: a real incident or policy development is the entry point, the framework stack determines the lens (not the other way around), and each writeup closes with concrete governance questions rather than a forward-looking teaser. Details in [`framework-reference/methodology.md`](framework-reference/methodology.md).

## Companion content

This repo runs alongside an ongoing LinkedIn series applying the same framework-mapped approach to current AI security incidents, for both technical and non-technical audiences.
