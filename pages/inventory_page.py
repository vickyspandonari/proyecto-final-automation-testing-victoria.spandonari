from selenium.webdriver.common.by import By
from .base_page import BasePage

class InventoryPage(BasePage):

    FIRST_PRODUCT_ADD_BTN = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_ICON = (By.ID, "shopping_cart_container")
    ITEM_NAME = (By.CSS_SELECTOR, ".inventory_item_name")

    def add_first_product_to_cart(self):
        # Aseguramos que el botón exista
        element = self.find(*self.FIRST_PRODUCT_ADD_BTN)

        # Scroll para evitar fallos en headless
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

        # Click robusto con WebDriverWait
        self.click(*self.FIRST_PRODUCT_ADD_BTN)

    def go_to_cart(self):
        self.click(*self.CART_ICON)

    def open_first_product(self):
        self.click(*self.ITEM_NAME)

