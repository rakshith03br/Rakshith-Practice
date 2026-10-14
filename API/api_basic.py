"""
======================================================================================
 API AUTOMATION - LEARN FROM SCRATCH
======================================================================================
Brief notes + runnable examples using Python's `requests` library.

How to use this file:
    - Read each numbered section top to bottom (concept -> tiny code example).
    - Run it directly to see live output:   python api_basic.py
    - Examples hit free public test APIs (jsonplaceholder, httpbin, reqres) so you
      can actually execute everything, no credentials needed.

Install once:   pip install requests
======================================================================================
"""

import requests
import time


# ======================================================================================
# 1. WHAT IS AN API / REST API?
# ======================================================================================
# API = a contract that lets one program talk to another over a protocol (usually HTTP).
# REST API = an API built on plain HTTP, where:
#     - each "thing" you operate on (a user, an order, a device) is a RESOURCE
#     - resources have a URL, e.g.  https://api.example.com/users/42
#     - you act on that URL using an HTTP METHOD (GET/POST/PUT/DELETE...)
#     - data is usually exchanged as JSON
#
# So "call the API" really just means: "send an HTTP request to a URL, and read the
# HTTP response". Everything below is just details of how to do that reliably.


# ======================================================================================
# 2. HTTP METHODS (the "verbs")
# ======================================================================================
# GET     -> read data.            Safe, no side effects. No body normally sent.
# POST    -> create new data.      Sends a body (JSON/form) with the new resource.
# PUT     -> replace data fully.   Sends the full updated object.
# PATCH   -> update data partially. Sends only the changed fields.
# DELETE  -> remove data.
#
# Rule of thumb while automating: GET/PUT/DELETE should be repeatable (idempotent) -
# calling them twice gives the same end state. POST is usually NOT - calling it twice
# creates two resources.


# ======================================================================================
# 3. HTTP STATUS CODES - QUICK REFERENCE
# ======================================================================================
# 2xx  Success            200 OK, 201 Created(POST), 204 No Content(PATCH)
# 3xx  Redirect           301 Moved, 302 Found
# 4xx  Client's fault     400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 409 conflit
# 5xx  Server's fault     500 Internal Server Error, 502/503/504 gateway/availability issues
#
# In automation: always assert on status_code FIRST, before touching the response
# body - a 500 response often doesn't even have the JSON shape you expect.


# ======================================================================================
# 4. ANATOMY OF A REQUEST
# ======================================================================================
# A request is made of 4 parts you control:
#   URL      -> https://api.example.com/users/42
#   Headers  -> metadata about the request, e.g. Content-Type, Authorization
#   Params   -> query string added to the URL,  ?page=2&limit=10
#   Body     -> the actual payload, usually JSON, sent with POST/PUT/PATCH
#
# requests.get(url, params={...}, headers={...})
# requests.post(url, json={...}, headers={...})


# ======================================================================================
# 5. YOUR FIRST GET REQUEST
# ======================================================================================
def example_get():
    resp = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    print("status:", resp.status_code)      # 200
    print("json:", resp.json())             # dict parsed from JSON body
    print("raw text:", resp.text[:60], "...")
    print("headers:", resp.headers["Content-Type"])


# ======================================================================================
# 6. YOUR FIRST POST REQUEST (sending a JSON body)
# ======================================================================================
def example_post():
    payload = {"title": "learning APIs", "body": "hello world", "userId": 1}
    resp = requests.post("https://jsonplaceholder.typicode.com/posts", json=payload)
    print("status:", resp.status_code)      # 201 Created
    print("created:", resp.json())          # server echoes back the created object + new id


# ======================================================================================
# 7. QUERY PARAMS vs PATH PARAMS
# ======================================================================================
# Path param  -> part of the URL itself, identifies a specific resource:
#     GET /posts/1                       (1 is the path param)
# Query param -> extra filters/options, appended after "?":
#     GET /comments?postId=1
def example_query_params():
    # requests builds "?postId=1" for you from the params dict - don't hand-build strings
    resp = requests.get("https://jsonplaceholder.typicode.com/comments", params={"postId": 1})
    print("url used:", resp.url)
    print("count:", len(resp.json()))


