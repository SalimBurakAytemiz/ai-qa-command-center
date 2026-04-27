# Quality Report Screen Mockup

## Purpose

This mockup defines the future quality report screen.

## Main Goal

The screen should show:

- Overall QA status
- Work completed
- Generated outputs
- Test case generation summary
- Risks
- Blockers
- Missing information
- Human review items
- Recommended next actions

## Example Report

| Field | Value |
|---|---|
| Feature | User Login |
| Status | Yellow |
| Product Context | Generated |
| Test Strategy | Generated |
| Test Plan | Generated |
| Test Cases | Generated |
| API Plan | Generated |
| DB Plan | Generated |
| Jira Drafts | Drafted |
| Executive Summary | Generated |

## Test Case Summary

| Type | Count |
|---|---:|
| Happy Path | 5 |
| Edge Cases | 3 |
| Negative Cases | 7 |
| Permission / Session | 3 |

## Risks

- P0: Guest can access dashboard directly
- P1: Disabled user login behavior unclear
- P1: Error message safety not confirmed
- P2: API status ambiguity

## Blockers

- API status codes unknown
- DB schema unknown
- Dashboard routes unknown

## Next Actions

1. Confirm API behavior
2. Confirm dashboard routes
3. Confirm DB schema
4. Review generated outputs
5. Decide execution plan

## Reporting Rule

Reports must separate generated, reviewed, executed, blocked, and approved states.

Do not report generated test cases as passed tests.
