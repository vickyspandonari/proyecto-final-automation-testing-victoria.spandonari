from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):

    USER = (By.ID, "user-name")
    PASS = (By.ID, "password")
    BTN_LOGIN = (By.ID, "login-button")
    ERROR = (By.CSS_SELECTOR, "h3[data-test='error']")

    def login(self, username, password):
        self.type(*self.USER, username)
        self.type(*self.PASS, password)
        self.click(*self.BTN_LOGIN)

    def get_error(self):
        return self.find(*self.ERROR).text