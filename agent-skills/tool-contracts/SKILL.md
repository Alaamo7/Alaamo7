---
name: tool-contracts
status: restored-from-documented-architecture
description: Define reliable contracts between agents and tools using strict schemas, preconditions, postconditions, error taxonomy, versioning, and compatibility rules.
---

# Tool Contracts Skill

Use explicit contracts so the agent knows exactly what a tool accepts, what it guarantees, and what failures mean.

## Contract fields

For each action define:

- Action name
- Description
- Input schema
- Required vs optional fields
- Preconditions
- Output schema
- Postconditions
- Side effects
- Error codes/classes
- Idempotency
- Version
- Compatibility notes

## Input rules

- Reject unknown destructive flags.
- Validate identifiers and paths.
- Prefer enums over arbitrary strings where the domain is bounded.
- Make defaults safe and documented.
- Do not infer missing high-risk parameters.

## Output rules

A caller should be able to distinguish:

```text
SUCCESS
PARTIAL_SUCCESS
CONFLICT
NOT_FOUND
PERMISSION_DENIED
INVALID_INPUT
TRANSIENT_FAILURE
PERMANENT_FAILURE
```

Do not return vague "done" responses for complex mutations.

## Preconditions and postconditions

Example:

```yaml
preconditions:
  - repository exists
  - target path is known
  - write permission granted
postconditions:
  - file exists at target path
  - returned revision identifies resulting state
```

## Contract versioning

Breaking changes require a version change when they alter required inputs, semantics, output shape, or side effects.

## Verification

Test contracts against:

- valid input
- missing required input
- malformed identifiers
- duplicate execution
- stale version/conflict
- permission denial
- timeout
- partial downstream failure

## Goal

The tool contract should reduce agent guesswork and make failures machine-actionable.