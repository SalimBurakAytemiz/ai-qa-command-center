# Output Standards

## Purpose

This document defines how outputs must be produced, stored, reviewed, and reused inside the AI QA Command Center.

The goal is to keep agent outputs consistent, traceable, readable, and useful for testing, reporting, and future automation.

## Core Rule

Every important output must follow a template.

Agents should not invent a new structure unless explicitly instructed.

## Output Categories

The system produces the following output categories:

1. Product context
2. Test strategy
3. Test plan
4. Test cases
5. Risk analysis
6. API validation
7. DB validation
8. UI validation
9. Jira or Trello drafts
10. Daily reports
11. Review reports
12. Automation candidate summaries

## Output Locations

Use these folders:

| Output Type | Folder |
|---|---|
| Test plans | `05-outputs/test-plans/` |
| General test cases | `05-outputs/test-cases/` |
| Happy path cases | `05-outputs/happy-path/` |
| Edge cases | `05-outputs/edge-cases/` |
| Negative cases | `05-outputs/negative-cases/` |
| Risk analysis | `05-outputs/risk-analysis/` |
| API review | `05-outputs/api-review/` |
| DB review | `05-outputs/db-review/` |
| Mobile review | `05-outputs/mobile-review/` |
| Security review | `05-outputs/security-review/` |
| Performance review | `05-outputs/performance-review/` |
| Jira or Trello drafts | `05-outputs/jira-trello/` |
| Reports | `05-outputs/reports/` |

## File Naming Rules

Use lowercase kebab-case.

Recommended pattern:

YYYY-MM-DD-product-or-feature-output-type.md

Examples:

- 2026-04-27-login-feature-test-plan.md
- 2026-04-27-login-feature-happy-path.md
- 2026-04-27-login-feature-edge-cases.md
- 2026-04-27-login-feature-api-validation.md
- 2026-04-27-daily-quality-report.md

## Status Values

Use these status values:

- Draft
- In Review
- Approved
- Needs Revision
- Rejected

## Priority Values

Use these priority values:

- P0: Release blocker
- P1: Critical
- P2: Important
- P3: Low priority

## Test Case Output Rules

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

## Risk Output Rules

Every risk should include:

- Risk ID
- Risk Area
- Description
- Impact
- Probability
- Priority
- Affected Platform
- Recommended Validation
- Owner Agent

## Report Output Rules

Reports must be:

- Short
- Clear
- Risk-focused
- Management-readable
- Actionable

Reports must not copy all raw test cases unless specifically requested.

## Jira and Trello Output Rules

Jira and Trello outputs must be drafts unless ticket creation is explicitly approved.

Every work item should include:

- Title
- Type
- Priority
- Description
- Suggested owner
- Labels
- Human approval status

## Automation Candidate Output Rules

Automation candidate fields must use:

- Yes
- No
- Later

### Yes

Use for stable, repeatable, deterministic scenarios.

### Later

Use when the scenario is valuable but needs better test data, locators, environment control, or mocks.

### No

Use when the scenario requires human judgment, unstable external dependencies, or destructive validation.

## Missing Information Rules

Every output must include missing information when relevant.

Do not hide uncertainty.

Example:

| Missing Item | Why Needed |
|---|---|
| API response schema | Required to validate contract correctness |

## Human Approval Rules

Human approval must be visible when required.

Human approval is required for:

- Ticket creation
- P0 classification
- Release go or no-go
- Security-sensitive issues
- Production data usage
- Destructive DB checks
- Unclear high-risk assumptions

## Review Rules

Important outputs should be reviewed by the Output Reviewer Agent.

The review should check:

- Completeness
- Correctness
- Clarity
- Actionability
- Duplication
- Risk coverage
- Format compliance
- Scope control

## Traceability Rules

When possible, outputs should reference:

- Product module
- Acceptance criteria
- User role
- Platform
- Related agent
- Related workflow

## Common Output Mistakes to Avoid

- No expected result
- Vague expected result
- Missing priority
- Missing platform
- Missing user role
- Duplicated test cases
- Mixed happy path and negative cases
- Unclear risk impact
- No missing information section
- Reporting generated plans as executed tests
- Creating ticket-looking outputs without human approval

## Output Review Checklist

Before accepting an output, check:

- Does it follow the correct template?
- Is it stored in the correct folder?
- Is the file name clear?
- Are priorities consistent?
- Are expected results observable?
- Are missing items listed?
- Are human approval needs visible?
- Is the output useful for the next workflow step?