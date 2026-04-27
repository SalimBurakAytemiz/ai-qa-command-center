# Login Feature API Notes

## 1. Feature Name

User Login

---

## 2. API Overview

The login API authenticates users with email and password.

If credentials are valid and the user is active, the API returns authentication data.

If credentials are invalid, missing, or user status is not allowed, the API returns an error response.

---

## 3. Endpoints

| Endpoint | Method | Purpose | Auth Required | Roles |
|---|---|---|---|---|
| /api/auth/login | POST | Authenticate user | No | Guest |
| /api/auth/me | GET | Get current authenticated user | Yes | Registered User, Admin User |
| /api/auth/logout | POST | End authenticated session | Yes | Registered User, Admin User |

---

## 4. Request Details

| Endpoint | Required Fields | Optional Fields | Validation Rules |
|---|---|---|---|
| /api/auth/login | email, password | none | email must be valid format, password must not be empty |
| /api/auth/me | none | none | valid token/session required |
| /api/auth/logout | none | none | valid token/session required |

---

## 5. Response Details

| Endpoint | Success Status | Response Body | Notes |
|---|---|---|---|
| /api/auth/login | 200 OK | user object and token/session data | Role should be included or available through /me |
| /api/auth/me | 200 OK | current user object | Must not expose sensitive data |
| /api/auth/logout | 204 No Content | empty body | Session/token invalidated |

---

## 6. Error Responses

| Scenario | Expected Status | Expected Error | Notes |
|---|---|---|---|
| Missing email | 400 or 422 | Validation error | Exact status needs confirmation |
| Missing password | 400 or 422 | Validation error | Exact status needs confirmation |
| Invalid email format | 400 or 422 | Validation error | Exact status needs confirmation |
| Wrong password | 401 Unauthorized | Generic invalid credentials message | Must not reveal if email exists |
| Unknown email | 401 Unauthorized | Generic invalid credentials message | Must not reveal if email exists |
| Disabled user | 403 Forbidden or 401 Unauthorized | Access not allowed | Exact status needs confirmation |
| Missing token for /me | 401 Unauthorized | Unauthorized | Protected endpoint |
| Invalid token for /me | 401 Unauthorized | Unauthorized | Protected endpoint |

---

## 7. Authentication Rules

- Login endpoint does not require authentication.
- Protected endpoints require valid token or session.
- Token/session must be created after successful login.
- Logout should invalidate token or session if supported.

---

## 8. Authorization Rules

- Registered user can access user dashboard APIs.
- Admin user can access admin APIs.
- Normal registered user must not access admin APIs.
- Guest user must not access protected APIs.

---

## 9. Database Impact

Login may update:

- last_login_at
- failed_login_count if supported
- session table if server-side sessions are used
- refresh token table if refresh tokens are used

Exact schema needs confirmation.

---

## 10. Missing API Information

| Missing Item | Why Needed | Impact |
|---|---|---|
| Exact error status codes | Needed for API validation | Test expectations may be uncertain |
| Token/session mechanism | Needed for auth validation | Cannot fully validate session behavior |
| User response schema | Needed for contract validation | Frontend/backend mismatch risk |
| Disabled user response rule | Needed for negative case | Ambiguous security expectation |
