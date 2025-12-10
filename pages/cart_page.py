from selenium.webdriver.common.by import By
from .base_page import BasePage

class CartPage(BasePage):

    CART_ITEM = (By.CLASS_NAME, "cart_item")
    CHECKOUT_BTN = (By.ID, "checkout")

    def get_cart_items_count(self):
        return len(self.driver.find_elements(*self.CART_ITEM))

    def is_checkout_button_present(self):
        try:
            self.find(*self.CHECKOUT_BTN)
            return True
        except:
            return False

    def go_to_checkout(self):
        # Scroll para que el botón sea visible en headless mode
        element = self.find(*self.CHECKOUT_BTN)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
