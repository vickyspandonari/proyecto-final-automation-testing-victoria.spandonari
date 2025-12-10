import json
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def load_users():
    with open("data/users.json") as f:
        return json.load(f)

def test_login_correcto(driver):
    data = load_users()["valid_user"]
    login_page = LoginPage(driver)
    login_page.login(data["username"], data["password"])

    assert "inventory" in driver.current_url


def test_login_incorrecto(driver):
    data = load_users()["invalid_user"]
    login_page = LoginPage(driver)
    login_page.login(data["username"], data["password"])

    assert "Epic sadface" in login_page.get_error()
    
def test_agregar_producto(driver):
    data = load_users()["valid_user"]
    login_page = LoginPage(driver)
    login_page.login(data["username"], data["password"])

    inventory = InventoryPage(driver)
    inventory.add_first_product_to_cart()
    inventory.go_to_cart()

    cart = CartPage(driver)
    assert cart.get_cart_items_count() == 1
    
def test_checkout(driver):
    data = load_users()["valid_user"]
    login_page = LoginPage(driver)
    login_page.login(data["username"], data["password"])

    inventory = InventoryPage(driver)
    inventory.add_first_product_to_cart()
    inventory.go_to_cart()

    cart = CartPage(driver)
    cart.go_to_checkout()

    checkout = CheckoutPage(driver)
    checkout.fill_form("Victoria", "Spandonari", "1000")
    checkout.finish_purchase()

    assert "Thank you" in checkout.get_confirmation_text()
    
def test_detalle_producto(driver):
    data = load_users()["valid_user"]
    login_page = LoginPage(driver)
    login_page.login(data["username"], data["password"])

    inventory = InventoryPage(driver)
    inventory.open_first_product()

    assert "inventory-item" in driver.current_url