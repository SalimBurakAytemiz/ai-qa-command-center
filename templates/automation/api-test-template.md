# API Test Automation Template

## Purpose

Use this template when preparing API automation drafts from approved API validation scenarios.

Important rule:

Generated API tests are automation drafts only.

They are not executed API test results unless the tests are actually run and execution evidence exists.

---

## 1. Automation Metadata

| Field | Value |
|---|---|
| Feature | |
| Scenario ID | |
| Endpoint | |
| Method | GET / POST / PUT / PATCH / DELETE |
| Test Type | Smoke / Regression / Contract / Security / Negative |
| Priority | P0 / P1 / P2 / P3 |
| Source API Scenario | |
| Automation Candidate Decision | Yes / Later |
| Human Approval Required | If sensitive, destructive, production-related, or external-impacting |

---

## 2. Preconditions

List required setup before the API test can run.

Examples:

- API environment is available.
- Required test user exists.
- Auth token can be created safely.
- Required test data exists.
- Endpoint path and method are confirmed.
- Request and response schema are confirmed.

---

## 3. Environment Variables

Do not hardcode secrets.

| Variable | Purpose | Required |
|---|---|---|
| API_BASE_URL | Base API URL | Yes |
| TEST_USER_EMAIL | Test user email | If auth needed |
| TEST_USER_PASSWORD | Test user password | If auth needed |
| ADMIN_USER_EMAIL | Admin user email | If admin flow needed |
| ADMIN_USER_PASSWORD | Admin user password | If admin flow needed |
| API_TOKEN | Existing token if used | If applicable |

---

## 4. Request Definition

| Field | Value |
|---|---|
| Endpoint | |
| Method | |
| Auth Required | Yes / No |
| Authorized Roles | |
| Headers | |
| Query Params | |
| Request Body | |

---

## 5. Expected Response

| Check | Expected Value | Notes |
|---|---|---|
| Status Code | | Use Needs Confirmation if unknown |
| Response Body | | |
| Required Fields | | |
| Field Types | | |
| Sensitive Data Exposure | Must not expose secrets | |
| Error Format | | For negative cases |

---

## 6. Database Impact

Use this section for state-changing APIs.

| API Action | Expected DB Impact | DB Validation Needed |
|---|---|---|
| | | |

Do not write destructive DB checks without human approval.

---

## 7. Test Steps

| Step | Action | Expected Result |
|---:|---|---|
| 1 | | |
| 2 | | |
| 3 | | |

---

## 8. Assertions

Every API automation draft must include meaningful assertions.

| Assertion | Reason |
|---|---|
| Status code matches expected value | Confirms API response contract |
| Required fields exist | Confirms response completeness |
| Sensitive fields are not exposed | Protects security/privacy |
| Error message format is consistent | Confirms negative behavior |

---

## 9. Draft API Test

Use this section only when code generation is requested.

Recommended approaches:

- Playwright APIRequestContext
- Postman collection
- Newman
- Python requests
- Supertest if Node backend context exists

Generic Playwright API draft structure:

import { test, expect, request } from '@playwright/test';

test('API scenario title here', async () => {
  const api = await request.newContext({
    baseURL: process.env.API_BASE_URL,
    extraHTTPHeaders: {
      'Content-Type': 'application/json'
    }
  });

  const response = await api.post('/path-here', {
    data: {
      // request body here
    }
  });

  expect(response.status()).toBe(200);
  const body = await response.json();
  expect(body).toBeTruthy();
});

---

## 10. Negative Case Guidance

For negative API tests, include:

- Invalid payload
- Missing required fields
- Wrong field type
- Unauthorized request
- Wrong role request
- Not found request
- Conflict request
- Rate limit or retry behavior if relevant

Use exact status codes only when confirmed.

If not confirmed, write Needs Confirmation.

---

## 11. Flakiness Risks

| Risk | Impact | Mitigation |
|---|---|---|
| Shared test data | Parallel conflicts | Use isolated synthetic data |
| Unstable environment | False failures | Add health checks |
| Unknown status codes | Wrong assertions | Confirm API contract |
| Third-party dependency | Non-deterministic failures | Mock or isolate when possible |
| Rate limits | Test failures | Use controlled test profile |

---

## 12. Cleanup Needs

| Cleanup Item | Required | Method |
|---|---|---|
| Created records | Yes / No | |
| Tokens/sessions | Yes / No | |
| Test user state | Yes / No | |

---

## 13. Human Approval Points

| Item | Approval Needed | Reason |
|---|---|---|
| Production API execution | Yes | Must not run without approval |
| Real customer data | Yes | Sensitive data risk |
| Destructive endpoint | Yes | Data loss risk |
| Payment or financial API | Yes | High-risk flow |
| External side effect | Yes | Could affect users or systems |

---

## 14. Generated vs Executed Note

This API automation output is a generated draft.

It must not be reported as passed, verified, executed, or release-ready unless the test is actually run and execution evidence exists.

---

## 15. References

- references/patterns/api-testing-patterns.md
- references/examples/api-test-examples.md
- references/automation/automation-generation-patterns.md
- .github/instructions/api-testing.instructions.md
- .github/skills/api-testing/SKILL.md
