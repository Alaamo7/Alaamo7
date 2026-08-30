---
name: cost-control
status: restored-from-documented-architecture
description: Control AI-agent operating cost by budgeting model usage, context size, tool calls, retries, batch execution, caching, and escalation while preserving minimum quality and verification requirements.
---

# Agent Cost Control Skill

Optimize cost without breaking reliability.

## Cost drivers

Track:

- Input tokens
- Output tokens
- Model/provider pricing
- Number of model calls
- Tool/API charges
- Search/retrieval calls
- Retries
- Parallel agents
- Generated media/document costs
- Storage/logging where material

## Core workflow

```text
Task
 ↓
Define minimum quality/capability
 ↓
Estimate expensive stages
 ↓
Choose efficient model/tool path
 ↓
Set call/retry budgets
 ↓
Execute + meter usage
 ↓
Escalate only when justified
 ↓
Report cost-sensitive decisions
```

## Rules

1. Never sacrifice required verification merely to reduce cost.
2. Use cheaper models for low-risk preprocessing when they meet the capability requirement.
3. Reserve stronger models for stages where reasoning quality materially affects outcomes.
4. Reduce irrelevant context before switching to a larger context window.
5. Batch compatible operations when doing so preserves traceability.
6. Avoid repeated searches/tool calls when a valid result is already available.
7. Retry only when the error is plausibly recoverable.

## Budget policy

Suggested controls:

```yaml
max_model_calls: null
max_retries_per_stage: 2
max_parallel_agents: null
max_context_tokens: null
preferred_cost_tier: balanced
verification_required: true
```

## Escalation model

Example:

```text
Lightweight model
   ↓ if confidence/evidence insufficient
General model
   ↓ if advanced reasoning required
Advanced model
```

Do not escalate based only on stylistic preference.

## Cost report

```markdown
# Agent Cost Report
- Task:
- Models used:
- Major tool/API calls:
- Retries:
- Cost-saving decisions:
- Quality safeguards preserved:
- Estimated/actual cost: [only when reliable data exists]
```

## Anti-patterns

Avoid:

- Sending the full conversation to every call.
- Running multiple agents that duplicate the same reasoning.
- Re-retrieving unchanged sources.
- Using the most expensive model as a universal default.
- Hiding quality degradation caused by cost constraints.

Cost optimization means better allocation of compute—not simply fewer tokens.