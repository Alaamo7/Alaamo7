---
name: knowledge-quality-control
status: restored
description: Evaluate knowledge-base quality across coverage, authority, freshness, duplication, extraction integrity, metadata completeness, retrieval performance, and unsupported-answer risk.
---

# Knowledge Quality Control Skill

Use this skill to audit whether a knowledge base is suitable for reliable agent retrieval.

## Quality dimensions

Evaluate:

- Coverage
- Source authority
- Freshness
- Extraction integrity
- Metadata completeness
- Duplicate rate
- Version conflicts
- Chunk coherence
- Retrieval precision
- Retrieval recall on representative questions
- Citation traceability
- Unsupported-answer rate

## Audit workflow

```text
Define representative questions
  ↓
Inspect source inventory
  ↓
Check freshness and authority
  ↓
Sample extraction/chunks
  ↓
Run retrieval tests
  ↓
Inspect grounded answers
  ↓
Classify defects
  ↓
Prioritize remediation
```

## Defect classes

- Missing source
- Stale source
- Low-authority source dominating results
- Broken extraction
- Duplicate/superseded content
- Poor chunk boundary
- Wrong ranking
- Missing metadata
- Citation mismatch
- Hallucinated/unsupported answer

## Output

Produce a quality report with severity, evidence, affected source/query, remediation, and verification status.

A knowledge base should not be labeled production-ready solely because documents were indexed successfully.