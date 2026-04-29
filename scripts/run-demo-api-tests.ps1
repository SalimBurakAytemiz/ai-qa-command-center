$ErrorActionPreference = "Stop"

Write-Host "Starting AI QA Command Center demo API test run..."

$repoRoot = Split-Path -Parent $PSScriptRoot
Set-Location $repoRoot

$env:DEMO_APP_DB_PATH = "$repoRoot\demo-app\demo.db"
$env:DEMO_TEST_USER_EMAIL = "test@example.com"
$env:DEMO_TEST_USER_PASSWORD = "Password123!"
$env:DISABLED_TEST_USER_ID = "user-disabled-1"

$env:API_BASE_URL = "http://127.0.0.1:3000"
$env:TEST_USER_EMAIL = "test@example.com"
$env:TEST_USER_PASSWORD = "Password123!"
$env:API_RESPONSE_TIME_LIMIT_MS = "1000"

$logDir = "$repoRoot\test-results\demo-api-run"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null

$stdoutLog = "$logDir\demo-app.stdout.log"
$stderrLog = "$logDir\demo-app.stderr.log"

Remove-Item $stdoutLog -ErrorAction SilentlyContinue
Remove-Item $stderrLog -ErrorAction SilentlyContinue

Write-Host "Installing demo app Python dependencies..."
python -m pip install -r demo-app\requirements.txt

Write-Host "Seeding demo database..."
Push-Location demo-app
python -m app.seed
Pop-Location

Write-Host "Starting demo app..."
$demoProcess = Start-Process python `
    -ArgumentList "-m", "uvicorn", "app.main:app", "--host", "127.0.0.1", "--port", "3000" `
    -WorkingDirectory "$repoRoot\demo-app" `
    -RedirectStandardOutput $stdoutLog `
    -RedirectStandardError $stderrLog `
    -PassThru

try {
    Write-Host "Waiting for demo app health check..."

    $ready = $false

    for ($i = 1; $i -le 30; $i++) {
        if ($demoProcess.HasExited) {
            Write-Host "Demo app process exited early."
            Write-Host "STDOUT:"
            Get-Content $stdoutLog -ErrorAction SilentlyContinue
            Write-Host "STDERR:"
            Get-Content $stderrLog -ErrorAction SilentlyContinue
            throw "Demo app process exited before becoming ready."
        }

        try {
            $health = Invoke-RestMethod -Uri "http://127.0.0.1:3000/health" -Method Get -TimeoutSec 2
            if ($health.success -eq $true) {
                $ready = $true
                break
            }
        } catch {
            Start-Sleep -Seconds 1
        }
    }

    if (-not $ready) {
        Write-Host "Demo app did not become ready in time."
        Write-Host "STDOUT:"
        Get-Content $stdoutLog -ErrorAction SilentlyContinue
        Write-Host "STDERR:"
        Get-Content $stderrLog -ErrorAction SilentlyContinue
        throw "Demo app did not become ready in time."
    }

    Write-Host "Running Python API tests..."
    Push-Location 06-tests\api
    python -m pip install -r requirements.txt
    python -m pytest
    Pop-Location

    Write-Host "Running AJV API contract tests..."
    Push-Location 06-tests\api-ajv
    npm.cmd install
    npm.cmd test
    Pop-Location

    Write-Host "Running DB validation..."
    $env:SQLITE_DB_PATH = "$repoRoot\demo-app\demo.db"
    python 06-tests\db-validation\validate_login_state.py

    Write-Host "Demo API test run completed successfully."
}
finally {
    if ($demoProcess -and -not $demoProcess.HasExited) {
        Write-Host "Stopping demo app..."
        Stop-Process -Id $demoProcess.Id -Force
    }
}
