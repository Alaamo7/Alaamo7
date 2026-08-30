# AI Agent Skills Portfolio

Reusable agent skills and workflow instructions designed for AI agents, agent harnesses, OpenClaw-style runtimes, GPT Work, and related automation systems.

## Status legend

- **Verified** — recovered from an existing saved `SKILL.md` in the working library.
- **Restored** — reconstructed from a previously designed skill package whose original archive is no longer directly available.
- **Restored from documented workflow/architecture** — rebuilt from previously documented procedures, incident workflows, or architecture notes; not presented as the byte-identical original skill file.
- **Manifest** — documented skill pack whose individual source files are not yet recovered in the current workspace.

## Skills

### Agent infrastructure & orchestration

- [`agent-orchestrator`](./agent-orchestrator/SKILL.md)
- [`skill-router`](./skill-router/SKILL.md)
- [`context-engineering`](./context-engineering/SKILL.md)
- [`memory-management`](./memory-management/SKILL.md)
- [`verification-agent`](./verification-agent/SKILL.md)
- [`model-router`](./model-router/SKILL.md)
- [`cost-control`](./cost-control/SKILL.md)
- [`harness-engineering`](./harness-engineering/SKILL.md)

### Tool engineering layer

- [`tool-design`](./tool-design/SKILL.md) — narrow tool purpose, permissions, failure modes, and verification.
- [`tool-contracts`](./tool-contracts/SKILL.md) — schemas, preconditions, postconditions, error taxonomy, and compatibility.
- [`api-integration`](./api-integration/SKILL.md) — authentication, API requests, pagination, rate limits, retries, and mutation verification.
- [`filesystem-operations`](./filesystem-operations/SKILL.md) — safe read/write/move/copy/delete operations with path controls and verification.
- [`terminal-execution`](./terminal-execution/SKILL.md) — command classification, environment checks, output capture, privilege boundaries, and verification.
- [`browser-automation`](./browser-automation/SKILL.md) — deterministic browser workflows with page-state checks, safe form handling, and confirmation gates.
- [`connector-routing`](./connector-routing/SKILL.md) — route work to the authoritative connected system based on data ownership and write-back semantics.
- [`data-validation`](./data-validation/SKILL.md) — schema, domain, completeness, consistency, provenance, and anomaly checks before actions.

### Observability, reliability & production operations

- [`agent-logging`](./agent-logging/SKILL.md)
- [`error-recovery`](./error-recovery/SKILL.md)
- [`retry-policy`](./retry-policy/SKILL.md)
- [`evaluation-framework`](./evaluation-framework/SKILL.md)
- [`agent-testing`](./agent-testing/SKILL.md)
- [`human-in-the-loop`](./human-in-the-loop/SKILL.md)
- [`secrets-management`](./secrets-management/SKILL.md)
- [`deployment-readiness`](./deployment-readiness/SKILL.md)

### Governance & security

- [`agent-security-permissions`](./agent-security-permissions/SKILL.md)
- [`secrets-management`](./secrets-management/SKILL.md)
- [`human-in-the-loop`](./human-in-the-loop/SKILL.md)
- [`verification-agent`](./verification-agent/SKILL.md)
- [`cost-control`](./cost-control/SKILL.md)

### IT operations & automation

- [`it-support`](./it-support/SKILL.md)
- [`network-diagnostics`](./network-diagnostics/SKILL.md)
- [`usb-repair`](./usb-repair/SKILL.md)
- [`windows-deployment`](./windows-deployment/SKILL.md)
- [`powershell-automation`](./powershell-automation/SKILL.md)
- [`knowledge-capture`](./knowledge-capture/SKILL.md)

### Development, research & repository QA

- [`pine-script-testing`](./pine-script-testing/SKILL.md)
- [`github-agent`](./github-agent/SKILL.md)
- [`ai-research`](./ai-research/SKILL.md)

### Content, learning & career systems

- [`presentation-design`](./presentation-design/SKILL.md) — Verified
- [`build-ats-resume`](./build-ats-resume/SKILL.md) — Verified
- [`youtube-to-course`](./youtube-to-course/SKILL.md)
- [`ai-video-creator`](./ai-video-creator/SKILL.md)
- [`job-agent`](./job-agent/SKILL.md)
- [`spark-image-first-presentation-pack`](./spark-image-first-presentation-pack/README.md) — Manifest

## Lifecycle architecture

```text
User Objective
    ↓
Harness Engineering
    ↓
Agent Orchestrator
    ↓
Skill Router + Model Router
    ↓
Context Engineering + Memory Management
    ↓
Security + Cost + Human Approval Gates
    ↓
Data Validation
    ↓
Tool / Connector Selection
    ├── API Integration
    ├── Filesystem Operations
    ├── Terminal Execution
    ├── Browser Automation
    └── Connected Services
    ↓
Tool Contract Enforcement
    ↓
Execution
    ↓
Agent Logging / Observability
    ↓
Verification Agent
    ↓
PASS ──────────────────────┐
  │                        │
FAIL                       │
  ↓                        │
Error Classification       │
  ↓                        │
Retry / Recovery           │
  ↓                        │
Human Review if needed     │
  ↓                        │
Re-verify ─────────────────┘
    ↓
Evaluation + Agent Testing
    ↓
Deployment Readiness
    ↓
Production
```

## Tool engineering principles

1. **Narrow contracts** — each tool should have a clear purpose and predictable semantics.
2. **Validated input** — malformed or incomplete critical data should fail before side effects occur.
3. **Structured output** — downstream agents should be able to distinguish success, conflict, validation errors, permission failures, and transient failures.
4. **Authoritative connector routing** — operate on the original source system when identity or write-back matters.
5. **Read before write** — inspect state before mutation where practical.
6. **Read-after-write verification** — check the actual resulting state instead of trusting a success response blindly.
7. **Least privilege** — tools receive only the permissions required for the current task.
8. **No secret propagation** — credentials stay in secret stores/runtime injection, not prompts, logs, or repositories.

## Core design principles

1. **Evidence before claims** — do not invent facts, qualifications, metrics, sources, technical findings, or outcomes.
2. **Tool-aware execution** — distinguish reasoning from actions performed by Files, Web, Terminal, GitHub, APIs, browsers, or document generators.
3. **Verification loops** — generation or a successful tool call is not completion; inspect the actual result against the objective.
4. **Least privilege** — use only the permissions needed for the current task.
5. **Minimum sufficient context** — retrieve only instructions, evidence, memory, and tool results that materially affect the task.
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
├── tool-engineering/
│   ├── tool-design/
│   ├── tool-contracts/
│   ├── api-integration/
│   ├── filesystem-operations/
│   ├── terminal-execution/
│   ├── browser-automation/
│   ├── connector-routing/
│   └── data-validation/
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
├── state/
├── policies/
├── evals/
└── logs/
```

## Compatibility

The files use Markdown-based `SKILL.md` instructions and can be adapted to agent runtimes that support reusable skills or system/task instruction modules. Tool names, schemas, permission models, model routing, memory persistence, state handling, observability, approval gates, and connector behavior should be mapped to the target runtime before execution.

## Security note

No API keys, tokens, passwords, private candidate data, customer data, or other secrets should be committed to this directory. Use environment variables or the target platform's secret manager for credentials. If a real secret is exposed in Git history, rotate/revoke it rather than relying only on deletion from the latest file version.

## Portfolio intent

This directory demonstrates reusable workflows and agent/harness engineering patterns rather than isolated prompts. The target is an auditable execution system covering architecture, routing, context, tool engineering, permissions, execution, observability, recovery, evaluation, human review, and production readiness.
