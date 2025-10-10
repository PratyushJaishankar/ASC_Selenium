import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class MultipleTabsDemo:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://google.com")
        time.sleep(2)

    def open_new_tab(self, link_text):
        link = self.driver.find_element(By.LINK_TEXT, link_text)
        link.send_keys(Keys.CONTROL + Keys.RETURN)
        time.sleep(3)

    def close(self):
        print("Using Close")
        self.driver.close()
        time.sleep(2)

    def quit(self):
        print("Using Quit")
        self.driver.quit()


if __name__ == "__main__":
    demo = MultipleTabsDemo()
    demo.open_new_tab("Gmail")
    demo.open_new_tab("Images")
    demo.close()  # Close current tab
    demo.quit()   # Quit the browser