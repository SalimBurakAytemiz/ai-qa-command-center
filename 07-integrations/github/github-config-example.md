# GitHub Integration Configuration Example

## Purpose

Use this file as a safe example for future GitHub Issues or repository integration configuration.

Important rule:

Do not commit real GitHub tokens or private repository secrets.

## Required Environment Variables

| Variable | Purpose | Required |
|---|---|---|
| GITHUB_TOKEN | GitHub token | Yes for API actions |
| GITHUB_OWNER | Repository owner or organization | Yes |
| GITHUB_REPO | Repository name | Yes |

## Required Permissions

- Read repository contents
- Create issues if issue creation is enabled
- Read workflow status if CI status is needed
- Create comments if report comments are enabled

## Human Approval Required For

- Creating GitHub issues
- Creating issue comments
- Labeling P0/P1 risks
- Posting security-sensitive details
- Referencing private customer data

## Safety Rules

- Generated GitHub issue drafts are not created issues.
- Human approval is required before external issue creation.
- Do not post secrets, tokens, logs with credentials, or private customer data.
- Do not report tests as passed unless execution evidence exists.

## Example Dry-Run Configuration

| Setting | Example Value | Notes |
|---|---|---|
| Mode | dry_run | Recommended default |
| Create Issues | false | Must remain false until approved |
| Read Actions Status | true | Safe read-only usage |
| Default Labels | qa, generated-draft | Avoid misleading labels |
