# Workflow: Product Intake

## Purpose

This workflow converts raw product information into compact, structured, test-ready context.

It prevents specialist agents from reading large raw documents unnecessarily.

## Owner

Product Intake Agent

## Supporting Agents

- Test Strategy Agent
- Token Controller Agent
- Output Reviewer Agent

## Input Sources

Possible inputs:

- Product overview
- PRD
- User stories
- Acceptance criteria
- Figma notes
- API documentation
- Backend notes
- Frontend notes
- Mobile notes
- CMS documentation
- Firebase event list
- Release notes
- Human test leader notes

## Main Output

Product Testing Context

## Execution Steps

### Step 1: Collect Product Inputs

Collect available product information from:

- `00-product-context/`
- `01-inputs/prd/`
- `01-inputs/figma/`
- `01-inputs/api-specs/`
- `01-inputs/backend-docs/`
- `01-inputs/frontend-docs/`
- `01-inputs/mobile-docs/`
- `01-inputs/cms-docs/`
- `01-inputs/firebase-events/`
- `01-inputs/release-notes/`

### Step 2: Identify Product Purpose

Extract:

- Product goal
- Business goal
- Target users
- Main value proposition

### Step 3: Identify Product Surfaces

Extract affected surfaces:

- Web site
- Responsive web
- Admin panel
- CMS
- iOS app
- Android app
- Backend API
- Socket / realtime
- Database
- Firebase analytics
- Notification system

### Step 4: Identify User Roles

Extract:

- Guest user
- Registered user
- Admin user
- Super admin
- Content manager
- Operation user
- Any custom project-specific role

### Step 5: Identify Product Modules

Extract modules such as:

- Authentication
- Onboarding
- Profile
- CMS content
- Notification
- Admin operations
- API layer
- Database layer
- Socket layer
- Firebase event layer

### Step 6: Identify Critical User Journeys

Extract journeys such as:

- Register
- Login
- Password reset
- Profile update
- Content viewing
- Notification open
- Admin action
- CMS publish
- Realtime update

### Step 7: Identify Technical Impact

Extract:

- API impact
- DB impact
- Socket impact
- CMS impact
- Notification impact
- Firebase event impact
- Security impact
- Performance impact

### Step 8: Identify Missing Information

List missing information required for testing:

- Missing acceptance criteria
- Missing API spec
- Missing DB schema
- Missing Figma screen
- Missing role matrix
- Missing Firebase event list
- Missing test environment info

### Step 9: Create Compact Product Testing Context

Generate compact output using the Product Intake Agent prompt.

### Step 10: Review Product Context

Use Output Reviewer Agent to check:

- Completeness
- Clarity
- Missing information
- Test usefulness
- Risk visibility

## Output Location

Store the final output under:

`05-outputs/reports/product-testing-context.md`

## Quality Gate

The workflow can continue only if:

- Product purpose is clear
- At least one platform is identified
- At least one user role is identified
- Critical flows are identified
- Missing information is clearly listed
- High-risk areas are visible

## Stop Conditions

Stop and request human clarification when:

- Product purpose is unknown
- Platform scope is unknown
- No acceptance criteria exist
- User roles are unclear
- Technical scope is completely missing