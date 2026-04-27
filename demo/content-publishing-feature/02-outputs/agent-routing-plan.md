# Content Publishing Agent Routing Plan

## 1. Routing Summary

The content publishing feature affects CMS UI, public web visibility, API authorization, backend workflow logic, database state transitions, audit/timestamp behavior, and reporting.

Phase 1 agents are required for this demo.

---

## 2. Required Agents

| Order | Agent | Required | Reason | Expected Output |
|---:|---|---|---|---|
| 1 | Product Intake Agent | Yes | Convert feature input into testing context | Product Testing Context |
| 2 | Test Strategy Agent | Yes | Define risk-based test strategy | Test Strategy |
| 3 | Task Router Agent | Yes | Select relevant agents | Agent Routing Plan |
| 4 | Token Controller Agent | Yes | Prepare compact context | Compact context per agent |
| 5 | Test Planning Agent | Yes | Create test plan | Test Plan |
| 6 | Happy Path Test Case Agent | Yes | Generate draft/publish success flows | Happy path cases |
| 7 | Edge Case and Negative Case Agent | Yes | Generate invalid/permission/state cases | Edge/negative cases |
| 8 | Web Functional Test Agent | Yes | Validate CMS and public web behavior | Web/CMS scenarios |
| 9 | API Test Agent | Yes | Validate CMS/public content APIs | API validation plan |
| 10 | Database Validation Agent | Yes | Validate state transitions and no-change behavior | DB validation plan |
| 11 | Jira/Trello Work Tracking Agent | Yes | Create draft work items | Jira/Trello drafts |
| 12 | Daily Quality Report Agent | Yes | Summarize generated package | Daily quality report |
| 13 | Output Reviewer Agent | Yes | Review critical outputs | Review report |

---

## 3. Agents Not Required For This Demo

| Agent Area | Reason |
|---|---|
| Native Mobile Appium Agent | Native mobile is out of scope |
| Firebase Event Agent | No analytics events defined in input |
| Notification Agent | No push/email notification behavior in scope |
| Performance Agent | Performance is not required for this demo |
| Visual Regression Agent | Pixel-perfect design validation is not in scope |

---

## 4. Compact Context Routing

| Target Agent | Include | Exclude |
|---|---|---|
| Happy Path Test Case Agent | Draft creation, admin publish, public visibility | Full DB schema details |
| Edge Case and Negative Case Agent | Missing fields, duplicate slug, draft privacy, wrong role | Reporting format details |
| Web Functional Test Agent | CMS UI notes, public visibility, loading/error states | DB implementation details |
| API Test Agent | API notes, auth rules, content state behavior | Full UI layout details |
| Database Validation Agent | DB notes, status transitions, no-change risks | CSS/UI layout details |
| Reporting Agent | Risks, blockers, generated outputs, missing info | Raw full context |

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
| P0 CMS access-control risk | Security boundary |
| P0 publish API authorization risk | Security boundary |
| Jira/Trello ticket creation | External action requires approval |
| DB validation execution | Safe environment and schema required |
| Release readiness | Execution not performed |

---

## 7. Routing Decision

Approved for Phase 1 demo generation.

Output review is required before using generated outputs as official QA artifacts.
