# API Testing Patterns

## Purpose

This document defines practical API testing patterns for AI QA agents.

Use this reference when designing API validation plans, API test cases, contract checks, authentication checks, authorization checks, and API-DB consistency reviews.

---

## 1. Basic Endpoint Coverage Pattern

For each endpoint, identify:

- Endpoint path
- HTTP method
- Purpose
- Authentication requirement
- Authorized roles
- Required request fields
- Optional request fields
- Expected success status
- Expected error statuses
- Response schema
- DB impact if any
- Integration dependencies if any

## Example

| Endpoint | Method | Purpose | Auth Required | Roles | Expected Success |
|---|---|---|---|---|---|
| /api/profile | PATCH | Update user profile | Yes | Registered User | 200 OK |

---

## 2. Valid Request Pattern

A valid request scenario checks the expected successful behavior.

### Example

| ID | Type | Endpoint | Method | User Role | Request Data | Expected Status | Expected Response |
|---|---|---|---|---|---|---|---|
| API-PROFILE-001 | Valid Request | /api/profile | PATCH | Registered User | Valid name and phone | 200 OK | Updated profile object is returned |

### Rules

- Use realistic valid data.
- Include required auth.
- Verify response body.
- Mention DB impact when state changes.

---

## 3. Missing Required Field Pattern

### Example

| ID | Type | Endpoint | Method | Request Data | Expected Status | Expected Response |
|---|---|---|---|---|---|---|
| API-PROFILE-002 | Missing Required Field | /api/profile | PATCH | Name field missing | 400 or 422 | Validation error for name field |

### Rules

- Do not guess exact status if not specified.
- Use "Needs Confirmation" if the API spec does not define it.
- Expected error should include field-level detail when available.

---

## 4. Invalid Data Type Pattern

### Example

| ID | Type | Endpoint | Method | Request Data | Expected Status | Expected Response |
|---|---|---|---|---|---|---|
| API-PROFILE-003 | Invalid Field Type | /api/profile | PATCH | phone as object instead of string | 400 or 422 | Validation error for phone field |

### Rules

- Test invalid strings, numbers, booleans, objects, arrays, dates and IDs when relevant.
- Focus on business-critical fields.

---

## 5. Authentication Pattern

For protected endpoints, always test:

| Scenario | Expected Result |
|---|---|
| No token | 401 Unauthorized |
| Invalid token | 401 Unauthorized |
| Expired token | 401 Unauthorized or token refresh behavior |
| Valid token | Request is processed |
| Logged out token | 401 Unauthorized |

### Rule

If authentication behavior is not documented, list it under Missing Information.

---

## 6. Authorization Pattern

For role-based systems, test:

| Scenario | Expected Result |
|---|---|
| Correct role accesses endpoint | Allowed |
| Lower role accesses endpoint | Forbidden |
| User accesses another user's data | Forbidden or Not Found |
| Admin accesses admin endpoint | Allowed |
| Normal user accesses admin endpoint | Forbidden |

### Example

| ID | Type | Endpoint | User Role | Expected Status | Notes |
|---|---|---|---|---|---|
| API-ADMIN-001 | Authorization | /api/admin/users | Registered User | 403 Forbidden | Normal user must not access admin user list |

---

## 7. Pagination Pattern

When endpoint returns a list, test:

- Default page
- Specific page
- Page size
- Maximum page size
- Empty result page
- Invalid page number
- Invalid page size

### Example

| Scenario | Expected Behavior |
|---|---|
| page=1&pageSize=20 | Returns first 20 records |
| page=9999 | Returns empty list or valid not found behavior |
| pageSize=100000 | Rejects or caps page size |

---

## 8. Sorting Pattern

Test:

- Ascending sort
- Descending sort
- Invalid sort field
- Multiple sort fields if supported

### Example

| Scenario | Expected Behavior |
|---|---|
| sort=createdAt:desc | Records sorted newest first |
| sort=unknownField | Validation error or ignored based on spec |

---

## 9. Filtering Pattern

Test:

- Valid filter
- Invalid filter value
- Multiple filters
- Empty result
- Role-limited filtered result

### Example

| Scenario | Expected Behavior |
|---|---|
| status=active | Only active records returned |
| status=invalid | Validation error or empty result based on spec |

---

## 10. State-Changing API Pattern

For POST, PUT, PATCH, DELETE:

Always identify:

- Before state
- Request action
- Expected response
- Expected database state
- Audit or timestamp impact
- Duplicate or retry risk

### Example

| API Action | Expected API Response | Expected DB State |
|---|---|---|
| PATCH /api/profile | 200 OK with updated profile | User name updated and updated_at changed |

---

## 11. Idempotency Pattern

For operations that may be retried:

Test:

- Same request sent once
- Same request sent twice
- Retry after timeout
- Duplicate request with same idempotency key if supported

### Risk

Without idempotency, duplicate records or duplicate actions may occur.

---

## 12. Error Handling Pattern

For error cases, check:

- Status code
- Error message
- Error code
- Field-level details
- No sensitive data leaked
- Consistent error structure

### Bad

```json
{
  "error": "Something went wrong"
}