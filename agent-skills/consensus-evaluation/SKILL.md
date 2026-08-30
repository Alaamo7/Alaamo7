---
name: consensus-evaluation
status: restored-from-documented-architecture
description: Evaluate multiple agent outputs using evidence-weighted comparison, independent scoring, disagreement analysis, and verification instead of naive majority voting.
---

# Consensus Evaluation

Use multiple agents as independent reviewers when diversity of reasoning can improve reliability, but do not confuse agreement with truth.

## Appropriate uses

- Independent code/research reviews
- Competing implementation plans
- Risk assessments
- Ambiguous classification
- Quality scoring
- High-impact synthesis where one model may miss issues

## Method

1. Define common task and rubric.
2. Obtain independent outputs before cross-exposure when independence matters.
3. Extract claims, recommendations, evidence, and uncertainty.
4. Score each output against the rubric.
5. Identify areas of agreement and disagreement.
6. Resolve disagreements using authoritative evidence or direct verification.
7. Produce a final synthesis with confidence and unresolved uncertainty.

## Do not

- Treat 2-of-3 agreement as automatically correct.
- Reward verbosity instead of evidence.
- Allow one agent to contaminate all reviewers before independent evaluation.
- Average mutually exclusive factual claims.

## Evaluation dimensions

- Correctness
- Evidence quality
- Source authority
- Freshness
- Requirement coverage
- Risk awareness
- Reproducibility
- Verification status

## Output

```markdown
# Consensus Evaluation
- Task:
- Reviewers:
- Common rubric:
- Agreement areas:
- Disagreements:
- Evidence comparison:
- Verification performed:
- Selected/synthesized result:
- Confidence:
- Unresolved issues:
```