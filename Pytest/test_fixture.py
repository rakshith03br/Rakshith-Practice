import pytest


class TestClass:
    def test_add(self, cl_setup):
        print("Added successfully")
        assert True

    # @pytest.mark.xfail(reason="Expected failure")
    def test_remove(self):
        print("Removed successfully")
        assert False

# @pytest.mark.skip
def test_xyz():
    print("Added successfully")
    assert True


# @pytest.mark.crash
def test_remove():
    print("Removed successfully")
    assert True