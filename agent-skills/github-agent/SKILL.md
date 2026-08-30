---
name: github-agent
status: restored
description: Manage GitHub repositories, files, issues, pull requests, documentation, validation, and portfolio hygiene using evidence-first changes, safe branching, verification, and secret-aware repository practices.
---

# GitHub Agent Skill

Use this skill for repository maintenance, portfolio work, documentation, issue tracking, PR review, and safe GitHub automation.

## Core rules

1. Inspect the repository before changing it.
2. Do not overwrite files blindly; fetch current content first.
3. Keep secrets, API keys, tokens, credentials, and private user data out of commits.
4. Prefer small, reviewable commits with clear messages.
5. Verify every write by fetching the changed path or comparing refs afterward.
6. Preserve repository intent and existing conventions unless a deliberate migration is requested.
7. Distinguish repository problems from CI/workflow failures.

## Repository intake

Collect:

- Repository name and purpose
- Default branch
- Existing README/docs
- Directory structure
- Open issues/PRs when relevant
- CI/workflow status
- Secret-scanning or security findings
- Naming and contribution conventions

## File-change workflow

```text
Read current file
   ↓
Understand repository convention
   ↓
Prepare minimal change
   ↓
Create/update file
   ↓
Fetch changed path
   ↓
Verify content
   ↓
Document commit/result
```

## Portfolio repository workflow

For profile/portfolio repos, prioritize:

- Clear project summaries
- Live project links
- GitHub/Hugging Face/other portfolio links
- Skills grouped by domain
- Evidence of troubleshooting, automation, and documentation work
- No exaggerated claims
- Working links
- Consistent project status labels

## Issue management

A good issue should contain:

```markdown
# Problem
What is wrong or missing?

# Evidence
Logs, screenshots, errors, affected files, or reproducible steps.

# Expected result
What should happen instead?

# Proposed fix
High-level approach.

# Validation
How the fix will be confirmed.
```

## Pull request review

Review:

- Scope matches title/description
- No unrelated changes
- No leaked secrets
- Tests/validation are appropriate
- Documentation is updated when behavior changes
- Error handling and rollback are reasonable
- Naming and formatting match repo conventions

## Secret-aware practices

Never commit:

- API keys
- Access tokens
- Passwords
- Private keys
- `.env` files containing credentials
- Personal customer/user data

Use:

- Environment variables
- `.env.example` without secrets
- GitHub Actions secrets or platform secret stores
- `.gitignore` rules for local credential files

If a secret was committed, removing it from the current file is not enough. Treat it as exposed and rotate/revoke it where applicable; historical cleanup may also be required.

## Validation

After changes, verify:

- File exists at intended path
- README links resolve
- Markdown renders logically
- CI status if relevant
- No obvious secret exposure
- Changed repository state matches the requested goal

## Output

```markdown
# GitHub Change Report
- Repository:
- Files changed:
- Issues/PRs affected:
- Security checks:
- Validation performed:
- Remaining risks:
- Final status:
```
