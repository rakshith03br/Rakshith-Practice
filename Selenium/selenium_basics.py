"""
==================
Selenium WebDriver Notes — Locators & Interview Prep

This file is meant to be read top-to-bottom like study notes, and also
run directly — the runnable sections at the bottom demonstrate each
locator strategy and wait type in actual code.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    NoSuchElementException,
    TimeoutException,
    StaleElementReferenceException,
    ElementClickInterceptedException,)


# ============================================================
# 1. WHAT IS A LOCATOR?
# ============================================================
"""
A locator tells Selenium HOW to find an element in the DOM. It's always
passed as a (strategy, value) pair to find_element() / find_elements().

    driver.find_element(By.ID, "login-button")

In POM, locators are stored as a tuple and unpacked with *:

    LOGIN_BUTTON = (By.ID, "login-button")
    driver.find_element(*LOGIN_BUTTON)
"""


# ============================================================
# 2. THE 8 LOCATOR STRATEGIES  (By class)
# ============================================================
"""
Strategy                 Matches by                  Example
---------------------------------------------------------------------------
By.ID                     id attribute                (By.ID, "login-button")
By.NAME                   name attribute              (By.NAME, "username")
By.CLASS_NAME             a single CSS class          (By.CLASS_NAME, "btn-primary")
By.TAG_NAME               HTML tag                    (By.TAG_NAME, "input")
By.CSS_SELECTOR           any valid CSS selector      (By.CSS_SELECTOR, "h3[data-test='error']")
By.XPATH                  any valid XPath expression  (By.XPATH, "//button[text()='Login']")
By.LINK_TEXT              exact <a> visible text      (By.LINK_TEXT, "Sign up")
By.PARTIAL_LINK_TEXT      partial <a> visible text    (By.PARTIAL_LINK_TEXT, "Sign")

Priority order (most -> least preferred):
    1. By.ID              -> fastest, unique by HTML spec
    2. By.NAME
    3. By.CSS_SELECTOR    -> fast, flexible, readable
    4. By.XPATH           -> most powerful (can go UP the DOM, match by
                              text) but slower / more brittle
    5. By.CLASS_NAME / By.TAG_NAME -> usually too broad alone
"""

# --- Example locators for each strategy ---
LOCATOR_EXAMPLES = {
    "by_id":                (By.ID, "login-button"),
    "by_name":               (By.NAME, "username"),
    "by_class_name":         (By.CLASS_NAME, "btn-primary"),
    "by_tag_name":           (By.TAG_NAME, "input"),
    "by_css_selector":       (By.CSS_SELECTOR, "h3[data-test='error']"),
    "by_xpath":              (By.XPATH, "//button[text()='Login']"),
    "by_link_text":          (By.LINK_TEXT, "Sign up"),
    "by_partial_link_text":  (By.PARTIAL_LINK_TEXT, "Sign"),
}


"""
CSS SELECTOR CHEAT-SHEET
------------------------
#id                     -> id="id"
.class                  -> class="class"
tag[attr='value']       -> exact attribute match
[attr^='value']         -> attribute starts with
[attr$='value']         -> attribute ends with
[attr*='value']         -> attribute contains
div > span              -> direct child
div span                -> any descendant
input:nth-child(2)      -> nth child

