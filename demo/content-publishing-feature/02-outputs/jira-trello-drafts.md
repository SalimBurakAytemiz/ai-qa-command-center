# Content Publishing Jira and Trello Drafts

## 1. Purpose

These are draft work-tracking items for the content publishing QA workflow.

They are not created in Jira or Trello.

Human approval is required before external creation.

---

## 2. Jira Drafts

| Draft ID | Type | Title | Priority | Description | Acceptance / Done Criteria |
|---|---|---|---|---|---|
| JIRA-CONTENT-QA-001 | Task | Prepare content publishing test plan | P1 | Create risk-based test plan for CMS draft/publish workflow. | Test plan reviewed by human test leader. |
| JIRA-CONTENT-QA-002 | Task | Generate content publishing happy path test cases | P1 | Generate draft creation, admin publish, and public visibility cases. | Happy path cases reviewed. |
| JIRA-CONTENT-QA-003 | Task | Generate content publishing negative and permission cases | P1 | Generate unauthorized CMS, wrong-role API, draft privacy, duplicate slug cases. | Negative cases reviewed. |
| JIRA-CONTENT-QA-004 | Task | Prepare content publishing API validation plan | P1 | Validate CMS content endpoints and public content endpoint. | Missing API details documented. |
| JIRA-CONTENT-QA-005 | Task | Prepare content publishing DB validation plan | P2 | Define DB state transition and no-change checks. | Schema gaps documented. |
| JIRA-CONTENT-QA-006 | Risk | Confirm editor publish permission rule | P1 | Editor/admin publish boundary is unclear. | Product owner confirms role rule. |
| JIRA-CONTENT-QA-007 | Risk | Confirm archive and unpublish behavior | P2 | Expected state after archive/unpublish is unclear. | Product owner confirms behavior. |
| JIRA-CONTENT-QA-008 | Security Risk | Validate wrong-role publish API is rejected | P0 | Normal users must not publish content via API. | Authorization case reviewed and executed later. |
| JIRA-CONTENT-QA-009 | Security Risk | Validate draft content is not publicly visible | P0 | Draft content leakage is a data exposure risk. | Draft public route case reviewed and executed later. |

---

## 3. Trello Drafts

| Card | List | Priority | Notes |
|---|---|---|---|
| Content QA - Test Plan | QA To Do | P1 | Prepare CMS workflow plan |
| Content QA - Happy Path Cases | QA To Do | P1 | Draft creation and admin publish |
| Content QA - Permission Cases | QA To Do | P0 | Guest/registered/CMS access |
| Content QA - API Validation Plan | QA To Do | P1 | CMS content endpoints |
| Content QA - DB Validation Plan | QA To Do | P2 | State transitions and no-change checks |
| Content QA - Missing Info Review | Blocked / Needs Clarification | P1 | Role rules, schema, status enums |

---

## 4. Human Approval Required

| Item | Reason |
|---|---|
| Creating Jira tickets | External system action |
| Creating Trello cards | External system action |
| P0 security risk classification | Human QA leader approval |
| Release readiness decision | Execution has not happened |
