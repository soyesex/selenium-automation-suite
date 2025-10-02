from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

class DashboardPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.USER_TITLE = (By.CLASS_NAME, "caption-title")
    
    def get_user_profile_name(self):
        return self.get_text(self.USER_TITLE, timeout=50)

        
