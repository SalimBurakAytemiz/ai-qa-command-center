# AI QA Command Center System Architecture

## Purpose

This document explains the system architecture of the AI QA Command Center.

It describes the main layers, agent responsibilities, workflow flow, model routing, token policy, output review, safety rules, and future expansion points.

This document is written for human test leaders, QA engineers, SDET engineers, AI workflow designers, and future maintainers.

---

## 1. System Overview

AI QA Command Center is a structured AI-assisted QA operating system.

It helps one human test leader coordinate AI QA agents for product analysis, test planning, test case design, API validation, database validation, web validation, reporting, and future automation.

The system is not a random prompt collection.

It is a layered QA command system.

---

## 2. Core Operating Model

The core model is:

Human Test Leader
-> Management Agents
-> Specialist Agents
-> Output Reviewer Agent
-> Work Tracking and Reporting Agents
-> Human Approval and Decision

The human test leader remains in control.

AI agents assist the workflow, but they do not make final release, security, production, destructive database, or external ticket creation decisions without human approval.

---

## 3. Main Architecture Layers

The system contains these layers:

1. Product Context Layer
2. Agent Registry Layer
3. Management Agent Layer
4. Specialist Agent Layer
5. Prompt Layer
6. Workflow Layer
7. Output Template Layer
8. Skill Library Layer
9. AI Tool Compatibility Layer
10. Reference Library Layer
11. Model Routing Layer
12. Token and Context Policy Layer
13. Output Review Layer
14. Human Approval Layer
15. Integration Layer
16. Test Execution Layer
17. Dashboard Layer
18. Documentation and Governance Layer

---

## 4. Product Context Layer

Location:

- 00-product-context/
- 01-inputs/

Purpose:

This layer stores product and feature information.

It may include:

- Product overview
- User roles
- Product modules
- PRD files
- Figma notes
- API specifications
- Backend documentation
- Frontend documentation
- Mobile documentation
- CMS documentation
- Firebase event notes
- Release notes

Architecture rule:

Raw product information should not be sent directly to every agent.

Product Intake Agent and Token Controller Agent should reduce raw context into compact, task-specific context packages.

---

## 5. Agent Registry Layer

Location:

- 02-agent-registry/

Important files:

- agents.yaml
- teams.yaml
- management-agents.yaml
- model-routing.yaml
- permissions.yaml
- token-policy.yaml
- workflow-routing.yaml

Purpose:

This layer defines the AI QA organization model.

It defines:

- Teams
- Agents
- Agent roles
- Agent purposes
- Inputs
- Outputs
- Model routing
- Token policy
- Permissions
- Workflow routing

Architecture rule:

Important agents should be represented in the registry.

Agents should not be invented randomly during workflow execution.

---

## 6. Agent Team Architecture

The system is organized around:

- 1 Human Test Leader
- 8 AI QA Teams
- 44 AI Agent Profiles

Major team categories:

- Management and Orchestration
- Test Planning and Test Case Design
- Product Flow and Feature Validation
- Design, UI, and Visual Validation
- Web, Mobile, and Notification Validation
- Backend, API, DB, and Realtime Validation
- Security, Performance, and Release Readiness
- Operations, Reporting, and Work Tracking

Architecture rule:

Not all agents should run for every task.

Task Router Agent must select only the required agents based on scope, risk, platform, and technical layers.

---

## 7. Management Agent Layer

Purpose:

Management agents control the workflow.

They coordinate, route, reduce context, and review.

Current management agents:

- Product Intake Agent
- Test Strategy Agent
- Task Router Agent
- Token Controller Agent
- Output Reviewer Agent

Responsibilities:

Product Intake Agent:
Converts raw product information into structured product testing context.

Test Strategy Agent:
Defines test scope, risk level, validation types, and testing focus.

Task Router Agent:
Selects which specialist agents should work.

Token Controller Agent:
Creates compact context packages for specialist agents.

Output Reviewer Agent:
Reviews generated outputs, scores quality, detects issues, and identifies human approval needs.

---

## 8. Specialist Agent Layer

Purpose:

Specialist agents perform focused QA work.

Current Phase 1 specialist agents:

- Test Planning Agent
- Happy Path Test Case Agent
- Edge Case and Negative Case Agent
- Product Flow Test Agent
- Feature Validation Agent
- Web Functional Test Agent
- API Test Agent
- Database Validation and Data Integrity Agent
- Test Environment and System Health Agent
- Jira and Trello Work Tracking Agent
- Daily Quality Report Agent

Architecture rule:

Specialist agents must receive compact context, not full raw product documentation.

Each specialist agent must stay inside its responsibility area.

---

## 9. Prompt Layer

Location:

- 03-prompts/

Purpose:

This layer contains operational instructions for agent execution.

Prompt files define:

- Role
- Purpose
- Input sources
- Main task
- Working rules
- Output format
- Quality criteria

Architecture rule:

Prompt files should be stable, reusable, and role-specific.

One agent should not be responsible for everything.

---

## 10. Workflow Layer

Location:

- 04-workflows/

