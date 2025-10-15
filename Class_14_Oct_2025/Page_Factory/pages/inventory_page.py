from seleniumpagefactory import PageFactory

class InventoryPage(PageFactory):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    # ---------- Locators ----------
    page_title = {
        'by': 'class_name',
        'value': 'title'
    }

    inventory_items = {
        'by': 'class_name',
        'value': 'inventory_item'
    }

    menu_button = {
        'by': 'id',
        'value': 'react-burger-menu-btn'
    }

    logout_link = {
        'by': 'id',
        'value': 'logout_sidebar_link'
    }

    # ---------- Page Actions ----------
    def get_page_title(self):
        return self.page_title.text

    def get_inventory_count(self):
        # .inventory_items is a list-like WebElementList
        return len(self.inventory_items)

    def logout(self):
        self.menu_button.click()
        self.logout_link.click()

    def get_current_url(self):
        return self.driver.current_url
