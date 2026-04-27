# Sample Test Plan

## 1. Scope Summary

This sample test plan demonstrates the expected structure for feature-level QA planning outputs.

This is a sample planning artifact. It is not an executed test result.

---

## 2. Feature Under Test

| Field | Value |
|---|---|
| Product | Sample Product |
| Feature | Sample Feature |
| Platform | Web / API / Database |
| Status | Draft |
| Owner | Human Test Leader |

---

## 3. Testing Objectives

| Objective | Priority | Notes |
|---|---|---|
| Validate primary happy path | P0 | Critical user journey |
| Validate invalid input handling | P1 | Negative behavior |
| Validate role-based access | P1 | Permission boundary |
| Validate API response behavior | P1 | Backend contract |
| Validate database state change | P2 | Data consistency |

---

## 4. In Scope

- Functional validation
- Happy path testing
- Edge case testing
- Negative testing
- API validation planning
- Database validation planning
- Role-based access checks
- Basic regression candidates

---

## 5. Out of Scope

- Performance testing
- Security penetration testing
- Native mobile testing
- Visual regression
- Production data validation
- Release go/no-go decision

---

## 6. Entry Criteria

| Criteria | Status | Notes |
|---|---|---|
| Feature requirements available | Draft | Human review needed |
| Acceptance criteria available | Draft | May need clarification |
| Test environment available | Unknown | Must be confirmed |
| Test data available | Unknown | Must be prepared |
| API specification available | Unknown | Must be confirmed |

---

## 7. Exit Criteria

| Criteria | Status | Notes |
|---|---|---|
| Test plan generated | Completed | Planning artifact only |
| Test cases generated | Pending | Requires agent output |
| API validation plan generated | Pending | Requires API details |
| DB validation plan generated | Pending | Requires schema details |
| Output reviewed | Pending | Output Reviewer Agent required |

---

## 8. Test Areas

| Area | Required | Priority | Notes |
|---|---|---|---|
| Web Functional | Yes | P1 | Visible user behavior |
| API | Yes | P1 | Endpoint behavior |
| Database | Yes | P2 | State consistency |
| Permissions | Yes | P1 | Role checks |
| Reporting | Yes | P2 | Summary output |

---

## 9. Risks

| Risk | Priority | Impact | Recommended Mitigation |
|---|---|---|---|
| Missing acceptance criteria | P1 | Test expectations unclear | Request clarification |
| Unknown API behavior | P1 | API tests may be inaccurate | Confirm API spec |
| Unknown DB schema | P2 | DB validation remains high-level | Confirm schema |
| Role rules unclear | P1 | Permission tests incomplete | Confirm roles |

---

## 10. Human Approval Points

| Item | Reason |
|---|---|
| P0/P1 priority assignment | Human QA leader approval required |
| External ticket creation | Human approval required |
| Release readiness | Execution has not happened |
| Production data usage | Not allowed without approval |

---

## 11. Final Note

This sample shows the expected structure of a generated test plan.

It must not be reported as executed testing.
