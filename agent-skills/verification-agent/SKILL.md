---
name: verification-agent
status: restored-from-documented-architecture
description: Independently verify whether an agent action or artifact satisfies expected results by inspecting real outputs, testing critical behavior, checking evidence, and refusing false completion claims.
---

# Verification Agent Skill

Verification is a separate step from generation and execution.

## Core principle

```text
Expected result
   ↓
Actual artifact / tool output
   ↓
Independent inspection
   ↓
Test critical behavior
   ↓
PASS / FAIL / PARTIAL / NOT VERIFIED
```

## Rules

1. Never verify from the executor's success message alone.
2. Inspect the actual target when possible.
3. Use objective success criteria defined before execution.
4. Test high-risk and failure-prone pathways first.
5. Report uncertainty explicitly.
6. A partial result is not a pass.

## Verification patterns

### File changes

- Reopen the file.
- Confirm expected content exists.
- Confirm unrelated content was not damaged.
- Validate syntax/format when relevant.

### GitHub

- Fetch repository path after writes.
- Confirm branch/path/content.
- Check status/tests when available.

### Code

- Compile/lint/test.
- Exercise relevant edge cases.
- Compare behavior against the intended logic.

### IT support

- Reproduce original workflow.
- Confirm symptom is gone.
- Check for side effects.

### Documents

- Confirm required sections/content.
- Check rendering and text extraction when relevant.

### External sends

- Verify recipient, content, attachment, and submission status using the tool result where available.

## Verification report

```markdown
# Verification Report
- Objective:
- Expected result:
- Evidence inspected:
- Tests performed:
- Observed result:
- Status: PASS / FAIL / PARTIAL / NOT VERIFIED
- Remaining risks:
- Required repair:
```

## Independence

When possible, verify using a different pathway from the action itself. Example: after a GitHub write action, perform a separate fetch/read rather than trusting the write response.

## Stop conditions

Return **NOT VERIFIED** when access or tooling does not allow inspection. Never replace missing verification with confidence language.