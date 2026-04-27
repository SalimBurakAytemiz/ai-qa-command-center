# Jira Ticket Examples

## Purpose

This document provides practical Jira ticket and Trello card examples for AI QA agents.

Use this reference when creating work-tracking drafts.

Important rule:

Generated Jira/Trello drafts are not created tickets.

Human approval is required before creating external tickets or cards.

---

## 1. Good QA Task Example

## Title

Prepare login feature test plan

## Issue Type

Task

## Priority

P1

## Description

Create a risk-based test plan for the login feature.

The test plan should cover registered user login, admin login, invalid credentials, disabled user rejection, direct protected page access, API validation, DB validation, and UI states.

## Scope

- Web login
- Mobile web login
- Admin redirection
- Login API
- Current user API
- Session/token behavior
- Entity-level DB validation

## Acceptance Criteria

- Test plan includes scope and out-of-scope areas.
- Test plan includes entry and exit criteria.
- Test plan includes test data requirements.
- Test plan includes risks and blockers.
- Test plan does not report generated work as executed testing.

## Notes

This is a draft and requires human approval before creation.

---

## 2. Good Bug Ticket Example

## Title

Guest user can access dashboard directly without authentication

## Issue Type

Bug

## Priority

P0

## Severity

Critical

## Description

A guest user can access a protected dashboard URL without logging in.

This creates an unauthorized access risk.

## Preconditions

- User is not logged in.
- Dashboard URL is known.
- QA environment is accessible.

## Steps to Reproduce

1. Open a new browser session.
2. Ensure no user is logged in.
3. Navigate directly to the dashboard URL.

## Actual Result

Dashboard page is accessible.

## Expected Result

User should be redirected to the login page or receive an unauthorized access message.

## Impact

Unauthorized users may access protected user data or product functionality.

## Evidence Required

- Screenshot
- Video if possible
- Network response if available
- Environment and build information

## Human Approval

Required because this is a P0 security-sensitive bug.

---

## 3. Good Risk Ticket Example

## Title

Confirm login API error status codes before API execution

## Issue Type

Risk / Clarification

## Priority

P2

## Description

The login API validation plan requires exact error status codes for validation errors, invalid credentials, disabled users, and unauthorized access.

Current expectations include possible 400, 401, 403, or 422 responses, but the specification does not confirm exact behavior.

## Required Clarification

| Scenario | Needed Information |
|---|---|
| Missing email | Expected status code |
| Missing password | Expected status code |
| Invalid email format | Expected status code |
| Wrong password | Expected status code |
| Disabled user | Expected status code |
| Missing token | Expected status code |

## Impact

Without confirmation, API tests may use uncertain expected results.

## Acceptance Criteria

- Backend/API owner confirms expected status codes.
- API validation plan is updated.
- Negative API scenarios are no longer marked as Needs Confirmation.

---

## 4. Good Trello Card Example

## Card Title

Login QA - Generate edge and negative test cases

## List

QA To Do

## Priority

P1

## Description

Generate edge and negative test cases for the login feature.

Include invalid credentials, unknown email, empty required fields, invalid email format, disabled user, direct dashboard access, and wrong-role access.

## Checklist

- Invalid password case added
- Unknown email case added
- Empty email validation added
- Empty password validation added
- Disabled user case added
- Direct dashboard access case added
- Registered user admin access case added
- Human review completed

## Notes

Generated test cases are planning artifacts only.

---

## 5. Bad Jira Ticket Example

## Title

Fix login

## Description

Login has problems.

## Why This Is Bad

- Too vague
- No issue type
- No priority
- No environment
- No steps
- No expected result
- No evidence
- No owner or acceptance criteria
- Not actionable

---

## 6. Ticket Quality Checklist

A good Jira or Trello draft should include:

- Clear title
- Issue type
- Priority
- Description
- Scope
- Preconditions if relevant
- Steps if it is a bug
- Actual result if it is a bug
- Expected result if it is a bug
- Acceptance criteria
- Evidence requirements
- Human approval needs
- No false execution claims
