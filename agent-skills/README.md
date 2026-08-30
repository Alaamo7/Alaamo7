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
Orchestrator + Workflow Engine
        ↓
Dependency / Skill / Model Routing
        ↓
Task State + Checkpoints
        ↓
Knowledge Retrieval (when needed)
        ├── Ingest / Chunk / Index
        ├── Retrieve / Rank
        └── Ground / Cite
        ↓
Context + Memory
        ↓
Security + Cost + Human Gates
        ↓
Data Validation
        ↓
Tool / Connector Selection
        ↓
Tool Contract Enforcement
        ↓
Idempotency + Concurrency Controls
        ↓
Execution
        ↓
Logging + Persist State
        ↓
Verification
        ↓
PASS / RETRY / RECOVER / RESUME / ESCALATE
        ↓
Evaluation + Agent Testing
        ↓
Deployment Readiness
        ↓
Production / Event Loop
```

## Knowledge & retrieval principles

1. **Provenance survives ingestion** — source identity, version, location, and access metadata remain attached to retrieved content.
2. **Structure-aware chunking** — retrieval units should preserve semantic and document boundaries rather than rely only on fixed character counts.
3. **Ranking is multi-factor** — semantic relevance, exact match, authority, freshness, metadata, duplication, and permissions all matter.
4. **Minimum sufficient evidence** — do not overload the context with weak or duplicate chunks.
5. **Ground claims, not just answers** — material claims should map to supporting evidence.
6. **Citation integrity** — verify citations after edits to prevent citation drift.
7. **Freshness is explicit** — changed or stale sources should trigger refresh or qualification.
8. **Quality is measurable** — test retrieval with representative questions and audit unsupported-answer risk.

## Core design principles

- Evidence before claims.
- Verification after consequential actions.
- Least-privilege tools and connectors.
- Minimum sufficient context.
- Explicit workflow and task state.
- Idempotent and concurrency-safe side effects.
- Observability without secret leakage.
- Retry only after failure classification.
- Human review proportional to risk.
- Evaluation before production.

## Suggested harness layout

```text
agent-harness/
├── orchestration/
├── workflow/
├── state/
├── context/
├── knowledge/
│   ├── rag-pipeline/
│   ├── document-ingestion/
│   ├── chunking-strategy/
│   ├── retrieval-ranking/
│   ├── source-grounding/
│   ├── citation-management/
│   ├── knowledge-refresh/
│   └── knowledge-quality-control/
├── governance/
├── tool-engineering/
├── operations/
├── skills/
├── policies/
├── evals/
└── logs/
```

## Compatibility

The files use Markdown-based `SKILL.md` instructions and can be adapted to agent runtimes that support reusable skills or system/task instruction modules. Tool names, schemas, permission models, retrieval/index technology, model routing, memory persistence, state handling, workflow engines, observability, approval gates, and connector behavior should be mapped to the target runtime before execution.

## Security note

No API keys, tokens, passwords, private candidate data, customer data, or other secrets should be committed here. Use runtime secret injection or a secret manager. Retrieval permissions must respect source-system access boundaries; indexing content does not make it public.

## Portfolio intent

This directory demonstrates reusable AI agent and harness-engineering patterns rather than isolated prompts. The target is an auditable system covering architecture, routing, knowledge retrieval, context, state/workflows, tool engineering, permissions, execution, observability, recovery, evaluation, human review, and production readiness.
