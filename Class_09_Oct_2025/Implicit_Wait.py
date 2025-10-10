# Implicit_Wait.py - Demonstrates implicit waits in Selenium
# Author: [Your Name]
# Date: 09-Oct-2025

class ImplicitWaitDemo:
    def __init__(self):
        print("[INIT] Initializing Chrome WebDriver...")
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        self.driver = webdriver.Chrome()
        self.By = By
        print("[INIT] WebDriver initialized.")
        print("[STEP] Setting implicit wait to 10 seconds...")
        self.driver.implicitly_wait(10)

    def run(self):
        print("[RUN] Starting Implicit Wait demo...")
        try:
            print("[STEP] Navigating to https://www.saucedemo.com ...")
            self.driver.get("https://www.saucedemo.com")
            print("[STEP] Locating username, password, and login button...")
            username = self.driver.find_element(self.By.ID, "user-name")
            password = self.driver.find_element(self.By.ID, "password")
            login_btn = self.driver.find_element(self.By.ID, "login-button")
            print("[STEP] Entering credentials and logging in...")
            username.send_keys("standard_user")
            password.send_keys("secret_sauce")
            login_btn.click()
            print("[STEP] Login submitted.")
        except Exception as e:
            print(f"[ERROR] Exception occurred: {e}")
        finally:
            print("[END] Quitting browser...")
            self.driver.quit()
            print("[END] Browser closed.")

if __name__ == "__main__":
    print("[MAIN] Running ImplicitWaitDemo...")
    demo = ImplicitWaitDemo()
    demo.run()
    print("[MAIN] ImplicitWaitDemo finished.")
