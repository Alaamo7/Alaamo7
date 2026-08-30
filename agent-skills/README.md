# AI Agent Skills Portfolio

Reusable agent skills and workflow instructions designed for AI agents, agent harnesses, OpenClaw-style runtimes, GPT Work, and related automation systems.

## Status legend

- **Verified** — recovered from an existing saved `SKILL.md` in the working library.
- **Restored** — reconstructed from a previously designed skill package whose original archive is no longer directly available.
- **Restored from documented workflow/architecture** — rebuilt from previously documented procedures, incident workflows, or architecture notes; not presented as the byte-identical original skill file.
- **Manifest** — documented skill pack whose individual source files are not yet recovered in the current workspace.

## Skills

| Skill | Status | Purpose |
|---|---|---|
| [`agent-orchestrator`](./agent-orchestrator/SKILL.md) | Restored from documented architecture | Decompose tasks, coordinate skills/tools, track dependencies/state, and enforce completion gates. |
| [`skill-router`](./skill-router/SKILL.md) | Restored from documented architecture | Select the minimum relevant skill set based on intent, domain, risk, tools, and dependencies. |
| [`context-engineering`](./context-engineering/SKILL.md) | Restored from documented architecture | Build bounded task context from instructions, sources, memory, and tool results without context overload. |
| [`memory-management`](./memory-management/SKILL.md) | Restored from documented architecture | Manage working memory, task state, long-term memory, and knowledge references with hygiene controls. |
| [`verification-agent`](./verification-agent/SKILL.md) | Restored from documented architecture | Independently verify actual outputs and prevent false completion claims. |
| [`model-router`](./model-router/SKILL.md) | Restored from documented architecture | Route tasks to suitable models based on capability, context, latency, privacy, reliability, and cost. |
| [`cost-control`](./cost-control/SKILL.md) | Restored from documented architecture | Control model/tool usage, retries, context size, and escalation without removing required quality checks. |
| [`harness-engineering`](./harness-engineering/SKILL.md) | Restored from documented architecture | Design agent harnesses with tools, skills, context, memory, state, orchestration, verification, and security controls. |
| [`agent-security-permissions`](./agent-security-permissions/SKILL.md) | Restored from documented principles | Design least-privilege permissions, secret handling, tool boundaries, action gates, and audit controls. |
| [`agent-logging`](./agent-logging/SKILL.md) | Restored | Create structured, secret-safe execution logs for tools, models, retries, approvals, verification, and run status. |
| [`error-recovery`](./error-recovery/SKILL.md) | Restored | Recover from tool, model, permission, validation, partial-execution, and dependency failures without false success. |
| [`retry-policy`](./retry-policy/SKILL.md) | Restored | Define safe retryability, backoff, attempt limits, duplicate prevention, and stop conditions. |
| [`evaluation-framework`](./evaluation-framework/SKILL.md) | Restored | Evaluate agents and harnesses with repeatable task suites, objective success gates, regression tracking, cost, and latency. |
| [`agent-testing`](./agent-testing/SKILL.md) | Restored | Test skills, tool integrations, workflows, regressions, failure paths, and end-to-end agent behavior. |
| [`human-in-the-loop`](./human-in-the-loop/SKILL.md) | Restored | Add risk-based human approval and review gates for ambiguous, irreversible, external, financial, or sensitive actions. |
| [`secrets-management`](./secrets-management/SKILL.md) | Restored | Protect API keys, tokens, and credentials using secret stores, runtime injection, redaction, rotation, and repository-safe handling. |
| [`deployment-readiness`](./deployment-readiness/SKILL.md) | Restored | Gate production deployment using functional, security, reliability, observability, cost, documentation, and rollback criteria. |
| [`github-agent`](./github-agent/SKILL.md) | Restored | Maintain repositories, files, issues, PRs, documentation, validation, and secret-aware GitHub workflows. |
| [`ai-research`](./ai-research/SKILL.md) | Restored | Perform source-aware technical research, contradiction handling, evidence synthesis, and practical recommendations. |
| [`it-support`](./it-support/SKILL.md) | Restored | Diagnose Windows endpoints, users, software, peripherals, connectivity, and common infrastructure incidents. |
| [`network-diagnostics`](./network-diagnostics/SKILL.md) | Restored | Layered TCP/IP, DHCP, DNS, Wi-Fi, routing, firewall, and application-connectivity troubleshooting. |
| [`usb-repair`](./usb-repair/SKILL.md) | Restored from documented workflow | Diagnose USB flash-drive failures and safely perform controller-level recovery when justified. |
| [`windows-deployment`](./windows-deployment/SKILL.md) | Restored | Standardize Windows installation, drivers, updates, software, validation, and endpoint handoff. |
| [`powershell-automation`](./powershell-automation/SKILL.md) | Restored | Build safer repeatable Windows automation with validation, logging, idempotency, and rollback awareness. |
| [`knowledge-capture`](./knowledge-capture/SKILL.md) | Restored | Turn incidents, troubleshooting, decisions, and research into reusable KB/SOP documentation. |
| [`pine-script-testing`](./pine-script-testing/SKILL.md) | Restored from documented workflow | Validate Pine Script v6 compilation, logic, inputs, state, repainting risk, visuals, and repository readiness. |
| [`build-ats-resume`](./build-ats-resume/SKILL.md) | Verified | Create, audit, rewrite, and tailor ATS-compatible resumes using verified candidate data. |
| [`presentation-design`](./presentation-design/SKILL.md) | Verified | Turn educational/technical content into structured, visual slide decks and slide plans. |
| [`youtube-to-course`](./youtube-to-course/SKILL.md) | Restored | Convert long-form video or playlist content into a structured course with lessons, exercises, quizzes, and a final project. |
| [`ai-video-creator`](./ai-video-creator/SKILL.md) | Restored | Convert an idea or lesson into a production-ready video workflow: script, storyboard, prompts, recording, and editing plan. |
| [`job-agent`](./job-agent/SKILL.md) | Restored | Search, evaluate, tailor, apply, and track job applications with evidence-first controls. |
| [`spark-image-first-presentation-pack`](./spark-image-first-presentation-pack/README.md) | Manifest | 12-skill presentation pipeline derived from reference-deck reverse engineering. |

