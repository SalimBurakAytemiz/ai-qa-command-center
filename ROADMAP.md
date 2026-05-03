# AI QA Command Center Roadmap

This roadmap separates completed framework releases from future implementation work.

---

## Current Release

Current release:

- v1.4.0 Demo App, Docker Support, CI Test Execution, and Evidence Example

Current status:

- Demo-ready
- Validation-backed
- CI-enabled
- Product-packaging-ready
- Pricing-documentation-ready
- Sales-one-pager-ready
- Onboarding-ready
- Contributor-ready
- Maintainer-ready
- Runnable test skeleton available
- AJV API contract testing available
- FastAPI + SQLite demo app available
- Docker Compose support available
- Demo API test runner scripts available
- Demo API Tests workflow available
- CI artifact upload available
- Execution evidence example available
- Two GitHub workflows passing on latest main

---

## v1.4 Completed Scope

v1.4 includes:

- FastAPI demo app backend
- SQLite demo database
- Demo seed script
- Demo health endpoint
- Demo login endpoint
- Dockerfile for demo app
- Root Docker Compose file
- `.dockerignore`
- Local run scripts for demo app
- Demo API test runner scripts
- GitHub Actions Demo API Tests workflow
- Python API test execution in CI
- AJV API contract test execution in CI
- DB validation execution in CI
- Demo app logs uploaded as artifacts
- Python API JUnit report uploaded as artifact
- Demo API execution evidence example
- Validation coverage for all new v1.4 assets

---

## v1.3 Completed Scope

v1.3 includes:

- `06-tests/README.md`
- Playwright runnable skeleton
- API pytest runnable skeleton
- DB validation runnable skeleton
- k6 performance smoke skeleton
- AJV API contract test skeleton
- AJV request schema example
- AJV response schema example
- AJV contract assertion helpers
- AJV contract testing pattern documentation

---

## v1.2 Completed Scope

v1.2 includes:

- `09-docs/README.md` documentation index
- `09-docs/agent-coverage-matrix.md` agent coverage matrix
- Validation coverage for documentation index
- Validation coverage for agent coverage matrix

---

## v1.1 Completed Scope

v1.1 includes:

- P0 technical hygiene cleanup
- Clean validation scripts
- GitHub community files
- Execution evidence template
- Design/UI specialist prompts
- DIT specialist prompts

---

## v1.0 Completed Scope

v1.0 includes:

- Structured AI QA team architecture
- Agent registry
- Prompt library
- Workflow documentation
- Output templates
- Demo feature packs
- Product packaging documentation
- Validation scripts
- GitHub Actions CI

---

## What The Framework Still Does Not Include

The framework does not yet include:

- A completed SaaS product
- A production dashboard application
- User authentication for SaaS users
- Workspace/project persistence
- Async job queue
- Worker execution service
- Artifact storage service
- Billing/subscription layer
- Live external integrations
- Full Appium APK/AAB execution
- Socket/WebSocket test layer
- Full SaaS deployment infrastructure
- Production-grade security hardening

---

## Suggested v1.5 Scope

Recommended v1.5 direction:

- Add target configuration system.
- Add `target-config.example.yaml`.
- Add target config JSON Schema.
- Add target config validator.
- Add docs explaining how users provide domain, API, DB, socket, APK, and AAB information.
- Keep secrets out of committed config files.

---

## Suggested v1.6 Scope

Recommended v1.6 direction:

- Add WebSocket/socket test skeleton.
- Add socket message schema examples.
- Add socket validation docs.
- Add socket test workflow or local runner.

---

## Suggested v1.7 Scope

Recommended v1.7 direction:

- Add Appium Android APK test skeleton.
- Add Appium config.
- Add Android capability examples.
- Add mobile test data/config docs.
- Keep real APK/AAB files out of git unless they are safe sample artifacts.

---

## Suggested v1.8 Scope

Recommended v1.8 direction:

- Add orchestrator CLI.
- Add test selection logic from target config.
- Add evidence collector.
- Add report generator.

---

## Suggested v2.0 Local MVP

v2.0 should target:

- Clone repository
- Configure target
- Run selected test layers
- Collect artifacts
- Generate evidence
- Generate summary report

---

## SaaS Direction

After local MVP, SaaS work should add:

- Backend API
- Frontend dashboard
- Auth
- Workspace/project model
- Database persistence
- Job queue
- Worker execution service
- Artifact storage
- Billing
- Monitoring
- Deployment

---

## Core Safety Rule

AI may generate, organize, review, and recommend.

Humans approve, execute, verify, and decide.

Generated QA artifacts are not executed test results.

Reviewed artifacts are not release approval.

Release readiness requires execution evidence and human approval.
