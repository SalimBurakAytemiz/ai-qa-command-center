# Contributing Guide

## 1. Purpose

This guide explains how to contribute to the AI QA Command Center repository safely and consistently.

The repository is not just a folder of prompts.

It is a structured AI-assisted QA operating framework with validation, governance, examples, demos, templates, references, and product packaging documentation.

---

## 2. Core Contribution Rule

Every contribution must preserve this principle:

AI may generate, organize, review, and recommend.

Humans approve, execute, verify, and decide.

Generated QA artifacts are not executed test results.

Reviewed artifacts are not release approval.

Release readiness requires execution evidence and human approval.

---

## 3. What Contributions Are Welcome

Useful contributions include:

- New agent prompts
- Improved existing prompts
- New workflow documentation
- New output templates
- New reference examples
- New anti-patterns
- New demo feature packs
- New output review examples
- New automation templates
- New integration templates
- New dashboard mockups
- New product packaging documentation
- New onboarding documentation
- New validation checks
- Documentation cleanup
- Structure improvements

---

## 4. What Must Not Be Added

Do not add:

- Real API keys
- Access tokens
- Refresh tokens
- Passwords
- Private keys
- Service account JSON files
- Production credentials
- Customer personal data
- Payment data
- Private customer URLs
- Sensitive internal security details
- Real production logs
- Real customer screenshots
- Destructive DB scripts
- Live external integration actions without approval

Use placeholders and environment variable names instead.

---

## 5. Generated vs Executed Language Rules

Use safe wording for generated outputs:

- Generated
- Drafted
- Planned
- Proposed
- Reviewed
- Needs Revision
- Human Approval Required
- Execution Evidence Required

Do not use unsafe wording unless real execution evidence exists:

- Passed
- Verified
- Tested successfully
- Execution completed
- Production safe
- Release ready
- QA approved

If execution did not happen, say so clearly.

---

## 6. When To Update The Validation Script

Update this file when adding important repository assets:

- 10-scripts/validation/check-agent-prompt-coverage.py

Update validation coverage when adding:

- Required prompts
- Required instructions
- Required skills
- Required templates
- Required demo input files
- Required demo output files
- Required examples
- Required references
- Required dashboard mockups
- Required product packaging docs
- Required onboarding docs
- Required workflow examples
- Required integration examples

If a file is important enough that the repository depends on it, validation should check it.

---

## 7. When To Update README, ROADMAP, and CHANGELOG

Update documentation when a contribution adds a meaningful capability.

Update:

- README.md
- ROADMAP.md
- CHANGELOG.md

for changes such as:

- New demo feature pack
- New major reference layer
- New automation template layer
- New integration layer
- New dashboard layer
- New product packaging layer
- New onboarding layer
- New validation behavior
- New workflow examples
- New agent phase

Small typo fixes usually do not require roadmap updates.

---

## 8. Adding A New Demo Feature Pack

Use this structure:

demo/<feature-name>/01-input/

demo/<feature-name>/02-outputs/

Minimum input files:

- feature-brief.md
- acceptance-criteria.md
- api-notes.md
- db-notes.md
- ui-notes.md

Recommended output files:

- product-testing-context.md
- test-strategy.md
- agent-routing-plan.md
- test-plan.md
- happy-path-test-cases.md
- edge-negative-test-cases.md
- api-validation-plan.md
- db-validation-plan.md
- jira-trello-drafts.md
- daily-quality-report.md
- executive-summary.md
- release-readiness-report.md

After adding the demo:

1. Update validation script.
2. Run validation locally.
3. Update README, ROADMAP, and CHANGELOG if the demo is important.
4. Commit and push.
5. Check GitHub Actions.

---

## 9. Adding A New Agent Prompt

When adding a new agent prompt:

