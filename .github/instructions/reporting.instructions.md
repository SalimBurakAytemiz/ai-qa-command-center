# QA Reporting Instructions

## Purpose

Use these instructions when creating, reviewing, or improving QA reports, daily summaries, executive summaries, Jira/Trello summaries, risk reports, or release readiness summaries.

## Core Rules

1. Do not report generated plans as executed tests.
2. Separate generated, planned, reviewed, blocked, executed, and approved states.
3. Separate bugs from blockers.
4. Always include risks.
5. Always include missing information.
6. Always include next actions.
7. Keep management reports short, clear, and actionable.
8. Do not claim release readiness without human approval.
9. Do not create external tickets unless explicitly approved.
10. Mark human approval points clearly.

## Correct Status Words

Use:

- Generated
- Planned
- Reviewed
- Blocked
- Executed
- Approved
- Needs Revision

## Forbidden Without Evidence

Do not use these unless there is real execution evidence:

- Passed
- Verified
- Tested successfully
- Execution completed
- Release ready

## Overall Status Values

Use:

- Green
- Yellow
- Red

Green means no major blocker or critical risk.

Yellow means some risks, partial blockers, missing information, or incomplete coverage.

Red means critical blocker, release-impacting risk, security risk, data integrity risk, or urgent human decision needed.

## Blocker vs Bug Rule

A blocker prevents testing or workflow progress.

A bug is incorrect product behavior.

Do not mix blockers and bugs.

## Daily Report Format

Use this structure:

# Daily Quality Report

## 1. Date

## 2. Overall Status

## 3. Executive Summary

## 4. Work Completed Today

| Area | Output | Status | Notes |
|---|---|---|---|

## 5. Test Case Generation Summary

| Type | Count | Notes |
|---|---:|---|

## 6. Areas Covered

| Area | Coverage Status | Notes |
|---|---|---|

## 7. Critical Risks

| Risk | Priority | Impact | Recommended Action |
|---|---|---|---|

## 8. Blockers

| Blocker | Type | Impact | Required Action |
|---|---|---|---|

## 9. Items Needing Human Review

| Item | Reason | Recommended Decision |
|---|---|---|

## 10. Recommended Next Actions

| Action | Owner | Priority |
|---|---|---|

## 11. Human Test Leader Notes

## Executive Summary Format

Use this structure:

# Executive QA Summary

## 1. Product or Feature

## 2. Current Quality Status

## 3. What Was Prepared

## 4. Key Risks

## 5. Blockers

## 6. Human Decisions Needed

## 7. Recommended Next Step

## 8. Important Note

## Jira/Trello Draft Reporting Rule

Jira/Trello drafts are not created tickets.

Always state:

Human approval is required before creating external tickets or cards.

## References

Use these repository references when relevant:

- .github/skills/qa-reporting/SKILL.md
- 05-outputs/reports/
- 05-outputs/jira-trello/
- examples/outputs/sample-daily-quality-report.md
- examples/outputs/sample-executive-summary.md
- examples/outputs/sample-jira-drafts.md
