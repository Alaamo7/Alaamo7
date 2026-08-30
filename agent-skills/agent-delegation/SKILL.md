---
name: agent-delegation
status: restored-from-documented-architecture
description: Delegate subtasks to specialized agents using bounded objectives, context packages, authority limits, deadlines or stop conditions, and explicit acceptance criteria.
---

# Agent Delegation

Delegate work without losing control of scope, evidence, or ownership.

## Delegation package

A delegated task should contain:

- Parent objective
- Subtask objective
- Why this agent is selected
- Required inputs/context
- Allowed tools/actions
- Constraints
- Expected output schema
- Acceptance criteria
- Stop/escalation conditions

## Rules

1. Delegate complete, testable units of work.
2. Do not delegate ambiguous ownership of destructive or external actions.
3. Pass minimum sufficient context, not the full parent transcript by default.
4. Require workers to report evidence and unresolved uncertainty.
5. Parent/supervisor retains responsibility for final integration and acceptance.

## Delegation flow

```text
Identify subtask
  ↓
Select qualified agent
  ↓
Package bounded context
  ↓
Set permissions + acceptance criteria
  ↓
Worker executes
  ↓
Structured return
  ↓
Supervisor verifies/integrates
```

## Failure modes

Escalate or reassign when:

- Required capability is unavailable
- Dependency is missing
- Permission boundary blocks required work
- Output repeatedly fails acceptance criteria
- Agent discovers material conflict with parent assumptions