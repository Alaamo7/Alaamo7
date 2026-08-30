# AI Agent Skills Portfolio

Reusable agent skills and workflow instructions designed for AI agents, agent harnesses, OpenClaw-style runtimes, GPT Work, and related automation systems.

## Status legend

- **Verified** — recovered from an existing saved `SKILL.md` in the working library.
- **Restored** — reconstructed from previously designed workflows or architecture.
- **Restored from documented workflow/architecture** — rebuilt from prior documented procedures; not presented as the byte-identical original skill file.
- **Manifest** — documented skill pack whose individual source files are not yet recovered.

## Skill layers

### Agent infrastructure & orchestration
- [`agent-orchestrator`](./agent-orchestrator/SKILL.md)
- [`skill-router`](./skill-router/SKILL.md)
- [`context-engineering`](./context-engineering/SKILL.md)
- [`memory-management`](./memory-management/SKILL.md)
- [`verification-agent`](./verification-agent/SKILL.md)
- [`model-router`](./model-router/SKILL.md)
- [`cost-control`](./cost-control/SKILL.md)
- [`harness-engineering`](./harness-engineering/SKILL.md)

### Multi-agent coordination
- [`agent-role-design`](./agent-role-design/SKILL.md) — bounded responsibilities, capabilities, tools, authority, and escalation paths.
- [`agent-delegation`](./agent-delegation/SKILL.md) — structured subtask assignment with scoped context, permissions, and acceptance criteria.
- [`agent-handoff`](./agent-handoff/SKILL.md) — transfer verified progress, state, artifacts, side effects, blockers, and next actions.
- [`shared-state-coordination`](./shared-state-coordination/SKILL.md) — coordinate agents using ownership, revisions, conflict checks, and verified shared state.
- [`multi-agent-conflict-resolution`](./multi-agent-conflict-resolution/SKILL.md) — resolve disagreements by evidence, authority, freshness, ownership, and policy.
- [`supervisor-agent`](./supervisor-agent/SKILL.md) — decompose, delegate, supervise, verify, reconcile, and accept completion.
- [`worker-agent`](./worker-agent/SKILL.md) — execute bounded delegated work and return evidence-backed structured results.
- [`consensus-evaluation`](./consensus-evaluation/SKILL.md) — evidence-weighted review of multiple agent outputs without naive majority voting.

### Knowledge & retrieval
- [`rag-pipeline`](./rag-pipeline/SKILL.md) — end-to-end retrieval-augmented generation architecture.
- [`document-ingestion`](./document-ingestion/SKILL.md) — extraction, metadata, provenance, permissions, duplicate/version handling.
- [`chunking-strategy`](./chunking-strategy/SKILL.md) — structure-aware retrieval units with semantic coherence.
- [`retrieval-ranking`](./retrieval-ranking/SKILL.md) — relevance, authority, freshness, metadata filtering, deduplication, and reranking.
- [`source-grounding`](./source-grounding/SKILL.md) — map generated claims to supporting evidence and uncertainty.
- [`citation-management`](./citation-management/SKILL.md) — claim-to-source alignment and citation-drift prevention.
- [`knowledge-refresh`](./knowledge-refresh/SKILL.md) — incremental refresh, versioning, stale-content retirement, and retrieval verification.
- [`knowledge-quality-control`](./knowledge-quality-control/SKILL.md) — coverage, authority, freshness, extraction, retrieval, and unsupported-answer audits.

### State & workflow engineering
- [`task-state-management`](./task-state-management/SKILL.md)
- [`workflow-engine`](./workflow-engine/SKILL.md)
- [`dependency-management`](./dependency-management/SKILL.md)
- [`checkpointing`](./checkpointing/SKILL.md)
- [`resume-recovery`](./resume-recovery/SKILL.md)
- [`idempotency-control`](./idempotency-control/SKILL.md)
- [`concurrency-control`](./concurrency-control/SKILL.md)
- [`event-driven-agents`](./event-driven-agents/SKILL.md)

### Tool engineering
- [`tool-design`](./tool-design/SKILL.md)
- [`tool-contracts`](./tool-contracts/SKILL.md)
- [`api-integration`](./api-integration/SKILL.md)
- [`filesystem-operations`](./filesystem-operations/SKILL.md)
- [`terminal-execution`](./terminal-execution/SKILL.md)
- [`browser-automation`](./browser-automation/SKILL.md)
- [`connector-routing`](./connector-routing/SKILL.md)
- [`data-validation`](./data-validation/SKILL.md)

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

## Multi-agent coordination pattern

