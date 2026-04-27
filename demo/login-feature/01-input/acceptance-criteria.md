# Login Feature Acceptance Criteria

## Feature Name

User Login

---

## Acceptance Criteria

| ID | Criteria | Priority | User Role | Platform | Notes |
|---|---|---|---|---|---|
| AC-LOGIN-001 | Registered user can log in with valid email and password and is redirected to the user dashboard. | P0 | Registered User | Web / Mobile Web | Dashboard must display user full name. |
| AC-LOGIN-002 | Admin user can log in with valid credentials and is redirected to the admin dashboard. | P1 | Admin User | Web / Admin Panel | Admin must not land on normal user dashboard. |
| AC-LOGIN-003 | Login is rejected when password is invalid. | P1 | Registered User | Web / Mobile Web | User remains on login page. |
| AC-LOGIN-004 | Login is rejected when email is not registered. | P1 | Guest User | Web / Mobile Web | Error message must be safe and generic. |
| AC-LOGIN-005 | Login button is disabled or validation is shown when required fields are empty. | P2 | Guest User | Web / Mobile Web | Email and password are required. |
| AC-LOGIN-006 | Disabled user cannot log in even with correct credentials. | P1 | Disabled User | Web / Mobile Web | Access must be rejected. |
| AC-LOGIN-007 | Guest user cannot access dashboard directly without authentication. | P0 | Guest User | Web / Mobile Web | User should be redirected to login page. |
| AC-LOGIN-008 | Successful login creates a valid authenticated session or token. | P0 | Registered User | API / Backend | Session/token must be usable for protected APIs. |
| AC-LOGIN-009 | Login error message must not reveal whether the email exists. | P1 | Guest User | Web / API | Prevent account enumeration. |
| AC-LOGIN-010 | Login page must show loading state while authentication request is in progress. | P3 | Guest User | Web / Mobile Web | Prevent duplicate submission. |

---

## Notes

Acceptance criteria are written for planning and test design.

They are not executed results.
