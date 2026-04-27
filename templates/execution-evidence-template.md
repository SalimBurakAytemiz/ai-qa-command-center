# Execution Evidence Template

## 1. Purpose

This template defines how real test execution evidence should be documented.

Use this template only when actual manual or automated execution has happened.

Generated QA plans, test cases, API plans, DB plans, automation drafts, or release readiness drafts are not execution evidence.

---

## 2. Evidence Metadata

| Field | Value |
|---|---|
| Feature | |
| Test Area | |
| Test Case ID | |
| Execution Type | Manual / Automated / API / DB / Performance / Mobile |
| Executor | |
| Execution Date | |
| Environment | |
| Build / Version | |
| Evidence Status | Draft / Reviewed / Approved |
| Reviewer | |
| Review Date | |

---

## 3. Execution Summary

Describe what was executed.

Include:

- Scope executed
- What was not executed
- Environment used
- Test data used
- Any limitations

---

## 4. Preconditions

| Preconditions | Status | Notes |
|---|---|---|
| Test environment available | Pending / Confirmed | |
| Test user available | Pending / Confirmed | |
| Required data prepared | Pending / Confirmed | |
| Required permissions available | Pending / Confirmed | |
| External systems approved | Pending / Confirmed / Not Applicable | |

---

## 5. Execution Steps and Results

| Step | Action | Expected Result | Actual Result | Status | Evidence Link / Notes |
|---:|---|---|---|---|---|
| 1 | | | | Pending / Passed / Failed / Blocked | |
| 2 | | | | Pending / Passed / Failed / Blocked | |
| 3 | | | | Pending / Passed / Failed / Blocked | |

---

## 6. Evidence Attachments

| Evidence Type | Location / Link | Notes |
|---|---|---|
| Screenshot | | |
| Video | | |
| API response log | | |
| DB query result | | |
| CI run | | |
| Test report | | |
| Performance report | | |
| Mobile device log | | |

Do not attach secrets, tokens, production credentials, customer personal data, or sensitive logs.

---

## 7. Defects Found

| Defect ID | Summary | Severity | Priority | Status | Link |
|---|---|---|---|---|---|
| | | | | | |

If no defects were found, write:

No confirmed defects were found during this execution.

Do not convert planned risks into confirmed bugs without execution evidence.

---

## 8. Blockers

| Blocker | Impact | Owner Needed | Required Action |
|---|---|---|---|
| | | | |

---

## 9. Result Summary

| Result Type | Count |
|---|---:|
| Passed | 0 |
| Failed | 0 |
| Blocked | 0 |
| Not Run | 0 |

Overall execution result:

- Passed
- Failed
- Blocked
- Partial
- Inconclusive

---

## 10. Human Review

| Review Item | Status | Reviewer Notes |
|---|---|---|
| Evidence reviewed | Pending / Approved / Needs Revision | |
| Sensitive data removed | Pending / Approved / Needs Revision | |
| Result wording safe | Pending / Approved / Needs Revision | |
| Release impact reviewed | Pending / Approved / Needs Revision | |

---

## 11. Release Impact

Describe whether this execution affects release readiness.

Allowed wording:

- Execution evidence supports the tested scope.
- Execution evidence is incomplete.
- Release readiness still requires human approval.
- Additional execution is required.

Do not write release-ready unless release approval has actually happened.

---

## 12. Final Evidence Note

This document records real execution evidence only if the listed execution actually occurred.

If this file was generated as a draft before execution, mark all results as Pending and do not claim pass/fail status.
