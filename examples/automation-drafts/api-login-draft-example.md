# API Login Draft Example

## Purpose

This document shows an example API automation draft for the login feature.

Important rule:

This is not an executed API test result.

It is a generated automation draft example only.

---

## 1. Automation Metadata

| Field | Value |
|---|---|
| Feature | User Login |
| Scenario ID | API-LOGIN-001 |
| Endpoint | /api/auth/login |
| Method | POST |
| Test Type | Smoke / Contract / Security |
| Priority | P1 |
| Automation Candidate Decision | Yes |
| Human Approval Required | Yes for production or real customer data |

---

## 2. Preconditions

- API environment is available.
- Login endpoint is confirmed.
- Valid synthetic test user exists.
- Response schema is confirmed or marked as Needs Confirmation.
- Credentials are stored in environment variables.

---

## 3. Draft API Test

~~~typescript
import { test, expect, request } from '@playwright/test';

test('login API accepts valid credentials', async () => {
  const baseURL = process.env.API_BASE_URL;
  const email = process.env.TEST_USER_EMAIL;
  const password = process.env.TEST_USER_PASSWORD;

  if (!baseURL || !email || !password) {
    throw new Error('Missing required environment variables.');
  }

  const api = await request.newContext({
    baseURL,
    extraHTTPHeaders: {
      'Content-Type': 'application/json'
    }
  });

  const response = await api.post('/api/auth/login', {
    data: {
      email,
      password
    }
  });

  expect(response.status()).toBe(200);

  const body = await response.json();

  expect(body).toBeTruthy();
  expect(JSON.stringify(body).toLowerCase()).not.toContain(password.toLowerCase());
});
~~~

---

## 4. Negative Case Extension Ideas

| Scenario | Expected Result |
|---|---|
| Missing password | 400 or 422 validation error |
| Invalid password | 401 unauthorized or generic auth failure |
| Disabled user | 401 or 403 depending on product rule |
| Unknown email | Generic login failure without account enumeration |

Exact status codes must be confirmed before strict assertions.

---

## 5. Generated vs Executed Note

This API automation output is a generated draft example.

It must not be reported as passed, verified, executed, or release-ready unless the test is actually run and execution evidence exists.
