# RightClickDemo: Demonstrates right-click action and menu verification using Selenium
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

class RightClickDemo:
    # Initialize Chrome WebDriver in headless mode
    def __init__(self):
        print("Initializing Chrome WebDriver in headless mode...")
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=chrome_options)

    # Navigate to the specified URL
    def navigate(self, url):
        print(f"Navigating to {url} ...")
        self.driver.get(url)

    # Perform right-click on the target button
    def perform_right_click(self):
        print("Locating right-click button...")
        right_click_btn = self.driver.find_element(By.CSS_SELECTOR, ".awaken-content-float")
        print("Performing right-click...")
        actions = ActionChains(self.driver)
        actions.context_click(right_click_btn).perform()
        time.sleep(2)

    # Verify if the right-click menu is displayed
    def verify_right_click_menu(self):
        print("Verifying right-click menu...")
        try:
            if self.driver.find_element(By.CSS_SELECTOR, ".menuItems").is_displayed():
                print("Right click menu is displayed")
        except NoSuchElementException:
            print("Right click menu is not displayed")

    # Main runner for the demo
    def run(self):
        try:
            self.navigate("https://www.softwaretestingmentor.com/automation-practice-page-right-click-demo/")
            self.perform_right_click()
            self.verify_right_click_menu()
            print("Right Click Demo completed.")
        finally:
            print("Quitting browser...")
            self.driver.quit()

if __name__ == "__main__":
    demo = RightClickDemo()
    demo.run()
