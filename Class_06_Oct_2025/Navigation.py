from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


def navigation_commands():
    print("Starting Navigation Commands demo...")
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    try:
        print("Maximizing window...")
        driver.maximize_window()
        print("Navigating to Google...")
        driver.get("https://www.google.com")
        print(f"Page 1: {driver.title}")
        time.sleep(2)
        print("Navigating to Facebook...")
        driver.get("https://www.facebook.com")
        print(f"Page 2: {driver.title}")
        time.sleep(2)
        print("Navigating back...")
        driver.back()
        print(f"After back: {driver.title}")
        time.sleep(2)
        print("Navigating forward...")
        driver.forward()
        print(f"After forward: {driver.title}")
        time.sleep(2)
        print("Refreshing page...")
        driver.refresh()
        print("Navigation Commands demo completed.")
    finally:
        print("Quitting browser...")
        driver.quit()


navigation_commands()