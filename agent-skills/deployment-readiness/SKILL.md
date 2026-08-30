---
name: deployment-readiness
status: restored
description: Assess whether an AI agent or harness is ready for production deployment by checking tests, permissions, secrets, observability, rollback, cost, failure handling, documentation, and release gates.
---

# Deployment Readiness Skill

## Goal

Prevent demo-quality agents from being mislabeled as production-ready.

## Release gates

### Functional

- Critical workflows pass end-to-end tests.
- Known critical/high defects are resolved or explicitly accepted.
- Verification checks validate observable outcomes.

### Security

- Tool permissions follow least privilege.
- Secrets are stored securely.
- Prompt-injection boundaries exist for untrusted content.
- High-risk actions have approval gates.

### Reliability

- Retry policy exists.
- Partial execution is detectable.
- Error recovery and escalation are defined.
- Duplicate side effects are controlled.

### Observability

- Runs have structured logs.
- Errors and verification results are visible.
- Model/tool usage and cost can be tracked.

### Cost & performance

- Model routing is appropriate.
- Expected cost per task is understood.
- Cost/latency limits are defined for production use.

### Operations

- Deployment configuration is documented.
- Rollback or disable procedure exists where practical.
- Ownership/escalation path is defined.
- Required dependencies and environment variables are documented.

## Readiness report

```markdown
# Deployment Readiness Review
- Agent/version:
- Target environment:
- Functional tests: PASS / FAIL
- Security review: PASS / FAIL
- Secrets review: PASS / FAIL
- Reliability/recovery: PASS / FAIL
- Observability: PASS / FAIL
- Cost controls: PASS / FAIL
- Human approval gates: PASS / FAIL
- Documentation: PASS / FAIL
- Rollback/disable path: PASS / FAIL

## Blocking issues
...

## Accepted risks
...

## Decision
READY / CONDITIONAL / NOT READY
```

## Rule

A successful prototype or several successful manual demonstrations are evidence of potential—not production readiness.