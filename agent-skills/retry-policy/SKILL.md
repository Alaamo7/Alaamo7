---
name: retry-policy
status: restored
description: Define when AI agent actions may be retried, how backoff and attempt limits work, and when retries must stop to avoid duplicate side effects, wasted cost, or repeated failure.
---

# Retry Policy Skill

## Core principle

Retry only when there is a concrete reason a second attempt may succeed.

## Retryable examples

- Temporary network failure
- HTTP 429 / rate limit
- Transient 5xx service error
- Short-lived timeout
- Eventual-consistency delay

## Usually non-retryable without a change

- Invalid input
- Missing permission
- Unsupported operation
- Authentication failure caused by invalid credentials
- Deterministic validation failure
- Destructive action with uncertain completion state

## Policy flow

```text
Error
 ↓
Classify retryability
 ↓
Check side effects
 ↓
If retryable: apply attempt limit + backoff
 ↓
Re-run
 ↓
Verify
 ↓
Stop on success or escalation threshold
```

## Backoff

Prefer exponential or bounded backoff for transient services. Respect server-provided retry hints when available.

## Attempt limits

Set limits based on:

- Failure type
- Action cost
- Time sensitivity
- Side-effect risk

## Duplicate prevention

For writes, sends, orders, commits, or external actions, use idempotency keys or pre-retry state checks where supported.

## Stop conditions

Stop retrying when:

- The same deterministic failure repeats.
- Cost/time threshold is reached.
- Permission is missing.
- Side-effect state cannot be determined safely.
- Human approval is required.

## Logging

Record attempt number, error type, delay, model/tool used, side-effect check, and final result.