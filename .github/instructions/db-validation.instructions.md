# Database Validation Instructions

## Purpose

Use these instructions when creating, reviewing, or improving database validation plans.

These instructions apply to API-DB consistency, UI-DB consistency, data integrity, transaction behavior, duplicate risks, orphan record risks, audit validation, and timestamp validation.

## Core Rules

1. Do not invent database schema.
2. Do not invent table names, column names, relationships, or constraints.
3. If schema is missing, use entity-level language and mark schema as Missing Information.
4. Every DB validation scenario must include before state, trigger action, and after state.
5. Do not claim DB execution unless real query execution evidence exists.
6. Mark destructive validation as human approval required.
7. Always consider duplicate records, orphan records, wrong ownership, timestamps, and audit risks.
8. Separate API behavior from DB validation.
9. Recommend API Test Agent when endpoint behavior needs deeper validation.
10. Prefer synthetic test data and safe test environments.

## Required Inputs

Collect or identify:

- Feature or flow name
- Trigger action
- Expected state change
- Entity or table names if available
- Schema details if available
- User role
- Test data
- Relationship rules
- Audit requirements
- Soft delete rules
- Transaction rules

## Before / Trigger / After Rule

Every DB scenario should include:

- Before State
- Trigger Action
- After State
- Expected Database State

If these cannot be defined, the DB validation scenario is not ready.

## Human Approval Required

Human approval is required for:

- Production data usage
- Destructive delete validation
- Bulk update validation
- Migration validation
- Payment or financial data validation
- Security-sensitive user data validation
- Sensitive personal data validation

## Output Format

Use this structure:

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

## 11. Human Test Leader Notes

## References

Use these repository references when relevant:

- references/patterns/db-validation-patterns.md
- references/examples/db-validation-examples.md
- references/anti-patterns/testing-anti-patterns.md
- .github/skills/db-validation/SKILL.md
