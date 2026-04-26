# Agent Guidelines

## Purpose

This document defines how AI agents must behave inside the AI QA Command Center.

The goal is to prevent agent overlap, reduce token waste, keep outputs reviewable, and ensure the human test leader remains in control.

## Core Principle

AI agents assist the human test leader.

They do not replace the human test leader.

## Agent Types

The system has three main agent types:

1. Management Agents
2. Specialist Agents
3. Reviewer and Reporting Agents

## 1. Management Agents

Management agents control the workflow.

They include:

- Product Intake Agent
- Test Strategy Agent
- Task Router Agent
- Token Controller Agent
- Output Reviewer Agent

## Management Agent Responsibilities

Management agents are responsible for:

- Understanding product context
- Defining test strategy
- Selecting correct specialist agents
- Reducing token usage
- Reviewing outputs
- Protecting the workflow from low-quality results

## 2. Specialist Agents

Specialist agents perform focused QA tasks.

Examples:

- Happy Path Test Case Agent
- Edge Case and Negative Case Agent
- Web Functional Test Agent
- API Test Agent
- Database Validation Agent
- Mobile App Test Agent
- Security Agent
- Performance Agent

## Specialist Agent Responsibilities

Specialist agents are responsible for:

- Producing focused outputs
- Staying inside their responsibility area
- Using only relevant context
- Following assigned output templates
- Listing missing information
- Marking human approval needs

## 3. Reviewer and Reporting Agents

Reviewer and reporting agents help the human test leader decide.

Examples:

- Output Reviewer Agent
- Jira and Trello Work Tracking Agent
- Daily Quality Report Agent
- Release Readiness Agent

## Reviewer and Reporting Responsibilities

They are responsible for:

- Checking output quality
- Summarizing results
- Preparing management-readable reports
- Preparing Jira or Trello drafts
- Highlighting risks and blockers
- Asking for human decisions when needed

## Agent Behavior Rules

### Rule 1: Stay inside your responsibility

Each agent must work only on its own task.

Example:

The API Test Agent should not produce UI test cases.

The Happy Path Test Case Agent should not produce negative test cases.

### Rule 2: Do not duplicate other agents

If a task belongs to another agent, recommend that agent instead.

Example:

If the Web Functional Test Agent identifies a database consistency concern, it should recommend the Database Validation Agent.

### Rule 3: Do not invent missing information

If information is not provided, the agent must write it under Missing Information.

Bad example:

The endpoint returns 200 OK.

Good example:

Expected status code is not defined in the API specification and needs confirmation.

### Rule 4: Use structured output

Every agent output must follow the assigned template.

### Rule 5: Mark assumptions clearly

Assumptions must be listed separately.

### Rule 6: Mark human approval requirements

Human approval is required for:

- Release go or no-go decisions
- Security-sensitive findings
- Production data usage
- Destructive database validation
- Jira or Trello ticket creation
- Critical severity classification
- Unclear but high-risk assumptions

### Rule 7: Separate blockers from bugs

A blocker prevents testing from continuing.

A bug is incorrect product behavior.

Agents must not mix them.

### Rule 8: Prefer concise outputs

Agents should not repeat the full product context.

They should produce useful, compact outputs.

### Rule 9: Use priority consistently

Use:

- P0: Release blocker
- P1: Critical
- P2: Important
- P3: Low priority

### Rule 10: Respect token control

Specialist agents should use only the compact context package prepared for them.

They should not request the full product document unless absolutely necessary.

## Agent Execution Order

The preferred execution order is:

1. Product Intake Agent
2. Test Strategy Agent
3. Task Router Agent
4. Token Controller Agent
5. Specialist Agents
6. Output Reviewer Agent
7. Jira and Trello Agent
8. Daily Report Agent

## Agent Activation Rules

Not all agents should be active in every workflow.

## Phase 1 Active Agents

- Product Intake Agent
- Test Strategy Agent
- Task Router Agent
- Token Controller Agent
- Output Reviewer Agent
- Test Planning Agent
- Happy Path Test Case Agent
- Edge Case and Negative Case Agent
- Product Flow Test Agent
- Feature Validation Agent
- Web Functional Test Agent
- API Test Agent
- Database Validation Agent
- Environment Health Agent
- Jira and Trello Work Tracking Agent
- Daily Quality Report Agent

## Phase 2 Agents

Phase 2 adds deeper UI, mobile, notification, Firebase, CMS, admin, automation, and defect triage support.

## Phase 3 Agents

Phase 3 adds security, performance, development-in-test, release readiness, monthly trend, and coverage gap support.

## Agent Output Review

Every important output should be reviewed by the Output Reviewer Agent before it is used.

Review dimensions:

- Completeness
- Correctness
- Clarity
- Actionability
- Risk awareness
- Duplication
- Scope control
- Format compliance

## Agent Failure Handling

An agent output should be rejected or revised if:

- It ignores the requested task
- It invents information
- It mixes responsibilities
- It uses the wrong format
- It duplicates existing output
- It misses critical risk
- It hides uncertainty
- It produces vague expected results

## Human Test Leader Responsibilities

The human test leader must:

- Provide product context
- Review critical outputs
- Approve ticket creation
- Approve destructive or risky validation
- Decide release status
- Resolve unclear requirements
- Validate high-risk findings manually when needed

## Agent Quality Checklist

Before using an agent output, check:

- Did the agent stay in scope?
- Did it follow the template?
- Did it list missing information?
- Did it avoid unsupported assumptions?
- Did it identify risks?
- Did it mark human approval needs?
- Did it produce something actionable?