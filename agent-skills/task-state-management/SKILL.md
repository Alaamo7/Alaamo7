---
name: task-state-management
status: restored
description: Track long-running agent task state, objectives, completed work, blockers, pending actions, verification results, and resumable execution metadata without conflating transient reasoning with durable state.
---

# Task State Management Skill

Use this skill when an agent must execute multi-step or long-running work without losing progress or repeating completed actions.

## State model

Track explicit fields such as:

```yaml
task_id: ...
objective: ...
status: planned|running|blocked|waiting_approval|verifying|completed|failed
current_step: ...
completed_steps: []
pending_steps: []
blockers: []
artifacts: []
external_actions: []
verification: []
last_checkpoint: ...
```

## Rules

1. Durable state stores outcomes and execution facts, not hidden reasoning.
2. Mark a step complete only after required verification.
3. Preserve external side effects such as emails sent, files written, tickets created, or repository changes.
4. Store blocker cause and required next action.
5. Record artifact identifiers/paths rather than duplicating large content.
6. Keep state transitions explicit.

## State transitions

```text
planned → running → verifying → completed
                ↘ blocked
                ↘ waiting_approval
                ↘ failed
```

A blocked or failed run may return to `running` only when the blocking condition changes or a recovery path is selected.

## Completion criteria

Do not mark `completed` when:

- a tool call was made but not checked,
- a required external side effect is uncertain,
- an approval gate remains unresolved,
- a required artifact is missing,
- validation failed.

## Resume payload

When resuming a task, load only the state necessary to continue:

- objective
- last verified checkpoint
- completed actions and side effects
- pending dependency
- next safe step
