# Database Notes Template

## Purpose

Use this template to describe expected database behavior for a product or feature.

This helps the Database Validation Agent generate DB validation plans.

---

## 1. Feature Name

Write feature name here.

---

## 2. Database Overview

Describe what data this feature affects.

---

## 3. Entities or Tables

| Entity or Table | Purpose | Notes |
|---|---|---|
| | | |

---

## 4. Expected State Changes

| User Action or API Action | Before State | After State | Priority |
|---|---|---|---|
| | | | |

---

## 5. Insert Behavior

Describe records that should be created.

---

## 6. Update Behavior

Describe records that should be updated.

---

## 7. Delete or Soft Delete Behavior

Describe delete behavior if relevant.

---

## 8. State Transitions

| Entity | From State | Trigger | To State |
|---|---|---|---|
| | | | |

---

## 9. Relationship Rules

Describe parent-child relationships, ownership rules, and foreign key expectations.

---

## 10. Audit and Timestamp Rules

Describe expected fields such as:

- created_at
- updated_at
- deleted_at
- created_by
- updated_by
- audit log

---

## 11. Duplicate and Orphan Risks

Describe possible duplicate or orphan record risks.

---

## 12. Transaction and Rollback Notes

Describe transaction behavior if relevant.

---

## 13. Human Approval Needed

List DB validations that need human approval.

Examples:

- Production data usage
- Destructive delete validation
- Bulk update validation
- Payment data validation

---

## 14. Missing DB Information

| Missing Item | Why Needed | Impact |
|---|---|---|
| | | |
