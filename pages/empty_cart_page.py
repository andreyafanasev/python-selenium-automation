from selenium.webdriver.common.by import By
from pages.base_page import Page


class EmptyCart(Page):
    CART_ICON = (By.CSS_SELECTOR, "a[href*='cart']")
    CART_TEXT = (By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']/h2")

    def click_cart_icon(self, *locator):
        self.driver.find_element(*self.CART_ICON).click()

    def verify_empty_cart_text(self):
        cart_header = self.driver.find_element(*self.CART_TEXT).text
        assert 'Cart is empty' in cart_header, f'Incorrect header {cart_header}'