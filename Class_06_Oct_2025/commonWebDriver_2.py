from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def webdriver_methods_demo():
    print("Starting commonWebDriver_2 demo...")
    driver = webdriver.Chrome()

    try:
        print("Navigating to Google...")
        driver.get("https://www.google.com")

        # Get page title
        print(f"Title: {driver.title}")

        # Get current URL
        print(f"URL: {driver.current_url}")

        print("Maximizing window...")
        # Maximize window
        driver.maximize_window()
        time.sleep(2)

        print("Setting window size to 800x600...")
        # Set window size
        driver.set_window_size(800, 600)
        time.sleep(2)

        print("Navigating to python.org...")
        # Navigate to another site
        driver.get("https://www.python.org")
        time.sleep(2)

        print("Going back to Google...")
        # Go back to Google
        driver.back()
        time.sleep(2)

        print("Going forward to Python.org...")
        # Go forward to Python
        driver.forward()
        time.sleep(2)

        print("Refreshing page...")
        # Refresh page
        driver.refresh()

    finally:
        print("Quitting browser...")
        driver.quit()
        print("commonWebDriver_2 demo completed.")


webdriver_methods_demo()
