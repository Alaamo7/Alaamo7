---
name: source-grounding
status: restored
description: Ground generated claims in retrieved evidence by mapping claims to sources, separating inference from fact, handling contradictions, and refusing unsupported certainty.
---

# Source Grounding Skill

Use this skill when an answer must be traceable to retrieved documents, web sources, connected systems, or other evidence.

## Grounding workflow

```text
Question
  ↓
Retrieve evidence
  ↓
Extract supported facts
  ↓
Identify uncertainty/conflict
  ↓
Generate claim
  ↓
Map claim to source evidence
  ↓
Verify support
  ↓
Publish with citation / uncertainty
```

## Rules

1. Every material factual claim should be supported by evidence when the task requires grounded output.
2. Do not stretch a source beyond what it actually states.
3. Separate direct source facts from derived conclusions.
4. Preserve contradictory evidence when relevant.
5. Mark missing evidence explicitly.
6. Do not convert weak retrieval confidence into strong prose certainty.

## Claim classes

- **Directly supported** — explicit in the source.
- **Derived** — reasonable inference from multiple supported facts.
- **Unverified** — plausible but insufficiently supported.
- **Contradicted** — evidence conflicts materially.

Only the first two should normally appear as affirmative claims, and derived claims should be labeled when useful.
