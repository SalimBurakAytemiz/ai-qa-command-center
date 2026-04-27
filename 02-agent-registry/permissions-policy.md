# Permissions Policy

## 1. Purpose

This document defines permission and approval rules for the AI QA Command Center.

It prevents AI-generated outputs from being treated as executed results, release approvals, external actions, or production-safe decisions without human review and evidence.

---

## 2. Core Principle

AI may generate, organize, review, and recommend.

Humans approve, execute, verify, and decide.

Generated QA artifacts are not executed test results.

Reviewed artifacts are not release approval.

Release readiness requires execution evidence and human approval.

---

## 3. Actions AI Agents May Perform

AI agents may:

- Generate planning artifacts
- Draft test plans
- Draft test cases
- Draft API validation plans
- Draft DB validation plans
- Draft Jira/Trello/GitHub/Slack content
- Draft release readiness reports
- Draft automation candidates
- Draft automation examples
- Review generated outputs
- Identify risks and blockers
- Recommend next actions

---

## 4. Actions Requiring Human Approval

Human approval is required for:

- Release readiness decisions
- P0/P1 risk acceptance
- External Jira ticket creation
- External Trello card creation
- External GitHub issue creation
- Slack message sending
- Figma comment posting
- Firebase analytics changes
- Production data usage
- Real customer account usage
- Security-sensitive findings
- Destructive DB validation
- High-load performance testing
- Payment or financial flow validation
- Executive report publication

---

## 5. Actions AI Agents Must Not Perform Automatically

AI agents must not automatically:

- Approve releases
- Mark tests as passed without evidence
- Mark features as verified without evidence
- Create external tickets without approval
- Send external messages without approval
- Use production credentials
- Use real customer data
- Run destructive DB actions
- Run high-load production performance tests
- Claim security verification without evidence
- Claim performance verification without evidence

---

## 6. External Integration Default Mode

Default integration mode must be:

- dry_run

External integration output should be treated as draft preview until approved.

---

## 7. Generated vs Executed Language

Safe wording:

- Generated
- Drafted
- Planned
- Proposed
- Reviewed
- Needs revision
- Human approval required
- Execution evidence required

Unsafe wording without evidence:

- Passed
- Verified
- Tested successfully
- Production safe
- Release ready
- QA approved
- Execution completed

---

## 8. Final Rule

When evidence is missing, say evidence is missing.

When approval is required, say approval is required.

Do not hide uncertainty behind confident language.
