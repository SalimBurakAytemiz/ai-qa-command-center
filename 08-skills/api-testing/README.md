# Skill: API Testing

## Purpose

This skill defines how AI QA agents should analyze and design API validation scenarios.

It should be used by:

- API Test Agent
- Backend Integration Test Agent
- Database Validation and Data Integrity Agent
- Role, Permission and Session Security Agent
- Output Reviewer Agent

## API Testing Goals

API testing must validate:

1. Correct endpoint behavior
2. Request validation
3. Response schema
4. Status codes
5. Authentication
6. Authorization
7. Role-based access
8. Error handling
9. Pagination
10. Sorting
11. Filtering
12. Rate or abuse risks
13. Contract consistency
14. Database state impact
15. Integration dependency risks

## Required API Test Fields

Each API scenario should include:

- ID
- Endpoint
- HTTP Method
- Scenario Type
- Priority
- User Role
- Preconditions
- Request Data
- Expected Status Code
- Expected Response
- Notes

## Common HTTP Methods

Use:

- GET
- POST
- PUT
- PATCH
- DELETE

## Status Code Expectations

Use status codes carefully.

Common examples:

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

Do not guess status codes when the API specification is missing. Mark them as "Needs Confirmation".

## Scenario Types

Use these types:

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

## Authentication Checks

Validate:

- Request without token
- Request with invalid token
- Request with expired token
- Request with valid token
- Logout and token invalidation
- Token refresh behavior

## Authorization Checks

Validate:

- Correct role can access endpoint
- Wrong role cannot access endpoint
- User cannot access another user's data
- Admin-only endpoint rejects normal users
- Super admin-only action rejects lower roles

## Request Validation Checks

Validate:

- Missing required fields
- Null values
- Empty strings
- Invalid data type
- Invalid enum value
- Invalid date format
- Invalid ID format
- Very long strings
- Boundary values
- Duplicate payload
- Unexpected extra fields

## Response Validation Checks

Validate:

- Correct status code
- Correct response schema
- Correct field types
- Required fields exist
- Sensitive data is not exposed
- Error response format is consistent
- Response data belongs to correct user
- Pagination metadata is correct

## Pagination, Sorting and Filtering

When relevant, validate:

- First page
- Last page
- Empty page
- Invalid page number
- Page size limit
- Sorting ascending
- Sorting descending
- Invalid sort field
- Valid filter
- Invalid filter
- Combined filters

## API and Database Consistency

For state-changing APIs, check:

- Was the correct record created?
- Was the correct record updated?
- Was the correct record deleted or soft deleted?
- Was audit data written?
- Was timestamp updated?
- Was duplicate data prevented?
- Was related data preserved?
- Was API response consistent with DB state?

## Integration Risks

Consider:

- Service dependency unavailable
- Timeout
- Retry behavior
- Partial failure
- Duplicate processing
- External provider error
- Queue delay
- Event not emitted

## Common Mistakes to Avoid

- Testing only valid requests
- Ignoring authorization
- Ignoring expired tokens
- Ignoring error response body
- Ignoring DB impact
- Ignoring pagination edge cases
- Assuming status codes without API spec
- Mixing UI test cases into API output
- Creating duplicate validation cases

## Review Checklist

Before approving API validation output, check:

- Are endpoints clearly listed?
- Are methods correct?
- Are auth and authorization covered?
- Are request validation cases included?
- Are expected status codes defined?
- Are response expectations specific?
- Are DB impacts listed when relevant?
- Are missing API details clearly marked?