---
name: ai-research
status: restored
description: Conduct structured technical research using source evaluation, evidence synthesis, contradiction handling, uncertainty labeling, and practical recommendations without conflating search results with verified conclusions.
---

# AI Research Skill

Use this skill for deep technical research, vendor/model comparisons, architecture studies, tool evaluation, and knowledge synthesis.

## Core rules

1. Define the research question before gathering sources.
2. Prefer primary sources, official documentation, peer-reviewed work, and high-quality technical references.
3. Use fresh sources for rapidly changing products, APIs, pricing, models, and regulations.
4. Separate verified facts, interpretation, and uncertainty.
5. Do not treat search-result snippets as sufficient evidence when the underlying source is available.
6. Report contradictions instead of silently choosing the answer that best fits expectations.
7. Avoid unsupported claims about performance, safety, cost, or capability.

## Research workflow

```text
Define question
   ↓
Break into subquestions
   ↓
Set source-quality criteria
   ↓
Gather evidence
   ↓
Extract claims
   ↓
Cross-check important claims
   ↓
Resolve or document contradictions
   ↓
Synthesize findings
   ↓
Translate into practical implications
```

## Source hierarchy

Prefer, when available:

1. Official documentation / specifications
2. Peer-reviewed papers / standards
3. Official engineering blogs and changelogs
4. Reputable independent benchmarks or analysis
5. Community reports for experience-based insights

Community reports can be valuable for real-world behavior but should not replace primary evidence for hard specifications.

## Evidence table

For complex research maintain an internal structure like:

```text
Claim
Source
Publication/update date
Evidence strength
Contradicting source(s)
Confidence
Practical implication
```

## Comparing AI models or platforms

Compare only dimensions supported by evidence, such as:

- Model/API availability
- Context limits
- Tool/function calling
- Multimodal capabilities
- Pricing
- Rate limits
- Hosting/deployment model
- Licensing
- Data/privacy terms
- Benchmark evidence
- Latency or reliability evidence when available

Do not assume benchmark leadership automatically means best fit for a workflow.

## Architecture research

For topics such as agents or harnesses, separate:

- Definitions
- Components
- Competing terminology
- Reference architectures
- Research evidence
- Industry implementation patterns
- Security implications
- Operational trade-offs

## Contradictions

If two credible sources disagree:

1. Check dates and version scope.
2. Check whether they describe different configurations or definitions.
3. Prefer newer primary evidence when the underlying system changed.
4. If conflict remains, present both and lower confidence.

## Output structure

```markdown
# Research Question

## Executive Summary

## Scope and Definitions

## Key Findings
### Finding 1
- Evidence:
- Confidence:
- Implication:

## Contradictions / Uncertainty

## Practical Recommendations

## Open Questions
```

## Quality checklist

- Important claims are source-backed.
- Freshness is appropriate for the topic.
- Primary evidence was preferred where possible.
- Conflicting evidence is visible.
- Facts and interpretation are clearly separated.
- Recommendations follow from evidence rather than preference.
