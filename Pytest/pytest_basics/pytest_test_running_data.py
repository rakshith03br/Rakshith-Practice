"""
A single file demonstrating pytest test structures (classes, functions,
markers, parametrization, fixtures) so you can practice every way of
running tests with pytest.

============================================================
 HOW TO RUN THESE TESTS - ALL POSSIBLE WAYS (commands below)
============================================================

1. Run all tests
   pytest
   pytest -v
   pytest -vv

2. Run this specific file
   pytest test_pytest_examples.py

3. Run a specific class
   pytest test_pytest_examples.py::TestLogin

4. Run a specific method inside a class
   pytest test_pytest_examples.py::TestLogin::test_valid_credentials

5. Run a specific standalone function
   pytest test_pytest_examples.py::test_forgot_password

6. Run by keyword expression (-k)
   pytest -k "login"
   pytest -k "login and not admin"
   pytest -k "TestLogin and valid_credentials"
   pytest -k "login or logout"

7. Run by marker (-m)
   pytest -m smoke
   pytest -m "smoke and not slow"
   pytest -m "smoke or regression"
   pytest -m "not slow"

8. Run multiple specific tests (node IDs)
   pytest test_pytest_examples.py::test_forgot_password test_pytest_examples.py::TestLogin::test_invalid_credentials

9. Run a specific parametrized case
   pytest "test_pytest_examples.py::test_is_even[2-True]"
   pytest "test_pytest_examples.py::test_is_even[3-False]"

10. Run last failed / failed first
    pytest --lf
    pytest --ff

11. Stop after first failure / after N failures
    pytest -x
    pytest --maxfail=2

12. Run tests by file + line number
    pytest test_pytest_examples.py:40

13. Preview what would run without executing
    pytest --collect-only
    pytest -k "smoke" --collect-only -q

14. Run in parallel (requires: pip install pytest-xdist)
    pytest -n auto
    pytest -n 4

15. Show available fixtures / setup steps
    pytest --fixtures
    pytest --setup-show

16. Combine directory + keyword
    pytest . -k "post and not delete"

============================================================
"""

import pytest


# ------------------------------------------------------------------
# Register custom markers (normally done in pytest.ini / pyproject.toml,
# shown here as a reference so this file is self-explanatory)
#
# pytest.ini example:
#
# [pytest]
# markers =
#     smoke: quick smoke tests
#     regression: full regression tests
#     slow: long running tests
#     admin: tests related to admin features
# ------------------------------------------------------------------


# ------------------------------------------------------------------
# 1. Standalone functions
# ------------------------------------------------------------------

def test_forgot_password():
    """A simple standalone test function."""
    assert "reset link sent" == "reset link sent"


@pytest.mark.smoke
def test_home_page_loads():
    """Marked as smoke test."""
    assert True


@pytest.mark.slow
def test_generate_large_report():
    """Marked as slow test."""
    result = sum(range(1_000_000))
    assert result > 0


# ------------------------------------------------------------------
# 2. Test class (group related tests)
# ------------------------------------------------------------------

class TestLogin:
    """Groups all login-related tests."""

    @pytest.mark.smoke
    def test_valid_credentials(self):
        username, password = "user1", "correct_password"
        assert username == "user1" and password == "correct_password"

    @pytest.mark.regression
    def test_invalid_credentials(self):
        username, password = "user1", "wrong_password"
        assert password != "correct_password"

    @pytest.mark.admin
    def test_admin_login(self):
        role = "admin"
        assert role == "admin"


class TestLogout:
    """Groups all logout-related tests."""

    def test_logout_clears_session(self):
        session = {"active": True}
        session["active"] = False
        assert session["active"] is False


# ------------------------------------------------------------------
# 3. Parametrized tests
# ------------------------------------------------------------------

@pytest.mark.parametrize("number, expected", [
    (2, True),
    (3, False),
    (10, True),
    (7, False),
])
def test_is_even(number, expected):
    assert (number % 2 == 0) == expected


@pytest.mark.parametrize("a, b, total", [
    (1, 2, 3),
    (5, 5, 10),
    (-1, 1, 0),
])
def test_addition(a, b, total):
    assert a + b == total


# ------------------------------------------------------------------
# 4. Fixtures
# ------------------------------------------------------------------

@pytest.fixture
def sample_user():
    return {"username": "test_user", "role": "member"}


def test_user_role(sample_user):
    assert sample_user["role"] == "member"


# ------------------------------------------------------------------
# 5. Expected failures / skips
# ------------------------------------------------------------------

@pytest.mark.xfail(reason="Known bug, ticket #123")
def test_known_bug():
    assert 1 == 2


@pytest.mark.skip(reason="Not implemented yet")
def test_future_feature():
    assert False


@pytest.mark.skipif(True, reason="Example conditional skip")
def test_conditional_skip():
    assert False
