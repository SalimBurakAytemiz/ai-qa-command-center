from __future__ import annotations

import os
import sqlite3
from pathlib import Path


DEFAULT_DB_PATH = Path(__file__).resolve().parents[1] / "demo.db"


def get_db_path() -> Path:
    return Path(os.getenv("DEMO_APP_DB_PATH", str(DEFAULT_DB_PATH)))


def get_connection() -> sqlite3.Connection:
    db_path = get_db_path()
    db_path.parent.mkdir(parents=True, exist_ok=True)

    connection = sqlite3.connect(db_path)
    connection.row_factory = sqlite3.Row
    return connection


def init_db() -> None:
    with get_connection() as connection:
        connection.execute(
            '''
            CREATE TABLE IF NOT EXISTS users (
                id TEXT PRIMARY KEY,
                email TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                status TEXT NOT NULL
            )
            '''
        )

        connection.execute(
            '''
            CREATE TABLE IF NOT EXISTS sessions (
                id TEXT PRIMARY KEY,
                user_id TEXT NOT NULL,
                created_at TEXT NOT NULL,
                revoked_at TEXT,
                FOREIGN KEY(user_id) REFERENCES users(id)
            )
            '''
        )

        connection.commit()
