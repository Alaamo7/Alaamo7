---
name: model-router
status: restored-from-documented-architecture
description: Select an appropriate model for each task based on capability, reasoning needs, tool support, context size, latency, privacy, reliability, and cost while defining explicit fallback behavior.
---

# Model Router Skill

Choose models intentionally instead of using the same model for every task.

## Routing dimensions

Evaluate:

- Task complexity
- Required reasoning depth
- Coding capability
- Multimodal needs
- Tool-calling support
- Context-window requirement
- Latency target
- Reliability
- Privacy/deployment constraints
- Cost budget

## Workflow

```text
Task requirements
   ↓
Minimum capability threshold
   ↓
Candidate models
   ↓
Filter incompatible models
   ↓
Compare quality / latency / cost
   ↓
Select primary
   ↓
Define fallback
```

## Rules

1. Do not route solely by price.
2. Do not use a premium model for trivial tasks without reason.
3. Do not silently downgrade to a model that lacks required tool, modality, or reasoning capability.
4. Keep routing logic separate from provider marketing claims.
5. Revalidate model availability and pricing when they are time-sensitive.

## Suggested task classes

- **Class A — Lightweight:** extraction, formatting, simple classification.
- **Class B — General:** normal writing, summarization, routine tool workflows.
- **Class C — Advanced reasoning:** architecture, debugging, multi-source synthesis, consequential planning.
- **Class D — Specialized:** vision, long context, code execution, local/private inference, or other hard constraints.

## Fallback policy

A fallback must meet the minimum task requirements.

```yaml
primary_model: ""
minimum_capabilities: []
fallback_models: []
no_fallback_if_missing: []
routing_reason: ""
```

## Verification

If the fallback path materially changes expected quality or capability, mark it in the execution log rather than hiding the change.