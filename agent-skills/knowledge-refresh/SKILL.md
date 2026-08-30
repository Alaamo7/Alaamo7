---
name: knowledge-refresh
status: restored
description: Keep an AI knowledge base current by detecting stale sources, re-ingesting changed content, versioning updates, retiring superseded material, and validating index freshness.
---

# Knowledge Refresh Skill

Use this skill to maintain freshness in a knowledge base whose source content can change.

## Workflow

```text
Inventory sources
  ↓
Check last-seen version/update time
  ↓
Detect changed/new/removed content
  ↓
Re-ingest affected items
  ↓
Re-chunk/re-index as needed
  ↓
Retire superseded versions
  ↓
Validate retrieval freshness
  ↓
Record refresh status
```

## Rules

1. Do not rebuild an entire corpus when only a small subset changed unless the indexing architecture requires it.
2. Preserve version history when useful for auditability.
3. Mark stale or unavailable sources instead of silently serving them as current.
4. Validate that new content is retrievable after refresh.
5. Remove or quarantine superseded content when it can mislead retrieval.

## Refresh triggers

Possible triggers:

- Source modified timestamp
- Content hash change
- New document/version
- Scheduled refresh
- Manual invalidation
- Upstream webhook/event

## Output

Record changed items, ingestion result, index update result, stale/failed sources, and retrieval verification.