from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def auto_suggestion():
    print("Starting Auto Suggestion demo...")
    driver = webdriver.Chrome()

    try:
        print("Navigating to Google...")
        driver.get("https://www.google.com")
        print("Finding search box and entering text...")
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("selenium")
        time.sleep(2)  # Wait for suggestions to appear
        print("Getting all suggestions...")
        suggestions = driver.find_elements(By.CSS_SELECTOR, "ul.G43f7e li")
        print(f"Number of suggestions: {len(suggestions)}")

        for i, suggestion in enumerate(suggestions):
            text = suggestion.text

            if text:
                print(f"{i + 1}. {text}")

        if suggestions:
            print("Clicking on the first suggestion...")
            suggestions[0].click()

            time.sleep(2)

    finally:
        print("Quitting browser...")
        driver.quit()
        print("Auto Suggestion demo completed.")


auto_suggestion()
