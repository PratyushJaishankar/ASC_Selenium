# JavaScript Executor Demo: Demonstrates executing JavaScript commands in Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def javascript_executor_demo():
    driver = webdriver.Chrome()

    try:
        # Open the login page
        driver.get("https://www.saucedemo.com")

        # Login using provided credentials
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        time.sleep(2)

        # JavaScript Executor examples
        # 1. Scroll to bottom of the page
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

        # 2. Scroll to top of the page
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)

        # 3. Scroll to a specific element (footer)
        footer = driver.find_element(By.CLASS_NAME, "footer")
        driver.execute_script("arguments[0].scrollIntoView();", footer)
        time.sleep(2)

        # 4. Highlight a product element
        product = driver.find_element(By.CLASS_NAME, "inventory_item_name")
        # You can add highlight code here if needed

    finally:
        # Quit the browser
        driver.quit()


javascript_executor_demo()