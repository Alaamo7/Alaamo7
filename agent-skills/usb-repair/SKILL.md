---
name: usb-repair
status: restored-from-documented-workflow
description: Diagnose USB flash-drive failures, identify controller/NAND information, distinguish logical from controller-level faults, choose recovery paths cautiously, and verify capacity and read/write integrity after repair.
---

# USB Repair Skill

Use this skill for USB flash drives that are read-only, show wrong capacity, fail formatting, disconnect, or require controller-level diagnosis.

## Safety boundary

USB controller tools can destroy data. Before any low-level operation:

1. Determine whether data recovery or device reuse is the priority.
2. Never run MPTool/production-tool operations on a drive containing needed data unless the user explicitly accepts destructive recovery.
3. Confirm the physical USB target to avoid acting on the wrong disk.
4. Record VID/PID/controller/NAND details before changing firmware or production settings.

## Diagnostic workflow

```text
Detect device
  ↓
Confirm physical disk identity
  ↓
Check Windows Disk Management / Device Manager
  ↓
Read VID / PID
  ↓
Inspect controller information
  ↓
Identify NAND where possible
  ↓
Classify logical vs controller-level failure
  ↓
Choose non-destructive or destructive path
  ↓
Repair / restore
  ↓
Reconnect
  ↓
Verify reported capacity
  ↓
Full write/read integrity test
```

## First-line checks

Inspect:

- Device Manager detection
- Disk Management capacity/partition state
- `diskpart` attributes
- File-system errors
- Write-protect state
- VID/PID
- Controller identification using appropriate diagnostic tooling

Logical issues may be solved without controller-level tooling. Do not jump directly to MPTool.

## Controller-level diagnosis

When ordinary formatting/partition repair fails and the evidence points to controller state:

1. Identify the controller family.
2. Confirm compatible production/MPTool variants from reliable sources.
3. Match tool/controller/NAND information as closely as possible.
4. Save screenshots or configuration evidence before execution.
5. Use conservative/default configurations unless documented evidence supports custom settings.

## Verification

A drive is not considered repaired merely because Windows formats it.

Verify:

- Stable reconnect/detection
- Correct capacity
- No immediate write-protect return
- Full-capacity write test when practical
- Read-back verification
- Reconnect after test
- No obvious fake-capacity behavior

## Failure reporting

If repair fails, document:

```markdown
# USB Repair Report
- Device:
- VID/PID:
- Reported capacity:
- Controller:
- NAND info:
- Initial symptoms:
- Logical tests:
- Controller-level tool attempted:
- Configuration used:
- Result:
- Capacity verification:
- Read/write verification:
- Final status: Repaired / Unstable / Data-recovery-only / Hardware failure suspected
```

## Do not infer

Do not claim that a NAND chip, controller, firmware image, or production-tool version is correct unless it was actually identified or verified.