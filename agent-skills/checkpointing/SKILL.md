---
name: checkpointing
status: restored
description: Create resumable checkpoints for long-running agent workflows by persisting verified progress, outputs, side effects, blockers, and next actions at safe boundaries.
---

# Checkpointing Skill

Use checkpoints to reduce repeated work and make recovery safe after interruptions or failures.

## Checkpoint contents

Store:

- task/workflow ID
- checkpoint ID
- verified completed steps
- produced artifacts and identifiers
- external side effects
- pending dependencies
- approvals obtained
- unresolved warnings
- next safe step

## Rules

1. Checkpoint after meaningful verified milestones, not every trivial operation.
2. Never checkpoint unverified success as completed work.
3. Record side effects precisely so resumed runs do not repeat them.
4. Keep checkpoint payloads compact and durable.
5. Avoid storing secrets in checkpoint data.

## Example

```yaml
checkpoint: cp-03
completed:
  - job_discovered
  - fit_evaluated
  - cv_generated
verified: true
external_side_effects: []
next_step: pre_send_review
```

## Good checkpoint boundaries

- after source collection
- after successful artifact generation and validation
- before external sending
- after external side effect and confirmation
- before/after destructive operations
- after completing a workflow phase
