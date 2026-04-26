# Prompt Standards

## Purpose

This document defines how prompts must be written inside the AI QA Command Center.

The goal is to keep all agent prompts clear, consistent, reusable, reviewable, and safe for multi-agent QA workflows.

## Core Rule

Every agent prompt must be written as an operational instruction, not as a casual chat message.

A good prompt tells the agent:

- Who it is
- What it must do
- What input it can use
- What it must not do
- What format it must produce
- How quality will be judged

## Standard Prompt Structure

Each agent prompt should include the following sections:

1. Role
2. Purpose
3. Input Sources
4. Main Task
5. Working Rules
6. Output Format
7. Quality Criteria

## 1. Role

The Role section defines the agent identity.

The role must be specific.

Bad example:

You are a tester.

Good example:

You are the Database Validation and Data Integrity Agent in the AI QA Command Center.

## 2. Purpose

The Purpose section defines why the agent exists.

The purpose must be narrow enough to avoid overlapping with other agents.

Good example:

Your purpose is to validate backend API behavior from a quality engineering perspective.

## 3. Input Sources

The Input Sources section defines what information the agent may use.

Good example:

You may receive:

- Product testing context
- API specifications
- Acceptance criteria
- User roles
- Business rules

This prevents agents from assuming unlimited context.

## 4. Main Task

The Main Task section defines the actual work.

The task must be action-oriented.

Good example:

Generate API validation scenarios for the given product, feature, module, or endpoint.

## 5. Working Rules

Working rules prevent bad output.

Common working rules:

- Do not generate automation code unless explicitly requested.
- Do not duplicate other agent responsibilities.
- Do not invent missing information.
- If information is missing, list it clearly.
- Keep the output structured and practical.
- Stay inside your responsibility area.

## 6. Output Format

Output format must be explicit.

Use Markdown tables when the output is intended for human review.

Use JSON only when the output will be processed by automation.

Use YAML only for configuration.

## 7. Quality Criteria

Quality criteria define how the output will be judged.

Good quality criteria should check:

- Is the output actionable?
- Does it follow the expected format?
- Does it avoid duplicate scenarios?
- Does it list missing information clearly?
- Does it stay inside the agent responsibility?

## Prompt Writing Rules

### Rule 1: One agent, one responsibility

Do not make one agent responsible for everything.

Bad example:

Create test cases, write automation, find bugs, generate reports, and decide release readiness.

Good example:

Generate happy path test cases for expected user behavior.

### Rule 2: Prevent responsibility overlap

If another agent owns a task, the current agent should recommend that agent instead of doing the work.

Example:

If deeper database validation is required, recommend the Database Validation Agent.

### Rule 3: Always define what the agent must not do

Negative instructions are important.

Examples:

- Do not generate API-only test cases.
- Do not generate automation code.
- Do not create Jira tickets directly.

### Rule 4: Always include missing information handling

Every agent must be able to say what is missing.

Example:

If API specification is missing, list it under Missing Information.

### Rule 5: Use stable output sections

Do not change output headings randomly.

Stable headings make the system easier to review, automate, and report.

### Rule 6: Separate facts from assumptions

If the agent makes an assumption, it must clearly mark it as an assumption.

### Rule 7: Avoid vague expected results

Bad example:

The system works correctly.

Good example:

The user is redirected to the dashboard and the dashboard displays the logged-in user's name.

### Rule 8: Keep prompts reusable

Prompts should not be written for only one product unless the file is inside a product-specific folder.

### Rule 9: Keep prompts tool-aware but not tool-dependent

An agent may mention a tool category such as Playwright, Appium, JMeter, Jira, or Trello.

However, the prompt should still be usable even if the tool is not connected yet.

### Rule 10: Human decision remains final

No agent should make final release, security, production, or destructive data decisions without human approval.

## Bad Prompt Example

Test this feature and find everything wrong. Also create automation and Jira bugs.

Problems:

- Too broad
- No role
- No input definition
- No output format
- No quality criteria
- No human approval rule

## Good Prompt Example

# API Test Agent

## Role

You are the API Test Agent in the AI QA Command Center.

## Purpose

Your purpose is to validate backend API behavior.

## Main Task

Generate API validation scenarios for the provided endpoint.

## Working Rules

- Do not generate UI test cases.
- Do not generate automation code.
- If API specification is missing, list it under Missing Information.

## Output Format

Use the API Validation Template.

## Quality Criteria

Your output is good only if endpoint behavior, auth, validation, error handling, and missing information are clearly listed.

## Prompt Review Checklist

Before accepting a prompt, check:

- Does it define the agent role?
- Does it define the purpose?
- Does it define input sources?
- Does it define the main task?
- Does it define what not to do?
- Does it define output format?
- Does it define quality criteria?
- Does it avoid overlap with other agents?
- Does it handle missing information?
- Does it preserve human approval for critical decisions?