$ErrorActionPreference = "Stop"

Write-Host "Installing demo app dependencies..."
pip install -r demo-app/requirements.txt

Write-Host "Seeding demo database..."
python demo-app/app/seed.py

Write-Host "Starting demo app on http://localhost:3000 ..."
Push-Location demo-app
uvicorn app.main:app --reload --port 3000
Pop-Location
