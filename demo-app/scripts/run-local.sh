#!/usr/bin/env bash
set -euo pipefail

echo "Installing demo app dependencies..."
pip install -r demo-app/requirements.txt

echo "Seeding demo database..."
python demo-app/app/seed.py

echo "Starting demo app on http://localhost:3000 ..."
cd demo-app
uvicorn app.main:app --reload --port 3000
