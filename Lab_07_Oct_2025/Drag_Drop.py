from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common import NoSuchElementException
import time

class DragDropDemo:
    def __init__(self):
        print("Initializing Chrome WebDriver...")
        self.driver = webdriver.Chrome()
        self.actions = ActionChains(self.driver)

    def navigate(self, url):
        print(f"Navigating to {url} ...")
        self.driver.get(url)

    def find_elements(self):
        print("Locating source and target elements...")
        sources = [
            self.driver.find_element(By.ID, "angular"),
            self.driver.find_element(By.ID, "mongo"),
            self.driver.find_element(By.ID, "node")
        ]
        target = self.driver.find_element(By.ID, "droparea")
        print("Elements located.")
        return sources, target

    def drag_and_drop(self, source, target):
        print(f"Dragging '{source.get_attribute('id')}' to drop area...")
        self.actions.drag_and_drop(source, target).perform()
        time.sleep(2)

    def verify_drop(self, source, target):
        try:
            inside = target.find_element(By.ID, source.get_attribute("id"))
            print(f"'{source.get_attribute('id')}' is inside 'droparea'")
        except NoSuchElementException:
            print(f"'{source.get_attribute('id')}' is NOT inside 'droparea'")

    def run(self):
        try:
            self.navigate("https://demo.automationtesting.in/Static.html")
            sources, target = self.find_elements()
            for source in sources:
                self.drag_and_drop(source, target)
                self.verify_drop(source, target)
            print("Drag and Drop Demo completed.")
        finally:
            print("Quitting browser...")
            self.driver.quit()

if __name__ == "__main__":
    demo = DragDropDemo()
    demo.run()