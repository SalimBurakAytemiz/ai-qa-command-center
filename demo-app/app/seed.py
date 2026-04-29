from __future__ import annotations

import os

from app.db import init_db, get_connection


def seed() -> None:
    init_db()

    test_email = os.getenv("DEMO_TEST_USER_EMAIL", "test@example.com")
    test_password = os.getenv("DEMO_TEST_USER_PASSWORD", "Password123!")

    with get_connection() as connection:
        connection.execute(
            '''
            INSERT OR REPLACE INTO users (id, email, password, status)
            VALUES (?, ?, ?, ?)
            ''',
            ("user-active-1", test_email, test_password, "active"),
        )

        connection.execute(
            '''
            INSERT OR REPLACE INTO users (id, email, password, status)
            VALUES (?, ?, ?, ?)
            ''',
            ("user-disabled-1", "disabled@example.com", "Password123!", "disabled"),
        )

        connection.commit()


if __name__ == "__main__":
    seed()
    print("Demo database seeded.")
