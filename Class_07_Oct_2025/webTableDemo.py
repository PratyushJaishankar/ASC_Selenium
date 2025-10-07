from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def web_table_demo():
    print("Starting Web Table Demo...")
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    try:
        print("Navigating to demoqa.com/webtables...")
        driver.get("https://demoqa.com/webtables")
        print("Getting all rows in the table...")
        rows = driver.find_elements(By.CSS_SELECTOR, ".rt-tr-group")
        print(f"Total rows: {len(rows)}")
        print("Extracting data from each row...")
        for i, row in enumerate(rows):
            cells = row.find_elements(By.CSS_SELECTOR, ".rt-td")
            if len(cells) >= 6:
                row_data = [cell.text for cell in cells[:6]]
                if any(row_data):
                    print(f"Row {i + 1}: {row_data}")
        print("Searching for 'Cierra' in the table...")
        for row in rows:
            cells = row.find_elements(By.CSS_SELECTOR, ".rt-td")
            if len(cells) >= 4 and cells[0].text == "Cierra":
                print(f"Found Cierra: {cells[3].text}")
                break
        print("Web Table Demo completed.")
    finally:
        print("Quitting browser...")
        driver.quit()


web_table_demo()