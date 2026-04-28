import os

import pytest
import requests


def has_api_login_env() -> bool:
    return bool(
        os.getenv("API_BASE_URL")
        and os.getenv("TEST_USER_EMAIL")
        and os.getenv("TEST_USER_PASSWORD")
    )


@pytest.mark.skipif(
    not has_api_login_env(),
    reason="API_BASE_URL, TEST_USER_EMAIL, and TEST_USER_PASSWORD are required.",
)
def test_login_api_accepts_valid_credentials() -> None:
    base_url = os.environ["API_BASE_URL"].rstrip("/")
    email = os.environ["TEST_USER_EMAIL"]
    password = os.environ["TEST_USER_PASSWORD"]

    response = requests.post(
        f"{base_url}/api/auth/login",
        json={"email": email, "password": password},
        timeout=10,
    )

    assert response.status_code == 200

    body_text = response.text.lower()
    assert password.lower() not in body_text
