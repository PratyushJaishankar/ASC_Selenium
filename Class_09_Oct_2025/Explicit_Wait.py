# Explicit_Wait.py - Demonstrates explicit waits in Selenium
# Author: Pratyush Jaishankar
# Date: 09-Oct-2025

class ExplicitWaitDemo:
    def __init__(self):
        print("[INIT] Initializing Chrome WebDriver...")
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        self.driver = webdriver.Chrome()
        self.By = By
        self.WebDriverWait = WebDriverWait
        self.EC = EC
        print("[INIT] WebDriver initialized.")

    def run(self):
        print("[RUN] Starting Explicit Wait demo...")
        try:
            print("[STEP] Navigating to https://www.saucedemo.com ...")
            self.driver.get("https://www.saucedemo.com")
            print("[STEP] Logging in...")
            self.driver.find_element(self.By.ID, "user-name").send_keys("standard_user")
            self.driver.find_element(self.By.ID, "password").send_keys("secret_sauce")
            self.driver.find_element(self.By.ID, "login-button").click()
            print("[STEP] Waiting for products to be visible...")
            wait = self.WebDriverWait(self.driver, 10)
            products = wait.until(
                self.EC.visibility_of_element_located((self.By.CLASS_NAME, "inventory_list"))
            )
            print("[STEP] Products are visible.")
            print("[STEP] Waiting for product item to be clickable...")
            product_item = wait.until(
                self.EC.element_to_be_clickable((self.By.CLASS_NAME, "inventory_item_name"))
            )
            product_item.click()
            print("[STEP] Product item clicked.")
        except Exception as e:
            print(f"[ERROR] Exception occurred: {e}")
        finally:
            print("[END] Quitting browser...")
            self.driver.quit()
            print("[END] Browser closed.")

if __name__ == "__main__":
    print("[MAIN] Running ExplicitWaitDemo...")
    demo = ExplicitWaitDemo()
    demo.run()
    print("[MAIN] ExplicitWaitDemo finished.")
