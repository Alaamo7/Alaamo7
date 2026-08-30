---
name: resume-recovery
status: restored
description: Resume interrupted agent workflows from verified checkpoints by reconstructing the minimum required state, checking external side effects, and continuing from the next safe step without duplicating prior actions.
---

# Resume Recovery Skill

Use this skill after interruption, timeout, model/tool failure, process restart, or other partial execution.

## Recovery workflow

```text
Load latest trusted checkpoint
        ↓
Inspect recorded side effects
        ↓
Re-validate external state where needed
        ↓
Identify incomplete/uncertain step
        ↓
Choose safe continuation point
        ↓
Resume
        ↓
Verify new progress
```

## Rules

1. Never assume the last attempted action failed merely because the run stopped.
2. Recheck external systems before repeating writes, sends, payments, tickets, commits, or destructive actions.
3. Resume from the last verified safe boundary, not from memory of the conversation.
4. Mark uncertain actions explicitly until confirmed.
5. Preserve prior verified outputs rather than regenerating them unnecessarily.
6. If checkpoint data is stale or contradictory, prefer external truth and escalate uncertainty.

## Duplicate-risk examples

Before repeating:

- email send → search Sent/target state,
- GitHub file write → fetch file/commit,
- ticket creation → search ticket system,
- calendar creation → search matching event,
- payment/order → check transaction/order state.

## Recovery result

Document:

```markdown
# Recovery Resume
- Last trusted checkpoint:
- Confirmed completed work:
- Side effects rechecked:
- Uncertain actions:
- Safe resume step:
- Work intentionally not repeated:
```
