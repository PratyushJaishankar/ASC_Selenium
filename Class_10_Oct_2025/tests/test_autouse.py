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


def test_simple_alert(browser):
    browser.get("https://demoqa.com/alerts")
    browser.find_element(By.ID, "alertButton").click()
    time.sleep(1)
    alert = browser.switch_to.alert
    assert "You clicked a button" in alert.text
    alert.accept()


def test_confirmation_alert(browser):
    browser.get("https://demoqa.com/alerts")
    browser.find_element(By.ID, "confirmButton").click()
    time.sleep(1)
    alert = browser.switch_to.alert
    assert "Do you confirm action?" in alert.text
    alert.dismiss()


def test_prompt_alert(browser):
    browser.get("https://demoqa.com/alerts")
    browser.find_element(By.ID, "promtButton").click()
    time.sleep(1)
    alert = browser.switch_to.alert
    entered_text = "Selenium Python"
    alert.send_keys(entered_text)
    alert.accept()
    prompt_result = browser.find_element(By.ID, "promptResult")
    assert entered_text in prompt_result.text
