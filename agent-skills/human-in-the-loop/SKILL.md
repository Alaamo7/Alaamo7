---
name: human-in-the-loop
status: restored
description: Define human review and approval checkpoints for AI agent workflows where ambiguity, irreversible actions, external communications, financial/security impact, or policy risk make autonomous execution inappropriate.
---

# Human-in-the-Loop Skill

## Goal

Use human review where it meaningfully reduces risk without forcing unnecessary approval for routine low-risk work.

## Approval triggers

Require explicit human approval before actions such as:

- Sending consequential external messages
- Deleting or overwriting important data
- Changing permissions or access controls
- Firmware or low-level disk operations
- Production deployment
- Financially consequential actions
- Publishing sensitive or reputation-impacting content
- Acting when critical ambiguity remains

## Review modes

### Pre-action approval

Use before irreversible or high-impact actions.

### Mid-workflow review

Use when the agent can complete safe preparation autonomously but needs approval to proceed.

### Post-action audit

Use for low-risk actions where immediate execution is acceptable but traceability still matters.

## Approval packet

Present only what the reviewer needs:

```markdown
# Approval Request
- Objective:
- Proposed action:
- Target:
- Why this action is needed:
- Expected effect:
- Material risks:
- Reversibility:
- Evidence reviewed:
- Alternatives:
```

## Rules

1. Do not ask for approval when the user already explicitly authorized the exact action and no new material risk appeared.
2. Do not hide uncertainty to avoid human review.
3. Do not overload reviewers with raw logs when a concise evidence summary is sufficient.
4. Record approval identity/reference and approved scope when the platform supports it.
5. If the approved scope changes materially, request approval again.

## Automation principle

Human-in-the-loop should be risk-based, not a blanket requirement for every step.