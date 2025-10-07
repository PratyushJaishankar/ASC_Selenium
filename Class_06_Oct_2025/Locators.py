from selenium import webdriver

from selenium.webdriver.common.by import By

import time



def locators_demo():
    print("Starting Locators Demo...")
    driver = webdriver.Chrome()

    try:

        print("Navigating to saucedemo.com...")

        driver.get("https://www.saucedemo.com")

        print("Using ID locator for username...")

        # username = driver.find_element(By.ID, "user-name")

        username = driver.find_element(By.CSS_SELECTOR, "input[data-test='username']")
        username.send_keys("standard_user")

        print("Using NAME locator for password...")

        password = driver.find_element(By.NAME, "password")

        password.send_keys("secret_sauce")

        print("Using CLASS_NAME locator for login button...")

        login_btn = driver.find_element(By.CLASS_NAME, "submit-button")

        login_btn.click()

        time.sleep(2)

        print("Using TAG_NAME locator for links...")

        links = driver.find_elements(By.TAG_NAME, "a")

        print(f"Number of links: {len(links)}")

        print("Navigating to the-internet.herokuapp.com...")

        driver.get("https://the-internet.herokuapp.com")

        print("Using LINK_TEXT locator for A/B Testing link...")

        ab_testing_link = driver.find_element(By.LINK_TEXT, "A/B Testing")

        ab_testing_link.click()

        time.sleep(2)

        # 6. PARTIAL_LINK_TEXT Locator

        driver.back()

        test_link = driver.find_element(By.PARTIAL_LINK_TEXT, "A/B")

        test_link.click()

        time.sleep(2)

        # 7. CSS_SELECTOR Locator

        driver.get("https://www.saucedemo.com")

        username_css = driver.find_element(By.CSS_SELECTOR, "#user-name")

        username_css.send_keys("standard_user")

        # 8. XPATH Locator

        password_xpath = driver.find_element(By.XPATH, "//input[@id='password']")

        password_xpath.send_keys("secret_sauce")


        print("Locators Demo completed.")

    finally:

        print("Quitting browser...")

        driver.quit()


locators_demo()