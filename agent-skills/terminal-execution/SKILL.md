---
name: terminal-execution
status: restored
description: Execute shell, PowerShell, or terminal commands through an agent with command classification, environment checks, least privilege, output capture, timeout controls, and verification.
---

# Terminal Execution Skill

Use the terminal as an execution tool, not a guessing machine.

## Before execution

Determine:

- OS and shell
- Working directory
- Required privileges
- Expected side effects
- Whether the command is read-only, mutating, destructive, or privileged
- Success criteria

## Risk classes

- **Read-only** — inspection and diagnostics.
- **Mutating** — changes files/configuration but is recoverable.
- **Privileged** — requires elevation or affects protected resources.
- **Destructive** — deletion, formatting, irreversible reset, destructive overwrite.

Apply stronger approval and verification as risk increases.

## Command construction

- Quote paths correctly.
- Avoid unsafe wildcard expansion.
- Prefer explicit identifiers.
- Use non-interactive flags only when behavior is understood.
- Avoid chaining many unrelated operations into one opaque command.

## Output handling

Capture:

- exit code
- stdout
- stderr
- timeout
- working directory
- relevant environment state

Do not equate exit code 0 with task completion when the command's effect still needs verification.

## Failure handling

Classify failures as syntax, missing dependency, permission, environment, timeout, transient external failure, or wrong hypothesis.

Do not repeatedly rerun the same failed command without changing the conditions.

## Verification

Examples:

- Service command → query service state.
- Package install → check installed version.
- File change → inspect resulting file.
- Network command → test the actual endpoint/workflow.

## Logging

Record command purpose and result, but redact credentials, secrets, tokens, and sensitive data.