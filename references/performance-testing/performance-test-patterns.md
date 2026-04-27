# Performance Testing Patterns

## Purpose

This document defines practical performance testing patterns for AI QA agents.

Use this reference when creating performance-aware test strategies, API validation plans, release readiness drafts, risk analysis outputs, and automation candidate recommendations.

Important rule:

Generated performance scenarios are planning artifacts only.

They are not executed performance results unless real execution evidence exists from tools such as JMeter, k6, Gatling, Lighthouse, Playwright traces, APM tools, logs, or monitoring dashboards.

---

## 1. Performance Testing Scope

Performance testing may include:

- API response time
- Page load time
- Frontend rendering performance
- Database query performance
- Concurrent user behavior
- Load testing
- Stress testing
- Spike testing
- Soak testing
- Scalability testing
- Resource usage
- Third-party dependency performance
- Timeout behavior
- Rate limiting behavior
- Queue and background job behavior

---

## 2. Performance Test Types

| Test Type | Purpose | Example |
|---|---|---|
| Load Test | Validate expected traffic level | 500 users login over 10 minutes |
| Stress Test | Find system breaking point | Increase users until errors rise |
| Spike Test | Validate sudden traffic increase | 50 users to 1000 users in 30 seconds |
| Soak Test | Validate stability over time | 200 users for 4 hours |
| Scalability Test | Validate scaling behavior | Compare 1 instance vs 3 instances |
| Endurance Test | Detect memory leaks or degradation | Long-running API usage |
| Frontend Performance Test | Validate page speed and UX | Login page loads under expected threshold |
| DB Performance Test | Validate query/state change speed | Search query returns within target time |

---

## 3. Performance Risk Categories

| Risk Category | Description | Example |
|---|---|---|
| Slow API Response | API response exceeds expected threshold | Login API takes 5 seconds |
| Timeout Risk | Request fails due to timeout | Checkout request times out |
| High Error Rate | More errors under load | 5xx errors increase above 2 percent |
| DB Bottleneck | Query or transaction slows system | Product search query locks table |
| Frontend Slowness | User-visible page becomes slow | Dashboard takes 8 seconds to render |
| Third-Party Dependency | External service slows core flow | Payment provider latency |
| Resource Saturation | CPU, memory, DB connections, or queue overload | DB connection pool exhausted |
| Rate Limit Risk | Users hit limits unexpectedly | Login blocked after normal usage |
| Queue Backlog | Background jobs pile up | Notification queue delayed |
| Cache Risk | Cache miss causes slow response | Homepage slow after deploy |

---

## 4. Performance Priority Mapping

| Priority | Meaning | Example |
|---|---|---|
| P0 | Release-blocking performance risk | Checkout unusable under expected traffic |
| P1 | Critical performance issue | Login API consistently exceeds timeout |
| P2 | Important performance concern | Search becomes slow with large dataset |
| P3 | Low priority optimization | Minor page speed improvement |

Do not mark every performance issue as P0.

P0 requires severe user, business, release, revenue, or availability impact.

---

## 5. Performance Scenario Format

Use this format:

| ID | Scenario | Type | Priority | Preconditions | Load Profile | Expected Behavior | Metrics | Tool Candidate | Notes |
|---|---|---|---|---|---|---|---|---|---|

Example:

| ID | Scenario | Type | Priority | Preconditions | Load Profile | Expected Behavior | Metrics | Tool Candidate | Notes |
|---|---|---|---|---|---|---|---|---|---|
| PERF-LOGIN-001 | Validate login API under normal expected traffic | Load Test | P1 | Login API deployed, test users available | 200 virtual users over 10 minutes | Login response remains within accepted threshold and error rate stays low | response time, error rate, throughput | k6 / JMeter | Thresholds need confirmation |

---

## 6. Metrics To Track

Common performance metrics:

