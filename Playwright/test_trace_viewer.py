
"""
# python -m playwright show-trace C:\Users\rbr100\Practice\trace.zip
    Command to view the trace viewer data
"""
import re
from playwright.sync_api import Playwright, sync_playwright, expect


def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Start tracing before creating / navigating a page.
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page = context.new_page()

    page.goto("https://playwright.dev/")
    page.get_by_role("button", name="Node.js").click()
    page.get_by_role("navigation", name="Main").get_by_role("link", name="Python").click()
    page.get_by_role("link", name="Get started").click()

    # Stop tracing and export it into a zip archive.
    context.tracing.stop(path="trace.zip")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    test_run(playwright)
