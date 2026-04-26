# Workflow: Test Case Generation

## Purpose

This workflow generates structured happy path, edge case, negative case, product flow, and feature validation outputs from product context and test strategy.

## Owner

Test Planning Agent

## Main Agents

- Test Planning Agent
- Happy Path Test Case Agent
- Edge Case and Negative Case Agent
- Product Flow Test Agent
- Feature Validation Agent
- Output Reviewer Agent

## Input Requirements

Required inputs:

- Product Testing Context
- Test Strategy
- Acceptance Criteria
- User Roles
- Product Modules
- Platform List
- Business Rules

Optional inputs:

- Previous defects
- Release notes
- API specs
- DB impact notes
- Figma notes
- Human test leader notes

## Main Outputs

- Test Plan
- Happy Path Test Cases
- Edge Case Test Cases
- Negative Case Test Cases
- Product Flow Validation
- Feature Validation Plan
- Risk Matrix
- Automation Candidate Summary

## Execution Steps

### Step 1: Create Test Plan

Agent:

- Test Planning Agent

Output:

- Test Plan

The test plan must define:

- Scope
- Platforms
- User roles
- Critical flows
- Required test types
- Risk areas
- Test data needs
- Environment needs
- Automation candidate areas

### Step 2: Generate Happy Path Test Cases

Agent:

- Happy Path Test Case Agent

Input:

- Test Plan
- Acceptance Criteria
- Critical User Journeys
- User Roles

Output:

- Happy Path Test Cases

Rules:

- Only successful expected flows
- No edge cases
- No negative cases
- Clear expected results
- Automation candidate marking

### Step 3: Generate Edge and Negative Cases

Agent:

- Edge Case and Negative Case Agent

Input:

- Test Plan
- Business Rules
- Acceptance Criteria
- Known Risks
- Permission Rules

Output:

- Edge Case Test Cases
- Negative Case Test Cases

Rules:

- Separate edge cases from negative cases
- Include permission, session, API, DB and state risks when relevant
- Expected rejection behavior must be clear

### Step 4: Validate Product Flow

Agent:

- Product Flow Test Agent

Input:

- Test Plan
- Product Context
- Critical User Journeys

Output:

- Product Flow Validation

Rules:

- Focus on end-to-end user journeys
- Identify broken flow risks
- Identify cross-module dependencies
- Mention specialist agents when needed

### Step 5: Validate Feature Coverage

Agent:

- Feature Validation Agent

Input:

- Feature Description
- Acceptance Criteria
- Business Rules
- Generated Test Cases

Output:

- Feature Validation Plan

Rules:

- Map acceptance criteria to validation scenarios
- Identify missing or unclear requirements
- Separate UI, API, DB, notification and analytics validation needs

### Step 6: Review Outputs

Agent:

- Output Reviewer Agent

Input:

- Test Plan
- Happy Path Test Cases
- Edge Case Test Cases
- Negative Case Test Cases
- Product Flow Validation
- Feature Validation Plan

Output:

- Output Review Report

Review dimensions:

- Completeness
- Duplicates
- Testability
- Expected result clarity
- Risk coverage
- Format compliance

## Output Locations

Store outputs under:

- `05-outputs/test-plans/`
- `05-outputs/happy-path/`
- `05-outputs/edge-cases/`
- `05-outputs/negative-cases/`
- `05-outputs/test-cases/`
- `05-outputs/risk-analysis/`

## Quality Gate

The workflow is complete only if:

- Happy path and negative cases are not mixed
- Edge cases are realistic
- Test cases are executable
- Expected results are observable
- Acceptance criteria are mapped
- Missing information is clearly listed
- Output Reviewer Agent approves or provides revision notes

## Stop Conditions

Stop and request clarification when:

- Acceptance criteria are missing
- User roles are unclear
- Feature behavior is ambiguous
- Expected result cannot be defined
- Required test data is unknown