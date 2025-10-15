import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class TitleChecker:
    def __init__(self, website_url, expected_title=""):
        print("Opening Chrome browser in headless mode...")
        self.website_url = website_url
        self.expected_title = expected_title
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()

    def navigate(self):
        print(f"Navigating to {self.website_url} ...")
        self.driver.get(self.website_url)
        time.sleep(2)

    def check_title(self):
        actual_title = self.driver.title
        return actual_title
        print(f"Expected Title: {self.expected_title}")
        print(f"Actual Title: {actual_title}")

    def quit(self):
        print("Quitting browser...")
        self.driver.quit()
        print("title.py completed.")

    def run(self):
        print("Starting TitleChecker...")
        self.navigate()
        # self.check_title()

if __name__ == "__main__":
    checker = TitleChecker("https://www.saucedemo.com/", "Swag Labs")
    checker.run()
