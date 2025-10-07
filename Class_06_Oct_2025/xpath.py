from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def xpath_examples():
    print("Starting XPath Examples demo...")
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)

    try:
        print("Navigating to saucedemo.com...")
        driver.get("https://www.saucedemo.com")

        print("Using XPath for username...")
        username = driver.find_element(By.XPATH, "//input[@id='user-name']")
        username.send_keys("standard_user")

        print("Using XPath for password...")
        password = driver.find_element(By.XPATH, "//input[@id='password' and @name='password']")
        password.send_keys("secret_sauce")

        print("Using XPath for login button...")
        login_btn = driver.find_element(By.XPATH, "//input[@value='Login']")
        login_btn.click()

        print("Using XPath for menu button (contains)...")
        menu_btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Open Menu')]")

        print("XPath Examples demo completed.")

    finally:
        print("Quitting browser...")
        driver.quit()


xpath_examples()