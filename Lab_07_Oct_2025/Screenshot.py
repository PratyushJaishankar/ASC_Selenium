from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

class ScreenshotDemo:
    def __init__(self, username, password):
        print("Initializing Chrome WebDriver...")
        self.driver = webdriver.Chrome()
        self.screenshot_dir = "screenshots"
        self.ensure_screenshot_dir()
        self.username = username
        self.password = password

    def ensure_screenshot_dir(self):
        if not os.path.exists(self.screenshot_dir):
            os.makedirs(self.screenshot_dir)
            print(f"Created directory: {self.screenshot_dir}")

    def take_screenshot(self, filename):
        base, ext = os.path.splitext(filename)
        path = os.path.join(self.screenshot_dir, filename)
        counter = 2

        # Keep incrementing the counter until a unique filename is found
        while os.path.exists(path):
            new_filename = f"{base}-{counter}{ext}"
            path = os.path.join(self.screenshot_dir, new_filename)
            counter += 1

        self.driver.save_screenshot(path)
        print(f"Screenshot saved: {path}")

    def login(self):
        print(f"Attempting login with username='{self.username}' and password='{self.password}'")
        self.driver.find_element(By.ID, "username").send_keys(self.username)
        self.driver.find_element(By.ID, "password").send_keys(self.password)
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(2)
        if "/secure" in self.driver.current_url:
            print("Login successful")
            return True
        else:
            self.take_screenshot("Failed_Login.png")
            print("Login failed")
            return False

    def run(self):
        try:
            self.driver.get("https://practice.expandtesting.com/login")
            time.sleep(2)
            self.login()
        finally:
            print("Quitting browser...")
            self.driver.quit()

if __name__ == "__main__":
    demo = ScreenshotDemo("practice", "SuperSecretPassword!")
    demo.run()
    demo1 = ScreenshotDemo("practice", "")
    demo1.run()
    demo1 = ScreenshotDemo("", "")
    demo1.run()
    demo1 = ScreenshotDemo("", "asdsasd")
    demo1.run()