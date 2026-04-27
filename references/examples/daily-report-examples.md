# Daily Report Examples

## Purpose

This document provides practical daily QA report examples for AI QA agents.

Use this reference when creating daily quality reports, management summaries, blocker summaries, or generated QA package summaries.

Important rule:

Generated planning artifacts must not be reported as executed test results.

---

## 1. Good Daily Quality Report Example

# Daily Quality Report

## 1. Date

2026-04-27

## 2. Overall Status

Yellow

## 3. Executive Summary

The QA team generated planning artifacts for the login feature.

Generated outputs include product testing context, test strategy, test plan, happy path test cases, edge and negative test cases, API validation plan, DB validation plan, and Jira/Trello drafts.

No tests have been executed yet.

The current status is Yellow because API status codes, DB schema, dashboard routes, and token/session mechanism still need confirmation.

## 4. Work Completed Today

| Area | Output | Status | Notes |
|---|---|---|---|
| Product Analysis | Product testing context | Generated | Ready for human review |
| Strategy | Test strategy | Generated | Risk-based scope prepared |
| Planning | Test plan | Generated | Execution not started |
| Test Cases | Happy path and negative cases | Generated | Review required |
| API | API validation plan | Generated | Some statuses need confirmation |
| DB | DB validation plan | Generated | Schema needs confirmation |
| Work Tracking | Jira/Trello drafts | Drafted | Human approval required |

## 5. Test Case Generation Summary

| Type | Count | Notes |
|---|---:|---|
| Happy Path | 5 | Includes registered and admin login |
| Edge Case | 3 | Includes duplicate submit and mobile usability |
| Negative Case | 7 | Includes invalid credentials and disabled user |
| Permission / Session | 3 | Includes direct access and session checks |

## 6. Critical Risks

| Risk | Priority | Impact | Recommended Action |
|---|---|---|---|
| Guest can access dashboard directly | P0 | Unauthorized access | Execute direct URL access test |
| Session/token behavior unclear | P0 | Auth state may be invalid | Confirm auth mechanism |
| Disabled user behavior unclear | P1 | Access control risk | Confirm expected API and DB behavior |
| Error message safety not confirmed | P1 | Account enumeration risk | Confirm generic error copy |

## 7. Blockers

| Blocker | Type | Impact | Required Action |
|---|---|---|---|
| Exact API statuses unknown | Requirement gap | API validation not precise | Backend owner confirmation |
| Exact DB schema unknown | Technical gap | DB validation remains entity-level | DB/schema confirmation |
| Dashboard routes unknown | Requirement gap | Redirect validation is generic | Frontend/product confirmation |

## 8. Items Needing Human Review

| Item | Reason | Recommended Decision |
|---|---|---|
| P0 dashboard access risk | Security boundary | Confirm priority |
| Jira/Trello drafts | External action | Approve before creation |
| Missing API status codes | Requirement gap | Request clarification |
| DB validation scope | Technical gap | Confirm safe DB access |

## 9. Recommended Next Actions

| Action | Owner | Priority |
|---|---|---|
| Review generated QA package | Human Test Leader | P1 |
| Confirm API behavior | Backend/API Owner | P1 |
| Confirm dashboard routes | Frontend/Product Owner | P2 |
| Confirm DB schema | Backend/DB Owner | P2 |
| Decide execution plan | Human Test Leader | P1 |

## 10. Human Test Leader Notes

This report summarizes generated planning artifacts only.

No manual or automated execution has occurred.

---

## 2. Bad Daily Report Example

## Summary

Login testing is done. Everything looks good.

## Why This Is Bad

- Claims testing is done without evidence.
- No generated vs executed distinction.
- No risks.
- No blockers.
- No missing information.
- No next actions.
- No human approval points.
- No test case summary.
- No management-readable detail.

---

## 3. Good Status Examples

## Green Example

Use Green only when:

- No major blockers exist.
- No critical risks are open.
- Required outputs are reviewed.
- Remaining work is low-risk.

## Yellow Example

Use Yellow when:

- Some requirements are missing.
- Some API or DB details need confirmation.
- Generated outputs need review.
- Execution has not started.
- There are manageable risks.

## Red Example

Use Red when:

- Environment is down.
- Critical security risk exists.
- Release-impacting blocker exists.
- Required test data is missing.
- P0 risk needs urgent human decision.

---

## 4. Correct Reporting Language

Correct:

- Test plan generated
- Test cases generated
- API validation plan prepared
- DB validation plan prepared
- Output reviewed
- Execution blocked
- Human approval required

Incorrect without execution evidence:

- Tests passed
- Feature verified
- Execution completed
- Tested successfully
- Release ready

---

## 5. Daily Report Quality Checklist

A good daily QA report should include:

- Date
- Overall status
- Executive summary
- Work completed
- Test case generation summary
- Coverage areas
- Risks
- Blockers
- Human review needs
- Recommended next actions
- Generated vs executed distinction
- No false release readiness claim
