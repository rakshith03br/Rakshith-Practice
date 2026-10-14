"""
================================================================================
REST API TESTING & AUTOMATION WITH PYTHON — REFERENCE NOTES
================================================================================

This file is organized as a single reference module. Each SECTION covers one
topic with explanation (in comments) + runnable example code.

Install dependencies:
    pip install requests pytest jsonschema pydantic pydantic-settings \
                pytest-xdist pytest-html allure-pytest responses \
                python-dotenv pytest-rerunfailures schemathesis locust

Run all example tests in this file with:
    pytest rest_api_testing_notes.py -v
================================================================================
"""

import json
import logging
import time
from unittest.mock import MagicMock, patch

import requests

# ==============================================================================
# SECTION 1: REST FUNDAMENTALS (QUICK RECAP — comments only, no code needed)
# ==============================================================================
#
# HTTP METHODS & IDEMPOTENCY
#   GET     - Retrieve resource        | Idempotent: Yes | Safe: Yes
#   POST    - Create resource          | Idempotent: No  | Safe: No
#   PUT     - Replace resource         | Idempotent: Yes | Safe: No
#   PATCH   - Partial update           | Idempotent: No* | Safe: No
#   DELETE  - Remove resource          | Idempotent: Yes | Safe: No
#   HEAD    - Headers only             | Idempotent: Yes | Safe: Yes
#   OPTIONS - Supported methods        | Idempotent: Yes | Safe: Yes
#
# COMMON STATUS CODES
#   2xx: 200 OK, 201 Created, 202 Accepted, 204 No Content
#   3xx: 301/302 Redirect, 304 Not Modified
#   4xx: 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found,
#        409 Conflict, 422 Unprocessable Entity, 429 Too Many Requests
#   5xx: 500 Internal Server Error, 502 Bad Gateway, 503 Service Unavailable
#
# REST CONSTRAINTS (interview favorite)
#   Stateless, Client-Server, Cacheable, Uniform Interface,
#   Layered System, Code on Demand (optional)
# ==============================================================================


BASE_URL = "https://reqres.in/api"


# ==============================================================================
# SECTION 2: BASIC REQUESTS USAGE
# ==============================================================================

def test_get_user():
    response = requests.get(f"{BASE_URL}/users/2", timeout=10)
    assert response.status_code == 200
    body = response.json()
    assert body["data"]["id"] == 2
    assert "email" in body["data"]


def test_create_user():
    payload = {"name": "morpheus", "job": "leader"}
    response = requests.post(f"{BASE_URL}/users", json=payload, timeout=10)
    assert response.status_code == 201
    assert response.json()["name"] == "morpheus"


# Key `requests` params to know cold:
#
# requests.request(
#     method="POST",
#     url=url,
#     params={"page": 2},          # query string
#     json={"key": "value"},       # auto sets Content-Type: application/json
#     data={"key": "value"},       # form-encoded
#     headers={"Authorization": "Bearer <token>"},
#     auth=("user", "pass"),       # basic auth
#     timeout=10,                  # ALWAYS set a timeout
#     verify=True,                 # SSL verification
#     allow_redirects=True,
#     cookies={"session": "abc"},
# )


# ==============================================================================
# SECTION 3: STRUCTURING A REAL FRAMEWORK (not just scripts)
# ==============================================================================
#
# Recommended layered project structure:
#
# api_tests/
# ├── config/
# │   └── settings.py          # env-based config (base_url, creds)
# ├── clients/
# │   ├── base_client.py       # wraps requests.Session
# │   └── user_client.py       # endpoint-specific methods
# ├── models/
# │   └── user.py              # pydantic response models
# ├── tests/
# │   ├── test_users.py
# │   └── test_auth.py
# ├── utils/
# │   ├── schema_validator.py
# │   └── logger.py
# ├── conftest.py
# ├── pytest.ini
# └── requirements.txt
#
# Below is a single-file version of that layering (Client + Fixtures + Tests)
# for illustration purposes.


# --- config/settings.py -------------------------------------------------------
# from pydantic_settings import BaseSettings
#
# class Settings(BaseSettings):
#     base_url: str = "https://reqres.in/api"
#     api_key: str = ""
#     timeout: int = 10
#
#     class Config:
#         env_file = ".env"
#
# settings = Settings()


