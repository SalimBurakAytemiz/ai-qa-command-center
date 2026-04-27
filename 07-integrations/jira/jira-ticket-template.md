# Jira Ticket Template

## Purpose

Use this template to prepare Jira ticket drafts from AI QA outputs.

Important rule:

This is a draft template only.

AI agents must not create Jira tickets without explicit human approval.

---

## 1. Ticket Metadata

| Field | Value |
|---|---|
| Project Key | |
| Issue Type | Task / Bug / Risk / Clarification / Story |
| Priority | P0 / P1 / P2 / P3 |
| Severity | Critical / High / Medium / Low |
| Status | Draft |
| Owner | |
| Source Agent | |
| Human Approval Required | Yes |

---

## 2. Title

Write a clear, actionable title.

Bad:

Fix login

Good:

Guest user can access dashboard directly without authentication

---

## 3. Description

Describe the issue, task, risk, or clarification need.

Include:

- Feature or module
- User role
- Platform
- Business impact
- Technical impact
- Risk if unresolved

---

## 4. Preconditions

List required setup.

1.
2.
3.

---

## 5. Steps to Reproduce

Use only for bug drafts.

1.
2.
3.

---

## 6. Actual Result

Use only when execution evidence exists.

If no execution happened, write:

Not executed. This is a generated draft.

---

## 7. Expected Result

Describe the observable expected behavior.

---

## 8. Acceptance or Done Criteria

| Criteria | Notes |
|---|---|
| | |

---

## 9. Evidence

| Evidence Type | Link or Note |
|---|---|
| Screenshot | |
| Video | |
| API response | |
| Logs | |
| DB evidence | |

---

## 10. Related Risks

| Risk | Priority | Notes |
|---|---|---|
| | | |

---

## 11. Human Approval

| Approval Item | Required | Reason |
|---|---|---|
| Create Jira ticket | Yes | External system action |
| P0/P1 priority | If applicable | Human QA leader approval |
| Security-sensitive issue | If applicable | Human review required |
| Release-impacting decision | If applicable | Human review required |

---

## 12. Final Note

Generated Jira drafts are not created Jira tickets.

Human approval is required before external creation.
