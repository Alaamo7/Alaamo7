---
name: evaluation-framework
status: restored
description: Evaluate AI agents, skills, and harnesses using repeatable task suites, objective success criteria, evidence-based scoring, regression tracking, and failure analysis.
---

# Agent Evaluation Framework Skill

## Goal

Measure whether an agent actually completes its intended work reliably—not whether the output merely sounds plausible.

## Evaluation dimensions

- Task completion
- Factual accuracy
- Tool-use correctness
- Verification quality
- Security/policy compliance
- Hallucination rate
- Recovery behavior
- Cost efficiency
- Latency
- User intervention required

## Test case format

```markdown
# Eval Case
- ID:
- Task:
- Initial state:
- Allowed tools:
- Expected artifacts/actions:
- Forbidden actions:
- Success criteria:
- Verification method:
- Max cost/time:
```

## Scoring

Prefer objective pass/fail gates where possible. Use graded scores only for dimensions that genuinely require judgment.

Example:

- Task completed: 0/1
- Correct target modified: 0/1
- Verification executed: 0/1
- No unsupported claim: 0/1
- No forbidden action: 0/1

## Evaluation suites

Maintain categories such as:

- Happy path
- Ambiguous input
- Missing data
- Tool failure
- Permission failure
- Partial execution
- Adversarial/injection content
- High-cost task
- Regression cases from past failures

## Regression tracking

Every important production failure should become a future eval case when safe and representative.

Track:

```text
Agent/skill version
Model/version
Eval suite version
Pass rate
Critical failures
Average cost
Average latency
```

## Human review

Use human grading for:

- Writing quality
- Visual quality
- Judgment-heavy research synthesis
- Ambiguous business decisions

Do not replace objective checks with subjective ratings when machine-verifiable criteria exist.

## Output

```markdown
# Evaluation Report
- Version under test:
- Test cases:
- Passed:
- Failed:
- Critical failures:
- Cost/latency summary:
- Regressions:
- Recommended fixes:
- Release decision: PASS / CONDITIONAL / FAIL
```
