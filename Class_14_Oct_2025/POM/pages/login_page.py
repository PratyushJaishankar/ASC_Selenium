from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """Page object for the login page."""
    # Locator variables defined at class level

    USERNAME_FIELD = (By.ID, "user-name")

    PASSWORD_FIELD = (By.ID, "password")

    LOGIN_BUTTON = (By.ID, "login-button")

    ERROR_MESSAGE = (By.CLASS_NAME, "error-message-container")

    def open(self, driver):
        """Opens the login page."""
        print("Opening SauceDemo login page...")
        driver.get("https://www.saucedemo.com/")

    def enter_username(self, driver, username):
        """Enters the username into the username field."""
        print(f"Entering username: {username}")
        try:
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(self.USERNAME_FIELD)
            ).send_keys(username)
        except Exception as e:
            print(f"Error entering username: {e}")

    def enter_password(self, driver, password):
        """Enters the password into the password field."""
        print(f"Entering password: {'*' * len(password)}")
        try:
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(self.PASSWORD_FIELD)
            ).send_keys(password)
        except Exception as e:
            print(f"Error entering password: {e}")

    def click_login(self, driver):
        """Clicks the login button."""
        print("Clicking login button...")
        try:
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(self.LOGIN_BUTTON)
            ).click()
        except Exception as e:
            print(f"Error clicking login button: {e}")

    def login(self, driver, username, password):
        """Performs login with provided credentials."""
        print("Performing login...")
        self.enter_username(driver, username)
        self.enter_password(driver, password)
        self.click_login(driver)

    def get_error_message(self, driver):
        """Returns the error message text if present."""
        print("Getting error message...")
        try:
            error = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located(self.ERROR_MESSAGE)
            ).text
            print(f"Error message found: {error}")
            return error
        except Exception as e:
            print(f"No error message found: {e}")
            return None

