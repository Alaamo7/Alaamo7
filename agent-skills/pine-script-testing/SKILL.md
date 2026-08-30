---
name: pine-script-testing
status: restored-from-documented-workflow
description: Review, test, validate, and document Pine Script v6 indicators and strategies for compilation, logic correctness, repainting risk, configurable inputs, state persistence, visual behavior, and repository readiness.
---

# Pine Script Testing & Validation Skill

Use this skill to perform structured QA on Pine Script v6 code rather than treating successful compilation as sufficient validation.

## Core rules

1. Compilation success does not prove trading logic is correct.
2. Separate syntax errors, runtime issues, logic flaws, repainting risks, UX problems, and documentation gaps.
3. Do not claim profitability or predictive value from code correctness.
4. Verify user-configurable inputs are actually used by the logic.
5. Treat higher-timeframe and future-looking data as repainting-sensitive until proven otherwise.
6. Preserve the original trading intent when fixing code.
7. Document every material change.

## Validation pipeline

```text
Read script
   ↓
Identify script type and intent
   ↓
Static code review
   ↓
Compile / syntax validation
   ↓
Input and state validation
   ↓
Signal logic review
   ↓
Repainting / HTF review
   ↓
Visual / dashboard review
   ↓
Behavioral test cases
   ↓
Regression check
   ↓
Documentation and repository readiness
```

## 1. Script inventory

Capture:

- Script name
- Pine version
- `indicator()` or `strategy()`
- Overlay setting
- Inputs
- Main calculations
- Entry/signal conditions
- Alerts
- Plots/tables/labels
- External/timeframe requests

## 2. Static review

Check for:

- Deprecated or invalid syntax
- Unused variables or inputs
- Repeated calculations
- Incorrect type assumptions
- State variables that reset unexpectedly
- Unsafe array/table usage
- Hard-coded thresholds that should respect inputs

## 3. Input validation

For every user input, verify that changing the input changes the intended behavior.

Example failure class:

```text
RSI threshold input exists
but signal logic still uses a hard-coded 70/30 value
```

This is a functional bug even if the script compiles.

## 4. Repainting and higher-timeframe review

Pay special attention to:

- `request.security()`
- Higher-timeframe OHLC values
- Current unfinished HTF candles
- Lookahead behavior
- Pivot confirmation delay
- Signals that visually move or disappear after bar close

When prior completed HTF data is intended, explicitly verify that the implementation references completed bars rather than an unfinished current HTF bar.

Do not label a script "non-repainting" unless the relevant pathways have been inspected and tested.

## 5. Persistent state review

Inspect stateful dashboard fields, "last signal", "last break", counters, and historical markers.

Verify whether values should:

- Update every bar
- Persist until a new event
- Reset on session/timeframe change
- Be historical series rather than simple state

A dashboard that displays only the current-bar condition instead of the most recent event may be logically wrong even if its appearance looks correct on some bars.

## 6. Signal logic

For each signal:

```text
Inputs
  ↓
Calculated series
  ↓
Condition
  ↓
Confirmation/filter
  ↓
Plot/alert/order
```

Trace the entire chain and confirm no input or condition is bypassed.

## 7. Strategy-specific checks

When the script is a strategy, inspect:

- Entry conditions
- Exit conditions
- Stop-loss / take-profit logic
- Position sizing
- Pyramiding
- Commission/slippage assumptions
- Date/session filters
- Same-bar entry/exit edge cases

Code QA is not the same as assessing trading performance.

## 8. Visual QA

Check:

- Plots align with the intended bars.
- Labels do not explode in number unnecessarily.
- Tables update correctly.
- Colors/status text match conditions.
- Support/resistance and signal markers do not shift unexpectedly.
- Chart remains readable.

## 9. Test cases

Create deliberate scenarios such as:

- Input threshold changed from default
- No-signal region
- Strong signal region
- First bars with insufficient history
- Timeframe change
- HTF boundary transition
- Session boundary
- Last-event persistence

## 10. Issue report

```markdown
# Pine Script QA Report

## Script
- Name:
- Version:
- Type:

## Status
- Compile: PASS / FAIL
- Logic: PASS / ISSUES
- Repainting review: PASS / RISK / NOT VERIFIED
- Inputs: PASS / ISSUES
- Visuals: PASS / ISSUES
- Documentation: PASS / ISSUES

## Findings
### [Severity] Finding title
- Evidence:
- Impact:
- Recommended fix:
- Verification after fix:
```

## Severity

- **Critical** — invalid orders/signals, future leakage, severe repainting, or materially false output.
- **High** — important logic/input/state behavior is incorrect.
- **Medium** — edge case or usability problem that can affect interpretation.
- **Low** — maintainability, naming, formatting, or minor UX issue.

## Repository readiness

Before marking ready:

- Compiles under Pine v6.
- No known critical/high logic issue remains.
- Inputs are functional.
- Repainting characteristics are documented.
- README explains purpose and limitations.
- Screenshots/examples match current code.
- Changelog or commit notes explain material fixes.
