import pytest


@pytest.mark.reg
def test_login():
    print("Login Success")


def test_add():
    print("Added Successfully")


@pytest.mark.reg
def test_logout():
    print("Logout Success")


def test_assert():
    assert 10 == 10
