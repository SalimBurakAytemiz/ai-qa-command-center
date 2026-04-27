# Content Publishing API Notes

## 1. Feature Name

Content Publishing

---

## 2. API Overview

The content publishing API allows authorized CMS users to create, update, publish, unpublish, archive, and retrieve content items.

Guest and normal registered users should only access published public content through public endpoints.

---

## 3. Endpoints

| Endpoint | Method | Purpose | Auth Required | Roles |
|---|---|---|---|---|
| /api/cms/content | POST | Create content draft | Yes | Content Editor, Admin User |
| /api/cms/content/{id} | PATCH | Update content draft | Yes | Content Editor, Admin User |
| /api/cms/content/{id}/publish | POST | Publish content | Yes | Admin User |
| /api/cms/content/{id}/unpublish | POST | Unpublish content | Yes | Admin User |
| /api/cms/content/{id}/archive | POST | Archive content | Yes | Admin User |
| /api/content/{slug} | GET | Get public published content | No | Guest, Registered User |
| /api/cms/content/{id} | GET | Get CMS content detail | Yes | Content Editor, Admin User |

---

## 4. Request Details

| Endpoint | Required Fields | Optional Fields | Validation Rules |
|---|---|---|---|
| /api/cms/content | title, slug, body | summary, category, tags | slug unique, title/body not empty |
| /api/cms/content/{id} | at least one editable field | summary, category, tags | only draft/editable content should be updated if product requires |
| /api/cms/content/{id}/publish | none | none | content must be valid and publishable |
| /api/cms/content/{id}/unpublish | none | none | content must be currently published |
| /api/cms/content/{id}/archive | none | none | content must be archivable |

---

## 5. Response Details

| Endpoint | Success Status | Response Body | Notes |
|---|---|---|---|
| /api/cms/content | 201 Created | content object with Draft status | Exact schema needs confirmation |
| /api/cms/content/{id} | 200 OK | updated content object | Exact schema needs confirmation |
| /api/cms/content/{id}/publish | 200 OK | content object with Published status | published_at expected |
| /api/cms/content/{id}/unpublish | 200 OK | content object with unpublished/draft status | Exact status name needs confirmation |
| /api/cms/content/{id}/archive | 200 OK | content object with Archived status | Exact archive behavior needs confirmation |
| /api/content/{slug} | 200 OK | public content object | Must not expose CMS-only fields |

---

## 6. Error Responses

| Scenario | Expected Status | Expected Error | Notes |
|---|---|---|---|
| Missing token on CMS endpoint | 401 Unauthorized | Unauthorized | Protected endpoint |
| Wrong role creates content | 403 Forbidden | Forbidden | Role-based access |
| Wrong role publishes content | 403 Forbidden | Forbidden | Critical authorization check |
| Missing title | 400 or 422 | Validation error | Exact status needs confirmation |
| Missing body | 400 or 422 | Validation error | Exact status needs confirmation |
| Duplicate slug | 409 or 422 | Duplicate slug error | Exact status needs confirmation |
| Unknown content ID | 404 Not Found | Not found | Content does not exist |
| Draft content requested publicly | 404 or 403 | Not found or forbidden | Product rule needs confirmation |
| Archived content requested publicly | 404 or 410 | Not found or gone | Product rule needs confirmation |

---

## 7. Authentication Rules

- CMS endpoints require authentication.
- Public content endpoint may be accessible without authentication.
- Token/session must belong to an active authorized user.

---

## 8. Authorization Rules

- Guest user cannot access CMS endpoints.
- Registered user cannot access CMS endpoints.
- Content editor can create and edit drafts.
- Admin can publish, unpublish, and archive content.
- Disabled user cannot access CMS endpoints.

---

## 9. Database Impact

Content actions may affect:

- content record
- content status
- slug uniqueness
- published_at
- updated_at
- archived_at
- created_by
- updated_by
- published_by
- audit log if supported

Exact schema needs confirmation.

---

## 10. Missing API Information

| Missing Item | Why Needed | Impact |
|---|---|---|
| Exact content response schema | Needed for contract validation | API tests remain generic |
| Exact status names | Needed for DB/API validation | State expectations uncertain |
| Publish role rule | Needed for authorization validation | Editor vs admin behavior uncertain |
| Error status codes | Needed for precise negative tests | 400/409/422 ambiguity |
| Archive/unpublish behavior | Needed for state validation | Expected result unclear |
