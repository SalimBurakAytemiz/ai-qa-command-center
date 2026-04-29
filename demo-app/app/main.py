from __future__ import annotations

from datetime import datetime, timedelta, timezone
import secrets

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.db import init_db, get_connection
from app.schemas import LoginCodeResponse, LoginCodeResponseData, LoginRequest


app = FastAPI(title="AI QA Command Center Demo App", version="1.4.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def timestamp_with_microseconds(dt: datetime) -> str:
    return dt.strftime("%Y-%m-%dT%H:%M:%S.%fZ")


@app.on_event("startup")
def startup() -> None:
    init_db()


@app.get("/health")
def health() -> dict[str, object]:
    return {
        "success": True,
        "code": 200,
        "data": {
            "status": "ok"
        }
    }


@app.post("/api/auth/login", response_model=LoginCodeResponse)
def login(payload: LoginRequest) -> LoginCodeResponse:
    with get_connection() as connection:
        user = connection.execute(
            "SELECT id, email, password, status FROM users WHERE email = ?",
            (payload.email,),
        ).fetchone()

    if user is None:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if user["status"] != "active":
        raise HTTPException(status_code=403, detail="User is disabled")

    if user["password"] != payload.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    now = datetime.now(timezone.utc)
    expires_at = now + timedelta(minutes=5)

    return LoginCodeResponse(
        success=True,
        code=200,
        data=LoginCodeResponseData(
            expires_at=timestamp_with_microseconds(expires_at),
            server_time=timestamp_with_microseconds(now),
            code=f"{secrets.randbelow(1_000_000):06d}",
        ),
    )
