from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

print("Starting Multiple Tabs demo...")
chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)
driver1 = webdriver.Chrome(options=chrome_options)
print("Opening Google in first tab...")
driver.get("https://www.google.com")
print("Opening Facebook in second tab...")
driver1.get("https://www.facebook.com")

time.sleep(2)
print("Closing first tab...")
driver.close()

time.sleep(2)
print("Multiple Tabs demo completed.")
