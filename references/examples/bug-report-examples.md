# Bug Report Examples

## Purpose

This document provides practical bug report examples for AI QA agents.

Use this reference when creating bug report drafts, reviewing defect quality, or preparing Jira/Trello bug cards.

Important rule:

A generated bug report draft is not a confirmed bug unless there is real evidence from execution, logs, screenshots, videos, API responses, or DB validation.

---

## 1. Good Bug Report Example

## Title

Registered user is redirected to blank page after successful login

## Type

Bug Draft

## Severity

High

## Priority

P1

## Environment

| Field | Value |
|---|---|
| Platform | Web |
| Browser | Chrome |
| Environment | QA |
| Build | Needs Confirmation |
| User Role | Registered User |

## Preconditions

- Active registered user exists.
- Login page is available.
- QA environment is accessible.

## Steps to Reproduce

1. Open the login page.
2. Enter valid registered user email.
3. Enter valid password.
4. Click Login.

## Actual Result

User is redirected to a blank page after login.

## Expected Result

User should be redirected to the dashboard and the dashboard should display the logged-in user's full name.

## Evidence

- Screenshot: Required
- Video: Optional
- Console logs: Required if available
- Network response: Required if available

## Impact

Registered users may be blocked from accessing the product after successful login.

## Suggested Area

- Frontend routing
- Authentication callback
- Dashboard loading
- Session/token handling

## Notes

This bug should not be marked as confirmed until execution evidence is attached.

---

## 2. Bad Bug Report Example

## Title

Login broken

## Description

Login does not work.

## Why This Is Bad

- Title is vague.
- Environment is missing.
- User role is missing.
- Preconditions are missing.
- Steps are missing.
- Actual result is vague.
- Expected result is missing.
- Evidence is missing.
- Impact is unclear.

---

## 3. Good API Bug Draft Example

## Title

Login API returns 200 OK for disabled user credentials

## Type

Bug Draft

## Severity

Critical

## Priority

P0

## Environment

| Field | Value |
|---|---|
| Platform | API |
| Environment | QA |
| Endpoint | /api/auth/login |
| Method | POST |

## Preconditions

- Disabled user account exists.
- Disabled user has valid email and password.
- Login API is available.

## Request

| Field | Value |
|---|---|
| email | disabled.user@example.com |
| password | ValidPassword123 |

## Actual Result

API returns 200 OK and creates an authenticated session/token.

## Expected Result

API should reject login for disabled user and no authenticated session/token should be created.

## Evidence Needed

- Request payload
- Response status
- Response body
- Session/token evidence
- DB validation showing whether session/token was created

## Impact

Disabled users may gain access to protected areas.

## Notes

This is a security-sensitive issue and requires human review.

---

## 4. Good UI Bug Draft Example

## Title

Login error message reveals that email address exists

## Type

Bug Draft

## Severity

High

## Priority

P1

## Environment

| Field | Value |
|---|---|
| Platform | Web |
| Browser | Chrome |
| Environment | QA |
| User Role | Guest User |

## Preconditions

- Login page is available.
- Registered email exists.
- Unknown email does not exist.

## Steps to Reproduce

1. Open login page.
2. Enter existing email with wrong password.
3. Observe error message.
4. Enter unknown email with any password.
5. Observe error message.

## Actual Result

The system displays different error messages for existing email and unknown email.

## Expected Result

The system should display the same generic invalid credentials message in both cases.

## Impact

Different error messages may allow account enumeration.

## Evidence Needed

- Screenshot of both error messages
- Network response if available
- Timestamp and environment

---

## 5. Severity Guidance

| Severity | Meaning | Example |
|---|---|---|
| Critical | Blocks release or creates severe security/data/business risk | Unauthorized admin access |
| High | Major feature broken or important security risk | Valid users cannot log in |
| Medium | Important but non-blocking issue | Incorrect validation message |
| Low | Minor issue | Small copy or layout problem |

---

## 6. Priority Guidance

| Priority | Meaning | Example |
|---|---|---|
| P0 | Release blocker | Guest can access protected dashboard |
| P1 | Critical | Disabled user can log in |
| P2 | Important | Loading state missing |
| P3 | Low | Minor UI alignment issue |

---

## 7. Bug Report Quality Checklist

A good bug report should include:

- Clear title
- Environment
- User role
- Preconditions
- Steps to reproduce
- Actual result
- Expected result
- Evidence
- Severity
- Priority
- Impact
- Human review needs
- No unsupported execution claims
