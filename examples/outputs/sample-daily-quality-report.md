# Sample Daily Quality Report

## 1. Date

YYYY-MM-DD

---

## 2. Overall Status

Status: Yellow

Use one of:

- Green
- Yellow
- Red

---

## 3. Executive Summary

The AI QA Command Center generated planning artifacts for the selected feature.

Generated outputs include test planning, test case design, API validation planning, DB validation planning, risk notes, and work-tracking drafts.

No test execution has occurred unless explicitly stated with evidence.

---

## 4. Work Completed Today

| Area | Output | Status | Notes |
|---|---|---|---|
| Product Analysis | Product testing context | Generated | Needs human review |
| Strategy | Test strategy | Generated | Risk-based scope prepared |
| Planning | Test plan | Generated | Execution not started |
| Test Cases | Happy path / edge / negative | Generated | Review required |
| API | API validation plan | Generated | Missing API info documented |
| DB | DB validation plan | Generated | Schema gaps documented |
| Work Tracking | Jira/Trello drafts | Drafted | Human approval required |

---

## 5. Test Case Generation Summary

| Type | Count | Notes |
|---|---:|---|
| Happy Path | 0 | Replace with actual generated count |
| Edge Case | 0 | Replace with actual generated count |
| Negative Case | 0 | Replace with actual generated count |
| Permission / Session | 0 | Replace with actual generated count |
| API Scenarios | 0 | Replace with actual generated count |
| DB Scenarios | 0 | Replace with actual generated count |

---

## 6. Areas Covered

| Area | Coverage Status | Notes |
|---|---|---|
| Product behavior | Planned | Based on available requirements |
| Web UI | Planned | Needs UI confirmation |
| API | Planned | Needs API contract confirmation |
| Database | Planned | Needs schema confirmation |
| Permissions | Planned | Needs role confirmation |
| Reporting | Planned | Draft report generated |

---

## 7. Critical Risks

| Risk | Priority | Impact | Recommended Action |
|---|---|---|---|
| Missing acceptance criteria | P1 | Test scope unclear | Request product clarification |
| Unknown API contract | P1 | API validation uncertain | Request API documentation |
| Unknown DB schema | P2 | DB validation high-level | Request schema details |
| Permission rules unclear | P1 | Security coverage incomplete | Confirm access matrix |

---

## 8. Blockers

| Blocker | Type | Impact | Required Action |
|---|---|---|---|
| Test environment unavailable | Environment | Execution cannot start | Provide environment URL |
| Test users missing | Test data | Login/role tests blocked | Create synthetic users |
| API documentation missing | Requirement gap | API validation incomplete | Provide API spec |
| DB access unavailable | Technical gap | DB validation cannot execute | Provide safe test DB access |

---

## 9. Items Needing Human Review

| Item | Reason | Recommended Decision |
|---|---|---|
| P0/P1 risks | Human approval required | Confirm or adjust priority |
| Jira/Trello drafts | External action | Approve before creation |
| Missing requirements | Scope risk | Request clarification |
| Release readiness | No execution evidence | Do not mark release-ready |

---

## 10. Recommended Next Actions

| Action | Owner | Priority |
|---|---|---|
| Review generated outputs | Human Test Leader | P1 |
| Confirm missing requirements | Product Owner | P1 |
| Confirm API behavior | Backend/API Owner | P1 |
| Confirm DB schema | Backend/DB Owner | P2 |
| Prepare execution plan | QA Engineer | P1 |

---

## 11. Final Note

This report separates generated planning work from executed testing.

Do not report the feature as passed, verified, tested successfully, or release-ready unless actual execution evidence exists.