Purpose:

This layer defines how agents work together.

Current workflows include:

- Product to Test Pack workflow
- Product Intake workflow
- Test Case Generation workflow
- API and DB Validation workflow
- Daily Report workflow

Standard workflow:

1. Raw product input is collected.
2. Product Intake Agent creates product testing context.
3. Test Strategy Agent defines scope and risk.
4. Task Router Agent selects required agents.
5. Token Controller Agent prepares compact context packages.
6. Selected specialist agents generate outputs.
7. Output Reviewer Agent reviews and scores outputs.
8. Jira/Trello and reporting agents prepare drafts.
9. Human test leader reviews and approves next action.

Architecture rule:

Workflow execution must move from broad understanding to focused execution.

The system must not send full product documents to every agent.

---

## 11. Output Template Layer

Location:

- 05-outputs/

Purpose:

This layer defines standard structures for generated QA artifacts.

Output categories include:

- Test plans
- Test cases
- Happy path cases
- Edge cases
- Negative cases
- Risk analysis
- API validation
- DB validation
- Jira/Trello drafts
- Reports

Architecture rule:

Agents should follow templates.

Agents should not invent output structures unless explicitly instructed.

---

## 12. Skill Library Layer

Location:

- 08-skills/

Purpose:

This layer gives agents QA domain knowledge.

Current skill areas include:

- Test case design
- API testing
- DB validation
- UI testing
- QA reporting

Architecture rule:

Skills define how to think about QA problems.

Prompts define what the agent must do.

Both are needed.

---

## 13. AI Tool Compatibility Layer

Location:

- .github/

Structure:

- .github/agents/
- .github/instructions/
- .github/skills/

Purpose:

This layer makes the repository easier to use with AI coding and assistant tools such as Cursor, Claude Code, GitHub Copilot, and VS Code-based AI workflows.

Current AI-compatible agents:

- QA Orchestrator Agent
- Test Case Designer Agent
- API Test Agent
- Database Validation Agent
- Web Functional Test Agent

Current AI-compatible skills:

- Test Case Design
- API Testing
- DB Validation
- Web Functional Testing
- QA Reporting

Architecture rule:

The .github layer must stay aligned with the core prompt and skill layers.

It must not contradict 03-prompts/, 08-skills/, or 09-docs/.

---

## 14. Reference Library Layer

Location:

- references/

Purpose:

This layer improves AI output quality with examples, patterns, and anti-patterns.

Current references include:

- Testing anti-patterns
- Test case examples
- API testing patterns
- DB validation patterns
- Playwright testing patterns

Architecture rule:

Reference documents should teach behavior through concrete examples.

They should reduce vague, generic, and low-quality AI output.

---

## 15. Model Routing Layer

Location:

- 02-agent-registry/model-routing.yaml

Purpose:

This layer defines which AI provider or model profile should be used for different agent types and task categories.

Supported provider categories include:

- OpenAI
- Anthropic
- Google Gemini
- Azure OpenAI
- OpenRouter
- Mistral
- Groq
- Together AI
- Perplexity
- Cohere
- DeepSeek
- xAI
- Ollama
- LM Studio

Routing strategy:

Use stronger reasoning models for:

- Product intake
- Test strategy
- Agent routing
- Token/context reduction
- Output review
- Risk analysis
- Release readiness
- Executive summaries

Use faster or cheaper models for:

- Bulk test case generation
- Initial scenario drafts
- Repetitive output formatting
- Simple summaries

Use local models for:

- Private product context
- Sensitive customer-specific information
- Internal architecture notes
- Security-sensitive information

Architecture rule:

Model routing must be task-aware.

The system should not use the most expensive model for every task.

The system should not send sensitive context to external providers without approval.

---

## 16. Token and Context Policy Layer

Location:

- 02-agent-registry/token-policy.yaml

Purpose:

This layer defines how much context agents should receive and when human approval is required for large, sensitive, or expensive context usage.

Context modes:

- minimal
- compact
- standard
- extended
- full_requires_approval

Key rules:

- Do not send full product documentation to every agent.
- Use compact context packages for specialist agents.
- Preserve acceptance criteria, business rules, user roles, platforms, and risks.
- Remove unrelated modules and duplicate descriptions.
- Require review for fallback-generated critical outputs.
- Prefer local models for sensitive data.
- Do not treat generated outputs as executed results.

Architecture rule:

Token control is not optional.

Without token control, multi-agent QA workflows become expensive, noisy, and unreliable.

---

## 17. Output Review Layer

Main agent:

- Output Reviewer Agent

Purpose:

This layer protects the workflow from poor AI outputs.

It checks:

- Completeness
- Clarity
- Risk coverage
- Actionability
- Duplicate control
- Format compliance
- Traceability
- Safety and approval awareness
- Generated vs executed wording
- Fallback metadata
- Token/context policy compliance
- Model routing compliance

Quality score dimensions:

- Completeness
- Clarity
- Risk Coverage
- Actionability
- Duplicate Control
- Format Compliance
- Traceability
- Safety and Approval Awareness

