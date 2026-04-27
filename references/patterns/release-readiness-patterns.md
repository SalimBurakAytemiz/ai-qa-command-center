# Release Readiness Patterns

## Purpose

This document defines practical release readiness patterns for AI QA agents.

Use this reference when creating release readiness reports, executive summaries, daily quality reports, output reviews, and risk-based release recommendations.

Important rule:

AI agents may prepare release readiness drafts, but they must not make final release go/no-go decisions without human approval.

---

## 1. Release Readiness Status

Use these status values:

| Status | Meaning |
|---|---|
| Green | No major blocker or critical risk identified |
| Yellow | Some risks, blockers, missing information, or incomplete validation exist |
| Red | Critical blocker, P0 risk, severe data/security risk, or execution blocker exists |

Do not use Green if execution has not happened and important information is missing.

---

## 2. Generated vs Executed Rule

Generated planning artifacts are not release evidence.

Correct wording:

- Release readiness draft prepared
- Test plan generated
- Test cases generated
- API validation plan prepared
- DB validation plan prepared
- Risks identified
- Human approval required

Forbidden without evidence:

- Release ready
- Testing completed
- Feature verified
- Tests passed
- Execution completed
- Production safe

---

## 3. Release Readiness Inputs

A release readiness report should consider:

| Input | Required | Notes |
|---|---|---|
| Test strategy | Yes | Defines risk and scope |
| Test plan | Yes | Defines coverage |
| Test case results | Required for execution readiness | Must separate generated from executed |
| API validation results | If API in scope | Planning is not execution |
| DB validation results | If DB in scope | Requires safe environment |
| Bug list | Yes | Must include severity and priority |
| Blocker list | Yes | Must separate blockers from bugs |
| Risk matrix | Yes | Must include P0/P1 risks |
| Environment status | Yes | Environment can block release |
| Human approvals | Yes | Required for final decisions |

---

## 4. Release Readiness Report Format

Use this structure:

# Release Readiness Report

## 1. Release or Feature

## 2. Overall Status

Use Green, Yellow, or Red.

## 3. Executive Summary

## 4. Scope Covered

| Area | Covered | Evidence | Notes |
|---|---|---|---|

## 5. Execution Status

| Area | Generated | Reviewed | Executed | Evidence |
|---|---|---|---|---|

## 6. Open Risks

| Risk | Priority | Impact | Status | Required Action |
|---|---|---|---|---|

## 7. Open Blockers

| Blocker | Impact | Owner | Required Action |
|---|---|---|---|

## 8. Known Bugs

| Bug | Severity | Priority | Release Impact | Decision Needed |
|---|---|---|---|---|

## 9. Missing Information

| Missing Item | Impact | Required Owner |
|---|---|---|

## 10. Human Approval Points

| Decision | Reason | Approver |
|---|---|---|

## 11. Recommendation Draft

Use cautious language.

Do not give final go/no-go unless explicitly approved.

---

## 5. Green Status Pattern

Use Green only when:

- Critical test areas are reviewed or executed as required.
- No P0 risks are open.
- No release blockers are open.
- Required test data exists.
- Required environment is stable.
- High-priority bugs are resolved or accepted.
- Human approval points are completed.

Example:

Status: Green

Reason:

No open P0/P1 risks remain. Required validation areas have execution evidence or approved review evidence. Remaining issues are low-risk and accepted by the human test leader.

---

## 6. Yellow Status Pattern

Use Yellow when:

- Generated outputs exist but execution has not started.
- Important implementation details are missing.
- Some risks need review.
- Some blockers are not release-blocking yet.
- Some P1/P2 issues need clarification.
- Human approval is still required.

Example:

Status: Yellow

Reason:

QA planning artifacts are complete, but execution has not started. API status codes, DB schema, and dashboard routes still need confirmation before precise validation.

---

## 7. Red Status Pattern

Use Red when:

- P0 risk exists.
- Critical environment is unavailable.
- Core user flow cannot be tested.
- Unauthorized access risk is open.
- Data integrity risk is unresolved.
- Release decision requires urgent human intervention.

Example:

Status: Red

Reason:

Direct dashboard access by unauthenticated users is possible or strongly suspected, and no execution evidence exists proving route-level protection. This is a P0 access-control risk requiring immediate human review.

---

## 8. Blocker vs Bug in Release Readiness

A blocker prevents testing or release workflow progress.

Examples:

| Blocker | Impact |
|---|---|
| QA environment unavailable | Testing cannot start |
| Test user missing | Core flow cannot be validated |
| API not deployed | API validation blocked |
| DB access unavailable | DB validation blocked |
| Acceptance criteria missing | Expected behavior unclear |

A bug is incorrect product behavior.

Examples:

| Bug | Impact |
|---|---|
| Login returns blank page | User cannot access dashboard |
| Wrong API status returned | Contract mismatch |
| Duplicate records created | Data integrity issue |

Do not mix blockers and bugs.

---

## 9. Human Approval Required

Human approval is required for:

- Final release go/no-go
- P0/P1 risk acceptance
- Security-sensitive findings
- Production data validation
- Destructive DB validation
- External ticket creation
- Release readiness status finalization
- Fallback-generated critical outputs
- Executive summary publication

---

## 10. Release Decision Language

Use this careful language:

Good:

- Based on generated planning artifacts, the current draft status is Yellow.
- Human approval is required before release readiness can be finalized.
- Execution evidence is missing, so release readiness cannot be confirmed.
- P0 risk requires human review before proceeding.

Bad:

- The feature is release ready.
- All tests passed.
- QA verified the feature.
- The system is safe for production.

---

## 11. Release Readiness Quality Checklist

A good release readiness draft should include:

- Feature or release name
- Overall status
- Scope covered
- Execution status
- Evidence distinction
- Open risks
- Open blockers
- Known bugs
- Missing information
- Human approval points
- Recommended next action
- No false execution claims
- No final go/no-go without approval

A bad release readiness draft:

- Claims release ready without evidence
- Ignores blockers
- Ignores missing information
- Does not separate generated and executed work
- Does not mention human approval
- Hides P0/P1 risks
