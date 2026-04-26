# Skill: Database Validation

## Purpose

This skill defines how AI QA agents should plan database validation and data integrity checks.

It should be used by:

- Database Validation and Data Integrity Agent
- API Test Agent
- Backend Integration Test Agent
- Product Flow Test Agent
- Output Reviewer Agent

## Database Validation Goals

Database validation must confirm that product actions produce correct and consistent data state.

It should validate:

1. Record creation
2. Record update
3. Record deletion
4. Soft delete behavior
5. State transitions
6. Relationships
7. Constraints
8. Duplicate prevention
9. Orphan record prevention
10. Transaction consistency
11. Rollback behavior
12. Audit fields
13. Timestamp fields
14. User ownership
15. API and DB consistency
16. UI and DB consistency
17. CMS and DB consistency
18. Socket and DB consistency

## Required DB Validation Fields

Each DB validation scenario should include:

- ID
- Entity or Table
- Trigger Action
- Scenario Type
- Priority
- Preconditions
- Before State
- Validation Steps
- Expected Database State
- Risk
- Notes

## Scenario Types

Use these types:

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

## Before and After State

Always define:

### Before State

- Which record should exist?
- Which record should not exist?
- What is the current status?
- What user owns the data?
- What related records exist?

### After State

- What new record should be created?
- What field should be updated?
- What status should change?
- What record should be deleted or soft deleted?
- What audit record should exist?
- What timestamp should change?
- What related data should remain unchanged?

## Data Integrity Risks

Look for:

- Duplicate records
- Orphan records
- Wrong owner ID
- Wrong status
- Missing audit data
- Missing timestamp
- Broken relationship
- Partial update
- Incorrect rollback
- Incorrect soft delete
- Inconsistent cache
- Stale realtime data

## Transaction Checks

For multi-step operations, validate:

- All changes are committed together
- Failed operation rolls back correctly
- Partial data is not left behind
- Retry does not create duplicates
- Concurrent actions do not corrupt state

## Audit Checks

When relevant, validate:

- created_at
- updated_at
- created_by
- updated_by
- deleted_at
- deleted_by
- status_changed_at
- audit log record
- admin action log

## API and DB Consistency

For API-triggered changes, validate:

- API response matches DB state
- API success creates expected state
- API failure does not create invalid state
- API retry does not create duplicate data
- API authorization prevents unauthorized data changes

## UI and DB Consistency

For UI-triggered changes, validate:

- UI shows the same data stored in DB
- UI state matches backend state
- Refresh does not show stale data
- Role-based data visibility is correct

## Safety Rules

Never suggest destructive validation on production data.

Human approval is required for:

- Delete validation
- Bulk update validation
- Data migration validation
- Production-like data validation
- Security-sensitive user data validation
- Payment or financial data validation

## Common Mistakes to Avoid

- Checking only API response and ignoring DB state
- Not defining before state
- Not defining after state
- Ignoring duplicate records
- Ignoring orphan records
- Ignoring audit fields
- Ignoring transaction rollback
- Assuming table names when schema is missing
- Suggesting risky DB operations without human approval

## Review Checklist

Before approving DB validation output, check:

- Is before state clear?
- Is after state clear?
- Are entities or tables listed?
- Are risky operations marked?
- Are transaction risks covered?
- Are duplicate and orphan risks covered?
- Are audit fields covered?
- Is human approval required where needed?