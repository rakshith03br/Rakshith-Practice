import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class CartPage:
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CART_ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")

    @staticmethod
    def get_item_names(driver):
        '''
        Returns the names of all items currently in the cart
        parameters:
            driver: Selenium web driver
        Returns:
            List: item names
        Raises:
            NoSuchElementException:
            Exception
        '''
        try:
            return [el.text for el in driver.find_elements(*CartPage.CART_ITEM_NAMES)]
        except (NoSuchElementException, Exception):
            raise

    @staticmethod
    def checkout(driver):
        '''
        Clicks the Checkout button
        parameters:
            driver: Selenium web driver
        Raises:
            NoSuchElementException:
            Exception
        '''
        try:
            driver.find_element(*CartPage.CHECKOUT_BUTTON).click()
            time.sleep(1)
        except (NoSuchElementException, Exception):
            raise
