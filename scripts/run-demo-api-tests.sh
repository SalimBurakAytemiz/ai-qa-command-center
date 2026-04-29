#!/usr/bin/env bash
set -euo pipefail

echo "Starting AI QA Command Center demo API test run..."

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

export DEMO_APP_DB_PATH="$REPO_ROOT/demo-app/demo.db"
export DEMO_TEST_USER_EMAIL="test@example.com"
export DEMO_TEST_USER_PASSWORD="Password123!"
export DISABLED_TEST_USER_ID="user-disabled-1"

export API_BASE_URL="http://127.0.0.1:3000"
export TEST_USER_EMAIL="test@example.com"
export TEST_USER_PASSWORD="Password123!"
export API_RESPONSE_TIME_LIMIT_MS="1000"

echo "Installing demo app Python dependencies..."
python -m pip install -r demo-app/requirements.txt

echo "Seeding demo database..."
(
  cd demo-app
  python -m app.seed
)

echo "Starting demo app..."
(
  cd demo-app
  uvicorn app.main:app --host 127.0.0.1 --port 3000
) &
DEMO_PID=$!

cleanup() {
  echo "Stopping demo app..."
  kill "$DEMO_PID" 2>/dev/null || true
}

trap cleanup EXIT

echo "Waiting for demo app health check..."

READY=0

for i in $(seq 1 30); do
  if python - <<'PY'
import json
import urllib.request

try:
    with urllib.request.urlopen("http://127.0.0.1:3000/health", timeout=2) as response:
        data = json.loads(response.read().decode("utf-8"))
        raise SystemExit(0 if data.get("success") is True else 1)
except Exception:
    raise SystemExit(1)
PY
  then
    READY=1
    break
  fi

  sleep 1
done

if [ "$READY" != "1" ]; then
  echo "Demo app did not become ready in time."
  exit 1
fi

echo "Running Python API tests..."
(
  cd 06-tests/api
  python -m pip install -r requirements.txt
  python -m pytest
)

echo "Running AJV API contract tests..."
(
  cd 06-tests/api-ajv
  npm install
  npm test
)

echo "Running DB validation..."
export SQLITE_DB_PATH="$REPO_ROOT/demo-app/demo.db"
python 06-tests/db-validation/validate_login_state.py

echo "Demo API test run completed successfully."

