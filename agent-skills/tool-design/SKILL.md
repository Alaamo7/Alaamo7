---
name: tool-design
status: restored-from-documented-architecture
description: Design agent tools with a narrow purpose, explicit inputs/outputs, permission boundaries, verification requirements, and predictable failure behavior.
---

# Tool Design Skill

Design tools that are easy for an agent to call correctly and hard to misuse.

## Core principles

1. One clear responsibility per tool where practical.
2. Prefer explicit schemas over free-form arguments.
3. Separate read-only actions from mutating actions.
4. Minimize permissions and side effects.
5. Define success and failure states explicitly.
6. Require verification for consequential mutations.
7. Do not expose secrets in arguments, logs, or outputs.

## Design workflow

```text
Task capability
  ↓
Define action boundary
  ↓
Define input schema
  ↓
Define output schema
  ↓
Define permissions
  ↓
Define failure modes
  ↓
Define verification
  ↓
Test misuse and edge cases
```

## Tool specification

Document:

- Name
- Purpose
- Read/write classification
- Required permissions
- Inputs and validation
- Outputs
- Side effects
- Idempotency behavior
- Timeout/retry guidance
- Security concerns
- Verification method

## Design checks

Reject designs where:

- one tool performs unrelated actions;
- an optional argument can silently trigger destructive behavior;
- success does not mean the intended effect occurred;
- error messages hide the cause;
- raw credentials must be passed through the model;
- the output is too ambiguous for downstream reasoning.

## Example contract

```yaml
name: update_text_file
mode: write
inputs:
  path: required string
  content: required string
  expected_version: optional string
outputs:
  status: success|conflict|error
  new_version: string|null
verification:
  reopen file and compare expected content
```

## Completion checklist

- Purpose is narrow.
- Inputs are validated.
- Outputs are structured.
- Permissions are minimal.
- Mutations are explicit.
- Failure modes are documented.
- Verification is possible.
