import requests

req_obj = requests.get('https://www.google.com/', stream=True)
print(req_obj)
print(req_obj.status_code)
print(req_obj.headers)
print(req_obj.content)
print(req_obj.text)
print(req_obj.url)


## ==========================================================
## ADDITIONAL NOTES FOR INTERVIEW PREPARATION
## ==========================================================
# NOTE: network-dependent examples below are written to be run in an
# environment with internet access. They are commented with expected
# behavior/output so you can study them even without executing every line.

# -------------------------
# 1. requests.Response object - the key attributes/methods, explained
# -------------------------
"""
response.status_code   -> int, e.g. 200, 404, 500
response.headers        -> dict-like (case-insensitive) of response headers
response.text            -> response body decoded as a STRING (using detected/guessed encoding)
response.content          -> response body as raw BYTES (undecoded)
response.json()            -> parses body as JSON, returns dict/list (raises if not valid JSON)
response.url                 -> the FINAL url (after any redirects were followed)
response.history               -> list of Response objects that led to this one via redirects
response.elapsed                -> timedelta - how long the request took
response.encoding                -> the encoding used to decode .text
response.cookies                  -> cookies set by the server in this response
response.request                   -> the PreparedRequest object that was actually sent
"""

print(f"{'*' * 70}")

# -------------------------
# 2. .text vs .content - the crucial difference (VERY common interview question)
# -------------------------
# .content -> raw bytes, exactly as received over the wire (no decoding applied)
# .text    -> requests tries to DECODE .content into a str, using the encoding
#             from response headers (or its own guess if headers don't specify one)
#
# WHEN TO USE WHICH:
#   - Use .text for HTML/JSON/plain text responses you want as a Python string
#   - Use .content for BINARY data (images, PDFs, zip files) - decoding binary
#     data as text would corrupt it / raise a UnicodeDecodeError
"""
image_response = requests.get('https://example.com/photo.jpg')
with open('photo.jpg', 'wb') as f:       # 'wb' = write BINARY mode
    f.write(image_response.content)        # MUST use .content for binary data, not .text
"""

print(f"{'*' * 70}")

# -------------------------
# 3. GET with query parameters - the 'params' argument (avoids manual URL string-building)
# -------------------------
"""
response = requests.get(
    'https://api.example.com/search',
    params={'q': 'python', 'page': 2}
)
print(response.url)   # 'https://api.example.com/search?q=python&page=2'
# requests handles URL-encoding automatically - safer than building the query
# string yourself with string concatenation (which risks encoding bugs).
"""

print(f"{'*' * 70}")

# -------------------------
# 4. POST requests - sending form data vs JSON (a common real-world confusion point)
# -------------------------
"""
# Sending FORM-encoded data (Content-Type: application/x-www-form-urlencoded)
response = requests.post('https://api.example.com/login', data={'username': 'bob', 'password': 'secret'})

# Sending JSON data (Content-Type: application/json) - MUCH more common for modern REST APIs
response = requests.post('https://api.example.com/users', json={'name': 'Alice', 'age': 30})
# Using json= automatically:
#   1. Serializes the dict to a JSON string
#   2. Sets the Content-Type header to 'application/json' for you
# Using data= with a dict instead would send FORM-encoded data, which many
# JSON APIs would reject or misinterpret - this is a classic real bug.
"""

print(f"{'*' * 70}")

# -------------------------
# 5. Custom headers - commonly needed for auth tokens, content negotiation, etc.
# -------------------------
"""
headers = {
    'Authorization': 'Bearer YOUR_TOKEN_HERE',
    'Accept': 'application/json',
    'User-Agent': 'MyApp/1.0'
}
response = requests.get('https://api.example.com/profile', headers=headers)
"""

print(f"{'*' * 70}")

# -------------------------
# 6. Timeouts - ALWAYS set one in production code (a real-world best practice
#    that's frequently tested in interviews)
# -------------------------
"""
try:
    response = requests.get('https://api.example.com/data', timeout=5)   # 5 seconds
except requests.exceptions.Timeout:
    print("Request timed out!")

# You can also set separate connect and read timeouts:
response = requests.get('https://api.example.com/data', timeout=(3, 10))  # (connect_timeout, read_timeout)
"""
# WHY THIS MATTERS: without a timeout, requests.get() will wait INDEFINITELY
# if the server never responds - this can hang your entire application. This
# is one of the most commonly cited "gotchas" in real production code reviews.

