# Database Validation Patterns

## Purpose

This document defines practical database validation patterns for AI QA agents.

Use this reference when planning database validation, API-DB consistency checks, data integrity checks, transaction checks, and audit validation.

---

## 1. Before / Trigger / After Pattern

Every database validation scenario should include:

1. Before state
2. Trigger action
3. After state
4. Expected database result

### Example

| Before State | Trigger Action | After State |
|---|---|---|
| User name is "Old Name" | User updates profile name from UI | User name becomes "New Name" and updated_at changes |

### Rule

If before and after state cannot be defined, the DB validation is not ready.

---

## 2. Insert Validation Pattern

Use when an action creates a new record.

### Example

| Trigger | Expected DB State |
|---|---|
| User registers successfully | New user record is created with active status |

Check:

- Record exists
- Required fields are populated
- Default values are correct
- created_at exists
- created_by exists if applicable
- No duplicate record created

---

## 3. Update Validation Pattern

Use when an action modifies an existing record.

### Example

| Trigger | Expected DB State |
|---|---|
| User updates profile name | Existing user record has updated name and updated_at timestamp changes |

Check:

- Correct record updated
- Incorrect records unchanged
- updated_at changes
- updated_by changes if applicable
- Business rules preserved

---

## 4. Delete Validation Pattern

Use when an action removes data.

### Hard Delete

Record is physically removed.

### Soft Delete

Record remains but is marked deleted.

### Example

| Trigger | Expected DB State |
|---|---|
| Admin archives content | Content record remains with deleted_at or archived status |

Check:

- Correct deletion type
- Related records handled correctly
- No orphan records created
- Audit log exists
- Human approval if operation is risky

---

## 5. State Transition Pattern

Use when records move between statuses.

### Example

| Before State | Trigger | After State |
|---|---|---|
| Article status is Draft | Content manager clicks Publish | Article status becomes Published |

Check:

- Only allowed transitions happen
- Invalid transitions are rejected
- status_changed_at updates
- status_changed_by updates if applicable

---

## 6. Relationship Integrity Pattern

Use when entities are related.

### Example

| Parent Entity | Child Entity | Validation |
|---|---|---|
| User | Orders | Orders remain linked to correct user |

Check:

- Foreign keys valid
- Parent exists
- Child records not orphaned
- Deleting parent handles children correctly
- User ownership remains correct

---

## 7. Duplicate Prevention Pattern

Use when repeated actions can create duplicate records.

### Example

| Trigger | Risk |
|---|---|
| User double-clicks Submit | Duplicate profile update, duplicate order, duplicate ticket |

Check:

- Unique constraints
- Idempotency
- Duplicate request handling
- Retry behavior
- UI duplicate prevention if relevant

---

## 8. Orphan Record Pattern

Use when deleting or updating parent records.

### Example

| Action | Risk |
|---|---|
| Delete CMS category | Articles may remain linked to deleted category |

Check:

- Child records are reassigned, blocked, deleted, or preserved according to business rules
- No child record references invalid parent
- UI and API do not expose broken relationships

---

## 9. Transaction Consistency Pattern

Use for multi-step operations.

### Example

| Operation | Risk |
|---|---|
| Create order and payment record | Order created but payment record missing |

Check:

- All required records are created together
- Failure rolls back all changes
- Partial state is not left behind
- Retry does not create duplicates

---

## 10. Audit Validation Pattern

Use for admin, security, or sensitive actions.

Check:

- audit log created
- actor user recorded
- action type recorded
- timestamp recorded
- old value recorded if required
- new value recorded if required
- IP or device info recorded if required

### Example

| Action | Expected Audit |
|---|---|
| Admin changes user role | Audit log records admin ID, target user ID, old role, new role, timestamp |

---

## 11. Timestamp Validation Pattern

Check:

- created_at set on insert
- updated_at changes on update
- deleted_at set on soft delete
- published_at set on publish
- status_changed_at set on state change

### Rule

Timestamp fields should reflect the correct action.

---

## 12. API-DB Consistency Pattern

For API-triggered changes:

| API Action | Expected API Response | Expected DB State |
|---|---|---|
| POST /api/users | 201 Created | User record exists |
| PATCH /api/profile | 200 OK | User profile fields updated |
| DELETE /api/content/{id} | 204 No Content | Content is soft deleted |

Check:

- API response matches DB state
- Failed API request does not change DB incorrectly
- Unauthorized API request does not change DB
- Duplicate API request does not create duplicate DB state

---

## 13. UI-DB Consistency Pattern

For UI-triggered changes:

Check:

- UI success state matches DB state
- Refresh displays DB state
- Another session sees correct state
- User role sees only allowed data
- Deleted or archived data is hidden or shown according to rules

---

## 14. CMS-DB Consistency Pattern

For CMS content:

Check:

- Draft content is stored correctly
- Published content changes status
- Public web displays published content
- Unpublished content is hidden
- Edited content updates correct record
- Deleted content follows soft delete or archive rules

---

## 15. Socket-DB Consistency Pattern

For realtime behavior:

Check:

- DB state changes when realtime event is processed
- Realtime event reflects correct DB state
- Reconnect does not create duplicate state
- Stale data is not shown after DB update
- Multi-client view remains consistent

---

## 16. Human Approval Required

Human approval is required for:

- Production data access
- Destructive delete validation
- Bulk update validation
- Migration validation
- Payment or financial records
- Sensitive personal data
- Security-sensitive user data

---

## 17. DB Validation Quality Checklist

Before finalizing DB validation, check:

- Is before state clear?
- Is trigger action clear?
- Is after state clear?
- Are entities or tables identified?
- Are schema gaps listed?
- Are duplicate risks considered?
- Are orphan risks considered?
- Are transaction risks considered?
- Are audit fields considered?
- Are timestamp fields considered?
- Are risky checks marked for human approval?
- Is execution language avoided unless real execution happened?