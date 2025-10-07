from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def radio_button_demo():
    print("Starting Radio Button demo...")
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    try:
        print("Navigating to demoqa.com/radio-button...")
        driver.get("https://demoqa.com/radio-button")
        print("Finding radio buttons...")
        yes_radio = driver.find_element(By.ID, "yesRadio")
        impressive_radio = driver.find_element(By.ID, "impressiveRadio")
        no_radio = driver.find_element(By.ID, "noRadio")
        print("Clicking Yes radio button...")
        driver.execute_script("arguments[0].click();", yes_radio)
        time.sleep(2)
        is_selected = driver.execute_script("return arguments[0].checked;", yes_radio)
        print(f"Yes radio selected: {is_selected}")
        print("Clicking Impressive radio button...")
        driver.execute_script("arguments[0].click();", impressive_radio)
        time.sleep(2)
        is_selected = driver.execute_script("return arguments[0].checked;", impressive_radio)
        print(f"Impressive radio selected: {is_selected}")
        print("Radio Button demo completed.")
    finally:
        print("Quitting browser...")
        driver.quit()

radio_button_demo()
