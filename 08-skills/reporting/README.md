# Skill: QA Reporting

## Purpose

This skill defines how AI QA agents should create clear, useful, management-readable QA reports.

It should be used by:

- Daily Quality Report Agent
- Weekly Quality Summary Agent
- Monthly Quality and Risk Trend Agent
- Release Readiness Agent
- Jira and Trello Work Tracking Agent
- Output Reviewer Agent

## Reporting Goals

QA reports must help the reader understand:

1. What was tested
2. What was produced
3. What is working
4. What is risky
5. What is blocked
6. What needs human review
7. What needs development action
8. What needs product clarification
9. What should happen next
10. Whether release confidence is increasing or decreasing

## Audience Types

Reports may be written for:

- Human test leader
- QA team
- Developers
- Product manager
- Engineering manager
- CTO or senior management
- Client or stakeholder

The language must change depending on the audience.

## Daily Report Rules

Daily reports should be:

- Short
- Clear
- Actionable
- Risk-focused
- Management-readable

They should include:

- Overall status
- Work completed today
- Test case generation summary
- Areas covered
- Critical risks
- Blockers
- Jira/Trello summary
- Items needing human review
- Recommended next actions

## Status Values

Use:

- Green
- Yellow
- Red

### Green

Use when:

- No critical blocker exists
- No release-impacting risk exists
- Work is progressing normally

### Yellow

Use when:

- Some risks exist
- Some areas are blocked
- Requirements are partially unclear
- Test coverage is incomplete but manageable

### Red

Use when:

- Critical blocker exists
- Environment blocks testing
- Release-impacting risk exists
- Security or data integrity risk exists
- Human decision is urgently required

## Risk Reporting Rules

Each risk should include:

- Risk description
- Priority
- Impact
- Recommended action
- Owner or next responsible team
- Human approval need if relevant

## Blocker Reporting Rules

Separate blockers from bugs.

A blocker prevents work from continuing.

Examples:

- Environment unavailable
- API not deployed
- Test user missing
- Acceptance criteria missing
- DB access unavailable
- Build not installed
- Critical service down

A bug is product behavior that does not match expectation.

## Jira/Trello Reporting Rules

Work tracking outputs should separate:

- Test tasks
- Bug drafts
- Subtasks
- Checklist items
- Release blocker candidates
- Needs human review
- Status comments

Do not create tickets automatically unless explicitly allowed.

## Executive Summary Rules

An executive summary should be:

- Short
- Non-technical when possible
- Focused on risk and decision
- Clear about next action

Bad:

"Several agents generated outputs and some risks were identified."

Good:

"Testing preparation for the login and onboarding scope is partially complete. API and DB validation plans are ready, but final execution is blocked until staging environment access and test users are confirmed."

## Common Mistakes to Avoid

- Copying all raw test cases into the report
- Making the report too long
- Hiding uncertainty
- Mixing blockers and bugs
- Not giving next actions
- Not marking human review items
- Using vague status
- Reporting green when critical coverage is missing
- Reporting red without specific reason

## Review Checklist

Before approving a report, check:

- Is the overall status clear?
- Are critical risks visible?
- Are blockers separated from bugs?
- Are next actions specific?
- Are human review items listed?
- Is the report short enough for management?
- Is uncertainty clearly stated?
- Is release impact visible?