import pytest
from selenium import webdriver

from ..pages.login_page import LoginPage

from ..pages.inventory_page import InventoryPage


class TestSauceDemo:
    """Test suite for SauceDemo login and inventory functionality."""
    print("Starting TestSauceDemo class...")

    @pytest.fixture
    def driver(self):
        """Setup and teardown for Chrome WebDriver."""
        print("Setting up Chrome WebDriver...")
        driver = webdriver.Chrome()

        driver.maximize_window()

        yield driver

        print("Quitting Chrome WebDriver...")
        driver.quit()

    def test_successful_login(self, driver):
        """Test for successful login and inventory page validation."""
        print("Running test_successful_login...")
        login_page = LoginPage()
        print("Opening login page...")
        login_page.open(driver)
        print("Logging in with standard_user...")
        login_page.login(driver, "standard_user", "secret_sauce")
        inventory_page = InventoryPage()
        print("Checking if URL contains 'inventory'...")
        assert "inventory" in inventory_page.get_current_url(driver), "URL does not contain 'inventory'!"
        print("URL contains 'inventory'.")
        print("Checking if page title is 'Products'...")
        assert inventory_page.get_page_title(driver) == "Products", "Page title is not 'Products'!"
        print("Page title is 'Products'.")
        print("Checking if inventory items are displayed...")
        assert inventory_page.get_inventory_count(driver) > 0, "No inventory items found!"
        print("Inventory items are displayed.")
