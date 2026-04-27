# Operator Dashboard Mockup

## Purpose

This mockup defines the main dashboard screen for the AI QA Command Center operator.

The dashboard is not implemented yet.

## Main Goal

The operator dashboard should help the human test leader see:

- Active product or feature
- Current QA workflow status
- Selected agents
- Generated outputs
- Review status
- Open risks
- Blockers
- Human approval points
- Validation status
- Next recommended actions

## Main Dashboard Sections

| Section | Purpose |
|---|---|
| Project / Feature Selector | Choose active product, release, or feature |
| Workflow Status | Show current workflow phase |
| Agent Routing Summary | Show selected agents and why |
| Output Package | Show generated artifacts |
| Quality Review | Show Output Reviewer score and decision |
| Risk Summary | Show P0/P1/P2/P3 risks |
| Blockers | Show environment, data, requirement, or access blockers |
| Human Approval Queue | Show decisions requiring human approval |
| Validation Status | Show local and CI validation status |
| Next Actions | Show recommended next steps |

## Example Dashboard Content

Project: User Login
Status: Yellow

Selected Agents:
- Product Intake Agent
- Test Strategy Agent
- Test Planning Agent
- API Test Agent
- DB Validation Agent
- Output Reviewer Agent

Skipped Agents:
- Native Mobile Agent
- Performance Agent
- Firebase Agent

Output Package:
- Product Context
- Test Strategy
- Test Plan
- Test Cases
- API Plan
- DB Plan
- Jira Drafts
- Daily Report

Quality Review:
- Overall Score: 8.4 / 10
- Decision: Approved with Minor Notes
- Human Approval Required: Yes

Risks and Blockers:
- P0 Risks: 1
- P1 Risks: 3
- Blockers: 2

Human Approval Queue:
- Approve P0 risk classification
- Approve Jira draft creation
- Confirm release readiness decision

Next Actions:
1. Confirm API status codes
2. Confirm DB schema
3. Review generated outputs
4. Decide execution plan

## Important Rules

The dashboard must not imply that generated outputs are executed results.

Use safe labels:

- Generated
- Reviewed
- Needs Revision
- Blocked
- Human Approval Required

Avoid unsafe labels unless execution evidence exists:

- Passed
- Verified
- Tested successfully
- Release ready
