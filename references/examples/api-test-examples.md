# API Test Examples

## Purpose

This document provides practical API testing examples for AI QA agents.

Use this reference when creating API validation plans, endpoint test scenarios, request validation checks, authentication checks, authorization checks, and API-DB consistency notes.

---

## 1. Good API Test Scenario Example

| ID | Type | Endpoint | Method | Priority | User Role | Preconditions | Request Data | Expected Status | Expected Response | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| API-LOGIN-001 | Valid Request | /api/auth/login | POST | P0 | Registered User | Active user exists | valid email and password | 200 OK | User object and token/session data are returned | Response must not expose password or sensitive fields |

### Why This Is Good

- Endpoint and method are clear.
- User role is defined.
- Preconditions are included.
- Request data is clear.
- Expected status is specific.
- Expected response is observable.
- Security note is included.

---

## 2. Bad API Test Scenario Example

| ID | Type | Endpoint | Method | Expected Result |
|---|---|---|---|---|
| API-001 | Test API | /login | POST | API works |

### Why This Is Bad

- Expected result is vague.
- User role is missing.
- Preconditions are missing.
- Request data is missing.
- Expected status is missing.
- Response expectation is not testable.
- Security and error behavior are ignored.

---

## 3. Missing Required Field Example

| ID | Type | Endpoint | Method | Priority | User Role | Preconditions | Request Data | Expected Status | Expected Response | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| API-PROFILE-002 | Missing Required Field | /api/profile | PATCH | P1 | Registered User | User is authenticated | name field missing | 400 or 422 | Validation error for name field | Exact status must be confirmed from API spec |

### Why This Is Good

- It identifies the missing field.
- It does not invent the exact status code.
- It clearly marks uncertainty.
- It expects field-level validation.

---

## 4. Authentication Example

| Scenario | Endpoint | Expected Status | Notes |
|---|---|---|---|
| No token | /api/me | 401 Unauthorized | Protected endpoint |
| Invalid token | /api/me | 401 Unauthorized | Token rejected |
| Expired token | /api/me | 401 Unauthorized | Expiry behavior |
| Valid token | /api/me | 200 OK | Current user returned |

### Good Practice

Protected endpoints should always include authentication checks.

Do not only test the valid token case.

---

## 5. Authorization Example

| User Role | Endpoint | Expected Access | Expected Status | Notes |
|---|---|---|---|---|
| Admin User | /api/admin/users | Allowed | 200 OK | Admin can view user list |
| Registered User | /api/admin/users | Denied | 403 Forbidden | Normal user must not access admin endpoint |
| Guest User | /api/admin/users | Denied | 401 Unauthorized | Guest has no token/session |

### Good Practice

Authorization testing must include wrong-role access.

Do not only check whether UI menu is hidden.

Direct API access must also be validated.

---

## 6. Safe Error Message Example

| ID | Scenario | Expected Behavior |
|---|---|---|
| API-LOGIN-NEG-001 | Wrong password | Generic invalid credentials error |
| API-LOGIN-NEG-002 | Unknown email | Same generic invalid credentials error |

### Why This Matters

If wrong password and unknown email return different messages, the API may allow account enumeration.

---

## 7. API-DB Consistency Example

| API Action | Expected API Response | Expected DB Change | DB Validation Needed |
|---|---|---|---|
| POST /api/users | 201 Created with user object | New user record exists | Yes |
| PATCH /api/profile | 200 OK with updated profile | User profile fields updated | Yes |
| DELETE /api/content/{id} | 204 No Content | Content is soft deleted or archived | Yes |
| Unauthorized PATCH request | 401 or 403 | No DB state change | Yes |

### Good Practice

State-changing API tests should mention database impact.

The API Test Agent should not perform DB validation directly, but it should recommend DB validation when needed.

---

## 8. Contract Risk Example

| Risk | Impact | Recommended Validation |
|---|---|---|
| API returns `name` but frontend expects `fullName` | Frontend display breaks | Contract/schema validation |
| API returns number as string | Client parsing issue | Field type validation |
| API removes required field | Breaking change | Required field check |
| API returns undocumented enum | UI state may break | Enum validation |

---

## 9. Pagination Example

| Scenario | Expected Behavior |
|---|---|
| page=1&pageSize=20 | First 20 records are returned |
| page=9999 | Empty list or valid out-of-range behavior |
| pageSize=100000 | Request is rejected or page size is capped |
| invalid page value | Validation error or default behavior based on spec |

---

## 10. API Test Quality Checklist

A good API test scenario should include:

- Endpoint
- Method
- Type
- Priority
- User role
- Preconditions
- Request data
- Expected status
- Expected response
- Auth expectation
- Authorization expectation when relevant
- DB impact when relevant
- Missing information when details are unknown
- No execution claim unless execution happened
