# Jira Dry-Run Example

## Purpose

This document shows an example Jira dry-run output.

Important rule:

This is not a created Jira ticket.

It is a draft preview that requires human approval before any external action.

---

## 1. Integration Metadata

| Field | Value |
|---|---|
| Integration | Jira |
| Mode | dry_run |
| External Action Taken | No |
| Human Approval Required | Yes |
| Source Feature | User Login |
| Source Artifact | release-readiness-report.md |
| Draft Type | Bug / Risk / QA Task |

---

## 2. Draft Jira Issue

| Field | Draft Value |
|---|---|
| Project Key | QA |
| Issue Type | Bug |
| Priority | P0 |
| Summary | Guest user may access dashboard directly without authentication |
| Labels | qa, security-risk, generated-draft |
| Assignee | Needs Human Assignment |
| Status | Draft Only |

---

## 3. Draft Description

A generated QA planning artifact identified a P0 authorization risk.

Risk:

Guest users may be able to access the dashboard directly if route protection is weak.

Expected behavior:

Unauthenticated users should be redirected to login or shown access denied.

Validation needed:

- Direct URL access test
- API/session authorization validation
- DB no-session validation if applicable

Important:

This is not a confirmed bug.

No execution evidence exists yet.

---

## 4. Evidence Status

| Evidence Type | Available | Notes |
|---|---|---|
| Test execution evidence | No | Scenario has not been executed |
| Screenshot | No | Not available |
| API response log | No | Not available |
| DB evidence | No | Not available |
| Human approval | No | Required before creating Jira issue |

---

## 5. Human Approval Gate

Before creating this Jira issue, a human test leader must confirm:

- The risk classification is valid.
- The issue should be created externally.
- No sensitive information is included.
- The issue wording does not claim confirmed execution.

---

## 6. Safe Action

Recommended action:

Keep as draft until human approval.

---

## 7. Generated vs Executed Note

This Jira dry-run example is a generated draft.

It must not be treated as a created Jira issue or confirmed bug.
