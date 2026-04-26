# Workflow Guidelines

## Purpose

This document defines how workflows should be designed and executed inside the AI QA Command Center.

Workflows describe the order in which agents work together to produce QA outputs.

## Core Workflow Principle

A workflow must move from broad understanding to focused execution.

Correct flow:

1. Understand product context
2. Define strategy
3. Select agents
4. Reduce context
5. Generate specialist outputs
6. Review outputs
7. Prepare reports and work tracking drafts

Incorrect flow:

1. Send the full product document to every agent
2. Ask all agents to produce everything
3. Review a large pile of duplicated outputs

## Standard Workflow Structure

Each workflow document must include:

1. Purpose
2. Owner
3. Main Agents
4. Optional Agents
5. Input Requirements
6. Main Outputs
7. Execution Steps
8. Output Locations
9. Quality Gate
10. Stop Conditions

## Workflow Owners

A workflow must have one owner.

Examples:

- Product Intake Workflow: Product Intake Agent
- Test Case Generation Workflow: Test Planning Agent
- API and DB Validation Workflow: API Test Agent
- Daily Report Workflow: Daily Quality Report Agent
- Release Readiness Workflow: Release Readiness Agent

## Input Requirements

Each workflow must define required inputs.

Bad example:

Use all available information.

Good example:

Required inputs:

- Product Testing Context
- Acceptance Criteria
- User Roles
- Platform List

## Execution Steps

Execution steps must be sequential.

Each step should define:

- Agent
- Input
- Output
- Goal

Example:

Step 1: Product Intake

Agent:

- Product Intake Agent

Input:

- Raw product information

Output:

- Product Testing Context

Goal:

- Convert raw information into compact test-ready context.

## Quality Gates

A quality gate defines when the workflow can continue.

Example:

The workflow can continue only if:

- Product purpose is clear
- At least one platform is identified
- Critical user flows are identified
- Missing information is listed

## Stop Conditions

A workflow must stop or request clarification when key information is missing.

Examples:

- Product scope is unclear
- Acceptance criteria are missing
- Environment is blocked
- API specification is missing
- Expected DB state is unknown
- Human approval is required but not provided

## Human Approval Gates

Human approval is required for:

- Security-sensitive findings
- Destructive DB validation
- Production data usage
- Ticket creation
- P0 severity decision
- Release go or no-go decision
- Any unclear but high-risk assumption

## Token Control in Workflows

Every workflow should use token control.

Recommended pattern:

1. Product Intake Agent creates compact product context.
2. Task Router Agent selects only needed agents.
3. Token Controller Agent prepares target-specific context.
4. Specialist agents work only with compact context.
5. Reporting agents summarize outputs instead of copying raw content.

## Output Locations

Every workflow must specify where outputs should be stored.

Examples:

- `05-outputs/test-plans/`
- `05-outputs/happy-path/`
- `05-outputs/edge-cases/`
- `05-outputs/api-review/`
- `05-outputs/db-review/`
- `05-outputs/reports/`

## Workflow Naming Rules

Workflow files should use lowercase kebab-case.

Good examples:

- product-to-test-pack.md
- api-db-validation-workflow.md
- daily-report-workflow.md

Bad example:

- My Workflow File Final Version.md

## Workflow Design Rules

### Rule 1: Start with context

Never start with test case generation before product context is understood.

### Rule 2: Do not run all agents

Task Router Agent must select only relevant agents.

### Rule 3: Keep specialist work focused

Each specialist agent should receive only the context it needs.

### Rule 4: Review before reporting

Output Reviewer Agent should review important outputs before they are summarized.

### Rule 5: Separate planning from execution

Planning outputs should not pretend that tests were executed.

If tests were only generated, report them as generated, not executed.

### Rule 6: Separate environment blockers from product bugs

Environment Health Agent must help distinguish environment problems from product defects.

### Rule 7: Store final outputs

Important generated outputs must be saved under `05-outputs/`.

## Workflow Review Checklist

Before approving a workflow, check:

- Does it have a clear purpose?
- Does it have one owner?
- Are main agents listed?
- Are optional agents listed?
- Are input requirements clear?
- Are output locations defined?
- Are execution steps sequential?
- Are quality gates defined?
- Are stop conditions defined?
- Are human approval gates defined?
- Does it avoid unnecessary agent execution?
- Does it include token control?