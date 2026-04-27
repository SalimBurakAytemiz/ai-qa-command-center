# DB Validation Script Template

## Purpose

Use this template when preparing database validation script drafts from approved DB validation scenarios.

Important rule:

Generated DB validation scripts are automation drafts only.

They are not executed DB validation results unless the script is actually run in a safe environment and execution evidence exists.

---

## 1. Automation Metadata

| Field | Value |
|---|---|
| Feature | |
| Scenario ID | |
| Validation Type | Insert / Update / Soft Delete / Relationship / Audit / Timestamp / No-Change |
| Priority | P0 / P1 / P2 / P3 |
| Source DB Scenario | |
| Automation Candidate Decision | Yes / Later |
| Human Approval Required | If production, destructive, sensitive, or high-risk |

---

## 2. Safety Rules

DB validation scripts must follow these rules:

- Prefer read-only validation.
- Use synthetic test data.
- Do not use production data without approval.
- Do not run destructive queries without approval.
- Do not expose secrets in scripts.
- Do not hardcode DB passwords.
- Use environment variables for connection strings.
- Log only safe validation output.
- Separate generated script drafts from executed results.

---

## 3. Preconditions

List required setup before the DB validation can run.

Examples:

- Safe test database is available.
- DB connection string is available through environment variable.
- Required test user exists.
- Trigger action has been executed in the test environment.
- Exact table and column names are confirmed.
- Expected before and after states are documented.

---

## 4. Environment Variables

| Variable | Purpose | Required |
|---|---|---|
| DATABASE_READONLY_URL | Read-only DB connection | Preferred |
| DATABASE_URL | DB connection | Only if approved |
| DB_HOST | DB host | If not using URL |
| DB_PORT | DB port | If not using URL |
| DB_NAME | DB name | If not using URL |
| DB_USER | DB user | If not using URL |
| DB_PASSWORD | DB password | If not using URL |

Do not commit real values.

---

## 5. Before / Trigger / After Definition

| Item | Description |
|---|---|
| Before State | |
| Trigger Action | |
| Expected After State | |
| Entity or Table | |
| Key Identifier | |
| Expected Risk | |

Every DB validation script must be based on a clear before, trigger, and after state.

---

## 6. Query Plan

| Query Purpose | Query Type | Expected Result | Notes |
|---|---|---|---|
| Confirm record exists | SELECT | | |
| Confirm correct owner | SELECT | | |
| Confirm status changed | SELECT | | |
| Confirm timestamp changed | SELECT | | |
| Confirm no duplicate record | SELECT | | |
| Confirm no unauthorized state change | SELECT | | |

Do not include destructive DELETE, UPDATE, or INSERT queries unless explicitly approved.

---

## 7. Assertions

| Assertion | Reason |
|---|---|
| Record exists or does not exist as expected | Confirms persistence behavior |
| Correct user owns the record | Prevents data leakage |
| Status changed correctly | Confirms state transition |
| updated_at changed when expected | Confirms update behavior |
| No duplicate records exist | Prevents duplicate data risk |
| Unauthorized action caused no DB change | Confirms access-control integrity |

---

## 8. Draft Python DB Validation Script

Use this section only when code generation is requested.

Generic Python script structure:

import os
import sys

def main():
    database_url = os.getenv('DATABASE_READONLY_URL') or os.getenv('DATABASE_URL')

    if not database_url:
        print('Missing database connection environment variable.')
        return 1

    print('DB validation draft placeholder.')
    print('Add safe read-only queries here after schema is confirmed.')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())

---

## 9. Draft SQL Query Section

Use this section only after schema is confirmed.

Example read-only query placeholder:

SELECT
  id,
  status,
  user_id,
  created_at,
  updated_at
FROM table_name_here
WHERE id = 'test-record-id';

Replace placeholder table and column names only when schema is confirmed.

---

## 10. No-Change Validation Pattern

Use this pattern for rejected or unauthorized actions.

| Trigger | Expected DB State |
|---|---|
| Guest attempts protected action | No record is created or updated |
| Wrong role attempts admin action | No admin-level state change occurs |
| Disabled user attempts login | No active session/token is created |

No-change validation is critical for authorization and security checks.

---

## 11. Cleanup Needs

| Cleanup Item | Required | Method | Approval Needed |
|---|---|---|---|
| Test records | Yes / No | | If destructive |
| Sessions/tokens | Yes / No | | If destructive |
| Audit test events | Yes / No | | If sensitive |

Cleanup must be safe and approved when it changes data.

---

## 12. Human Approval Points

| Item | Approval Needed | Reason |
|---|---|---|
| Production DB access | Yes | Production data risk |
| Destructive query | Yes | Data loss risk |
| Sensitive customer data | Yes | Privacy risk |
| Payment or financial data | Yes | High-risk data |
| Bulk validation | Yes | May affect performance or data |

---

## 13. Generated vs Executed Note

This DB validation output is a generated automation draft.

It must not be reported as passed, verified, executed, or release-ready unless it is actually run in a safe environment and execution evidence exists.

---

## 14. References

- references/patterns/db-validation-patterns.md
- references/examples/db-validation-examples.md
- references/automation/automation-generation-patterns.md
- .github/instructions/db-validation.instructions.md
- .github/skills/db-validation/SKILL.md
