from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By

import openpyxl

import time

import os


class LoginTester:

    def __init__(self):

        self.driver = None

        self.excel_file = "test_data/login_data.xlsx"

    def read_test_data(self):

        print("Reading login test data from Excel...")

        if not os.path.exists(self.excel_file):
            print(f"Error: File {self.excel_file} not found!")

            return []

        workbook = openpyxl.load_workbook(self.excel_file)

        sheet = workbook["LoginTests"]

        test_cases = []

        headers = [cell.value for cell in sheet[1]]

        for row in sheet.iter_rows(min_row=2, values_only=True):

            if row[0]:  # If TestCaseID exists

                test_case = dict(zip(headers, row))

                test_cases.append(test_case)

        workbook.close()

        print(f"Found {len(test_cases)} test cases")

        return test_cases

    def read_test_data_xlsx(self):
        xlsx_file = "test_data/login_data.xlsx"
        print(f"Using Excel file on path: {xlsx_file}")
        test_cases = []
        if not os.path.exists(xlsx_file):
            print(f"Error: File {xlsx_file} not found!")
            return test_cases
        wb = openpyxl.load_workbook(xlsx_file)
        ws = wb.active
        for row in ws.iter_rows(min_row=2, values_only=True):
            test_cases.append(row)
        print(f"Found {len(test_cases)} test cases in Excel file")
        return test_cases

    def setup_browser(self):

        print("Setting up browser...")

        self.driver = webdriver.Chrome()

        self.driver.get("https://www.saucedemo.com/")

        time.sleep(2)

        print("Login page loaded successfully")

    def perform_login(self, username, password):

        try:

            # Find username field and enter data

            username_field = self.driver.find_element(By.ID, "user-name")

            username_field.clear()

            if username:
                username_field.send_keys(username)

                # Find password field and enter data

            password_field = self.driver.find_element(By.ID, "password")

            password_field.clear()

            if password:
                password_field.send_keys(password)

                # Click login button

            login_btn = self.driver.find_element(By.ID, "login-button")

            login_btn.click()

            time.sleep(3)

            # Check if login was successful or not

            current_url = self.driver.current_url

            if "inventory.html" in current_url:

                return "Success", "Login successful - redirected to products page"

            else:

                # Check for error message

                error_element = self.driver.find_element(By.CLASS_NAME, "error-message-container")

                error_text = error_element.text

                return "Error", error_text



        except Exception as e:

            return "Error", f"Exception: {str(e)}"

    def logout(self):

        """Logout after successful login to reset for next test"""

        try:

            menu_btn = self.driver.find_element(By.ID, "react-burger-menu-btn")

            menu_btn.click()

            time.sleep(1)

            logout_btn = self.driver.find_element(By.ID, "logout_sidebar_link")

            logout_btn.click()

            time.sleep(2)

        except:

            # If logout fails, just refresh the page to go back to login

            self.driver.get("https://www.saucedemo.com/")

            time.sleep(2)

    def run_tests(self):

        print("Starting run_tests method...")

        try:

            # Setup

            self.setup_browser()

            print("Reading login test data from Excel...")

            test_cases_xlsx = self.read_test_data_xlsx()

            if not test_cases_xlsx:

                print("No test cases found. Exiting.")

                return

            print(f"Running {len(test_cases_xlsx)} Excel test cases...")

            passed_count = 0

            for i, test_case in enumerate(test_cases_xlsx, 1):

                username = test_case[1]

                password = test_case[2]

                expected = test_case[3]

                print(f"\nExcel Test {i}:")

                print(f"  Username: '{username}'")

                print(f"  Password: '{password}'")

                print(f"  Expected: {expected}")

                # Perform login

                actual_result, message = self.perform_login(username, password)

                # Check result

                test_passed = actual_result == expected

                if test_passed:

                    print(f"  ✓ PASS - {message}")

                    passed_count += 1

                else:

                    print(f"  ✗ FAIL - {message}")

                # Reset for next test

                if actual_result == "Success":

                    self.logout()

                else:

                    # If login failed, refresh to go back to login page

                    self.driver.get("https://www.saucedemo.com/")

                    time.sleep(2)

            print("\n" + "=" * 60)

            print("TEST RESULTS SUMMARY")

            print("=" * 60)

            total_count = len(test_cases_xlsx)

            print(f"Total Tests: {total_count}")

            print(f"Passed: {passed_count}")

            print(f"Failed: {total_count - passed_count}")

            if total_count > 0:

                success_rate = (passed_count / total_count) * 100

                print(f"Success Rate: {success_rate:.1f}%")



        except Exception as e:

            print(f"Error in test execution: {e}")

        finally:

            if self.driver:
                self.driver.quit()

                print("\nBrowser closed")


if __name__ == "__main__":
    print("SauceDemo Login Data-Driven Testing")

    print("Website: https://www.saucedemo.com/")

    print()

    tester = LoginTester()

    tester.run_tests()