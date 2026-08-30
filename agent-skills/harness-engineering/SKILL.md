---
name: harness-engineering
status: restored-from-documented-architecture
description: Design and review AI agent harnesses that combine models, tools, skills, context, memory, orchestration, execution controls, verification loops, and security boundaries for reliable task execution.
---

# Harness Engineering Skill

Use this skill when designing an AI system that must do more than chat: select tools, load skills, manage context, maintain memory, execute actions, verify results, and recover from failures.

## Goal

Turn a foundation model into a controlled execution system:

```text
User Task
   ↓
Harness / Orchestrator
   ├── Model
   ├── Tools
   ├── Skills
   ├── Memory
   ├── Context Builder
   ├── State
   ├── Policies / Permissions
   ├── Verification
   └── Execution Control
```

## Core components

### 1. Model layer

Define:

- Primary model
- Fallback model(s)
- Reasoning requirements
- Context-window constraints
- Cost/latency trade-offs

Do not assume a larger model compensates for poor harness design.

### 2. Tool layer

Tools may include:

- Filesystem
- Terminal / PowerShell / Bash
- Web search
- GitHub
- APIs
- Databases
- Email/calendar
- Document generation

Each tool should have:

- Clear purpose
- Input/output contract
- Permission boundary
- Failure behavior
- Verification strategy

### 3. Skills layer

Skills are reusable domain-specific instructions.

Example layout:

```text
skills/
├── it-support/
├── usb-repair/
├── network-diagnostics/
├── pine-script-testing/
├── presentation-design/
├── job-agent/
└── ai-video-creator/
```

The harness should load only skills relevant to the current task.

### 4. Context engineering

Do not dump all available documents, memory, and skills into the model.

Use:

```text
Task
 ↓
Select relevant skills
 ↓
Select relevant files/data
 ↓
Select relevant memory
 ↓
Build bounded context
 ↓
Model execution
```

Context quality is more important than raw context size.

### 5. Memory

Separate:

- **Task state** — current execution state.
- **Working memory** — temporary observations/results.
- **Long-term memory** — stable project/user/environment facts.
- **Knowledge base** — documents/reference material.

Do not store secrets or transient noise in long-term memory.

### 6. State management

Track at minimum:

- Current objective
- Completed steps
- Pending steps
- Tool outputs
- Errors
- Retries
- Decisions
- Verification status

This prevents the agent from repeatedly starting from zero or falsely assuming an action succeeded.

### 7. Orchestration

Use explicit stages when the task is consequential:

```text
Plan
 ↓
Gather evidence
 ↓
Choose skill/tool
 ↓
Execute
 ↓
Inspect result
 ↓
Verify against objective
 ↓
Retry / repair / escalate
 ↓
Complete
```

Multi-agent designs should be used only when specialization, isolation, or parallel work creates clear value.

## Verification loop

Generation is not completion.

For any action:

```text
Expected result
     ↓
Execute tool/action
     ↓
Read actual result
     ↓
Compare actual vs expected
     ↓
PASS → continue
FAIL → diagnose / retry / escalate
```

Examples:

- File edit → reopen and inspect file.
- Code change → compile/test.
- GitHub write → fetch the repository path afterward.
- Network fix → test actual application connectivity.
- Resume export → verify text extraction and layout.

## Security model

Apply least privilege:

- Give the agent only the tools needed for the current task.
- Prefer read access before write access.
- Require stronger controls for deletion, email sending, access changes, secrets, firmware, or destructive disk operations.
- Keep API keys in environment variables or secret managers.
- Never hard-code credentials into skills, source code, logs, or repositories.

## Tool failure handling

When a tool fails:

1. Capture the exact error.
2. Determine whether failure is transient, input-related, permission-related, or capability-related.
3. Do not report success when execution did not occur.
4. Retry only when there is a reason the retry may succeed.
5. Escalate with evidence if blocked.

## Model fallback

Fallback should be explicit, not random.

Example:

```text
Primary model unavailable
  ↓
Check whether fallback meets task capability requirements
  ↓
Use fallback
  ↓
Mark execution path in logs
```

Never silently downgrade a task that requires capabilities the fallback lacks.

## Observability

Recommended execution log:

```markdown
# Agent Run
- Task ID:
- Objective:
- Model:
- Skills loaded:
- Tools used:
- Data sources:
- Actions:
- Verification results:
- Errors/retries:
- Final status:
```

## Harness review checklist

Evaluate:

- Is task routing clear?
- Are skills selected dynamically rather than all loaded at once?
- Are tool permissions minimal?
- Is context bounded and relevant?
- Is memory separated by purpose?
- Is execution state persistent enough?
- Does every consequential action have verification?
- Can the harness recover from partial failure?
- Are secrets excluded from prompts/logs/repos?
- Are human-review gates present where required?

## Anti-patterns

Avoid:

- One giant system prompt containing every workflow.
- Giving unrestricted tools to every task.
- Treating tool-call success as task success without checking output.
- Using memory as an unfiltered transcript archive.
- Adding multiple agents when a single agent with good skills is sufficient.
- Sending the entire knowledge base into every model request.

## Deliverables

Depending on the task, produce:

- Harness architecture
- Component map
- Skill-routing design
- Tool permission matrix
- Memory/context strategy
- Verification plan
- Failure/retry policy
- Security review
- Execution-state schema
- Implementation roadmap
