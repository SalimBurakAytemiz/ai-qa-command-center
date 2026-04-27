# Jira Configuration Example

## Purpose

Use this file as a safe example for future Jira integration configuration.

Important rule:

Do not commit real Jira tokens, emails, project keys, or private URLs.

## Required Environment Variables

| Variable | Purpose | Required |
|---|---|---|
| JIRA_BASE_URL | Jira workspace base URL | Yes |
| JIRA_EMAIL | Jira account email | Yes |
| JIRA_API_TOKEN | Jira API token | Yes |
| JIRA_PROJECT_KEY | Target Jira project key | Yes |

## Required Permissions

- Browse projects
- Create issues
- Edit issues if updates are needed
- Add comments if report updates are needed

## Human Approval Required For

- Creating Jira tickets
- Creating bug reports
- Assigning P0 or P1 priority
- Posting security-sensitive findings
- Posting release-impacting findings
- Attaching sensitive evidence

## Safety Rules

- Generated Jira drafts are not created Jira tickets.
- Human approval is required before external ticket creation.
- Do not include secrets or customer personal data in tickets.
- Do not create bugs without execution evidence.
- Do not mark release readiness in Jira without human approval.

## Example Dry-Run Configuration

| Setting | Example Value | Notes |
|---|---|---|
| Mode | dry_run | Recommended default |
| Create Tickets | false | Must remain false until approved |
| Attach Evidence | false | Enable only after review |
| Default Priority | P2 | Avoid defaulting everything to P0/P1 |
