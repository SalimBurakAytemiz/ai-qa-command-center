# Login Feature Edge and Negative Test Cases

## 1. Scope Summary

These test cases validate invalid login behavior, required field validation, disabled user access, direct protected page access, and safe error handling.

These test cases are generated planning artifacts only. They are not executed test results.

---

## 2. Edge Case Test Cases

| ID | Title | Priority | Platform | User Role | Preconditions | Test Data | Steps | Expected Result | Risk Area | Automation Candidate | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| TC-LOGIN-EDGE-001 | Verify login form handles email with uppercase characters | P3 | Web | Guest User | Login page is available | USER@EXAMPLE.COM with valid password | 1. Open login page 2. Enter uppercase email 3. Enter valid password 4. Click Login | System handles email according to product rule and does not break validation | Input normalization | Later | Expected behavior needs confirmation |
| TC-LOGIN-EDGE-002 | Verify duplicate login submit is prevented during loading | P2 | Web | Guest User | Login API response delay can be simulated | valid credentials | 1. Enter valid credentials 2. Click Login repeatedly while loading | Duplicate submission is prevented and only one login request should be processed | Duplicate request | Later | Requires network/control setup |
| TC-LOGIN-EDGE-003 | Verify mobile web keyboard does not hide login button | P3 | Mobile Web | Guest User | Mobile viewport available | valid credentials | 1. Open login page on mobile viewport 2. Focus password field | Login button remains reachable or page can scroll correctly | Mobile usability | No | Manual review may be better |

---

## 3. Negative Test Cases

| ID | Title | Priority | Platform | User Role | Preconditions | Test Data | Steps | Expected Result | Risk Area | Automation Candidate | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| TC-LOGIN-NEG-001 | Verify login is rejected with invalid password | P1 | Web | Registered User | Active registered user exists | valid email and wrong password | 1. Open login page 2. Enter valid email 3. Enter wrong password 4. Click Login | User remains on login page and generic invalid credentials message is displayed | Authentication | Yes | Must not reveal account state |
| TC-LOGIN-NEG-002 | Verify login is rejected for unknown email | P1 | Web | Guest User | Login page is available | unknown email and any password | 1. Open login page 2. Enter unknown email 3. Enter password 4. Click Login | User remains on login page and generic invalid credentials message is displayed | Account enumeration | Yes | Message should match invalid password case |
| TC-LOGIN-NEG-003 | Verify empty email validation | P2 | Web | Guest User | Login page is available | empty email and valid password | 1. Open login page 2. Leave email empty 3. Enter password 4. Click Login | Login is not submitted or validation error is shown for email | Form validation | Yes | Exact copy needs confirmation |
| TC-LOGIN-NEG-004 | Verify empty password validation | P2 | Web | Guest User | Login page is available | valid email and empty password | 1. Open login page 2. Enter email 3. Leave password empty 4. Click Login | Login is not submitted or validation error is shown for password | Form validation | Yes | Exact copy needs confirmation |
| TC-LOGIN-NEG-005 | Verify invalid email format validation | P2 | Web | Guest User | Login page is available | invalid email format and password | 1. Open login page 2. Enter invalid email format 3. Enter password 4. Click Login | Validation error is shown or API rejects request with validation error | Input validation | Yes | UI/API behavior needs confirmation |
| TC-LOGIN-NEG-006 | Verify disabled user cannot log in | P1 | Web / API | Disabled User | Disabled user account exists | disabled user email and correct password | 1. Open login page 2. Enter disabled user credentials 3. Click Login | Login is rejected and no authenticated session/token is created | Authorization | Later | Requires disabled test user |
| TC-LOGIN-NEG-007 | Verify guest cannot access dashboard directly | P0 | Web | Guest User | User is not logged in | dashboard URL | 1. Open dashboard URL directly without login | User is redirected to login page or receives unauthorized access page | Access control | Yes | Critical security boundary |

---

## 4. Permission and Session Test Cases

| ID | Title | Priority | Platform | User Role | Preconditions | Steps | Expected Result | Risk Area | Automation Candidate |
|---|---|---|---|---|---|---|---|---|---|
| TC-LOGIN-PERM-001 | Verify registered user cannot access admin dashboard | P0 | Web / Admin Panel | Registered User | Registered user is logged in | Navigate directly to admin dashboard URL | Access is denied or user is redirected to allowed area | Authorization | Yes |
| TC-LOGIN-SESSION-001 | Verify protected API rejects missing token/session | P1 | API | Guest User | No active token/session | Call current user endpoint | API returns unauthorized response | Authentication | Yes |
| TC-LOGIN-SESSION-002 | Verify logout invalidates session/token if supported | P2 | Web / API | Registered User | User is logged in | Logout and try to access protected page/API | Access is rejected after logout | Session management | Later |

---

## 5. Missing Information

| Missing Item | Why Needed | Impact |
|---|---|---|
| Exact validation message copy | Needed for precise UI assertions | Some expected results remain generic |
| Exact dashboard URLs | Needed for redirect validation | Direct URL tests need confirmed paths |
| Account lockout rules | Needed for repeated failed login cases | Not covered in this demo |
| Disabled user API status | Needed for API negative test | Expected status uncertain |
