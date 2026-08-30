---
name: connector-routing
status: restored-from-documented-architecture
description: Route tasks to the correct connected service or tool based on data ownership, operation type, permissions, freshness, and write-back requirements.
---

# Connector Routing Skill

Choose the authoritative connector instead of using the wrong data source or duplicating state.

## Routing questions

1. Where does the authoritative data live?
2. Is the task read-only or mutating?
3. Does the operation require account context?
4. Is freshness important?
5. Must changes write back to the original source?
6. Does the selected connector support the exact operation?

## Examples

- GitHub repository mutation → GitHub connector, not generic web browsing.
- Google Drive document update → Drive/Docs connector when original-file editing is required.
- Gmail send/reply → authenticated Gmail action, not a generic HTTP workaround.
- Public current information → web/search rather than private account connectors unless user-owned context is required.

## Routing workflow

```text
Task
 ↓
Identify authoritative system
 ↓
Classify read/write
 ↓
Check available connector capabilities
 ↓
Select minimum required action
 ↓
Execute
 ↓
Verify in source system
```

## Fallback rules

Do not silently substitute a weaker connector when it cannot preserve identity, permissions, or write-back semantics.

If the correct connector cannot perform the requested action:

- state the capability gap;
- preserve the original resource;
- do not create replacement copies unless requested.

## Security

Only expose data necessary for the task. Do not copy private connector data to public repositories or external services without explicit need and authorization.

## Verification

For mutations, verify against the authoritative source after execution.