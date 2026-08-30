---
name: agent-handoff
status: restored-from-documented-architecture
description: Transfer work between agents using structured handoff packets that preserve objective, state, evidence, decisions, artifacts, unresolved risks, and next actions.
---

# Agent Handoff

A handoff should preserve enough trusted state for the next agent to continue without restarting or guessing.

## Handoff packet

Include:

- Parent objective
- Current subtask
- Completed steps
- Verified results
- Artifacts/links/IDs
- Tool side effects already performed
- Decisions and rationale summary
- Open questions
- Blockers
- Risks
- Required next action
- Acceptance criteria

## Rules

1. Never hand off hidden assumptions as facts.
2. Distinguish verified state from hypotheses.
3. Record irreversible/external actions explicitly.
4. Include identifiers required to continue safely.
5. Receiving agent must validate critical external state before repeating writes or sends.

## Handoff states

- `READY` — enough verified context to continue.
- `BLOCKED` — dependency or permission is missing.
- `REVIEW_REQUIRED` — human/supervisor decision needed.
- `FAILED` — subtask cannot continue under current constraints.

## Template

```markdown
# Agent Handoff
- Objective:
- From role:
- To role:
- Status:
- Completed:
- Verified evidence:
- Side effects:
- Artifacts/IDs:
- Open issues:
- Next action:
- Acceptance criteria:
```
