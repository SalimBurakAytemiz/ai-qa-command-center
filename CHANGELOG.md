# Changelog

All notable changes to the AI QA Command Center repository will be documented in this file.

This changelog tracks repository-level progress, not executed QA results.

---

## [Unreleased]

## [0.6.0] - Demo, References, Instructions, and Validation Layer

### Added

- Added product and feature intake templates.
- Added acceptance criteria template.
- Added API notes template.
- Added DB notes template.
- Added release scope template.
- Added complete login feature demo input pack.
- Added complete login feature demo output pack.
- Added sample output library.
- Added sample test plan output.
- Added sample happy path test cases output.
- Added sample edge and negative test cases output.
- Added sample API validation plan output.
- Added sample DB validation plan output.
- Added sample Jira draft output.
- Added sample daily quality report output.
- Added sample executive summary output.
- Added specialized AI instruction files for:
  - Test case design
  - API testing
  - DB validation
  - Playwright
  - QA reporting
- Added reference examples for:
  - API testing
  - DB validation
  - Bug reports
  - Jira tickets
  - Daily reports
- Added permissions policy file.
- Added agent prompt coverage validation script.
- Added Python requirements file.
- Added GitHub Actions workflow for repository validation.

### Changed

- Improved repository validation coverage.
- Strengthened CI readiness.
- Aligned repository structure with demo, examples, references, templates, and AI tool instructions.
- Renamed prompt files for better validation consistency:
  - `edge-negative-case-agent.md` to `edge-case-negative-case-agent.md`
  - `db-validation-agent.md` to `database-validation-agent.md`
  - `jira-trello-agent.md` to `jira-trello-work-tracking-agent.md`

### Validation

- Agent registry validation passes.
- Agent prompt coverage validation passes.
- GitHub Actions repository validation workflow passes on `main`.

### Notes

This phase turns the repository from a structured foundation into a demonstrable AI QA framework.

The repository now includes reusable input templates, a complete login feature demo, sample outputs, expanded AI tool instructions, stronger reference examples, validation scripts, and GitHub Actions CI.

Generated demo outputs are still planning artifacts only.

They must not be reported as executed test results.

---


### Planned

- Add complete login feature demo pack.
- Add output quality scoring to Output Reviewer Agent.
- Expand AI tool instructions.
- Add more reference examples for API, DB, bug reporting, Jira/Trello, and daily reports.
- Add agent prompt coverage validation.
- Add GitHub Actions validation workflow.
- Update README with current repository structure and usage flow.
- Add architecture documentation.
- Add product and feature intake templates.

---

## [0.5.0] - Repository Completeness Layer

### Added

- Added `.gitkeep` files for empty structural folders.
- Added visible input folders under `01-inputs/`.
- Added visible test folders under `06-tests/`.
- Added visible integration folders under `07-integrations/`.
- Added visible dashboard folders under `11-dashboard/`.
- Added `demo/` folder structure.
- Added `examples/` folder structure.
- Added `templates/` folder structure.
- Added `ROADMAP.md`.

### Notes

This phase improves repository completeness and makes the intended project structure visible on GitHub.

---

## [0.4.0] - AI Tool Compatibility and Reference Layer

### Added

- Added `.github/agents/` structure.
- Added `.github/instructions/` structure.
- Added `.github/skills/` structure.
- Added QA Orchestrator agent.
- Added Test Case Designer agent.
- Added API Test Agent.
- Added Database Validation Agent.
- Added Web Functional Test Agent.
- Added general QA instructions.
- Added AI-compatible QA skill files.
- Added testing anti-patterns reference.
- Added test case examples.
- Added API testing patterns.
- Added DB validation patterns.
- Added Playwright testing patterns.

### Notes

This phase makes the repository more usable by AI coding and assistant tools such as Cursor, Claude Code, GitHub Copilot, and VS Code-based workflows.

---

## [0.3.0] - Standards, Scripts, and Documentation Layer

### Added

- Added prompt standards documentation.
- Added agent guidelines.
- Added workflow guidelines.
- Added output standards.
- Added first-run runbook.
- Added setup script for repository folders.
- Added required files validation script.
- Added agent registry validation script.
- Added generated output cleanup script.

### Notes

This phase improves maintainability, repeatability, and repository governance.

---

## [0.2.0] - Workflow, Output, and Skill Foundation

### Added

- Added output templates for test plans.
- Added output templates for test cases.
- Added output templates for happy path cases.
- Added output templates for edge cases.
- Added output templates for negative cases.
- Added output templates for risk analysis.
- Added output templates for API validation.
- Added output templates for DB validation.
- Added output templates for Jira/Trello drafts.
- Added output templates for daily quality reports.
- Added master product-to-test-pack workflow.
- Added product intake workflow.
- Added test case generation workflow.
- Added API and DB validation workflow.
- Added daily quality report workflow.
- Added QA skill library for:
  - Test case design
  - API testing
  - DB validation
  - UI testing
  - QA reporting

### Notes

This phase defines how agents should produce standard outputs and how workflows should operate.

---

## [0.1.0] - Agent Registry and Prompt Foundation

### Added

- Added initial repository structure.
- Added product context files.
- Added 8 AI QA team definitions.
- Added 44 AI agent registry.
- Added management agent registry.
- Added model routing rules.
- Added permission rules.
- Added workflow routing rules.
- Added token policy.
- Added management team prompts:
  - Product Intake Agent
  - Test Strategy Agent
  - Task Router Agent
  - Token Controller Agent
  - Output Reviewer Agent
- Added Phase 1 specialist agent prompts:
  - Test Planning Agent
  - Happy Path Test Case Agent
  - Edge Case and Negative Case Agent
  - Product Flow Test Agent
  - Feature Validation Agent
  - Web Functional Test Agent
  - API Test Agent
  - Database Validation Agent
  - Environment Health Agent
  - Jira/Trello Work Tracking Agent
  - Daily Quality Report Agent

### Notes

This phase establishes the core AI QA Command Center structure and the first usable manual AI QA workflow foundation.

---

## [0.0.1] - Initial Repository

### Added

- Created initial Git repository.
- Added initial README.
- Added `.gitignore`.
- Added `.env.example`.

### Notes

This was the starting point of the AI QA Command Center repository.
