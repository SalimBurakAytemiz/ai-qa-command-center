# Content Publishing Test Strategy

## 1. Strategy Summary

The content publishing feature requires risk-based validation because it controls public content visibility and CMS permissions.

Testing should focus on role-based access, draft/published/archived state transitions, API authorization, DB persistence, slug uniqueness, audit/timestamp behavior, and safe release readiness wording.

This strategy is generated for planning purposes only.

---

## 2. Testing Objectives

| Objective | Priority | Notes |
|---|---|---|
| Validate authorized content editor can create draft | P1 | Core CMS workflow |
| Validate admin can publish valid draft | P0 | Core publish flow |
| Validate draft content is not publicly visible | P0 | Data exposure prevention |
| Validate guest/registered users cannot access CMS | P0 | Access-control boundary |
| Validate registered user cannot publish via API | P0 | API authorization |
| Validate required field validation | P1 | Data quality |
| Validate duplicate slug rejection | P1 | Routing/data integrity |
| Validate publish/unpublish/archive state transitions | P1/P2 | Workflow consistency |
| Validate DB state impact | P1 | Persistence and integrity |
| Validate audit/timestamp behavior if supported | P2 | Governance |

---

## 3. In Scope

- CMS content creation
- Draft save behavior
- Admin publish behavior
- Public content visibility
- Draft content privacy
- CMS access control
- API authorization
- Required field validation
- Duplicate slug validation
- DB state transition planning
- Audit/timestamp planning
- Jira/Trello draft planning
- Daily report and release readiness draft

---

## 4. Out of Scope

- Rich text editor plugin testing
- Image upload
- SEO scoring
- Localization
- Scheduled publishing
- Version history
- Multi-approver workflow
- CDN cache purge
- Search indexing

---

## 5. Test Types Required

| Test Type | Required | Priority |
|---|---|---|
| Happy Path | Yes | P0/P1 |
| Edge Case | Yes | P2 |
| Negative Case | Yes | P0/P1 |
| Permission Case | Yes | P0 |
| API Validation | Yes | P0/P1 |
| DB Validation | Yes | P1 |
| CMS Functional | Yes | P1 |
| Public Web Validation | Yes | P1 |
| Security Checklist | Partial | P0/P1 |
| Performance | No | P3 |
| Mobile Native | No | P3 |

---

## 6. Main Risks

| Risk | Priority | Recommended Validation |
|---|---|---|
| Guest accesses CMS directly | P0 | Direct URL permission test |
| Registered user publishes content through API | P0 | Wrong-role API authorization test |
| Draft content visible publicly | P0 | Public route check for draft slug |
| Publish state not persisted | P1 | API and DB validation |
| Duplicate slug allowed | P1 | API and DB duplicate validation |
| Unauthorized action changes DB | P0 | No-change DB validation |
| Archive behavior unclear | P2 | Product clarification |

---

## 7. Recommended Agent Usage

| Agent | Reason |
|---|---|
| Product Intake Agent | Create product testing context |
| Test Strategy Agent | Define risk-based strategy |
| Task Router Agent | Select CMS/API/DB/reporting agents |
| Token Controller Agent | Prepare compact context |
| Test Planning Agent | Create test plan |
| Happy Path Test Case Agent | Generate successful draft/publish cases |
| Edge Case and Negative Case Agent | Generate invalid/permission/state cases |
| Web Functional Test Agent | Validate CMS and public web behavior |
| API Test Agent | Validate content endpoints |
| Database Validation Agent | Validate state transitions and no-change behavior |
| Jira/Trello Work Tracking Agent | Draft work items |
| Daily Quality Report Agent | Summarize generated QA package |
| Output Reviewer Agent | Review outputs |

---

## 8. Human Approval Needed

| Item | Reason |
|---|---|
| P0 authorization risks | Security boundary |
| External ticket creation | Human approval required |
| DB validation against shared environment | Data safety |
| Release readiness decision | Execution has not happened |
| Archive/unpublish business rule | Product decision needed |

---

## 9. Strategy Decision

Status: Yellow

Reason:

The feature is testable, but several implementation details are missing, including exact CMS routes, API response schema, DB schema, state enum values, and archive/unpublish behavior.
