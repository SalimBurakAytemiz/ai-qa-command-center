# DB Validation Login Draft Example

## Purpose

This document shows an example DB validation automation draft for the login feature.

Important rule:

This is not an executed DB validation result.

It is a generated DB validation draft example only.

---

## 1. Automation Metadata

| Field | Value |
|---|---|
| Feature | User Login |
| Scenario ID | DB-LOGIN-001 |
| Validation Type | No-Change / Session State |
| Priority | P1 |
| Source DB Scenario | Disabled user should not create active session |
| Automation Candidate Decision | Later |
| Human Approval Required | Yes for DB access, production data, or destructive cleanup |

---

## 2. Safety Rules

- Prefer read-only validation.
- Use synthetic users.
- Do not query production without approval.
- Do not hardcode credentials.
- Use environment variables.
- Do not expose token values in logs.
- Do not run destructive cleanup without approval.

---

## 3. Draft Python DB Validation Script

~~~python
import os
import sys

def main() -> int:
    database_url = os.getenv("DATABASE_READONLY_URL") or os.getenv("DATABASE_URL")
    disabled_user_id = os.getenv("DISABLED_TEST_USER_ID")

    if not database_url:
        print("Missing database connection environment variable.")
        return 1

    if not disabled_user_id:
        print("Missing DISABLED_TEST_USER_ID environment variable.")
        return 1

    print("DB validation draft placeholder.")
    print("Validate that disabled user has no active session after rejected login.")
    print("Add safe read-only queries after schema is confirmed.")

    return 0

if __name__ == "__main__":
    raise SystemExit(main())
~~~

---

## 4. Draft SQL Placeholder

Use only after schema is confirmed.

~~~sql
SELECT
  id,
  status
FROM users
WHERE id = '<disabled-test-user-id>';

SELECT
  id,
  user_id,
  created_at
FROM sessions
WHERE user_id = '<disabled-test-user-id>'
  AND revoked_at IS NULL;
~~~

---

## 5. Generated vs Executed Note

This DB validation output is a generated draft example.

It must not be reported as passed, verified, executed, or release-ready unless the validation is actually run in a safe environment and execution evidence exists.
