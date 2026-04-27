# Content Publishing API Validation Plan

## 1. Scope Summary

This API validation plan covers CMS content creation, update, publish, unpublish, archive, public content retrieval, authorization checks, validation errors, duplicate slug handling, and state-changing API impact.

This is a generated API validation plan. No API execution has occurred.

---

## 2. Missing Information

| Missing Item | Why Needed | Impact |
|---|---|---|
| Exact response schema | Needed for contract validation | Response checks remain generic |
| Exact status codes | Needed for negative assertions | 400/403/409/422 ambiguity |
| Exact content status enum | Needed for state assertions | Draft/Published/Archived naming uncertain |
| Editor publish rule | Needed for authorization matrix | Role behavior uncertain |
| Archive/unpublish behavior | Needed for endpoint expectations | Expected result uncertain |

---

## 3. Endpoints Covered

| Endpoint | Method | Purpose | Auth Required | Priority |
|---|---|---|---|---|
| /api/cms/content | POST | Create content draft | Yes | P1 |
| /api/cms/content/{id} | PATCH | Update content | Yes | P2 |
| /api/cms/content/{id}/publish | POST | Publish content | Yes | P0 |
| /api/cms/content/{id}/unpublish | POST | Unpublish content | Yes | P2 |
| /api/cms/content/{id}/archive | POST | Archive content | Yes | P2 |
| /api/content/{slug} | GET | Get public published content | No | P1 |
| /api/cms/content/{id} | GET | Get CMS content detail | Yes | P2 |

---

## 4. API Test Scenarios

| ID | Type | Endpoint | Method | Priority | User Role | Preconditions | Request Data | Expected Status | Expected Response | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| API-CONTENT-001 | Valid Request | /api/cms/content | POST | P1 | Content Editor | Editor token exists | Valid title, unique slug, body | 201 Created | Content object with Draft status | Must not be public |
| API-CONTENT-002 | Valid Request | /api/cms/content/{id}/publish | POST | P0 | Admin User | Valid draft exists | Draft content ID | 200 OK | Content object with Published status | published_at expected |
| API-CONTENT-003 | Public Read | /api/content/{slug} | GET | P1 | Guest User | Published content exists | Published slug | 200 OK | Public content object | Must not expose CMS-only fields |
| API-CONTENT-004 | Unauthorized | /api/cms/content | POST | P0 | Guest User | No token | Valid payload | 401 Unauthorized | Unauthorized error | Protected endpoint |
| API-CONTENT-005 | Forbidden | /api/cms/content/{id}/publish | POST | P0 | Registered User | Registered user token exists | Draft content ID | 403 Forbidden | Forbidden error | Content state must not change |
| API-CONTENT-006 | Draft Privacy | /api/content/{slug} | GET | P0 | Guest User | Draft exists | Draft slug | Needs Confirmation | Not found or forbidden | Product rule needed |
| API-CONTENT-007 | Missing Required Field | /api/cms/content | POST | P1 | Content Editor | Editor token exists | Missing title | 400 or 422 | Validation error | Exact status needed |
| API-CONTENT-008 | Missing Required Field | /api/cms/content | POST | P1 | Content Editor | Editor token exists | Missing body | 400 or 422 | Validation error | Exact status needed |
| API-CONTENT-009 | Duplicate Data | /api/cms/content | POST | P1 | Content Editor | Existing slug exists | Duplicate slug | 409 or 422 | Duplicate slug error | Exact status needed |
| API-CONTENT-010 | Not Found | /api/cms/content/{id}/publish | POST | P2 | Admin User | Admin token exists | Unknown content ID | 404 Not Found | Not found error | Standard not found behavior |
| API-CONTENT-011 | Archive | /api/cms/content/{id}/archive | POST | P2 | Admin User | Content exists | Content ID | 200 OK | Archived content object | Archive rule needs confirmation |

---

## 5. Authentication Checks

| Scenario | Endpoint | Expected Status | Notes |
|---|---|---|---|
| No token | /api/cms/content | 401 Unauthorized | CMS protected endpoint |
| Invalid token | /api/cms/content | 401 Unauthorized | Token rejected |
| Expired token | /api/cms/content | 401 Unauthorized | Expiry behavior |
| Valid editor token | /api/cms/content | 201 Created | Draft creation allowed |
| Valid admin token | /api/cms/content/{id}/publish | 200 OK | Publish allowed |

---

## 6. Authorization Checks

| User Role | Endpoint | Expected Access | Expected Status | Notes |
|---|---|---|---|---|
| Guest User | /api/cms/content | Denied | 401 | No auth |
| Registered User | /api/cms/content | Denied | 403 | Wrong role |
| Content Editor | /api/cms/content | Allowed | 201 | Draft creation |
| Content Editor | /api/cms/content/{id}/publish | Needs Confirmation | Needs Confirmation | Product rule needed |
| Admin User | /api/cms/content/{id}/publish | Allowed | 200 | Publish action |
| Disabled User | CMS endpoints | Denied | 401 or 403 | Needs confirmation |

---

## 7. Database Impact Notes

| API Action | Expected Database Impact | DB Validation Needed |
|---|---|---|
| Create draft | New content record with Draft status | Yes |
| Publish | Content status becomes Published, published_at may update | Yes |
| Unpublish | Content status changes according to rule | Yes |
| Archive | Content status becomes Archived or archived_at set | Yes |
| Unauthorized publish | No DB state change | Yes |
| Duplicate slug | No duplicate content created | Yes |

---

## 8. Human Test Leader Notes

This API plan requires confirmation of exact status codes, response schema, status enum values, and role rules before execution.
