# Skill: QA Reporting

## Purpose

Use this skill when creating QA reports, daily summaries, weekly summaries, release readiness summaries, Jira/Trello drafts, executive summaries, or risk reports.

This skill helps the AI produce clear, useful, management-readable QA communication.

## When To Use This Skill

Use this skill when the task includes:

- Daily QA report
- Weekly quality summary
- Release readiness summary
- Risk matrix summary
- Coverage gap summary
- Jira task draft
- Trello card draft
- Executive summary
- Human review summary
- Blocker summary
- Defect triage summary

## Required Inputs

Before generating a QA report, collect as much of the following as possible:

- Product or feature name
- Date
- Generated outputs
- Reviewed outputs
- Executed tests if available
- Blockers
- Risks
- Missing information
- Jira or Trello drafts
- Environment status
- Human notes
- Release scope
- Open defects
- Recommended next actions

If execution did not happen, clearly state that outputs were generated or planned, not executed.

## Core Rules

### Rule 1: Do Not Report Generated Plans as Executed Tests

Generated test cases are not executed tests.

Correct wording:

- Test plan generated
- Test cases generated
- API validation plan prepared
- DB validation plan prepared
- Review completed

Incorrect wording:

- Test passed
- Feature verified
- Execution completed

unless real test execution happened.

### Rule 2: Separate Bugs From Blockers

A bug is incorrect product behavior.

A blocker prevents work from continuing.

Examples of blockers:

- Environment unavailable
- API not deployed
- Test user missing
- Acceptance criteria missing
- DB access unavailable
- Build not installed
- Critical service down

### Rule 3: Keep Reports Management-Readable

Reports should be:

- Short
- Clear
- Risk-focused
- Actionable
- Honest about uncertainty

Do not paste all raw test cases into management reports unless explicitly requested.

### Rule 4: Use Clear Status

Use:

- Green
- Yellow
- Red

Green:

No major blocker or critical risk.

Yellow:

Some risks, partial blockers, unclear requirements, or incomplete coverage.

Red:

Critical blocker, release-impacting risk, security risk, data integrity risk, or urgent human decision needed.

### Rule 5: Always Include Next Actions

Every report must include recommended next actions.

A report without next actions is weak.

### Rule 6: Mark Human Review Items

Human review is required for:

- P0 risks
- Security-sensitive findings
- Destructive DB validation
- Jira/Trello ticket creation
- Release decisions
- Unclear but high-risk assumptions
- Final executive reporting

### Rule 7: Do Not Hide Missing Information

If important information is missing, show it clearly.

## Output Format

Use this format for daily reports:

# Daily Quality Report

## 1. Date

## 2. Overall Status

Use one of:

- Green
- Yellow
- Red

## 3. Executive Summary

## 4. Work Completed Today

| Area | Output | Status | Notes |
|---|---|---|---|

## 5. Test Case Generation Summary

| Type | Count | Notes |
|---|---|---|

## 6. Areas Covered

| Area | Coverage Status | Notes |
|---|---|---|

## 7. Critical Risks

| Risk | Priority | Impact | Recommended Action |
|---|---|---|---|

## 8. Blockers

| Blocker | Type | Impact | Required Action |
|---|---|---|---|

## 9. Jira and Trello Summary

| Item Type | Count | Notes |
|---|---|---|

## 10. Items Needing Human Review

| Item | Reason | Recommended Decision |
|---|---|---|

## 11. Recommended Next Actions

| Action | Owner | Priority |
|---|---|---|

## 12. Human Test Leader Notes

## Output Format for Executive Summary

Use this format:

# Executive QA Summary

## 1. Product or Feature

## 2. Current Quality Status

## 3. What Was Prepared

## 4. Key Risks

## 5. Blockers

## 6. Human Decisions Needed

## 7. Recommended Next Step

## References

When needed, use:

- `08-skills/reporting/README.md`
- `05-outputs/reports/daily-quality-report-template.md`
- `05-outputs/jira-trello/jira-trello-template.md`

## Quality Checklist

Before finalizing, check:

- Is the status clear?
- Are generated and executed outputs separated?
- Are risks visible?
- Are blockers separated from bugs?
- Are next actions specific?
- Are human review items listed?
- Is the report short enough for management?
- Is uncertainty clearly stated?
- Is release impact visible?