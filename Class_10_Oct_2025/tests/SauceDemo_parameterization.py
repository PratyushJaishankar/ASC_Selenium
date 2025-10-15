import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@pytest.fixture(autouse=True)
def browser():
    print("\n[Setup] Launching Chrome browser...")
    driver = webdriver.Chrome()
    yield driver
    print("[Teardown] Closing Chrome browser...")
    driver.quit()


@pytest.mark.parametrize("username,password,expected_success", [
    ("standard_user", "secret_sauce", True),     # valid credentials
    ("locked_out_user", "secret_sauce", False),  # locked account
    ("problem_user", "secret_sauce", True),      # valid but buggy
    ("invalid_user", "wrong_pass", False),       # invalid credentials
    ("", "", False),
    ("standard_user", "", False), 
    ("", "secret_sauce", False),
    # empty fields
])
def test_login(browser, username, password, expected_success):
    browser.get("https://www.saucedemo.com/")

    # enter username and password
    browser.find_element(By.ID, "user-name").send_keys(username)
    browser.find_element(By.ID, "password").send_keys(password)
    browser.find_element(By.ID, "login-button").click()
    time.sleep(1)

    # check login success or failure
    if expected_success:
        # login success: URL should change to inventory.html
        assert "inventory.html" in browser.current_url, f"Login failed for {username}"
    else:
        # login failure: error message should be visible
        error_elements = browser.find_elements(By.CSS_SELECTOR, "h3[data-test='error']")
        assert error_elements, f"Expected login failure for {username}, but no error found."
