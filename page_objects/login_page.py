from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    # This method inherits from its parent and gets all the methods, then uses a tuple to unpack those two values.
    def __init__(self, driver):
        super().__init__(driver)
        self.EMAIL_INPUT = (By.NAME, "email")
        self.PASSWORD_INPUT = (By.NAME, "password")
        self.LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    # Method login for the login action in the system
    def login(self, email, password):
        # 1. Find field username and fill it
        email_field = self.find_element_with_wait(self.EMAIL_INPUT)
        email_field.send_keys(email)

        # 2. Find field password and fill it
        password_field = self.find_element_with_wait(self.PASSWORD_INPUT)
        password_field.send_keys(password)

        # 3. Clic on the login button
        self.click(self.LOGIN_BUTTON)
        
