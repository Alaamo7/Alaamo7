---
name: agent-logging
status: restored
description: Design structured execution logs for AI agents and harnesses so actions, tool calls, decisions, errors, retries, costs, and verification results can be inspected without exposing secrets.
---

# Agent Logging Skill

Create useful operational logs for agent runs without turning logs into an uncontrolled transcript archive.

## Goals

Logs should answer:

- What task was attempted?
- Which model and skills were used?
- Which tools/actions were executed?
- What succeeded or failed?
- What changed?
- What was verified?
- How much did the run cost?
- Where did human approval occur?

## Core principles

1. Log events, not hidden reasoning.
2. Redact secrets and sensitive personal data.
3. Use stable event types and IDs.
4. Distinguish requested action, actual action, and verified result.
5. Record retries and fallback paths.
6. Preserve enough evidence for incident review.

## Recommended event schema

```json
{
  "run_id": "...",
  "timestamp": "...",
  "event_type": "tool_call|tool_result|decision|verification|error|retry|approval|completion",
  "component": "orchestrator|skill|tool|model|verifier",
  "task_step": "...",
  "status": "started|success|failed|blocked|skipped",
  "summary": "...",
  "duration_ms": 0,
  "cost": null,
  "metadata": {}
}
```

## Never log

- API keys
- Passwords
- Session tokens
- Full auth headers
- Private document contents when a hash/reference is sufficient
- Hidden chain-of-thought

## Run summary

At completion produce:

```markdown
# Agent Run Summary
- Run ID:
- Objective:
- Models:
- Skills:
- Tools:
- Key actions:
- Verification:
- Errors/retries:
- Human approvals:
- Cost/usage:
- Final status:
```

## Observability rule

A successful tool response is not automatically a successful task. Log verification as a separate event.
