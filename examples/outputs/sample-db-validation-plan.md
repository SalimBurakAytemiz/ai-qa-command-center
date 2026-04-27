# Sample Database Validation Plan

## 1. Scope Summary

This sample demonstrates the expected structure for a database validation plan.

This is a planning artifact only. No database query has been executed.

---

## 2. Missing Information

| Missing Item | Why Needed | Impact |
|---|---|---|
| Exact table names | Needed for query-level validation | DB checks remain entity-level |
| Column names | Needed for precise validation | Assertions cannot be exact |
| Relationship rules | Needed for integrity checks | Orphan/ownership risks may be missed |
| Audit rules | Needed for audit validation | Audit expectations remain unclear |
| Soft delete rules | Needed for delete validation | Delete behavior may be misinterpreted |

---

## 3. Entities or Tables Covered

| Entity or Table | Purpose | Related Flow | Priority |
|---|---|---|---|
| sample_entity | Main feature data | Create / update / delete sample record | P1 |
| user_entity | Owner or actor data | Role and ownership validation | P1 |
| audit_log | Optional audit trail | Admin or sensitive actions | P2 |

---

## 4. Expected State Changes

| Action | Before State | Trigger | After State | Priority | Notes |
|---|---|---|---|---|---|
| Create sample record | No sample record exists | Valid create action | New sample record exists | P1 | Insert validation |
| Update sample record | Existing record exists | Valid update action | Existing record is updated | P1 | Update validation |
| Delete or archive sample record | Active record exists | Delete/archive action | Record is deleted or marked inactive | P2 | Exact delete rule needed |
| Unauthorized action | User lacks permission | Restricted action attempted | No DB state change | P0 | Security boundary |

---

## 5. Database Validation Scenarios

| ID | Type | Entity or Table | Trigger Action | Priority | Preconditions | Validation Steps | Expected Database State | Risk | Notes |
|---|---|---|---|---|---|---|---|---|---|
| DB-SAMPLE-001 | Insert Validation | sample_entity | Create action | P1 | Valid user exists | Check new entity after create | Record exists with correct owner and required fields | Missing or wrong record | Exact table/columns needed |
| DB-SAMPLE-002 | Update Validation | sample_entity | Update action | P1 | Existing record exists | Check entity after update | Correct record updated, unrelated records unchanged | Wrong record update | Check ownership |
| DB-SAMPLE-003 | Soft Delete Validation | sample_entity | Archive/delete action | P2 | Active record exists | Check delete/archive state | Record follows expected delete rule | Data loss or stale visibility | Delete rule must be confirmed |
| DB-SAMPLE-004 | Relationship Integrity | sample_entity / user_entity | Create or update action | P1 | User owns record | Check owner relationship | Record belongs to correct user | Data leakage | Critical for multi-user systems |
| DB-SAMPLE-005 | Duplicate Risk | sample_entity | Duplicate submit | P2 | Duplicate action possible | Check duplicate records | No unexpected duplicate records | Duplicate data | May need idempotency |
| DB-SAMPLE-006 | Unauthorized No-Change | sample_entity | Unauthorized action | P0 | User lacks permission | Check database after rejected action | No state change occurs | Permission bypass | Critical security check |

---

## 6. API, UI, or CMS Consistency Checks

| Source | Expected Database Impact | Validation Needed | Priority |
|---|---|---|---|
| UI create action | New record exists | Yes | P1 |
| API create action | New record exists | Yes | P1 |
| UI update action | Existing record updated | Yes | P1 |
| Unauthorized API action | No DB change | Yes | P0 |
| CMS publish action | Status changes correctly | If CMS is in scope | P2 |

---

## 7. Transaction and Concurrency Risks

| Risk | Impact | Recommended Validation |
|---|---|---|
| Partial update | Data inconsistency | Validate all expected fields update together |
| Duplicate request | Duplicate record | Validate idempotency or duplicate prevention |
| Concurrent update | Lost update | Validate expected conflict or last-write behavior |
| Failed action changes DB | False success or data corruption | Validate rollback behavior |

---

## 8. Audit and Timestamp Checks

| Field or Log | Expected Behavior | Priority |
|---|---|---|
| created_at | Set when record is created | P2 |
| updated_at | Changes when record is updated | P2 |
| deleted_at | Set when soft delete happens | P2 |
| created_by | Stores actor if supported | P2 |
| updated_by | Stores actor if supported | P2 |
| audit_log | Records sensitive/admin action if required | P2 |

---

## 9. Human Approval Needed

| Scenario | Reason |
|---|---|
| Production data validation | Production data must not be used without approval |
| Destructive delete validation | Could damage test data |
| Bulk update validation | Could impact multiple records |
| Sensitive personal data validation | Privacy risk |
| Payment or financial record validation | High-risk data |

---

## 10. Final Note

This sample DB validation plan should be adapted to the real schema before execution.

Do not invent table names or columns when schema is missing.
