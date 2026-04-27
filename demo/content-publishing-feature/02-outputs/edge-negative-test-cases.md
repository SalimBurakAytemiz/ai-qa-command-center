# Content Publishing Edge and Negative Test Cases

## 1. Scope Summary

These test cases validate invalid content data, duplicate slug handling, unauthorized CMS access, wrong-role API actions, draft privacy, disabled user behavior, and state transition risks.

These test cases are generated planning artifacts only. They are not executed test results.

---

## 2. Edge Case Test Cases

| ID | Title | Priority | Platform | User Role | Preconditions | Test Data | Steps | Expected Result | Risk Area | Automation Candidate | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| TC-CONTENT-EDGE-001 | Verify very long title is handled safely | P2 | CMS / API | Content Editor | CMS/API available | Very long title, valid slug/body | 1. Create content with very long title 2. Save draft | Content is rejected or safely accepted according to product rule | Input boundary | Later | Max length needs confirmation |
| TC-CONTENT-EDGE-002 | Verify duplicate publish click is prevented | P2 | CMS / API | Admin User | Valid draft exists | Valid draft content | 1. Click Publish repeatedly while loading | Duplicate publish action is prevented and final state is consistent | Duplicate action | Later | Requires request/state observation |
| TC-CONTENT-EDGE-003 | Verify slug with special characters is handled | P2 | CMS / API | Content Editor | CMS/API available | Slug with spaces/special chars | 1. Enter special-character slug 2. Save draft | Slug is normalized, rejected, or validated according to product rule | Slug validation | Later | Slug rules need confirmation |
| TC-CONTENT-EDGE-004 | Verify archive action requires clear confirmation if destructive-ish | P3 | CMS | Admin User | Content exists | Existing content | 1. Click Archive | User sees expected confirmation or archive happens according to product rule | UX safety | No | Product decision needed |

---

## 3. Negative Test Cases

| ID | Title | Priority | Platform | User Role | Preconditions | Test Data | Steps | Expected Result | Risk Area | Automation Candidate | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| TC-CONTENT-NEG-001 | Verify guest cannot access CMS content list directly | P0 | Admin Panel / CMS | Guest User | User is not logged in | CMS content list URL | 1. Open CMS content list URL directly | User is redirected to login or access is denied | Authorization | Yes | Critical access-control boundary |
| TC-CONTENT-NEG-002 | Verify registered user cannot access CMS content editor directly | P0 | Admin Panel / CMS | Registered User | Registered user is logged in | CMS editor URL | 1. Open CMS editor URL directly | Access is denied and CMS editor is not visible | Authorization | Yes | Must test direct URL, not only menu visibility |
| TC-CONTENT-NEG-003 | Verify registered user cannot publish content through API | P0 | API | Registered User | Draft content exists, registered user token exists | Draft content ID | 1. Call publish endpoint with registered user token | API rejects request and content state does not change | API authorization | Yes | Critical wrong-role API case |
| TC-CONTENT-NEG-004 | Verify draft content is not visible publicly | P0 | Web / API | Guest User | Draft content exists | Draft content slug | 1. Open public content URL for draft slug | Draft content is not visible publicly | Data exposure | Yes | Product may use 404 or 403 |
| TC-CONTENT-NEG-005 | Verify content creation is rejected without title | P1 | CMS / API | Content Editor | CMS/API available | Missing title, valid slug/body | 1. Try to save draft without title | Save is rejected and validation error is shown | Required field | Yes | Exact message/status needs confirmation |
| TC-CONTENT-NEG-006 | Verify content creation is rejected without body | P1 | CMS / API | Content Editor | CMS/API available | Valid title/slug, missing body | 1. Try to save draft without body | Save is rejected and validation error is shown | Required field | Yes | Exact message/status needs confirmation |
| TC-CONTENT-NEG-007 | Verify duplicate slug is rejected | P1 | CMS / API / DB | Content Editor | Existing content slug exists | Duplicate slug | 1. Create new content with existing slug | Request is rejected and no duplicate content is created | Data integrity | Yes | Status code needs confirmation |
| TC-CONTENT-NEG-008 | Verify disabled user cannot access CMS | P1 | CMS / API | Disabled User | Disabled user exists | Disabled user credentials/session | 1. Attempt CMS access or CMS API request | Access is rejected | Authorization | Later | Requires disabled test user |

---

## 4. Permission and State Test Cases

| ID | Title | Priority | Platform | User Role | Preconditions | Steps | Expected Result | Risk Area | Automation Candidate |
|---|---|---|---|---|---|---|---|---|---|
| TC-CONTENT-PERM-001 | Verify content editor cannot publish if only admin can publish | P0 | CMS / API | Content Editor | Draft exists and editor is logged in | Attempt publish action from UI or API | Publish is denied or unavailable according to product rule | Authorization | Yes | Editor publish rule must be confirmed |
| TC-CONTENT-STATE-001 | Verify unauthorized publish attempt causes no DB state change | P0 | API / DB | Registered User | Draft exists | Attempt publish endpoint with wrong role | Content remains Draft | No-change DB validation | Later | Requires DB/schema access |
| TC-CONTENT-STATE-002 | Verify archived content is not publicly visible | P1 | Web / API / DB | Guest User | Archived content exists | Open public URL or public listing | Archived content is not visible | Public visibility | Later | Archive public behavior needs confirmation |

---

## 5. Missing Information

| Missing Item | Why Needed | Impact |
|---|---|---|
| Exact CMS routes | Needed for direct URL tests | UI permission tests generic |
| Exact validation messages | Needed for UI assertions | Expected results generic |
| Exact API status codes | Needed for API assertions | 400/403/409/422 ambiguity |
| Editor publish permission | Needed for role tests | Editor/admin boundary uncertain |
| Archive/unpublish product rule | Needed for state tests | Expected state unclear |
| DB schema | Needed for no-change DB validation | DB tests remain entity-level |
