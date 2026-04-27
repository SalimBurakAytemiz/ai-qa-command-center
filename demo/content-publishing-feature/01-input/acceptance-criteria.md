# Content Publishing Acceptance Criteria

## Feature Name

Content Publishing

---

## Acceptance Criteria

| ID | Criteria | Priority | User Role | Platform | Notes |
|---|---|---|---|---|---|
| AC-CONTENT-001 | Content editor can create a new content item and save it as Draft. | P1 | Content Editor | CMS / Admin Panel | Draft should not be public. |
| AC-CONTENT-002 | Admin can publish a valid draft content item. | P0 | Admin User | CMS / API / DB | Status changes to Published. |
| AC-CONTENT-003 | Published content is visible to guest and registered users. | P1 | Guest User / Registered User | Web | Public route must work. |
| AC-CONTENT-004 | Draft content is not visible to guest or registered users. | P0 | Guest User / Registered User | Web / API | Prevent private content leakage. |
| AC-CONTENT-005 | Normal registered user cannot access CMS content creation screen. | P0 | Registered User | Admin Panel | Direct URL access must be denied. |
| AC-CONTENT-006 | Normal registered user cannot publish content through API. | P0 | Registered User | API | API must enforce authorization. |
| AC-CONTENT-007 | Content creation is rejected when required fields are missing. | P1 | Content Editor | CMS / API | title, slug, body required. |
| AC-CONTENT-008 | Duplicate slug is rejected. | P1 | Content Editor / Admin User | API / DB | Slug must be unique. |
| AC-CONTENT-009 | Admin can unpublish published content. | P2 | Admin User | CMS / API / DB | Product rule needs confirmation. |
| AC-CONTENT-010 | Admin can archive content and archived content is not publicly listed. | P2 | Admin User | CMS / API / DB | Archive behavior needs confirmation. |
| AC-CONTENT-011 | Publishing content updates published_at and updated_at timestamps. | P2 | Admin User | DB | Exact field names need confirmation. |
| AC-CONTENT-012 | Content state changes should be auditable if audit logging is supported. | P2 | Admin User | DB / Backend | Audit behavior needs confirmation. |

---

## Notes

Acceptance criteria are written for planning and test design.

They are not executed results.
