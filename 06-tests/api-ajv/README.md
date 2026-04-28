# AJV API Contract Tests

## Purpose

This folder contains AJV-based API contract tests.

This is stricter than basic status-code-only API smoke testing.

It validates:

- Request body schema
- Response body schema
- Required fields
- Extra fields using `additionalProperties: false`
- Regex patterns
- Null values
- Empty strings
- Empty arrays
- Response time
- Sensitive value echoing

---

## Why AJV

AJV is useful for contract testing because it validates response structure against JSON Schema.

The system should prefer strict validation for API contracts.

Important rule:

Do not use `removeAdditional: all` for API contract tests.

Contract tests should detect unexpected fields, not remove them.

---

## Install

~~~bash
cd 06-tests/api-ajv
npm install
~~~

---

## Run

~~~bash
API_BASE_URL=http://localhost:3000 TEST_USER_EMAIL=test@example.com TEST_USER_PASSWORD=password npm test
~~~

Optional response time threshold:

~~~bash
API_RESPONSE_TIME_LIMIT_MS=500 npm test
~~~

---

## Environment Variables

| Variable | Required | Purpose |
|---|---|---|
| API_BASE_URL | Yes | Base API URL |
| TEST_USER_EMAIL | Yes | Synthetic test user email |
| TEST_USER_PASSWORD | Yes | Synthetic test user password |
| API_RESPONSE_TIME_LIMIT_MS | No | Response time limit, default 200ms |

---

## Safety Note

These tests require a real API target.

If environment variables are missing, the tests are skipped safely.

Do not use production credentials or real customer accounts without explicit human approval.
