---
name: windows-deployment
status: restored
description: Plan and execute Windows installation, post-install configuration, driver validation, essential software deployment, recovery, and handoff using reproducible checklists and verification rather than ad-hoc setup.
---

# Windows Deployment Skill

Use this skill for clean Windows installations, reinstallations, post-deployment configuration, customer-device preparation, and standardized endpoint handoff.

## Core rules

1. Preserve required user data before destructive installation steps.
2. Confirm target disk and partition plan before formatting.
3. Record device model and critical hardware before deployment.
4. Prefer OEM/vendor drivers for chipset, storage, graphics, network, audio, touchpad, and device-specific components.
5. Do not assume Device Manager showing no unknown devices means every device feature works correctly.
6. Verify Windows activation/licensing status without bypassing licensing controls.
7. Avoid unnecessary software bundles, duplicate players/codecs, and adware.
8. Validate the final user workflow before handoff.

## Deployment workflow

```text
Requirements and backup
      ↓
Hardware / firmware inventory
      ↓
Installation media validation
      ↓
Boot mode / disk target confirmation
      ↓
Windows installation
      ↓
Chipset / platform drivers
      ↓
Network / graphics / audio / input drivers
      ↓
Windows Update
      ↓
Essential software
      ↓
Security and recovery checks
      ↓
Functional validation
      ↓
Handoff documentation
```

## Pre-install checklist

Capture:

- Device manufacturer/model
- BIOS/UEFI mode
- Storage devices and capacities
- Existing Windows edition when relevant
- User data requiring backup
- Network driver availability
- BitLocker/encryption state
- Special hardware such as touchscreen, fingerprint, discrete GPU, card reader, docking station

## Installation media

Verify:

- Correct architecture
- Appropriate Windows edition
- Trusted installation source
- UEFI/Legacy compatibility
- USB media integrity when installation errors are suspected

## Driver order

A practical order is:

1. Chipset/platform
2. Storage/controller when required
3. Management Engine / system components where applicable
4. Network
5. Graphics
6. Audio
7. Touchpad/input/touchscreen
8. Card reader/Bluetooth/camera/other peripherals
9. OEM utilities only when they provide real device functionality

The exact order can vary by device/vendor.

## Post-install software

Install only software justified by the user's workflow. Categories may include:

- Supported browser(s)
- Office/productivity software when licensed/required
- PDF reader/editor
- Media player
- Compression utility
- Remote-support tool when authorized
- Hardware/vendor utilities when necessary

Avoid installing overlapping applications solely because they were traditionally included in an old setup checklist.

## Windows Update

After drivers are functional:

- Run updates
- Reboot as required
- Recheck optional driver updates cautiously
- Confirm no update introduced device regression

## Functional verification

Test actual device functions:

- Boot/restart
- Wi-Fi/Ethernet
- Audio input/output
- Display resolution/brightness
- Touchpad/mouse
- Touchscreen if present
- USB ports
- Camera/microphone
- Sleep/wake
- Battery/charging indicators where relevant
- Printers or customer peripherals when part of the job

## Recovery and rollback

Where appropriate:

- Create restore/recovery information
- Record driver sources
- Keep deployment notes
- Document unresolved hardware limitations

## Handoff report

```markdown
# Windows Deployment Report
- Device:
- Windows edition/build:
- Installation type:
- Backup performed:
- Driver status:
- Windows Update status:
- Applications installed:
- Functional tests:
- Known limitations:
- Final status:
```
