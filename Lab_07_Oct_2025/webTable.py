# WebTableDemo: Demonstrates extracting and searching data from a web table using Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

class WebTableDemo:
    # Initialize Chrome WebDriver in headless mode
    def __init__(self):
        print("Initializing Chrome WebDriver in headless mode...")
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=chrome_options)

    # Navigate to the specified URL
    def navigate(self, url):
        print(f"Navigating to {url} ...")
        self.driver.get(url)

    # Locate all table rows on the page
    def get_table_rows(self):
        print("Locating all table rows...")
        rows = self.driver.find_elements(By.CSS_SELECTOR, "tr")
        print(f"Found {len(rows)} rows.")
        return rows

    # Calculate the number of columns in the table
    def get_column_count(self, rows):
        print("Calculating number of columns...")
        total_cells = len(self.driver.find_elements(By.CSS_SELECTOR, "td"))
        columns = total_cells // len(rows) if rows else 0
        print(f"Detected {columns} columns.")
        return columns

    # Print data from the first 'limit' rows of the table
    def print_table_data(self, rows, columns, limit=10):
        print(f"Extracting data from the first {limit} rows...")
        for i, row in enumerate(rows[:limit]):
            cells = row.find_elements(By.CSS_SELECTOR, "td")
            row_data = [cell.text for cell in cells[:columns]]
            if any(row_data):
                print(f"Row {i + 1}: {row_data}")

    # Search for a specific country in the table and print its row data
    def search_country(self, rows, columns, country="India"):
        print(f"Searching for '{country}' in the table...")
        for i, row in enumerate(rows):
            cells = row.find_elements(By.CSS_SELECTOR, "td")
            if len(cells) > 1 and cells[1].text == country:
                row_data = [cell.text for cell in cells[:columns]]
                print(f"Found {country} at Row: {i + 1}")
                print(f"Row Data: {row_data}")
                return
        print(f"{country} not found in the table.")

    # Main runner for the demo
    def run(self):
        try:
            self.navigate("https://cosmocode.io/automation-practice-webtable/")
            rows = self.get_table_rows()
            columns = self.get_column_count(rows)
            self.print_table_data(rows, columns)
            self.search_country(rows, columns)
            print("Web Table Demo completed.")
        finally:
            print("Quitting browser...")
            self.driver.quit()

if __name__ == "__main__":
    demo = WebTableDemo()
    demo.run()
