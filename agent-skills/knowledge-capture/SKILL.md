---
name: knowledge-capture
status: restored
description: Convert troubleshooting sessions, project decisions, research findings, conversations, and recurring workflows into structured reusable documentation or knowledge-base entries with clear evidence, steps, outcomes, and follow-up actions.
---

# Knowledge Capture Skill

Use this skill to turn raw work into reusable operational knowledge rather than leaving useful fixes buried in chat history.

## Core rules

1. Preserve facts and separate them from inference.
2. Record the actual symptom, cause, action, and verification—not only the final fix.
3. Remove secrets and unnecessary personal data before publishing or sharing.
4. Prefer concise reusable procedures over transcript-like notes.
5. Mark unresolved or uncertain root causes explicitly.
6. Link related incidents, repositories, files, or issues when available.

## Supported outputs

- Troubleshooting KB article
- Incident postmortem
- How-to guide
- Decision record
- Research note
- Lessons learned
- SOP
- FAQ
- Project knowledge page

## Troubleshooting article structure

```markdown
# Issue Title

## Environment
- Device / OS / application:
- Relevant versions:

## Symptoms
- Exact user-visible behavior:
- Error code/message:

## Scope
- One user/device or multiple?

## Diagnosis
- Evidence collected:
- Tests performed:
- Findings:

## Root cause
Verified / suspected / unresolved

## Resolution
Step-by-step actions.

## Verification
How success was confirmed.

## Prevention / Notes
What to check next time.
```

## Decision record

```markdown
# Decision

## Context
Why a decision was required.

## Options considered
1. ...
2. ...

## Decision
What was selected.

## Rationale
Why it was selected.

## Trade-offs
What is gained and lost.

## Review trigger
When this decision should be reconsidered.
```

## Research capture

For research notes, separate:

- Question
- Sources
- Verified findings
- Interpretations
- Open questions
- Practical implications

Do not blur source evidence with the agent's own conclusions.

## Deduplication

Before creating a new KB article, check whether a closely related article already exists. Prefer updating or linking to an existing entry when appropriate.

## Quality checklist

- Title describes the actual issue/topic.
- Environment and versions are captured when relevant.
- Exact errors are preserved.
- Steps are reproducible.
- Destructive steps carry warnings.
- Final state was verified.
- Secrets/private data are removed.
- Unknowns are not presented as facts.
