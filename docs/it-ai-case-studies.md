# IT Support + AI-Assisted Troubleshooting Case Studies

This section documents selected real-world technical support cases from my troubleshooting notes. The goal is to demonstrate practical IT diagnosis, controlled remediation, evidence-based verification, and the use of AI as a technical copilot.

> **Scope of AI use:** AI was used to help structure symptoms, organize troubleshooting hypotheses, research technical identifiers, improve documentation, and define verification steps. Hands-on diagnosis, configuration changes, firmware operations, driver installation, and final validation were performed on the actual systems/devices.

## 1. Autodesk 3ds Max startup failure — User Profile isolation

**Problem**

Autodesk 3ds Max stopped during startup at `Starting 3ds Max...`, while `Script Controller` became `Not Responding`.

**Troubleshooting approach**

- Avoided an immediate full reinstall.
- Treated the issue as a profile/configuration problem first.
- Isolated the user environment by resetting the 3ds Max profile under `%LOCALAPPDATA%`.
- Allowed the application to rebuild a clean default profile.

**Result**

3ds Max started normally after the profile reset. The evidence pointed to corrupted or incompatible user preferences, startup scripts, plugin settings, or configuration files rather than the core installation.

**IT skills demonstrated**

Windows user-profile troubleshooting, application isolation, configuration recovery, root-cause narrowing, low-risk remediation.

**AI-assisted value**

Structured the symptom-to-hypothesis flow, helped separate installation-level causes from profile-level causes, and converted the resolution into a reusable troubleshooting record.

---

## 2. Redragon RU014D 16GB USB recovery — FirstChip controller / NAND mapping

**Problem**

A Redragon USB flash drive appeared as `NAND USB2DISK` with abnormal identifiers `VID FFFF / PID 1201`. Standard tools could see the device, but older FirstChip MPTools could not manage it correctly.

**Diagnosis**

- Used ChipGenius to identify the controller family and Flash ID.
- Identified the device as FirstChip-based and later resolved the controller as `FC212W`.
- Tested multiple MPTool versions rather than forcing incompatible firmware utilities.
- Observed failed High Scan results and a Factory Scan that temporarily reduced the visible capacity to 240 MB.
- Interpreted the capacity drop as a Bin/NAND mapping problem rather than a Windows partition issue.

**Resolution**

Used `Clear + Factory scan` with automatic capacity allocation. The controller rebuilt the NAND mapping and restored approximately 14.65 GB usable capacity.

**Verification**

A full H2testw write/read verification completed without errors across the tested capacity.

**IT skills demonstrated**

USB controller identification, VID/PID analysis, NAND diagnostics, firmware-tool selection, recovery risk management, full-capacity verification.

**AI-assisted value**

Helped organize controller evidence, compare tool versions and scan outcomes, distinguish logical partition symptoms from controller-level mapping faults, and preserve a reproducible troubleshooting history.

---

## 3. Kingston DataTraveler 3.0 16GB — Read Only / Write Protection recovery

**Problem**

A Kingston DataTraveler 3.0 became Read Only / Write Protected and could no longer be used normally.

**Diagnosis**

- Identified the controller as `Phison PS2307 / PS2251-07`.
- Collected VID/PID, Flash ID, firmware information, USB version, and physical capacity before attempting repair.
- Tested Phison MPALL and multiple Format & Restore versions.
- Stopped repeated firmware operations when restore tools returned error codes instead of forcing a blind firmware flash.

**Resolution**

After controlled recovery attempts, Windows again accepted a normal format and the drive returned to its expected capacity.

**Verification**

Successful file creation, write operations, deletion, and normal capacity reporting confirmed that the Write Protection state was no longer blocking normal use.

**IT skills demonstrated**

Phison controller analysis, storage recovery, firmware-risk judgment, stop conditions, practical validation.

**AI-assisted value**

Supported evidence tracking and decision logging, especially the decision **not** to continue flashing firmware once the device had returned to normal operation.

---

## 4. HP Chromebook 14 G6 (DORP) — ChromeOS to Windows via MrChromebox UEFI

**Objective**

Convert an HP Chromebook 14 G6 from the stock ChromeOS boot environment to a Full ROM UEFI environment capable of booting and installing Windows.

**Technical challenges**

- ChromeOS firmware does not behave like a conventional PC BIOS/UEFI installation path.
- Hardware Write Protection and Software Write Protection had to be disabled correctly.
- The Chromebook failed to boot reliably with the battery disconnected when using one USB-C charger.
- Windows installation completed, but several devices required manual Hardware-ID-based driver identification.

**Key troubleshooting decisions**

- Enabled Developer Mode and used MrChromebox Firmware Utility.
- Diagnosed the battery-disconnected boot problem as USB Power Delivery compatibility rather than a motherboard fault.
- Switched to a known-good Dell USB-C 65W adapter, allowing stable boot and firmware work.
- Installed Full ROM UEFI and Windows x64 using GPT/UEFI boot media.
- Used Hardware IDs instead of generic driver packs for post-install driver work.

**Driver work**

- `ACPI\ELAN0001` → ELAN I2C Touchpad.
- `ACPI\ELAN0000` → ELAN Touchscreen.
- `ACPI\BOOT0000` → Coreboot table device.
- Identified the audio stack as Intel Gemini Lake + SOF + Realtek RT5682 + Maxim MAX98357A.
- Confirmed that a Code 10 on the CoolStar SOF audio driver was related to licensing/tamper enforcement rather than an incorrect hardware match.

**Result**

Windows booted successfully through MrChromebox UEFI. Touchpad and touchscreen were restored with matched drivers. The internal audio hardware was correctly identified, while the remaining limitation was documented rather than hidden.

**IT skills demonstrated**

Firmware/UEFI work, Chromebook platform conversion, write-protection handling, USB-PD troubleshooting, Windows deployment, Device Manager, Hardware IDs, driver-stack analysis, limitation documentation.

**AI-assisted value**

Helped correlate Hardware IDs with device classes, structure driver hypotheses, maintain a controlled troubleshooting sequence, and document verified results versus unresolved limitations.

---

## My IT + AI troubleshooting model

I use AI as a **copilot**, not as a substitute for technical verification.

Typical workflow:

1. Capture symptoms, error messages, screenshots, Hardware IDs, logs, and device state.
2. Build multiple technical hypotheses instead of jumping to one cause.
3. Rank troubleshooting steps by risk and reversibility.
4. Use trusted technical sources and vendor/controller information when selecting tools or drivers.
5. Perform the actual repair or configuration change on the system.
6. Verify with measurable evidence: successful boot, Device Manager state, write/read tests, application startup, capacity checks, or logs.
7. Record what worked, what failed, and what remains unresolved.

This approach combines traditional IT support discipline with AI-assisted research, reasoning support, and structured documentation.