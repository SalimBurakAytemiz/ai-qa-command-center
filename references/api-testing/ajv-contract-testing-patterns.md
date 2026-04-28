# AJV Contract Testing Patterns

## 1. Purpose

This document defines the preferred API contract testing pattern for AI QA Command Center.

The recommended API contract testing approach is:

- AJV
- JSON Schema
- strict response validation
- regex pattern validation
- request body validation
- response body validation
- null and empty value checks
- sensitive value echo checks
- response time checks

This is stronger than status-code-only API smoke testing.

---

## 2. Why Status Code Checks Are Not Enough

A basic API smoke test may check only:

- HTTP status is 200
- response is JSON
- one or two fields exist

That is not enough for serious API validation.

A response can return 200 while still being wrong.

Examples:

- Required field is missing
- Extra unexpected field is added
- Field type changed
- Date format changed
- Code format changed
- Sensitive value is echoed
- Null value appears unexpectedly
- Empty string appears unexpectedly
- Empty array appears unexpectedly
- Response is too slow

---

## 3. Recommended Contract Test Layers

| Layer | Purpose |
|---|---|
| Status code check | Confirms HTTP-level response |
| Request schema validation | Confirms request payload shape before sending |
| Response schema validation | Confirms response body contract |
| Regex pattern validation | Confirms strict field format |
| Additional property rejection | Detects unexpected fields |
| Null / empty value check | Detects incomplete response data |
| Sensitive echo check | Prevents passwords/tokens from being returned |
| Response time check | Detects basic latency violation |

---

## 4. AJV Configuration Standard

Recommended AJV configuration:

~~~javascript
import Ajv from 'ajv';
import addFormats from 'ajv-formats';

export function createAjv() {
  const ajv = new Ajv({
    allErrors: true,
    strict: true,
    removeAdditional: false
  });

  addFormats(ajv);

  return ajv;
}
~~~

Important:

Do not use this for API contract tests:

~~~javascript
removeAdditional: 'all'
~~~

Reason:

Contract tests should detect unexpected fields.

They should not silently remove them.

---

## 5. Schema Strictness

Use:

~~~json
{
  "type": "object",
  "additionalProperties": false,
  "required": ["success", "code", "data"],
  "properties": {
    "success": {
      "type": "boolean"
    },
    "code": {
      "type": "integer"
    },
    "data": {
      "type": "object"
    }
  }
}
~~~

Why:

- `required` catches missing fields.
- `type` catches type changes.
- `additionalProperties: false` catches unexpected fields.

---

## 6. Regex Pattern Validation

Use regex patterns for strict business formats.

Examples:

| Field | Pattern | Meaning |
|---|---|---|
| Six digit code | `^\\d{6}$` | Exactly six digits |
| ISO-like microsecond UTC timestamp | `^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}\\.\\d{6}Z$` | Strict timestamp |
| Basic email | `^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$` | Basic email format |

Example:

~~~json
{
  "code": {
    "type": "string",
    "pattern": "^\\d{6}$"
  }
}
~~~

---

## 7. Request Body Validation

Validate request payloads before sending them.

Example:

~~~javascript
assertSchemaValid({
  schema: loginRequestSchema,
  data: requestBody,
  label: 'Login request'
});
~~~

Why:

- Prevents bad test data from producing misleading API failures.
- Confirms test setup matches API contract.
- Makes test failures easier to diagnose.

---

## 8. Response Body Validation

Validate response payloads after receiving them.

Example:

~~~javascript
assertSchemaValid({
  schema: loginCodeResponseSchema,
  data: jsonData,
  label: 'Login response'
});
~~~

Why:

- Detects response structure drift.
- Detects missing fields.
- Detects added unexpected fields.
- Detects type changes.
- Detects format changes.

---

## 9. Null and Empty Value Checks

Schema validation is not always enough.

A string field may be valid as a string but still be empty.

Use recursive checks for:

- null
- empty string
- empty array

Example rule:

~~~text
Response body should not contain null or empty values unless the schema explicitly allows them.
~~~

If a field is allowed to be null, model it explicitly in schema.

Example:

~~~json
{
  "middle_name": {
    "type": ["string", "null"]
  }
}
~~~

---

## 10. Sensitive Value Echo Checks

API responses must not echo sensitive request values.

Check that response body does not include:

- password
- access token
- refresh token
- OTP secret
- private key
- session secret

Example:

~~~javascript
assertNoSensitiveEcho({
  responseText,
  sensitiveValues: [password]
});
~~~

Important:

Do not log sensitive values in test output.

---

## 11. Response Time Checks

Response time checks should be configurable.

Default example:

~~~text
API_RESPONSE_TIME_LIMIT_MS=200
~~~

Use stricter or looser thresholds based on product requirements.

Do not invent performance thresholds.

If no official threshold exists, mark it as Needs Confirmation.

---

## 12. Safe Environment Behavior

Tests should not hit real systems accidentally.

Recommended environment variables:

| Variable | Purpose |
|---|---|
| API_BASE_URL | Target API base URL |
| TEST_USER_EMAIL | Synthetic test user email |
| TEST_USER_PASSWORD | Synthetic test user password |
| API_RESPONSE_TIME_LIMIT_MS | Optional response time limit |

If required environment variables are missing, tests should skip safely.

---

## 13. Recommended Folder Structure

Recommended API AJV test structure:

~~~text
06-tests/api-ajv/
  package.json
  README.md
  schemas/
    login-request.schema.json
    login-code-response.schema.json
  helpers/
    env.js
    assert-json-contract.js
  tests/
    login-code.contract.test.js
~~~

---

## 14. When To Use AJV Contract Tests

Use AJV contract tests for:

- login/auth endpoints
- payment-safe response checks
- user profile APIs
- content publishing APIs
- role/permission APIs
- analytics event payload APIs
- integration payload APIs
- critical business workflow APIs

---

## 15. When Not To Use Only AJV

AJV validates structure.

It does not fully validate:

- business correctness
- authorization logic
- DB state change correctness
- side effects
- event delivery
- async behavior
- security vulnerabilities

For full confidence, combine AJV with:

- API behavior tests
- DB validation
- authorization tests
- negative tests
- integration tests
- execution evidence

---

## 16. Generated vs Executed Note

AJV schemas and contract test skeletons are not execution evidence.

Execution evidence requires:

- tests actually run
- output captured
- failures reviewed
- environment documented
- human review when release impact exists

Use:

- `templates/execution-evidence-template.md`

---

## 17. Current Implementation

Current AJV API contract skeleton:

- `06-tests/api-ajv/package.json`
- `06-tests/api-ajv/schemas/login-request.schema.json`
- `06-tests/api-ajv/schemas/login-code-response.schema.json`
- `06-tests/api-ajv/helpers/env.js`
- `06-tests/api-ajv/helpers/assert-json-contract.js`
- `06-tests/api-ajv/tests/login-code.contract.test.js`

Run:

~~~bash
cd 06-tests/api-ajv
npm install
API_BASE_URL=http://localhost:3000 TEST_USER_EMAIL=test@example.com TEST_USER_PASSWORD=password npm test
~~~

---

## 18. Final Rule

API contract tests should fail loudly when the response contract changes.

Do not hide response changes by removing unexpected fields during validation.
