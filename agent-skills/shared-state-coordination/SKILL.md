---
name: shared-state-coordination
status: restored-from-documented-architecture
description: Coordinate multiple agents around shared task state using explicit ownership, version checks, conflict detection, append-only evidence, and controlled updates to mutable fields.
---

# Shared State Coordination

Use shared state as a coordination contract, not as an unstructured chat transcript.

## State model

Recommended shared fields:

- Task objective
- Workflow stage
- Assigned agents
- Resource ownership
- Completed steps
- Verified artifacts
- Pending dependencies
- Open risks
- External side effects
- Version/revision
- Last updater

## Rules

1. One owner per mutable resource when practical.
2. Use version/revision checks before updates.
3. Preserve append-only evidence/history separately from mutable summary fields.
4. Detect stale writes and conflicting updates.
5. Never infer completion from another agent's intent; require verified state.
6. Shared state must not contain secrets unless the backing store is explicitly appropriate.

## Update pattern

```text
Read latest state
  ↓
Confirm ownership + version
  ↓
Apply bounded update
  ↓
Persist new revision
  ↓
Verify persisted state
```

## Conflict handling

On conflict:

- Stop conflicting mutation.
- Compare revisions and side effects.
- Prefer verified external state over stale local assumptions.
- Escalate unresolved ownership or semantic conflicts to supervisor.