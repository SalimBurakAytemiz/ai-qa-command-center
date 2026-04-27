# Sample Edge and Negative Test Cases

## 1. Scope Summary

This sample demonstrates how edge case and negative case outputs should be structured.

Edge cases validate unusual but possible behavior.

Negative cases validate rejected, invalid, unauthorized, or failure behavior.

These are sample test cases only. They are not executed results.

---

## 2. Edge Case Test Cases

| ID | Title | Priority | Platform | User Role | Preconditions | Test Data | Steps | Expected Result | Risk Area | Automation Candidate | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| TC-SAMPLE-EDGE-001 | Verify maximum allowed input length is handled correctly | P2 | Web | Registered User | Feature form is available | Maximum allowed text length | 1. Open form 2. Enter max length value 3. Submit | Value is accepted or validation is shown according to rule | Boundary | Yes | Exact max length must be confirmed |
| TC-SAMPLE-EDGE-002 | Verify duplicate submit is prevented | P2 | Web | Registered User | Submit action available | Valid form data | 1. Fill valid data 2. Click submit repeatedly | Duplicate records or duplicate actions are not created | Duplicate action | Later | Requires API or DB validation |
| TC-SAMPLE-EDGE-003 | Verify empty result state is displayed | P3 | Web | Registered User | No records exist | Empty dataset | 1. Open feature list page | Empty state message is displayed clearly | Empty state | Yes | UI copy must be confirmed |

---

## 3. Negative Test Cases

| ID | Title | Priority | Platform | User Role | Preconditions | Test Data | Steps | Expected Result | Risk Area | Automation Candidate | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| TC-SAMPLE-NEG-001 | Verify required field validation | P1 | Web | Registered User | Feature form is available | Missing required field | 1. Open form 2. Leave required field empty 3. Submit | Submission is blocked and validation message is displayed | Form validation | Yes | Exact message may need confirmation |
| TC-SAMPLE-NEG-002 | Verify unauthorized user cannot access restricted feature | P0 | Web | Guest User | User is not logged in | Restricted feature URL | 1. Navigate directly to restricted URL | Access is denied or user is redirected to login | Authorization | Yes | Critical permission boundary |
| TC-SAMPLE-NEG-003 | Verify invalid API payload is rejected | P1 | API | Registered User | API is available | Invalid payload | 1. Send invalid request payload | API returns validation error and no state change occurs | API validation | Yes | Status code must be confirmed |
| TC-SAMPLE-NEG-004 | Verify wrong role cannot perform admin action | P0 | Admin Panel / API | Registered User | Registered user exists without admin permission | Normal user credentials | 1. Attempt admin action | Action is rejected and no data is changed | Authorization | Yes | Must test direct access, not only hidden UI |

---

## 4. Permission and Session Cases

| ID | Title | Priority | Platform | User Role | Preconditions | Steps | Expected Result | Risk Area | Automation Candidate |
|---|---|---|---|---|---|---|---|---|---|
| TC-SAMPLE-PERM-001 | Verify expired session cannot access protected feature | P1 | Web / API | Registered User | Session is expired | Attempt protected action | User is rejected and asked to authenticate again | Session management | Later |
| TC-SAMPLE-PERM-002 | Verify direct URL access respects permissions | P0 | Web | Unauthorized User | User lacks required permission | Open restricted URL directly | Access is denied | Authorization | Yes |

---

## 5. Quality Notes

Edge and negative case outputs should not be mixed with happy path outputs.

Every negative case must have a clear rejected behavior.
