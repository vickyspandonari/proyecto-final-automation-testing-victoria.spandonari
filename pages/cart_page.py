from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

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
        # Esperar que el botón 
        checkout_btn = self.wait.until(
        EC.element_to_be_clickable(self.CHECKOUT_BTN)
    )

        # Scroll para headless
        self.driver.execute_script("arguments[0].scrollIntoView();", checkout_btn)

        # Click
        checkout_btn.click()

        # Esperar a que cargue la página de checkout (First Name visible)
        self.wait.until(
        EC.visibility_of_element_located((By.ID, "first-name"))
        )