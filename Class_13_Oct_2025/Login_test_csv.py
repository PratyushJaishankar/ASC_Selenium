from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By

import time

import os

import csv

class LoginTester:
    def __init__(self):
        self.driver = None
        self.csv_file = "test_data/login_data.csv"

    def read_test_data(self):
        print("Reading login test data from CSV...")
        if not os.path.exists(self.csv_file):
            print(f"Error: File {self.csv_file} not found!")
            return []

        test_cases = []
        with open(self.csv_file, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row.get('TestCaseID'):
                    test_cases.append(row)
        print(f"Found {len(test_cases)} test cases")
        return test_cases

    def read_test_data_csv(self):
        csv_file = "test_data/login_data.csv"
        print(f"Using CSV file on path: {csv_file}")
        test_cases = []
        if not os.path.exists(csv_file):
            print(f"Error: File {csv_file} not found!")
            return test_cases
        with open(csv_file, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                test_cases.append(row)
        print(f"Found {len(test_cases)} test cases in CSV file")
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

            print("Reading login test data from CSV...")
            test_cases_csv = self.read_test_data_csv()
            if test_cases_csv:
                print(f"Running {len(test_cases_csv)} CSV test cases...")
                passed_count = 0
                for i, test_case in enumerate(test_cases_csv, 1):

                    test_id = test_case['TestCaseID']

                    username = test_case['Username']

                    password = test_case['Password']

                    expected = test_case['ExpectedResult']

                    print(f"\nTest {i}: {test_id}")

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

                # Results summary

                total_count = len(test_cases_csv)

                print("\n" + "=" * 60)

                print("TEST RESULTS SUMMARY")

                print("=" * 60)

                print(f"Total Tests: {total_count}")

                print(f"Passed: {passed_count}")

                print(f"Failed: {total_count - passed_count}")

                if total_count > 0:
                    success_rate = (passed_count / total_count) * 100

                    print(f"Success Rate: {success_rate:.1f}%")

            else:
                print("No test cases found. Exiting.")

                return

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