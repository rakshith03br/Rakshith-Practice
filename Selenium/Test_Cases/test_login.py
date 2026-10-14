import pytest

from Selenium.Page_Objects.login_page import LoginPage
from Selenium.Page_Objects.inventory_page import InventoryPage


@pytest.mark.RUNTEST
class TestLogin:

    def test_valid_login(self, driver):
        LoginPage.open(driver)
        LoginPage.login(driver, "standard_user", "secret_sauce")
        assert InventoryPage.is_loaded(driver)

    def test_invalid_login_shows_error(self, driver):
        LoginPage.open(driver)
        LoginPage.login(driver, "locked_out_user", "secret_sauce")
        assert "locked out" in LoginPage.get_error_message(driver).lower()

"""
# pip install pytest-html
# pytest .\Test_Cases\test_login.py --html=.\report.html -v
    command to run test case and generate html report

---------------------------------------------------------------------------
# pip install pytest-xdist
#  pip install pytest pytest-xdist selenium
#  pytest your_tests.py -n 4        # 4 parallel workers        
                                                   
"""
