---
name: api-integration
status: restored
description: Integrate external APIs into agent workflows with authentication hygiene, schema validation, pagination, rate-limit handling, retries, error classification, and verification.
---

# API Integration Skill

Build API integrations that are reliable, observable, and safe for agent execution.

## Workflow

1. Read authoritative API documentation.
2. Identify authentication method and required scopes.
3. Define endpoint and request schema.
4. Validate request data before sending.
5. Handle pagination and rate limits explicitly.
6. Parse response into a stable internal structure.
7. Classify errors.
8. Verify mutations using a read-after-write check when available.

## Authentication

- Use environment variables or secret managers.
- Never hard-code API keys or tokens.
- Request minimum scopes.
- Do not log authorization headers.
- Distinguish authentication failure from authorization failure.

## Request controls

Validate:

- HTTP method
- endpoint
- identifiers
- required body fields
- content type
- query parameters
- timeout

## Response handling

Do not assume `2xx` alone means the business objective succeeded. Inspect returned state.

Handle:

- pagination
- empty result sets
- partial records
- asynchronous job IDs
- eventual consistency
- malformed responses

## Error taxonomy

Classify at minimum:

- Invalid request
- Authentication failure
- Permission failure
- Not found
- Conflict
- Rate limited
- Transient server failure
- Permanent failure

## Retry behavior

Retry transient failures only. Respect server-provided backoff when available. Do not retry invalid inputs or permission failures blindly.

## Mutation verification

For create/update/delete actions:

```text
Send mutation
  ↓
Read response
  ↓
Fetch resulting resource if supported
  ↓
Compare with intended state
```

## Integration report

Document endpoint, auth mechanism, scopes, request/response mapping, limits, error behavior, and verification strategy.