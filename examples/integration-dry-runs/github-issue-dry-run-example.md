# GitHub Issue Dry-Run Example

## Purpose

This document shows an example GitHub issue dry-run output.

Important rule:

This is not a created GitHub issue.

It is a draft preview that requires human approval before any external action.

---

## 1. Integration Metadata

| Field | Value |
|---|---|
| Integration | GitHub Issues |
| Mode | dry_run |
| External Action Taken | No |
| Human Approval Required | Yes |
| Source Feature | Content Publishing |
| Source Artifact | edge-negative-test-cases.md |
| Draft Type | QA Risk / Bug Candidate |

---

## 2. Draft GitHub Issue

| Field | Draft Value |
|---|---|
| Repository | owner/repository |
| Issue Type | Bug Candidate |
| Title | Draft content should not be visible publicly |
| Labels | qa, security-risk, generated-draft |
| Milestone | Needs Human Decision |
| Assignee | Needs Human Assignment |

---

## 3. Draft Body

## Summary

Generated QA planning identified a P0 risk:

Draft content may become publicly visible if public content routes do not enforce content status.

## Expected Behavior

Draft content should not be visible to guest or registered users.

Public content routes should return an approved response such as 404 or 403 depending on product rules.

## Validation Needed

- Create draft content
- Attempt to access public slug as guest
- Attempt to access public slug as registered user
- Confirm API behavior
- Confirm DB state remains Draft

## Evidence Status

No execution evidence exists yet.

This is a generated QA risk draft, not a confirmed bug.

## Human Approval Required

A human test leader must approve issue creation.

---

## 4. Safety Checks

| Check | Status |
|---|---|
| Contains secrets | No |
| Contains customer data | No |
| Claims execution | No |
| Claims confirmed bug | No |
| Requires approval | Yes |

---

## 5. Generated vs Executed Note

This GitHub issue dry-run example is a generated draft.

It must not be treated as a created GitHub issue or confirmed defect.
