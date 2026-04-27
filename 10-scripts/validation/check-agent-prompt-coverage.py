from __future__ import annotations

from pathlib import Path
from typing import Dict, List


ROOT = Path(__file__).resolve().parents[2]


REQUIRED_FILES: Dict[str, List[str]] = {
    "Core repository files": [
        "README.md",
        "ROADMAP.md",
        "CHANGELOG.md",
        "LICENSE",
        "CONTRIBUTING.md",
        "MAINTAINERS.md",
        ".gitignore",
        ".gitattributes",
        "requirements.txt",
        ".github/workflows/validate-repo.yml",
    ],

    "Agent registry": [
        "02-agent-registry/agents.yaml",
        "02-agent-registry/teams.yaml",
        "02-agent-registry/model-routing.yaml",
        "02-agent-registry/token-policy.yaml",
        "02-agent-registry/permissions-policy.md",
    ],

    "Validation scripts": [
        "10-scripts/validation/check-agent-registry.py",
        "10-scripts/validation/check-agent-prompt-coverage.py",
    ],

    "Phase 2 specialist prompts": [
        "03-prompts/phase-2-specialists/security-test-agent.md",
        "03-prompts/phase-2-specialists/performance-test-agent.md",
        "03-prompts/phase-2-specialists/mobile-test-agent.md",
        "03-prompts/phase-2-specialists/firebase-analytics-agent.md",
    ],

    "Design UI specialist prompts": [
        "03-prompts/phase-2-specialists/design-ui/web-pixel-perfect-agent.md",
        "03-prompts/phase-2-specialists/design-ui/mobile-responsive-agent.md",
        "03-prompts/phase-2-specialists/design-ui/ios-ui-agent.md",
        "03-prompts/phase-2-specialists/design-ui/android-ui-agent.md",
        "03-prompts/phase-2-specialists/design-ui/visual-regression-agent.md",
        "03-prompts/phase-2-specialists/design-ui/accessibility-agent.md",
    ],
    "Phase 3 operations prompts": [
        "03-prompts/phase-3-operations/release-readiness-agent.md",
        "03-prompts/phase-3-operations/automation-candidate-agent.md",
    ],

    "Demo login feature inputs": [
        "demo/login-feature/01-input/feature-brief.md",
        "demo/login-feature/01-input/acceptance-criteria.md",
        "demo/login-feature/01-input/api-notes.md",
        "demo/login-feature/01-input/db-notes.md",
        "demo/login-feature/01-input/ui-notes.md",
    ],

    "Demo login feature outputs": [
        "demo/login-feature/02-outputs/product-testing-context.md",
        "demo/login-feature/02-outputs/test-strategy.md",
        "demo/login-feature/02-outputs/agent-routing-plan.md",
        "demo/login-feature/02-outputs/test-plan.md",
        "demo/login-feature/02-outputs/happy-path-test-cases.md",
        "demo/login-feature/02-outputs/edge-negative-test-cases.md",
        "demo/login-feature/02-outputs/api-validation-plan.md",
        "demo/login-feature/02-outputs/db-validation-plan.md",
        "demo/login-feature/02-outputs/jira-trello-drafts.md",
        "demo/login-feature/02-outputs/daily-quality-report.md",
        "demo/login-feature/02-outputs/executive-summary.md",
        "demo/login-feature/02-outputs/release-readiness-report.md",
    ],

    "Demo content publishing feature inputs": [
        "demo/content-publishing-feature/01-input/feature-brief.md",
        "demo/content-publishing-feature/01-input/acceptance-criteria.md",
        "demo/content-publishing-feature/01-input/api-notes.md",
        "demo/content-publishing-feature/01-input/db-notes.md",
        "demo/content-publishing-feature/01-input/ui-notes.md",
    ],

    "Demo content publishing feature outputs": [
        "demo/content-publishing-feature/02-outputs/product-testing-context.md",
        "demo/content-publishing-feature/02-outputs/test-strategy.md",
        "demo/content-publishing-feature/02-outputs/agent-routing-plan.md",
        "demo/content-publishing-feature/02-outputs/test-plan.md",
        "demo/content-publishing-feature/02-outputs/happy-path-test-cases.md",
        "demo/content-publishing-feature/02-outputs/edge-negative-test-cases.md",
        "demo/content-publishing-feature/02-outputs/api-validation-plan.md",
        "demo/content-publishing-feature/02-outputs/db-validation-plan.md",
        "demo/content-publishing-feature/02-outputs/jira-trello-drafts.md",
        "demo/content-publishing-feature/02-outputs/daily-quality-report.md",
        "demo/content-publishing-feature/02-outputs/executive-summary.md",
        "demo/content-publishing-feature/02-outputs/release-readiness-report.md",
    ],

    "Execution evidence templates": [
        "templates/execution-evidence-template.md",
    ],
    "Automation draft examples": [
        "examples/automation-drafts/playwright-login-draft-example.md",
        "examples/automation-drafts/api-login-draft-example.md",
        "examples/automation-drafts/db-validation-login-draft-example.md",
        "examples/automation-drafts/performance-login-draft-example.md",
    ],

    "Integration dry-run examples": [
        "examples/integration-dry-runs/jira-dry-run-example.md",
        "examples/integration-dry-runs/slack-dry-run-example.md",
        "examples/integration-dry-runs/github-issue-dry-run-example.md",
        "examples/integration-dry-runs/trello-dry-run-example.md",
    ],

    "Output review examples": [
        "examples/output-reviews/test-plan-review-example.md",
        "examples/output-reviews/test-cases-review-example.md",
        "examples/output-reviews/api-plan-review-example.md",
        "examples/output-reviews/db-plan-review-example.md",
        "examples/output-reviews/executive-summary-review-example.md",
    ],

    "Dashboard docs": [
        "11-dashboard/operator-workflow.md",
        "11-dashboard/mockups/operator-dashboard.md",
        "11-dashboard/mockups/feature-intake-screen.md",
        "11-dashboard/mockups/agent-routing-screen.md",
        "11-dashboard/mockups/output-review-screen.md",
        "11-dashboard/mockups/quality-report-screen.md",
    ],

    "Product packaging docs": [
        "09-docs/product-packaging/product-overview.md",
        "09-docs/product-packaging/target-users.md",
        "09-docs/product-packaging/value-proposition.md",
        "09-docs/product-packaging/demo-script.md",
        "09-docs/product-packaging/limitations-and-safety.md",
        "09-docs/product-packaging/buyer-faq.md",
        "09-docs/product-packaging/sales-one-pager.md",
        "09-docs/product-packaging/pricing/pricing-models.md",
        "09-docs/product-packaging/pricing/package-tiers.md",
        "09-docs/product-packaging/pricing/service-offers.md",
    ],

    "Onboarding docs": [
        "09-docs/onboarding/getting-started.md",
    ],

    "Release docs": [
        "09-docs/releases/v1.0-release-candidate.md",
        "09-docs/releases/v1.0-release-notes.md",
    ],
}


def check_file(path: str) -> tuple[bool, str]:
    file_path = ROOT / path

    if not file_path.exists():
        return False, "MISSING"

    if not file_path.is_file():
        return False, "NOT A FILE"

    if file_path.stat().st_size == 0:
        return False, "EMPTY"

    return True, "OK"


def main() -> int:
    total = 0
    passed = 0
    failures: list[tuple[str, str]] = []

    for section, paths in REQUIRED_FILES.items():
        print(f"\n[{section}]")

        for path in paths:
            total += 1
            ok, status = check_file(path)

            if ok:
                passed += 1
                print(f"  OK      {path}")
            else:
                failures.append((path, status))
                print(f"  {status:<7} {path}")

    print("\n" + "=" * 72)
    print(f"Checked Files: {total}")
    print(f"Passed:        {passed}")
    print(f"Missing/Bad:   {len(failures)}")

    if failures:
        print("\nMissing or invalid files:")
        for path, status in failures:
            print(f"  - {status}: {path}")

        print("\nResult: FAILED")
        return 1

    print("\nResult: PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


