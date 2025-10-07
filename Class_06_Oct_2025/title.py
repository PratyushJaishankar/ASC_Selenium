import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

print("Starting title.py...")
chrome_options = Options()
chrome_options.add_argument('--headless')

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

website_url = "https://www.saucedemo.com/"
print(f"Navigating to {website_url} ...")
driver.get(website_url)

time.sleep(2)

expected_title = "Swag Labs"
actual_title = driver.title

print(f"Expected Title: {expected_title}")
print(f"Actual Title: {actual_title}")
assert actual_title == expected_title, "Title does not match!"

if expected_title == actual_title:
    print("PASSED!")
else:
    print("FAILED!")

print("Quitting browser...")
driver.quit()
print("title.py completed.")
