from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import openpyxl
import time
import os
import xml.etree.ElementTree as ET

class LoginTester:
    def __init__(self):
        self.driver = None
        self.excel_file = "test_data/login_data.xlsx"
        print(f"Excel file path set to: {self.excel_file}")

    def read_test_data(self):
        print("Reading login test data from XML...")
        xml_file = "test_data/login_data.xml"
        print(f"Using XML file on path: {xml_file}")
        if not os.path.exists(xml_file):
            print(f"Error: File {xml_file} not found!")
            return []
        tree = ET.parse(xml_file)
        root = tree.getroot()
        test_cases = []
        for testcase in root.findall("TestCase"):
            test_case = {
                "TestCaseID": testcase.findtext("TestCaseID"),
                "Username": testcase.findtext("Username"),
                "Password": testcase.findtext("Password"),
                "ExpectedResult": testcase.findtext("ExpectedResult")
            }
            if test_case["TestCaseID"]:
                test_cases.append(test_case)
        print(f"Found {len(test_cases)} test cases in XML file")
        return test_cases

    def read_test_data_xml(self):
        xml_file = "test_data/login_data.xml"
        print(f"Using XML file on path: {xml_file}")
        test_cases = []
        if not os.path.exists(xml_file):
            print(f"Error: File {xml_file} not found!")
            return test_cases
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for testcase in root.findall("TestCase"):
            test_cases.append(testcase)
        print(f"Found {len(test_cases)} test cases in XML file")
        return test_cases

    def setup_browser(self):
        print("Setting up browser...")
        print("Using Chrome WebDriver from webdriver_manager")
        self.driver = webdriver.Chrome()
        print("Chrome browser launched")
        self.driver.get("https://www.saucedemo.com/")
        time.sleep(2)
        print("Login page loaded successfully")

    def perform_login(self, username, password):
        print(f"Performing login with Username: '{username}' and Password: '{password}'")
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
            print("Clicking login button...")
            login_btn = self.driver.find_element(By.ID, "login-button")
            login_btn.click()
            time.sleep(3)
            # Check if login was successful or not
            current_url = self.driver.current_url
            print(f"Current URL after login: {current_url}")
            if "inventory.html" in current_url:
                print("Login successful - redirected to products page")
                return "Success", "Login successful - redirected to products page"
            else:
                # Check for error message
                error_element = self.driver.find_element(By.CLASS_NAME, "error-message-container")
                error_text = error_element.text
                print(f"Login failed - error message: {error_text}")
                return "Error", error_text
        except Exception as e:
            print(f"Exception during login: {str(e)}")
            return "Error", f"Exception: {str(e)}"

    def logout(self):
        print("Attempting logout...")
        try:
            menu_btn = self.driver.find_element(By.ID, "react-burger-menu-btn")
            menu_btn.click()
            time.sleep(1)
            logout_btn = self.driver.find_element(By.ID, "logout_sidebar_link")
            logout_btn.click()
            time.sleep(2)
            print("Logout successful")
        except:
            print("Logout failed, refreshing page to reset session")
            self.driver.get("https://www.saucedemo.com/")
            time.sleep(2)

    def run_tests(self):
        print("Starting run_tests method...")
        try:
            # Setup
            self.setup_browser()
            test_cases = self.read_test_data()
            if not test_cases:
                print("No test cases found. Exiting.")
                return
            print("\n" + "=" * 60)
            print("STARTING LOGIN TESTS")
            print("=" * 60)
            # Run tests
            passed_count = 0
            for i, test_case in enumerate(test_cases, 1):
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
                    print("Refreshing browser for next test...")
                    self.driver.get("https://www.saucedemo.com/")
                    time.sleep(2)
            # Results summary
            total_count = len(test_cases)
            print("\n" + "=" * 60)
            print("TEST RESULTS SUMMARY")
            print("=" * 60)
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
    print("Using XML file on path: test_data/login_data.xml")
    print("Using Excel file on path: test_data/login_data.xlsx")
    print()
    tester = LoginTester()

    tester.run_tests()