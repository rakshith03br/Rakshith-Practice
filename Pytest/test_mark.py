import pytest

@pytest.fixture(scope="class")
def config_push_1():
    print("config push 1")

@pytest.fixture(scope="class")
def config_push_2():
    print("config push 2")


@pytest.mark.usefixtures("config_push_1")
class Test_Fixture_1:

    def test_first(self):
        print("First test, class 1")
        assert True

    def test_first_1(self):
        print("First test, class 1")
        assert True

    def test_first_2(self):
        print("First test, class 1")
        assert True


@pytest.mark.usefixtures("config_push_2")
class Test_Fixture_2:

    def test_first(self):
        print("Second test, class 2")
        assert True

    def test_first_1(self):
        print("Second test, class 2")
        assert True
