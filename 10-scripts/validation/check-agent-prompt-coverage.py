from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]

REQUIRED_FILES = {
    "Core repository files": [
        "README.md",
        "ROADMAP.md",
        "CHANGELOG.md",
        "LICENSE",
        ".env.example",
        ".gitignore",
    ],
    "Agent registry": [
        "02-agent-registry/agents.yaml",
        "02-agent-registry/teams.yaml",
        "02-agent-registry/management-agents.yaml",
        "02-agent-registry/model-routing.yaml",
        "02-agent-registry/permissions.yaml",
        "02-agent-registry/token-policy.yaml",
        "02-agent-registry/workflow-routing.yaml",
    ],
    "Management prompts": [
        "03-prompts/01-management-team/product-intake-agent.md",
        "03-prompts/01-management-team/test-strategy-agent.md",
        "03-prompts/01-management-team/task-router-agent.md",
        "03-prompts/01-management-team/token-controller-agent.md",
        "03-prompts/01-management-team/output-reviewer-agent.md",
    ],
    "Phase 1 specialist prompts": [
        "03-prompts/02-test-planning/test-planning-agent.md",
        "03-prompts/02-test-planning/happy-path-test-case-agent.md",
        "03-prompts/02-test-planning/edge-case-negative-case-agent.md",
        "03-prompts/03-product-flow/product-flow-test-agent.md",
        "03-prompts/03-product-flow/feature-validation-agent.md",
        "03-prompts/05-web-mobile-notification/web-functional-test-agent.md",
        "03-prompts/06-backend-db-realtime/api-test-agent.md",
        "03-prompts/06-backend-db-realtime/database-validation-agent.md",
        "03-prompts/09-operations-reporting/environment-health-agent.md",
        "03-prompts/09-operations-reporting/jira-trello-work-tracking-agent.md",
        "03-prompts/09-operations-reporting/daily-quality-report-agent.md",
    ],
    "AI tool compatible agents": [
        ".github/agents/qa-orchestrator.agent.md",
        ".github/agents/test-case-designer.agent.md",
        ".github/agents/api-test-agent.agent.md",
        ".github/agents/db-validation-agent.agent.md",
        ".github/agents/web-functional-test-agent.agent.md",
    ],
    "AI tool instructions": [
        ".github/instructions/qa-general.instructions.md",
        ".github/instructions/test-case-design.instructions.md",
        ".github/instructions/api-testing.instructions.md",
        ".github/instructions/db-validation.instructions.md",
        ".github/instructions/playwright.instructions.md",
        ".github/instructions/reporting.instructions.md",
    ],
    "AI tool skills": [
        ".github/skills/test-case-design/SKILL.md",
        ".github/skills/api-testing/SKILL.md",
        ".github/skills/db-validation/SKILL.md",
        ".github/skills/web-functional-testing/SKILL.md",
        ".github/skills/qa-reporting/SKILL.md",
    ],
    "Templates": [
        "templates/product-intake-form.md",
        "templates/feature-intake-form.md",
        "templates/acceptance-criteria-template.md",
        "templates/api-notes-template.md",
        "templates/db-notes-template.md",
        "templates/release-scope-template.md",
    ],
    "Automation templates": [
        "templates/automation/playwright-test-template.md",
        "templates/automation/api-test-template.md",
        "templates/automation/db-validation-script-template.md",
        "templates/automation/appium-test-template.md",
        "templates/automation/performance-test-template.md",
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
    ],
    "Example output library": [
        "examples/outputs/sample-test-plan.md",
        "examples/outputs/sample-happy-path-test-cases.md",
        "examples/outputs/sample-edge-negative-test-cases.md",
        "examples/outputs/sample-api-validation-plan.md",
        "examples/outputs/sample-db-validation-plan.md",
        "examples/outputs/sample-jira-drafts.md",
        "examples/outputs/sample-daily-quality-report.md",
        "examples/outputs/sample-executive-summary.md",
    ],
    "Reference library": [
        "references/anti-patterns/testing-anti-patterns.md",
        "references/examples/test-case-examples.md",
        "references/examples/api-test-examples.md",
        "references/examples/db-validation-examples.md",
        "references/examples/bug-report-examples.md",
        "references/examples/jira-ticket-examples.md",
        "references/examples/daily-report-examples.md",
        "references/patterns/api-testing-patterns.md",
        "references/patterns/db-validation-patterns.md",
        "references/playwright/playwright-patterns.md",
    ],
    "Integration templates": [
        "07-integrations/jira/jira-ticket-template.md",
        "07-integrations/jira/jira-config-example.md",
        "07-integrations/trello/trello-card-template.md",
        "07-integrations/trello/trello-config-example.md",
        "07-integrations/github/github-issue-template.md",
        "07-integrations/github/github-config-example.md",
        "07-integrations/slack/slack-report-template.md",
        "07-integrations/slack/slack-config-example.md",
        "07-integrations/firebase/firebase-validation-template.md",
        "07-integrations/firebase/firebase-config-example.md",
        "07-integrations/figma/figma-review-template.md",
        "07-integrations/figma/figma-config-example.md",
    ],
    "Dashboard mockups": [
        "11-dashboard/mockups/operator-dashboard.md",
        "11-dashboard/mockups/feature-intake-screen.md",
        "11-dashboard/mockups/agent-routing-screen.md",
        "11-dashboard/mockups/output-review-screen.md",
        "11-dashboard/mockups/quality-report-screen.md",
    ],
    "Architecture and docs": [
        "09-docs/architecture/system-architecture.md",
        "09-docs/prompt-standards/README.md",
        "09-docs/agent-guidelines/README.md",
        "09-docs/workflow-guidelines/README.md",
        "09-docs/output-standards/README.md",
        "09-docs/runbooks/first-run.md",
    ],
}


def file_has_content(path: Path) -> bool:
    if not path.exists() or not path.is_file():
        return False
    return path.stat().st_size > 0


def main() -> int:
    print("AI QA Command Center - Agent Prompt Coverage Check")
    print("=" * 60)

    total = 0
    passed = 0
    missing = []

    for section, files in REQUIRED_FILES.items():
        print(f"\n[{section}]")
        for file_path in files:
            total += 1
            full_path = ROOT / file_path

            if file_has_content(full_path):
                passed += 1
                print(f"  OK      {file_path}")
            else:
                missing.append(file_path)
                print(f"  MISSING {file_path}")

    print("\n" + "=" * 60)
    print(f"Checked files: {total}")
    print(f"Passed:        {passed}")
    print(f"Missing:       {len(missing)}")

    if missing:
        print("\nMissing or empty files:")
        for file_path in missing:
            print(f"  - {file_path}")

        print("\nResult: FAILED")
        return 1

    print("\nResult: PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())