Architecture rule:

Important outputs should not be used without review.

Fallback-generated critical outputs must be reviewed.

---

## 18. Human Approval Layer

Purpose:

This layer ensures that the AI system does not make risky decisions without human control.

Human approval is required for:

- P0 classification
- Release go/no-go decisions
- Security-sensitive findings
- Production data usage
- Destructive DB validation
- External AI usage for sensitive data
- Jira/Trello ticket creation
- Final management reports
- Unclear but high-risk assumptions
- Fallback-generated critical outputs

Architecture rule:

The human test leader is the final authority.

AI agents can recommend, prepare, summarize, and review.

They cannot make final high-risk decisions alone.

---

## 19. Integration Layer

Location:

- 07-integrations/

Purpose:

This layer is reserved for future integrations.

Planned integrations include:

- Jira
- Trello
- GitHub
- Firebase
- CMS
- Slack
- Email
- Figma
- OpenAPI / Swagger
- Postman / Newman

Architecture rule:

Integration output should start as drafts.

External actions should require human approval unless explicitly configured otherwise.

---

## 20. Test Execution Layer

Location:

- 06-tests/

Purpose:

This layer is reserved for future generated or manually maintained test assets.

Planned areas include:

- Playwright web tests
- Appium mobile tests
- API tests
- DB validation tests
- JMeter performance tests
- Security tests
- Fixtures

Architecture rule:

The system must clearly separate:

- Generated test plans
- Generated test cases
- Automation candidates
- Executed test results

Generated test artifacts are not execution results.

---

## 21. Dashboard Layer

Location:

- 11-dashboard/

Purpose:

This layer is reserved for future operator interface work.

Planned dashboard capabilities include:

- Project selection
- Feature intake
- Agent routing view
- Output package view
- Risk matrix view
- Quality score view
- Jira/Trello draft view
- Daily report view
- Human approval gates
- Workflow history

Architecture rule:

The dashboard should not be built before the manual workflow, output examples, and validation rules are stable.

---

## 22. Documentation and Governance Layer

Location:

- 09-docs/

Purpose:

This layer defines standards, rules, and operational guidance.

Current documents include:

- Prompt standards
- Agent guidelines
- Workflow guidelines
- Output standards
- First-run runbook
- System architecture

Architecture rule:

The system must remain understandable to future maintainers.

Documentation is part of the product, not an afterthought.

---

## 23. Data Flow

Input flow:

Raw input files
-> Product Testing Context
-> Test Strategy
-> Agent Routing Plan
-> Compact Context Packages

Specialist output flow:

Compact Context Package
-> Specialist Agent Output
-> Output Review
-> Revised or Approved Output

Reporting flow:

Reviewed Outputs
-> Jira/Trello Drafts
-> Daily Quality Report
-> Executive Summary
-> Human Review

---

## 24. Safety Architecture

The system includes safety controls in multiple layers.

Registry safety:

- 02-agent-registry/permissions.yaml

Model routing safety:

- 02-agent-registry/model-routing.yaml

Token and context safety:

- 02-agent-registry/token-policy.yaml

Output safety:

- 03-prompts/01-management-team/output-reviewer-agent.md
- 09-docs/output-standards/README.md

General AI instruction safety:

- .github/instructions/qa-general.instructions.md

---

## 25. What The System Is Not

The system is not:

- A fully automated test execution platform yet
- A replacement for a human QA leader
- A release decision engine
- A production monitoring tool
- A security scanner
- A CI/CD system
- A Jira automation bot by default
- A one-click test automation generator yet

These capabilities may be added in future phases.

---

## 26. Current Architecture Status

Completed:

- Foundation repository structure
- Agent registry
- Management prompts
- Phase 1 specialist prompts
- Output templates
- Workflow documents
- Skill library
- AI tool compatibility layer
- Reference library foundation
- Multi-provider model routing
- Token and context policy
- Output reviewer scoring
- General AI instructions
- Roadmap
- Changelog
- License
- README update

In progress:

- Architecture documentation
- Demo feature packs
- Templates
- Example outputs
- Expanded AI instructions
- Expanded references
- Validation and CI

Not started:

- External integrations
- Test execution automation
- Dashboard
- Full Phase 2 and Phase 3 prompt coverage
- GitHub Actions validation
- Agent prompt coverage validation

---

## 27. Recommended Next Architecture Steps

The next architecture steps are:

1. Complete demo login feature pack.
2. Add product and feature intake templates.
3. Add sample output examples.
4. Add AI instruction files for test case design, API testing, DB validation, Playwright, and reporting.
5. Add agent prompt coverage validation.
6. Add GitHub Actions validation.
7. Expand references for bug reports, Jira tickets, daily reports, risk analysis, and release readiness.
8. Add integration templates.
9. Add automation generation patterns.
10. Add dashboard mockups.

---

## 28. Final Architecture Principle

The system should grow carefully.

Do not build dashboards, integrations, or automation execution before the manual workflow, output examples, and validation rules are stable.

The goal is controlled AI-assisted QA operations, not uncontrolled AI output generation.
