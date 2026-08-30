---
name: skill-router
status: restored-from-documented-architecture
description: Select the minimum relevant set of reusable agent skills for a task based on intent, domain, risk, required tools, and dependencies while avoiding context overload and incompatible skill combinations.
---

# Skill Router

Route each task to the smallest relevant skill set.

## Inputs

- User objective
- Domain
- Required action type
- Risk level
- Available tools
- Available skills
- Existing state/context

## Routing process

```text
Task
 ↓
Extract intent + domain
 ↓
Detect risk / destructive actions
 ↓
Match candidate skills
 ↓
Resolve overlap and dependencies
 ↓
Load minimum sufficient skills
 ↓
Return route + rationale
```

## Rules

1. Do not load every skill by default.
2. Prefer one primary skill plus supporting skills.
3. Load governance/security skills when the task includes external sends, credentials, deletions, firmware, permissions, or destructive storage actions.
4. Load verification skill whenever execution must be checked against an expected result.
5. Avoid duplicate skills that solve the same layer unless comparison is explicitly needed.
6. If no skill fits, fall back to general reasoning and flag the coverage gap.

## Example routes

### IT incident

```text
Primary: it-support
Supporting: network-diagnostics (if connectivity-related)
Supporting: knowledge-capture (after resolution)
Governance: agent-security-permissions (if admin credentials/actions are required)
```

### Pine Script repository fix

```text
Primary: pine-script-testing
Supporting: github-agent
Supporting: verification-agent
```

### Job application

```text
Primary: job-agent
Supporting: build-ats-resume
Governance: agent-security-permissions
```

## Route output

```yaml
primary_skill: ""
supporting_skills: []
excluded_skills: []
risk_controls: []
required_tools: []
reason: ""
```

## Context budget

If many skills appear relevant, prioritize:

1. Safety/governance constraints
2. Primary domain skill
3. Verification
4. Optional supporting skills

Context quality beats skill quantity.