from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element_with_wait(self, locator, timeout = 10):
        """Encuentra un elemento esperando a que sea visible"""
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located(locator))
    
    def click(self, locator, timeout = 10):
        """Hace clic en un elemento despues de esperar a que sea clickeable"""
        wait = WebDriverWait(self.driver, timeout)
        element = wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def get_text(self, locator, timeout = 10):
        """Obtiene el texto de un elemento esperando a que sea visible."""
        element = self.find_element_with_wait(locator, timeout)
        return element.text