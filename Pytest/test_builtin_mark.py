import pytest


@pytest.mark.skip
def test_login():
    print("Login Success")


def test_add():
    print("Added Successfully")


def test_logout():
    print("Logout Success")


@pytest.mark.xfail
def test_assert():
    assert 10 == 11


@pytest.mark.skipif(True, reason="Example conditional skip")
def test_conditional_skip():
    assert False
