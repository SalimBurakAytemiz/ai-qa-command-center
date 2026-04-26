# Workflow: Product to Test Pack

## Purpose

This workflow converts product information into a complete QA starter package.

It is the main workflow for turning product context, PRD, Figma notes, API documentation, backend notes, mobile notes, CMS details, Firebase events, and acceptance criteria into structured QA outputs.

## Main Output

The workflow must produce:

- Product testing context
- Test strategy
- Agent routing plan
- Compact context packages
- Test plan
- Happy path test cases
- Edge case test cases
- Negative test cases
- Feature validation plan
- Web functional validation plan
- API validation plan
- Database validation plan
- Jira or Trello work tracking drafts
- Daily quality report

## Workflow Owner

Human Test Leader

## Required Management Agents

1. Product Intake Agent
2. Test Strategy Agent
3. Task Router Agent
4. Token Controller Agent
5. Output Reviewer Agent

## Required Phase 1 Specialist Agents

1. Test Planning Agent
2. Happy Path Test Case Agent
3. Edge Case and Negative Case Agent
4. Product Flow Test Agent
5. Feature Validation Agent
6. Web Functional Test Agent
7. API Test Agent
8. Database Validation and Data Integrity Agent
9. Test Environment and System Health Agent
10. Jira and Trello Work Tracking Agent
11. Daily Quality Report Agent

## Input Requirements

The workflow can start with one or more of the following:

- Product overview
- PRD
- Feature description
- Acceptance criteria
- Figma notes
- API specs
- Backend documentation
- Frontend documentation
- Mobile documentation
- CMS documentation
- Firebase event list
- Release notes
- Human test leader instruction

## Execution Order

### Step 1: Product Intake

Agent:

- Product Intake Agent

Input:

- Raw product information
- PRD
- Figma notes
- Technical notes
- Acceptance criteria

Output:

- Product Testing Context

Goal:

- Convert raw information into compact test-ready context.

### Step 2: Test Strategy

Agent:

- Test Strategy Agent

Input:

- Product Testing Context
- Business goals
- Acceptance criteria
- Platform list
- Known risks

Output:

- Test Strategy

Goal:

- Define test scope, risk level, affected platforms, required test types, and recommended teams.

### Step 3: Agent Routing

Agent:

- Task Router Agent

Input:

- Product Testing Context
- Test Strategy
- Feature scope
- Risk matrix

Output:

- Agent Routing Plan

Goal:

- Select only the required agents and avoid unnecessary token usage.

### Step 4: Context Reduction

Agent:

- Token Controller Agent

Input:

- Product Testing Context
- Test Strategy
- Agent Routing Plan
- Target agent name
- Target task

Output:

- Compact Context Package for each target agent

Goal:

- Send only relevant information to each specialist agent.

### Step 5: Environment Readiness

Agent:

- Test Environment and System Health Agent

Input:

- Environment config
- Service list
- Build/deployment notes

Output:

- Environment Health Report

Goal:

- Confirm whether QA execution can start and identify blocked areas.

### Step 6: Test Planning

Agent:

- Test Planning Agent

Input:

- Product Testing Context
- Test Strategy
- Compact Context Package

Output:

- Test Plan

Goal:

- Create a structured, risk-based test plan.

### Step 7: Test Case Generation

Agents:

- Happy Path Test Case Agent
- Edge Case and Negative Case Agent
- Product Flow Test Agent
- Feature Validation Agent

Input:

- Test Plan
- Product Testing Context
- Acceptance criteria
- Business rules

Output:

- Happy path test cases
- Edge case test cases
- Negative case test cases
- Product flow validation
- Feature validation plan

Goal:

- Produce actionable test coverage.

### Step 8: Web, API and DB Validation

Agents:

- Web Functional Test Agent
- API Test Agent
- Database Validation and Data Integrity Agent

Input:

- Test Plan
- Feature validation plan
- API specs
- Expected state changes
- Platform requirements

Output:

- Web functional validation
- API validation plan
- Database validation plan

Goal:

- Cover the first full-stack validation layer.

### Step 9: Output Review

Agent:

- Output Reviewer Agent

Input:

- All generated outputs
- Expected templates
- Test strategy
- Product context

Output:

- Output Review Report

Goal:

- Validate clarity, completeness, duplication, actionability, risk coverage, and format compliance.

### Step 10: Work Tracking Drafts

Agent:

- Jira and Trello Work Tracking Agent

Input:

- Test plan
- Test cases
- Risks
- Review report
- Blockers

Output:

- Jira task drafts
- Trello card drafts
- Checklist items
- Status update comment

Goal:

- Prepare work tracking outputs for human review.

### Step 11: Daily Quality Report

Agent:

- Daily Quality Report Agent

Input:

- All workflow outputs
- Jira/Trello drafts
- Blockers
- Human notes

Output:

- Daily Quality Report

Goal:

- Provide management-readable QA status.

## Human Approval Gates

Human approval is required for:

- Release blocker classification
- Security-sensitive findings
- Production data usage
- Destructive DB validation
- Jira/Trello ticket creation
- Release go/no-go decision
- Any unclear high-risk assumption

## Success Criteria

The workflow is successful when:

- Product context is clear
- Test strategy is risk-based
- Only required agents are selected
- Token usage is controlled
- Test plan is actionable
- Test cases are clear and executable
- API and DB impacts are covered when relevant
- Outputs are reviewed
- Jira/Trello drafts are ready for human approval
- Daily quality report is management-readable

## Failure Conditions

The workflow must stop or request clarification when:

- Product scope is unclear
- Acceptance criteria are missing
- Environment is blocked
- Required API or DB information is unavailable
- Agent outputs fail review
- Human approval is required but not provided

## Final Output Package

The final package should be stored under:

- `05-outputs/test-plans/`
- `05-outputs/happy-path/`
- `05-outputs/edge-cases/`
- `05-outputs/negative-cases/`
- `05-outputs/risk-analysis/`
- `05-outputs/api-review/`
- `05-outputs/db-review/`
- `05-outputs/jira-trello/`
- `05-outputs/reports/`