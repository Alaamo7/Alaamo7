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
| [`build-ats-resume`](./build-ats-resume/SKILL.md) | Verified | Create, audit, rewrite, and tailor ATS-compatible resumes using verified candidate data. |
| [`presentation-design`](./presentation-design/SKILL.md) | Verified | Turn educational/technical content into structured, visual slide decks and slide plans. |
| [`youtube-to-course`](./youtube-to-course/SKILL.md) | Restored | Convert long-form video or playlist content into a structured course with lessons, exercises, quizzes, and a final project. |
| [`ai-video-creator`](./ai-video-creator/SKILL.md) | Restored | Convert an idea or lesson into a production-ready video workflow: script, storyboard, prompts, recording, and editing plan. |
| [`job-agent`](./job-agent/SKILL.md) | Restored | Search, evaluate, tailor, apply, and track job applications with evidence-first controls. |
| [`it-support`](./it-support/SKILL.md) | Restored | Diagnose Windows endpoints, users, software, peripherals, connectivity, and common infrastructure incidents. |
| [`usb-repair`](./usb-repair/SKILL.md) | Restored from documented workflow | Diagnose USB flash-drive failures and safely perform controller-level recovery when justified. |
| [`network-diagnostics`](./network-diagnostics/SKILL.md) | Restored | Layered TCP/IP, DHCP, DNS, Wi-Fi, routing, firewall, and application-connectivity troubleshooting. |
| [`windows-deployment`](./windows-deployment/SKILL.md) | Restored | Standardize Windows installation, drivers, updates, software, validation, and endpoint handoff. |
| [`powershell-automation`](./powershell-automation/SKILL.md) | Restored | Build safer repeatable Windows automation with validation, logging, idempotency, and rollback awareness. |
| [`pine-script-testing`](./pine-script-testing/SKILL.md) | Restored from documented workflow | Validate Pine Script v6 compilation, logic, inputs, state, repainting risk, visuals, and repository readiness. |
| [`github-agent`](./github-agent/SKILL.md) | Restored | Maintain repositories, files, issues, PRs, documentation, validation, and secret-aware GitHub workflows. |
| [`knowledge-capture`](./knowledge-capture/SKILL.md) | Restored | Turn incidents, troubleshooting, decisions, and research into reusable KB/SOP documentation. |
| [`ai-research`](./ai-research/SKILL.md) | Restored | Perform source-aware technical research, contradiction handling, evidence synthesis, and practical recommendations. |
| [`harness-engineering`](./harness-engineering/SKILL.md) | Restored from documented architecture | Design agent harnesses with tools, skills, context, memory, state, orchestration, verification, and security controls. |
| [`agent-security-permissions`](./agent-security-permissions/SKILL.md) | Restored from documented principles | Design least-privilege agent permissions, secret handling, tool boundaries, action gates, and audit controls. |
| [`spark-image-first-presentation-pack`](./spark-image-first-presentation-pack/README.md) | Manifest | 12-skill presentation pipeline derived from reference-deck reverse engineering. |

## Skill groups

### Agent engineering & governance

- `harness-engineering`
- `agent-security-permissions`
- `github-agent`
- `ai-research`

### IT operations & automation

- `it-support`
- `network-diagnostics`
- `usb-repair`
- `windows-deployment`
- `powershell-automation`
- `knowledge-capture`

### Development & QA

- `pine-script-testing`
- `github-agent`

### Content, learning & career systems

- `presentation-design`
- `build-ats-resume`
- `youtube-to-course`
- `ai-video-creator`
- `job-agent`
- `spark-image-first-presentation-pack`

## Design principles

These skills are built around several common rules:

1. **Evidence before claims** — do not invent facts, qualifications, metrics, sources, technical findings, or outcomes.
2. **Tool-aware execution** — distinguish reasoning from actions performed by tools such as Files, Web, Terminal, GitHub, APIs, or document generators.
3. **Verification loops** — do not treat generation or a successful tool call as completion; inspect the actual result and test it against the objective.
4. **Least-privilege behavior** — request or use only the access required for the current task.
5. **Reusable context** — keep stable domain instructions in skills while keeping task-specific data outside the skill file.
6. **Clear status reporting** — separate verified facts, hypotheses, missing data, and unresolved failures.
7. **Controlled destructive actions** — disk repair, profile replacement, permission changes, firmware operations, deletions, and external sends require stronger evidence and authorization.
8. **Operational documentation** — reusable workflows should record environment, evidence, action, verification, and unresolved risk.

## Suggested harness layout

```text
agent-harness/
├── skills/
│   ├── harness-engineering/
│   ├── agent-security-permissions/
│   ├── github-agent/
│   ├── ai-research/
│   ├── it-support/
│   ├── network-diagnostics/
│   ├── usb-repair/
│   ├── windows-deployment/
│   ├── powershell-automation/
│   ├── knowledge-capture/
│   ├── pine-script-testing/
│   ├── build-ats-resume/
│   ├── presentation-design/
│   ├── youtube-to-course/
│   ├── ai-video-creator/
│   └── job-agent/
├── memory/
├── tools/
├── workflows/
├── state/
├── policies/
└── verification/
```

## Compatibility

The files use Markdown-based `SKILL.md` instructions and can be adapted to agent runtimes that support reusable system/task skills. Tool names, permissions, state management, and connector behavior should be mapped to the target runtime before execution.

## Security note

No API keys, tokens, passwords, private candidate data, customer data, or other secrets should be committed to this directory. Use environment variables or the target platform's secret manager for credentials.

## Portfolio intent

This directory documents reusable workflows and agent-engineering patterns rather than isolated prompts. A skill should demonstrate a repeatable process, explicit boundaries, verification, failure handling, and operational value—not just a long instruction block.
