from selenium.webdriver.common.by import By
from .base_page import BasePage

class CheckoutPage(BasePage):

    FIRSTNAME = (By.ID, "first-name")
    LASTNAME = (By.ID, "last-name")
    POSTALCODE = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")
    FINISH_BTN = (By.ID, "finish")
    CONFIRM_MSG = (By.CLASS_NAME, "complete-header")

    def fill_form(self, fname, lname, zip):
        self.type(*self.FIRSTNAME, fname)
        self.type(*self.LASTNAME, lname)
        self.type(*self.POSTALCODE, zip)
        self.click(*self.CONTINUE_BTN)

    def finish_purchase(self):
        self.click(*self.FINISH_BTN)

    def get_confirmation_text(self):
        return self.find(*self.CONFIRM_MSG).text