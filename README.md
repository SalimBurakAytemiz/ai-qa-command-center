# AI QA Command Center

AI QA Command Center is a structured AI-assisted QA operating system designed to help one human test leader coordinate multiple AI QA agents across product analysis, test planning, test case design, API validation, database validation, web validation, work tracking, reporting, and future automation.

This repository is not just a prompt collection.

It is a product-centered QA framework built around:

- 1 human test leader
- 8 AI QA teams
- 44 AI agent profiles
- Management agents
- Specialist QA agents
- Output review agents
- Token and context control
- Multi-provider AI routing
- Standardized outputs
- Repeatable workflows
- Reference examples and testing patterns

---

## Core Concept

The system is designed around the idea that one human QA leader can control an AI-supported QA organization.

The human test leader remains responsible for:

- Final review
- Human approval
- Release decisions
- Security-sensitive decisions
- Production data decisions
- Jira/Trello ticket creation approval
- Risk acceptance

AI agents assist with structured QA work such as:

- Product understanding
- Test strategy
- Agent routing
- Test planning
- Test case generation
- Happy path design
- Edge case design
- Negative case design
- Web functional validation
- API validation
- Database validation
- Risk analysis
- Jira/Trello draft creation
- Daily quality reporting
- Output review

---

## What This Repository Contains

This repository contains:

- Agent registry files
- Prompt files
- Workflow documents
- Output templates
- QA skill libraries
- AI tool-compatible agent files
- AI tool instruction files
- AI-compatible skill files
- Reference examples
- Testing anti-patterns
- API, DB, and Playwright testing patterns
- Setup and validation scripts
- Repository roadmap
- Changelog
- Environment example configuration

---

## Repository Structure

