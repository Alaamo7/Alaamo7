---
name: memory-management
status: restored-from-documented-architecture
description: Manage agent working memory, task state, long-term memory, and knowledge-base references while preventing stale, sensitive, contradictory, or low-value information from polluting future execution.
---

# Memory Management Skill

Treat memory as a controlled data layer, not a transcript dump.

## Memory classes

- **Task state** — what is happening now.
- **Working memory** — temporary observations and intermediate results.
- **Long-term memory** — stable facts or preferences that materially improve future execution.
- **Knowledge base** — documents, SOPs, reports, and reference material.

## Write policy

Store long-term memory only when information is:

- Stable enough to remain useful.
- Relevant to future tasks.
- Supported by the user's own information or authorized sources.
- Appropriate to retain.

Do not store:

- Passwords, API keys, tokens, recovery codes.
- Temporary error noise.
- Unverified guesses.
- Sensitive personal data unless the platform and task explicitly support appropriate retention.
- Entire conversation transcripts merely because they exist.

## Lifecycle

```text
Observation
 ↓
Classify memory type
 ↓
Assess stability + relevance + sensitivity
 ↓
Store / keep temporary / discard
 ↓
Retrieve only when task-relevant
 ↓
Revalidate if potentially stale
```

## Conflict handling

If new evidence conflicts with stored memory:

1. Do not silently choose one.
2. Prefer the newer verified source when appropriate.
3. Preserve uncertainty if neither source is authoritative.
4. Update or invalidate stale memory once resolved.

## Retrieval rules

- Retrieve narrowly by task.
- Prefer exact project/entity matches.
- Avoid injecting unrelated profile information.
- Recheck time-sensitive memories before consequential decisions.

## Suggested record

```yaml
key: ""
value: ""
source: ""
confidence: verified | inferred
created_at: ""
last_verified_at: ""
expiry_or_review: ""
scope: user | project | environment | task
sensitivity: low | restricted
```

## Memory hygiene review

Periodically identify:

- Duplicate entries
- Stale technical versions
- Contradictory facts
- Low-value transient notes
- Sensitive data that should not remain

The goal is high-signal memory, not maximum retention.