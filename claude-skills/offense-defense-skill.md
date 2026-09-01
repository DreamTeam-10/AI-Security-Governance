---
name: offense-defense-skill
description: Maps a cybersecurity or AI-security incident, attack technique, or defensive control to MITRE ATT&CK, MITRE ATLAS, and MITRE D3FEND with correct current version numbers and specific tactic/technique/countermeasure IDs. Use this skill whenever building AI security case studies, incident writeups, GitHub repo skill files (agentskills.io-style YAML frontmatter), threat models, or LinkedIn/report content that needs an attack or control tied to one of these three frameworks — even if the user just describes an attack in plain language without naming the framework. Always use this skill instead of recalling technique IDs from memory, since IDs and version numbers change across framework releases.
---

# MITRE Offense/Defense Framework Mapper

Maps real-world or hypothetical attacker behavior (ATT&CK, ATLAS) and defensive countermeasures (D3FEND) to current framework IDs. Covers traditional enterprise attacks (ATT&CK), AI/ML-specific adversarial attacks (ATLAS), and engineering countermeasures (D3FEND).

## Before mapping anything: verify current versions

Framework versions and technique sets update on independent release cycles. **Do not cite a version number from this file's baseline table without spot-checking it first** if the task is for a formal deliverable (case study, repo file, report) — a stale version number is a credibility problem in security writing.

- Web search `"MITRE ATT&CK" current version` (or ATLAS / D3FEND) if it's been more than ~4-6 weeks since last checked in this conversation, or if the user is publishing/shipping the output.
- For quick internal discussion or drafts, the baseline table below is fine as a starting point.

**Baseline versions (last verified 2026-08-05 — re-check before formal use):**

| Framework | Version | Scope | Canonical source |
|---|---|---|---|
| MITRE ATT&CK | v19.1 | 14 Enterprise tactics · 286 techniques (traditional enterprise TTPs; Reconnaissance and Resource Development folded in from PRE-ATT&CK as of v8 — a commonly cited "15" is outdated) | attack.mitre.org |
| MITRE ATLAS | v5.4 | 16 tactics · 84 techniques (AI/ML adversarial threats) | atlas.mitre.org |
| MITRE D3FEND | v1.3 | 7 categories · 267 techniques (defensive countermeasures) | d3fend.mitre.org |

## Mapping logic

1. **Read the incident/control description carefully.** Identify the discrete action(s), not just the overall narrative — one incident often maps to multiple technique IDs across multiple phases (initial access, execution, privilege escalation, lateral movement, exfiltration, etc.).
2. **Choose the right framework per action:**
   - Traditional IT/cloud/network attacker behavior (credential theft, lateral movement, C2, supply-chain abuse) → **ATT&CK**
   - Attacks specific to the AI/ML pipeline itself (prompt injection, model extraction, training-data poisoning, sandbox/evaluation escape by an AI agent, jailbreaks) → **ATLAS**
   - Any defensive/detective/deceptive countermeasure being described or recommended → **D3FEND**
3. **Do not force a mapping.** If an action has no clean ID in a framework (common for very new agentic-AI behavior — e.g. an agent's own tool-use decisions mid-attack), say so explicitly rather than inventing an ID. Note it as an "emerging technique, not yet catalogued" rather than guessing a T-number.
4. **Cite the rationale**, not just the ID — one sentence on why that ID applies, referencing the specific mechanic (e.g. "T1078 Valid Accounts, because the agent authenticated using a stolen static password read from the pod's environment variables").
5. **Never fabricate a technique ID.** If unsure of the exact ID, say "technique in the [tactic name] category, exact ID not confirmed — verify against atlas.mitre.org" rather than presenting a guess as fact.

## Output formats

### Format A — Markdown mapping table (for case studies, reports, LinkedIn-support docs)

| Phase | Action | Framework | ID | Rationale |
|---|---|---|---|---|
| Initial Access | Sandbox escape via zero-day in package proxy | ATLAS | AML.T00xx (verify) | AI agent broke its evaluation sandbox boundary to reach the open internet |
| Lateral Movement | Stolen service-account token used to access cluster API | ATT&CK | T1078 | Valid Accounts — reused a legitimate credential harvested from pod environment |
| Countermeasure | Blocking pod-level access to cloud instance metadata service | D3FEND | D3-xxx (verify) | Network isolation control that prevents metadata-to-credential escalation path |

### Format B — agentskills.io-style YAML frontmatter (for DreamTeam-10 repo skill files)

```yaml
---
name: detecting-agentic-sandbox-escape
mitre_attack:
  - T1078   # Valid Accounts
  - T1021   # Remote Services (lateral movement)
mitre_atlas:
  - AML.T00xx  # verify exact ID — sandbox/evaluation escape
mitre_d3fend:
  - D3-xxx  # verify exact ID — network isolation / IMDS lockdown
---
```

Leave a `# verify exact ID` comment on any ID you have not confirmed against the live framework site in the current session — never ship an unverified ID silently.

## Typical tooling by category (for "what would a defender actually run" questions)

When a case study or control needs a concrete tool example rather than just a framework ID, these are the categories practitioners commonly reach for. Treat this as illustrative market context, not an endorsement — always note that specific vendor choice depends on the org's existing stack.

| Category | Maps to | Representative tools |
|---|---|---|
| SIEM (log aggregation + correlation) | ATT&CK Detect / D3FEND Detect | Splunk, Microsoft Sentinel, IBM QRadar, Elastic Security |
| EDR/XDR (endpoint & extended detection/response) | ATT&CK Detect+Respond / D3FEND Isolate | CrowdStrike Falcon, Microsoft Defender for Endpoint, SentinelOne |
| Network detection & analysis | ATT&CK Lateral Movement detection | Zeek, Corelight, Darktrace |
| Sandboxing / isolation for untrusted code execution | D3FEND Isolate | gVisor, Firecracker microVMs, Kata Containers — relevant directly to the HF dataset-processing-worker case study |
| Cloud posture / metadata protection | D3FEND Harden | IMDSv2 enforcement, AWS GuardDuty, Wiz, Prisma Cloud |
