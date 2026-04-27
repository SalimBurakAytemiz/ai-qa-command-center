# Login Feature Agent Routing Plan

## 1. Routing Summary

The login feature affects web UI, mobile web, admin redirection, API authentication, backend session/token logic, database state, and reporting.

Only Phase 1 agents are required for this demo.

---

## 2. Required Agents

| Order | Agent | Required | Reason | Expected Output |
|---:|---|---|---|---|
| 1 | Product Intake Agent | Yes | Convert feature input into testing context | Product Testing Context |
| 2 | Test Strategy Agent | Yes | Define risk-based test strategy | Test Strategy |
| 3 | Task Router Agent | Yes | Select relevant agents | Agent Routing Plan |
| 4 | Token Controller Agent | Yes | Prepare compact context | Compact context per agent |
| 5 | Test Planning Agent | Yes | Create test plan | Test Plan |
| 6 | Happy Path Test Case Agent | Yes | Generate successful login flows | Happy path cases |
| 7 | Edge Case and Negative Case Agent | Yes | Generate invalid and boundary cases | Edge/negative cases |
| 8 | Web Functional Test Agent | Yes | Validate visible login behavior | Web validation scenarios |
| 9 | API Test Agent | Yes | Validate auth API behavior | API validation plan |
| 10 | Database Validation Agent | Yes | Validate DB state impact | DB validation plan |
| 11 | Jira/Trello Work Tracking Agent | Yes | Create draft work items | Jira/Trello drafts |
| 12 | Daily Quality Report Agent | Yes | Summarize generated package | Daily quality report |
| 13 | Output Reviewer Agent | Yes | Review critical outputs | Review report |

---

## 3. Agents Not Required For This Demo

| Agent Area | Reason |
|---|---|
| Native Mobile Appium Agent | Native app is not in scope |
| Firebase Event Agent | No analytics events defined |
| Notification Agent | No notification behavior in scope |
| Performance Agent | Performance is not required for login demo |
| Security Deep Review Agent | Only basic auth/security risk notes are needed |
| Visual Regression Agent | Pixel-perfect validation is not in scope |

---

## 4. Compact Context Routing

| Target Agent | Include | Exclude |
|---|---|---|
| Happy Path Test Case Agent | Valid login flow, roles, platforms, AC-LOGIN-001/002/008 | DB schema details |
| Edge Case and Negative Case Agent | Invalid credentials, disabled user, empty fields, direct access | Detailed reporting format |
| Web Functional Test Agent | UI notes, loading/error states, responsive behavior | DB implementation details |
| API Test Agent | API notes, auth rules, error response expectations | Full UI copy unless needed |
| Database Validation Agent | DB notes, session/token impact, user status | CSS/UI layout details |
| Reporting Agent | Reviewed summary, risks, blockers, missing info | Raw full context |

---

## 5. Model Routing Recommendation

| Task Type | Recommended Profile |
|---|---|
| Strategy and routing | orchestration_and_strategy |
| Test case generation | bulk_test_generation |
| API validation | api_and_backend_analysis |
| DB validation | database_validation |
| Reporting | reporting_and_summaries |
| Review | output_review_and_quality |

---

## 6. Human Approval Points

| Point | Reason |
|---|---|
| P0 access-control risk | Security boundary |
| Release readiness | Execution not performed |
| Jira/Trello ticket creation | External action requires approval |
| Exact API expected statuses | Requirements need confirmation |

---

## 7. Routing Decision

Approved for Phase 1 demo generation.

Output review is required before using generated outputs as official QA artifacts.