print(f"{'*' * 70}")

# -------------------------
# 7. Exception handling - the requests exception hierarchy
# -------------------------
"""
requests.exceptions.RequestException        <- base class for ALL requests exceptions
 ├── requests.exceptions.ConnectionError      -> DNS failure, refused connection, etc.
 ├── requests.exceptions.Timeout                -> request timed out
 │    ├── requests.exceptions.ConnectTimeout
 │    └── requests.exceptions.ReadTimeout
 ├── requests.exceptions.HTTPError                -> raised by raise_for_status() on 4xx/5xx
 └── requests.exceptions.TooManyRedirects            -> exceeded max redirect limit

try:
    response = requests.get('https://api.example.com/data', timeout=5)
    response.raise_for_status()   # raises HTTPError if status is 4xx or 5xx
except requests.exceptions.HTTPError as e:
    print(f"HTTP error: {e}")
except requests.exceptions.ConnectionError:
    print("Failed to connect")
except requests.exceptions.Timeout:
    print("Request timed out")
except requests.exceptions.RequestException as e:
    print(f"Some other requests error: {e}")   # catch-all for anything else
"""

print(f"{'*' * 70}")

# -------------------------
# 8. IMPORTANT GOTCHA: requests does NOT raise an exception for 4xx/5xx
#    status codes by default - you must call raise_for_status() explicitly
# -------------------------
"""
response = requests.get('https://api.example.com/does-not-exist')
print(response.status_code)   # 404 -> but NO EXCEPTION was raised automatically!
if response.status_code == 404:
    print("Not found - handled manually")

# raise_for_status() is the standard way to convert a bad status code into
# an actual exception you can catch:
response.raise_for_status()   # raises requests.exceptions.HTTPError only if status >= 400
"""

print(f"{'*' * 70}")

# -------------------------
# 9. Sessions - reusing connections/cookies across multiple requests
#    (a significant performance + convenience feature many candidates miss)
# -------------------------
"""
with requests.Session() as session:
    session.headers.update({'Authorization': 'Bearer TOKEN'})   # applied to ALL requests in this session

    login_response = session.post('https://api.example.com/login', json={'user': 'bob', 'pass': 'secret'})
    # cookies set by the login response are AUTOMATICALLY reused in subsequent requests:
    profile_response = session.get('https://api.example.com/profile')

# WHY use a Session instead of plain requests.get()/post() calls:
#   1. Reuses the underlying TCP connection (connection pooling) - faster
#      for multiple requests to the same host
#   2. Automatically persists cookies between requests (like a real browser session)
#   3. Lets you set default headers/auth ONCE for all requests made through it
"""

print(f"{'*' * 70}")

# -------------------------
# 10. Streaming large responses (your original code uses stream=True - here's WHY)
# -------------------------
"""
# stream=True delays downloading the response BODY until you actually access
# it - useful for LARGE files, so you don't load the whole thing into memory at once.
response = requests.get('https://example.com/large-file.zip', stream=True)
with open('large-file.zip', 'wb') as f:
    for chunk in response.iter_content(chunk_size=8192):   # read in 8KB chunks
        f.write(chunk)
# Without stream=True, requests.get() downloads the ENTIRE response body
# immediately into memory - fine for small responses (like a webpage), but
# potentially a MemoryError for a large file.
"""

print(f"{'*' * 70}")

# -------------------------
# 11. Authentication helpers - built-in support for common auth schemes
# -------------------------
"""
from requests.auth import HTTPBasicAuth

# Basic auth - shorthand tuple form:
response = requests.get('https://api.example.com/data', auth=('username', 'password'))
# Equivalent, more explicit form:
response = requests.get('https://api.example.com/data', auth=HTTPBasicAuth('username', 'password'))
"""

print(f"{'*' * 70}")

