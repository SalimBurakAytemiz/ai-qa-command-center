# Agent Coverage Matrix

## 1. Purpose

This document summarizes current agent and prompt coverage in AI QA Command Center.

It helps answer:

- Which agent areas are currently covered?
- Which areas are partially covered?
- Which areas are future work?
- What should be prioritized next?

---

## 2. Coverage Status Legend

| Status | Meaning |
|---|---|
| Covered | Dedicated prompt or strong direct coverage exists |
| Partially Covered | Some coverage exists, but not full specialist depth |
| Planned | Identified as future work |
| Not Started | No meaningful prompt or template exists yet |
| Not Applicable | Out of current framework scope |

---

## 3. Foundation and Orchestration Coverage

| Area / Agent | Current Status | Current Location | Notes |
|---|---|---|---|
| Product Intake | Covered | Prompt/library and demo outputs | Used in demo feature packs |
| Test Strategy | Covered | Prompt/library and demo outputs | Strategy outputs exist |
| Task Routing / Agent Routing | Covered | Demo outputs and workflow docs | Agent routing plans exist |
| Token / Context Control | Covered | `02-agent-registry/token-policy.yaml` | Policy exists |
| Output Review | Covered | `examples/output-reviews/` | Review examples exist |
| Release Readiness | Covered | `03-prompts/phase-3-operations/release-readiness-agent.md` | Prompt and demo reports exist |
| Automation Candidate | Covered | `03-prompts/phase-3-operations/automation-candidate-agent.md` | Prompt and references exist |

---

## 4. Core QA Agent Coverage

| Area / Agent | Current Status | Current Location | Notes |
|---|---|---|---|
| Test Planning | Covered | Demo outputs and templates | Test plans exist |
| Happy Path Test Cases | Covered | Demo outputs | Login and content publishing examples |
| Edge / Negative Test Cases | Covered | Demo outputs | Login and content publishing examples |
| API Validation | Covered | Demo outputs and automation draft examples | API validation plans exist |
| DB Validation | Covered | Demo outputs and automation draft examples | DB validation plans exist |
| Jira / Trello Drafting | Covered | Demo outputs and integration dry-runs | Draft-only, no live action |
| Daily QA Reporting | Covered | Demo outputs | Planning summary only |
| Executive Summary | Covered | Demo outputs | Draft summary only |

---

## 5. Security, Performance, Mobile, and Analytics Coverage

| Area / Agent | Current Status | Current Location | Notes |
|---|---|---|---|
| Security Test Agent | Covered | `03-prompts/phase-2-specialists/security-test-agent.md` | Planning only, not penetration testing |
| Performance Test Agent | Covered | `03-prompts/phase-2-specialists/performance-test-agent.md` | Planning only, not execution |
| Mobile Test Agent | Covered | `03-prompts/phase-2-specialists/mobile-test-agent.md` | General mobile planning |
| Firebase Analytics Agent | Covered | `03-prompts/phase-2-specialists/firebase-analytics-agent.md` | Planning only, no live analytics query |

---

## 6. Design/UI Coverage

| Area / Agent | Current Status | Current Location | Notes |
|---|---|---|---|
| Web Pixel Perfect Agent | Covered | `03-prompts/phase-2-specialists/design-ui/web-pixel-perfect-agent.md` | Requires design evidence |
| Mobile Responsive Agent | Covered | `03-prompts/phase-2-specialists/design-ui/mobile-responsive-agent.md` | Responsive web, not native mobile |
| iOS UI Agent | Covered | `03-prompts/phase-2-specialists/design-ui/ios-ui-agent.md` | Requires device/simulator evidence for execution |
| Android UI Agent | Covered | `03-prompts/phase-2-specialists/design-ui/android-ui-agent.md` | Requires device/emulator evidence for execution |
| Visual Regression Agent | Covered | `03-prompts/phase-2-specialists/design-ui/visual-regression-agent.md` | Requires baseline/comparison evidence |
| Accessibility Agent | Covered | `03-prompts/phase-2-specialists/design-ui/accessibility-agent.md` | Does not claim WCAG compliance without evidence |