# ======================================================================================
# 8. HEADERS
# ======================================================================================
# Common ones you'll set yourself in automation:
#   Content-Type: application/json     -> "the body I'm sending is JSON"
#   Accept: application/json           -> "send me JSON back"
#   Authorization: Bearer <token>      -> auth credential (section 9.3)
def example_headers():
    headers = {"Accept": "application/json"}
    resp = requests.get("https://jsonplaceholder.typicode.com/posts/1", headers=headers)
    print("sent headers:", resp.request.headers)   # inspect what was ACTUALLY sent


# ======================================================================================
# 9. AUTHENTICATION - THE 4 KINDS YOU'LL MEET MOST OFTEN
# ======================================================================================

# 9.1 HTTP Basic Auth - username+password encoded straight into the request header.
#     Simple, but credentials go on every single call.
def example_basic_auth():
    from requests.auth import HTTPBasicAuth
    resp = requests.get(
        "https://httpbin.org/basic-auth/testuser/testpass",
        auth=HTTPBasicAuth("testuser", "testpass"),)
    print("status:", resp.status_code)   # 200 if credentials correct
    print(resp.json())


# 9.2 API Key - a fixed secret string, usually sent as a header (sometimes query param).
#     No login step at all - the key itself IS the credential.
def example_api_key():
    headers = {"x-api-key": "demo-key-123"}
    resp = requests.get("https://httpbin.org/headers", headers=headers)
    print(resp.json()["headers"].get("X-Api-Key"))


# 9.3 Bearer Token / OAuth2 - you first exchange credentials for a short-lived TOKEN,
#     then send that token on every later call as "Authorization: Bearer <token>".
#     This is the standard for most modern public APIs.
def example_bearer_token_flow():
    # Step 1: log in / request a token (reqres.in is a free fake-auth test API)
    login_resp = requests.post(
        "https://reqres.in/api/login",
        json={"email": "eve.holt@reqres.in", "password": "cityslicka"},
    )
    print("login status:", login_resp.status_code)
    token = login_resp.json().get("token")
    print("token:", token)

    # Step 2: use the token on subsequent calls (httpbin.org/bearer just echoes back
    # whatever bearer token it received, so it's a reliable way to prove the header
    # round-trips correctly - a real API would instead validate the token itself)
    headers = {"Authorization": f"Bearer {token}"}
    resp = requests.get("https://httpbin.org/bearer", headers=headers)
    print("authenticated call status:", resp.status_code, resp.json())

## Usage of OAuth2
TOKEN_URL = "https://auth.example.com/oauth/token"
API_URL = "https://api.example.com/api/v1/devices"

# 1. Get the token
token_resp = requests.post(TOKEN_URL,
    data={"grant_type": "client_credentials", "scope": "devices.read"},
    auth=("my_client_id", "my_client_secret"),  # sent as Basic auth
    timeout=10,)
token_resp.raise_for_status()
access_token = token_resp.json()["access_token"]

# 2. Call the protected API
resp = requests.get(API_URL,
    headers={"Authorization": f"Bearer {access_token}"},
    timeout=10,)
print(resp.status_code, resp.json())

# 9.4 Session / Cookie based login - typical of WEB APPLICATIONS (not pure APIs):
#     you POST credentials to a login endpoint, the server sets a session cookie,
#     and a requests.Session() object automatically resends that cookie on every
#     later call - you never touch it manually again.
def example_session_login():
    session = requests.Session()          # persists cookies across calls
    # (httpbin has a demo cookie-setting endpoint to illustrate the mechanism)
    session.get("https://httpbin.org/cookies/set/session_id/abc123")
    resp = session.get("https://httpbin.org/cookies")   # cookie auto-attached here
    print("cookies sent back automatically:", resp.json())


# ======================================================================================
# 10. WHY requests.Session() MATTERS FOR AUTOMATION
# ======================================================================================
# requests.get(...) / requests.post(...) each open a brand-new connection and start
# with an EMPTY cookie jar every time - fine for one-off scripts, bad for automation
# where you log in once and then make 100 more calls.
#
# requests.Session() gives you:
#   - cookie persistence (login once, stay logged in - section 9.4)
#   - TCP connection reuse (faster - no repeated handshakes)
#   - a place to set default headers ONCE for every future call:
def example_session_reuse():
    session = requests.Session()
    session.headers.update({"Accept": "application/json"})   # applies to every call below
    r1 = session.get("https://jsonplaceholder.typicode.com/posts/1")
    r2 = session.get("https://jsonplaceholder.typicode.com/posts/2")
    print(r1.status_code, r2.status_code)


