# IT Support Lab

A practical portfolio area for evidence-backed IT Support, Help Desk, Technical Support, and IT Operations work.

## What this lab proves

This lab is designed to demonstrate troubleshooting discipline rather than a list of claimed skills. Each real case is documented with the available symptoms, evidence, hypotheses, repair path, validation, and limitations.

### Current verified evidence

The current documented portfolio contains five real-world troubleshooting cases:

1. **Autodesk 3ds Max startup failure** — isolated and resolved by resetting a corrupted Windows user profile instead of reinstalling the application or operating system.
2. **Redragon USB flash recovery** — controller/NAND-level recovery using FirstChip tooling, followed by a full H2testw write/read verification.
3. **Kingston DataTraveler read-only recovery** — Phison controller analysis with a controlled recovery path and explicit stop conditions.
4. **HP Chromebook 14 G6 Windows conversion** — MrChromebox Full ROM UEFI, USB-PD troubleshooting, and Hardware-ID-based driver analysis.
5. **The Sims 4 startup failure** — isolated to a user-data/version mismatch and corrected without an unnecessary full reinstall.

Read the detailed cases: [IT + AI-Assisted Troubleshooting Case Studies](../it-ai-case-studies.md).

Use the reusable format: [IT Case Study Template](../it-case-study-template.md).

## Troubleshooting workflow

```text
Incident / symptom
      |
      v
Capture evidence
(error text, logs, Hardware IDs, device state)
      |
      v
Build ranked hypotheses
      |
      v
Choose lowest-risk useful test
      |
      v
Apply repair / configuration change
      |
      v
Validate the result
      |
      +--> PASS -> document evidence and prevention notes
      |
      +--> FAIL -> preserve evidence, revise hypothesis, escalate if needed
```

## Lab capability map

| Area | Current evidence | Next portfolio evidence |
| --- | --- | --- |
| Windows support | Real application/profile/startup cases | Repeatable OS health and deployment runbooks |
| Hardware & storage | USB controller/NAND recovery cases | SMART/storage triage runbook and safe stop conditions |
| Firmware / UEFI | Chromebook conversion case | Firmware recovery checklist and rollback notes |
| Drivers | Hardware-ID-based analysis | Driver triage decision tree |
| Networking | Troubleshooting experience to be documented | DNS/DHCP/Wi-Fi/LAN diagnostic runbooks |
| Identity & access | Portfolio evidence still to be added | AD/GPO/M365 lab scenarios |
| Automation | Portfolio evidence still to be added | PowerShell diagnostics and evidence collection |
| Monitoring / backup | Portfolio evidence still to be added | Health-check, backup verification, and recovery scenarios |

The table deliberately separates **verified evidence** from **planned evidence**. Planned items are not presented as completed work.

## Evidence standard

A case is portfolio-ready only when it has enough information to answer:

- What was the reported symptom?
- What evidence was captured before changing the system?
- Which hypotheses were considered?
- Why was the selected action lower risk than the alternatives?
- What was changed?
- How was success or failure verified?
- What remains unknown or environment-specific?

## AI-assisted operations

AI may be used as a technical copilot for:

- structuring hypotheses,
- researching documentation,
- comparing likely causes,
- organizing logs and Hardware IDs,
- drafting runbooks,
- and converting successful fixes into reusable knowledge.

AI output is not treated as proof. The final evidence must come from the actual system, device, logs, tests, or reproducible lab execution.

## Next build targets

The next useful additions are:

1. Windows diagnostic runbooks.
2. Networking triage: IP, gateway, DNS, DHCP, Wi-Fi, and LAN isolation.
3. Identity lab: Active Directory, users/groups, permissions, password resets, and GPO basics.
4. PowerShell diagnostics and inventory scripts with sample output.
5. Backup/restore verification scenarios.
6. Monitoring and escalation examples.

The long-term target is a dedicated `Alaamo7/it-support-lab` repository after the lab has enough independently testable content to justify a separate project.
