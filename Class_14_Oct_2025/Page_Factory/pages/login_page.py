from seleniumpagefactory import PageFactory

class LoginPage(PageFactory):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    # ✅ Correct use of @FindBy with seleniumpagefactory
    username_field = {
        'by': 'id',
        'value': 'user-name'
    }

    password_field = {
        'by': 'id',
        'value': 'password'
    }

    login_button = {
        'by': 'id',
        'value': 'login-button'
    }

    error_message = {
        'by': 'class_name',
        'value': 'error-message-container'
    }

    # ---------- Page Actions ----------
    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    def enter_username(self, username):
        self.username_field.clear()
        self.username_field.send_keys(username)

    def enter_password(self, password):
        self.password_field.clear()
        self.password_field.send_keys(password)

    def click_login(self):
        self.login_button.click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self):
        return self.error_message.text
