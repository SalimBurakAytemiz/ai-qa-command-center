# Workflow: Daily Quality Report

## Purpose

This workflow converts daily AI QA activity into a short, management-readable quality report.

The report should help the human test leader, QA team, product team, and management understand current quality status, risks, blockers, and next actions.

## Owner

Daily Quality Report Agent

## Main Agents

- Daily Quality Report Agent
- Jira and Trello Work Tracking Agent
- Output Reviewer Agent

## Input Sources

Possible inputs:

- Product Testing Context
- Test Plan
- Happy Path Test Cases
- Edge Case Test Cases
- Negative Case Test Cases
- Product Flow Validation
- Feature Validation Plan
- Web Functional Validation
- API Validation Plan
- Database Validation Plan
- Environment Health Report
- Risk Matrix
- Jira/Trello Drafts
- Human Test Leader Notes

## Main Output

Daily Quality Report

## Execution Steps

### Step 1: Collect Daily Outputs

Collect outputs generated during the day from:

- `05-outputs/test-plans/`
- `05-outputs/happy-path/`
- `05-outputs/edge-cases/`
- `05-outputs/negative-cases/`
- `05-outputs/api-review/`
- `05-outputs/db-review/`
- `05-outputs/risk-analysis/`
- `05-outputs/jira-trello/`

### Step 2: Summarize Work Completed

Agent:

- Daily Quality Report Agent

Summarize:

- What was analyzed
- What test cases were generated
- What risks were found
- Which areas were covered
- Which areas are still missing

### Step 3: Separate Risks and Blockers

Separate:

- Product risks
- Environment blockers
- Missing information
- Release-impacting risks
- Human approval items

### Step 4: Summarize Jira and Trello Work

Agent:

- Jira and Trello Work Tracking Agent

Summarize:

- Test task drafts
- Bug drafts
- Checklist items
- Release blocker candidates
- Items needing human approval

### Step 5: Determine Overall Status

Use one of:

- Green
- Yellow
- Red

Status rules:

- Green: No major blocker or critical risk
- Yellow: Partial blocker, unclear requirement, or moderate risk
- Red: Critical blocker, release-impacting risk, or test execution blocked

### Step 6: Create Recommended Next Actions

Create specific next actions:

- What must be clarified
- What must be tested next
- What must be reviewed by human test leader
- What must be assigned to development, QA, product, or management

### Step 7: Review Report

Agent:

- Output Reviewer Agent

Check:

- Clarity
- Management readability
- Risk visibility
- Missing sections
- Overly long content
- Unclear next actions

## Output Location

Store final report under:

`05-outputs/reports/daily-quality-report-YYYY-MM-DD.md`

## Daily Report Template

Use:

`05-outputs/reports/daily-quality-report-template.md`

## Quality Gate

The workflow is complete only if:

- Overall status is clear
- Critical risks are visible
- Blockers are separated from product bugs
- Next actions are specific
- Human review items are listed
- Report is short enough to send daily

## Stop Conditions

Stop and request clarification when:

- No outputs exist
- Product or feature name is unknown
- Risk status cannot be determined
- Human decision is required before reporting