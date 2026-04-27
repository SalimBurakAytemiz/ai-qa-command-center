# Sample Jira and Trello Drafts

## 1. Purpose

This sample demonstrates how AI-generated work-tracking drafts should be structured.

These are draft items only.

They must not be created in Jira or Trello without human approval.

---

## 2. Jira Drafts

| Draft ID | Type | Title | Priority | Description | Acceptance / Done Criteria |
|---|---|---|---|---|---|
| JIRA-SAMPLE-QA-001 | Task | Prepare feature test plan | P1 | Create a risk-based test plan for the feature. | Test plan reviewed by human test leader. |
| JIRA-SAMPLE-QA-002 | Task | Generate happy path test cases | P1 | Generate successful-flow test cases mapped to acceptance criteria. | Happy path cases reviewed and approved. |
| JIRA-SAMPLE-QA-003 | Task | Generate edge and negative test cases | P1 | Generate invalid, boundary, permission, and failure cases. | Edge and negative cases reviewed. |
| JIRA-SAMPLE-QA-004 | Task | Prepare API validation plan | P1 | Define endpoint, auth, payload, response, and error validation scenarios. | Missing API information documented. |
| JIRA-SAMPLE-QA-005 | Task | Prepare DB validation plan | P2 | Define expected database state changes and integrity checks. | DB schema gaps documented. |
| JIRA-SAMPLE-QA-006 | Risk | Confirm missing acceptance criteria | P1 | Some acceptance criteria are unclear or incomplete. | Product owner confirms expected behavior. |
| JIRA-SAMPLE-QA-007 | Risk | Confirm role-based access rules | P1 | Permission expectations are required for security validation. | Role rules confirmed by product or backend owner. |
| JIRA-SAMPLE-QA-008 | Bug Draft | Investigate potential unauthorized access | P0 | Generated plan identified a possible direct URL access risk. | Human test leader validates and approves bug creation. |

---

## 3. Trello Drafts

| Card | List | Priority | Notes |
|---|---|---|---|
| Feature QA - Test Plan | QA To Do | P1 | Prepare and review feature test plan |
| Feature QA - Happy Path Cases | QA To Do | P1 | Generate successful-flow test cases |
| Feature QA - Edge and Negative Cases | QA To Do | P1 | Generate invalid and boundary cases |
| Feature QA - API Validation Plan | QA To Do | P1 | Prepare endpoint validation |
| Feature QA - DB Validation Plan | QA To Do | P2 | Prepare state validation |
| Feature QA - Missing Info Review | Blocked / Needs Clarification | P1 | Confirm incomplete requirements |

---

## 4. Required Human Approval

| Item | Reason |
|---|---|
| Creating Jira tickets | External system action |
| Creating Trello cards | External system action |
| Creating bug reports | Requires validation evidence |
| Assigning P0/P1 priority | Human QA leader approval required |
| Release-related decisions | Execution evidence required |

---

## 5. Draft Quality Rules

Good work-tracking drafts should:

- Be clear
- Be actionable
- Include priority
- Include owner if known
- Include acceptance or done criteria
- Separate tasks, risks, blockers, and bugs
- Avoid claiming execution unless execution happened

---

## 6. Final Note

Generated Jira/Trello drafts are not created tickets.

A human must review and approve them before external creation.
