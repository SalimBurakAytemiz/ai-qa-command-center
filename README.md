# AI QA Command Center

AI QA Command Center is a product-centered, AI-assisted quality engineering system designed to support one human test leader with eight specialized AI agent teams and forty-four AI agent profiles.

The system is designed to analyze a product, understand its frontend, backend, mobile, database, API, socket, CMS, notification, analytics, security, performance, and design layers, then generate structured test outputs such as test plans, happy path cases, edge cases, negative cases, risk analysis, automation candidates, Jira/Trello task drafts, and quality reports.

## Core Concept

This repository does not represent forty-four separate running bots.

It represents:

- One human AI-supported test leader
- Eight AI agent teams
- Forty-four AI agent profiles
- A product-centered workflow
- Token-controlled task routing
- Standardized prompt files
- Standardized output templates
- Future-ready test execution structure

## Main Goal

The main goal is to turn product knowledge into structured quality outputs.

The system should be able to:

1. Read and summarize product context
2. Understand product modules and user roles
3. Identify frontend, backend, mobile, database, API, socket, CMS, notification, Firebase, security, performance, and design risks
4. Generate happy path, edge case, and negative test cases
5. Route tasks to the correct AI agent profiles
6. Reduce token usage through context filtering
7. Review generated outputs
8. Produce reports and Jira/Trello-ready task drafts
9. Support future automation with Playwright, Appium, API tests, DB checks, and JMeter

## Human Role

The human test leader is responsible for:

- Giving product context
- Reviewing AI outputs
- Approving critical decisions
- Validating high-risk findings
- Deciding release quality status
- Managing the AI agent workflow

The AI agents assist the human test leader. They do not replace final human judgment.

## High-Level Workflow

Product Information
→ Product Intake Agent
→ Test Strategy Agent
→ Task Router Agent
→ Token Controller Agent
→ Specialist AI Agent Teams
→ Output Reviewer Agent
→ Reports, Test Cases, Jira/Trello Tasks, Automation Candidates

## Repository Structure

- `00-product-context`: Product knowledge, business context, user roles, modules, platforms, and assumptions
- `01-inputs`: PRD files, Figma notes, API specs, backend docs, frontend docs, mobile docs, CMS docs, Firebase events, and release notes
- `02-agent-registry`: Agent definitions, team definitions, model routing, token policy, permissions, and workflow routing
- `03-prompts`: Global prompts, management prompts, team prompts, reviewer prompts, and prompt templates
- `04-workflows`: Master workflows and team-specific workflow definitions
- `05-outputs`: Generated test plans, test cases, reviews, risk analysis, and reports
- `06-tests`: Future execution layer for Playwright, Appium, API, DB, JMeter, and security tests
- `07-integrations`: Jira, Trello, GitHub, Firebase, CMS, Slack, and email integration files
- `08-skills`: Skill library for UI testing, API testing, mobile testing, DB validation, socket testing, security, performance, and reporting
- `09-docs`: Architecture, agent guidelines, workflow guidelines, prompt standards, output standards, and runbooks
- `10-scripts`: Setup, local-run, validation, reporting, and cleanup scripts
- `11-dashboard`: Future operator dashboard and UI mockups

## Phases

### Phase 1

Phase 1 focuses on product analysis and structured test output generation.

Active capabilities:

- Product context extraction
- Test strategy generation
- Task routing
- Token control
- Happy path test case generation
- Edge case and negative case generation
- Basic web, API, and DB analysis
- Daily quality reporting
- Jira/Trello task draft generation

### Phase 2

Phase 2 expands into deeper platform coverage.

Additional capabilities:

- Design and visual QA
- Mobile app analysis
- Notification and Firebase event validation
- Admin panel validation
- CMS validation
- Automation candidate generation
- Basic Playwright and Appium integration

### Phase 3

Phase 3 represents the full AI QA organization.

Full capabilities:

- Eight AI agent teams
- Forty-four AI agent profiles
- Security testing
- Performance and load testing
- Backend development-in-test
- Android development-in-test
- iOS development-in-test
- Release readiness
- Coverage gap and risk trend analysis

## Core Principle

Do not send every task to every agent.

The correct flow is:

1. Understand the product
2. Extract the relevant context
3. Select only the required agents
4. Reduce context before handoff
5. Generate structured outputs
6. Review outputs
7. Produce reports and task drafts

## Current Status

This repository is currently in the foundation stage.

The first target is to complete:

- Repository structure
- Product context files
- Agent registry
- Management agent prompts
- Token policy
- Workflow routing
- Standard output templates