## Lifecycle architecture

```text
Design
  ↓
Harness Engineering
  ↓
Orchestrate / Route
  ↓
Context + Memory + Security + Cost Controls
  ↓
Execute Skills / Tools
  ↓
Log + Observe
  ↓
Verify
  ↓
PASS ────────────────┐
  │                  │
FAIL                 │
  ↓                  │
Classify Error       │
  ↓                  │
Retry / Recover      │
  ↓                  │
Human Approval?      │
  ↓                  │
Re-verify ───────────┘
  ↓
Evaluate / Test
  ↓
Deployment Readiness
  ↓
Production
```

## Skill groups

### Agent infrastructure & orchestration

- `agent-orchestrator`
- `skill-router`
- `context-engineering`
- `memory-management`
- `verification-agent`
- `model-router`
- `cost-control`
- `harness-engineering`

### Observability, reliability & production operations

- `agent-logging`
- `error-recovery`
- `retry-policy`
- `evaluation-framework`
- `agent-testing`
- `human-in-the-loop`
- `deployment-readiness`

### Governance & security

- `agent-security-permissions`
- `secrets-management`
- `human-in-the-loop`
- `verification-agent`
- `cost-control`

### IT operations & automation

- `it-support`
- `network-diagnostics`
- `usb-repair`
- `windows-deployment`
- `powershell-automation`
- `knowledge-capture`

### Development, research & repository QA

- `pine-script-testing`
- `github-agent`
- `ai-research`
- `agent-testing`
- `evaluation-framework`

### Content, learning & career systems

- `presentation-design`
- `build-ats-resume`
- `youtube-to-course`
- `ai-video-creator`
- `job-agent`
- `spark-image-first-presentation-pack`

## Design principles

1. **Evidence before claims** — do not invent facts, qualifications, metrics, sources, technical findings, or outcomes.
2. **Tool-aware execution** — distinguish reasoning from actions performed by Files, Web, Terminal, GitHub, APIs, or document generators.
3. **Verification loops** — generation or a successful tool call is not completion; inspect the actual result against the objective.
4. **Least privilege** — use only the permissions needed for the current task.
5. **Minimum sufficient context** — retrieve only the instructions, evidence, memory, and tool results that materially affect the task.
6. **Skill routing** — load relevant skills dynamically instead of maintaining one giant universal prompt.
7. **Explicit state** — track objectives, completed work, blockers, errors, and verification status.
8. **Controlled destructive actions** — disk repair, profile replacement, permission changes, firmware operations, deletion, and external sends require stronger gates.
9. **Model/cost discipline** — match model capability and compute spend to the task without silently degrading required quality.
10. **Observability without secret leakage** — log actions, outcomes, failures, approvals, and verification while excluding secrets and hidden reasoning.
11. **Retry only when justified** — classify failures before retrying and inspect side effects before repeating writes or sends.
12. **Evaluation before production** — successful demos do not equal production readiness; require representative tests and failure-path coverage.
13. **Human review by risk** — use human approval where it materially reduces risk, not as a blanket gate for routine operations.
14. **Operational documentation** — reusable workflows should record environment, evidence, action, verification, and unresolved risk.

## Suggested harness layout

```text
agent-harness/
├── orchestration/
│   ├── agent-orchestrator/
│   ├── skill-router/
│   ├── model-router/
│   └── cost-control/
├── context/
│   ├── context-engineering/
│   └── memory-management/
├── governance/
│   ├── agent-security-permissions/
│   ├── secrets-management/
│   ├── human-in-the-loop/
│   └── verification-agent/
├── operations/
│   ├── agent-logging/
│   ├── error-recovery/
│   ├── retry-policy/
│   ├── evaluation-framework/
│   ├── agent-testing/
│   └── deployment-readiness/
├── skills/
│   ├── it-support/
│   ├── network-diagnostics/
│   ├── usb-repair/
│   ├── windows-deployment/
│   ├── powershell-automation/
│   ├── knowledge-capture/
│   ├── pine-script-testing/
│   ├── github-agent/
│   ├── ai-research/
│   ├── build-ats-resume/
│   ├── presentation-design/
│   ├── youtube-to-course/
│   ├── ai-video-creator/
│   └── job-agent/
├── tools/
├── state/
├── policies/
├── evals/
└── logs/
```

## Compatibility

The files use Markdown-based `SKILL.md` instructions and can be adapted to agent runtimes that support reusable skills or system/task instruction modules. Tool names, permissions, model routing, memory persistence, state handling, observability, approval gates, and connector behavior should be mapped to the target runtime before execution.

## Security note

No API keys, tokens, passwords, private candidate data, customer data, or other secrets should be committed to this directory. Use environment variables or the target platform's secret manager for credentials. If a real secret is exposed in Git history, rotate/revoke it rather than relying only on deletion from the latest file version.

## Portfolio intent

This directory demonstrates reusable workflows and agent/harness engineering patterns rather than isolated prompts. The target is an auditable execution system covering design, routing, context, permissions, execution, observability, recovery, evaluation, human review, and production readiness.