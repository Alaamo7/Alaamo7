---
name: multi-agent-conflict-resolution
status: restored-from-documented-architecture
description: Resolve disagreements between agents by comparing evidence quality, source authority, state freshness, scope ownership, policy constraints, and verification results instead of averaging answers blindly.
---

# Multi-Agent Conflict Resolution

Use this skill when agents produce contradictory recommendations, facts, state updates, or execution plans.

## Conflict classes

- Evidence conflict
- State-version conflict
- Scope/ownership conflict
- Policy conflict
- Tool-result conflict
- Interpretation conflict
- Plan/priority conflict

## Resolution hierarchy

Prefer, in order when relevant:

1. Current authoritative external state
2. Direct tool output / primary source
3. Verified artifact
4. Fresher state revision
5. Domain-specific trusted source
6. Explicit policy/permission rule
7. Agent inference

## Rules

1. Do not choose by majority alone.
2. Do not merge incompatible facts into a false compromise.
3. Ask which claim is better supported and more current.
4. Preserve unresolved uncertainty when evidence is insufficient.
5. Escalate policy, ownership, or high-risk ambiguity to supervisor/human review.

## Output

```markdown
# Conflict Resolution
- Conflict type:
- Agent A claim:
- Agent B claim:
- Evidence A:
- Evidence B:
- Authority/freshness comparison:
- Decision:
- Confidence:
- Remaining uncertainty:
- Required verification:
```