```text
ai-qa-command-center/
│
├── .github/
│   ├── agents/
│   ├── instructions/
│   └── skills/
│
├── 00-product-context/
│
├── 01-inputs/
│   ├── prd/
│   ├── figma/
│   ├── api-specs/
│   ├── backend-docs/
│   ├── frontend-docs/
│   ├── mobile-docs/
│   ├── cms-docs/
│   ├── firebase-events/
│   └── release-notes/
│
├── 02-agent-registry/
│
├── 03-prompts/
│
├── 04-workflows/
│
├── 05-outputs/
│
├── 06-tests/
│
├── 07-integrations/
│
├── 08-skills/
│
├── 09-docs/
│
├── 10-scripts/
│
├── 11-dashboard/
│
├── demo/
│
├── examples/
│
├── references/
│
├── templates/
│
├── .env.example
├── .gitignore
├── CHANGELOG.md
├── LICENSE
├── README.md
└── ROADMAP.md
---

## Latest Repository Capabilities

The repository now includes the following completed capability layers:

### Templates Layer

Reusable input templates are available under templates/.

Current templates include:

- Product intake form
- Feature intake form
- Acceptance criteria template
- API notes template
- DB notes template
- Release scope template

### Demo Feature Pack

A complete login feature demo is available under demo/login-feature/.

The demo includes input files and generated planning outputs for a login feature.

Demo input files include:

- Feature brief
- Acceptance criteria
- API notes
- DB notes
- UI notes

Demo output files include:

- Product testing context
- Test strategy
- Agent routing plan
- Test plan
- Happy path test cases
- Edge and negative test cases
- API validation plan
- DB validation plan
- Jira/Trello drafts
- Daily quality report
- Executive summary

Important: demo outputs are generated planning artifacts only. They are not executed test results.

### Example Output Library

Reusable sample outputs are available under examples/outputs/.

Current sample outputs include:

- Sample test plan
- Sample happy path test cases
- Sample edge and negative test cases
- Sample API validation plan
- Sample DB validation plan
- Sample Jira drafts
- Sample daily quality report
- Sample executive summary

### Expanded AI Instructions

Specialized AI tool instructions are available under .github/instructions/.

Current instruction files include:

- General QA instructions
- Test case design instructions
- API testing instructions
- DB validation instructions
- Playwright instructions
- QA reporting instructions

### Expanded Reference Examples

Reference examples are available under references/examples/.

Current reference examples include:

- Test case examples
- API test examples
- DB validation examples
- Bug report examples
- Jira ticket examples
- Daily report examples

### Validation and CI

The repository includes validation scripts under 10-scripts/validation/.

Current validation scripts include:

- Agent registry validation
- Agent prompt coverage validation
- Required files validation

The repository also includes GitHub Actions validation under .github/workflows/validate-repo.yml.

The workflow runs on push and pull request to main.

Current validation status:

- Agent registry validation passes.
- Agent prompt coverage validation passes.
- GitHub Actions repository validation passes on main.

### Current Framework Maturity

The repository is now more than a prompt collection.

It currently includes:

- AI QA organization structure
- Agent registry
- Prompt library
- Workflow layer
- Output templates
- Skill library
- AI tool compatibility layer
- Multi-provider model routing
- Token and context policy
- Output review rules
- Input templates
- Complete demo feature pack
- Sample output library
- Reference examples
- Validation scripts
- GitHub Actions CI

The next major development areas are:

- More reference patterns
- Security testing checklist
- Performance testing patterns
- Mobile testing patterns
- Firebase validation patterns
- Integration templates
- Automation generation patterns
- Dashboard mockups

---

## Advanced QA Operations Capabilities

The repository now includes advanced QA operation references and templates added in the v0.7.0 layer.

### Risk and Release Readiness References

Risk and release readiness references are available under references/patterns/.

Current files include:

- references/patterns/risk-analysis-patterns.md
- references/patterns/release-readiness-patterns.md

These references help AI agents create better risk matrices, release readiness drafts, P0/P1 decisions, mitigation actions, and human approval points.

### Security Testing Reference

Security testing guidance is available under references/security-testing/.

Current file:

- references/security-testing/security-checklist.md

This reference improves coverage for authentication, authorization, direct URL access, API security, session/token handling, sensitive data exposure, account enumeration, and human approval gates.

### Performance Testing Reference

Performance testing guidance is available under references/performance-testing/.

Current file:

- references/performance-testing/performance-test-patterns.md

This reference improves planning for load testing, stress testing, spike testing, soak testing, frontend performance, API response time risks, DB performance risks, and tool candidates such as JMeter and k6.

### Mobile Testing Reference

Mobile testing guidance is available under references/mobile-testing/.

Current file:

- references/mobile-testing/mobile-testing-patterns.md

This reference improves planning for iOS, Android, mobile web, device matrix, OS version coverage, app lifecycle, poor network behavior, permissions, deep links, push notifications, crash risks, and Appium candidates.

### Firebase Event Validation Reference

Firebase and analytics validation guidance is available under references/firebase/.

Current file:

- references/firebase/firebase-event-validation-patterns.md

This reference improves planning for analytics events, event parameters, screen_view checks, conversion events, duplicate event risks, missing event risks, user properties, notification tracking, and deep link tracking.

### Automation Generation Reference

Automation candidate selection guidance is available under references/automation/.

Current file:

- references/automation/automation-generation-patterns.md

This reference helps decide whether a test should be automated now, automated later, or not automated. It also supports Playwright, Appium, API, DB, and performance automation planning.

### Integration Draft Templates

Integration draft templates are available under 07-integrations/.

Current integration template areas:

- Jira
- Trello
- GitHub Issues
- Slack
- Firebase
- Figma

These templates are draft-only. AI agents must not create external tickets, cards, issues, Slack messages, or integration actions without explicit human approval.

### Expanded Validation Coverage

The validation script now checks the expanded reference library, integration templates, and automation reference.

Validation script:

- 10-scripts/validation/check-agent-prompt-coverage.py

GitHub Actions workflow:

- .github/workflows/validate-repo.yml

Current validation expectations:

- Agent registry validation passes.
- Agent prompt coverage validation passes.
- Expanded reference validation passes.
- Integration template validation passes.
- Automation reference validation passes.
- GitHub Actions repository validation passes on main.

### Current v0.7.0 Capability Summary

The AI QA Command Center now supports:

- Structured AI QA team architecture
- Multi-provider AI model routing
- Token and context policy
- Output review and quality scoring
- Product and feature intake templates
- Complete login feature demo
- Sample output library
- AI tool instructions
- Reference examples
- Risk analysis patterns
- Release readiness patterns
- Security testing checklist
- Performance testing patterns
- Mobile testing patterns
- Firebase analytics validation patterns
- Integration draft templates
- Automation candidate selection patterns
- Validation scripts
- GitHub Actions CI

Important rule:

Generated outputs, plans, test cases, reports, automation candidates, and integration drafts are planning artifacts only unless real execution evidence exists.

---

## Dashboard Mockup Layer

The repository now includes dashboard mockup documentation added in the v0.8.0 layer.

Current dashboard mockups are available under 11-dashboard/mockups/.

Dashboard mockup files include:

- 11-dashboard/mockups/operator-dashboard.md
- 11-dashboard/mockups/feature-intake-screen.md
- 11-dashboard/mockups/agent-routing-screen.md
- 11-dashboard/mockups/output-review-screen.md
- 11-dashboard/mockups/quality-report-screen.md

These mockups define the future operator-facing dashboard concept for the AI QA Command Center.

## Dashboard Purpose

The future dashboard should help the human test leader review:

- Active product or feature
- Workflow status
- Selected and skipped agents
- Generated output package
- Output review score
- Open risks
- Blockers
- Human approval queue
- Validation status
- Recommended next actions

## Dashboard Safety Rule

The dashboard mockups are documentation only.

They are not a working dashboard application yet.

Generated outputs shown in dashboard concepts must not be treated as executed test results.

Safe dashboard labels include:

- Generated
- Reviewed
- Needs Revision
- Blocked
- Human Approval Required

Unsafe labels must not be used unless execution evidence exists:

- Passed
- Verified
- Tested successfully
- Release ready

## Current v0.8.0 Capability Summary

The AI QA Command Center now includes:

- Structured AI QA team architecture
- Agent registry
- Prompt library
- Workflow layer
- Output templates
- Skill library
- AI tool compatibility layer
- Multi-provider model routing
- Token and context policy
- Output review rules
- Input templates
- Complete demo feature pack
- Sample output library
- Reference examples
- Security testing checklist
- Performance testing patterns
- Mobile testing patterns
- Firebase analytics validation patterns
- Integration draft templates
- Automation candidate selection patterns
- Dashboard mockup documentation
- Validation scripts
- GitHub Actions CI

Next major development areas:

- Automation generation templates
- Integration configuration examples
- Test execution workflow examples
- Phase 2 and Phase 3 agent prompts
- Additional demo feature packs
- Output review examples
- Release readiness demo output
- Future dashboard implementation

---

## Automation Generation Template Layer

The repository now includes automation generation templates added in the v0.9.0 layer.

Current automation templates are available under templates/automation/.

Automation template files include:

- templates/automation/playwright-test-template.md
- templates/automation/api-test-template.md
- templates/automation/db-validation-script-template.md
- templates/automation/appium-test-template.md
- templates/automation/performance-test-template.md

These templates define how future AI agents should prepare automation drafts.

## Automation Template Purpose

The automation templates support future draft generation for:

- Web automation with Playwright
- API automation
- Database validation automation
- Mobile automation with Appium
- Performance automation with k6, JMeter, Gatling, Lighthouse, or similar tools

## Automation Safety Rule

Generated automation drafts are not executed test results.

They must not be reported as passed, verified, executed, stable, scalable, or release-ready unless real execution evidence exists.

Safe wording:

- Automation candidate identified
- Automation template prepared
- Automation draft generated
- Execution evidence required
- Human approval required

Unsafe wording without evidence:

- Automation passed
- Test executed successfully
- Regression passed
- Performance verified
- Mobile verified
- Release ready

## Current v0.9.0 Capability Summary

The AI QA Command Center now includes:

- Structured AI QA team architecture
- Agent registry
- Prompt library
- Workflow layer
- Output templates
- Skill library
- AI tool compatibility layer
- Multi-provider model routing
- Token and context policy
- Output review rules
- Input templates
- Complete login feature demo
- Sample output library
- Reference examples
- Risk analysis patterns
- Release readiness patterns
- Security testing checklist
- Performance testing patterns
- Mobile testing patterns
- Firebase analytics validation patterns
- Integration draft templates
- Automation candidate selection patterns
- Automation generation templates
- Dashboard mockup documentation
- Validation scripts
- GitHub Actions CI

## Next Major Development Areas

- Integration configuration examples
- Sample GitHub Actions workflows for future test execution
- Output review examples
- Release readiness demo output
- More demo feature packs beyond login
- Phase 2 and Phase 3 agent prompts
- Dashboard operator workflow documentation
- Future executable automation generation scripts
- Future dashboard implementation

---

## Integration Configuration Example Layer

The repository now includes integration configuration examples added in the v0.10.0 layer.

Current integration configuration examples are available under 07-integrations/.

Configuration example files include:

- 07-integrations/jira/jira-config-example.md
- 07-integrations/trello/trello-config-example.md
- 07-integrations/github/github-config-example.md
- 07-integrations/slack/slack-config-example.md
- 07-integrations/firebase/firebase-config-example.md
- 07-integrations/figma/figma-config-example.md

These files define safe future configuration expectations for external integrations.

## Integration Configuration Purpose

The integration configuration examples document:

- Required environment variables
- Required permissions
- Dry-run defaults
- Human approval gates
- Safety rules
- Secret handling rules
- External action restrictions

## Supported Future Integration Areas

The repository now has draft templates and configuration examples for:

- Jira
- Trello
- GitHub Issues
- Slack
- Firebase
- Figma

## Integration Safety Rule

These files do not implement live integrations.

They are configuration planning examples only.

No real secrets, tokens, private URLs, service account files, customer data, or production credentials should be committed.

AI agents must not create external tickets, cards, issues, Slack messages, analytics changes, Figma comments, or integration actions without explicit human approval.

Recommended default mode for future integrations:

- dry_run

External action defaults should remain disabled until approved.

## Current v0.10.0 Capability Summary

The AI QA Command Center now includes:

- Structured AI QA team architecture
- Agent registry
- Prompt library
- Workflow layer
- Output templates
- Skill library
- AI tool compatibility layer
- Multi-provider model routing
- Token and context policy
- Output review rules
- Permissions policy
- Input templates
- Complete login feature demo
- Sample output library
- Reference examples
- Risk analysis patterns
- Release readiness patterns
- Security testing checklist
- Performance testing patterns
- Mobile testing patterns
- Firebase analytics validation patterns
- Integration draft templates
- Integration configuration examples
- Automation candidate selection patterns
- Automation generation templates
- Dashboard mockup documentation
- Validation scripts
- GitHub Actions CI

## Next Major Development Areas

- Sample GitHub Actions workflows for future test execution
- Output review examples
- Release readiness demo output
- More demo feature packs beyond login
- Phase 2 and Phase 3 agent prompts
- Dashboard operator workflow documentation
- Future executable automation generation scripts
- Future live integrations
- Future dashboard implementation
