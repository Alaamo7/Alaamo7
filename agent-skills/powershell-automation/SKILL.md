---
name: powershell-automation
status: restored
description: Design, review, and execute PowerShell automation for Windows support and administration with idempotency, logging, validation, rollback awareness, least privilege, and explicit handling of destructive actions.
---

# PowerShell Automation Skill

Use this skill for Windows automation, diagnostics, software checks, user/device administration, deployment support, and repeatable IT tasks.

## Core rules

1. Prefer read-only inspection before state-changing commands.
2. Make scripts idempotent where practical: rerunning them should not create duplicate or inconsistent state.
3. Validate prerequisites and target scope before execution.
4. Use explicit error handling and meaningful exit behavior.
5. Log material actions without exposing secrets.
6. Do not embed credentials in scripts.
7. Treat registry edits, service changes, permission changes, disk operations, and mass actions as higher-risk operations requiring stronger validation.

## Script structure

Recommended pattern:

```powershell
# 1. Parameters
param(...)

# 2. Strict/error behavior
$ErrorActionPreference = 'Stop'

# 3. Prerequisite checks

# 4. Current-state inspection

# 5. Planned change

# 6. Execution

# 7. Verification

# 8. Logging / exit
```

## Parameters

Prefer parameterized scripts over hard-coded values.

```powershell
param(
    [Parameter(Mandatory)]
    [string]$ComputerName
)
```

Validate inputs using appropriate validation attributes or explicit checks.

## Error handling

Use structured handling for consequential operations:

```powershell
try {
    # operation
}
catch {
    Write-Error $_
    exit 1
}
```

Do not suppress errors merely to make a script appear successful.

## Idempotency

Before creating or changing something:

1. Read current state.
2. Compare with desired state.
3. Change only when necessary.
4. Verify desired state afterward.

Example pattern:

```text
Check service state
  ↓
Already desired? → no change
  ↓ no
Apply change
  ↓
Read service state again
```

## Logging

Log:

- Timestamp
- Target
- Operation
- Before state when relevant
- Result
- Errors

Never log plaintext passwords, tokens, private keys, or sensitive authentication data.

## Remote execution

Before using PowerShell Remoting:

- Confirm authorization
- Confirm correct target
- Understand credential/delegation model
- Restrict scope
- Handle unreachable systems cleanly

## Common IT automation categories

- System inventory
- Service checks
- Network configuration inspection
- Event log collection
- Software inventory
- Disk/storage reporting
- Windows update checks
- User/group inspection
- File deployment
- Configuration validation

## Destructive-action gate

Require additional verification before:

- Removing files/directories
- Deleting user profiles
- Modifying partitions
- Registry deletion
- Disabling security controls
- Bulk account changes
- Remote restart/shutdown

Where supported, offer a dry-run or `-WhatIf` path.

## Verification

After execution, query the actual system state. A command returning without an exception does not prove the desired outcome occurred.

## Output

```markdown
# PowerShell Automation Report
- Objective:
- Targets:
- Prerequisites:
- Script/action:
- Changes made:
- Validation:
- Errors:
- Rollback considerations:
- Final status:
```
