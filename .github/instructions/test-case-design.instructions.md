# Test Case Design Instructions

## Purpose

Use these instructions when creating, reviewing, improving, or restructuring test cases.

These instructions apply to manual test cases, regression candidates, automation candidate lists, happy path cases, edge cases, negative cases, permission cases, and session cases.

## Core Rules

1. Do not create vague test cases.
2. Do not mix happy path, edge case, and negative case scenarios in the same section.
3. Do not claim execution.
4. Do not mark tests as passed unless real execution evidence exists.
5. Always include user role, platform, preconditions, test data, steps, and expected result.
6. Expected results must be observable and testable.
7. If information is missing, list it under Missing Information.
8. Do not invent acceptance criteria, API behavior, DB schema, routes, or user roles.
9. Mark automation candidates realistically.
10. Use risk-based priority values.

## Priority Rules

Use:

- P0: Release blocker
- P1: Critical
- P2: Important
- P3: Low priority

P0 should be used only for severe business, security, data, access-control, or release-blocking risk.

Do not mark every case as P0 or P1.

## Required Test Case Fields

Every test case should include:

- ID
- Title
- Priority
- Platform
- User Role
- Preconditions
- Test Data
- Steps
- Expected Result
- Risk Area or Acceptance Criteria Coverage
- Automation Candidate
- Notes if needed

## Scenario Separation

Use separate sections for:

- Happy Path Test Cases
- Edge Case Test Cases
- Negative Test Cases
- Permission and Session Test Cases
- Regression Candidates
- Automation Candidate Summary

## Good Expected Result Rule

Bad expected result:

The system works correctly.

Good expected result:

The user is redirected to the dashboard and the dashboard displays the logged-in user's full name.

## Automation Candidate Rules

Use:

- Yes
- No
- Later

Use "Yes" only when the test is stable, repeatable, deterministic, and useful for regression.

Use "Later" when the test is valuable but requires stable locators, test data, environment control, mocks, API hooks, or observability.

Use "No" when the test requires human judgment, unstable external systems, or destructive validation.

## Missing Information Rule

If key information is missing, do not guess.

List missing information using this format:

| Missing Item | Why Needed | Impact |
|---|---|---|

## Output Format

Use this structure when generating test cases:

# Test Case Design Output

## 1. Scope Summary

## 2. Assumptions

| Assumption | Reason |
|---|---|

## 3. Missing Information

| Missing Item | Why Needed | Impact |
|---|---|---|

## 4. Happy Path Test Cases

| ID | Title | Priority | Platform | User Role | Preconditions | Test Data | Steps | Expected Result | Acceptance Criteria Coverage | Automation Candidate | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|

## 5. Edge Case Test Cases

| ID | Title | Priority | Platform | User Role | Preconditions | Test Data | Steps | Expected Result | Risk Area | Automation Candidate | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|

## 6. Negative Test Cases

| ID | Title | Priority | Platform | User Role | Preconditions | Test Data | Steps | Expected Result | Risk Area | Automation Candidate | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|

## 7. Permission and Session Test Cases

| ID | Title | Priority | Platform | User Role | Preconditions | Steps | Expected Result | Risk Area | Automation Candidate |
|---|---|---|---|---|---|---|---|---|---|

## 8. Regression Candidates

| Test Case ID | Reason | Recommended Frequency |
|---|---|---|

## 9. Automation Candidate Summary

| Test Case ID | Automation Candidate | Reason | Recommended Tool |
|---|---|---|---|

## 10. Human Test Leader Notes

## References

Use these repository references when relevant:

- references/examples/test-case-examples.md
- references/anti-patterns/testing-anti-patterns.md
- .github/skills/test-case-design/SKILL.md
