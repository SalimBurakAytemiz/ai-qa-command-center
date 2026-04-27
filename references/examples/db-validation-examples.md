# Database Validation Examples

## Purpose

This document provides practical database validation examples for AI QA agents.

Use this reference when creating DB validation plans, API-DB consistency checks, UI-DB consistency checks, transaction checks, audit checks, and data integrity reviews.

---

## 1. Good DB Validation Scenario Example

| ID | Type | Entity or Table | Trigger Action | Priority | Preconditions | Validation Steps | Expected Database State | Risk | Notes |
|---|---|---|---|---|---|---|---|---|---|
| DB-PROFILE-001 | Update Validation | users | User updates profile name | P1 | Active user exists | Check user entity after profile update | Correct user record has updated name and updated_at changes | Wrong record update | Exact table and column names must be confirmed |

### Why This Is Good

- Trigger action is clear.
- Before condition is clear.
- Expected DB state is specific.
- Risk is included.
- It avoids pretending that a query was executed.
- It does not invent schema when schema is not confirmed.

---

## 2. Bad DB Validation Scenario Example

| ID | Title | Expected Result |
|---|---|---|
| DB-001 | Check database | Database is correct |

### Why This Is Bad

- No entity or table is identified.
- No trigger action is defined.
- No before state is defined.
- No after state is defined.
- Expected result is vague.
- Risk is missing.
- It cannot be executed or reviewed.

---

## 3. Before / Trigger / After Example

| Before State | Trigger Action | After State |
|---|---|---|
| User name is "Old Name" | User updates profile name from UI | User name becomes "New Name" and updated_at changes |

### Good Practice

If before and after state cannot be explained, the DB validation is not ready.

---

## 4. Insert Validation Example

| Trigger | Expected DB State |
|---|---|
| User registers successfully | New user record is created with active status |
| User creates content | New content record is created and linked to the correct owner |
| Admin creates category | New category record exists and is visible to allowed roles |

### Checks

- Record exists.
- Required fields are populated.
- Default values are correct.
- created_at exists.
- created_by exists if applicable.
- No duplicate record is created.

---

## 5. Update Validation Example

| Trigger | Expected DB State |
|---|---|
| User updates profile name | Existing user record has updated name and updated_at changes |
| Admin changes user role | User role changes and audit log is created |
| Content manager publishes article | Article status changes from Draft to Published |

### Checks

- Correct record updated.
- Incorrect records unchanged.
- updated_at changes.
- updated_by changes if applicable.
- Business rules are preserved.

---

## 6. Soft Delete Example

| Trigger | Expected DB State |
|---|---|
| Admin archives content | Content record remains but status changes to Archived |
| User deletes saved item | Item is marked deleted with deleted_at timestamp |
| CMS content is unpublished | Content remains but public visibility changes |

### Checks

- Correct deletion type is used.
- Related records are handled correctly.
- No orphan records are created.
- Audit log exists if required.
- Human approval exists for risky validation.

---

## 7. Unauthorized No-Change Example

| Trigger | Expected DB State |
|---|---|
| Normal user attempts admin action | No admin-level DB change occurs |
| Guest sends protected API request | No record is created or updated |
| Disabled user attempts login | No active session/token is created |

### Why This Matters

Security validation is not only about API status codes.

The database must also remain unchanged after rejected or unauthorized actions.

---

## 8. Duplicate Risk Example

| Trigger | Risk | Recommended Validation |
|---|---|---|
| User double-clicks submit | Duplicate records | Check duplicate prevention or idempotency |
| API retry after timeout | Duplicate action | Check idempotency key or uniqueness rule |
| Reconnect event in realtime system | Duplicate state | Check event handling and state consistency |

---

## 9. Orphan Record Example

| Action | Risk | Recommended Validation |
|---|---|---|
| Delete CMS category | Articles may reference deleted category | Confirm reassignment, deletion, or blocked delete behavior |
| Delete user | User-owned records may become orphaned | Confirm retention or ownership policy |
| Delete parent order | Order items may remain without valid parent | Confirm relationship handling |

---

## 10. Audit Validation Example

| Action | Expected Audit |
|---|---|
| Admin changes user role | Audit log records actor, target user, old role, new role, timestamp |
| User changes email | Audit log records user ID, old email, new email, timestamp if required |
| Failed login attempt | Security log records attempt if supported |

---

## 11. Timestamp Validation Example

| Action | Expected Timestamp Behavior |
|---|---|
| Record created | created_at is set |
| Record updated | updated_at changes |
| Record soft deleted | deleted_at is set |
| Content published | published_at is set |
| Status changed | status_changed_at is set |

---

## 12. DB Validation Quality Checklist

A good DB validation plan should include:

- Before state
- Trigger action
- After state
- Entity or table
- Expected DB state
- Risk
- Preconditions
- Human approval needs
- Missing schema information
- Duplicate risk
- Orphan record risk
- Transaction risk
- Audit/timestamp checks
- No execution claim unless query evidence exists
