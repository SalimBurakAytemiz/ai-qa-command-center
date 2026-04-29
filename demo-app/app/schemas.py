from __future__ import annotations

from pydantic import BaseModel, EmailStr, Field


class LoginRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=1, max_length=256)


class LoginCodeResponseData(BaseModel):
    expires_at: str
    server_time: str
    code: str = Field(pattern=r"^\d{6}$")


class LoginCodeResponse(BaseModel):
    success: bool
    code: int
    data: LoginCodeResponseData
