---
name: context-engineering
status: restored-from-documented-architecture
description: Build bounded, task-relevant model context by selecting the right instructions, files, memory, tool results, and evidence while excluding stale, redundant, sensitive, or irrelevant information.
---

# Context Engineering Skill

Design the information package given to the model for a specific task.

## Objective

Provide enough context to execute correctly without flooding the model with unrelated data.

## Context layers

```text
System / policy constraints
        ↓
Task objective
        ↓
Relevant skill instructions
        ↓
Relevant source evidence
        ↓
Relevant project/user memory
        ↓
Recent tool outputs / state
        ↓
Expected output contract
```

## Selection rules

1. Include information only when it can materially affect the current task.
2. Prefer authoritative and current sources over repeated secondary summaries.
3. Exclude stale versions when a newer verified version exists.
4. Avoid duplicate chunks that say the same thing.
5. Keep secrets and unrelated personal data out of prompts.
6. Distinguish source evidence from agent-generated notes.
7. Preserve identifiers, paths, exact commands, and constraints when precision matters.

## Retrieval workflow

```text
Objective
 ↓
List required knowledge categories
 ↓
Retrieve candidates
 ↓
Rank by relevance + authority + freshness
 ↓
Remove duplicates / stale items
 ↓
Compress while preserving critical details
 ↓
Assemble context
 ↓
Check token budget and missing evidence
```

## Compression policy

Compress:

- Repeated explanations
- Long conversational history
- Irrelevant examples
- Decorative prose

Preserve:

- User constraints
- Exact technical values
- Error codes
- Source citations/identifiers
- Decisions already made
- Security boundaries
- Success criteria

## Context failure modes

Avoid:

- Loading an entire knowledge base for a narrow question.
- Mixing multiple conflicting versions without marking the conflict.
- Summarizing away a critical parameter.
- Including irrelevant sensitive user data.
- Treating generated notes as verified source material.

## Output contract

```yaml
objective: ""
critical_constraints: []
skills: []
source_evidence: []
relevant_memory: []
recent_tool_results: []
excluded_context: []
known_gaps: []
```

## Quality check

Before handing context to the model, ask:

- Does every included item help solve this task?
- Is anything critical missing?
- Is any information stale or contradictory?
- Are facts distinguishable from hypotheses?
- Is the context small enough to reason over reliably?