"""
Reference Materials:
    1. Youtube Video:
        https://www.youtube.com/watch?v=c7QQab7e_Gs
            GitHub Link: https://github.com/microsoft/playwright-python

    Installation commands:
        python -m pip install pytest-playwright
        python -m playwright install

    Reference UI page for automation:
        http://www.uitestingplayground.com/
"""
import time

def test_click(page):
    page.goto("http://www.uitestingplayground.com/")
    # expect(page).to_have_title(re.compile("Facebook"))
    page.click("text=Click")
    page.click("#badButton")


def test_load_dealy(page):
    page.goto("http://www.uitestingplayground.com/")
    # expect(page).to_have_title(re.compile("Facebook"))
    page.click("text=Load Delay")
    page.click("text=Button Appearing After Delay")


def test_input(page):
    page.goto("http://www.uitestingplayground.com/")
    page.click("text=Text Input")
    page.fill("#newButtonName", "Fill New Name")
    page.click("#updatingButton")
    assert page.inner_text("#updatingButton") == "Fill New Name"


def test_scrollbars(page):
    page.goto("http://www.uitestingplayground.com/")
    page.click("text=Scrollbars")
    page.click("#hidingButton")


def test_sample_app(page):
    page.goto("http://www.uitestingplayground.com/")
    page.click("text=Sample App")
    assert page.inner_text("#loginstatus") == "User logged out."

    page.fill("//input[@placeholder='User Name']", "Tim")
    page.click("#login")

    assert page.inner_text("#loginstatus") == "Invalid username/password"

    page.fill("//input[@placeholder='User Name']", "Tim")
    page.fill("//input[@name='Password']", "pwd")
    page.click("#login")

    assert page.inner_text("#loginstatus") == "Welcome, Tim!"

    page.click("text=Log Out")
    assert page.inner_text("#loginstatus") == "User logged out."

def test_non_breaking_space(page):
    page.goto("/")

    page.click("text=Non-Breaking Space")
    page.click("text=My Button")
    time.sleep(5)

def test_progress_bar(page):
    page.goto("/progressbar")

    page.click("#startButton")
    page.inner_text("#progressBar[aria-valuenow='75']")
    page.click("#stopButton")
    # print(page.inner_text("#result"))
    assert "Result: 0" in page.inner_text("#result")
    time.sleep(3)

