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
