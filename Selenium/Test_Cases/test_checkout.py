import pytest

from Selenium.Page_Objects.inventory_page import InventoryPage
from Selenium.Page_Objects.cart_page import CartPage
from Selenium.Page_Objects.checkout_page import CheckoutStepOnePage


@pytest.mark.RUNTEST
class TestCheckout:

    def test_end_to_end_checkout_flow(self, logged_in_driver):
        InventoryPage.reset_app_state(logged_in_driver)
        InventoryPage.add_backpack_to_cart(logged_in_driver)

        InventoryPage.go_to_cart(logged_in_driver)
        assert "Sauce Labs Backpack" in CartPage.get_item_names(logged_in_driver)

        CartPage.checkout(logged_in_driver)
        CheckoutStepOnePage.fill_info(logged_in_driver, "John", "Doe", "560001")
