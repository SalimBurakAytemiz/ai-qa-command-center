# Skill: Database Validation

## Purpose

Use this skill when designing database validation scenarios, data integrity checks, API-DB consistency checks, or state validation plans.

This skill helps the AI reason about database impact without pretending to execute queries.

## When To Use This Skill

Use this skill when the task includes:

- Database validation planning
- API and DB consistency review
- Data integrity analysis
- Before and after state validation
- Admin action DB impact review
- CMS publish DB impact review
- Mobile action DB impact review
- Socket event DB impact review
- Transaction risk analysis
- Duplicate and orphan record risk analysis
- Audit and timestamp validation

## Required Inputs

Before generating DB validation scenarios, collect as much of the following as possible:

- Feature description
- Acceptance criteria
- Business rules
- API action
- Trigger action
- Expected state change
- Entity names
- Table names if available
- Database schema if available
- User roles
- Test data
- Relationship rules
- Audit requirements
- Soft delete rules
- Transaction rules

If schema or table names are unknown, use entity names and list schema as missing information.

## Core Rules

### Rule 1: Always Define Before and After State

Every DB validation scenario must include:

- Before state
- Trigger action
- After state
- Expected database result

### Rule 2: Do Not Invent Schema

Do not invent table names, column names, relationships, or constraints.

If not provided, write:

Schema details need confirmation.

### Rule 3: Mark Risky Operations

Human approval is required for:

- Delete validation
- Bulk update validation
- Migration validation
- Production data usage
- Payment or financial data validation
- Security-sensitive user data validation

### Rule 4: Separate API Testing From DB Validation

Do not create API-only test cases.

If endpoint behavior needs validation, recommend the API Test Agent.

### Rule 5: Consider Data Integrity Risks

Always consider:

- Duplicate records
- Orphan records
- Wrong owner ID
- Wrong status
- Missing audit data
- Missing timestamp
- Broken relationship
- Partial update
- Incorrect rollback
- Stale cache
- Stale realtime data

### Rule 6: Consider Transaction Risks

For multi-step operations, check:

- All changes are committed together
- Failed operation rolls back correctly
- Retry does not create duplicates
- Concurrent actions do not corrupt state
- Partial state is not left behind

### Rule 7: Consider Audit and Timestamp Fields

When relevant, check:

- created_at
- updated_at
- deleted_at
- created_by
- updated_by
- deleted_by
- status_changed_at
- audit log record
- admin action log

### Rule 8: Do Not Claim Execution

A DB validation plan is not an executed DB validation result.

Use:

- Database validation plan generated
- DB scenarios prepared
- DB impact reviewed

Do not use:

- DB validation passed
- Database verified
- Query executed successfully

unless actual execution evidence exists.

## Scenario Types

Use:

- Insert Validation
- Update Validation
- Delete Validation
- Soft Delete Validation
- State Transition
- Relationship Integrity
- Unique Constraint
- Foreign Key
- Nullability
- Duplicate Risk
- Orphan Record Risk
- Transaction Consistency
- Rollback
- Audit Validation
- Timestamp Validation
- API-DB Consistency
- UI-DB Consistency
- CMS-DB Consistency
- Socket-DB Consistency
- Concurrency

## Output Format

Use this format:

# Database Validation Plan

## 1. Scope Summary

## 2. Missing Information

| Missing Item | Why Needed | Impact |
|---|---|---|

## 3. Entities or Tables Covered

| Entity or Table | Purpose | Related Flow | Priority |
|---|---|---|---|

## 4. Expected State Changes

| Action | Before State | Trigger | After State | Priority | Notes |
|---|---|---|---|---|---|

## 5. Database Validation Scenarios

| ID | Type | Entity or Table | Trigger Action | Priority | Preconditions | Validation Steps | Expected Database State | Risk | Notes |
|---|---|---|---|---|---|---|---|---|---|

## 6. API, UI, CMS, or Socket Consistency Checks

| Source | Expected Database Impact | Validation Needed | Priority |
|---|---|---|---|

## 7. Transaction and Concurrency Risks

| Risk | Impact | Recommended Validation |
|---|---|---|

## 8. Duplicate and Orphan Record Risks

| Risk | Trigger | Recommended Validation |
|---|---|---|

## 9. Audit and Timestamp Checks

| Field or Log | Expected Behavior | Priority |
|---|---|---|

## 10. Human Approval Needed

| Scenario | Reason |
|---|---|

## 11. Recommended Specialist Agents

| Agent | Reason |
|---|---|

## 12. Human Test Leader Notes

## References

When needed, use:

- `references/patterns/db-validation-patterns.md`
- `references/anti-patterns/testing-anti-patterns.md`
- `08-skills/db-validation/README.md`

## Quality Checklist

Before finalizing, check:

- Is before state clear?
- Is after state clear?
- Is trigger action clear?
- Are entities or tables identified?
- Are missing schema details listed?
- Are duplicate risks considered?
- Are orphan risks considered?
- Are transaction risks considered?
- Are audit and timestamp checks included?
- Are risky operations marked for human approval?
- Is execution language avoided unless real execution happened?