# Alerts.py - Demonstrates handling different types of browser alerts using Selenium
# Author: Pratyush Jaishankar
# Date: 09-Oct-2025

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class AlertsDemo:
    def __init__(self):
        print("[INIT] Initializing Chrome WebDriver...")
        self.driver = webdriver.Chrome()
        self.By = By
        print("[INIT] WebDriver initialized.")

    def run(self):
        print("[RUN] Starting Alerts demo...")
        try:
            print("[STEP] Navigating to https://demoqa.com/alerts ...")
            self.driver.get("https://demoqa.com/alerts")

            # 1. Simple Alert
            print("[STEP] Triggering simple alert...")
            simple_alert_btn = self.driver.find_element(self.By.ID, "alertButton")
            simple_alert_btn.click()
            time.sleep(1)
            alert = self.driver.switch_to.alert
            print(f"[ALERT] Alert text: {alert.text}")
            alert.accept()
            print("[STEP] Simple alert accepted.")
            time.sleep(1)

            # 2. Confirmation Alert
            print("[STEP] Triggering confirmation alert...")
            confirm_alert_btn = self.driver.find_element(self.By.ID, "confirmButton")
            confirm_alert_btn.click()
            time.sleep(1)
            alert = self.driver.switch_to.alert
            print(f"[ALERT] Confirm alert text: {alert.text}")
            alert.dismiss()
            print("[STEP] Confirmation alert dismissed.")
            time.sleep(1)

            # 3. Prompt Alert
            print("[STEP] Triggering prompt alert...")
            prompt_alert_btn = self.driver.find_element(self.By.ID, "promtButton")
            prompt_alert_btn.click()
            time.sleep(1)
            alert = self.driver.switch_to.alert
            entered_text = "Selenium Python"
            print(f"[STEP] Entering text in prompt: {entered_text}")
            alert.send_keys(entered_text)
            print("[STEP] Text entered in prompt.")
            alert.accept()
            time.sleep(1)
            prompt_result = self.driver.find_element(self.By.ID, "promptResult")
            assert entered_text in prompt_result.text, "Prompt result does not contain input text"
            print(f"[RESULT] Text entered in prompt result: {prompt_result.text}")
            print("[STEP] Prompt alert accepted.")

        except Exception as e:
            print(f"[ERROR] Exception occurred: {e}")
        finally:
            print("[END] Quitting browser...")
            self.driver.quit()
            print("[END] Browser closed.")

if __name__ == "__main__":
    print("[MAIN] Running AlertsDemo...")
    demo = AlertsDemo()
    demo.run()
    print("[MAIN] AlertsDemo finished.")
