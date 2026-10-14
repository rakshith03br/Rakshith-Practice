import pytest


@pytest.mark.usefixtures("mod_setup")
def test_add(mod_setup):
    print("Added successfully")


def test_remove(mod_setup):
    print("Removed successfully")
