# Dashboard Operator Workflow

## 1. Purpose

This document defines how a future human test leader or QA operator should use the AI QA Command Center dashboard.

The dashboard is not implemented yet.

This document describes the intended operator workflow, safety rules, review flow, approval gates, and generated-vs-executed boundaries.

---

## 2. Operator Role

The primary dashboard operator is the Human Test Leader.

The operator is responsible for:

- Reviewing feature input
- Confirming selected agents
- Reviewing generated output packages
- Checking missing information
- Checking risks and blockers
- Managing human approval gates
- Deciding whether outputs need revision
- Deciding whether execution may start
- Preventing generated artifacts from being reported as executed results
- Preventing unsafe external actions

---

## 3. Core Dashboard Principle

The dashboard must preserve this rule:

AI may generate, organize, review, and recommend.

Humans approve, execute, verify, and decide.

The dashboard must clearly separate:

- Generated planning artifacts
- Reviewed artifacts
- Executed evidence
- Approved decisions

---

## 4. High-Level Workflow

Recommended operator workflow:

1. Select project or feature.
2. Review feature intake.
3. Check missing information.
4. Review agent routing plan.
5. Review generated output package.
6. Review quality score and output review notes.
7. Review risks and blockers.
8. Review human approval queue.
9. Decide next action.
10. Approve, request revision, block, or move to execution planning.

---

## 5. Workflow Statuses

| Status | Meaning | Operator Action |
|---|---|---|
| Draft | Feature input exists but is incomplete | Complete or request missing information |
| Ready for Routing | Input is sufficient for agent selection | Review routing plan |
| Routing Generated | Agents were selected or skipped | Confirm routing |
| Outputs Generated | QA artifacts were generated | Start output review |
| Needs Review | Human review is required | Review quality, risks, blockers |
| Needs Revision | Output must be revised | Send back for revision |
| Blocked | Missing critical information or approval | Resolve blocker |
| Approved for Planning Use | Output can be used as planning artifact | Continue to execution planning |
| Execution Ready | Execution prerequisites are met | Human approval required |
| Executed | Real execution evidence exists | Review evidence |
| Release Decision Required | Human release decision needed | Escalate to test leader/product owner |

---

## 6. Feature Intake Workflow

The operator should review:

- Feature name
- Feature summary
- Business purpose
- Affected platforms
- User roles
- Acceptance criteria
- API notes
- DB notes
- UI notes
- Known risks
- Missing information
- Human notes

The dashboard should warn when:

- Feature summary is empty
- No platform is selected
- No user role is defined
- Acceptance criteria are missing
- API is selected but API notes are missing
- Database impact exists but DB notes are missing
- Security-sensitive data appears in input
- Production credentials or secrets appear in input

---

## 7. Agent Routing Workflow

The operator should inspect:

- Selected agents
- Skipped agents
- Optional agents
- Blocked agents
- Reason for each routing decision
- Context package per agent
- Model profile recommendation
- Human approval requirements

Routing should not run all agents by default.

Agents should be selected based on:

- Feature scope
- Affected platforms
- Risk level
- API impact
- DB impact
- UI impact
- Security impact
- Reporting needs
- Release readiness needs

---

## 8. Output Package Workflow

The dashboard should group generated outputs into an output package.

Example package:

| Output | Status | Notes |
|---|---|---|
| Product Testing Context | Generated | Planning artifact |
| Test Strategy | Generated | Requires review |
| Agent Routing Plan | Generated | Requires review |
| Test Plan | Generated | Requires review |
| Happy Path Test Cases | Generated | Not executed |
| Edge and Negative Test Cases | Generated | Not executed |
| API Validation Plan | Generated | Not executed |
| DB Validation Plan | Generated | Not executed |
| Jira/Trello Drafts | Drafted | External approval required |
| Daily Quality Report | Generated | Planning summary |
| Executive Summary | Drafted | Human approval required |
| Release Readiness Report | Drafted | Not release approval |

The dashboard must not label generated outputs as passed, verified, or executed.

---

## 9. Output Review Workflow

The operator should review generated outputs using these dimensions:

- Completeness
- Clarity
- Risk coverage
- Actionability
- Traceability
- Format compliance
- Missing information handling
- Unsupported assumption handling
- Human approval awareness
- Generated vs executed safety

Possible review decisions:

| Decision | Meaning |
|---|---|
| Approved | Output can be used as planning artifact |
| Approved with Minor Notes | Output is usable but has small caveats |
| Needs Minor Revision | Small fixes required |
| Needs Revision | Output should not be used until revised |
| Rejected | Output is unsafe or not useful |
| Human Approval Required | Operator decision required before use |

---

## 10. Risk and Blocker Workflow

The dashboard should show:

- P0 risks
- P1 risks
- P2/P3 risks
- Missing information
- Blockers
- Owner needed
- Required action
- Approval required

