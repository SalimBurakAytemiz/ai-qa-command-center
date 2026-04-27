# Trello Configuration Example

## Purpose

Use this file as a safe example for future Trello integration configuration.

Important rule:

Do not commit real Trello API keys, tokens, board IDs, or private workspace data.

## Required Environment Variables

| Variable | Purpose | Required |
|---|---|---|
| TRELLO_API_KEY | Trello API key | Yes |
| TRELLO_TOKEN | Trello token | Yes |
| TRELLO_BOARD_ID | Target board ID | Yes |

## Recommended Lists

- QA To Do
- In Review
- Blocked
- Approved
- Done

## Recommended Labels

- QA
- Bug
- Risk
- API
- DB
- Web
- Mobile
- Security
- Performance

## Human Approval Required For

- Creating Trello cards
- Moving cards to Done
- Adding P0/P1 labels
- Posting security-sensitive findings
- Attaching evidence

## Safety Rules

- Generated Trello drafts are not created Trello cards.
- Human approval is required before external card creation.
- Do not attach secrets or production data.
- Do not mark QA work as done unless review or execution evidence exists.

## Example Dry-Run Configuration

| Setting | Example Value | Notes |
|---|---|---|
| Mode | dry_run | Recommended default |
| Create Cards | false | Must remain false until approved |
| Default List | QA To Do | Safe starting point |
| Default Label | QA | Avoid over-labeling |
