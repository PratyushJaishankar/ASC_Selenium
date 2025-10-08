import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

class DoubleClickDemo:
    def __init__(self):
        print("Initializing Chrome WebDriver in headless mode...")
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=options)

    def navigate(self, url):
        print(f"Navigating to {url} ...")
        self.driver.get(url)

    def perform_double_click(self):
        print("Locating double-click button...")
        double_click_btn = self.driver.find_element(By.CLASS_NAME, "gaBwhe")
        print("Performing double-click...")
        actions = ActionChains(self.driver)
        actions.double_click(double_click_btn).perform()
        time.sleep(2)

    def run(self):
        try:
            self.navigate("https://www.google.com/maps/")
            for i in range(3):
                self.perform_double_click()
            print("Double Click Demo completed.")
        finally:
            print("Quitting browser...")
            self.driver.quit()

if __name__ == "__main__":
    demo = DoubleClickDemo()
    demo.run()
