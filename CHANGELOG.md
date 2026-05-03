# Changelog

All notable changes to AI QA Command Center are documented here.

---

## [1.4.0] - Demo App, Docker Support, CI Test Execution, and Evidence Example

### Added

- Added runnable FastAPI + SQLite demo app backend.
- Added demo app seed script.
- Added demo app Dockerfile.
- Added root `docker-compose.yml`.
- Added `.dockerignore`.
- Added local demo app run scripts.
- Added demo API test runner scripts.
- Added GitHub Actions Demo API Tests workflow.
- Added workflow artifact upload for demo API test outputs.
- Added demo API execution evidence example.
- Added validation coverage for demo app backend.
- Added validation coverage for Docker support.
- Added validation coverage for demo API test runner scripts.
- Added validation coverage for demo API workflow.
- Added validation coverage for demo API evidence example.

### Fixed

- Fixed demo app dependency requirements for Pydantic `EmailStr`.
- Fixed local Windows script execution compatibility by using `python -m pip`.
- Fixed local Windows pytest execution compatibility by using `python -m pytest`.
- Fixed PowerShell npm execution compatibility by using `npm.cmd`.
- Fixed AJV draft 2020-12 schema support with `Ajv2020`.
- Fixed Demo API workflow database path handling.
- Fixed local demo API runner health check binding by using `127.0.0.1`.

### Validation

- Repository validation workflow passes.
- Demo API Tests workflow passes.
- Demo API test artifacts are uploaded by GitHub Actions.
- Python API smoke test executes against the demo app.
- AJV API contract test executes against the demo app.
- DB validation executes against the demo database.

### Notes

v1.4 is the first release where the repository contains a real runnable demo app and a real CI-executed demo API test workflow.

This still does not make the framework a SaaS product.

It is now a stronger local/CI execution seed for the future SaaS platform.

---

## [1.3.0] - Runnable Test Skeleton and AJV API Contract Testing

### Added

- Added runnable test skeleton under `06-tests/`.
- Added Playwright web test skeleton.
- Added API pytest skeleton.
- Added DB validation skeleton.
- Added k6 performance smoke skeleton.
- Added AJV API contract test skeleton.
- Added AJV JSON schema examples for request and response validation.
- Added AJV contract testing pattern documentation.
- Added validation coverage for runnable test skeleton assets.
- Added validation coverage for AJV API contract test assets.
- Added validation coverage for AJV contract testing patterns.

### Changed

- Improved the repository from documentation-only examples toward runnable testing infrastructure.
- Established AJV + JSON Schema as the preferred strict API contract testing pattern.
- Clarified that status-code-only API tests are not enough for serious API validation.

### Notes

v1.3 introduced the first runnable testing infrastructure layer.

These tests were skeletons and required a real target application or configured environment variables to execute meaningful validations.

---

## [1.2.0] - Documentation Index and Agent Coverage Matrix

### Added

- Added documentation index at `09-docs/README.md`.
- Added agent coverage matrix at `09-docs/agent-coverage-matrix.md`.
- Added validation coverage for the documentation index and agent coverage matrix.

---

## [1.1.0] - Repository Hygiene, Evidence, Design/UI, and DIT Expansion

### Added

- Added `.gitattributes` for line ending normalization.
- Added `SECURITY.md`.
- Added GitHub pull request template.
- Added GitHub issue templates.
- Added GitHub CODEOWNERS.
- Added execution evidence template.
- Added Design/UI specialist prompts.
- Added DIT specialist prompts.

---

## [1.0.0] - Stable Framework Release

### Added

- Added v1.0 release candidate documentation.
- Added v1.0 release notes.
- Finalized the first stable AI QA Command Center framework release.

### Notes

v1.0 was the first stable framework release.

Generated QA artifacts are not executed test results.

Reviewed artifacts are not release approval.

Release readiness requires execution evidence and human approval.