# ======================================================================================
# 11. READING A RESPONSE PROPERLY
# ======================================================================================
def inspect_response(resp):
    print("status_code :", resp.status_code)   # int, e.g. 200
    print("ok           :", resp.ok)            # True if status_code < 400
    print("headers      :", dict(resp.headers))
    print("text (raw)   :", resp.text[:80])
    print("json (parsed):", resp.json() if "application/json" in resp.headers.get("Content-Type", "") else "not json")
    print("elapsed      :", resp.elapsed)        # how long the call took - useful for perf checks


# ======================================================================================
# 12. ERROR HANDLING - DON'T LET A BAD RESPONSE CRASH YOUR SCRIPT
# ======================================================================================
def safe_get(url, **kwargs):
    """
    A defensive wrapper - the pattern every real automation framework uses:
    always assume the network/server can misbehave, never assume `resp` exists
    or that `.json()` will parse cleanly.
    """
    try:
        resp = requests.get(url, timeout=10, **kwargs)
        resp.raise_for_status()          # raises HTTPError for 4xx/5xx status codes
        return resp.json(), None
    except requests.exceptions.Timeout:
        return None, "request timed out"
    except requests.exceptions.HTTPError as e:
        return None, f"server returned error: {e}"
    except requests.exceptions.RequestException as e:
        return None, f"request failed: {e}"


# ======================================================================================
# 13. RETRY WITH BACKOFF - SURVIVING FLAKY SERVERS
# ======================================================================================
def get_with_retry(url, max_retries=3, backoff_seconds=2):
    for attempt in range(1, max_retries + 1):
        try:
            resp = requests.get(url, timeout=10)
            if resp.status_code == 200:
                return resp
            print(f"attempt {attempt}: got {resp.status_code}, retrying...")
        except requests.exceptions.RequestException as e:
            print(f"attempt {attempt}: {e}, retrying...")
        time.sleep(backoff_seconds)
    return None   # gave up after max_retries


# ======================================================================================
# 14. BUILDING A REUSABLE API CLIENT (mini wrapper class)
# ======================================================================================
# Real automation frameworks don't call `requests.get(full_url, ...)` everywhere -
# they wrap it once so the base URL, headers, and error handling are consistent.
# This is the same idea used by this repo's own lib/web_services.py, just simplified.
class ApiClient:
    def __init__(self, base_url):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()

    def get(self, path, **kwargs):
        return self._request("get", path, **kwargs)

    def post(self, path, json=None, **kwargs):
        return self._request("post", path, json=json, **kwargs)

    def _request(self, method, path, **kwargs):
        url = f"{self.base_url}/{path.lstrip('/')}"
        resp = self.session.request(method, url, timeout=10, **kwargs)
        return resp


def example_api_client():
    client = ApiClient("https://jsonplaceholder.typicode.com")
    resp = client.get("/posts/1")
    print(resp.status_code, resp.json())


# ======================================================================================
# 15. WRITING ASSERTIONS - TURNING A CALL INTO A TEST
# ======================================================================================
def test_get_single_post():
    resp = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    assert resp.status_code == 200, f"expected 200, got {resp.status_code}"
    data = resp.json()
    assert data["id"] == 1
    assert "title" in data
    print("test_get_single_post passed")


# ======================================================================================
# 16. USING pytest (how this looks as a real test file)
# ======================================================================================
# In a real project, the above test would live in its own file, e.g. test_posts.py,
# and pytest auto-discovers any function named test_*:
#
#     import requests
#
#     def test_get_single_post():
#         resp = requests.get("https://jsonplaceholder.typicode.com/posts/1")
#         assert resp.status_code == 200
#         assert resp.json()["id"] == 1
#
# Run it with:   pytest test_posts.py -v
#
# Fixtures (setup/teardown) are how you share a logged-in session across many tests:
#
#     import pytest
#
#     @pytest.fixture(scope="session")
#     def api_client():
#         client = ApiClient("https://api.example.com")
#         # do login here once
#         return client
#
#     def test_something(api_client):
#         resp = api_client.get("/some/endpoint")
#         assert resp.status_code == 200


