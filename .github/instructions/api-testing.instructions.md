# API Testing Instructions

## Purpose

Use these instructions when creating, reviewing, or improving API validation plans and API test scenarios.

These instructions apply to REST API testing, authentication, authorization, request validation, response validation, error handling, contract validation, and API-DB consistency planning.

## Core Rules

1. Do not invent endpoint paths.
2. Do not invent HTTP methods.
3. Do not invent request or response fields.
4. Do not invent status codes.
5. If API details are missing, mark them as Needs Confirmation.
6. Always cover authentication for protected endpoints.
7. Always cover authorization for role-based systems.
8. Always include invalid request cases.
9. Always include response validation.
10. Always mention database impact for state-changing APIs.
11. Do not claim API execution unless real execution evidence exists.

## Required API Inputs

Collect or identify:

- Endpoint path
- HTTP method
- Purpose
- Auth requirement
- Authorized roles
- Request fields
- Response schema
- Success status
- Error statuses
- Error response format
- Database impact
- Integration dependencies

If any of these are missing, list them under Missing Information.

## Authentication Coverage

For protected endpoints, include:

- No token
- Invalid token
- Expired token
- Valid token
- Logged out or revoked token if relevant

## Authorization Coverage

For role-based systems, include:

- Correct role can access endpoint
- Wrong role is denied
- Guest user is denied
- Normal user cannot access admin endpoint
- User cannot access another user's data
- Disabled user behavior if relevant

## Request Validation Coverage

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

## Response Validation Coverage

Check:

- Correct status code
- Required fields exist
- Field types are correct
- Sensitive data is not exposed
- Error format is consistent
- Response belongs to correct user
- Pagination metadata is correct when relevant

## State-Changing API Rule

For POST, PUT, PATCH, DELETE actions, identify:

- Before state
- Request action
- Expected response
- Expected database state
- Audit or timestamp impact
- Duplicate or retry risk

## Status Code Rule

Use exact expected status only when provided by specification or requirement.

If not defined, use:

Needs Confirmation

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

## Output Format

Use this structure:

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

## 12. Human Test Leader Notes

## References

Use these repository references when relevant:

- references/patterns/api-testing-patterns.md
- references/examples/api-test-examples.md
- references/anti-patterns/testing-anti-patterns.md
- .github/skills/api-testing/SKILL.md