1. Place it under the correct prompt team folder in 03-prompts.
2. Define the agent role clearly.
3. Define input expectations.
4. Define output format.
5. Define safety rules.
6. Define human approval needs.
7. Avoid execution claims.
8. Add references if needed.
9. Update agent registry if the agent is part of the formal system.
10. Update validation script if the prompt is required.

---

## 10. Adding A New Template

When adding a template:

1. Put it in the correct templates folder.
2. Use clear section headings.
3. Include missing information handling.
4. Include human approval points when relevant.
5. Include generated vs executed notes.
6. Avoid real secrets or real production data.
7. Update validation script if the template is required.

---

## 11. Adding A New Reference

When adding a reference document:

1. Put it in the correct references folder.
2. Explain purpose.
3. Provide good examples.
4. Provide bad examples when useful.
5. Include safety notes.
6. Include human approval points when relevant.
7. Include generated vs executed distinction when relevant.
8. Update validation script if it is a core reference.

---

## 12. Adding Integration Documentation

Integration documents must remain safe by default.

Rules:

- Default mode should be dry_run.
- External actions should be disabled by default.
- Human approval must be required for external actions.
- Do not include real tokens or private URLs.
- Do not send or create anything automatically in documentation examples.

Integration areas currently include:

- Jira
- Trello
- GitHub Issues
- Slack
- Firebase
- Figma

---

## 13. Adding Automation Documentation

Automation documentation must distinguish between:

- Automation candidate
- Automation draft
- Automation execution
- Automation result

Generated automation drafts are not executed results.

Human approval is required before:

- Production execution
- Destructive DB checks
- High-load performance tests
- Payment flow tests
- Real customer data usage
- Security-sensitive execution

---

## 14. Local Validation Before Commit

Before committing meaningful changes, run:

python 10-scripts/validation/check-agent-registry.py

python 10-scripts/validation/check-agent-prompt-coverage.py

Expected result:

- Agent registry validation passed successfully.
- Result: PASSED

If validation fails, fix the missing or empty files before pushing.

---

## 15. Git Workflow

Recommended flow:

1. Make changes.
2. Run validation.
3. Check git status.
4. Add relevant files.
5. Commit with a clear message.
6. Push.
7. Check GitHub Actions.

Example:

git status

python 10-scripts/validation/check-agent-registry.py

python 10-scripts/validation/check-agent-prompt-coverage.py

git add <files>

git commit -m "Clear commit message"

git push

git status

---

## 16. Commit Message Guidance

Good commit messages:

- Add content publishing demo input pack
- Update validation coverage for onboarding guide
- Add automation generation templates
- Update README with product packaging layer
- Add output review examples

Bad commit messages:

- update
- fix
- stuff
- changes
- final
- aaa

Commit messages should explain what changed.

---

## 17. Pull Request Checklist

Before opening or merging a pull request, confirm:

- No secrets are committed.
- No production data is included.
- Generated vs executed language is safe.
- Human approval gates are preserved.
- New required files are added to validation.
- README/ROADMAP/CHANGELOG are updated if needed.
- Local validation passes.
- GitHub Actions passes.
- The contribution fits the repository structure.

---

## 18. Review Checklist

Reviewers should check:

- Is the contribution useful?
- Is the file in the correct location?
- Does it preserve safety rules?
- Does it avoid overclaiming?
- Does it avoid secrets?
- Does it avoid fake execution claims?
- Does it include missing information handling?
- Does it include human approval points when relevant?
- Does validation pass?
- Does documentation need updating?

---

## 19. Safety Escalation

Human approval is required for:

- Release readiness claims
- P0/P1 risk acceptance
- Security-sensitive findings
- Production data usage
- Real customer account usage
- Destructive DB validation
- High-load performance testing
- External ticket/message/comment creation
- Executive report publication

Do not bypass these gates.

---

## 20. Final Principle

The repository should become more useful without becoming less safe.

If a contribution makes the system sound more powerful than it really is, revise it.

If a contribution helps humans review, decide, and execute more responsibly, it is probably aligned with the project.