| Metric | Meaning |
|---|---|
| Average Response Time | Mean response time |
| P50 | Median response time |
| P90 | 90 percent of requests are faster than this |
| P95 | 95 percent of requests are faster than this |
| P99 | 99 percent of requests are faster than this |
| Throughput | Requests per second or transactions per minute |
| Error Rate | Percentage of failed requests |
| Timeout Count | Number of timed-out requests |
| CPU Usage | Server CPU utilization |
| Memory Usage | Server memory utilization |
| DB Connections | Database connection usage |
| Queue Length | Pending background jobs |
| Page Load Time | User-visible page load time |
| Time To Interactive | Frontend usable time |
| First Contentful Paint | Initial visible content timing |

---

## 7. Threshold Rule

Do not invent performance thresholds unless the product or engineering team provides them.

If thresholds are missing, write:

Needs Confirmation

Example:

| Metric | Target |
|---|---|
| Login API P95 response time | Needs Confirmation |
| Error rate under load | Needs Confirmation |
| Dashboard page load time | Needs Confirmation |

Better:

The login API P95 response time target must be confirmed before execution.

Bad:

Login API must always respond under 200ms.

Reason bad:

- Threshold may be unrealistic.
- No source is given.
- Environment differences are ignored.

---

## 8. API Performance Pattern

API performance validation should include:

- Endpoint
- Method
- Load profile
- Auth requirement
- Test data
- Expected response time threshold
- Error rate threshold
- Throughput expectation
- DB impact
- Third-party dependencies
- Rate limit expectations

Example:

| ID | Endpoint | Method | Type | Priority | Load Profile | Expected Behavior | Metrics |
|---|---|---|---|---|---|---|---|
| PERF-API-001 | /api/auth/login | POST | Load Test | P1 | 200 VUs, 10 minutes | Response time and error rate stay within approved threshold | P95, error rate, throughput |

---

## 9. Frontend Performance Pattern

Frontend performance validation should consider:

- Initial page load
- Asset size
- Rendering time
- Large list rendering
- Form responsiveness
- Mobile viewport performance
- Slow network behavior
- API wait state behavior
- Loading indicators

Example:

| ID | Scenario | Platform | Priority | Expected Behavior | Metrics |
|---|---|---|---|---|---|
| PERF-WEB-001 | Login page loads on mobile web | Mobile Web | P2 | Login form becomes usable within approved threshold | page load time, time to interactive |

---

## 10. Database Performance Pattern

Database performance validation should consider:

- Slow queries
- Missing indexes
- Large table scans
- Locking issues
- Transaction duration
- Duplicate request impact
- Concurrent update impact
- Pagination performance
- Search/filter performance

Example:

| ID | Scenario | Risk | Recommended Validation |
|---|---|---|
| PERF-DB-001 | Product search with large dataset | Slow query or table scan | Validate query time and index usage in safe test environment |
| PERF-DB-002 | Concurrent checkout updates | Lock contention | Validate transaction behavior under concurrency |
| PERF-DB-003 | Duplicate submit | Duplicate records or slow constraint checks | Validate idempotency and DB uniqueness behavior |

---

## 11. Load Test Pattern

Use load testing to validate expected traffic.

Example:

| Field | Example |
|---|---|
| Scenario | Login API normal load |
| Users | 200 virtual users |
| Duration | 10 minutes |
| Ramp-up | 2 minutes |
| Target | Needs Confirmation |
| Tool | k6 or JMeter |
| Metrics | P95 response time, error rate, throughput |

Good load test question:

Can the system handle expected normal usage?

---

## 12. Stress Test Pattern

Use stress testing to find breaking points.

Example:

| Field | Example |
|---|---|
| Scenario | Search API stress test |
| Users | Increase from 100 to 2000 |
| Duration | Until degradation or failure |
| Target | Identify breaking point |
| Tool | k6 or JMeter |
| Metrics | error rate, saturation, P95, P99 |

Good stress test question:

At what point does the system degrade or fail?

---

## 13. Spike Test Pattern

Use spike testing to validate sudden traffic increase.

