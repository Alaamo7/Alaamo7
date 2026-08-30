---
name: agent-role-design
status: restored-from-documented-architecture
description: Design clear agent roles with bounded responsibilities, required capabilities, tool permissions, inputs, outputs, escalation paths, and success criteria for multi-agent systems.
---

# Agent Role Design

Design specialized agents so responsibilities are explicit and overlap is minimized.

## Role contract

Every agent role should define:

- Objective
- Scope
- Required capabilities
- Allowed tools
- Required inputs
- Expected outputs
- Data ownership
- Decision authority
- Escalation conditions
- Verification requirements

## Rules

1. Prefer narrow roles over vague universal agents.
2. Avoid duplicated ownership of the same mutable resource.
3. Give each role the minimum tool access needed.
4. Separate execution roles from approval/verification roles when risk justifies it.
5. Define what the agent must not do.

## Example

```text
Supervisor Agent
- Owns task decomposition and acceptance
- Does not perform every low-level action

Research Worker
- Collects and synthesizes evidence
- Cannot mutate external systems

Execution Worker
- Performs approved tool actions
- Must return structured results

Verification Agent
- Independently checks outputs
- Cannot silently alter the target result
```

## Deliverable

Produce a role matrix with role, responsibility, tools, permissions, inputs, outputs, and escalation rules.