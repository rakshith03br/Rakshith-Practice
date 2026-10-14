
"""
# python -m playwright codegen "https://playwright.dev/"
    This open a browser window and code generator windows. This will generate a code for whatever
        actions that we perform in UI
"""
import re
from playwright.sync_api import Playwright, sync_playwright, expect


def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    page = context.new_page()

    page.goto("https://playwright.dev/")
    page.get_by_role("button", name="Node.js").click()
    page.get_by_role("navigation", name="Main").get_by_role("link", name="Python").click()
    page.get_by_role("link", name="Get started").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    test_run(playwright)