# ======================================================================================
# 17. HOW THIS SCALES UP IN A REAL FRAMEWORK (this repo, for reference)
# ======================================================================================
# lib/web_services.py in this repo is exactly the ApiClient idea from section 14,
# grown up:
#   - one requests.Session() shared across the whole test run (section 10)
#   - a single `session_exec()` method ALL calls go through (section 14's `_request`)
#   - centralised error handling (section 12) and retry-with-backoff (section 13)
#   - login once (section 9.3/9.4 style flows) to populate session cookies/tokens,
#     then every later call reuses that same session automatically
# Once these fundamentals feel natural, that file will read as "the same ideas,
# just applied consistently across ~500 endpoints" rather than anything new.


# ======================================================================================
# 18. CHEAT SHEET
# ======================================================================================
# - GET = read, POST = create, PUT = replace, PATCH = partial update, DELETE = remove
# - Always check resp.status_code before touching resp.json()
# - Use requests.Session() the moment you have more than one call to make
# - json=payload sets Content-Type automatically; data=payload sends form-encoded
# - resp.raise_for_status() turns a bad status code into a Python exception
# - Never hardcode secrets/tokens in source - use env vars / a secrets manager
# - auth types: Basic (user+pass) -> API Key (fixed header) -> Bearer/OAuth2 (token
#   from a login call) -> Cookie/Session (browser-style login)


if __name__ == "__main__":
    print("\n--- 5. GET ---")
    example_get()

    print("\n--- 6. POST ---")
    example_post()

    print("\n--- 7. Query params ---")
    example_query_params()

    print("\n--- 8. Headers ---")
    example_headers()

    print("\n--- 9.1 Basic auth ---")
    example_basic_auth()

    print("\n--- 9.2 API key ---")
    example_api_key()

    print("\n--- 9.3 Bearer token flow ---")
    example_bearer_token_flow()

    print("\n--- 9.4 Session/cookie login ---")
    example_session_login()

    print("\n--- 10. Session reuse ---")
    example_session_reuse()

    print("\n--- 14. API client wrapper ---")
    example_api_client()

    print("\n--- 15. Assertion-based test ---")
    test_get_single_post()


