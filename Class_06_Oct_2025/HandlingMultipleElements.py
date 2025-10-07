from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def multiple_elements():
    print("Starting Handling Multiple Elements demo...")
    driver = webdriver.Chrome()
    try:
        print("Navigating to Google...")
        driver.get("https://www.google.com")
        print("Finding all links on the page...")
        links = driver.find_elements(By.TAG_NAME, "a")
        print(f"Total links found: {len(links)}")
        print("Printing first 10 links with visible text...")
        for i, link in enumerate(links[:10]):
            href = link.get_attribute("href")
            text = link.text
            if text:
                print(f"{i + 1}. {text} -> {href}")
        print("Handling Multiple Elements demo completed.")
    finally:
        print("Quitting browser...")
        driver.quit()

multiple_elements()
