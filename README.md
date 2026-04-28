# AI QA Command Center

AI QA Command Center is a structured AI-assisted QA operating framework.

It helps software teams generate, review, organize, and govern QA planning artifacts across product analysis, test planning, API validation, DB validation, reporting, release readiness, automation planning, integration planning, and future dashboard workflows.

> Current release: v1.2.0 Documentation Index and Agent Coverage Matrix

---

## What This Repository Is

AI QA Command Center is a repository-based QA operating kit for AI-assisted software testing work.

It provides:

- Agent registry
- Prompt library
- Workflow documentation
- Output templates
- Demo feature packs
- Reference examples
- Output review examples
- Automation draft examples
- Integration dry-run examples
- Dashboard workflow documentation
- Product packaging documentation
- Validation scripts
- GitHub Actions CI

---

## What This Repository Is Not

This repository is not:

- A completed SaaS product
- A live dashboard application
- A fully autonomous QA execution engine
- A live Jira/Trello/GitHub/Slack/Figma/Firebase integration platform
- A replacement for QA engineers
- A replacement for human release approval
- A replacement for security testing or penetration testing

Generated QA artifacts are not executed test results.

Reviewed artifacts are not release approval.

Release readiness requires execution evidence and human approval.

---

## Core Principle

AI may generate, organize, review, and recommend.

Humans approve, execute, verify, and decide.

The framework must always separate:

- Generated planning artifacts
- Reviewed artifacts
- Executed test evidence
- Approved release decisions

---

## Current v1.0.0 Capability Summary

AI QA Command Center v1.0.0 includes:

- Structured AI QA team architecture
- Agent registry
- Prompt library
- Phase 2 specialist prompts
- Phase 3 operations prompts
- Workflow documentation
- Output templates
- Skill library
- AI tool compatibility layer
- Multi-provider model routing
- Token and context policy
- Permissions policy
- Output review rules
- Output review examples
- Input templates
- Complete login feature demo
- Complete content publishing feature demo
- Release readiness demo outputs
- Reference examples
- Anti-patterns
- Security testing checklist
- Performance testing patterns
- Mobile testing patterns
- Firebase analytics validation patterns
- Integration templates
- Integration configuration examples
- Integration dry-run examples
- Automation candidate guidance
- Automation templates
- Automation draft examples
- Dashboard mockups
- Dashboard operator workflow documentation
- Sample GitHub Actions workflow examples
- Product packaging documentation
- Pricing and packaging documentation
- Sales one-pager
- Onboarding guide
- Contributor guide
- Maintainers guide
- Validation scripts
- GitHub Actions CI

---

## Demo Feature Packs

The repository includes two complete demo feature packs.

| Demo | Focus |
|---|---|
| Login Feature Demo | Authentication, authorization, API, DB, session, release readiness |
| Content Publishing Feature Demo | CMS workflow, draft/publish states, role boundaries, API, DB, reporting, release readiness |

Demo locations:

- demo/login-feature/
- demo/content-publishing-feature/

---

## Key Folders

| Folder | Purpose |
|---|---|
| 02-agent-registry/ | Agent, team, routing, token, model, and permission policies |
| 03-prompts/ | Prompt library for QA agents |
| 04-workflows/ | Workflow documentation |
| 05-outputs/ | Output standards and templates |
| 07-integrations/ | Integration templates and config examples |
| 09-docs/ | Architecture, onboarding, product packaging, and release docs |
| 10-scripts/validation/ | Repository validation scripts |
| 11-dashboard/ | Dashboard mockups and operator workflow |
| demo/ | Complete demo feature packs |
| examples/ | Output review, automation draft, and integration dry-run examples |
| references/ | Patterns, examples, anti-patterns, and QA guidance |
| templates/ | Input and automation templates |

---

## Quick Start

Clone the repository:

~~~bash
git clone https://github.com/SalimBurakAytemiz/ai-qa-command-center.git
cd ai-qa-command-center
~~~

Install dependencies:

~~~bash
pip install -r requirements.txt
~~~

Run validation:

~~~bash
python 10-scripts/validation/check-agent-registry.py
python 10-scripts/validation/check-agent-prompt-coverage.py
~~~

Expected result:

~~~text
Agent registry validation passed successfully.
Result: PASSED
~~~

---

## Recommended Reading Order

Start here:

1. README.md
2. 09-docs/onboarding/getting-started.md
3. 09-docs/product-packaging/product-overview.md
4. 09-docs/product-packaging/value-proposition.md
5. 09-docs/product-packaging/limitations-and-safety.md
6. 09-docs/product-packaging/sales-one-pager.md
7. demo/login-feature/
8. demo/content-publishing-feature/
9. 09-docs/releases/v1.0-release-notes.md

