# Demo API Test Run Evidence Example

## 1. Purpose

This document shows an example execution evidence record for the demo API test workflow.

It demonstrates how test execution evidence should be documented after a real run.

This is a sample evidence file.

Do not treat this file as proof that a specific external product, customer system, or production environment was tested.

---

## 2. Evidence Metadata

| Field | Value |
|---|---|
| Feature | Demo Login API |
| Test Area | API contract, API behavior, DB validation |
| Test Case ID | DEMO-API-SMOKE-001 |
| Execution Type | Automated API / AJV Contract / DB Validation |
| Executor | GitHub Actions / Local Runner |
| Execution Date | Sample |
| Environment | Local demo app / GitHub Actions demo environment |
| Build / Version | v1.4 candidate |
| Evidence Status | Example |
| Reviewer | Human reviewer required for real release decisions |
| Review Date | Not applicable for sample |

---

## 3. Execution Summary

The demo API test run validates the local FastAPI demo application.

The run covers:

- Demo app health check
- Python API login smoke test
- AJV API contract validation
- DB validation for disabled user sessions

The run does not cover:

- Production API validation
- Real customer account validation
- Payment or financial flows
- Security verification
- Load testing
- Release approval

---

## 4. Preconditions

| Preconditions | Status | Notes |
|---|---|---|
| Demo app dependencies installed | Confirmed | Installed from demo-app/requirements.txt |
| Demo database seeded | Confirmed | Seeded with synthetic users |
| Demo app started | Confirmed | Started with Uvicorn |
| Health endpoint reachable | Confirmed | /health returned success |
| Python API dependencies installed | Confirmed | Installed from 06-tests/api/requirements.txt |
| AJV dependencies installed | Confirmed | Installed from 06-tests/api-ajv/package.json |
| Production credentials used | Not Applicable | Demo uses synthetic data only |

---

## 5. Execution Steps and Results

| Step | Action | Expected Result | Actual Result | Status | Evidence Link / Notes |
|---:|---|---|---|---|---|
| 1 | Seed demo database | Synthetic active and disabled users created | Database seeded | Passed | Demo seed script |
| 2 | Start demo app | API starts on 127.0.0.1:3000 | API started | Passed | Demo app logs |
| 3 | Call /health | Health response returns success | Success response received | Passed | Workflow log |
| 4 | Run Python API test | Login endpoint accepts valid synthetic credentials | API test passed | Passed | JUnit artifact |
| 5 | Run AJV contract test | Response matches strict schema and regex patterns | Contract test passed | Passed | Node test output |
| 6 | Run DB validation | Disabled user has no active sessions | DB validation passed | Passed | DB validation output |

---

## 6. Evidence Attachments

| Evidence Type | Location / Link | Notes |
|---|---|---|
| GitHub Actions run | Demo API Tests workflow | Use the actual run URL when documenting a real execution |
| Python API JUnit report | test-results/python-api-results.xml | Uploaded as workflow artifact |
| Demo app stdout log | test-results/demo-app/demo-app.stdout.log | Uploaded as workflow artifact |
| Demo app stderr log | test-results/demo-app/demo-app.stderr.log | Uploaded as workflow artifact |
| AJV test output | Workflow log | Node test output |
| DB validation output | Workflow log | Python script output |

---

## 7. Defects Found

No confirmed defects were found during this sample execution.

Do not convert sample evidence into production claims.

---

## 8. Result Summary

| Result Type | Count |
|---|---:|
| Passed | 6 |
| Failed | 0 |
| Blocked | 0 |
| Not Run | 0 |

Overall execution result:

- Passed for local demo scope only

---

## 9. Release Impact

This evidence supports only the local demo API workflow.

It does not prove customer system quality, production readiness, security verification, performance verification, mobile verification, or release readiness.

Release readiness still requires real project-specific execution evidence and human approval.

---

## 10. Final Evidence Note

This file is an example evidence record.

For real execution evidence, replace sample values with the actual run date, GitHub Actions run URL, commit SHA, environment, artifact links, test results, and reviewer notes.
