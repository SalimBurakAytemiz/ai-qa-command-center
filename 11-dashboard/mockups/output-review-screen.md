# Output Review Screen Mockup

## Purpose

This mockup defines the future output review screen.

## Main Goal

The screen should show:

- Output file
- Source agent
- Output type
- Quality score
- Review decision
- Missing information
- Unsupported assumptions
- Human approval needs
- Required revisions
- Generated vs executed warning

## Example Review

| Field | Value |
|---|---|
| Selected Output | test-strategy.md |
| Source Agent | Test Strategy Agent |
| Output Type | Test Strategy |
| Review Decision | Approved with Minor Notes |
| Overall Score | 8.4 / 10 |
| Human Approval Required | Yes |

## Quality Score Dimensions

| Dimension | Score |
|---|---|
| Completeness | 8/10 |
| Clarity | 9/10 |
| Risk Coverage | 8/10 |
| Actionability | 8/10 |
| Duplicate Control | 9/10 |
| Format Compliance | 9/10 |
| Traceability | 7/10 |
| Safety / Approval Awareness | 9/10 |

## Issues Found

- API status codes need confirmation
- DB schema not confirmed
- Dashboard route not confirmed

## Human Approval Required

- P0 access-control risk
- External Jira/Trello ticket creation
- Final release readiness

## Review Decision Values

| Decision | Meaning |
|---|---|
| Approved | Output can be used |
| Approved with Minor Notes | Output usable with small notes |
| Needs Minor Revision | Small correction needed |
| Needs Revision | Output must be revised |
| Rejected | Output should not be used |
| Human Approval Required | Human decision required before use |

## Important Warning

Generated outputs are not executed test results.