# ======================================================================================
#  INTERVIEW QUESTIONS - API AUTOMATION
# ======================================================================================
# Organized by topic. Answers are intentionally concise - back them up with your own
# real project examples in an actual interview.
#
# ---------------------------------------------------------------------
# A. HTTP / REST FUNDAMENTALS
# ---------------------------------------------------------------------
# Q1: What is the difference between PUT and PATCH?
# A:  PUT replaces the ENTIRE resource - you send the full object, and any field
#     you omit may get reset/nulled by the server. PATCH updates only the fields
#     you send, leaving the rest untouched. PUT is idempotent; PATCH may or may
#     not be, depending on the API.
#
# Q2: What does "idempotent" mean, and which HTTP methods are idempotent?
# A:  An idempotent operation produces the same end state no matter how many
#     times you repeat it with the same input. GET, PUT, DELETE, HEAD, OPTIONS
#     are idempotent by spec; POST (and often PATCH) is not - calling POST twice
#     usually creates two resources instead of one.
#
# Q3: 401 vs 403 - what's the difference?
# A:  401 Unauthorized = you are not authenticated at all (missing/invalid
#     credentials). 403 Forbidden = you ARE authenticated, but you don't have
#     permission for this specific resource/action.
#
# Q4: What's the difference between a query parameter and a path parameter?
# A:  A path param identifies WHICH resource and is part of the URL structure
#     itself (/users/42 - required). A query param is optional filtering/
#     pagination/sorting info appended after "?" (?page=2&limit=10).
#
# Q5: REST vs SOAP, briefly?
# A:  REST is resource-oriented, uses plain HTTP verbs/status codes, typically
#     JSON, and is lightweight. SOAP is a stricter XML-based protocol with its
#     own envelope and formal contract (WSDL), common in older enterprise
#     systems. REST is simpler and dominant in modern APIs.
#
# ---------------------------------------------------------------------
# B. requests / PYTHON AUTOMATION SPECIFICS
# ---------------------------------------------------------------------
# Q6: What's the difference between data= and json= in requests.post()?
# A:  json=payload serializes a dict to a JSON string AND sets
#     "Content-Type: application/json" automatically. data=payload sends
#     form-encoded data ("application/x-www-form-urlencoded") unless you pass a
#     raw string/bytes, in which case it's sent as-is.
#
# Q7: Why use requests.Session() instead of calling requests.get()/post()
#     directly every time?
# A:  A Session persists cookies (so you don't have to re-login every call),
#     reuses the underlying TCP connection (faster, less overhead), and lets you
#     set default headers/auth ONCE instead of repeating them on every call.
#
# Q8: How do you handle a request that might hang forever?
# A:  Always pass timeout=. Without it, requests waits indefinitely if the
#     server never responds. Catch requests.exceptions.Timeout separately from
#     other request exceptions so you can retry or fail fast appropriately.
#
# Q9: What does resp.raise_for_status() do?
# A:  Raises an HTTPError if the status code is 4xx/5xx; does nothing on
#     2xx/3xx. In test automation you usually prefer an explicit
#     `assert resp.status_code == 200` instead, so a failure shows up as a clean
#     test assertion failure rather than a raw exception.
#
# Q10: How do you debug what was ACTUALLY sent in a request?
# A:   Inspect resp.request.headers, resp.request.body, and resp.request.url
#      after the call - requests stores the fully-prepared request object on
#      every response, which is invaluable when headers/auth aren't behaving as
#      expected.
#
# ---------------------------------------------------------------------
# C. AUTHENTICATION
# ---------------------------------------------------------------------
# Q11: Explain the OAuth2 client_credentials grant in your own words.
# A:   A machine-to-machine flow with no human/browser involved - you POST a
#      client_id + client_secret (+ grant_type=client_credentials) to a token
#      endpoint, the server returns a short-lived bearer access_token, and you
#      attach that as "Authorization: Bearer <token>" on every later call until
#      it expires.
#
# Q12: What is a JWT and why is it popular for APIs?
# A:   A JSON Web Token is a self-contained, signed token with 3 base64 parts
#      (header, payload, signature). The server can verify it hasn't been
#      tampered with using the signature alone, without a database lookup, and
#      the payload can carry claims (user id, role, expiry) directly - which
#      makes it fast to validate at scale.
#
# Q13: What is CSRF and how do APIs typically defend against it?
# A:   Cross-Site Request Forgery - tricking a logged-in user's browser into
#      firing a request to a site it's authenticated on. A common defense is the
#      "double-submit cookie": the server sets a token in a cookie and requires
#      that SAME value echoed back in a custom header (e.g. X-XSRF-TOKEN) on
#      state-changing calls - a cross-site attacker's page can't read the cookie
#      to copy it into the header.
#
# Q14: How would you securely store and use an API token in a test automation
#      framework? What would you NOT do?
# A:   Store it in environment variables, a secrets manager, or a CI/CD secret
#      store - never hardcode it in source control. Load it at runtime, mask it
#      in logs, and scope test-only tokens narrowly rather than reusing
#      production credentials.
#
# ---------------------------------------------------------------------
# D. TEST DESIGN / FRAMEWORK
# ---------------------------------------------------------------------
# Q15: How do you structure API automation so 500 endpoints don't turn into 500
#      copy-pasted request calls?
# A:   Build one thin wrapper/client class that owns the Session, base URL, and
#      default headers/auth, and route every call through one core
#      request()/session_exec() method. Each endpoint method just builds the
#      URL/payload and calls that shared method - error handling, retries, and
#      auth attachment live in exactly one place.
#
# Q16: How do you validate a JSON response beyond just the status code?
# A:   Check the specific keys/values you actually depend on
#      (assert data["id"] == 1), and for larger payloads use schema validation
#      (e.g. the jsonschema library) so a field being silently removed or
#      retyped by the backend fails the test instead of passing by accident.
#
# Q17: How would you handle flaky tests caused by a slow/eventually-consistent
#      backend (e.g. an async job that isn't done yet)?
# A:   Poll with a bounded wait-and-retry loop (check status, sleep, repeat up
#      to a timeout) instead of one fixed sleep(). Fail with a clear message if
#      the timeout is exceeded, and keep the poll interval reasonable so tests
#      aren't needlessly slow when the condition is met quickly.
#
# Q18: What's the difference between a mock and a real integration test, and
#      when do you use each?
# A:   A mock/stub simulates the API response without hitting the real service
#      - fast, deterministic, good for testing your OWN code's handling of edge
#      cases (e.g. a simulated 500). An integration test hits the real API -
#      slower, but the only way to catch real contract breaks (backend changed a
#      field name, auth flow changed). Good suites use both.
#
# Q19: How do you avoid one test's data affecting another test (test
#      isolation)?
# A:   Create fresh test data per test/run rather than relying on shared fixed
#      records, clean up (DELETE) what you created in teardown/fixture
#      finalizers, and avoid asserting on absolute shared state (e.g. "there are
#      exactly 5 users") - assert on the delta/thing you created instead.
#
# Q20: How do you handle pagination when testing a list endpoint?
# A:   Follow the API's pagination contract (page/limit, or a next cursor/link
#      in the response) in a loop until there's no next page, rather than
#      assuming all results fit on one page - a common bug is a test that only
#      checks page 1 and misses data further in.
#
# ---------------------------------------------------------------------
# E. DEBUGGING / REAL-WORLD SCENARIOS
# ---------------------------------------------------------------------
# Q21: A test that logs in and then calls an endpoint suddenly starts failing
#      with 401 on the second call, even though login itself returned 200. How
#      do you debug it?
# A:   Check whether the session/cookie or auth header is actually being
#      carried into the second call - a common cause is using a fresh
#      requests.get() instead of the authenticated Session, or the token/cookie
#      having a very short expiry that ran out between calls. Inspect
#      resp.request.headers on the failing call to see exactly what auth was (or
#      wasn't) sent.
#
# Q22: An API call that used to take 200ms now takes 8 seconds and eventually
#      times out. What do you check?
# A:   Whether it's the SERVER being slow (check server-side logs/metrics, is
#      the backend under load or mid-sync?) vs a client-side issue (DNS
#      resolution, no connection pooling because a new Session is created every
#      call, or a network/proxy problem). Also check if the response body
#      indicates a "busy/retry" condition that your own retry logic is silently
#      looping on.
#
# Q23: How would you test that an API correctly rejects invalid input
#      (negative testing)?
# A:   Send deliberately malformed/missing/wrong-typed fields and boundary
#      values (empty string, huge numbers, wrong data types), and confirm you
#      get an appropriate 4xx with a clear error message - not a 500 (which
#      would indicate unsafe backend validation) and not a silent 200 with bad
#      data accepted.
#
# Q24: How do you integrate API automation into CI/CD, and what do you do about
#      tests that depend on external/flaky third-party services?
# A:   Run the suite on every PR/merge (or nightly for longer-running ones),
#      fail the build on test failure, and publish a report. For flaky
#      externally-dependent calls, isolate/mock the external dependency where
#      possible, or tag those tests separately (e.g. "flaky"/"external") so they
#      don't block the whole pipeline while still being tracked.
#
# Q25: Tell me about a bug you found through API testing that wouldn't have
#      been caught through the UI.
# A:   (Answer with your own real example - interviewers want a concrete story
#      here.) Good structure: what you were testing -> what looked off in the
#      raw response (wrong field, wrong status code, a race condition between
#      two calls) -> how you confirmed it was a real backend bug, not a test bug
#      -> the fix/impact.
# ======================================================================================
"""
𝗔𝗣𝗜 𝗧𝗲𝘀𝘁𝗶𝗻𝗴 

• What is REST API and how is it different from SOAP?
• How do you validate API response status codes?
• What are the commonly used HTTP methods?
• How do you perform API testing using Postman or Rest Assured?
• How do you validate JSON response data?
• What is authentication? Explain Basic, Bearer Token, and OAuth.
• How do you test negative scenarios in APIs?
• How do you automate API test cases?
• What is contract testing?
• How do you integrate API tests into automation frameworks?
"""
