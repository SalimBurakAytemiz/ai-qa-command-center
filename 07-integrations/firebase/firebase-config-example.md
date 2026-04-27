# Firebase Configuration Example

## Purpose

Use this file as a safe example for future Firebase validation integration.

Important rule:

Do not commit real Firebase private keys, service account JSON files, project secrets, or production analytics exports.

## Required Environment Variables

| Variable | Purpose | Required |
|---|---|---|
| FIREBASE_PROJECT_ID | Firebase project ID | Yes |
| FIREBASE_CLIENT_EMAIL | Service account email | If service account mode is used |
| FIREBASE_PRIVATE_KEY | Service account private key | If service account mode is used |

## Possible Validation Sources

- Firebase DebugView
- Analytics event logs
- BigQuery export
- Device logs
- Network logs for web analytics

## Human Approval Required For

- Accessing production analytics
- Using real user data
- Exporting analytics data
- Sharing analytics screenshots externally
- Modifying conversion events
- Testing push notifications against real users

## Safety Rules

- Generated Firebase validation plans are not executed analytics results.
- Do not include personal data in analytics events unless approved.
- Do not commit service account JSON files.
- Do not share production analytics data without approval.

## Example Dry-Run Configuration

| Setting | Example Value | Notes |
|---|---|---|
| Mode | dry_run | Recommended default |
| Read Production Analytics | false | Must remain false until approved |
| Validate DebugView | manual_evidence_required | Requires screenshot/log evidence |
| Export Events | false | Enable only after approval |
