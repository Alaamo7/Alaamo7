---
name: secrets-management
status: restored
description: Protect API keys, tokens, credentials, and other secrets in AI agent systems using secret stores, environment variables, redaction, rotation, least privilege, and repository-safe handling.
---

# Secrets Management Skill

## Core rules

1. Never hard-code secrets into source code, prompts, `SKILL.md`, logs, screenshots, examples, tests, or public repositories.
2. Prefer platform secret stores or environment variables.
3. Give each secret the minimum scope required.
4. Rotate exposed or suspected-compromised credentials.
5. Redact secret values from error reports and logs.
6. Do not confuse identifiers such as usernames or endpoint URLs with authentication secrets.

## Secret lifecycle

```text
Create
 ↓
Store securely
 ↓
Grant least privilege
 ↓
Inject at runtime
 ↓
Use without logging
 ↓
Monitor exposure/expiry
 ↓
Rotate/revoke
```

## Repository safety

Before commits or publication, check for:

- API keys
- Access tokens
- `.env` files
- Private certificates/keys
- Credential JSON files
- Hard-coded auth headers
- Test fixtures containing real credentials

Use `.gitignore` and secret-scanning controls, but do not treat `.gitignore` as protection for a secret that was already committed.

## Exposure response

If a secret enters version control:

1. Treat it as compromised.
2. Revoke/rotate it first.
3. Remove it from active code.
4. Replace with runtime secret injection.
5. Review repository/history exposure based on risk.
6. Scan for related credentials.
7. Document the incident without reproducing the secret.

## Agent rules

Agents must not:

- Echo secret values back to users unnecessarily.
- Persist credentials to memory.
- Include secrets in generated documentation.
- Copy credentials between unrelated services.

## Verification

A secret-handling change passes only when the application still authenticates correctly while the credential is no longer embedded in public or persistent plaintext artifacts.