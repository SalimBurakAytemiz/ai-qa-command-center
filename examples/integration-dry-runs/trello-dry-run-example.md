# Trello Dry-Run Example

## Purpose

This document shows an example Trello dry-run card.

Important rule:

This is not a created Trello card.

It is a draft preview that requires human approval before any external action.

---

## 1. Integration Metadata

| Field | Value |
|---|---|
| Integration | Trello |
| Mode | dry_run |
| External Action Taken | No |
| Human Approval Required | Yes |
| Source Feature | User Login |
| Source Artifact | test-plan.md |
| Draft Type | QA Task |

---

## 2. Draft Trello Card

| Field | Draft Value |
|---|---|
| Board | QA Board |
| List | QA To Do |
| Card Title | Execute login P0 access-control validation |
| Labels | QA, Security, P0, Generated Draft |
| Due Date | Needs Human Decision |
| Members | Needs Human Assignment |

---

## 3. Draft Card Description

Generated QA planning identified P0 access-control validation needs for the login feature.

Required checks:

- Guest cannot access dashboard directly
- Registered user sees only authorized pages
- Disabled user cannot create active session
- Invalid login does not leak account existence
- API authorization behavior is confirmed
- DB no-session behavior is validated if applicable

Important:

This Trello card is only a draft.

No tests have been executed.

No bug has been confirmed.

---

## 4. Checklist Draft

- Confirm test environment
- Confirm test users
- Confirm dashboard routes
- Confirm API status codes
- Confirm DB schema
- Execute P0 access-control tests
- Review evidence
- Decide whether external bug creation is needed

---

## 5. Human Approval Gate

Before creating this Trello card, a human test leader must approve:

- External card creation
- Priority classification
- Card wording
- Evidence status
- Assignment

---

## 6. Generated vs Executed Note

This Trello dry-run example is a generated draft.

It must not be treated as a created Trello card or executed QA task.
