from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    """Page object for the inventory page."""
    # Locator variables defined at class level

    PAGE_TITLE = (By.CLASS_NAME, "title")

    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")

    MENU_BUTTON = (By.ID, "react-burger-menu-btn")

    LOGOUT_LINK = (By.ID, "logout_sidebar_link")

    def get_page_title(self, driver):
        """Returns the page title text."""
        print("Getting page title...")
        try:
            title = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(self.PAGE_TITLE)
            ).text
            print(f"Page title found: {title}")
            return title
        except Exception as e:
            print(f"Error getting page title: {e}")
            return None

    def get_inventory_count(self, driver):
        """Returns the number of inventory items displayed."""
        print("Counting inventory items...")
        try:
            items = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located(self.INVENTORY_ITEMS)
            )
            count = len(items)
            print(f"Inventory item count: {count}")
            return count
        except Exception as e:
            print(f"Error counting inventory items: {e}")
            return 0

    def logout(self, driver):
        """Logs out from the inventory page."""
        print("Logging out...")
        try:
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(self.MENU_BUTTON)
            ).click()
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(self.LOGOUT_LINK)
            ).click()
            print("Logout successful.")
        except Exception as e:
            print(f"Error during logout: {e}")

    def get_current_url(self, driver):
        """Returns the current URL of the page."""
        url = driver.current_url
        print(f"Current URL: {url}")
        return url
