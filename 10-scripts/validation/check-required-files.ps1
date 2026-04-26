$requiredFiles = @(
    "README.md",
    ".gitignore",
    ".env.example",

    "00-product-context\product-overview.md",
    "00-product-context\user-roles.md",
    "00-product-context\modules.md",

    "02-agent-registry\teams.yaml",
    "02-agent-registry\agents.yaml",
    "02-agent-registry\management-agents.yaml",
    "02-agent-registry\model-routing.yaml",
    "02-agent-registry\permissions.yaml",
    "02-agent-registry\workflow-routing.yaml",
    "02-agent-registry\token-policy.yaml",

    "03-prompts\01-management-team\product-intake-agent.md",
    "03-prompts\01-management-team\test-strategy-agent.md",
    "03-prompts\01-management-team\task-router-agent.md",
    "03-prompts\01-management-team\token-controller-agent.md",
    "03-prompts\01-management-team\output-reviewer-agent.md",

    "03-prompts\02-test-planning\test-planning-agent.md",
    "03-prompts\02-test-planning\happy-path-test-case-agent.md",
    "03-prompts\02-test-planning\edge-negative-case-agent.md",

    "03-prompts\03-product-flow\product-flow-test-agent.md",
    "03-prompts\03-product-flow\feature-validation-agent.md",

    "03-prompts\05-web-mobile-notification\web-functional-test-agent.md",

    "03-prompts\06-backend-db-realtime\api-test-agent.md",
    "03-prompts\06-backend-db-realtime\db-validation-agent.md",
    "03-prompts\06-backend-db-realtime\environment-health-agent.md",

    "03-prompts\09-operations-reporting\jira-trello-agent.md",
    "03-prompts\09-operations-reporting\daily-quality-report-agent.md",

    "04-workflows\00-master-workflows\product-to-test-pack.md",
    "04-workflows\01-product-analysis\product-intake-workflow.md",
    "04-workflows\02-test-case-generation\test-case-generation-workflow.md",
    "04-workflows\04-backend-validation\api-db-validation-workflow.md",
    "04-workflows\07-reporting\daily-report-workflow.md",

    "08-skills\test-case-design\README.md",
    "08-skills\api-testing\README.md",
    "08-skills\db-validation\README.md",
    "08-skills\ui-testing\README.md",
    "08-skills\reporting\README.md",

    "09-docs\prompt-standards\README.md",
    "09-docs\agent-guidelines\README.md",
    "09-docs\workflow-guidelines\README.md",
    "09-docs\output-standards\README.md",
    "09-docs\runbooks\first-run.md"
)

$missingFiles = @()

foreach ($file in $requiredFiles) {
    if (-not (Test-Path $file)) {
        $missingFiles += $file
    }
}

if ($missingFiles.Count -eq 0) {
    Write-Host "All required files exist."
    exit 0
}

Write-Host "Missing required files:"
foreach ($file in $missingFiles) {
    Write-Host "- $file"
}

exit 1