XPATH CHEAT-SHEET
-----------------
//tag[@attr='value']            -> exact match
//tag[contains(@attr,'val')]    -> partial match
//tag[text()='Login']           -> exact text match
//tag[contains(text(),'Log')]   -> partial text match
//div[@id='x']//button          -> descendant
//button/parent::div            -> go UP the DOM (CSS can't do this)
//button/following-sibling::*   -> sibling traversal
(//button)[2]                   -> nth match (1-indexed)
"""


# ============================================================
# 3. find_element vs find_elements
# ============================================================
"""
                    find_element                find_elements
Returns             single WebElement            list of WebElement
If nothing found    raises NoSuchElementException returns empty list []
Use case            expect exactly one match      check presence/count,
                                                    or iterate
"""


def element_exists(driver, locator) -> bool:
    """Safe existence check without waiting the full timeout or using
    try/except — find_elements() never throws."""
    return len(driver.find_elements(*locator)) > 0


# ============================================================
# 4. WAITS
# ============================================================
"""
Type        How                                                           Notes
------------------------------------------------------------------------------
Implicit    driver.implicitly_wait(10)                                    Global; polls DOM before
                                                                           NoSuchElementException.
                                                                           Applies to EVERY find call.
Explicit    WebDriverWait(driver, 10).until(EC.element_to_be_clickable)   Targeted wait for one
                                                                           condition on one element.
                                                                           PREFERRED.
Fluent      WebDriverWait(driver, 10, poll_frequency=1,
            ignored_exceptions=[...]).until(EC.element_to_be_clickable)   Explicit wait + configurable
                                                                           poll interval / ignored
                                                                           exceptions.

WARNING: never mix implicit + explicit wait on the same driver instance
-- their timeouts can stack unpredictably.
"""


def wait_for_clickable(driver, locator, timeout=10):
    """Example of an explicit wait using expected_conditions (EC)."""
    return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator))


def wait_for_fluent(driver, locator, timeout=10, poll_frequency=0.5):
    """Example of a fluent wait: same as explicit wait but with a
    configurable polling frequency and ignored exceptions while polling."""
    return WebDriverWait(driver, timeout, poll_frequency=poll_frequency,
                         ignored_exceptions=[NoSuchElementException, StaleElementReferenceException],
                         ).until(EC.presence_of_element_located(locator))


# Common expected_conditions (EC) used day to day:
#   EC.presence_of_element_located(locator)
#   EC.visibility_of_element_located(locator)
#   EC.element_to_be_clickable(locator)
#   EC.invisibility_of_element_located(locator)
#   EC.alert_is_present()
#   EC.url_contains("dashboard")
#   EC.presence_of_all_elements_located(locator)


# ============================================================
# 5. PAGE OBJECT MODEL (POM) — QUICK RECAP
# ============================================================
"""
Selenium/
├── conftest.py
├── pages/
│   ├── base_page.py     -> common reusable actions
│   ├── login_page.py    -> locators + actions for login screen
│   └── ...
└── tests/
    └── test_login.py    -> calls page methods only, never By.* directly

- Locators live as class attributes on the page object.
- Tests never touch By.* directly -- only call page methods
  (login(), add_to_cart()).
- Page methods can return the NEXT page object for fluent chaining:
      inventory_page = login_page.login(user, pwd)
"""


class ExamplePage:
    """Minimal illustrative page object (see the full multi-file
    project for the real BasePage / LoginPage / etc.)."""

    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_login(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()
        return self

    def is_visible(self, locator):
        return bool(self.wait.until(EC.visibility_of_element_located(locator)))

    def get_error_text(self):
        return self.wait.until(EC.visibility_of_element_located(self.ERROR_MESSAGE)).text

    def get_title(self, title):
        self.wait.until(EC.title_is(title))
        return self.driver.title


# ============================================================
# 6. COMMON EXCEPTIONS
# ============================================================
"""
Exception                              Cause
-------------------------------------------------------------------------
NoSuchElementException                 Locator matched nothing
TimeoutException                       Explicit wait condition never
                                        became true in time
StaleElementReferenceException         Element no longer attached to DOM
                                        (page re-rendered)
ElementClickInterceptedException       Another element (overlay/modal)
                                        is covering the target
ElementNotInteractableException        Element found but not visible/
                                        enabled for interaction
"""


def safe_click(driver, locator, retries=3):
    """Retry pattern for StaleElementReferenceException /
    ElementClickInterceptedException."""
    for _ in range(retries):
        try:
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(locator)
            ).click()
            return
        except (StaleElementReferenceException, ElementClickInterceptedException):
            continue
    raise TimeoutException(f"Could not click element: {locator}")


# ============================================================================
# ============================================================================
#            INTERVIEW QUESTIONS & ANSWERS
# ============================================================================
# ============================================================================

INTERVIEW_QA = """
LOCATORS
--------
Q1. CSS Selector vs XPath — which do you prefer and why?
A1. CSS is faster and more readable; use it by default. XPath is
    necessary when you need to go UP the DOM (parent/ancestor) or match
    by visible text — CSS cannot do either natively.

Q2. How do you locate an element that has no id, name, or unique class?
A2. Use a CSS/XPath combination based on a stable ancestor + relative
    position, an attribute like data-testid, partial-match XPath
    (contains(@class,'...')), or text-based XPath if the text is stable.

Q3. How do you handle dynamic locators where the id/class changes on
    every page load (e.g., auto-generated ids)?
A3. Use partial-match selectors: CSS [id^='product-'] /
    [class*='btn-dynamic'], or XPath //button[contains(@id,'submit')].
    Alternatively locate relative to a stable sibling/parent element.

Q4. How do you select the nth matching element?
A4. XPath: (//button)[2]. CSS: :nth-child(2) / :nth-of-type(2) — note
    these count DOM position, not just matches of the same tag.

Q5. Difference between find_element and find_elements?
A5. find_element returns the first match or raises
    NoSuchElementException. find_elements returns a list (empty if no
    match) — useful for existence checks or counting without
    try/except.

Q6. How do you check if an element exists WITHOUT waiting the full
    timeout when it's absent?
A6. len(driver.find_elements(locator)) == 0 — find_elements never
    throws, so there's no wasted wait on a negative case.


WAITS & SYNCHRONIZATION
------------------------
Q7. Implicit vs Explicit vs Fluent wait?
A7. Implicit = global wait applied to every find_element call before
    throwing. Explicit = WebDriverWait + expected_conditions, targeted
    at one condition on one element (preferred). Fluent = explicit wait
    with configurable polling frequency and ignored exceptions — useful
    for intermittently appearing/disappearing elements.

Q8. Why should implicit and explicit waits never be mixed?
A8. Their timeouts stack unpredictably (e.g., an implicit 10s + an
    explicit 10s can, in some driver versions, effectively wait up to
    20s), making test timing inconsistent and hard to debug.

Q9. What causes StaleElementReferenceException and how do you fix it?
A9. The DOM node backing your WebElement reference was removed/replaced
    (e.g., after an AJAX re-render). Fix by re-locating the element
    right before use, or wrapping the interaction in a small retry loop
    instead of caching WebElements long-term.

Q10. How do you handle ElementClickInterceptedException?
A10. Scroll the element into view first (scrollIntoView), wait for any
     overlay/modal to disappear (EC.invisibility_of_element_located),
     or as a last resort click via
     execute_script("arguments[0].click();", el).


FRAMEWORK / POM DESIGN
------------------------
Q11. Why use the Page Object Model?
A11. It separates locators/page actions from test logic. UI changes
     only require updating the page object, not every test. It also
     improves readability (page.login(user, pwd)) and reusability
     across suites.

Q12. How do you avoid duplicating locators across multiple test files?
A12. Store locators as class attributes on the page object only; tests
     call methods, never reference By.* directly. For very large
     suites, some teams externalize locators into a JSON/YAML
     repository.

Q13. How do you structure a Selenium + pytest framework at scale?
A13. pages/ for page objects, tests/ for test cases, conftest.py for
     shared fixtures (driver setup/teardown) and hooks (screenshot on
     failure), pytest.ini for config, plus CI integration with
     --junitxml reports and headless mode.


HANDLING COMMON UI ELEMENTS
------------------------------
Q14. How do you handle a dropdown?
A14. Native <select> -> Select(element).select_by_visible_text(...).
     Custom (div-based) dropdown -> click to open, wait for options to
     render, then click the target option like any normal element.

Q15. How do you handle multiple windows/tabs?
A15. driver.window_handles lists all open handles.
     driver.switch_to.window(handle) moves focus. Store the original
     handle, switch to interact with the new window, then switch back.

Q16. How do you handle iframes?
A16. driver.switch_to.frame(locator/index/name) to enter,
     driver.switch_to.default_content() to return to the main
     document. Elements inside a frame are invisible to Selenium until
     you switch in.

Q17. How do you handle a JS alert/confirm/prompt?
A17. WebDriverWait(driver, 10).until(EC.alert_is_present())
     alert = driver.switch_to.alert
     alert.accept()      # or alert.dismiss() / alert.send_keys(text)

Q18. How do you handle file upload?
A18. If <input type="file"> exists in the DOM (even visually hidden),
     call send_keys(absolute_path) directly — no OS dialog interaction
     needed. For custom widgets with no visible input, unhide it via
     execute_script first.

Q19. When do you use execute_script / JavaScriptExecutor?
A19. When a normal click/send_keys fails due to a hidden/out-of-viewport
     element or an intercepting overlay — e.g., scrollIntoView, forcing
     a JS click, or setting a value on a disabled field. Use as a
     fallback, not the default, since it can mask real user-facing bugs.


TEST STRATEGY & EXECUTION
----------------------------
Q20. How do you reduce flakiness in your test suite?
A20. Use explicit waits, avoid brittle auto-generated locators, isolate
     test data per test, add retries only for known-transient issues
     (stale element, click intercepted — not to mask real bugs), and
     run headless consistently in CI and locally.

Q21. How do you run tests in parallel?
A21. pytest-xdist (pytest -n 4) for local parallel processes; Selenium
     Grid or a cloud grid (BrowserStack/Sauce Labs) for cross-browser/
     OS scale. Each parallel test must get its own driver instance
     (function-scoped fixture) to avoid race conditions.

Q22. driver.close() vs driver.quit()?
A22. close() shuts only the current tab/window. quit() closes all
     windows for that session and ends the WebDriver process. Always
     quit() in teardown to avoid orphaned browser processes.

Q23. How do you integrate Selenium tests into CI/CD?
A23. Run headless, add as a pipeline stage (GitHub Actions/Jenkins/
     GitLab CI), generate JUnit XML (--junitxml=report.xml) for
     pass/fail parsing, archive failure screenshots as build artifacts,
     and gate merge/deploy on suite success.

Q24. How do you implement soft assertions (continue after one assertion
     fails)?
A24. Regular assert stops execution immediately (hard assert). Use a
     plugin like pytest-check, or a custom SoftAssert helper that
     collects failures in a list and raises one combined
     AssertionError at the end.

Q25. How do you capture evidence (screenshots) automatically on
     failure?
A25. A pytest hook (pytest_runtest_makereport) that checks
     report.failed and calls driver.save_screenshot(...), typically
     placed in conftest.py so it applies to every test automatically.

TIP: whenever you answer a "how do you handle X" question, mention the
POM angle — e.g., "I'd put this logic inside the relevant page object's
method, not the test" — it signals framework design maturity expected
at the 4-year level.
================================================================================================
𝗦𝗲𝗹𝗲𝗻𝗶𝘂𝗺 𝗔𝘂𝘁𝗼𝗺𝗮𝘁𝗶𝗼𝗻

• How do you handle dynamic web elements in Selenium?
• What is the difference between implicit, explicit, and fluent waits?
• How do you design a scalable automation framework?
• Explain Page Object Model (POM) with real-time usage.
• How do you handle stale element exceptions?
• How do you run tests in parallel using TestNG?
• How do you handle dropdowns, alerts, and frames?
• How do you capture screenshots on test failure?
• How do you integrate Selenium with CI/CD tools like Jenkins?
• How do you handle browser compatibility testing?
"""


# ============================================================
# 7. RUNNABLE DEMO (optional — run this file directly to see it work)
# ============================================================
if __name__ == "__main__":
    print(INTERVIEW_QA)

    # Uncomment to actually exercise the locator/wait examples in a browser:
    #
    # driver = webdriver.Chrome()
    # driver.get("https://www.saucedemo.com/")
    #
    # driver.find_element(By.ID, "user-name").send_keys("standard_user")
    # driver.find_element(By.ID, "password").send_keys("secret_sauce")
    # safe_click(driver, (By.ID, "login-button"))
    #
    # print("Element exists?", element_exists(driver, (By.CLASS_NAME, "title")))
    #
    # driver.quit()
