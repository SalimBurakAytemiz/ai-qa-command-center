# Figma Configuration Example

## Purpose

Use this file as a safe example for future Figma review integration.

Important rule:

Do not commit real Figma tokens, private file keys, or customer design links.

## Required Environment Variables

| Variable | Purpose | Required |
|---|---|---|
| FIGMA_TOKEN | Figma API token | Yes for API access |
| FIGMA_FILE_KEY | Target Figma file key | If file-level access is used |

## Possible Review Sources

- Figma screen links
- Figma design tokens
- Exported screenshots
- Design notes
- Component names
- UX copy

## Human Approval Required For

- Accessing private customer designs
- Sharing design screenshots externally
- Reporting design-impacting issues
- Posting Figma comments
- Making release-impacting UI decisions

## Safety Rules

- Generated Figma review drafts are not completed UI validation results.
- Human review is required for design-impacting decisions.
- Do not publish private design links without approval.
- Do not claim design match unless implementation comparison evidence exists.

## Example Dry-Run Configuration

| Setting | Example Value | Notes |
|---|---|---|
| Mode | dry_run | Recommended default |
| Read Figma File | false | Enable only after approval |
| Export Screens | false | Enable only after approval |
| Post Comments | false | Must remain false until approved |
