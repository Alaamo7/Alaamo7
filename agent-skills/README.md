# AI Agent Skills Portfolio

Reusable agent skills and workflow instructions designed for AI agents, agent harnesses, OpenClaw-style runtimes, GPT Work, and related automation systems.

## Status legend

- **Verified** — recovered from an existing saved `SKILL.md` in the working library.
- **Restored** — reconstructed from a previously designed skill package whose original archive is no longer directly available.
- **Manifest** — documented skill pack whose individual source files are not yet recovered in the current workspace.

## Skills

| Skill | Status | Purpose |
|---|---|---|
| [`build-ats-resume`](./build-ats-resume/SKILL.md) | Verified | Create, audit, rewrite, and tailor ATS-compatible resumes using verified candidate data. |
| [`presentation-design`](./presentation-design/SKILL.md) | Verified | Turn educational/technical content into structured, visual slide decks and slide plans. |
| [`youtube-to-course`](./youtube-to-course/SKILL.md) | Restored | Convert long-form video or playlist content into a structured course with lessons, exercises, quizzes, and a final project. |
| [`ai-video-creator`](./ai-video-creator/SKILL.md) | Restored | Convert an idea or lesson into a production-ready video workflow: script, storyboard, prompts, recording, and editing plan. |
| [`job-agent`](./job-agent/SKILL.md) | Restored | Search, evaluate, tailor, apply, and track job applications with evidence-first controls. |
| [`spark-image-first-presentation-pack`](./spark-image-first-presentation-pack/README.md) | Manifest | 12-skill presentation pipeline derived from reference deck reverse engineering. |

## Design principles

These skills are built around several common rules:

1. **Evidence before claims** — do not invent facts, qualifications, metrics, sources, or outcomes.
2. **Tool-aware execution** — distinguish reasoning from actions performed by tools such as Files, Web, Terminal, GitHub, or document generators.
3. **Verification loops** — do not treat generation as completion; inspect outputs and validate results.
4. **Least-privilege behavior** — request or use only the access required for the current task.
5. **Reusable context** — keep stable instructions in skills while keeping task-specific data outside the skill file.
6. **Clear status reporting** — separate verified facts, inferred conclusions, missing data, and unresolved failures.

## Suggested harness layout

```text
agent-harness/
├── skills/
│   ├── build-ats-resume/
│   ├── presentation-design/
│   ├── youtube-to-course/
│   ├── ai-video-creator/
│   └── job-agent/
├── memory/
├── tools/
├── workflows/
└── verification/
```

## Compatibility

The files use Markdown-based `SKILL.md` instructions and can be adapted to agent runtimes that support reusable system/task skills. Tool names and permission models should be mapped to the target runtime before execution.

## Security note

No API keys, tokens, passwords, personal candidate data, or secrets should be committed to this directory. Use environment variables or the target platform's secret manager for credentials.
