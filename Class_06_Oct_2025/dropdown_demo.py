from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

def dropdown_demo():
    print("Starting Dropdown Demo...")
    driver = webdriver.Chrome()
    try:
        print("Navigating to demoqa.com/select-menu...")
        driver.get("https://demoqa.com/select-menu")
        print("Selecting 'Green' by visible text...")
        old_select = Select(driver.find_element(By.ID, "oldSelectMenu"))
        old_select.select_by_visible_text("Green")
        time.sleep(1)
        print("Selecting value '4'...")
        old_select.select_by_value("4")
        time.sleep(1)
        print("Selecting by index 1...")
        old_select.select_by_index(1)
        time.sleep(1)
        print("Getting all options...")
        options = old_select.options
        for option in options:
            print(f"Option: {option.text}")
        selected_option = old_select.first_selected_option
        print(f"Selected: {selected_option.text}")
        print("Dropdown Demo completed.")
    finally:
        print("Quitting browser...")
        driver.quit()


dropdown_demo()