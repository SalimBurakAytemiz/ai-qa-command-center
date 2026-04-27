# Performance Test Template

## Purpose

Use this template when preparing performance test drafts from approved performance scenarios.

Important rule:

Generated performance tests are planning or automation drafts only.

They are not executed performance results unless the performance test is actually run and execution evidence exists.

---

## 1. Automation Metadata

| Field | Value |
|---|---|
| Feature | |
| Scenario ID | |
| Test Type | Load / Stress / Spike / Soak / Frontend Performance / API Performance |
| Priority | P0 / P1 / P2 / P3 |
| Target System | Web / API / DB / Background Job / Third-Party Flow |
| Tool Candidate | k6 / JMeter / Gatling / Lighthouse / Playwright Trace |
| Source Performance Scenario | |
| Human Approval Required | If high-load, shared environment, production, or cost-impacting |

---

## 2. Preconditions

List required setup before the performance test can run.

Examples:

- Performance test environment is available.
- Environment capacity is known.
- Test data exists.
- Target endpoint or page is confirmed.
- Expected user volume is confirmed.
- Response time threshold is confirmed.
- Error rate threshold is confirmed.
- Monitoring or logs are available.

---

## 3. Environment Variables

Do not hardcode secrets.

| Variable | Purpose | Required |
|---|---|---|
| PERF_BASE_URL | Target base URL | Yes |
| API_BASE_URL | API base URL | If API test |
| PERF_TEST_USER_EMAIL | Test user email | If auth needed |
| PERF_TEST_USER_PASSWORD | Test user password | If auth needed |
| PERF_AUTH_TOKEN | Auth token | If token-based setup is used |

---

## 4. Load Profile

| Field | Value | Notes |
|---|---|---|
| Virtual Users | | Needs confirmation if unknown |
| Duration | | |
| Ramp-up | | |
| Ramp-down | | |
| Arrival Rate | | If using arrival-rate model |
| Target Throughput | | Needs confirmation if unknown |
| Environment | | QA / Staging / Performance / Production |

Do not invent load numbers.

If not provided, write Needs Confirmation.

---

## 5. Metrics and Thresholds

| Metric | Target | Source |
|---|---|---|
| P50 response time | | |
| P90 response time | | |
| P95 response time | | |
| P99 response time | | |
| Error rate | | |
| Throughput | | |
| Timeout count | | |
| CPU usage | | If available |
| Memory usage | | If available |
| DB connections | | If available |

Use Needs Confirmation if thresholds are missing.

---

## 6. Test Steps

| Step | Action | Expected Result |
|---:|---|---|
| 1 | Prepare environment | Environment ready |
| 2 | Prepare test data | Data available |
| 3 | Run performance scenario | Test executes under defined load |
| 4 | Collect metrics | Metrics captured |
| 5 | Review results | Human review completed |

---

## 7. Performance Scenario Definition

| Item | Description |
|---|---|
| User Journey | |
| Endpoint or Page | |
| Request Method | |
| Authentication Needed | Yes / No |
| Test Data Needed | |
| Expected Behavior | |
| DB Impact | |
| Third-Party Dependency | |

---

## 8. Draft k6 Script

Use this section only when code generation is requested.

Generic k6 draft structure:

import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  vus: 10,
  duration: '1m',
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500']
  }
};

export default function () {
  const baseUrl = __ENV.PERF_BASE_URL;
  const response = http.get(${baseUrl}/health);

  check(response, {
    'status is 200': (r) => r.status === 200
  });

  sleep(1);
}

Important:

- Replace placeholder VUs, duration, endpoint, and thresholds only after confirmation.
- Do not run high-load tests without human approval.

---

## 9. Draft JMeter Plan Notes

Use this section when JMeter is the selected tool.

Recommended JMeter elements:

- Thread Group
- HTTP Request
- HTTP Header Manager
- CSV Data Set Config if test users are needed
- Response Assertion
- Duration Assertion if thresholds are approved
- Summary Report
- View Results Tree only for debugging

JMeter plan should define:

| Area | Value |
|---|---|
| Thread count | Needs Confirmation |
| Ramp-up period | Needs Confirmation |
| Loop count or duration | Needs Confirmation |
| Target endpoint | |
| Assertions | |
| Report output | |

---

## 10. Risks

| Risk | Impact | Mitigation |
|---|---|---|
| Environment capacity unknown | Results may be misleading | Confirm environment specs |
| Thresholds missing | Cannot determine pass/fail | Confirm targets |
| Shared environment | May affect other teams | Get approval and schedule window |
| Production target | User impact risk | Requires explicit approval |
| Third-party dependency | External bottleneck | Mock or isolate if possible |
| Test data not realistic | Results may be invalid | Prepare realistic synthetic data |

---

## 11. Cleanup Needs

| Cleanup Item | Required | Method |
|---|---|---|
| Generated test data | Yes / No | |
| Sessions/tokens | Yes / No | |
| Logs or reports | Yes / No | Store safely |
| External side effects | Yes / No | |

---

## 12. Human Approval Points

| Item | Approval Needed | Reason |
|---|---|---|
| Production performance test | Yes | Production impact risk |
| Shared environment load test | Yes | May affect other teams |
| High-load stress test | Yes | Stability risk |
| DB-heavy performance test | Yes | DB impact risk |
| Third-party dependency load | Yes | External provider risk |
| Cost-impacting device/cloud usage | Yes | Cost control |

---

## 13. Performance Result Reporting

If execution happens, report results separately from generated plan.

Required execution evidence:

- Tool used
- Test date and time
- Environment
- Load profile
- Metrics
- Thresholds
- Raw report or summary
- Errors
- Human review decision

---

## 14. Generated vs Executed Note

This performance output is a generated automation draft.

It must not be reported as passed, verified, executed, scalable, stable, or release-ready unless the test is actually run and execution evidence exists.

---

## 15. References

- references/performance-testing/performance-test-patterns.md
- references/automation/automation-generation-patterns.md
