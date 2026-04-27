# Content Publishing Database Validation Plan

## 1. Scope Summary

This database validation plan covers content creation, draft/published/archived state transitions, slug uniqueness, ownership, audit/timestamp behavior, and no-change validation for unauthorized actions.

Exact schema is not confirmed, so this plan uses entity-level language.

This is a generated DB validation plan. No DB queries have been executed.

---

## 2. Missing Information

| Missing Item | Why Needed | Impact |
|---|---|---|
| Exact table names | Needed for query-level checks | Entity-level only |
| Exact column names | Needed for assertions | Cannot write precise SQL |
| Status enum values | Needed for state validation | Draft/Published/Archived uncertain |
| Audit rules | Needed for audit validation | Optional until confirmed |
| Archive behavior | Needed for archived state checks | Expected result unclear |
| Ownership fields | Needed for actor validation | created_by/published_by uncertain |

---

## 3. Entities or Tables Covered

| Entity or Table | Purpose | Related Flow | Priority |
|---|---|---|---|
| content | Stores content items | Create, publish, unpublish, archive | P0/P1 |
| users | Stores actor identity | Editor/admin ownership | P1 |
| categories | Stores category relation if used | Content categorization | P3 |
| audit_logs | Stores governance events if supported | Publish/archive actions | P2 |

---

## 4. Expected State Changes

| Action | Before State | Trigger | After State | Priority | Notes |
|---|---|---|---|---|---|
| Create draft | No content exists | POST create content | Content exists with Draft status | P1 | Slug should be unique |
| Publish draft | Content is Draft | Admin publish action | Content becomes Published | P0 | published_at may update |
| Unpublish content | Content is Published | Admin unpublish action | Content becomes Draft or Unpublished | P2 | Product rule needed |
| Archive content | Content exists | Admin archive action | Content becomes Archived | P2 | archived_at may update |
| Unauthorized publish | Content is Draft | Registered user publish attempt | No state change | P0 | Critical no-change validation |
| Duplicate slug | Slug already exists | Create with duplicate slug | No duplicate record created | P1 | Unique constraint/rule |

---

## 5. Database Validation Scenarios

| ID | Type | Entity or Table | Trigger Action | Priority | Preconditions | Validation Steps | Expected Database State | Risk | Notes |
|---|---|---|---|---|---|---|---|---|---|
| DB-CONTENT-001 | Insert Validation | content | Create draft | P1 | Editor exists | Check content entity after create | Draft content exists with correct owner | Missing/wrong record | Schema needed |
| DB-CONTENT-002 | Update Validation | content | Publish draft | P0 | Draft exists | Check content after publish | Status Published and timestamp updated | Wrong public state | Status enum needed |
| DB-CONTENT-003 | No-Change Validation | content | Wrong role publish attempt | P0 | Draft exists, registered user token exists | Check content after rejected API request | Content remains Draft | Authorization bypass | Critical |
| DB-CONTENT-004 | Duplicate Validation | content | Duplicate slug create attempt | P1 | Existing slug exists | Check records for slug | Only one content record exists for slug | Routing conflict | Unique rule needed |
| DB-CONTENT-005 | Archive Validation | content | Archive content | P2 | Content exists | Check archived state | Content marked Archived or archived_at set | Stale public content | Archive rule needed |
| DB-CONTENT-006 | Audit Validation | audit_logs | Publish/archive action | P2 | Audit logging enabled | Check audit event | Actor, action, target, timestamp recorded | Missing audit trail | Optional until confirmed |

---

## 6. API/UI/DB Consistency Checks

| Source | Expected Database Impact | Validation Needed | Priority |
|---|---|---|---|
| CMS save draft | New Draft content | Yes | P1 |
| Admin publish from CMS | Published state persisted | Yes | P0 |
| Publish API | Published state persisted | Yes | P0 |
| Wrong-role publish API | No DB state change | Yes | P0 |
| Archive action | Archived state persisted | Yes | P2 |

---

## 7. Human Approval Needed

| Scenario | Reason |
|---|---|
| Production DB validation | Production data risk |
| Destructive cleanup | Data loss risk |
| Sensitive content validation | Privacy/content risk |
| Audit log validation | Security/governance review |

---

## 8. Human Test Leader Notes

DB validation should be executed only in a safe test environment with synthetic content.

Exact schema must be confirmed before writing real SQL.
