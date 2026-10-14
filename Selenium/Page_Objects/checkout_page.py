from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class CheckoutStepOnePage:
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    ZIP_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")

    @staticmethod
    def fill_info(driver, first, last, zip_code):
        '''
        Fills the checkout step-one form and continues
        parameters:
            driver: Selenium web driver
            first: First name
            last: Last name
            zip_code: Zip/postal code
        Raises:
            NoSuchElementException:
            Exception
        '''
        try:
            driver.find_element(*CheckoutStepOnePage.FIRST_NAME).send_keys(first)
            driver.find_element(*CheckoutStepOnePage.LAST_NAME).send_keys(last)
            driver.find_element(*CheckoutStepOnePage.ZIP_CODE).send_keys(zip_code)
            driver.find_element(*CheckoutStepOnePage.CONTINUE_BUTTON).click()
        except (NoSuchElementException, Exception):
            raise
