---
name: retrieval-ranking
status: restored
description: Rank and filter retrieved knowledge using relevance, authority, freshness, metadata, duplication, and query intent instead of raw similarity alone.
---

# Retrieval Ranking Skill

Use this skill after initial retrieval to decide which evidence should actually enter the model context.

## Ranking factors

Evaluate candidates by:

- Semantic relevance
- Keyword/exact-match relevance
- Source authority
- Freshness
- Metadata fit
- User/task scope
- Duplicate overlap
- Access permissions
- Citation usefulness

## Workflow

```text
Initial candidates
  ↓
Remove inaccessible/invalid items
  ↓
Deduplicate
  ↓
Apply metadata filters
  ↓
Score relevance + authority + freshness
  ↓
Rerank
  ↓
Select minimum sufficient evidence
```

## Rules

1. High similarity does not override a clearly more authoritative source.
2. Freshness matters when the underlying fact can change.
3. Avoid filling the context window with near-duplicate chunks.
4. Keep contradictory evidence when it materially affects the answer.
5. If ranking confidence is weak, retrieve more evidence instead of forcing a confident answer.
