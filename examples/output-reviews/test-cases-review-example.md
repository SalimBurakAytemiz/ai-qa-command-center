# Test Cases Review Example

## Purpose

This document shows an example review of generated test cases.

Important rule:

This is a review example only. It is not an executed test result.

---

## 1. Reviewed Output

| Field | Value |
|---|---|
| Output Type | Test Cases |
| Source Agent | Happy Path / Edge Case / Negative Case Agents |
| Feature | User Login |
| Review Agent | Output Reviewer Agent |
| Review Status | Needs Minor Revision |

---

## 2. Quality Score

| Dimension | Score | Notes |
|---|---:|---|
| Completeness | 8/10 | Happy, edge, negative, permission cases included |
| Clarity | 8/10 | Cases are readable |
| Risk Coverage | 9/10 | Direct access and disabled user risks included |
| Actionability | 8/10 | Steps and expected results are usable |
| Format Compliance | 9/10 | Table format is consistent |
| Traceability | 7/10 | Some cases need stronger AC mapping |
| Automation Candidate Quality | 8/10 | Most automation decisions are realistic |
| Safety Awareness | 9/10 | No execution claim |

Overall Score: 8.2 / 10

---

## 3. Positive Findings

- Happy path and negative cases are separated.
- Permission and session cases are included.
- P0 direct dashboard access case is included.
- Automation candidate decisions are present.
- Expected results are mostly observable.

---

## 4. Issues Found

| Issue | Severity | Recommended Fix |
|---|---|---|
| Some expected results are generic | Medium | Make expected results more observable |
| Some automation candidates marked Yes may need stable test data | Medium | Change to Later where setup is not ready |
| AC coverage missing for a few negative cases | Low | Add AC or risk mapping |

---

## 5. Example Required Revision

Before:

Expected Result: Login fails.

After:

Expected Result: User remains on the login page and a generic invalid credentials message is displayed without revealing whether the email exists.

---

## 6. Human Approval Required

| Item | Reason |
|---|---|
| P0 direct URL access case | Security boundary |
| Automation execution | Requires environment and test data |
| External bug/ticket creation | Human approval required |

---

## 7. Review Decision

Decision: Needs Minor Revision

Reason:

The test cases are strong, but a few expected results and automation candidate decisions need tightening before official use.

---

## 8. Safety Note

These reviewed test cases are still generated planning artifacts.

They are not passed or executed tests.
