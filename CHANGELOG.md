# Changelog

All notable changes to AI QA Command Center are documented here.

---

## [1.1.0] - Repository Hygiene, Evidence, Design/UI, and DIT Expansion

### Added

- Added `.gitattributes` for line ending normalization.
- Added `SECURITY.md`.
- Added GitHub pull request template.
- Added GitHub issue templates.
- Added GitHub CODEOWNERS.
- Added execution evidence template.
- Added Design/UI specialist prompts:
  - Web Pixel Perfect Agent
  - Mobile Responsive Agent
  - iOS UI Agent
  - Android UI Agent
  - Visual Regression Agent
  - Accessibility Agent
- Added DIT specialist prompts:
  - Backend DIT Agent
  - Android DIT Agent
  - iOS DIT Agent
  - Testability Agent
- Added validation coverage for new evidence, Design/UI, and DIT assets.

### Changed

- Rewrote `.gitignore` into a proper line-based ignore file.
- Rewrote GitHub Actions workflow as clean YAML.
- Rewrote validation scripts into clean Python files.
- Added `PyYAML` to `requirements.txt`.
- Added missing permissions policy under agent registry.
- Simplified README into a professional project landing page.
- Normalized CHANGELOG and ROADMAP for readability.
- Improved public repository hygiene and maintainability.

### Validation

- Agent registry validation passes.
- Agent prompt coverage validation passes.
- GitHub Actions repository validation is expected to pass.

### Notes

v1.1 improves repository quality and closes several framework coverage gaps.

Design/UI and DIT prompts generate planning and review artifacts only.

Execution evidence still requires real execution, safe evidence handling, and human review.

---

## [1.0.0] - Stable Framework Release

### Added

- Added v1.0 release candidate documentation.
- Added v1.0 release notes.
- Finalized the first stable AI QA Command Center framework release.

### Included In v1.0

- Structured AI QA team architecture
- Agent registry and team registry
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
- Output review rules and examples
- Input templates
- Complete login feature demo
- Complete content publishing feature demo
- Release readiness demo outputs
- Reference library
- Anti-patterns
- Security testing checklist
- Performance testing patterns
- Mobile testing patterns
- Firebase analytics validation patterns
- Integration draft templates
- Integration configuration examples
- Integration dry-run examples
- Automation candidate guidance
- Automation generation templates
- Automation draft examples
- Dashboard mockup documentation
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

### Validation

- Agent registry validation passes.
- Agent prompt coverage validation passes.
- GitHub Actions repository validation is available.

### Notes

v1.0 is a stable framework release.

It is demo-ready, validation-backed, CI-enabled, product-packaging-ready, onboarding-ready, contributor-ready, and maintainer-ready.

v1.0 is not a completed SaaS product, live dashboard application, autonomous QA execution engine, or live integration platform.

Generated QA artifacts are not executed test results.

Reviewed artifacts are not release approval.

Release readiness requires execution evidence and human approval.

---

## Pre-1.0 Development Summary

The pre-1.0 development phase added the main framework foundation across multiple incremental layers.

Major pre-1.0 layers included:

- Repository foundation
- Agent registry
- Prompt library
- Workflow layer
- Output templates
- Reference library
- Demo feature packs
- Integration templates
- Automation templates
- Dashboard mockups
- GitHub Actions validation
- Product packaging documentation
- Pricing documentation
- Sales one-pager
- Onboarding guide
- Contributor guide
- Maintainers guide
- Release candidate documentation

For detailed release notes, see:

- 09-docs/releases/v1.0-release-candidate.md
- 09-docs/releases/v1.0-release-notes.md
