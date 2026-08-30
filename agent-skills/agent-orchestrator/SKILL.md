---
name: agent-orchestrator
status: restored-from-documented-architecture
description: Decompose complex tasks, select skills and tools, coordinate execution stages, manage dependencies and state, enforce verification gates, and escalate blocked work without falsely reporting completion.
---

# Agent Orchestrator Skill

Coordinate complex agent work across skills, tools, models, and verification steps.

## Responsibilities

- Understand the objective and success criteria.
- Decompose work into executable stages.
- Select only the required skills/tools.
- Respect dependencies and ordering.
- Track state and blockers.
- Trigger verification after consequential actions.
- Retry selectively when there is evidence a retry can succeed.
- Escalate when permissions, capability, or evidence are insufficient.

## Core workflow

```text
Objective
  ↓
Define success criteria
  ↓
Decompose task
  ↓
Map dependencies
  ↓
Select skills/tools/models
  ↓
Execute stage
  ↓
Verify result
  ↓
Update state
  ↓
Next stage / repair / escalate
  ↓
Final verification
```

## Planning rules

1. Prefer the smallest plan that safely reaches the objective.
2. Do not create multiple agents unless specialization or parallelism materially helps.
3. Do not front-load every available skill into context.
4. Mark destructive or external actions as gated steps.
5. Keep facts, hypotheses, and planned actions separate.

## State schema

```yaml
objective: ""
success_criteria: []
current_stage: ""
completed_stages: []
pending_stages: []
blocked_stages: []
skills_loaded: []
tools_used: []
artifacts: []
verification_status: "pending"
errors: []
```

## Dependency handling

Examples:

- Do not send an application before the CV is tailored and verified.
- Do not publish documentation before the technical result is confirmed.
- Do not run controller-level USB repair before confirming destructive-action consent.
- Do not merge code before tests/validation pass when the workflow requires them.

## Completion rule

A task is complete only when:

- Required outputs exist.
- Consequential actions were verified.
- Known blockers are resolved or clearly reported.
- Final output matches the original success criteria.

Never convert partial execution into a success claim.