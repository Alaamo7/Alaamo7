---
name: dependency-management
status: restored
description: Track prerequisite data, tool availability, permissions, artifacts, task ordering, and blocking dependencies so agents execute steps only when required conditions are satisfied.
---

# Dependency Management Skill

Use this skill to prevent agents from executing steps before their prerequisites are ready.

## Dependency types

- Data dependency
- Artifact dependency
- Tool dependency
- Permission dependency
- Human approval dependency
- External-system dependency
- Temporal/event dependency

## Rules

1. Declare prerequisites explicitly.
2. Distinguish hard dependencies from optional enhancements.
3. Do not fabricate missing dependency outputs.
4. A blocked dependency must identify what is missing and what can still proceed.
5. Recheck dependencies before retrying downstream steps.
6. Avoid circular dependencies.

## Dependency record

```yaml
step: deploy
requires:
  - tests_passed
  - secrets_configured
  - rollback_plan
  - approval_if_required
status: blocked|ready|satisfied
```

## DAG thinking

Prefer Directed Acyclic Graph structures for complex workflows so independent branches can proceed while blocked branches wait.

Example:

```text
Source collection ──→ Research ──→ Draft
        │                         │
        └────→ Asset collection ──┘
```

## Failure handling

If a dependency fails:

- stop only dependent nodes,
- preserve completed independent work,
- record the failed prerequisite,
- provide the safest recovery or escalation path.
