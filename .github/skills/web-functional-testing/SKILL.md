# Skill: Web Functional Testing

## Purpose

Use this skill when designing web functional validation scenarios for websites, responsive web interfaces, admin panels, dashboards, forms, tables, CMS-driven pages, and user-facing browser flows.

This skill helps the AI focus on visible product behavior and browser-based user interaction.

## When To Use This Skill

Use this skill when the task includes:

- Web functional testing
- Responsive web testing
- Admin panel testing
- Form validation testing
- UI state validation
- Role-based UI validation
- CMS content visibility testing
- Navigation testing
- Search, filter, sorting, and pagination testing
- Playwright automation planning

## Required Inputs

Before generating web validation scenarios, collect as much of the following as possible:

- Page or screen name
- Feature description
- Acceptance criteria
- User roles
- Supported browsers if available
- Supported viewports if available
- UI requirements
- Figma notes
- Form fields
- Validation rules
- API dependencies
- CMS dependencies
- Expected empty states
- Expected loading states
- Expected error states
- Human test leader instruction

If important UI behavior is missing, list it under "Missing Information".

## Core Rules

### Rule 1: Focus on Visible Behavior

Web functional testing should validate what the user can see and do.

Do not turn the output into API-only or DB-only validation.

### Rule 2: Include UI States

When relevant, include:

- Default state
- Loading state
- Empty state
- Error state
- Success state
- Disabled state
- Focus state
- Validation state

### Rule 3: Include Role-Based UI Behavior

When roles exist, validate:

- What each role can see
- What each role cannot see
- What each role can do
- What each role is blocked from doing

### Rule 4: Include Form Validation

For forms, validate:

- Required fields
- Optional fields
- Invalid format
- Min length
- Max length
- Special characters
- Numeric boundaries
- Date boundaries
- File type
- File size
- Submit button behavior
- Error messages
- Duplicate submission prevention

### Rule 5: Include Responsive Behavior

When responsive web is in scope, validate:

- Desktop layout
- Tablet layout
- Mobile layout
- Header behavior
- Menu behavior
- Overflow
- Horizontal scroll
- Text wrapping
- Button usability
- Modal behavior
- Sticky element behavior

### Rule 6: Use Stable Automation Thinking

When marking automation candidates, prefer scenarios that can use stable locators:

- role
- label
- accessible name
- test id

Avoid flaky selector assumptions.

### Rule 7: Recommend Specialist Agents When Needed

If deeper validation is needed:

- API concern: recommend API Test Agent
- DB concern: recommend Database Validation Agent
- Visual concern: recommend Design or Visual Agent
- Accessibility concern: recommend Accessibility Agent
- Automation concern: recommend Web Automation Agent

### Rule 8: Do Not Claim Execution

A web validation plan is not an executed test result.

Use:

- Web functional scenarios generated
- Web validation plan prepared
- Web coverage reviewed

Do not use:

- Web tests passed
- UI verified
- Browser execution completed

unless real execution evidence exists.

## Scenario Types

Use:

- Navigation
- Form Validation
- UI State
- Data Display
- Role Visibility
- Admin Action
- CMS Content
- Responsive Behavior
- Error Handling
- Empty State
- Loading State
- Pagination
- Sorting
- Filtering
- Search
- Modal
- Toast
- Regression Candidate

## Output Format

Use this format:

# Web Functional Validation Plan

## 1. Scope Summary

## 2. Missing Information

| Missing Item | Why Needed | Impact |
|---|---|---|

## 3. Pages or Screens Covered

| Page or Screen | Platform | User Role | Priority | Notes |
|---|---|---|---|---|

## 4. Web Functional Test Scenarios

| ID | Type | Title | Priority | Platform | User Role | Preconditions | Steps | Expected Result | Dependency | Automation Candidate |
|---|---|---|---|---|---|---|---|---|---|---|

## 5. Role-Based UI Checks

| User Role | Expected Visible Elements | Restricted Elements | Notes |
|---|---|---|---|

## 6. UI State Validation

| State | Expected Behavior | Priority |
|---|---|---|

## 7. Form Validation Checks

| Field | Validation Rule | Expected Behavior | Priority |
|---|---|---|---|

## 8. Responsive Web Notes

| Viewport | Expected Behavior | Risk |
|---|---|---|

## 9. Backend, API, CMS, or DB Dependencies

| Dependency | Why It Matters | Recommended Follow-up |
|---|---|---|

## 10. Automation Candidate Summary

| Scenario ID | Automation Candidate | Reason | Recommended Tool |
|---|---|---|---|

## 11. Specialist Agents Recommended

| Agent | Reason |
|---|---|

## 12. Human Test Leader Notes

## References

When needed, use:

- `references/anti-patterns/testing-anti-patterns.md`
- `references/playwright/playwright-patterns.md`
- `08-skills/ui-testing/README.md`

## Quality Checklist

Before finalizing, check:

- Is visible web behavior covered?
- Are expected results observable?
- Are UI states considered?
- Are role-based checks included?
- Are form validations included?
- Are responsive risks included when relevant?
- Are API and DB details not overmixed?
- Are automation candidates realistic?
- Is missing information listed?
- Is execution language avoided unless real execution happened?