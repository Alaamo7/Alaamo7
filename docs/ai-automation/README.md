# AI Automation Lab

A portfolio area for AI-assisted workflows, LLM application engineering, agent-harness concepts, workflow automation, provider integration, local models, validation, and technical documentation.

## Current anchor project

### PromptBench AI

[PromptBench AI](https://github.com/Alaamo7/promptbench-ai) is the current verified AI engineering project in this portfolio.

It provides evidence for:

- Gradio application development,
- prompt/instruction-following evaluation,
- deterministic validators,
- LLM-as-a-Judge scoring,
- Hugging Face Inference Provider integration,
- optional local Ollama integration,
- bilingual benchmark data,
- offline tests,
- CI and secret scanning,
- environment-variable-based secret handling,
- deployment documentation,
- and explicit limitation reporting.

Live deployment: [Hugging Face Space](https://huggingface.co/spaces/3la2mo7/promptbench-ai)

The project intentionally does **not** claim an autonomous agent loop when none is present in the runtime implementation.

## Engineering principles

The lab follows these rules:

1. **Verified implementation over tool-name lists.** A technology belongs in the portfolio only when there is a project, workflow, test, or documented artifact supporting the claim.
2. **Secrets stay outside source control.** API keys and credentials must use environment variables or provider secret stores.
3. **Automation needs verification.** A workflow is not considered complete because an LLM produced an answer; outputs require validation appropriate to the task.
4. **Model and provider boundaries are explicit.** Hosted APIs, local Ollama models, and orchestration layers should be documented separately.
5. **Human approval remains explicit for high-impact actions.** Automation should not hide where execution, review, or authorization happens.

## Portfolio capability map

| Area | Current evidence | Next evidence to build |
| --- | --- | --- |
| LLM application | PromptBench AI | Additional task-specific application |
| Model/API integration | Hugging Face + Ollama in PromptBench | Multi-provider routing example |
| Evaluation | Deterministic + LLM judge + benchmark dataset | Versioned evaluation datasets and regression gates |
| Testing | Offline pytest and CI | Bounded integration tests |
| Secret hygiene | `.env.example`, ignored secrets, Gitleaks | Credential-rotation runbook and reusable template |
| Agent harnesses | Research/documentation direction | Inspectable tool/memory/verification harness project |
| Workflow automation | Portfolio evidence still being assembled | n8n/API workflow with logs and validation |
| Local AI | Ollama backend support | Reproducible local deployment example |

Planned items are deliberately separated from verified implementation.

## Target architecture for future agent projects

```text
User / Trigger
     |
     v
Orchestrator
     |
     +--> Context / Memory
     +--> Skills / Policies
     +--> Model Router
     +--> Tools / APIs
     +--> State
     +--> Verification
     +--> Execution Controls
     |
     v
Auditable Result
```

The goal is not to call every LLM workflow an "agent". Future projects should document the actual harness components that exist: context, memory, tools, skills, state, orchestration, verification, and execution control.

## Next build targets

1. A small inspectable AI-agent harness with explicit tools, state, and verification.
2. A workflow-automation example with API calls, error handling, logs, and approval gates.
3. A multi-model routing example comparing hosted and local models.
4. Reusable security and evaluation templates for future AI projects.
5. Clear evidence for what was executed automatically versus manually reviewed.

The long-term target is a dedicated `Alaamo7/ai-automation-lab` repository once the lab contains enough runnable assets to stand independently from the profile repository.
