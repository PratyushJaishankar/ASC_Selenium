import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


def right_click_demo():
    driver = webdriver.Chrome()

    try:

        driver.get("https://demoqa.com/buttons")

        actions = ActionChains(driver)

        # Find the button for right click

        right_click_btn = driver.find_element(By.ID, "rightClickBtn")

        # Perform right click

        actions.context_click(right_click_btn).perform()

        time.sleep(2)

        # Verify right click message

        message = driver.find_element(By.ID, "rightClickMessage")

        print(f"Right click message: {message.text}")



    finally:

        driver.quit()


right_click_demo()