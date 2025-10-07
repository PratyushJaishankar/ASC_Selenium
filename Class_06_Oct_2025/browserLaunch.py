from selenium import webdriver
from selenium.webdriver.common.by import By
import time

print("Starting browser launch demo...")
# Chrome Browser

driver = webdriver.Chrome()
print("Launching Chrome browser...")
driver.get("https://www.google.com")
print("Navigated to Google in Chrome.")
time.sleep(2)
print("Quitting Chrome browser...")
driver.quit()

# Firefox Browser
print("Launching Firefox browser...")
driver = webdriver.Firefox()
driver.get("https://www.google.com")
print("Navigated to Google in Firefox.")
time.sleep(2)
print("Quitting Firefox browser...")
driver.quit()

# Edge Browser

driver = webdriver.Edge()
print("Launching Edge browser...")
driver.get("https://www.google.com")
print("Navigated to Google in Edge.")
time.sleep(2)
print("Quitting Edge browser...")
driver.quit()

print("Browser launch demo completed.")
