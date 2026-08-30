# Hi, I'm Alaa Hamza 👋

[![Profile quality](https://github.com/Alaamo7/Alaamo7/actions/workflows/profile-quality.yml/badge.svg)](https://github.com/Alaamo7/Alaamo7/actions/workflows/profile-quality.yml)

**IT Technical Support professional · AI-assisted operations · LLM application engineering · Pine Script developer**

I build and document practical technical work across IT support, structured troubleshooting, AI-assisted workflows, hosted LLM applications, automation experiments, and TradingView/Pine Script development.

## Portfolio map

- 🛠️ [IT Support Lab](docs/it-support/README.md) — real troubleshooting evidence, runbook methodology, hardware/storage/firmware cases, and the roadmap toward Windows, networking, identity, automation, monitoring, and backup labs.
- 🤖 [AI Automation Lab](docs/ai-automation/README.md) — PromptBench AI, LLM evaluation, provider integration, local Ollama, agent-harness architecture, workflow verification, and automation roadmap.
- 🧪 [Pine Script validation toolkit](https://github.com/Alaamo7/pine-script-indicators) — 120 individually tested TradingView scripts with reports and screenshot evidence.
- 📈 [Curated Pine Script portfolio](https://github.com/Alaamo7/pine-script-portfolio) — smaller presentation-focused set of verified Pine Script v6 indicators.

## What I work on

- Windows troubleshooting, deployment, drivers, storage, firmware, and endpoint support
- Evidence-backed IT incident analysis and reusable troubleshooting documentation
- AI-assisted technical research, hypothesis structuring, documentation, and verification workflows
- Hosted AI application prototyping and Hugging Face Spaces deployment
- Prompt engineering, LLM evaluation, model/API integration, and local Ollama workflows
- Agent-harness and workflow-automation design with explicit verification and execution controls
- TradingView indicators and Pine Script v6 development/debugging
- EGX-focused technical-analysis dashboards and backtesting workflows

## Portfolio highlights

### 🛠️ IT Support Lab — evidence-backed troubleshooting

The [IT Support Lab](docs/it-support/README.md) is organized around inspectable evidence rather than a list of claimed skills.

**Current documented portfolio: 5 verified real-world cases.**

Selected cases include:

- Autodesk 3ds Max startup failure resolved by isolating and resetting a corrupted user profile
- Redragon USB flash recovery at the FirstChip controller/NAND-mapping level, verified with a full H2testw write/read test
- Kingston DataTraveler Read Only / Write Protection recovery using Phison controller analysis and controlled stop conditions
- HP Chromebook 14 G6 conversion to Windows through MrChrombox Full ROM UEFI, USB-PD troubleshooting, and Hardware-ID-based driver analysis
- The Sims 4 startup failure resolved by isolating a user-data version mismatch instead of performing an unnecessary full reinstall

The workflow is consistent: capture symptoms and evidence, build ranked hypotheses, choose the lowest-risk useful test, execute the repair or configuration change, verify the result, and record limitations.

AI is used as a **technical copilot** for research, hypothesis structuring, evidence organization, and documentation; repair execution and final validation are performed on the actual devices and systems.

[Open the IT Support Lab →](docs/it-support/README.md)

[Read the detailed IT + AI troubleshooting cases →](docs/it-ai-case-studies.md)

[Open the reusable case-study template →](docs/it-case-study-template.md)

### 🤖 PromptBench AI — LLM evaluation platform

**PromptBench AI** is a Gradio application for testing whether language models follow user instructions. It combines deterministic constraint checks with an LLM judge and supports single tests, batch benchmarking, analytics, local run history, exports, and same-case model comparison.

**Verified public evidence — 2026-08-30:**

- Dedicated public source repository with application code, tests, documentation, CI, and genuine interface screenshots
- Hugging Face Spaces deployment linked; the Space was observed in `Sleeping` state during the audit
- Gradio 6.25.0 interface and `app.py` entry point
- 50-case Arabic/English evaluation dataset
- 35 offline tests passed locally
- GitHub CI run #1 passed dependency validation, syntax validation, offline pytest, and Gitleaks
- No autonomous agent loop is claimed or present in the runtime code

The repository documents verified architecture, provider integrations, evaluation logic, environment configuration, secret handling, deployment, validation evidence, limitations, and open technical work.

[Open the GitHub repository →](https://github.com/Alaamo7/promptbench-ai)

[Open the live Hugging Face Space →](https://huggingface.co/spaces/3la2mo7/promptbench-ai)

[Review validation evidence →](https://github.com/Alaamo7/promptbench-ai/blob/main/docs/validation.md)

### ⚙️ AI Automation Lab — agent harnesses and workflow engineering

The [AI Automation Lab](docs/ai-automation/README.md) separates **verified implementation** from **planned portfolio evidence**.

The current anchor is PromptBench AI, which demonstrates LLM application engineering, model/provider integration, evaluation, testing, secret hygiene, CI, deployment documentation, and local Ollama support.

The next build targets are inspectable automation projects that explicitly document the harness components that really exist: context, memory, tools, skills, state, orchestration, verification, and execution controls. The goal is to avoid calling every LLM workflow an "agent" without evidence.

[Open the AI Automation Lab →](docs/ai-automation/README.md)

### 🧪 120-script TradingView validation project

In [`pine-script-indicators`](https://github.com/Alaamo7/pine-script-indicators), I maintain a structured collection of TradingView/Pine Script assets and validation evidence.

**Latest validation snapshot — 2026-08-22:**

- **120** Pine scripts tested individually on TradingView
- **120** scripts loaded and rendered successfully after repairing and re-testing five original compilation failures
- **5 / 5** originally failing scripts were repaired and re-tested successfully
- **7** strategies have Strategy Tester evidence and screenshots
- Each tested script has an adjacent test report and TradingView screenshot evidence

[Open the toolkit →](https://github.com/Alaamo7/pine-script-indicators)

[Read the engineering validation case study →](https://github.com/Alaamo7/pine-script-indicators/blob/main/docs/case-studies/2026-08-22-tradingview-validation.md)

### 📈 Curated Pine Script v6 portfolio

[`pine-script-portfolio`](https://github.com/Alaamo7/pine-script-portfolio) contains a smaller curated set of Pine Script v6 indicators selected for portfolio presentation, with compile checks, screenshots, verification notes, and repainting caveats.

[Open the curated portfolio →](https://github.com/Alaamo7/pine-script-portfolio)

## Engineering approach

I prefer evidence-backed technical work over unsupported claims. My workflow emphasizes:

- reproducible troubleshooting records,
- Hardware-ID/log/error-based diagnosis,
- risk-aware repair sequencing,
- explicit verification after remediation,
- source-preserving archives,
- validation evidence,
- known failures and limitations,
- secure secret handling,
- and maintainable technical documentation.

AI is used to improve research speed, organize evidence, compare hypotheses, and turn successful fixes into reusable knowledge. It does not replace hands-on verification.

A successful compile, backtest, repair, device recovery, or LLM evaluation is treated as evidence for the tested setup—not as a reason to overstate what was proven.

## Current focus

Building a stronger combined portfolio around **IT Technical Support + AI-assisted operations + hosted AI applications + workflow automation**, while continuing to improve validation evidence, documentation, maintainability, and security across the projects.

Current expansion priorities are:

1. Add independently testable Windows/networking/identity/PowerShell evidence to the IT Support Lab.
2. Add an inspectable AI-agent harness with explicit tools, state, verification, and execution controls.
3. Add a workflow-automation project with API integration, error handling, logs, and approval gates.
4. Keep PromptBench AI validation, security, and deployment evidence current.

## Repository guide

- [`promptbench-ai`](https://github.com/Alaamo7/promptbench-ai) — Gradio LLM-evaluation application with source, 50-case dataset, offline tests, security controls, CI, deployment documentation, and Hugging Face demo
- [`IT Support Lab`](docs/it-support/README.md) — practical IT Support portfolio area with verified troubleshooting evidence and a clearly separated lab roadmap
- [`AI Automation Lab`](docs/ai-automation/README.md) — LLM engineering and automation portfolio area with verified-vs-planned evidence boundaries
- [`IT + AI case studies`](docs/it-ai-case-studies.md) — real troubleshooting cases covering Windows applications, USB storage recovery, firmware/UEFI, drivers, and verification
- [`IT case-study template`](docs/it-case-study-template.md) — reusable structure for future evidence-backed troubleshooting cases
- [`pine-script-indicators`](https://github.com/Alaamo7/pine-script-indicators) — main technical-analysis toolkit, archive, documentation, and TradingView validation evidence
- [`pine-script-portfolio`](https://github.com/Alaamo7/pine-script-portfolio) — curated public portfolio of verified Pine Script v6 indicators
- [`pine-script-v6-course`](https://github.com/Alaamo7/pine-script-v6-course) — educational Pine Script project currently being validated and developed

---

> Trading and technical-analysis projects shown here are for education, research, and software demonstration. They are not financial advice or guarantees of future performance.
