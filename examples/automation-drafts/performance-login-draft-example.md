# Performance Login Draft Example

## Purpose

This document shows an example performance automation draft for the login feature.

Important rule:

This is not an executed performance result.

It is a generated performance draft example only.

---

## 1. Automation Metadata

| Field | Value |
|---|---|
| Feature | User Login |
| Scenario ID | PERF-LOGIN-001 |
| Test Type | API Load Test |
| Priority | P2 |
| Target System | Login API |
| Tool Candidate | k6 |
| Human Approval Required | Yes for shared, high-load, or production environments |

---

## 2. Preconditions

- Performance-safe environment is available.
- Expected user volume is confirmed.
- Login endpoint is confirmed.
- Synthetic users are available.
- Rate limits are understood.
- Monitoring/logs are available.
- Thresholds are confirmed.

---

## 3. Draft k6 Script

~~~javascript
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
  const email = __ENV.PERF_TEST_USER_EMAIL;
  const password = __ENV.PERF_TEST_USER_PASSWORD;

  if (!baseUrl || !email || !password) {
    throw new Error('Missing required environment variables.');
  }

  const response = http.post(
    `${baseUrl}/api/auth/login`,
    JSON.stringify({
      email,
      password
    }),
    {
      headers: {
        'Content-Type': 'application/json'
      }
    }
  );

  check(response, {
    'status is 200': (r) => r.status === 200
  });

  sleep(1);
}
~~~

---

## 4. Risks

| Risk | Impact | Mitigation |
|---|---|---|
| Load profile unknown | Results may be meaningless | Confirm expected traffic |
| Thresholds invented | False pass/fail | Confirm targets |
| Shared environment impact | Other teams may be affected | Human approval and schedule window |
| Login rate limits | False errors | Use approved test profile |

---

## 5. Generated vs Executed Note

This performance output is a generated automation draft example.

It must not be reported as passed, verified, executed, scalable, stable, or release-ready unless the test is actually run and execution evidence exists.