---

## Product Packaging

Product and sales documentation is available under:

- 09-docs/product-packaging/product-overview.md
- 09-docs/product-packaging/value-proposition.md
- 09-docs/product-packaging/target-users.md
- 09-docs/product-packaging/demo-script.md
- 09-docs/product-packaging/limitations-and-safety.md
- 09-docs/product-packaging/buyer-faq.md
- 09-docs/product-packaging/sales-one-pager.md
- 09-docs/product-packaging/pricing/

Recommended commercial positioning:

Framework + setup + customization + training + support.

Do not sell v1.0 as a fully autonomous QA SaaS product.

---

## Release Documentation

Release documents:

- 09-docs/releases/v1.0-release-candidate.md
- 09-docs/releases/v1.0-release-notes.md

GitHub release:

- v1.0.0

---

## Validation and CI

The repository includes local validation scripts and GitHub Actions validation.

Local validation:

~~~bash
python 10-scripts/validation/check-agent-registry.py
python 10-scripts/validation/check-agent-prompt-coverage.py
~~~

GitHub Actions workflow:

- .github/workflows/validate-repo.yml

---

## Safety Rules

Do not commit:

- API keys
- Access tokens
- Refresh tokens
- Passwords
- Private keys
- Service account files
- Production credentials
- Real customer data
- Payment data
- Sensitive logs
- Temporary debug files

Default integration mode should be:

~~~text
dry_run
~~~

Human approval is required before:

- External ticket/card/issue/message creation
- Production data usage
- Real customer account usage
- Destructive DB validation
- High-load performance testing
- Release readiness decisions

---

## Contributing and Maintaining

Contributor guide:

- CONTRIBUTING.md

Maintainer guide:

- MAINTAINERS.md

Before contributing:

1. Run local validation.
2. Keep generated vs executed language clear.
3. Update validation coverage when adding required files.
4. Update README, ROADMAP, and CHANGELOG for meaningful capability changes.
5. Check GitHub Actions after push.

---

## License

This repository is public for portfolio and demo visibility.

No reuse license is granted by default.

See:

- LICENSE

---


---

## Current v1.1.0 Update

v1.1.0 improves repository hygiene and expands advanced prompt coverage.

Added in v1.1.0:

- P0 technical hygiene cleanup
- Clean `.gitignore`
- `.gitattributes`
- Clean GitHub Actions workflow
- Clean validation scripts
- `requirements.txt` dependency definition
- Missing permissions policy
- Simplified README
- Normalized CHANGELOG and ROADMAP
- SECURITY.md
- Pull request template
- Issue templates
- CODEOWNERS
- Execution evidence template
- Design/UI specialist prompts
- DIT specialist prompts
- Validation coverage updates

New Design/UI prompts:

- `03-prompts/phase-2-specialists/design-ui/web-pixel-perfect-agent.md`
- `03-prompts/phase-2-specialists/design-ui/mobile-responsive-agent.md`
- `03-prompts/phase-2-specialists/design-ui/ios-ui-agent.md`
- `03-prompts/phase-2-specialists/design-ui/android-ui-agent.md`
- `03-prompts/phase-2-specialists/design-ui/visual-regression-agent.md`
- `03-prompts/phase-2-specialists/design-ui/accessibility-agent.md`

New DIT prompts:

- `03-prompts/phase-2-specialists/dit/backend-dit-agent.md`
- `03-prompts/phase-2-specialists/dit/android-dit-agent.md`
- `03-prompts/phase-2-specialists/dit/ios-dit-agent.md`
- `03-prompts/phase-2-specialists/dit/testability-agent.md`

Execution evidence template:

- `templates/execution-evidence-template.md`

Design/UI and DIT outputs are generated planning or review artifacts only.

They are not execution evidence.


---

## Current v1.2.0 Update

v1.2.0 improves documentation navigation and coverage transparency.

Added in v1.2.0:

- Documentation index
- Agent coverage matrix
- Validation coverage for the documentation index and coverage matrix

New documentation files:

- `09-docs/README.md`
- `09-docs/agent-coverage-matrix.md`

The agent coverage matrix clarifies:

- Covered agent areas
- Partially covered areas
- Planned areas
- Remaining implementation gaps
- Difference between planning coverage and execution evidence

Coverage does not mean execution.

Generated QA artifacts are not executed test results.

## Post-v1.0 Roadmap

Post-v1.0 work should focus on implementation:

- Real automation generation scripts
- Real live integrations
- Real dashboard application
- Execution evidence import
- Approval workflow implementation
- User/project management
- SaaS/product implementation plan
- Hosted documentation site if needed
