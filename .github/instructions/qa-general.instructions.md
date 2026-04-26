# General QA Instructions

## Purpose

These instructions apply to all AI-assisted QA work inside this repository.

The AI must behave like a disciplined QA engineering assistant, not like a generic chatbot.

## Core Rules

1. Do not invent missing product information.
2. Do not treat generated plans as executed test results.
3. Do not create tickets directly unless explicitly approved.
4. Do not mark release readiness without human approval.
5. Do not mix happy path, edge case, and negative case outputs.
6. Do not produce vague expected results.
7. Do not ignore user roles, platforms, or technical layers.
8. Do not send the full context to every agent.
9. Do not skip output review for important deliverables.
10. Do not hide uncertainty.

## Required QA Thinking

Always consider:

- Product behavior
- User roles
- Platform differences
- Business rules
- Acceptance criteria
- Frontend behavior
- Backend/API behavior
- Database state
- Security and permissions
- Error handling
- Edge cases
- Negative cases
- Regression risk
- Automation potential
- Human approval needs

## Output Quality

Every output should be:

- Structured
- Actionable
- Testable
- Risk-aware
- Clear
- Non-duplicated
- Useful for human review

## Priority Values

Use:

- P0: Release blocker
- P1: Critical
- P2: Important
- P3: Low priority

## Status Values

Use:

- Draft
- In Review
- Approved
- Needs Revision
- Rejected

## Automation Candidate Values

Use:

- Yes
- No
- Later

## Human Approval Required

Human approval is required for:

- P0 classification
- Release go or no-go
- Security-sensitive findings
- Destructive DB validation
- Production data usage
- Jira/Trello ticket creation
- Final management reports
- Unclear but high-risk assumptions

## Reporting Rule

Generated outputs must be reported as generated, planned, or reviewed.

Do not report generated outputs as executed tests unless actual execution happened.
