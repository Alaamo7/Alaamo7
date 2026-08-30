---
name: concurrency-control
status: restored
description: Coordinate parallel agent work safely by defining shared-resource locks, conflict detection, serialization points, merge policies, and race-condition prevention for tools and workflows.
---

# Concurrency Control Skill

Use this skill when multiple agents, branches, workers, or workflow paths may operate at the same time.

## Main risks

- Two workers update the same file or record.
- Duplicate external actions occur in parallel.
- One worker reads stale state while another writes.
- Conflicting outputs are merged without validation.
- Shared rate limits or quotas are exceeded.

## Rules

1. Parallelize independent work, not shared mutable state blindly.
2. Identify resources that require serialization.
3. Use optimistic concurrency when supported, such as version/SHA checks.
4. Use locks or single-writer rules for high-conflict resources.
5. Re-read shared state before committing changes.
6. Define merge/conflict policy before parallel execution.
7. Preserve operation IDs to detect duplicates.

## Examples

### GitHub file update

Fetch current SHA → modify → update with expected SHA → if conflict, re-fetch and reconcile.

### Shared task state

Allow parallel research branches, but serialize updates to the canonical completion state.

## Concurrency record

```yaml
resource: repository/path/file.md
mode: optimistic
expected_version: ...
on_conflict: re-read_and_reconcile
```

## Completion

Parallel branches are not considered fully complete until their outputs are reconciled and cross-checked for contradictions or overlapping side effects.
