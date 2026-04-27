# Limitations and Safety

## 1. Purpose

This document defines the current limitations and safety rules for AI QA Command Center.

It should be used during product packaging, buyer demos, onboarding, and internal governance.

---

## 2. Current Product Limitation

AI QA Command Center is currently a repository-based AI-assisted QA operating framework.

It is not yet a completed SaaS product, live dashboard, autonomous test execution engine, or live integration platform.

---

## 3. What The Current Version Can Do

The current version can help teams generate, organize, review, and govern QA planning artifacts.

It can support:

- Product testing context generation
- Test strategy drafting
- Agent routing planning
- Test plan drafting
- Happy path test case drafting
- Edge and negative test case drafting
- API validation planning
- DB validation planning
- Jira/Trello draft preparation
- Daily QA report drafting
- Executive summary drafting
- Release readiness drafting
- Output review examples
- Automation candidate planning
- Automation draft template structure
- Integration draft and configuration planning
- Repository validation
- GitHub Actions repository health checks

---

## 4. What The Current Version Cannot Do Yet

The current version does not yet:

- Execute manual tests
- Execute automated tests
- Run Playwright/Appium/API/DB/performance tests as active suites
- Create live Jira tickets
- Create live Trello cards
- Send live Slack messages
- Read live Figma files
- Query live Firebase analytics
- Make final release decisions
- Replace QA engineers
- Replace human test leadership
- Replace security testing
- Replace penetration testing
- Replace product owner decisions
- Guarantee production quality

---

## 5. Generated vs Executed Rule

The most important rule:

Generated output is not execution evidence.

Generated artifacts include:

- Test plans
- Test cases
- API validation plans
- DB validation plans
- Jira/Trello drafts
- Daily reports
- Executive summaries
- Release readiness drafts
- Automation candidates
- Automation draft templates
- Integration drafts

These must not be reported as:

- Passed
- Verified
- Tested successfully
- Execution completed
- Release ready
- Production safe

unless real execution evidence exists.

---

## 6. Human Approval Required

Human approval is required for:

- Final release go/no-go decisions
- P0/P1 risk acceptance
- External Jira/Trello/GitHub/Slack actions
- Production data usage
- Real customer account usage
- Security-sensitive findings
- Production environment test execution
- Destructive DB validation
- High-load performance testing
- Payment or financial flow validation
- Publishing executive reports
- Sharing sensitive evidence externally

---

## 7. Data Safety Rules

Do not put the following into the repository or AI prompts:

- API keys
- Access tokens
- Refresh tokens
- Passwords
- Private keys
- Service account JSON files
- Production credentials
- Customer personal data
- Payment data
- Internal security details
- Private URLs unless approved
- Confidential business data unless approved

Use placeholders, sanitized examples, or environment variable names instead.

---

## 8. Integration Safety Rules

Integration templates and config examples are draft-only.

AI agents must not create or send external actions without explicit human approval.

This includes:

- Jira tickets
- Trello cards
- GitHub issues
- Slack messages
- Figma comments
- Firebase analytics changes
- Email messages

Recommended default integration mode:

- dry_run

External action settings should remain disabled until approved.

---

## 9. Automation Safety Rules

Automation templates are not executable proof.

Generated automation drafts must not be reported as passed or verified unless actually executed.

Human approval is required before running automation against:

- Production
- Shared high-risk environments
- Real customer data
- Payment systems
- Destructive DB actions
- High-load performance targets

---

## 10. Release Readiness Safety Rules

Release readiness drafts are not release approvals.

A release readiness report can say:

- Current draft status is Yellow
- Execution evidence is missing
- Human approval is required
- Release readiness cannot be confirmed yet

It must not say:

- Release ready
- Production safe
- QA verified
- Tests passed
- Testing completed

unless evidence and human approval exist.

---

## 11. Security Safety Rules

The security checklist helps plan security validation.

It does not replace:

- Security review
- Secure code review
- Penetration testing
- Threat modeling
- Compliance review
- Privacy/legal review

Security-sensitive findings require human review.

---

## 12. Buyer Communication Rule

When presenting the product, be honest.

Correct positioning:

AI QA Command Center is a structured AI-assisted QA operating framework and productized service foundation.

Incorrect positioning:

AI QA Command Center is a fully autonomous QA platform that executes and verifies everything automatically.

---

## 13. Current Honest Status

Current status:

- Strong framework foundation
- Demo-ready
- CI-backed
- Documentation-rich
- Reference-rich
- Good for productized QA service packaging
- Good base for future dashboard, integrations, and automation generation

Not yet:

- Full SaaS
- Full live dashboard
- Full test execution system
- Full integration platform

---

## 14. Safety Principle

AI may generate, organize, review, and recommend.

Humans approve, execute, verify, and decide.
