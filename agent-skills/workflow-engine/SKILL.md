---
name: workflow-engine
status: restored
description: Design and execute explicit agent workflows with steps, conditions, branches, dependencies, retries, approvals, verification gates, and terminal states for reliable multi-step task automation.
---

# Workflow Engine Skill

Use this skill when a task requires an explicit executable workflow rather than a free-form plan.

## Workflow structure

Represent work as nodes and transitions:

```yaml
workflow:
  id: ...
  objective: ...
  steps:
    - id: discover
      action: ...
      on_success: evaluate
      on_failure: recover_discovery
```

## Step types

- Action
- Decision
- Validation
- Approval
- Wait/event
- Recovery
- Completion

## Rules

1. Each step must have a clear purpose and expected result.
2. Define what counts as success before executing the step.
3. Branch based on observed outputs, not vague intuition.
4. Do not hide destructive/external actions inside generic steps.
5. Attach verification gates to consequential actions.
6. Persist workflow position for resumability.
7. Define terminal states: completed, failed, cancelled, escalated.

## Example

```text
Discover jobs
    ↓
Validate posting
    ↓
Evaluate fit
 ┌──┴───┐
Skip   Tailor CV
          ↓
      Pre-send QA
          ↓
     Human gate?
          ↓
        Apply
          ↓
       Verify
          ↓
        Track
```

## Workflow definition checklist

- Entry condition
- Inputs
- Steps
- Dependencies
- Branch conditions
- Retry policy
- Approval gates
- Verification gates
- Failure path
- Resume point
- Completion criteria
