from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.common.action_chains import ActionChains

import time


def mouse_hover_demo():
    driver = webdriver.Chrome()

    try:

        driver.get("https://demoqa.com/menu")

        actions = ActionChains(driver)

        # Hover over main menu item

        main_item = driver.find_element(By.LINK_TEXT, "Main Item 2")

        actions.move_to_element(main_item).perform()

        time.sleep(2)

        # Hover over sub menu item (if visible)

        sub_items = driver.find_elements(By.CSS_SELECTOR, ".nav-item")

        for item in sub_items:

            if "SUB SUB LIST" in item.text.upper():
                actions.move_to_element(item).perform()

                time.sleep(2)

                break



    finally:

        driver.quit()


mouse_hover_demo() 