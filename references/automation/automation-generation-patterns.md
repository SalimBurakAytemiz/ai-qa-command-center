# Automation Generation Patterns

## Purpose

This document defines practical automation generation patterns for AI QA agents.

Use this reference when selecting automation candidates, creating automation plans, reviewing generated automation code, or deciding whether a manual test case should become an automated test.

Important rule:

Generated automation code or automation plans are not executed test results.

A test is not passed, verified, or completed until it is actually executed and evidence exists.

---

## 1. Automation Candidate Decision

Use this decision model:

| Decision | Meaning |
|---|---|
| Yes | Good automation candidate |
| Later | Valuable, but not ready yet |
| No | Not suitable for automation |

---

## 2. Good Automation Candidates

A test is a good automation candidate when it is:

- Stable
- Repeatable
- Deterministic
- High regression value
- Clear expected result
- Controlled test data available
- Environment is predictable
- Selectors or API contracts are stable
- Does not require heavy human judgment
- Does not depend on unstable third-party behavior

Examples:

| Scenario | Tool Candidate | Reason |
|---|---|---|
| User login with valid credentials | Playwright / Appium | Critical regression flow |
| Protected API rejects missing token | API test | Stable auth validation |
| Guest cannot access dashboard directly | Playwright / API | Critical access-control regression |
| API rejects invalid payload | API test | Deterministic negative validation |
| DB state changes after successful create action | DB validation script | Useful consistency check |
| Smoke check for homepage availability | Playwright | Fast confidence check |

---

## 3. Bad Automation Candidates

A test is a poor automation candidate when it:

- Requires subjective human judgment
- Depends on unstable external systems
- Requires production data
- Requires destructive validation
- Has unclear expected result
- Has unstable selectors
- Has random timing
- Needs heavy visual judgment
- Has no reliable test data
- Is a one-time exploratory scenario

Examples:

| Scenario | Why Poor Candidate |
|---|---|
| Check if design "looks nice" | Subjective |
| Validate production customer account manually | Sensitive and unsafe |
| Test random third-party outage behavior | Not deterministic |
| Confirm legal text is acceptable | Human/legal judgment |
| Verify all possible devices manually through automation | Too broad and unstable |
| Run destructive DB delete in shared environment | Unsafe |

---

## 4. Later Automation Candidates

Use "Later" when automation is valuable but blocked.

Common blockers:

| Blocker | Required Fix |
|---|---|
| Test data not stable | Create synthetic fixtures |
| Selectors not stable | Add test IDs or accessible locators |
| Environment unstable | Stabilize QA environment |
| API contract not confirmed | Confirm endpoint and schema |
| Expected result unclear | Clarify acceptance criteria |
| Third-party dependency uncontrolled | Add mocks or test doubles |
| DB schema unknown | Confirm schema or entity map |

---

## 5. Tool Selection Pattern

| Test Type | Recommended Tool |
|---|---|
| Web functional regression | Playwright |
| Mobile native regression | Appium |
| API contract and behavior | API test framework / Postman / Newman |
| DB consistency validation | Python / SQL validation script |
| Performance load testing | k6 / JMeter |
| Frontend performance | Lighthouse / Playwright traces |
| Visual regression | Visual regression tool |
| Security validation | Specialized security tooling plus manual review |
| Analytics/Firebase validation | DebugView / BigQuery / event logs |

---

## 6. Smoke vs Regression

Do not put every automated test into smoke.

Smoke tests should be:

- Fast
- Critical
- Stable
- Few in number
- High confidence
- Required after deploy

Good smoke candidates:

| Scenario | Reason |
|---|---|
| App loads | Basic availability |
| User can log in | Core access |
| Critical dashboard opens | Core navigation |
| Protected route blocks guest | Security boundary |
| Health check API responds | Backend availability |

Regression tests can be broader:

- Edge cases
- Negative cases
- Role-based cases
- API validation cases
- DB consistency checks
- Mobile responsive checks
- Cross-browser checks

---

## 7. Flaky Test Risk Pattern

A flaky test gives inconsistent results.

Common flaky test causes:

| Cause | Mitigation |
|---|---|
| Fixed wait | Wait for observable condition |
| Unstable selector | Use role, label, text, or test id |
| Shared test data | Use isolated synthetic data |
| External dependency | Mock or control dependency |
| Slow environment | Use proper timeout and readiness checks |
| Race condition | Wait for API/UI state |
| Date/time dependency | Control time where possible |
| Random ordering | Sort or assert stable output |
| Parallel data conflict | Unique test data per run |

---

## 8. Automation Readiness Checklist

Before generating automation code, confirm:

| Check | Status |
|---|---|
| Expected result is clear | |
| Test data exists | |
| Environment is available | |
| Selectors or API contracts are stable | |
| Authentication setup is clear | |
| Cleanup need is known | |
| Risk of flakiness is acceptable | |
| Tool is appropriate | |
| Human approval is not required or has been granted | |

