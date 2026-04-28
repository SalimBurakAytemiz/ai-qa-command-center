from __future__ import annotations

import os
import sqlite3
from pathlib import Path


def main() -> int:
    database_path = os.getenv("SQLITE_DB_PATH")

    if not database_path:
        print("SKIPPED: SQLITE_DB_PATH is not set.")
        return 0

    db_file = Path(database_path)

    if not db_file.exists():
        print(f"FAILED: SQLite database does not exist: {db_file}")
        return 1

    disabled_user_id = os.getenv("DISABLED_TEST_USER_ID")

    if not disabled_user_id:
        print("SKIPPED: DISABLED_TEST_USER_ID is not set.")
        return 0

    with sqlite3.connect(db_file) as connection:
        cursor = connection.cursor()

        cursor.execute(
            "SELECT COUNT(*) FROM sessions WHERE user_id = ? AND revoked_at IS NULL",
            (disabled_user_id,),
        )

        active_session_count = cursor.fetchone()[0]

    if active_session_count != 0:
        print(f"FAILED: Disabled user has active sessions: {active_session_count}")
        return 1

    print("PASSED: Disabled user has no active sessions.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
