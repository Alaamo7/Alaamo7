---
name: filesystem-operations
status: restored
description: Perform agent-controlled filesystem reads, writes, moves, copies, renames, and deletes with path validation, scope boundaries, backup awareness, conflict handling, and post-action verification.
---

# Filesystem Operations Skill

Use this skill when an agent reads or changes local or mounted files.

## Safety rules

1. Resolve the exact target path before mutation.
2. Distinguish files from folders.
3. Prefer read/inspect before write/delete.
4. Protect system and user-critical paths.
5. Do not recursively delete unless explicitly intended and authorized.
6. Use conflict-safe behavior for rename/move/copy.
7. Verify the resulting filesystem state after changes.

## Operations

### Read

- Confirm file exists.
- Detect encoding/type when relevant.
- Use bounded reads for large files.

### Write/update

- Preserve original when risk is meaningful.
- Use atomic or temp-file replacement when supported.
- Avoid truncating files because of partial input.

### Move/rename

- Check destination conflicts.
- Preserve extensions when required.
- Verify source disappears and destination exists.

### Delete

- Confirm target identity.
- Prefer recoverable deletion where the environment supports it.
- Never infer recursive deletion.

## Path controls

Reject ambiguous targets such as:

- wildcard-heavy destructive paths
- unresolved relative paths in high-risk tasks
- path traversal outside authorized workspace
- symlink/junction targets that escape expected boundaries

## Verification

Examples:

```text
Write → reopen → compare content/hash
Move → check destination + source state
Delete → confirm target absent
Copy → compare size/hash when appropriate
```

## Operation log

Record target, action, pre-state, post-state, conflicts, backup/rollback information, and verification result.