---

## 9. Playwright Automation Pattern

Use Playwright for:

- Web smoke tests
- Web regression tests
- Role-based UI flows
- Direct URL access checks
- Form validation
- Critical user journeys

Good Playwright principles:

- Prefer user-facing locators.
- Avoid fragile CSS selectors.
- Avoid fixed waits.
- Use meaningful assertions.
- Use API setup for preconditions when appropriate.
- Keep tests focused.
- Separate smoke and regression.

Example automation candidate:

| Scenario | Suite | Reason |
|---|---|---|
| Guest cannot access dashboard directly | Smoke / Security Regression | Critical access-control boundary |

---

## 10. Appium Automation Pattern

Use Appium for:

- Native iOS and Android critical flows
- Login smoke
- Navigation smoke
- Permission allow/deny flows
- Deep link routing
- Mobile regression flows

Avoid Appium for:

- Subjective visual checks
- Unstable push delivery timing
- Large device matrix without priority
- Flows requiring manual judgment

Appium readiness needs:

- Device matrix
- Stable app build
- Test users
- App identifiers
- Stable accessibility IDs
- Environment URL
- Cleanup strategy

---

## 11. API Automation Pattern

Use API automation for:

- Authentication checks
- Authorization checks
- Request validation
- Response validation
- Contract checks
- Error handling
- State-changing API checks
- Regression validation

Good API automation candidate:

| Scenario | Reason |
|---|---|
| Protected endpoint rejects missing token | Stable and critical |
| Wrong role receives 403 | Permission boundary |
| Invalid payload returns validation error | Deterministic |
| Create action returns expected schema | Contract validation |

Avoid API automation when:

- Endpoint is not confirmed
- Status codes are unknown
- Test data is not available
- API has unstable third-party dependency
- Running the test changes shared data unsafely

---

## 12. DB Validation Automation Pattern

Use DB validation automation for:

- API-DB consistency
- UI-DB consistency
- Insert/update/soft delete validation
- Ownership checks
- Duplicate record checks
- Audit/timestamp checks

DB automation requires:

- Safe test environment
- Synthetic test data
- Read-only access where possible
- Human approval for risky operations
- Known schema
- Cleanup strategy

Do not automate destructive DB validation in shared or production environments.

---

## 13. Performance Automation Pattern

Use performance automation for:

- API load tests
- Smoke-level performance checks
- Regression performance baselines
- Stress/spike/soak scenarios when approved

Performance automation requires:

- Load profile
- Target thresholds
- Environment approval
- Test data
- Tool selection
- Human approval for high-load tests

Do not run load tests against production or shared environments without explicit approval.

---

## 14. Automation Plan Format

Use this structure:

# Automation Plan

## 1. Scope Summary

## 2. Automation Candidates

| Scenario ID | Title | Priority | Tool Candidate | Decision | Reason |
|---|---|---|---|---|---|

## 3. Not Recommended For Automation

| Scenario ID | Reason |
|---|---|

## 4. Later Automation Candidates

| Scenario ID | Blocker | Required Fix |
|---|---|---|

## 5. Smoke Suite Candidates

| Scenario ID | Reason |
|---|---|

## 6. Regression Suite Candidates

| Scenario ID | Reason |
|---|---|

## 7. Test Data Requirements

| Data | Purpose | Setup Method | Cleanup Needed |
|---|---|---|---|

## 8. Environment Requirements

| Requirement | Why Needed |
|---|---|

## 9. Flakiness Risks

| Risk | Impact | Mitigation |
|---|---|---|

## 10. Human Approval Points

| Item | Reason |
|---|---|

## 11. Generated vs Executed Note

---

## 15. Generated vs Executed Rule

Correct wording:

- Automation candidate identified
- Automation plan generated
- Playwright test draft prepared
- API automation draft prepared
- Execution evidence required

Incorrect wording without execution evidence:

- Automation passed
- Test executed successfully
- Regression passed
- Playwright verified the flow
- CI confirmed quality

---

## 16. Human Approval Required

Human approval is required for:

- Running tests against production
- Running high-load performance tests
- Running destructive DB checks
- Creating external tickets
- Using production data
- Publishing automation results
- Release readiness decisions
- Security-sensitive automation

---

## 17. Automation Quality Checklist

A good automation recommendation should include:

- Scenario ID
- Priority
- Tool candidate
- Decision: Yes, No, or Later
- Reason
- Test data requirement
- Environment requirement
- Flakiness risk
- Cleanup need
- Human approval need
- Generated vs executed distinction

A bad automation recommendation:

- Says automate everything
- Ignores flaky risk
- Ignores test data
- Ignores environment stability
- Ignores selector stability
- Ignores human approval
- Claims execution without evidence
