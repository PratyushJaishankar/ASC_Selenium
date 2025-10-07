from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options

import time


def webelement_methods():
    print("Starting WebElement Methods demo...")
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)

    try:

        print("Navigating to saucedemo.com...")

        driver.get("https://www.saucedemo.com")

        print("Finding username element...")

        username = driver.find_element(By.ID, "user-name")

        print("Entering 'standard_user'...")

        username.send_keys("standard_user")

        print("Clearing username...")

        username.clear()

        print("Entering 'problem_user'...")

        username.send_keys("problem_user")

        print("Finding password element...")

        password = driver.find_element(By.ID, "password")

        print("Entering password...")

        password.send_keys("secret_sauce")

        print("Finding and clicking login button...")

        login_btn = driver.find_element(By.ID, "login-button")

        login_btn.click()

        time.sleep(2)

        print("Finding menu button and getting class attribute...")

        menu_btn = driver.find_element(By.ID, "react-burger-menu-btn")

        class_name = menu_btn.get_attribute("class")

        print(f"Class attribute: {class_name}")

        # 5. text - Get text content

        title = driver.find_element(By.CLASS_NAME, "title")

        print(f"Title text: {title.text}")

        # 6. is_displayed() - Check if element is displayed

        is_displayed = menu_btn.is_displayed()

        print(f"Is displayed: {is_displayed}")

        # 7. is_enabled() - Check if element is enabled

        is_enabled = menu_btn.is_enabled()

        print(f"Is enabled: {is_enabled}")

        # 8. is_selected() - Check if element is selected (for checkboxes/radio)

        menu_btn.click()

        time.sleep(1)

        logout_link = driver.find_element(By.ID, "logout_sidebar_link")

        is_selected = logout_link.is_selected()

        print(f"Is selected: {is_selected}")

        # 9. location - Get element location

        location = menu_btn.location

        print(f"Element location: {location}")

        # 10. size - Get element size

        size = menu_btn.size

        print(f"Element size: {size}")

        print("WebElement Methods demo completed.")

    finally:

        print("Quitting browser...")

        driver.quit()


webelement_methods()