# Risk Analysis Patterns

## Purpose

This document defines practical risk analysis patterns for AI QA agents.

Use this reference when creating test strategies, risk matrices, release summaries, daily reports, output reviews, and executive summaries.

Important rule:

Risk analysis is not execution evidence.

A generated risk analysis identifies possible risks. It does not prove that a defect exists unless supported by execution evidence.

---

## 1. Risk Categories

Common QA risk categories:

| Risk Category | Description | Example |
|---|---|---|
| Business Risk | Risk that affects business goals or revenue | Users cannot complete checkout |
| User Impact Risk | Risk that affects user experience or access | Registered users cannot log in |
| Security Risk | Risk involving unauthorized access or sensitive data | Guest can access protected dashboard |
| Data Integrity Risk | Risk involving incorrect, missing, duplicated, or corrupted data | Duplicate orders created |
| Permission Risk | Risk involving wrong role or access behavior | Normal user can access admin page |
| API Contract Risk | Risk involving endpoint, schema, status, or response mismatch | Frontend expects fullName but API returns name |
| Database State Risk | Risk involving wrong persistence or state transitions | Disabled user receives active session |
| Environment Risk | Risk caused by unstable or unavailable test environment | API not deployed to QA |
| Regression Risk | Risk that existing behavior breaks | Existing login flow breaks after auth change |
| Release Risk | Risk that affects release decision | P0 blocker unresolved before release |

---

## 2. Priority Mapping

Use this priority mapping:

| Priority | Meaning | When To Use |
|---|---|---|
| P0 | Release blocker | Severe security, data, access, payment, or core flow failure |
| P1 | Critical | Major feature failure or high-impact risk |
| P2 | Important | Medium impact, important but not release-blocking |
| P3 | Low | Minor issue, cosmetic, low business impact |

Do not mark every risk as P0 or P1.

P0 must be justified.

---

## 3. P0 Risk Pattern

Use P0 only when the risk can block release or cause severe damage.

Good P0 examples:

| Risk | Reason |
|---|---|
| Guest user can access protected dashboard | Unauthorized access |
| Payment succeeds but order is not created | Revenue and data integrity risk |
| User can see another user's personal data | Privacy and security risk |
| Admin permission is granted to normal user | Severe authorization risk |
| Production migration may delete customer data | Data loss risk |

Bad P0 examples:

| Risk | Why Bad |
|---|---|
| Button color is slightly wrong | Not release blocking |
| Error text has minor typo | Usually P3 |
| Loading spinner is missing | Usually P2 or P3 unless it causes duplicate critical action |

---

## 4. Risk Statement Format

Good risk statement format:

Risk:
If [condition] happens, then [impact] may occur because [reason].

Example:

If a guest user can directly access the dashboard URL, unauthorized users may view protected data because route-level authentication is missing or broken.

Bad risk statement:

Login risk exists.

Why bad:

- Too vague
- No condition
- No impact
- No reason
- Not actionable

---

## 5. Risk Matrix Format

Use this structure:

| ID | Risk | Category | Probability | Impact | Priority | Evidence / Source | Mitigation | Human Approval Needed |
|---|---|---|---|---|---|---|---|---|
| RISK-001 | Guest can access dashboard directly | Security | Medium | Critical | P0 | Requirement / planned validation | Direct URL permission test | Yes |

Probability values:

- Low
- Medium
- High
- Unknown

Impact values:

- Low
- Medium
- High
- Critical

---

## 6. Risk Mitigation Pattern

Every important risk should have a mitigation.

Good mitigation examples:

| Risk | Mitigation |
|---|---|
| API status codes unknown | Confirm API contract with backend owner |
| DB schema unknown | Request schema or entity map |
| Unauthorized access possible | Add direct URL and API permission tests |
| Duplicate submit risk | Add duplicate request and DB duplicate checks |
| Missing test users | Create synthetic test users before execution |

Bad mitigation:

Investigate later.

Why bad:

- No owner
- No action
- No clear next step

---

## 7. Risk Evidence Levels

Use this evidence model:

| Evidence Level | Meaning |
|---|---|
| Assumption | Risk is possible but not confirmed |
| Requirement-Based | Risk comes from requirement or missing requirement |
| Design-Based | Risk comes from design or flow review |
| API-Based | Risk comes from API spec or API behavior |
| DB-Based | Risk comes from schema or DB behavior |
| Execution-Based | Risk is supported by actual test execution evidence |
| Production-Based | Risk is supported by production observation |

Generated AI analysis usually starts as:

- Assumption
- Requirement-Based
- Design-Based

Do not present it as execution-based unless actual execution occurred.

---

## 8. Missing Information Risk Pattern

When information is missing, treat it as a risk.

Examples:

| Missing Information | Risk | Recommended Action |
|---|---|---|
| API status codes unknown | API expected results may be wrong | Request API contract |
| DB schema unknown | DB validation cannot be precise | Request schema |
| Role matrix unknown | Permission tests may miss gaps | Request access matrix |
| Dashboard route unknown | Redirect validation remains generic | Request route definitions |
| Error copy unknown | UI assertion may be vague | Request copy or UX spec |

---

## 9. Release Risk Pattern

Release risk should be used when a risk affects release decision.

Examples:

| Risk | Release Impact |
|---|---|
| P0 security issue open | Release should not proceed without approval |
| Critical API unavailable | Execution blocked |
| No test environment | QA cannot validate |
| Missing test data for core flow | Core flow cannot be tested |
| Payment or order DB mismatch | Release may cause business loss |

---

## 10. Risk Analysis Quality Checklist

A good risk analysis should include:

- Clear risk description
- Risk category
- Impact
- Probability
- Priority
- Evidence level
- Mitigation
- Owner or recommended owner
- Human approval need
- Missing information
- Generated vs executed distinction

A bad risk analysis:

- Lists vague risks
- Marks everything P0
- Has no mitigation
- Has no evidence level
- Confuses assumptions with confirmed defects
- Claims release readiness without execution
