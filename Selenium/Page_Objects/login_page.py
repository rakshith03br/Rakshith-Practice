import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class LoginPage:
    URL = "https://www.saucedemo.com/"

    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")

    @staticmethod
    def open(driver):
        '''
        Navigates to the login page
        parameters:
            driver: Selenium web driver
        '''
        driver.get(LoginPage.URL)

    @staticmethod
    def login(driver, username, password):
        '''
        Logs in with the given credentials
        parameters:
            driver: Selenium web driver
            username: Username to log in with
            password: Password to log in with
        Raises:
            NoSuchElementException:
            Exception
        '''
        try:
            driver.find_element(*LoginPage.USERNAME_INPUT).clear()
            driver.find_element(*LoginPage.USERNAME_INPUT).send_keys(username)
            driver.find_element(*LoginPage.PASSWORD_INPUT).clear()
            driver.find_element(*LoginPage.PASSWORD_INPUT).send_keys(password)
            driver.find_element(*LoginPage.LOGIN_BUTTON).click()
            time.sleep(2)
        except (NoSuchElementException, Exception):
            raise

    @staticmethod
    def get_error_message(driver):
        '''
        Returns the error message shown after a failed login attempt
        parameters:
            driver: Selenium web driver
        Returns:
            String: error message text
        Raises:
            NoSuchElementException:
            Exception
        '''
        try:
            return driver.find_element(*LoginPage.ERROR_MESSAGE).text
        except (NoSuchElementException, Exception):
            raise