# --- clients/base_client.py ----------------------------------------------------
class BaseClient:
    """Wraps requests.Session so every call shares headers/timeout/retries."""

    def __init__(self, base_url: str = BASE_URL, timeout: int = 10):
        self.session = requests.Session()
        self.base_url = base_url
        self.timeout = timeout
        self.session.headers.update({"Accept": "application/json"})

    def request(self, method, endpoint, **kwargs):
        url = f"{self.base_url}{endpoint}"
        kwargs.setdefault("timeout", self.timeout)
        response = self.session.request(method, url, **kwargs)
        return response

    def get(self, endpoint, **kwargs):
        return self.request("GET", endpoint, **kwargs)

    def post(self, endpoint, **kwargs):
        return self.request("POST", endpoint, **kwargs)

    def put(self, endpoint, **kwargs):
        return self.request("PUT", endpoint, **kwargs)

    def delete(self, endpoint, **kwargs):
        return self.request("DELETE", endpoint, **kwargs)


# --- clients/user_client.py ----------------------------------------------------
class UserClient(BaseClient):
    """Endpoint-specific client — like a Page Object Model, but for APIs."""

    def get_user(self, user_id):
        return self.get(f"/users/{user_id}")

    def create_user(self, name, job):
        return self.post("/users", json={"name": name, "job": job})

    def delete_user(self, user_id):
        return self.delete(f"/users/{user_id}")


# --- conftest.py fixtures (would live in conftest.py in a real project) --------
# import pytest
#
# @pytest.fixture(scope="session")
# def user_client():
#     return UserClient()
#
# @pytest.fixture
# def created_user(user_client):
#     """Setup + teardown pattern"""
#     response = user_client.create_user("Test User", "QA Engineer")
#     user_id = response.json().get("id")
#     yield response.json()
#     user_client.delete_user(user_id)   # teardown


def test_get_user_via_client():
    client = UserClient()
    response = client.get_user(2)
    assert response.status_code == 200
    assert response.json()["data"]["id"] == 2


def test_created_user_has_id():
    client = UserClient()
    response = client.create_user("Test User", "QA Engineer")
    body = response.json()
    assert "id" in body
    assert body["name"] == "Test User"
    client.delete_user(body["id"])  # manual teardown (use fixture in real suite)


# ==============================================================================
# SECTION 4: JSON SCHEMA VALIDATION
# ==============================================================================

USER_SCHEMA = {
    "type": "object",
    "properties": {
        "data": {
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "email": {"type": "string", "format": "email"},
                "first_name": {"type": "string"},
            },
            "required": ["id", "email", "first_name"],
        }
    },
    "required": ["data"],
}


def test_user_schema():
    import jsonschema

    client = UserClient()
    response = client.get_user(2)
    jsonschema.validate(instance=response.json(), schema=USER_SCHEMA)


# --- Using Pydantic instead (stronger typing, cleaner error messages) --------
# from pydantic import BaseModel, EmailStr
#
# class UserData(BaseModel):
#     id: int
#     email: EmailStr
#     first_name: str
#     last_name: str
#
# class UserResponse(BaseModel):
#     data: UserData
#
# def test_user_model():
#     client = UserClient()
#     response = client.get_user(2)
#     parsed = UserResponse(**response.json())  # raises ValidationError if malformed
#     assert parsed.data.id == 2


# ==============================================================================
# SECTION 5: DATA-DRIVEN TESTING (pytest.mark.parametrize)
# ==============================================================================
#
# import pytest
#
# @pytest.mark.parametrize("user_id, expected_status", [
#     (2, 200),
#     (23, 404),
#     (-1, 404),
# ])
# def test_get_user_status_codes(user_id, expected_status):
#     client = UserClient()
#     response = client.get_user(user_id)
#     assert response.status_code == expected_status
#
# --- Loading test data from JSON/CSV/YAML ------------------------------------
# with open("data/users_payloads.json") as f:
#     test_data = json.load(f)
#
# @pytest.mark.parametrize("payload", test_data)
# def test_create_user_variants(payload):
#     client = UserClient()
#     response = client.create_user(**payload)
#     assert response.status_code == 201


# ==============================================================================
# SECTION 6: AUTHENTICATION PATTERNS
# ==============================================================================

def example_basic_auth():
    return requests.get(BASE_URL, auth=("username", "password"), timeout=10)


def example_bearer_token(token):
    headers = {"Authorization": f"Bearer {token}"}
    return requests.get(BASE_URL, headers=headers, timeout=10)


def get_oauth_token(client_id, client_secret, token_url):
    """OAuth2 client-credentials flow — get token then reuse across session."""
    resp = requests.post(
        token_url,
        data={
            "grant_type": "client_credentials",
            "client_id": client_id,
            "client_secret": client_secret,
        },
        timeout=10,
    )
    return resp.json()["access_token"]


