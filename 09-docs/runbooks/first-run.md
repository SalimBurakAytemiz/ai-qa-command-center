# Runbook: First AI QA Workflow Run

## Purpose

This runbook explains how to run the first manual AI QA workflow using the repository structure.

This is not full automation yet.

The goal is to manually use the prompts, templates, and workflows to produce the first QA output package for a product or feature.

## Before You Start

Make sure the repository contains:

- Product context files
- Agent registry
- Management agent prompts
- Phase 1 specialist agent prompts
- Output templates
- Workflow documents
- Skill library
- Prompt and agent guidelines

## First Run Goal

The first run should produce:

1. Product Testing Context
2. Test Strategy
3. Agent Routing Plan
4. Test Plan
5. Happy Path Test Cases
6. Edge Case Test Cases
7. Negative Case Test Cases
8. API Validation Plan
9. Database Validation Plan
10. Jira or Trello Work Tracking Draft
11. Daily Quality Report

## Recommended Test Feature

Start with a simple but important feature.

Good examples:

- Login
- Registration
- Password reset
- Profile update
- CMS content publish
- Admin user update

Do not start with the most complex feature.

## Step 1: Prepare Product Inputs

Add available information into:

- `00-product-context/product-overview.md`
- `00-product-context/user-roles.md`
- `00-product-context/modules.md`
- `01-inputs/prd/`
- `01-inputs/api-specs/`
- `01-inputs/figma/`

Minimum required information:

- Feature name
- Feature purpose
- User roles
- Platforms
- Acceptance criteria
- Expected behavior

## Step 2: Run Product Intake Agent Manually

Open:

`03-prompts/01-management-team/product-intake-agent.md`

Copy the prompt into your AI tool.

Provide:

- Product overview
- Feature description
- Acceptance criteria
- Any relevant technical notes

Expected output:

- Product Testing Context

Save output as:

`05-outputs/reports/product-testing-context.md`

## Step 3: Run Test Strategy Agent

Open:

`03-prompts/01-management-team/test-strategy-agent.md`

Provide:

- Product Testing Context
- Feature description
- Acceptance criteria

Expected output:

- Test Strategy

Save output as:

`05-outputs/reports/test-strategy.md`

## Step 4: Run Task Router Agent

Open:

`03-prompts/01-management-team/task-router-agent.md`

Provide:

- Product Testing Context
- Test Strategy

Expected output:

- Agent Routing Plan

Save output as:

`05-outputs/reports/agent-routing-plan.md`

## Step 5: Run Token Controller Agent

Open:

`03-prompts/01-management-team/token-controller-agent.md`

For each selected specialist agent, provide:

- Product Testing Context
- Test Strategy
- Agent Routing Plan
- Target agent
- Target task

Expected output:

- Compact Context Package

Save outputs under:

`05-outputs/reports/compact-context-packages.md`

## Step 6: Run Test Planning Agent

Open:

`03-prompts/02-test-planning/test-planning-agent.md`

Provide:

- Compact Context Package
- Product Testing Context
- Test Strategy

Expected output:

- Test Plan

Save output as:

`05-outputs/test-plans/first-test-plan.md`

## Step 7: Run Happy Path Test Case Agent

Open:

`03-prompts/02-test-planning/happy-path-test-case-agent.md`

Provide:

- Test Plan
- Acceptance criteria
- Critical user flows

Expected output:

- Happy Path Test Cases

Save output as:

`05-outputs/happy-path/first-happy-path-test-cases.md`

## Step 8: Run Edge Case and Negative Case Agent

Open:

`03-prompts/02-test-planning/edge-negative-case-agent.md`

Provide:

- Test Plan
- Acceptance criteria
- Business rules
- Known risks

Expected output:

- Edge Case Test Cases
- Negative Case Test Cases

Save output as:

`05-outputs/edge-cases/first-edge-cases.md`

`05-outputs/negative-cases/first-negative-cases.md`

## Step 9: Run API Test Agent

Open:

`03-prompts/06-backend-db-realtime/api-test-agent.md`

Provide:

- API spec
- Test Plan
- Acceptance criteria
- User roles

Expected output:

- API Validation Plan

Save output as:

`05-outputs/api-review/first-api-validation.md`

## Step 10: Run Database Validation Agent

Open:

`03-prompts/06-backend-db-realtime/db-validation-agent.md`

Provide:

- API actions
- Expected state changes
- Business rules
- DB schema if available

Expected output:

- Database Validation Plan

Save output as:

`05-outputs/db-review/first-db-validation.md`

## Step 11: Run Output Reviewer Agent

Open:

`03-prompts/01-management-team/output-reviewer-agent.md`

Provide all generated outputs.

Expected output:

- Output Review Report

Save output as:

`05-outputs/reports/first-output-review.md`

## Step 12: Run Jira or Trello Agent

Open:

`03-prompts/09-operations-reporting/jira-trello-agent.md`

Provide:

- Test Plan
- Test Cases
- Risk notes
- Review report

Expected output:

- Jira or Trello Drafts

Save output as:

`05-outputs/jira-trello/first-jira-trello-drafts.md`

## Step 13: Run Daily Quality Report Agent

Open:

`03-prompts/09-operations-reporting/daily-quality-report-agent.md`

Provide:

- Summary of generated outputs
- Risks
- Blockers
- Human notes

Expected output:

- Daily Quality Report

Save output as:

`05-outputs/reports/first-daily-quality-report.md`

## Step 14: Human Review

The human test leader must review:

- Missing information
- P0 and P1 risks
- Jira or Trello drafts
- DB validation risks
- Security-sensitive notes
- Automation candidates
- Final daily report

## Step 15: Commit Outputs if Needed

Do not commit sensitive data.

If outputs are safe and useful for documentation, commit them.

Recommended command:

git status

git add 05-outputs

git commit -m "Add first AI QA workflow outputs"

git push

## Important Warning

Generated outputs are not executed test results.

Do not report generated test plans as executed tests.

Use correct wording:

- Generated
- Planned
- Reviewed
- Executed
- Blocked
- Approved

## First Run Success Criteria

The first run is successful if:

- Product Testing Context exists
- Test Strategy exists
- Agent Routing Plan exists
- Test Plan exists
- Happy path cases exist
- Edge and negative cases exist
- API and DB validation plans exist
- Output review exists
- Jira or Trello drafts exist
- Daily quality report exists
- Human test leader knows the next action

## Common First Run Mistakes

- Starting with too complex a feature
- Skipping Product Intake Agent
- Sending full product documents to every agent
- Not using Token Controller Agent
- Mixing happy path and negative cases
- Treating generated plans as executed tests
- Creating Jira tickets without review
- Ignoring missing information
- Not committing useful repo changes