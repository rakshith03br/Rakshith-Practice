import pytest


@pytest.fixture(scope="session",autouse=True)
def option_setup(browser):
    if browser == "chrome":
        print("Launch chrome")
    elif browser == "Firefox":
        print("Launch firefox")
    else:
        print("Provide valid option")

    print("Login")
    print("Search the product")
    yield
    print("Logoff")
    print("Close application")


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope="session",autouse=True)
def browser(request):
    return request.config.getoption("--browser")
