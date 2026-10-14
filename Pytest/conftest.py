import pytest


# @pytest.fixture(scope="session", autouse=False)
# default scope, the fixture is destroyed at the end of each test_case
# @pytest.fixture(scope="session", autouse=True) # setup first then all test_cases and teardown at the end
def fun_setup():
    print("session Launch the application")
    print("session Login")
    print("session Search the product")
    yield
    print("session Logoff")
    print("session Close application")


# @pytest.fixture(scope="session", autouse=False)
def cl_setup():
    print("class Launch the application")
    print("class Login")
    print("class Search the product")
    yield
    print("class Logoff")
    print("class Close application")


# @pytest.fixture(scope="module", autouse=True)
def mod_setup():
    print("module Launch the application")
    print("module Login")
    print("module Search the product")
    yield
    print("module Logoff")
    print("module Close application")

# @pytest.fixture(scope="function", autouse=False)
def rampdump():
    print("Ramp dump setup")
    yield
    print("Ramp dump teardown")


#####################################################################
# other way to write pytest fixtures

@pytest.fixture(scope="function")
def function_fixture(request):
    print("Setup")

    def teardown():
        print("teardown")
    request.addfinalizer(teardown)

