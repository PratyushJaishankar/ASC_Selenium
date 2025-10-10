# JavaScriptExecutorDemo: Demonstrates executing JavaScript commands in Selenium
class JavaScriptExecutorDemo:
    def __init__(self):
        print("Initializing Chrome WebDriver...")
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        self.driver = webdriver.Chrome()
        self.By = By

    def navigate(self, url):
        print(f"Navigating to {url} ...")
        self.driver.get(url)

    def perform_js_actions(self):
        import time
        print("Logging in with provided credentials...")
        self.driver.find_element(self.By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(self.By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(self.By.ID, "login-button").click()
        time.sleep(2)
        print("Scrolling to bottom of the page...")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        print("Scrolling to top of the page...")
        self.driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)
        print("Scrolling to footer element...")
        footer = self.driver.find_element(self.By.CLASS_NAME, "footer")
        self.driver.execute_script("arguments[0].scrollIntoView();", footer)
        time.sleep(2)
        print("Highlighting a product element...")
        product = self.driver.find_element(self.By.CLASS_NAME, "inventory_item_name")
        self.driver.execute_script("arguments[0].style.border='3px solid red'", product)
        time.sleep(2)

    def run(self):
        try:
            self.navigate("https://www.saucedemo.com")
            self.perform_js_actions()
            print("JavaScript Executor Demo completed.")
        finally:
            print("Quitting browser...")
            self.driver.quit()

if __name__ == "__main__":
    demo = JavaScriptExecutorDemo()
    demo.run()