Example:

| Field | Example |
|---|---|
| Scenario | Login after marketing campaign |
| Users | 50 to 1000 in 30 seconds |
| Duration | 5 minutes |
| Target | System remains stable |
| Metrics | error rate, response time, recovery time |

Good spike test question:

Can the system survive sudden traffic growth?

---

## 14. Soak Test Pattern

Use soak testing to detect long-term degradation.

Example:

| Field | Example |
|---|---|
| Scenario | Admin dashboard usage |
| Users | 100 concurrent users |
| Duration | 4 hours |
| Target | No memory leak, stable response time |
| Metrics | memory, CPU, response time, error rate |

Good soak test question:

Does the system degrade over time?

---

## 15. Tool Candidate Guidance

| Tool | Good For | Notes |
|---|---|---|
| JMeter | API load, complex test plans, enterprise-style performance testing | Good for structured load scenarios |
| k6 | API performance, developer-friendly scripts, CI integration | Good modern option |
| Gatling | High-performance load testing | Useful for engineering-heavy teams |
| Lighthouse | Frontend performance, accessibility, SEO checks | Good for web page analysis |
| Playwright Trace | Frontend flow timing and UI behavior | Not a full load testing tool |
| APM Tools | Real system performance monitoring | Requires instrumentation |
| Database EXPLAIN | Query performance analysis | Requires DB access and human approval |

---

## 16. Performance Reporting Format

Use this structure:

# Performance Test Plan

## 1. Scope Summary

## 2. Performance Risks

| Risk | Priority | Impact | Recommended Validation |
|---|---|---|---|

## 3. Performance Scenarios

| ID | Scenario | Type | Priority | Load Profile | Expected Behavior | Metrics | Tool Candidate |
|---|---|---|---|---|---|---|---|

## 4. Required Test Data

| Test Data | Purpose | Notes |
|---|---|---|

## 5. Environment Requirements

| Requirement | Why Needed |
|---|---|

## 6. Thresholds

| Metric | Target | Source |
|---|---|---|

## 7. Missing Information

| Missing Item | Why Needed | Impact |
|---|---|---|

## 8. Human Approval Points

| Item | Reason |
|---|---|

## 9. Reporting Notes

---

## 17. Performance Missing Information Examples

| Missing Item | Why Needed | Impact |
|---|---|---|
| Expected user volume | Needed for load profile | Cannot define realistic load |
| Response time target | Needed for pass/fail threshold | Cannot evaluate performance |
| Error rate threshold | Needed for quality gate | Cannot assess stability |
| Production-like data volume | Needed for realistic DB performance | Test may be misleading |
| Environment capacity | Needed for result interpretation | QA result may not reflect production |
| Third-party limits | Needed for dependency risk | External service may bottleneck |

---

## 18. Human Approval Required

Human approval is required for:

- Running performance tests against shared environments
- Running performance tests against production
- High-load tests that may affect other teams
- DB-heavy performance tests
- Destructive or data-generating load tests
- Tests involving payment, personal data, or customer data
- Publishing performance results externally
- Making release decisions based on performance reports

---

## 19. Generated vs Executed Rule

Correct wording:

- Performance scenario generated
- Performance test plan prepared
- Load test candidate identified
- Threshold needs confirmation
- Execution evidence required

Incorrect wording without evidence:

- Performance passed
- Load test completed
- System scales correctly
- Performance verified
- Production ready

---

## 20. Performance Quality Checklist

A good performance plan should include:

- Scenario
- Test type
- Priority
- Load profile
- Expected behavior
- Metrics
- Threshold source
- Tool candidate
- Test data needs
- Environment requirements
- Missing information
- Human approval points
- Generated vs executed distinction

A bad performance plan:

- Says "test performance" without scenario
- Has no load profile
- Has no metrics
- Invents unrealistic thresholds
- Ignores environment capacity
- Ignores DB and third-party bottlenecks
- Claims performance is verified without execution evidence
