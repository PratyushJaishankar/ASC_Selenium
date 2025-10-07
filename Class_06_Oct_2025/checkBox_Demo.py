from selenium import webdriver

from selenium.webdriver.common.by import By

import time


def checkbox_demo():
    print("Starting Checkbox Demo...")
    driver = webdriver.Chrome()

    try:
        print("Navigating to demoqa.com/checkbox...")
        driver.get("https://demoqa.com/checkbox")

        print("Expanding home checkbox...")

        home_checkbox = driver.find_element(By.CSS_SELECTOR, ".rct-checkbox")

        home_checkbox.click()

        time.sleep(2)

        print("Finding all checkboxes...")

        # Find all checkboxes

        checkboxes = driver.find_elements(By.CSS_SELECTOR, ".rct-checkbox")

        print(f"Total checkboxes: {len(checkboxes)}")

        print("Clicking specific checkboxes...")

        # Click specific checkboxes

        for i, checkbox in enumerate(checkboxes[1:4]):  # Skip first one (home)
            print(f"Clicking checkbox {i+2}...")
            checkbox.click()

            time.sleep(1)

        print("Verifying selected checkboxes...")

        # Verify selection

        selected_checkboxes = driver.find_elements(By.CSS_SELECTOR, ".rct-icon-check")

        print(f"Selected checkboxes: {len(selected_checkboxes)}")

    finally:
        print("Quitting browser...")
        driver.quit()
        print("Checkbox Demo completed.")


checkbox_demo()