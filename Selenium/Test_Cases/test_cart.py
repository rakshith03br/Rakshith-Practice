import pytest

from Selenium.Page_Objects.inventory_page import InventoryPage
from Selenium.Page_Objects.cart_page import CartPage


@pytest.mark.RUNTEST
class TestCart:

    def test_add_item_to_cart_updates_badge(self, logged_in_driver):
        # InventoryPage.reset_app_state(logged_in_driver)
        InventoryPage.add_backpack_to_cart(logged_in_driver)
        assert InventoryPage.get_cart_count(logged_in_driver) == "1"

    def test_cart_contains_added_item(self, logged_in_driver):
        InventoryPage.reset_app_state(logged_in_driver)
        InventoryPage.add_backpack_to_cart(logged_in_driver)
        InventoryPage.go_to_cart(logged_in_driver)
        assert "Sauce Labs Backpack" in CartPage.get_item_names(logged_in_driver)

    @pytest.mark.parametrize("sort_option", ["Name (Z to A)", "Price (low to high)"])
    def test_sorting_options(self, logged_in_driver, sort_option):
        """Data-driven test example using pytest.mark.parametrize."""
        InventoryPage.reset_app(logged_in_driver)
        InventoryPage.sort_by(logged_in_driver, sort_option)
        assert len(InventoryPage.get_all_product_names(logged_in_driver)) > 0
