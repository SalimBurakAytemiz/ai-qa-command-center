$outputFolders = @(
    "05-outputs\test-plans",
    "05-outputs\test-cases",
    "05-outputs\happy-path",
    "05-outputs\edge-cases",
    "05-outputs\negative-cases",
    "05-outputs\risk-analysis",
    "05-outputs\automation-candidates",
    "05-outputs\design-review",
    "05-outputs\api-review",
    "05-outputs\db-review",
    "05-outputs\mobile-review",
    "05-outputs\security-review",
    "05-outputs\performance-review",
    "05-outputs\jira-trello",
    "05-outputs\reports"
)

foreach ($folder in $outputFolders) {
    if (Test-Path $folder) {
        Get-ChildItem -Path $folder -File |
            Where-Object { $_.Name -notlike "*-template.md" } |
            Remove-Item -Force
    }
}

Write-Host "Generated output files have been cleaned. Template files were preserved."