# Slack Configuration Example

## Purpose

Use this file as a safe example for future Slack QA reporting integration.

Important rule:

Do not commit real Slack webhooks, bot tokens, channel IDs, or private workspace information.

## Required Environment Variables

| Variable | Purpose | Required |
|---|---|---|
| SLACK_WEBHOOK_URL | Incoming webhook URL | If webhook mode is used |
| SLACK_BOT_TOKEN | Bot token | If bot API mode is used |
| SLACK_CHANNEL_ID | Target channel ID | Yes for bot API mode |

## Recommended Message Types

- Daily QA summary
- Blocker update
- Risk summary
- Human approval request
- Release readiness draft summary

## Human Approval Required For

- Sending Slack messages
- Posting P0/P1 risks
- Posting security-sensitive findings
- Mentioning release readiness
- Sharing screenshots, logs, or evidence

## Safety Rules

- Generated Slack messages are drafts.
- Human approval is required before sending.
- Do not post secrets, customer data, or production credentials.
- Do not say tests passed unless execution evidence exists.
- Do not say release ready unless approved.

## Example Dry-Run Configuration

| Setting | Example Value | Notes |
|---|---|---|
| Mode | dry_run | Recommended default |
| Send Messages | false | Must remain false until approved |
| Default Status | Yellow | Safe when information is incomplete |
| Include Evidence | false | Enable only after review |
