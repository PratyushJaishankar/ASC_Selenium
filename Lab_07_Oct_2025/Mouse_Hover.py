# MouseHoverDemo: Demonstrates mouse hover action and color change detection using Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

class MouseHoverDemo:
    # Initialize Chrome WebDriver
    def __init__(self):
        print("Initializing Chrome WebDriver...")
        self.driver = webdriver.Chrome()

    # Navigate to the specified URL
    def navigate(self, url):
        print(f"Navigating to {url} ...")
        self.driver.get(url)

    # Hover over the element and check color change
    def hover_and_check_color(self, selector):
        print(f"Locating element with selector '{selector}' for mouse hover...")
        element = self.driver.find_element(By.CSS_SELECTOR, selector)
        color_before = element.value_of_css_property("color")
        print(f"Color before hover: {color_before}")

        actions = ActionChains(self.driver)
        print("Performing mouse hover...")
        actions.move_to_element(element).perform()
        time.sleep(2)
        color_after = element.value_of_css_property("color")
        print(f"Color after hover: {color_after}")

        if color_before != color_after:
            print("Mouse hover successful, color changed.")
        else:
            print("Mouse hover failed, color did not change.")
        time.sleep(2)

    # Main runner for the demo
    def run(self):
        try:
            self.navigate("https://practice.expandtesting.com/")
            self.hover_and_check_color("a.logo_title")
        finally:
            print("Quitting browser...")
            self.driver.quit()

if __name__ == "__main__":
    demo = MouseHoverDemo()
    demo.run()