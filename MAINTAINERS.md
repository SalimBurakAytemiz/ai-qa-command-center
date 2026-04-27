# Maintainers Guide

## 1. Purpose

This guide explains how to maintain the AI QA Command Center repository safely and consistently.

It is intended for maintainers who manage versions, validation, documentation updates, release preparation, and repository hygiene.

---

## 2. Maintainer Responsibility

Maintainers are responsible for:

- Keeping the repository structure consistent
- Running validation before release
- Updating README, ROADMAP, and CHANGELOG for meaningful changes
- Preventing temporary files from being committed
- Preserving generated vs executed safety language
- Checking GitHub Actions after push
- Keeping version updates honest
- Preparing release candidate audits
- Avoiding overclaiming product maturity

---

## 3. Core Maintainer Principle

The repository must preserve this principle:

AI may generate, organize, review, and recommend.

Humans approve, execute, verify, and decide.

Generated QA artifacts are not executed test results.

Reviewed artifacts are not release approval.

Release readiness requires execution evidence and human approval.

---

## 4. Versioning Approach

Use version updates when a meaningful capability layer is added.

Examples:

| Version Type | Example |
|---|---|
| Documentation layer | Product packaging docs, onboarding docs, maintainer docs |
| Demo layer | New complete demo feature pack |
| Validation layer | New required file coverage |
| Prompt layer | New agent prompt group |
| Example layer | Automation drafts, integration dry-runs |
| Dashboard layer | Dashboard mockups or workflow docs |

Avoid version bumps for tiny typo-only changes unless they affect public documentation significantly.

---

## 5. Required Release Files

For meaningful releases, update:

- CHANGELOG.md
- ROADMAP.md
- README.md

When applicable, also update:

- 10-scripts/validation/check-agent-prompt-coverage.py
- 02-agent-registry/agents.yaml
- 02-agent-registry/teams.yaml
- 02-agent-registry/model-routing.yaml
- CONTRIBUTING.md
- MAINTAINERS.md

---

## 6. Validation Before Push

Before pushing meaningful changes, run:

python 10-scripts/validation/check-agent-registry.py

python 10-scripts/validation/check-agent-prompt-coverage.py

Expected result:

- Agent registry validation passed successfully.
- Result: PASSED

Do not push knowingly broken validation unless the purpose of the branch is to fix validation.

---

## 7. GitHub Actions Check

After pushing to main, check:

Actions > Validate AI QA Command Center Repository

The latest run should be green.

If GitHub Actions fails:

1. Open the failed run.
2. Read the failed step.
3. Compare with local validation.
4. Fix missing or empty files.
5. Commit and push the fix.
6. Re-check Actions.

---

## 8. Temporary Files

Do not commit temporary files.

Examples of files that should not be committed:

- remote-files.txt
- local-debug.txt
- scratch.md
- temp-output.txt
- _create_*.py
- .env
- .env.local
- service-account.json
- credentials.json
- *.log
- local screenshots with sensitive data

If a temporary file is accidentally committed, remove it:

git rm <file>

git commit -m "Remove temporary file"

git push

---

## 9. Repository Hygiene Checklist

Before release, check:

- git status is clean
- main is up to date with origin/main
- validation passes
- GitHub Actions passes
- no temporary files exist
- no secrets exist
- no production credentials exist
- no real customer data exists
- README reflects current capability
- ROADMAP reflects completed and next work
- CHANGELOG includes release entry
- Generated vs executed language is safe

---

## 10. Release Candidate Audit

Before calling a release candidate ready, run:

git status

git fetch origin

git status -sb

python 10-scripts/validation/check-agent-registry.py

python 10-scripts/validation/check-agent-prompt-coverage.py

Then inspect:

- README.md
- ROADMAP.md
- CHANGELOG.md
- CONTRIBUTING.md
- MAINTAINERS.md
- 09-docs/onboarding/getting-started.md
- 09-docs/product-packaging/product-overview.md
- 09-docs/product-packaging/sales-one-pager.md
- demo/login-feature/
- demo/content-publishing-feature/
- examples/automation-drafts/
- examples/integration-dry-runs/

---

## 11. Documentation Consistency Rules

README should answer:

- What is this?
- What does it include?
- What is the current version capability?
- What is next?
- What safety rules apply?

ROADMAP should answer:

- What was completed?
- What is next?
- What is future implementation work?
- What should wait until post-v1.0?

CHANGELOG should answer:

- What was added?
- What changed?
- What validation passed?
- What limitations apply?

---

## 12. Safety Language Review

Search for unsafe claims before release.

Unsafe wording unless evidence exists:

- tests passed
- verified
- QA approved
- release ready
- production safe
- performance verified
- security verified
- mobile verified
- analytics verified
- automation executed

Safe wording:

- generated
- drafted
- planned
- reviewed
- candidate
- dry-run
- execution evidence required
- human approval required
- release readiness cannot be confirmed yet

---

## 13. External Action Safety

Maintainers must ensure external integrations remain safe by default.

Default integration mode:

- dry_run

External actions requiring approval:

- Jira ticket creation
- Trello card creation
- GitHub issue creation
- Slack message sending
- Figma comments
- Firebase changes
- Email sending

No external action should be presented as already performed unless it actually happened and evidence exists.

---

## 14. Automation Safety

Automation examples and templates are not execution evidence.

Do not claim:

- automation passed
- regression passed
- performance verified
- mobile verified
- API verified
- DB verified

unless real execution artifacts exist.

---

## 15. Maintainer Release Flow

Recommended flow:

1. Add or update files.
2. Update validation coverage if needed.
3. Run local validation.
4. Update CHANGELOG, ROADMAP, and README if capability changed.
5. Run final local validation.
6. Commit with clear message.
7. Push to main.
8. Check GitHub Actions.
9. Confirm git status is clean.
10. Perform release candidate audit if preparing release.

---

## 16. Commit Message Examples

Good:

- Add maintainers guide
- Update validation coverage for maintainers guide
- Update docs for maintainer guidance layer
- Remove temporary remote files listing
- Prepare v1.0 release candidate audit docs

Bad:

- update
- fix
- stuff
- final
- last
- aaa

---

## 17. v1.0 Readiness Criteria

The repository is ready for v1.0 when:

- Validation passes locally
- GitHub Actions passes
- README is coherent
- ROADMAP separates completed vs future work
- CHANGELOG has v1.0 release notes
- Product packaging docs exist
- Onboarding docs exist
- Contributor and maintainer docs exist
- At least two demo feature packs exist
- Safety rules are consistent
- Temporary files are removed
- The repository is honest about not being a completed SaaS or autonomous execution platform

---

## 18. Final Maintainer Rule

Do not make the repository look more mature than it is.

Make it more useful, safer, clearer, and easier to operate.

That is the maintainer job.