---

## 7. DIT Coverage

| Area / Agent | Current Status | Current Location | Notes |
|---|---|---|---|
| Backend DIT Agent | Covered | `03-prompts/phase-2-specialists/dit/backend-dit-agent.md` | Backend testability planning |
| Android DIT Agent | Covered | `03-prompts/phase-2-specialists/dit/android-dit-agent.md` | Android testability planning |
| iOS DIT Agent | Covered | `03-prompts/phase-2-specialists/dit/ios-dit-agent.md` | iOS testability planning |
| Testability Agent | Covered | `03-prompts/phase-2-specialists/dit/testability-agent.md` | General feature testability review |

---

## 8. Automation and Integration Coverage

| Area / Agent | Current Status | Current Location | Notes |
|---|---|---|---|
| Playwright Automation Drafting | Partially Covered | `templates/automation/`, `examples/automation-drafts/` | Draft examples exist, generator not implemented |
| API Automation Drafting | Partially Covered | `templates/automation/`, `examples/automation-drafts/` | Draft examples exist |
| DB Validation Script Drafting | Partially Covered | `templates/automation/`, `examples/automation-drafts/` | Draft examples exist |
| Appium Automation Drafting | Partially Covered | `templates/automation/appium-test-template.md` | Template exists, no full example suite |
| Performance Automation Drafting | Partially Covered | `templates/automation/`, `examples/automation-drafts/` | k6-style draft exists |
| Jira Integration | Partially Covered | `07-integrations/`, `examples/integration-dry-runs/` | Dry-run only |
| Trello Integration | Partially Covered | `07-integrations/`, `examples/integration-dry-runs/` | Dry-run only |
| GitHub Issue Integration | Partially Covered | `07-integrations/`, `examples/integration-dry-runs/` | Dry-run only |
| Slack Integration | Partially Covered | `07-integrations/`, `examples/integration-dry-runs/` | Dry-run only |
| Figma Integration | Partially Covered | `07-integrations/figma/` | Template/config only |
| Firebase Integration | Partially Covered | `07-integrations/firebase/` | Template/config only |

---

## 9. Dashboard Coverage

| Area / Agent | Current Status | Current Location | Notes |
|---|---|---|---|
| Dashboard Mockups | Covered | `11-dashboard/mockups/` | Documentation mockups |
| Dashboard Operator Workflow | Covered | `11-dashboard/operator-workflow.md` | Future dashboard workflow |
| Real Dashboard Application | Planned | Post-v1.x roadmap | Not implemented |

---

## 10. Demo Coverage

| Demo Type | Current Status | Location | Notes |
|---|---|---|---|
| Authentication/Login Demo | Covered | `demo/login-feature/` | Complete feature pack |
| CMS/Content Publishing Demo | Covered | `demo/content-publishing-feature/` | Complete feature pack |
| Mobile-heavy Demo | Planned | Post-v1.2 candidate | Useful for push/deep link/mobile coverage |
| Payment/Checkout Demo | Planned | Future | Would require careful safety wording |
| Notification Demo | Planned | Future | Useful for mobile/Firebase/integration coverage |

---

## 11. Known Remaining Gaps

| Gap | Priority | Reason |
|---|---|---|
| Real automation generation scripts | High | Templates/examples exist but generation is not implemented |
| Real live integrations | High | Dry-run examples exist but external actions are not implemented |
| Real dashboard application | High | Mockups/workflow exist but app is not implemented |
| Execution evidence examples | Medium | Template exists, but filled examples would help |
| Mobile-heavy third demo | Medium | Would prove native/mobile/Firebase/deep-link workflow |
| Architecture diagram | Medium | Would improve readability and onboarding |
| Hosted documentation site | Low | Useful later, not required now |

---

## 12. Safety Note

Coverage means planning, prompting, documentation, examples, or templates exist.

Coverage does not mean execution.

Do not claim that security, performance, mobile behavior, analytics, accessibility, visual regression, automation, integrations, or release readiness are verified unless real execution evidence and human approval exist.
