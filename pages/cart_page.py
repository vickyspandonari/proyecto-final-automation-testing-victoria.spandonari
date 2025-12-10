from selenium.webdriver.common.by import By
from .base_page import BasePage

class CartPage(BasePage):

    CART_ITEM = (By.CLASS_NAME, "cart_item")
    CHECKOUT_BTN = (By.ID, "checkout")

    def get_cart_items_count(self):
        return len(self.driver.find_elements(*self.CART_ITEM))

    def go_to_checkout(self):
        self.click(*self.CHECKOUT_BTN)