# Fixture pattern (in conftest.py):
# @pytest.fixture(scope="session")
# def auth_headers():
#     token = get_oauth_token(CLIENT_ID, CLIENT_SECRET, TOKEN_URL)
#     return {"Authorization": f"Bearer {token}"}
#
# Store secrets in `.env` — NEVER hardcode credentials in test files.


# ==============================================================================
# SECTION 7: MOCKING EXTERNAL DEPENDENCIES
# ==============================================================================
# Use mocking when testing code that CALLS an API (e.g. your client wrapper),
# not when testing the live API itself.

def test_get_user_mocked_with_responses():
    import responses

    @responses.activate
    def _run():
        responses.add(
            responses.GET,
            "https://reqres.in/api/users/2",
            json={"data": {"id": 2, "email": "janet.weaver@reqres.in"}},
            status=200,
        )
        response = requests.get("https://reqres.in/api/users/2", timeout=10)
        assert response.json()["data"]["id"] == 2

    _run()


@patch("requests.Session.request")
def test_get_user_unittest_mock(mock_request):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"data": {"id": 2}}
    mock_request.return_value = mock_response

    client = UserClient()
    response = client.get_user(2)
    assert response.json()["data"]["id"] == 2


# ==============================================================================
# SECTION 8: HANDLING FLAKINESS & RETRIES
# ==============================================================================

def build_session_with_retries():
    from requests.adapters import HTTPAdapter, Retry

    session = requests.Session()
    retries = Retry(
        total=3,
        backoff_factor=1,  # 1s, 2s, 4s...
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["GET", "POST"],
    )
    session.mount("https://", HTTPAdapter(max_retries=retries))
    return session


# Or via pytest-rerunfailures:
#   pytest --reruns 3 --reruns-delay 2


# ==============================================================================
# SECTION 9: RESPONSE TIME / BASIC PERFORMANCE ASSERTIONS
# ==============================================================================

def test_response_time():
    client = UserClient()
    response = client.get_user(2)
    assert response.elapsed.total_seconds() < 1.5


# For real load testing, use Locust (locustfile.py, separate from pytest suite):
#
# from locust import HttpUser, task, between
#
# class ApiUser(HttpUser):
#     wait_time = between(1, 3)
#
#     @task
#     def get_user(self):
#         self.client.get("/api/users/2")
#
# Run: locust -f locustfile.py --host https://reqres.in


# ==============================================================================
# SECTION 10: CONTRACT TESTING (Schemathesis — property-based, from OpenAPI)
# ==============================================================================
#
# import schemathesis
#
# schema = schemathesis.from_uri("https://reqres.in/api/openapi.json")
#
# @schema.parametrize()
# def test_api_contract(case):
#     response = case.call()
#     case.validate_response(response)
#
# Auto-generates edge-case inputs from your OpenAPI/Swagger spec — great for
# catching contract violations early.


# ==============================================================================
# SECTION 11: LOGGING & DEBUGGABILITY
# ==============================================================================

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("api_tests")


def log_request_response(response):
    logger.info("%s %s", response.request.method, response.request.url)
    logger.info("Status: %s", response.status_code)
    logger.info("Body: %s", response.text[:500])


# Attach this in an autouse fixture or inside BaseClient.request() so every
# call is logged — critical for CI debugging.


# ==============================================================================
# SECTION 12: pytest.ini / MARKERS / FIXTURE SCOPES (reference — separate file)
# ==============================================================================
#
# pytest.ini:
# ------------------------------------------------------------------------------
# [pytest]
# markers =
#     smoke: quick sanity checks
#     regression: full regression suite
#     negative: negative/error-path tests
# addopts = -v --tb=short --html=report.html --self-contained-html
# ------------------------------------------------------------------------------
#
# Usage:
# @pytest.mark.smoke
# def test_health_check():
#     ...
#
# Run selectively:
#   pytest -m smoke
#   pytest -m "not negative"
#
# Fixture scopes (narrow to wide): function (default) -> class -> module ->
# session. Use `session` for auth tokens/clients, `function` for data that
# must not leak between tests.


# ==============================================================================
# SECTION 13: PARALLEL EXECUTION & CI
# ==============================================================================
#
# pip install pytest-xdist
# pytest -n auto        # parallelize across CPU cores
#
# --- Sample GitHub Actions CI (.github/workflows/api-tests.yml) --------------
# name: API Tests
# on: [push, pull_request]
# jobs:
#   test:
#     runs-on: ubuntu-latest
#     steps:
#       - uses: actions/checkout@v4
#       - uses: actions/setup-python@v5
#         with:
#           python-version: "3.11"
#       - run: pip install -r requirements.txt
#       - run: pytest -m smoke -n auto --html=report.html
#       - uses: actions/upload-artifact@v4
#         with:
#           name: test-report
#           path: report.html


