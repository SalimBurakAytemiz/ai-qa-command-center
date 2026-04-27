# Demo Script

## 1. Purpose

This document defines a practical demo flow for presenting AI QA Command Center to potential buyers, internal stakeholders, or collaborators.

The demo should show that the framework is structured, safe, reviewable, and more serious than a random AI prompt collection.

---

## 2. Demo Goal

The goal of the demo is to prove:

- The system has a clear QA operating structure.
- It supports multiple feature types.
- It generates structured QA artifacts.
- It includes risk, API, DB, reporting, and release readiness thinking.
- It keeps generated outputs separate from executed results.
- It has validation scripts and GitHub Actions CI.
- It is ready to become a productized QA service or future SaaS base.

---

## 3. Recommended Demo Duration

| Demo Type | Duration | Audience |
|---|---:|---|
| Short Demo | 10-15 minutes | CTO, founder, manager |
| Standard Demo | 25-35 minutes | QA lead, engineering manager |
| Deep Demo | 45-60 minutes | QA team, technical evaluator |

---

## 4. Demo Opening

Suggested opening:

AI QA Command Center is a structured AI-assisted QA operating framework. It is designed to help teams generate, review, and govern QA planning artifacts across product analysis, test planning, API validation, DB validation, reporting, release readiness, and future automation planning.

Then clarify immediately:

It does not claim generated artifacts are executed results. Human review and execution evidence are required.

---

## 5. Demo Flow

## Step 1: Show Repository Structure

Show these areas:

- 02-agent-registry
- 03-prompts
- 04-workflows
- 05-outputs
- templates
- demo
- references
- examples
- 10-scripts/validation
- .github/workflows

Message:

This is not one prompt. This is a structured QA operating framework.

---

## Step 2: Show Agent Registry

Open:

- 02-agent-registry/agents.yaml
- 02-agent-registry/teams.yaml
- 02-agent-registry/model-routing.yaml
- 02-agent-registry/token-policy.yaml

Message:

The system separates QA responsibilities into agents and teams instead of asking one AI assistant to do everything.

Key point:

Different agents handle strategy, test planning, API, DB, reporting, output review, and routing.

---

## Step 3: Show Templates

Open:

- templates/product-intake-form.md
- templates/feature-intake-form.md
- templates/acceptance-criteria-template.md
- templates/automation/playwright-test-template.md
- templates/automation/api-test-template.md

Message:

The framework starts with structured input and produces structured output. This reduces vague AI results.

---

## Step 4: Show Login Demo

Open:

- demo/login-feature/01-input
- demo/login-feature/02-outputs

Show examples:

- product-testing-context.md
- test-plan.md
- api-validation-plan.md
- db-validation-plan.md
- release-readiness-report.md

Message:

The login demo shows authentication, authorization, API, DB, session, and release readiness coverage.

Important phrase:

These are generated planning artifacts, not executed results.

---

## Step 5: Show Content Publishing Demo

Open:

- demo/content-publishing-feature/01-input
- demo/content-publishing-feature/02-outputs

Show examples:

- feature-brief.md
- acceptance-criteria.md
- test-strategy.md
- edge-negative-test-cases.md
- api-validation-plan.md
- db-validation-plan.md
- release-readiness-report.md

Message:

The second demo proves this framework is not only for login/auth. It can handle workflow-heavy CMS-style features with role boundaries, draft/publish state transitions, API validation, DB validation, and release readiness.

---

## Step 6: Show Reference Library

Open:

- references/anti-patterns/testing-anti-patterns.md
- references/security-testing/security-checklist.md
- references/performance-testing/performance-test-patterns.md
- references/mobile-testing/mobile-testing-patterns.md
- references/automation/automation-generation-patterns.md
- references/patterns/release-readiness-patterns.md

Message:

The system teaches agents what good QA output looks like and what bad output looks like.

---

## Step 7: Show Output Review Examples

Open:

- examples/output-reviews/test-plan-review-example.md
- examples/output-reviews/api-plan-review-example.md
- examples/output-reviews/executive-summary-review-example.md

Message:

The framework does not blindly trust generated output. It includes review examples and scoring patterns.

---

## Step 8: Show Integration and Automation Readiness

Open:

- 07-integrations/jira/jira-ticket-template.md
- 07-integrations/slack/slack-report-template.md
- 07-integrations/github/github-config-example.md
- templates/automation/playwright-test-template.md
- templates/automation/performance-test-template.md

Message:

The current version does not execute live integrations, but it defines safe draft templates, config examples, dry-run defaults, and human approval gates.

---

## Step 9: Show Validation and CI

Run or show:

- python 10-scripts/validation/check-agent-registry.py
- python 10-scripts/validation/check-agent-prompt-coverage.py
- GitHub Actions validation workflow

Message:

The repository validates its own structure. If critical files are missing or empty, validation fails.

---

## 6. Demo Closing

Suggested closing:

AI QA Command Center is currently a strong framework foundation. It is demo-ready, reference-rich, validation-backed, and CI-enabled. It is not yet a full SaaS or autonomous execution engine, but it is a serious base for productized AI-assisted QA services, future dashboard development, future integrations, and future automation generation.

---

## 7. Questions To Ask The Buyer

Ask:

- How do you currently create test plans and test cases?
- Do your teams validate API and DB behavior consistently?
- How do you separate planned tests from executed results?
- How do you report release readiness today?
- Do you use Jira, Trello, GitHub, Slack, or another workflow tool?
- Would you use this first as a documentation framework, a QA service layer, or an internal AI QA assistant?

---

## 8. What Not To Claim

Do not claim:

- It executes tests automatically today.
- It replaces QA engineers.
- It guarantees release quality.
- It is a completed SaaS product.
- It creates Jira or Slack items live today.
- It verifies features without execution evidence.

---

## 9. Strong Demo Line

Use this line:

This framework does not try to make AI magically responsible for QA. It gives AI a disciplined QA operating structure and keeps the human test leader in control.

---

## 10. Demo Success Criteria

A successful demo should make the buyer understand:

- What the system is
- What it produces
- How it stays safe
- How it differs from random prompts
- How it could fit into their QA workflow
- What is ready now
- What is future roadmap
