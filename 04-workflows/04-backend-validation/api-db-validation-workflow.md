# Workflow: API and Database Validation

## Purpose

This workflow validates backend API behavior and database state consistency for product features, admin actions, CMS operations, mobile actions, and user flows.

## Owner

API Test Agent

## Main Agents

- API Test Agent
- Database Validation and Data Integrity Agent
- Test Environment and System Health Agent
- Output Reviewer Agent

## Optional Agents

- Backend Integration Test Agent
- Socket and Realtime Test Agent
- Log, Observability and Root Cause Analysis Agent
- Security Vulnerability Scan Agent
- Role, Permission and Session Security Agent

## Input Requirements

Required inputs:

- Product Testing Context
- Test Plan
- API Specification
- Acceptance Criteria
- User Roles
- Business Rules

Optional inputs:

- DB schema
- Expected state changes
- Admin panel flow
- CMS flow
- Socket event catalog
- Previous bug reports
- Logs or failed test outputs

## Main Outputs

- API Validation Plan
- Database Validation Plan
- API-DB Consistency Checks
- Auth and Authorization Checks
- Data Integrity Risk Notes
- Missing Backend Information

## Execution Steps

### Step 1: Environment Health Check

Agent:

- Test Environment and System Health Agent

Output:

- Environment Health Report

Goal:

- Confirm that API, DB and required services are available.

### Step 2: API Scope Analysis

Agent:

- API Test Agent

Input:

- API spec
- Feature scope
- User roles
- Auth rules
- Acceptance criteria

Output:

- API Validation Plan

The plan must include:

- Endpoints covered
- Valid request scenarios
- Invalid request scenarios
- Auth checks
- Authorization checks
- Validation and error handling
- Pagination, sorting and filtering if relevant
- Contract risks

### Step 3: Database Impact Analysis

Agent:

- Database Validation and Data Integrity Agent

Input:

- API actions
- Expected state changes
- DB schema or entity information
- Business rules

Output:

- Database Validation Plan

The plan must include:

- Before state
- After state
- Insert/update/delete checks
- Soft delete checks
- Relationship integrity
- Duplicate and orphan risks
- Transaction risks
- Audit and timestamp checks

### Step 4: API-DB Consistency Mapping

Agents:

- API Test Agent
- Database Validation and Data Integrity Agent

Output:

- API-DB Consistency Matrix

The matrix must show:

- API action
- Expected response
- Expected DB change
- Validation needed
- Risk level

### Step 5: Permission and Session Risk Review

Use optional security agents if the feature includes:

- Admin actions
- Role-based access
- Sensitive data
- Token expiration
- Session behavior
- User-specific data access

### Step 6: Output Review

Agent:

- Output Reviewer Agent

Review:

- API coverage
- DB coverage
- Auth coverage
- Missing information
- Testability
- Risk completeness

## Output Locations

Store outputs under:

- `05-outputs/api-review/`
- `05-outputs/db-review/`
- `05-outputs/risk-analysis/`

## API-DB Consistency Matrix Template

| API Action | Expected API Response | Expected DB State Change | Validation Needed | Priority | Risk |
|---|---|---|---|---|---|

## Quality Gate

The workflow is complete only if:

- API behavior is clear
- Auth and authorization checks are included
- Expected DB state is defined
- API-DB consistency is mapped
- Missing API or DB information is listed
- Risky or destructive validation requires human approval

## Stop Conditions

Stop and request clarification when:

- API spec is missing
- Auth rules are unclear
- Expected DB state is unknown
- Test DB access is unavailable
- Validation would touch production data
- Destructive DB action is required without human approval