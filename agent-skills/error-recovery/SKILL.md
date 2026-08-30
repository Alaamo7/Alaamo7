---
name: error-recovery
status: restored
description: Recover AI agent workflows from tool, model, data, permission, validation, and partial-execution failures using explicit classification, state preservation, safe rollback, retry, fallback, or escalation.
---

# Error Recovery Skill

## Goal

Recover from failures without losing state, duplicating actions, or falsely reporting success.

## Failure classes

- Input/data error
- Tool/API error
- Permission/auth error
- Model failure
- Timeout/transient failure
- Validation failure
- Partial execution
- External dependency failure
- Unknown failure

## Recovery flow

```text
Failure detected
  ↓
Capture exact error + current state
  ↓
Classify failure
  ↓
Determine whether side effects occurred
  ↓
Choose: repair input / retry / fallback / rollback / escalate
  ↓
Execute controlled recovery
  ↓
Re-verify objective and side effects
```

## Partial execution

Before retrying a consequential action, inspect whether the original action already succeeded partially or fully. Examples:

- File may already exist.
- Email may already have been sent.
- GitHub commit may already be present.
- Disk/configuration may already be changed.

Never blindly repeat side-effecting actions.

## Rollback

Use rollback when:

- A reversible change produced a regression.
- Verification clearly failed.
- Prior state is known and safe to restore.

Do not invent rollback capability when the action is irreversible.

## Escalation

Provide:

- Objective
- Failed step
- Exact error
- Side effects observed
- Recovery attempts
- Current state
- Required access/decision

## Completion rule

A recovered run must pass the same verification criteria as a normal successful run.