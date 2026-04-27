# Getting Started

## 1. Purpose

This guide helps new users understand how to start using the AI QA Command Center repository.

It explains what to read first, how to inspect demos, how to run validation, and how to add a new feature workflow safely.

---

## 2. What This Repository Is

AI QA Command Center is a structured AI-assisted QA operating framework.

It helps teams generate, organize, review, and govern QA planning artifacts such as:

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
- Release readiness report
- Output review examples
- Automation planning templates
- Integration draft templates

Important:

Generated outputs are planning artifacts only unless real execution evidence exists.

---

## 3. What This Repository Is Not

This repository is not yet:

- A completed SaaS product
- A live dashboard application
- A fully autonomous test execution engine
- A live Jira/Trello/Slack/Figma integration platform
- A replacement for QA engineers
- A replacement for human release approval

AI may generate, organize, review, and recommend.

Humans approve, execute, verify, and decide.

---

## 4. Recommended First Reading Order

| Order | File | Why Read It |
|---:|---|---|
| 1 | README.md | Understand the full repository capability overview |
| 2 | 09-docs/product-packaging/product-overview.md | Understand what the product is |
| 3 | 09-docs/product-packaging/value-proposition.md | Understand why it matters |
| 4 | 09-docs/product-packaging/limitations-and-safety.md | Understand what not to overclaim |
| 5 | 02-agent-registry/agents.yaml | Understand the agent structure |
| 6 | 02-agent-registry/model-routing.yaml | Understand model routing logic |
| 7 | 02-agent-registry/token-policy.yaml | Understand context/token control |
| 8 | 04-workflows | Understand workflow flow |
| 9 | demo/login-feature | Inspect the first complete demo |
| 10 | demo/content-publishing-feature | Inspect the second complete demo |

---

## 5. Key Folder Map

| Folder | Purpose |
|---|---|
| 02-agent-registry | Agent, team, routing, permission, model, and token policy definitions |
| 03-prompts | Agent prompt library |
| 04-workflows | Workflow documentation |
| 05-outputs | Output standards and templates |
| 06-tests | Reserved for future test assets |
| 07-integrations | Integration draft templates and config examples |
| 09-docs | Architecture, governance, onboarding, and product packaging docs |
| 10-scripts/validation | Repository validation scripts |
| 11-dashboard | Dashboard mockup documentation |
| demo | Complete demo feature packs |
| examples | Sample outputs and output review examples |
| references | Patterns, examples, anti-patterns, and QA guidance |
| templates | Input and automation templates |
| .github | AI tool agents, instructions, skills, and GitHub Actions workflow |

---

## 6. How To Inspect The Login Demo

Open:

- demo/login-feature/01-input/
- demo/login-feature/02-outputs/

Recommended files to inspect:

- feature-brief.md
- acceptance-criteria.md
- product-testing-context.md
- test-plan.md
- happy-path-test-cases.md
- edge-negative-test-cases.md
- api-validation-plan.md
- db-validation-plan.md
- release-readiness-report.md

What this demo proves:

- Authentication planning
- Authorization planning
- API validation planning
- DB validation planning
- Session/token risk thinking
- Release readiness safety language

---

## 7. How To Inspect The Content Publishing Demo

Open:

- demo/content-publishing-feature/01-input/
- demo/content-publishing-feature/02-outputs/

Recommended files to inspect:

- feature-brief.md
- acceptance-criteria.md
- test-strategy.md
- edge-negative-test-cases.md
- api-validation-plan.md
- db-validation-plan.md
- release-readiness-report.md

What this demo proves:

- CMS workflow planning
- Draft and publish state validation
- Role-based access coverage
- API authorization checks
- DB state transition planning
- Daily reporting
- Release readiness drafting

---

## 8. How To Run Local Validation

Run these commands from the repository root:

python 10-scripts/validation/check-agent-registry.py

python 10-scripts/validation/check-agent-prompt-coverage.py

Expected result:

- Agent registry validation passed successfully.
- Result: PASSED

If validation fails:

1. Read the missing file list.
2. Check whether the file exists.
3. Check whether the file is empty.
4. Restore or create the missing file.
5. Run validation again.

---

## 9. GitHub Actions Validation

The repository includes GitHub Actions validation:

- .github/workflows/validate-repo.yml

The workflow validates repository structure and required coverage on push and pull request to main.

GitHub Actions should be green after a valid push.

---

## 10. How To Add A New Feature Demo

Recommended structure:

- demo/<feature-name>/01-input/
- demo/<feature-name>/02-outputs/

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

After adding a new demo, update:

- 10-scripts/validation/check-agent-prompt-coverage.py
- CHANGELOG.md
- ROADMAP.md
- README.md if the demo is important enough

---

## 11. How To Review Generated Outputs

Use output review examples under:

- examples/output-reviews/

Recommended review dimensions:

- Completeness
- Clarity
- Risk coverage
- Actionability
- Traceability
- Format compliance
- Safety awareness
- Human approval awareness

Review decisions may include:

- Approved
- Approved with Minor Notes
- Needs Minor Revision
- Needs Revision
- Approved with Required Clarifications
- Approved with Safety Note
- Human Approval Required

---

## 12. How To Use Automation Templates

Automation templates are available under:

- templates/automation/

Current templates:

- playwright-test-template.md
- api-test-template.md
- db-validation-script-template.md
- appium-test-template.md
- performance-test-template.md

Important:

Generated automation drafts are not executed test results.

Do not report automation as passed unless it was actually executed and evidence exists.

---

## 13. How To Use Integration Templates

Integration templates and config examples are available under:

- 07-integrations/

Supported future integration areas:

- Jira
- Trello
- GitHub Issues
- Slack
- Firebase
- Figma

Important:

Integration files are draft and configuration examples only.

AI agents must not create external tickets, cards, issues, messages, comments, or analytics changes without explicit human approval.

---

## 14. What Not To Do

Do not:

- Commit API keys or tokens.
- Commit passwords or private keys.
- Commit production credentials.
- Use real customer data in examples.
- Claim generated outputs are executed results.
- Claim release readiness without evidence and approval.
- Create external tickets or messages without approval.
- Run destructive DB validation without approval.
- Run high-load performance tests without approval.
- Sell the current repository as a completed autonomous SaaS platform.

---

## 15. Recommended Development Flow

Use this flow when adding new capability:

1. Add the new file or folder.
2. Add clear documentation.
3. Update validation script if the file is important.
4. Run local validation.
5. Commit and push.
6. Check GitHub Actions.
7. Update CHANGELOG, ROADMAP, and README when the capability is significant.

---

## 16. Current Best Next Improvements

Recommended next improvements:

- Phase 2 and Phase 3 agent prompts
- Dashboard operator workflow documentation
- Example automation draft outputs
- Live integration dry-run examples
- Advanced output review scoring examples
- Pricing and packaging ideas
- New user onboarding improvements
- Future dashboard implementation
- Future automation generation scripts
- Future live integrations

---

## 17. Final Reminder

This framework is valuable because it is structured, safe, reviewable, and validation-backed.

Do not weaken it by overclaiming execution, skipping human approval, or mixing generated planning artifacts with real test results.
