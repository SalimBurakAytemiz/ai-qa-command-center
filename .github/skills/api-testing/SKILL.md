# Skill: API Testing

## Purpose

Use this skill when designing API validation scenarios, reviewing API test coverage, or preparing API testing plans.

This skill helps the AI analyze backend API behavior from a QA engineering perspective.

## When To Use This Skill

Use this skill when the task includes:

- API validation planning
- Endpoint test case design
- OpenAPI or Swagger review
- Request and response validation
- Authentication testing
- Authorization testing
- Role-based access testing
- Error handling review
- Contract risk analysis
- API and DB consistency planning
- API regression planning

## Required Inputs

Before generating API validation scenarios, collect as much of the following as possible:

- API base URL
- Endpoint path
- HTTP method
- Request payload
- Response schema
- Expected status codes
- Authentication rules
- Authorization rules
- User roles
- Business rules
- Acceptance criteria
- Error response format
- Pagination rules
- Sorting rules
- Filtering rules
- Database impact
- Rate limit rules
- Integration dependencies

If any critical API detail is missing, list it under "Missing Information".

## Core Rules

### Rule 1: Do Not Guess Missing API Details

Do not invent:

- Endpoint paths
- HTTP methods
- Request fields
- Response fields
- Status codes
- Auth rules
- Role permissions

If not provided, mark as "Needs Confirmation".

### Rule 2: Separate API Testing From UI Testing

Do not create UI test cases.

If UI validation is needed, recommend the Web Functional Test Agent.

### Rule 3: Always Cover Authentication

For protected endpoints, consider:

- No token
- Invalid token
- Expired token
- Valid token
- Token refresh
- Logout and token invalidation

### Rule 4: Always Cover Authorization

For role-based systems, consider:

- Correct role can access endpoint
- Wrong role receives forbidden response
- Normal user cannot access admin endpoint
- User cannot access another user's data
- Super admin-only action rejects lower roles

### Rule 5: Cover Request Validation

Consider:

- Missing required field
- Null field
- Empty string
- Invalid data type
- Invalid enum
- Invalid date
- Invalid ID
- Very long string
- Boundary value
- Duplicate request
- Unexpected extra field

### Rule 6: Cover Response Validation

Consider:

- Correct status code
- Correct response schema
- Required fields exist
- Field types are correct
- Sensitive data is not exposed
- Error response format is consistent
- Response belongs to correct user
- Pagination metadata is correct

### Rule 7: Cover Error Handling

For failures, define:

- Expected status code
- Expected error message
- Expected error code if available
- Field-level validation details if available

If error format is missing, list it as missing information.

### Rule 8: Mention Database Impact

For state-changing APIs, identify expected DB impact.

Examples:

- Record created
- Record updated
- Record deleted
- Soft delete applied
- Status changed
- Audit log created
- Timestamp updated
- Duplicate prevented

Do not perform DB validation directly. Recommend the Database Validation Agent when needed.

### Rule 9: Do Not Claim Execution

An API validation plan is not an executed API test result.

Use:

- API validation plan generated
- API scenarios prepared
- API coverage reviewed

Do not use:

- API tests passed
- Endpoint verified
- API execution completed

unless real execution evidence exists.

## API Scenario Types

Use:

- Valid Request
- Invalid Request
- Missing Required Field
- Invalid Field Type
- Invalid Enum
- Auth Required
- Unauthorized
- Forbidden
- Expired Token
- Role-Based Access
- Not Found
- Conflict
- Validation Error
- Pagination
- Sorting
- Filtering
- Contract
- State Change
- Timeout
- Retry
- Idempotency

## Status Code Guidance

Use expected status codes only when supported by specification or requirement.

Common values:

- 200 OK
- 201 Created
- 204 No Content
- 400 Bad Request
- 401 Unauthorized
- 403 Forbidden
- 404 Not Found
- 409 Conflict
- 422 Unprocessable Entity
- 429 Too Many Requests
- 500 Internal Server Error

If not defined, use:

Needs Confirmation

## Output Format

Use this format:

# API Validation Plan

## 1. Scope Summary

## 2. Missing Information

| Missing Item | Why Needed | Impact |
|---|---|---|

## 3. Endpoints Covered

| Endpoint | Method | Purpose | Auth Required | Priority |
|---|---|---|---|---|

## 4. API Test Scenarios

| ID | Type | Endpoint | Method | Priority | User Role | Preconditions | Request Data | Expected Status | Expected Response | Notes |
|---|---|---|---|---|---|---|---|---|---|---|

## 5. Authentication Checks

| Scenario | Endpoint | Expected Status | Notes |
|---|---|---|---|

## 6. Authorization Checks

| User Role | Endpoint | Expected Access | Expected Status | Notes |
|---|---|---|---|---|

## 7. Request Validation Checks

| Field or Rule | Invalid Case | Expected Error | Priority |
|---|---|---|---|

## 8. Pagination, Sorting and Filtering Checks

| Area | Scenario | Expected Behavior | Priority |
|---|---|---|---|

## 9. Contract Risks

| Risk | Impact | Recommended Validation |
|---|---|---|

## 10. Database Impact Notes

| API Action | Expected Database Impact | DB Validation Needed |
|---|---|---|

## 11. Integration Dependency Notes

| Dependency | Risk | Recommended Validation |
|---|---|---|

## 12. Recommended Specialist Agents

| Agent | Reason |
|---|---|

## 13. Human Test Leader Notes

## References

When needed, use:

- `references/patterns/api-testing-patterns.md`
- `references/anti-patterns/testing-anti-patterns.md`
- `08-skills/api-testing/README.md`

## Quality Checklist

Before finalizing, check:

- Are endpoints clearly listed?
- Are methods correct?
- Are auth cases included?
- Are authorization cases included?
- Are invalid request cases included?
- Are expected status codes not guessed?
- Are response expectations specific?
- Is DB impact mentioned when relevant?
- Is missing API information listed?
- Is execution language avoided unless real execution happened?