# -------------------------
# 12. Retries with backoff - production-grade resilience (via urllib3's Retry,
#     mounted onto a requests Session)
# -------------------------
"""
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

retry_strategy = Retry(
    total=3,                          # retry up to 3 times
    backoff_factor=1,                   # wait 1s, 2s, 4s... between retries
    status_forcelist=[429, 500, 502, 503, 504]   # only retry on these status codes
)
adapter = HTTPAdapter(max_retries=retry_strategy)
session = requests.Session()
session.mount("https://", adapter)     # apply retry logic to all HTTPS requests through this session
session.mount("http://", adapter)

response = session.get('https://api.example.com/data')
"""

print(f"{'*' * 70}")

# -------------------------
# 13. Common gotcha: .json() raises if the response body isn't valid JSON
# -------------------------
"""
response = requests.get('https://api.example.com/maybe-json')
try:
    data = response.json()
except requests.exceptions.JSONDecodeError:
    print("Response was not valid JSON:", response.text)
"""

print(f"{'*' * 70}")

# -------------------------
# 14. requests vs httpx/aiohttp - a common "what would you use instead" follow-up
# -------------------------
"""
requests   -> synchronous only, the most widely used, simplest API, huge ecosystem
httpx      -> supports BOTH sync and async, requests-like API, HTTP/2 support
aiohttp    -> async-first, commonly used for high-concurrency async applications
             (e.g., inside an asyncio event loop, making many concurrent requests)

Interview angle: if you need to make THOUSANDS of concurrent HTTP calls
efficiently (e.g., a web scraper hitting many URLs), plain 'requests' would
block one call at a time - httpx (async mode) or aiohttp would let you run
many requests CONCURRENTLY within a single thread via asyncio.
"""


## ==========================================================
## INTERVIEW QUESTIONS ON THE PYTHON REQUESTS LIBRARY
## ==========================================================

# 1. What is the difference between response.text and response.content? When
#    would using the wrong one cause a bug (e.g., saving a downloaded image)?
#
# 2. Does requests raise an exception automatically when the server returns a
#    4xx or 5xx status code? How would you make it raise one?
#
# 3. What does response.raise_for_status() do, and what exception type does
#    it raise?
#
# 4. Why is it important to always pass a `timeout` argument to requests.get()
#    /post() in production code? What happens if you don't?
#
# 5. What is the difference between passing data={...} versus json={...} to
#    requests.post()? How does each affect the Content-Type header and the
#    request body format?
#
# 6. What is a requests.Session, and what THREE practical benefits does it
#    provide over making individual requests.get()/post() calls?
#
# 7. What does stream=True do when making a GET request? Why would you use it
#    when downloading a large file?
#
# 8. What is the exception hierarchy in the requests library? Name at least
#    three specific exception types and what triggers each.
#
# 9. How would you add retry logic with exponential backoff to a requests
#    Session, so that failed requests (e.g., 503 errors) are automatically
#    retried?
#
# 10. What does response.json() do, and what happens if the response body is
#     not valid JSON?
#
# 11. How would you pass query parameters to a GET request without manually
#     building the URL string yourself (and why is that safer)?
#
# 12. What is response.history used for? In what scenario would a Response
#     object have a non-empty history list?
#
# 13. How would you send a custom Authorization header (e.g., a Bearer token)
#     with a request?
#
# 14. What is the difference between the synchronous `requests` library and
#     async alternatives like `httpx` (async mode) or `aiohttp`? When would
#     you need an async HTTP client instead of requests?
#
# 15. If you're making many requests to the SAME host, why would using a
#     Session object be more efficient than making separate requests.get()
#     calls each time?
#
# 16. What does response.elapsed tell you, and how might you use it to detect
#     slow API endpoints in a monitoring/logging context?
#
# 17. How would you send a file upload using requests (multipart/form-data)?
#
# 18. What's the difference between requests.get(url, auth=('user','pass'))
#     and manually setting an 'Authorization' header yourself? Are they
#     ultimately equivalent for Basic Auth?
#
# 19. If a server response is gzip-compressed, does requests automatically
#     decompress it before you access .content or .text?
#
# 20. How would you mock/test code that calls requests.get() in a unit test,
#     without making a real network call? (Hint: think about libraries like
#     `responses` or `unittest.mock`.)