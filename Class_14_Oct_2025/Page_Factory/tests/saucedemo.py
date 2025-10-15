import pytest

from selenium import webdriver

from ..pages.login_page import LoginPage

from ..pages.inventory_page import InventoryPage


class TestSauceDemo:

    @pytest.fixture
    def driver(self):
        driver = webdriver.Chrome()

        driver.maximize_window()

        yield driver

        driver.quit()

    def login_and_navigate(self, driver):
        login_page = LoginPage(driver)

        login_page.open(driver)

        login_page.login(driver, "standard_user", "secret_sauce")

        return InventoryPage()

    def test_url_contains_inventory(self, driver):
        inventory_page = self.login_and_navigate(driver)

        # Assertion 1: Check URL contains inventory

        assert "inventory" in inventory_page.get_current_url(driver)

    def test_page_title_is_products(self, driver):
        inventory_page = self.login_and_navigate(driver)

        # Assertion 2: Check page title is "Products"

        assert inventory_page.get_page_title(driver) == "Products"

    def test_inventory_items_displayed(self, driver):
        inventory_page = self.login_and_navigate(driver)

        # Assertion 3: Check inventory items are displayed

        assert inventory_page.get_inventory_count(driver) > 0