```text
Parent Objective
      ↓
Supervisor Agent
      ↓
Role Design + Delegation
      ↓
┌───────────────┬───────────────┬───────────────┐
│ Research      │ Execution     │ Specialist    │
│ Worker        │ Worker        │ Worker        │
└───────┬───────┴───────┬───────┴───────┬───────┘
        │               │               │
        └─────── Shared State ───────────┘
                        ↓
                    Handoffs
                        ↓
              Conflict Resolution
                        ↓
             Consensus / Verification
                        ↓
         PASS / REPAIR / REASSIGN / ESCALATE
```

## Multi-agent principles

1. **Roles are contracts** — responsibilities, tools, authority, inputs, outputs, and escalation paths are explicit.
2. **Delegate bounded work** — subtasks should be independently testable and have clear acceptance criteria.
3. **Structured handoffs** — transfer verified progress, side effects, IDs, artifacts, blockers, and next actions rather than entire transcripts.
4. **Shared state is versioned** — mutable coordination state uses ownership and revision checks to prevent stale writes.
5. **Resolve conflicts by evidence** — authoritative external state, direct tool results, freshness, and policy outweigh majority opinion.
6. **Supervisor owns integration** — workers own subtasks; the supervisor owns task-level reconciliation and acceptance.
7. **Workers stay in scope** — a worker does not silently broaden permissions or claim overall completion.
8. **Consensus is evidence-weighted** — agreement can improve confidence but does not replace verification.
9. **Multi-agent only when useful** — do not add agents when one agent with good skills/tools can complete the task reliably.

## Knowledge path

```text
Trusted Sources
    ↓
Document Ingestion
    ↓
Metadata + Provenance + Permissions
    ↓
Chunking Strategy
    ↓
Index / Retrieval
    ↓
Retrieval Ranking
    ↓
Minimum Sufficient Evidence
    ↓
Context Engineering
    ↓
Source-Grounded Generation
    ↓
Citation Management
    ↓
Verification Agent
    ↓
Answer

Knowledge Refresh ───────────────┐
Knowledge Quality Control ───────┴──→ continuously validate the corpus and retrieval path
```

## Lifecycle architecture

```text
Event / User Objective
        ↓
Supervisor / Orchestrator
        ↓
Workflow + Dependency Resolution
        ↓
Single-Agent or Multi-Agent Route?
        ├── Single agent → skill/model routing
        └── Multi-agent → role design → delegation → workers → handoffs
        ↓
Task State + Shared State + Checkpoints
        ↓
Knowledge Retrieval (when needed)
        ↓
Context + Memory
        ↓
Security + Cost + Human Gates
        ↓
Data Validation + Tool/Connector Selection
        ↓
Idempotency + Concurrency Controls
        ↓
Execution
        ↓
Logging + Persist State
        ↓
Conflict Resolution / Consensus (when multi-agent)
        ↓
Verification
        ↓
PASS / RETRY / RECOVER / REASSIGN / RESUME / ESCALATE
        ↓
Evaluation + Agent Testing
        ↓
Deployment Readiness
        ↓
Production / Event Loop
```

## Core design principles

- Evidence before claims.
- Verification after consequential actions.
- Least-privilege tools and connectors.
- Minimum sufficient context.
- Explicit workflow, task state, and shared state.
- Structured delegation and handoff.
- Idempotent and concurrency-safe side effects.
- Observability without secret leakage.
- Retry only after failure classification.
- Human review proportional to risk.
- Evaluation before production.
- Multi-agent complexity only when it creates measurable value.

## Suggested harness layout

```text
agent-harness/
├── orchestration/
│   ├── agent-orchestrator/
│   ├── supervisor-agent/
│   ├── skill-router/
│   └── model-router/
├── multi-agent/
│   ├── agent-role-design/
│   ├── agent-delegation/
│   ├── agent-handoff/
│   ├── shared-state-coordination/
│   ├── multi-agent-conflict-resolution/
│   ├── worker-agent/
│   └── consensus-evaluation/
├── workflow/
├── state/
├── context/
├── knowledge/
├── governance/
├── tool-engineering/
├── operations/
├── skills/
├── policies/
├── evals/
└── logs/
```

## Compatibility

The files use Markdown-based `SKILL.md` instructions and can be adapted to agent runtimes that support reusable skills or system/task instruction modules. Tool names, schemas, permission models, retrieval/index technology, model routing, memory persistence, shared-state storage, workflow engines, agent messaging, observability, approval gates, and connector behavior should be mapped to the target runtime before execution.

## Security note

No API keys, tokens, passwords, private candidate data, customer data, or other secrets should be committed here. Use runtime secret injection or a secret manager. Multi-agent systems should not copy secrets into shared state or handoff packets unless the storage and recipient permissions explicitly allow it.

## Portfolio intent

This directory demonstrates reusable AI agent and harness-engineering patterns rather than isolated prompts. The target is an auditable system covering architecture, routing, multi-agent coordination, knowledge retrieval, context, state/workflows, tool engineering, permissions, execution, observability, recovery, evaluation, human review, and production readiness.
