# Login Feature Jira and Trello Drafts

## 1. Purpose

These are draft work-tracking items for the login feature QA workflow.

They are not created in Jira or Trello.

Human approval is required before creating external tickets or cards.

---

## 2. Jira Drafts

| Draft ID | Type | Title | Priority | Description | Acceptance / Done Criteria |
|---|---|---|---|---|---|
| JIRA-LOGIN-QA-001 | Task | Prepare login feature test plan | P1 | Create test plan covering web, mobile web, API, DB, role routing, and error states. | Test plan reviewed by human test leader. |
| JIRA-LOGIN-QA-002 | Task | Generate login happy path test cases | P1 | Create successful login scenarios for registered and admin users. | Happy path cases reviewed and approved. |
| JIRA-LOGIN-QA-003 | Task | Generate login edge and negative test cases | P1 | Create invalid credential, empty field, disabled user, and direct access cases. | Edge/negative cases reviewed and approved. |
| JIRA-LOGIN-QA-004 | Task | Prepare login API validation plan | P1 | Validate login, current user, and logout endpoint behavior. | Missing API info documented. |
| JIRA-LOGIN-QA-005 | Task | Prepare login DB validation plan | P2 | Define DB validation for session/token and user state impact. | Schema gaps documented. |
| JIRA-LOGIN-QA-006 | Risk | Confirm login API error status codes | P2 | Exact 400/401/403/422 expectations are not confirmed. | Backend/API owner confirms expected status codes. |
| JIRA-LOGIN-QA-007 | Risk | Confirm token/session mechanism | P1 | Session/token behavior is needed for auth validation. | Auth mechanism documented. |
| JIRA-LOGIN-QA-008 | Security Risk | Validate guest cannot access dashboard directly | P0 | Direct protected page access must be blocked. | Direct URL access case reviewed and executed later. |

---

## 3. Trello Drafts

| Card | List | Priority | Notes |
|---|---|---|---|
| Login QA - Test Plan | QA To Do | P1 | Prepare and review login test plan |
| Login QA - Happy Path Cases | QA To Do | P1 | Registered/admin successful login |
| Login QA - Negative Cases | QA To Do | P1 | Invalid password, unknown email, disabled user |
| Login QA - API Validation Plan | QA To Do | P1 | Login/me/logout endpoints |
| Login QA - DB Validation Plan | QA To Do | P2 | Session/token/user state |
| Login QA - Missing Info Review | Blocked / Needs Clarification | P1 | API statuses, schema, dashboard routes |

---

## 4. Human Approval Required

| Item | Reason |
|---|---|
| Creating Jira tickets | External system action |
| Creating Trello cards | External system action |
| P0 security risk classification | Human QA leader approval required |
| Release readiness decision | Execution has not happened |
