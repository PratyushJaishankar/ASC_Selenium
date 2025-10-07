from selenium import webdriver

from selenium.webdriver.common.by import By

import time


def alerts_demo():
    driver = webdriver.Chrome()

    try:

        driver.get("https://demoqa.com/alerts")

        # 1. Simple Alert

        simple_alert_btn = driver.find_element(By.ID, "alertButton")

        simple_alert_btn.click()

        time.sleep(1)

        # Switch to alert and accept

        alert = driver.switch_to.alert

        print(f"Alert text: {alert.text}")

        alert.accept()

        print("Simple alert accepted")

        time.sleep(1)

        # 2. Confirmation Alert

        confirm_alert_btn = driver.find_element(By.ID, "confirmButton")

        confirm_alert_btn.click()

        time.sleep(1)

        alert = driver.switch_to.alert

        print(f"Confirm alert text: {alert.text}")

        alert.dismiss()  # Try accept() for OK

        print("Confirmation alert dismissed")

        time.sleep(1)

        # 3. Prompt Alert

        prompt_alert_btn = driver.find_element(By.ID, "promtButton")

        prompt_alert_btn.click()

        time.sleep(1)

        alert = driver.switch_to.alert

        alert.send_keys("Selenium Python")

        print("Text entered in prompt")

        alert.accept()

        print("Prompt alert accepted")



    finally:

        driver.quit()


alerts_demo()

