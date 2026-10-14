import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class InventoryPage:
    PAGE_TITLE = (By.CLASS_NAME, "title")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    ADD_TO_CART_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    RESET_LINK = (By.ID, "reset_sidebar_link")
    CLOSE_MENU_BUTTON = (By.ID, "react-burger-cross-btn")
    all_items = (By.ID, "inventory_sidebar_link")


    @staticmethod
    def reset_app(driver):
        try:
            driver.find_element(*InventoryPage.MENU_BUTTON).click()
            time.sleep(1)
            driver.find_element(*InventoryPage.all_items).click()
            driver.find_element(*InventoryPage.CLOSE_MENU_BUTTON).click()
            time.sleep(1)
            driver.refresh()
            time.sleep(2)
        except (NoSuchElementException, Exception):
            raise

    @staticmethod
    def reset_app_state(driver):
        '''
        Empties the cart via the side menu's "Reset App State" link, so a
        shared/session-scoped browser starts each test from a clean baseline.
        Sauce Demo clears the cart badge on reset but leaves "Remove" button
        labels stale until the page reloads, so this refreshes afterwards.
        parameters:
            driver: Selenium web driver
        Raises:
            NoSuchElementException:
            Exception
        '''
        try:
            driver.find_element(*InventoryPage.MENU_BUTTON).click()
            time.sleep(1)
            driver.find_element(*InventoryPage.RESET_LINK).click()
            driver.find_element(*InventoryPage.CLOSE_MENU_BUTTON).click()
            time.sleep(1)
            driver.refresh()
            time.sleep(2)
        except (NoSuchElementException, Exception):
            raise


    @staticmethod
    def is_loaded(driver):
        '''
        Checks if the inventory (Products) page has loaded
        parameters:
            driver: Selenium web driver
        Returns:
            Boolean: True/False
        '''
        try:
            return driver.find_element(*InventoryPage.PAGE_TITLE).text == "Products"
        except (NoSuchElementException, Exception):
            return False

    @staticmethod
    def sort_by(driver, visible_text):
        '''
        Sorts the product list using the given sort option
        parameters:
            driver: Selenium web driver
            visible_text: Visible text of the sort option to select
        Raises:
            NoSuchElementException:
            Exception
        '''
        try:
            dropdown = driver.find_element(*InventoryPage.SORT_DROPDOWN)
            Select(dropdown).select_by_visible_text(visible_text)
            time.sleep(1)
        except (NoSuchElementException, Exception):
            raise

    @staticmethod
    def add_backpack_to_cart(driver):
        '''
        Adds the Sauce Labs Backpack to the cart
        parameters:
            driver: Selenium web driver
        Raises:
            NoSuchElementException:
            Exception
        '''
        try:
            driver.find_element(*InventoryPage.ADD_TO_CART_BACKPACK).click()
        except (NoSuchElementException, Exception):
            raise

    @staticmethod
    def get_cart_count(driver):
        '''
        Returns the number displayed on the cart badge
        parameters:
            driver: Selenium web driver
        Returns:
            String: cart item count
        Raises:
            NoSuchElementException:
            Exception
        '''
        try:
            return driver.find_element(*InventoryPage.CART_BADGE).text
        except (NoSuchElementException, Exception):
            raise

    @staticmethod
    def get_all_product_names(driver):
        '''
        Returns the names of all products listed on the inventory page
        parameters:
            driver: Selenium web driver
        Returns:
            List: product names
        Raises:
            NoSuchElementException:
            Exception
        '''
        try:
            return [el.text for el in driver.find_elements(*InventoryPage.PRODUCT_NAMES)]
        except (NoSuchElementException, Exception):
            raise

    @staticmethod
    def go_to_cart(driver):
        '''
        Navigates to the cart page
        parameters:
            driver: Selenium web driver
        Raises:
            NoSuchElementException:
            Exception
        '''
        try:
            driver.find_element(*InventoryPage.CART_LINK).click()
            time.sleep(1)
        except (NoSuchElementException, Exception):
            raise
