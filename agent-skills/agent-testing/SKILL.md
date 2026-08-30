---
name: agent-testing
status: restored
description: Test AI agents and skills across unit-like skill tests, integration tests, tool-use flows, regression cases, and end-to-end scenarios before production deployment.
---

# Agent Testing Skill

## Test layers

### 1. Skill-level tests

Verify each skill:

- Triggers on the intended task
- Avoids triggering on unrelated tasks
- Produces the expected structure
- Respects safety and evidence rules
- Handles missing information correctly

### 2. Tool integration tests

Verify:

- Correct tool selected
- Correct arguments prepared
- Permission boundaries respected
- Tool result actually read
- Failed calls handled correctly

### 3. Workflow tests

Test multi-step flows such as:

```text
Discover → Plan → Execute → Verify → Document
```

Check state continuity between steps.

### 4. End-to-end tests

Use realistic tasks with real or controlled sandbox targets. Validate the final observable result, not just intermediate text.

## Required test categories

- Happy path
- Missing input
- Ambiguous input
- Permission denial
- Tool timeout/failure
- Partial success
- Duplicate action prevention
- Prompt injection in retrieved content
- Cost/latency threshold
- Human approval gate

## Test record

```markdown
# Agent Test
- Test ID:
- Agent/skill version:
- Input:
- Initial state:
- Expected behavior:
- Tools expected:
- Forbidden behavior:
- Actual result:
- Verification:
- Status: PASS / FAIL
- Notes:
```

## Regression rule

Every fixed meaningful bug should receive a regression test when practical.

## Production gate

Do not label an agent production-ready merely because several demos succeeded. Require representative tests, failure-path coverage, and verification of consequential actions.