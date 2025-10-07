from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class ScrollDemo:
    def __init__(self):
        print("Initializing Chrome WebDriver...")
        self.driver = webdriver.Chrome()

    def navigate(self, url):
        print(f"Navigating to {url} ...")
        self.driver.get(url)

    def scroll_by_pixel(self, down=1000, up=500):
        print(f"Scrolling down by {down} pixels")
        self.driver.execute_script(f"window.scrollBy(0, {down});")
        time.sleep(2)
        print(f"Scrolling up by {up} pixels")
        self.driver.execute_script(f"window.scrollBy(0, -{up});")
        time.sleep(2)

    def scroll_to_bottom(self):
        print("Scrolling to bottom")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

    def scroll_to_top(self):
        print("Scrolling to top")
        self.driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)

    def scroll_to_element(self, class_name="widget-content"):
        print(f"Scrolling to element with class name '{class_name}'")
        element = self.driver.find_element(By.CLASS_NAME, class_name)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(2)

    def scroll_with_keys(self):
        print("Scrolling using PAGE_DOWN key")
        self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        print("Scrolling using PAGE_UP key")
        self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_UP)
        time.sleep(1)

    def run(self):
        try:
            self.navigate("https://testautomationpractice.blogspot.com/")
            self.scroll_by_pixel()
            self.scroll_to_bottom()
            self.scroll_to_top()
            self.scroll_to_element()
            self.scroll_with_keys()
            print("Scroll Demo completed.")
        finally:
            print("Quitting browser...")
            self.driver.quit()

if __name__ == "__main__":
    demo = ScrollDemo()
    demo.run()