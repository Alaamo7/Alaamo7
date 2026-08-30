---
name: data-validation
status: restored-from-documented-architecture
description: Validate structured and semi-structured data before agent decisions or tool execution using schema checks, type/range validation, completeness rules, cross-field consistency, provenance, and anomaly handling.
---

# Data Validation Skill

Validate data before using it as evidence, configuration, or tool input.

## Validation layers

### 1. Schema

Check required fields, allowed fields, types, nesting, enums, and formats.

### 2. Domain constraints

Validate ranges and meaningful values such as ports, dates, percentages, identifiers, quantities, and supported states.

### 3. Cross-field consistency

Examples:

- start date must not be after end date;
- destination must match operation type;
- file extension should match intended representation where applicable;
- model/tool selection must satisfy task requirements.

### 4. Completeness

Separate:

- required missing data;
- optional missing data;
- unavailable but non-blocking data.

Do not fabricate missing values.

### 5. Provenance

Track where critical values came from:

- user input
- file
- connector
- API
- web source
- tool output
- inference

Do not silently promote inferred values to verified data.

## Validation workflow

```text
Raw data
 ↓
Parse
 ↓
Schema validation
 ↓
Domain validation
 ↓
Cross-field checks
 ↓
Provenance/confidence checks
 ↓
PASS / REJECT / NEEDS REVIEW
```

## Error output

Return actionable findings:

```markdown
- field: target_path
- status: invalid
- reason: path outside authorized workspace
- supplied_value: [redacted if sensitive]
- required_action: provide an authorized destination
```

## Before tool execution

High-risk actions should fail closed when critical input validation fails.

## After tool execution

Validate outputs before downstream use. A structurally successful API response may still contain missing, stale, inconsistent, or semantically invalid data.

## Goal

Prevent bad data from becoming bad actions.