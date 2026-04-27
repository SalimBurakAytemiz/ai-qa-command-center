# Slack Dry-Run Example

## Purpose

This document shows an example Slack dry-run message.

Important rule:

This is not a sent Slack message.

It is a draft preview that requires human approval before sending.

---

## 1. Integration Metadata

| Field | Value |
|---|---|
| Integration | Slack |
| Mode | dry_run |
| External Action Taken | No |
| Human Approval Required | Yes |
| Source Feature | Content Publishing |
| Source Artifact | daily-quality-report.md |
| Draft Type | Daily QA Summary |

---

## 2. Draft Slack Message

Channel:

#qa-updates

Message:

AI QA Command Center generated a QA planning package for Content Publishing.

Current status: Yellow

Generated artifacts:

- Product testing context
- Test strategy
- Test plan
- Happy path test cases
- Edge and negative test cases
- API validation plan
- DB validation plan
- Release readiness draft

Critical risks:

- Guest may access CMS directly
- Registered user may publish through API
- Draft content may be publicly visible
- Unauthorized action may change DB state

Blockers:

- CMS routes need confirmation
- API schema needs confirmation
- DB schema needs confirmation
- Editor publish permission needs confirmation

Important:

No tests have been executed yet.

This is a generated planning summary, not a QA pass result.

---

## 3. Approval Checklist

Before sending, confirm:

- Message does not contain secrets.
- Message does not contain customer personal data.
- Message does not claim tests passed.
- Message does not claim release readiness.
- Human test leader approves sending.

---

## 4. Safe Action

Recommended action:

Keep as draft until human approval.

---

## 5. Generated vs Executed Note

This Slack dry-run example is a generated draft.

It must not be treated as a sent message or executed QA report.
