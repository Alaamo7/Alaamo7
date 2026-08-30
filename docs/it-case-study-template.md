# IT + AI Troubleshooting Case Study Template

Use this template only after the incident has enough evidence to support a public technical write-up.

## Incident title

`[Product / Device] — [symptom or failure] — [main technical theme]`

## Date

YYYY-MM-DD

## Status

Resolved / Partially Resolved / Open

## Environment

- Device / platform:
- Operating system:
- Application / service:
- Relevant hardware:
- Relevant version / firmware:

> Do not include customer names, credentials, serial numbers, email addresses, phone numbers, private IPs, license keys, or other unnecessary identifiers.

## Problem

Describe the observable symptom and business/user impact. Include the exact error message when useful.

## Evidence collected

- Error messages:
- Screenshots:
- Logs / Event Viewer:
- Device Manager / Hardware IDs:
- VID/PID / controller / firmware data:
- Disk / SMART / health data:
- Network tests:
- Reproduction steps:

## Technical hypotheses

1. Hypothesis A — why it could explain the evidence.
2. Hypothesis B — why it could explain the evidence.
3. Hypothesis C — why it was considered or rejected.

## Risk assessment

- Lowest-risk reversible step:
- Changes requiring backup:
- Destructive operations considered:
- Stop condition / rollback plan:

## Troubleshooting actions

1. Action performed.
   - Reason:
   - Result:
2. Next action.
   - Reason:
   - Result:

Document failed attempts too when they improve the technical story.

## Root cause

State only what the evidence supports.

Use one of these forms when appropriate:

- **Confirmed:** direct evidence identifies the cause.
- **Strongly supported:** the fix isolated the fault but the individual corrupt file/component was not identified.
- **Probable:** evidence is incomplete; avoid presenting this as confirmed.

## Resolution

Describe the final repair or configuration change.

## Verification

List objective evidence that the fix worked:

- Successful boot / application startup
- Device Manager state
- Full write/read verification
- Capacity / SMART / health check
- Network connectivity test
- Event log result
- User workflow test

## Remaining limitations

Document anything unresolved instead of hiding it.

## IT skills demonstrated

Examples:

Windows troubleshooting, hardware diagnosis, networking, storage recovery, firmware/UEFI, Device Manager, Hardware IDs, application support, backup/recovery, Active Directory, Microsoft 365, PowerShell, virtualization.

## AI-assisted contribution

Describe AI only as actually used, for example:

- Structured symptoms and evidence
- Generated troubleshooting hypotheses
- Helped correlate technical identifiers
- Compared documentation or driver/controller information
- Suggested verification steps
- Converted the incident into structured documentation

Do **not** claim AI performed hands-on work that was actually performed by the technician.

## Lessons learned

- What prevented unnecessary work?
- Which clue was decisive?
- What should be checked earlier next time?
- What risk should future technicians avoid?

## Portfolio readiness checklist

- [ ] Real incident, not a simulation
- [ ] Evidence supports the technical claims
- [ ] Result is verified
- [ ] Root cause confidence is stated accurately
- [ ] Failed attempts are represented fairly
- [ ] No customer-sensitive information
- [ ] No credentials, keys, private URLs, or identifying serial numbers
- [ ] AI contribution is described accurately
- [ ] Technical limitations are disclosed
