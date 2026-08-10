"""
agent_action_gate.py

Reference implementation of a pre-execution policy gate for autonomous AI agents,
following the AARM (Autonomous Action Runtime Management) pattern referenced in
case-studies/03-agentic-sandbox-escape-breach.

The idea: every action an agent wants to take is intercepted BEFORE execution,
checked against an intent-aware policy, and logged in a tamper-evident record.
This is the concrete, code-level version of "human-in-the-loop" — it doesn't
require a human to click approve on every action, but it does require every
action to pass through a real checkpoint instead of executing directly.

This is a minimal, dependency-free reference you can adapt to your own agent
framework's tool-calling layer. It is NOT a production-hardened implementation —
treat the policy rules and logging as a starting point, not a finished control.
"""

from __future__ import annotations
import hashlib
import json
import time
from dataclasses import dataclass, field
from enum import Enum
from typing import Callable


class Decision(Enum):
      ALLOW = "allow"
      DENY = "deny"
      ESCALATE = "escalate"  # requires human review before proceeding


@dataclass
class AgentAction:
      agent_id: str
      action_type: str          # e.g. "network_request", "file_read", "credential_fetch"
    target: str                # e.g. an IP, a file path, an API endpoint
    justification: str         # the agent's own stated reason, logged for audit
    metadata: dict = field(default_factory=dict)


@dataclass
class PolicyResult:
      decision: Decision
      reason: str
      matched_rule: str | None = None


class ActionPolicyGate:
      """
          Intercepts agent actions before execution. Policy rules are evaluated in
              order; the first matching rule decides the outcome. Every decision is
                  logged with a hash chain so the audit trail is tamper-evident.
                      """

    def __init__(self):
              self._rules: list[tuple[str, Callable[[AgentAction], bool], Decision, str]] = []
              self._audit_log: list[dict] = []
              self._last_hash = "0" * 64

    def add_rule(self, name: str, predicate: Callable[[AgentAction], bool],
                                  decision: Decision, reason: str) -> None:
                                            """Register a policy rule. Predicate returns True if the rule applies."""
                                            self._rules.append((name, predicate, decision, reason))

    def evaluate(self, action: AgentAction) -> PolicyResult:
              for name, predicate, decision, reason in self._rules:
                            if predicate(action):
                                              result = PolicyResult(decision=decision, reason=reason, matched_rule=name)
                                              self._log(action, result)
                                              return result

                        # Default posture: deny by default rather than allow by default.
                        # An unrecognized action type should never silently pass through.
                        result = PolicyResult(
                                      decision=Decision.DENY,
                                      reason="No matching allow rule; default-deny posture applied.",
                        )
        self._log(action, result)
        return result

    def _log(self, action: AgentAction, result: PolicyResult) -> None:
              entry = {
                  "timestamp": time.time(),
                  "agent_id": action.agent_id,
                  "action_type": action.action_type,
                  "target": action.target,
                  "justification": action.justification,
                  "decision": result.decision.value,
                  "matched_rule": result.matched_rule,
                  "reason": result.reason,
                  "prev_hash": self._last_hash,
    }
        entry_bytes = json.dumps(entry, sort_keys=True).encode()
        entry_hash = hashlib.sha256(entry_bytes).hexdigest()
        entry["entry_hash"] = entry_hash
        self._last_hash = entry_hash
        self._audit_log.append(entry)

    def audit_log(self) -> list[dict]:
              return list(self._audit_log)

    def verify_log_integrity(self) -> bool:
              """Walk the hash chain to confirm no audit entry has been altered or removed."""
              prev = "0" * 64
              for entry in self._audit_log:
                            check = dict(entry)
                            stored_hash = check.pop("entry_hash")
                            if check["prev_hash"] != prev:
                                              return False
                                          recomputed = hashlib.sha256(json.dumps(check, sort_keys=True).encode()).hexdigest()
                            if recomputed != stored_hash:
                                              return False
                                          prev = stored_hash
                        return True


# ---------------------------------------------------------------------------
# Example: policy rules modeled on the failure points in the sandbox-escape case study
# ---------------------------------------------------------------------------

def build_default_gate() -> ActionPolicyGate:
      gate = ActionPolicyGate()

    # Deny outright: any attempt to reach the cloud instance metadata service
    # from a workload that has no declared need for cloud credentials.
    gate.add_rule(
              name="block-imds-access",
              predicate=lambda a: a.action_type == "network_request" and a.target == "169.254.169.254",
              decision=Decision.DENY,
              reason="Direct IMDS access is blocked by default; use a scoped credential broker instead.",
    )

    # Escalate to human review: any action that would use a credential with
    # broader scope than the current task declares it needs.
    gate.add_rule(
              name="escalate-privilege-mismatch",
              predicate=lambda a: a.action_type == "credential_fetch"
              and a.metadata.get("requested_scope") == "cluster-admin",
              decision=Decision.ESCALATE,
              reason="Requested credential scope exceeds task-declared need; requires human approval.",
    )

    # Deny outright: reading local files outside an explicit allowlist,
    # which is exactly how the HDF5/Jinja2 vector in the case study worked.
    gate.add_rule(
              name="block-unallowed-local-read",
              predicate=lambda a: a.action_type == "file_read"
              and not a.target.startswith(("/data/allowed/", "/tmp/sandboxed/")),
              decision=Decision.DENY,
              reason="File reads are restricted to explicitly allowlisted paths.",
    )

    # Allow: file reads that DO fall within the allowlisted paths above.
    # Rules are evaluated in order, so this must come after the block rule —
    # anything reaching here has already passed the allowlist check.
    gate.add_rule(
              name="allow-allowlisted-read",
              predicate=lambda a: a.action_type == "file_read"
              and a.target.startswith(("/data/allowed/", "/tmp/sandboxed/")),
              decision=Decision.ALLOW,
              reason="Path falls within the explicit read allowlist.",
    )

    return gate


if __name__ == "__main__":
      gate = build_default_gate()

    test_actions = [
              AgentAction("agent-01", "network_request", "169.254.169.254",
                                              "Need cloud credentials to continue task"),
              AgentAction("agent-01", "credential_fetch", "connector-svc-account",
                                              "Need broad access to finish faster",
                                              metadata={"requested_scope": "cluster-admin"}),
              AgentAction("agent-01", "file_read", "/proc/self/environ",
                                              "Checking environment for config values"),
              AgentAction("agent-01", "file_read", "/data/allowed/dataset.csv",
                                              "Loading the assigned training dataset"),
    ]

    for action in test_actions:
              result = gate.evaluate(action)
              print(f"[{result.decision.value.upper():9}] {action.action_type:16} -> {action.target:24} "
                    f"({result.matched_rule or 'default-deny'})")

    print("\nAudit log integrity check:", "PASS" if gate.verify_log_integrity() else "FAIL")
