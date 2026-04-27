# Content Publishing Database Notes

## 1. Feature Name

Content Publishing

---

## 2. Database Overview

The content publishing feature creates and updates content records and changes content state across Draft, Published, Unpublished, and Archived states.

The exact schema is not confirmed, so this demo uses entity-level validation.

---

## 3. Entities or Tables

| Entity or Table | Purpose | Notes |
|---|---|---|
| content | Stores content items | Exact table name needs confirmation |
| users | Stores author/editor/admin identity | Needed for ownership/audit |
| categories | Stores category relation if supported | Optional |
| audit_logs | Stores publishing actions if supported | Optional |

---

## 4. Expected State Changes

| User Action or API Action | Before State | After State | Priority |
|---|---|---|---|
| Create content | No content exists | Content exists with Draft status | P1 |
| Publish content | Content is Draft | Content becomes Published | P0 |
| Unpublish content | Content is Published | Content becomes Draft or Unpublished | P2 |
| Archive content | Content exists | Content becomes Archived and not publicly visible | P2 |
| Unauthorized publish attempt | Content exists | No DB state change | P0 |
| Duplicate slug attempt | Existing slug exists | No duplicate content created | P1 |

---

## 5. Insert Behavior

Possible inserts:

- content record
- audit log record

Exact behavior needs confirmation.

---

## 6. Update Behavior

Possible updates:

- content.status
- content.title
- content.slug
- content.body
- content.updated_at
- content.published_at
- content.archived_at
- content.updated_by
- content.published_by

Exact fields need confirmation.

---

## 7. Delete or Soft Delete Behavior

Content archiving should not physically delete content unless explicitly designed.

Archive behavior needs confirmation.

---

## 8. State Transitions

| Entity | From State | Trigger | To State |
|---|---|---|---|
| Content | None | Create draft | Draft |
| Content | Draft | Publish | Published |
| Content | Published | Unpublish | Draft or Unpublished |
| Content | Draft or Published | Archive | Archived |

---

## 9. Relationship Rules

- Content should belong to the correct creator.
- Publish action should store correct actor if supported.
- Category relation should remain valid if categories exist.
- Unauthorized actions must not change content state.

---

## 10. Audit and Timestamp Rules

Possible checks:

- created_at set on content creation
- updated_at changes on edit
- published_at set on publish
- archived_at set on archive if supported
- audit log created for publish/unpublish/archive if supported

---

## 11. Duplicate and Orphan Risks

| Risk | Trigger | Recommended Validation |
|---|---|---|
| Duplicate slug | Two content items use same slug | Confirm uniqueness rule |
| Orphan category relation | Category deleted or invalid | Confirm relationship behavior |
| Wrong owner | Content created under wrong user | Confirm created_by/owner |
| Unauthorized state change | Wrong role publishes | Confirm no DB change |

---

## 12. Missing DB Information

| Missing Item | Why Needed | Impact |
|---|---|---|
| Exact table names | Needed for query-level validation | DB plan remains entity-level |
| Status enum values | Needed for state validation | Expected states uncertain |
| Audit rules | Needed for governance validation | Audit expectations unclear |
| Archive behavior | Needed for public visibility validation | Delete/archive expectations unclear |
| Ownership fields | Needed for data integrity validation | Actor checks remain generic |
