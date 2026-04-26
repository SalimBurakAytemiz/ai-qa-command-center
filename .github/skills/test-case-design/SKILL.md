# Skill: Test Case Design

## Purpose

Use this skill when designing test cases from product context, feature descriptions, user stories, acceptance criteria, business rules, or QA requirements.

This skill helps the AI generate structured, useful, executable, and risk-aware test cases.

## When To Use This Skill

Use this skill when the task includes:

- Creating test cases
- Reviewing test cases
- Splitting happy path, edge case, and negative case scenarios
- Mapping test cases to acceptance criteria
- Identifying missing test coverage
- Preparing regression candidates
- Creating manual test scenarios
- Preparing automation candidate lists

## Required Inputs

Before generating test cases, collect as much of the following as possible:

- Feature name
- Feature purpose
- Acceptance criteria
- User roles
- Supported platforms
- Business rules
- Preconditions
- Test data requirements
- Known risks
- Expected behavior
- Error behavior
- API or DB impact if relevant

If any important input is missing, list it under "Missing Information".

## Core Rules

### Rule 1: Separate Test Types

Do not mix happy path, edge case, and negative case scenarios.

Use separate sections for:

- Happy Path Test Cases
- Edge Case Test Cases
- Negative Test Cases
- Permission and Session Test Cases
- Regression Candidates

### Rule 2: Use Clear Expected Results

Expected results must be specific, observable, and testable.

Bad:

The system works correctly.

Good:

The user is redirected to the dashboard and the dashboard displays the logged-in user's full name.

### Rule 3: Include Preconditions

Every test case must define preconditions.

Examples:

- User exists
- User is logged in
- User has the required role
- Feature flag is enabled
- API is available
- Database is reachable
- Test data exists

### Rule 4: Include Test Data

Every test case should define required test data.

Examples:

- Valid registered user
- Admin user
- Invalid email address
- Expired token
- Existing CMS content
- User without permission

### Rule 5: Include User Role and Platform

Every test case must include:

- User role
- Platform

If unknown, mark it under "Missing Information".

### Rule 6: Do Not Claim Execution

Generated test cases are not executed results.

Correct wording:

- Test cases generated
- Test cases planned
- Test cases reviewed

Incorrect wording:

- Tests passed
- Feature passed testing
- Execution completed

Only use execution language if real execution evidence exists.

### Rule 7: Mark Automation Candidate Realistically

Use:

- Yes
- No
- Later

Use "Yes" only when the case is stable, repeatable, deterministic, and useful for regression.

Use "Later" when the case needs stable locators, test data, environment control, mocks, or observability.

Use "No" when the case requires human judgment, unstable external systems, or destructive validation.

### Rule 8: Avoid Duplicates

Do not create multiple test cases that verify the same behavior unless there is a meaningful difference in:

- User role
- Platform
- Risk
- Business rule
- Technical layer

## Test Case Priority Rules

Use:

- P0: Release blocker
- P1: Critical
- P2: Important
- P3: Low priority

### P0

Use P0 only when failure blocks release or creates severe business, security, data, or user-impacting risk.

Examples:

- Login completely broken
- Critical payment flow broken
- Data corruption
- Unauthorized access to sensitive data
- App crashes on launch

### P1

Use P1 for critical issues with possible workaround or limited scope.

Examples:

- Main feature partially broken
- Important API validation missing
- Critical mobile flow fails on one major device
- Notification missing for important flow

### P2

Use P2 for important but non-blocking issues.

Examples:

- Secondary flow issue
- Medium-risk edge case
- Non-critical role-specific behavior
- Moderate UI state problem

### P3

Use P3 for low-risk issues.

Examples:

- Minor copy issue
- Low-impact visual alignment
- Optional flow issue
- Cosmetic issue

## Output Format

Use this format:

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

When needed, use:

- `references/anti-patterns/testing-anti-patterns.md`
- `references/examples/test-case-examples.md`
- `08-skills/test-case-design/README.md`

## Quality Checklist

Before finalizing, check:

- Are test types separated?
- Are expected results observable?
- Are preconditions clear?
- Is test data defined?
- Are priorities reasonable?
- Are user roles included?
- Are platforms included?
- Are missing items listed?
- Are automation candidates realistic?
- Are duplicate cases avoided?
- Is execution language avoided unless real execution happened?