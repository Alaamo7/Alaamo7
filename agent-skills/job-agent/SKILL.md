---
name: job-agent
status: restored
description: Search for suitable jobs, evaluate fit, tailor application materials, apply only through authorized channels, and track submissions while preventing duplicate applications and invented candidate claims.
---

# Job Agent Skill

Run a disciplined job-search workflow from discovery to tracking.

## Core rules

1. Use verified candidate data only.
2. Never invent experience, degrees, certifications, dates, achievements, tools, salary history, or contact details.
3. Evaluate fit before applying.
4. Do not apply to a job that violates hard candidate constraints.
5. Prevent duplicate applications.
6. Use email only when a recruitment email address is explicitly available and verified.
7. Keep a clear audit trail for every application.
8. Treat application submission as a consequential action: confirm the target and materials are correct before sending.

## Workflow

### 1. Job discovery

Capture:

- Job title
- Company
- Location
- Work mode
- Posting date
- Source URL
- Contact/application channel
- Salary if published
- Mandatory requirements
- Preferred requirements

### 2. Eligibility screening

Reject or flag jobs with hard conflicts such as:

- Unsupported mandatory degree/certification
- Required experience materially above the verified profile
- Age restriction the candidate does not meet
- Location/travel constraints the candidate cannot satisfy
- Required language/tool that is mandatory and unsupported
- Suspicious or unverifiable application channel

### 3. Fit scoring

Classify requirements as:

- **Matched**
- **Transferable**
- **Gap**
- **Disqualifier**

Return an overall fit such as **Strong**, **Moderate**, or **Weak** instead of pretending to know employer ATS scoring.

### 4. Tailor the CV

Use the `build-ats-resume` skill when available.

Tailor:

- Target title
- Professional summary
- Relevant technical skills
- Experience bullet ordering
- Projects
- Vacancy keywords that are genuinely supported

Never add unsupported keywords as candidate capabilities.

### 5. Application message

Create a concise, role-specific email or message only when the application channel requires it.

Include:

- Target role
- Brief fit statement
- Key relevant experience/tools
- Availability of attached CV
- Professional closing

### 6. Pre-send verification

Before sending verify:

- Correct company and role
- Correct recipient
- Correct CV version
- No placeholder text
- No invented claim
- No duplicate application
- Attachments open correctly

### 7. Tracking

Log each application with:

```text
Date
Company
Role
Source
Application channel
CV version
Message version
Status
Follow-up date
Notes
```

Recommended statuses:

- Discovered
- Reviewed
- Rejected by agent
- Ready to apply
- Applied
- Follow-up due
- Interview
- Rejected by employer
- Offer
- Closed

## Duplicate prevention

Treat jobs as duplicates when the same company + role + location/source clearly represent the same vacancy. If uncertain, inspect the posting rather than submitting twice.

## Follow-up

Create follow-up actions only when appropriate. Do not spam recruiters. Preserve the original application date and channel.

## Security and privacy

- Do not expose candidate private data publicly.
- Do not commit CVs containing personal contact data into public repositories unless explicitly requested.
- Do not store credentials or email tokens in skill files or logs.

## Output per job

```markdown
# Job Evaluation
- Company:
- Role:
- Fit: Strong / Moderate / Weak
- Strong matches:
- Transferable matches:
- Gaps:
- Disqualifiers:
- Recommended action: Apply / Skip / Needs review
- CV tailoring notes:
- Application channel:
- Tracking status:
```