Example:

| Item | Priority | Type | Required Action |
|---|---|---|---|
| Guest can access dashboard directly | P0 | Security risk | Execute direct URL test |
| API status codes unknown | P2 | Missing information | Confirm API contract |
| DB schema unknown | P2 | Blocker | Request schema/entity map |
| Release decision requested | P0 | Human approval | Human test leader decision |

---

## 11. Human Approval Queue

The dashboard should clearly show items requiring human approval.

Approval is required for:

- P0/P1 risk acceptance
- Release readiness decisions
- External Jira/Trello/GitHub/Slack actions
- Production data usage
- Real customer account usage
- Security-sensitive findings
- Destructive DB validation
- High-load performance testing
- Payment or financial flow validation
- Executive report publication

Example approval queue:

| Approval Item | Reason | Required Approver | Status |
|---|---|---|---|
| Create Jira ticket for P0 risk | External action | Human Test Leader | Pending |
| Run DB validation | Data safety | Backend/DB Owner | Pending |
| Send Slack QA summary | External communication | Human Test Leader | Pending |
| Confirm release readiness | Release decision | Human Test Leader / Product Owner | Pending |

---

## 12. External Action Rules

The dashboard must not perform external actions by default.

External actions include:

- Creating Jira tickets
- Creating Trello cards
- Creating GitHub issues
- Sending Slack messages
- Posting Figma comments
- Changing Firebase analytics settings
- Sending emails

Default mode should be:

- dry_run

External action button labels should be explicit:

Safe labels:

- Preview Draft
- Request Approval
- Approve and Send
- Approve and Create

Unsafe labels:

- Auto Create
- Auto Send
- Mark Done
- Mark Passed
- Release Now

---

## 13. Execution Evidence Workflow

The dashboard may show execution status only when evidence exists.

Execution evidence may include:

- Manual test result log
- Playwright report
- API test report
- DB query result evidence
- Performance test report
- Screenshot or video evidence
- CI run artifact
- Human execution note

Without evidence, use:

- Generated
- Drafted
- Planned
- Not Executed
- Execution Evidence Missing

Do not use:

- Passed
- Verified
- Tested Successfully
- Execution Completed

---

## 14. Release Readiness Workflow

The release readiness section should show:

- Current status
- Scope covered
- Generated artifacts
- Reviewed artifacts
- Executed evidence
- Open risks
- Open blockers
- Known confirmed bugs
- Human approval points
- Release decision draft

Safe release readiness wording:

- Release readiness draft prepared
- Current status is Yellow
- Execution evidence is missing
- Human approval required
- Release readiness cannot be confirmed yet

Unsafe wording without evidence:

- Release ready
- Production safe
- QA verified
- Tests passed
- Testing completed

---

## 15. Dashboard Status Colors

| Color | Meaning |
|---|---|
| Green | No major blocker and evidence supports progress |
| Yellow | Missing information, review needed, or manageable risk |
| Red | P0 risk, blocker, unsafe output, or urgent decision needed |
| Gray | Draft, not reviewed, or not executed |

The dashboard should default to Yellow when important information is missing.

---

## 16. Operator Decision Matrix

| Situation | Correct Operator Decision |
|---|---|
| Output generated but not reviewed | Mark as Needs Review |
| Output reviewed but not executed | Mark as Approved for Planning Use |
| Execution evidence missing | Do not mark Passed |
| P0 risk exists | Escalate and require approval |
| DB schema missing | Block query-level DB validation |
| API schema missing | Mark API contract validation as Needs Confirmation |
| External ticket requested | Keep dry-run until approval |
| Release readiness requested without execution | Mark Not Ready for Release Confirmation |

---

## 17. Audit Trail Expectations

Future dashboard should record:

- Who reviewed the output
- Review decision
- Approval decision
- Timestamp
- Reason for decision
- Linked artifacts
- Execution evidence if available
- External action status
- Revision history

Audit trail should not expose secrets or sensitive customer data.

---

## 18. Minimum Dashboard MVP

A future MVP dashboard should include:

- Project/feature selector
- Feature intake view
- Agent routing view
- Output package view
- Output review view
- Risk and blocker view
- Human approval queue
- Release readiness view
- Validation status view
- Workflow history view

Do not build complex visualizations before these core flows are stable.

---

## 19. Safety Requirements

The dashboard must:

- Keep generated and executed states separate
- Require approval for external actions
- Warn about missing execution evidence
- Warn about secrets and production data
- Avoid false release readiness claims
- Show missing information clearly
- Preserve human test leader control
- Avoid auto-running all agents
- Avoid auto-creating external tickets/messages

---

## 20. Final Operator Rule

The dashboard should make QA work more visible, reviewable, and governable.

It should not make unsafe claims faster.

A good dashboard helps humans make better decisions.

It does not replace human judgment.
