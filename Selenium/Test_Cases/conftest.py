"""
conftest.py
============
Shared pytest fixtures and hooks, auto-discovered by pytest for every
test module under this directory tree — no explicit import needed.
"""

import pytest
from selenium import webdriver
from Selenium.Page_Objects.login_page import LoginPage


def _new_browser():
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless=new")   # uncomment for CI/headless runs
    options.add_argument("--start-maximized")
    return webdriver.Chrome(options=options)


@pytest.fixture
def driver():
    """Creates a fresh browser instance per test (function-scoped),
    which is required for safe parallel execution with pytest-xdist.
    Use this for tests that need to exercise the login flow itself
    (e.g. valid/invalid login) — those can't reuse an already-authenticated
    session."""
    drv = _new_browser()
    yield drv
    drv.quit()


@pytest.fixture(scope="session")
def logged_in_driver():
    """Creates one browser instance for the whole session and logs in once,
    instead of paying the login cost in every test. Use this for tests that
    only need to already be logged in (cart, checkout, etc.)."""
    drv = _new_browser()
    LoginPage.open(drv)
    LoginPage.login(drv, "standard_user", "secret_sauce")
    yield drv
    drv.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Saves a screenshot for every test using the `driver` or
    `logged_in_driver` fixture — on pass or fail — and embeds it into the
    pytest-html report so the final state can be inspected either way."""
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and (report.passed or report.failed):
        driver_fixture = item.funcargs.get("driver") or item.funcargs.get("logged_in_driver")
        if driver_fixture:
            status = "passed" if report.passed else "failed"
            screenshot_path = f"{status}_{item.name}.png"
            driver_fixture.save_screenshot(screenshot_path)
            if pytest_html:
                extra = getattr(report, "extra", [])
                extra.append(pytest_html.extras.png(driver_fixture.get_screenshot_as_base64()))
                report.extra = extra
