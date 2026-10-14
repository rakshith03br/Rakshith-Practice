import pytest


@pytest.mark.crash
class TestClass:

    @pytest.mark.skip
    def test_add(self):
        print("Added successfully")

    @pytest.mark.skip
    def test_remove(self):
        print("Removed successfully")
