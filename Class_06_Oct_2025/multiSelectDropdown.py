import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

def multi_select_demo():
    print("Starting Multi-Select Dropdown demo...")
    driver = webdriver.Chrome()
    try:
        print("Navigating to demoqa.com/select-menu...")
        driver.get("https://demoqa.com/select-menu")
        print("Selecting 'Volvo' and 'Audi'...")
        multi_select = Select(driver.find_element(By.ID, "cars"))
        multi_select.select_by_visible_text("Volvo")
        multi_select.select_by_visible_text("Audi")
        time.sleep(2)
        print("Getting all selected options...")
        selected_options = multi_select.all_selected_options
        for option in selected_options:
            print(f"Selected: {option.text}")
        print("Deselecting 'Volvo'...")
        multi_select.deselect_by_visible_text("Volvo")
        time.sleep(2)
        print("Deselecting all options...")
        multi_select.deselect_all()
        print("Multi-Select Dropdown demo completed.")
    finally:
        print("Quitting browser...")
        driver.quit()


multi_select_demo()