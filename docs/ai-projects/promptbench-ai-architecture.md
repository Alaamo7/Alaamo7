# PromptBench AI — Architecture Notes

## Purpose

This document defines the current **verified high-level architecture** for PromptBench AI and separates confirmed facts from implementation details that still need source-level verification.

## Verified deployment context

- Hosted on **Hugging Face Spaces**
- Public Space: https://huggingface.co/spaces/3la2mo7/promptbench-ai
- Portfolio category: hosted AI application / agent-oriented experimentation

## High-level architecture

```text
+------------------+
|  User / Tester   |
+--------+---------+
         |
         v
+--------------------------+
|   Hugging Face Space     |
|  Hosted application UI   |
+------------+-------------+
             |
             v
+--------------------------+
| Prompt / Task Workflow   |
| Input normalization      |
| Prompt construction      |
| Execution orchestration  |
+------------+-------------+
             |
             v
+--------------------------+
| Model / Service Layer    |
| External or hosted LLM   |
| integration when enabled |
+------------+-------------+
             |
             v
+--------------------------+
| Evaluation / Validation  |
| Output review            |
| Test cases               |
| Failure analysis         |
+------------+-------------+
             |
             v
+--------------------------+
| Result / Iteration Loop  |
+--------------------------+
```

## Architecture principles

### 1. Separation of concerns

The UI, prompt logic, model/service integration, and evaluation layer should remain logically separated so each can be tested independently.

### 2. Secrets stay outside source code

API credentials must be loaded from environment variables or Hugging Face Space Secrets.

### 3. Failures are evidence

Unexpected outputs, API failures, latency problems, validation failures, and deployment errors should be documented instead of removed from the engineering record.

### 4. Reproducibility

A future dedicated source repository should pin dependencies and document startup steps so another developer can reproduce the application locally.

## Source-level items still to verify

The following must not be presented as confirmed until checked directly from the current Space source:

- exact UI framework,
- exact Python version,
- model/provider names,
- external API providers,
- evaluation library implementation,
- persistent storage use,
- telemetry/logging implementation,
- CI/CD mechanism,
- runtime hardware configuration.

## Target repository layout

When mirrored to a dedicated GitHub repository, the recommended structure is:

```text
promptbench-ai/
├── README.md
├── app.py
├── requirements.txt
├── .gitignore
├── .env.example
├── LICENSE
├── docs/
│   ├── architecture.md
│   ├── security.md
│   ├── deployment.md
│   └── validation.md
├── tests/
│   ├── test_smoke.py
│   └── test_evaluator.py
└── .github/
    └── workflows/
        └── ci.yml
```

The exact file names should be adapted to the verified source tree rather than forcing this proposed layout onto the existing Space.
