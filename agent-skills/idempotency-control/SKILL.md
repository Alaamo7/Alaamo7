---
name: idempotency-control
status: restored
description: Prevent duplicate side effects by designing idempotent agent actions, deduplication keys, existence checks, safe upserts, and repeatable execution semantics for long-running workflows.
---

# Idempotency Control Skill

Use this skill whenever a workflow may retry, resume, or receive duplicate events.

## Goal

Repeated execution should not unintentionally create duplicate external effects.

## Techniques

- Existence checks
- Stable idempotency keys
- Upsert instead of blind create
- Compare-before-write
- Detect duplicate sends/submissions
- Store operation/result identifiers
- Separate read retries from write retries

## Example key

```text
job_application:<company>:<role>:<posting_id>
```

or

```text
artifact_publish:<project>:<version>
```

## Rules

1. Assign a stable identity to consequential operations when possible.
2. Before repeating a write, inspect whether the intended effect already exists.
3. Record external IDs returned by successful operations.
4. Do not rely only on local state when external state can be checked.
5. Treat non-idempotent operations as high-risk retry targets.
6. Prefer update/replace semantics when duplicate creation would be harmful.

## Idempotency checklist

For each consequential action ask:

- What uniquely identifies this operation?
- Can it be safely repeated?
- How can existing completion be detected?
- Is there an API idempotency key?
- What external result ID should be stored?
- What happens if the first response is lost after success?
