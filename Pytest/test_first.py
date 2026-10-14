import logging

import pytest
import logging

log  = logging.getLogger()
logging.basicConfig(filename='employee.log')

def test_demo():
    log.info('Test first')
    assert 7*7 == 49


def test_demo1():
    log.info('Test second')
    assert 'Python' != "python"


def func(x):
    return x + 1


def test_answer():
    log.info('Success')
    assert func(3) == 4

# Run pytest test case multiple times:
import pytest
@pytest.mark.parametrize('execution_number', range(5))
def run_multiple_times(execution_number):
    assert True
## ===or===
#pip install pytest-repeat
# --count 5

#######################################################################################################

import pytest

process_list = ["a", "b", "c"]


class Test:

    @pytest.mark.parametrize("process_list", process_list)
    def test_1(self, process_list):
        print(process_list)
        assert True