# ==============================================================================
# SECTION 14: REPORTING WITH ALLURE
# ==============================================================================
#
# pip install allure-pytest
# pytest --alluredir=allure-results
# allure serve allure-results
#
# import allure
#
# @allure.feature("User Management")
# @allure.story("Get User")
# def test_get_user_allure():
#     client = UserClient()
#     with allure.step("Send GET request"):
#         response = client.get_user(2)
#     with allure.step("Validate response"):
#         assert response.status_code == 200


# ==============================================================================
# SECTION 15: NEGATIVE & EDGE CASE CHECKLIST
# (what interviewers/reviewers look for)
# ==============================================================================
#
# - Missing/invalid auth token       -> expect 401
# - Malformed JSON body              -> expect 400
# - Missing required fields          -> expect 400/422
# - Invalid data types (str vs int)  -> expect 400
# - Non-existent resource ID         -> expect 404
# - Duplicate resource creation      -> expect 409
# - Boundary values (empty string, max length, negative numbers, 0)
# - SQL/NoSQL injection payloads in fields (security-adjacent testing)
# - Rate limiting                    -> expect 429 after N requests
# - Large payloads / pagination edge cases (page=0, limit=-1)
# - Content-Type mismatches (sending XML when API expects JSON)
# - Idempotency: repeated PUT/DELETE should not error


# ==============================================================================
# SECTION 16: FULL END-TO-END EXAMPLE TEST CLASS
# ==============================================================================

class TestUsersE2E:
    """Realistic grouped test class combining smoke/negative/regression tests."""

    def setup_method(self):
        self.client = UserClient()

    def test_get_single_user_success(self):
        response = self.client.get_user(2)
        assert response.status_code == 200
        data = response.json()["data"]
        assert data["id"] == 2
        assert "@" in data["email"]

    def test_get_user_not_found(self):
        response = self.client.get_user(9999)
        assert response.status_code == 404

    def test_create_and_delete_user(self):
        create_resp = self.client.create_user("QA Bot", "Automation Engineer")
        assert create_resp.status_code == 201
        user_id = create_resp.json()["id"]

        delete_resp = self.client.delete_user(user_id)
        assert delete_resp.status_code == 204

    def test_create_user_missing_field(self):
        payload = {"name": "QA Bot"}  # missing "job"
        response = self.client.post("/users", json=payload)
        # API-dependent: some mock APIs won't validate this, real APIs
        # should typically return 400.
        assert response.status_code in (200, 201, 400)


# ==============================================================================
# SECTION 17: INTERVIEW-STYLE TALKING POINTS (for a 4-YOE role)
# ==============================================================================
#
# - API testing vs UI testing trade-offs (speed, stability, coverage).
# - Test pyramid placement of API tests (more than UI, fewer than unit).
# - Framework design from scratch: client layer, config layer, data layer,
#   reporting layer.
# - Contract testing vs schema validation vs functional testing.
# - Test data management: setup/teardown, fixtures, dedicated test accounts,
#   cleanup scripts.
# - Idempotency testing and why it matters for PUT/DELETE.
# - Testing pagination, filtering, sorting on list endpoints.
# - Shift-left: running API tests in CI on every PR before UI/E2E.
# - Flaky test triage: retries vs root-causing timing/race conditions.


# ==============================================================================
# QUICK REFERENCE: COMMON ASSERTIONS CHEAT SHEET
# ==============================================================================
#
# assert response.status_code == 200
# assert response.headers["Content-Type"] == "application/json; charset=utf-8"
# assert response.json()["data"]["id"] == expected_id
# assert isinstance(response.json()["data"], list)
# assert len(response.json()["data"]) > 0
# assert "error" not in response.json()
# assert response.elapsed.total_seconds() < 2
# assert response.url.endswith("/users/2")


if __name__ == "__main__":
    # Quick manual smoke run without pytest, for demo purposes.
    print("Running a couple of example calls against reqres.in ...")
    client = UserClient()
    r = client.get_user(2)
    print("GET /users/2 ->", r.status_code, r.json()["data"]["email"])

    r = client.create_user("morpheus", "leader")
    print("POST /users ->", r.status_code, r.json()["name"])
