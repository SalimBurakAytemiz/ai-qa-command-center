# Skill: Test Case Design

## Purpose

This skill defines how AI QA agents should design high-quality test cases.

It should be used by:

- Test Planning Agent
- Happy Path Test Case Agent
- Edge Case and Negative Case Agent
- Feature Validation Agent
- Product Flow Test Agent
- Output Reviewer Agent

## Core Principles

A good test case must be:

1. Clear
2. Executable
3. Observable
4. Specific
5. Risk-aware
6. Non-duplicated
7. Linked to a requirement or product behavior
8. Useful for manual testing or future automation

## Required Test Case Fields

Every test case should include:

- ID
- Title
- Type
- Priority
- Platform
- User Role
- Preconditions
- Test Data
- Steps
- Expected Result
- Risk Area
- Automation Candidate
- Notes

## Test Case Types

Use these types consistently:

- Happy Path
- Edge Case
- Negative Case
- Boundary Case
- Permission Case
- Session Case
- State Transition Case
- API Validation
- DB Validation
- UI Functional
- Mobile Functional
- Notification
- Firebase Event
- Visual
- Accessibility
- Security
- Performance
- Regression

## Priority Rules

Use:

- P0: Release blocker
- P1: Critical
- P2: Important
- P3: Low priority

### P0

Use P0 when failure blocks release or creates severe business, security, data, or user-impacting risk.

Examples:

- Login completely broken
- Payment or critical transaction broken
- Admin can access restricted data
- Data corruption
- App crash on launch
- API unavailable for critical flow

### P1

Use P1 when the issue is critical but does not fully block release if a workaround exists.

Examples:

- Main feature partially broken
- Important API validation missing
- Critical mobile flow fails on one major device
- Notification not delivered for important flow

### P2

Use P2 for important but non-blocking issues.

Examples:

- Secondary flow issue
- Minor role-specific behavior issue
- Non-critical visual inconsistency
- Medium-risk edge case

### P3

Use P3 for low-risk issues.

Examples:

- Text alignment issue
- Minor copy issue
- Low-impact optional flow issue

## Happy Path Rules

Happy path test cases must verify expected successful behavior.

They should include:

- Valid user
- Valid data
- Valid permissions
- Healthy environment
- Expected successful result

Do not include:

- Invalid input
- Unauthorized access
- Expired session
- Error handling
- Boundary stress

## Edge Case Rules

Edge cases must cover unusual but possible situations.

Examples:

- Maximum character count
- Minimum value
- Optional field empty
- Very long text
- Slow network
- Rapid repeated click
- Switching app to background
- Reopening after session expiration
- Cross-platform state continuation

## Negative Case Rules

Negative cases must cover invalid, unauthorized, incomplete, or rejected behavior.

Examples:

- Invalid email
- Empty required field
- Wrong password
- Expired token
- Forbidden admin action
- Invalid API payload
- Invalid state transition
- Duplicate submission
- Accessing another user's data

## Expected Result Rules

Expected results must be:

- Specific
- Observable
- Testable
- Not vague

Bad example:

"The system works correctly."

Good example:

"The user is redirected to the dashboard and the dashboard displays the logged-in user's name."

## Automation Candidate Rules

Use:

- Yes
- No
- Later

### Yes

Use when:

- Scenario is stable
- Scenario is repeatable
- Expected result is deterministic
- Test data can be controlled
- It is valuable for regression

### Later

Use when:

- Test is valuable but needs stable locator
- Test needs better test data
- Test needs environment setup
- Test needs mock service or API support

### No

Use when:

- Scenario requires human judgment
- Scenario is unstable
- Scenario depends on external systems
- Scenario is destructive or risky

## Common Mistakes to Avoid

- Mixing happy path with negative cases
- Writing vague expected results
- Creating duplicate test cases
- Ignoring user roles
- Ignoring platform differences
- Writing too many low-value cases
- Missing preconditions
- Missing test data
- Marking everything as automation candidate
- Ignoring risk priority

## Review Checklist

Before approving test cases, check:

- Are they executable?
- Are expected results clear?
- Are user roles included?
- Are platforms included?
- Are priorities reasonable?
- Are duplicates removed?
- Are edge and negative cases separated?
- Are missing requirements listed?
- Are automation candidates realistic?