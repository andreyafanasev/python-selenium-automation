from pages.base_page import Page
from selenium.webdriver.common.by import By


class SignIn(Page):

    ORDERS_ICON = (By.ID, 'nav-orders')
    SIGN_IN_TEXT = (By.XPATH, "//h1[@class='a-spacing-small']")

    def click_orders(self):
        self.driver.find_element(*self.ORDERS_ICON).click()

    def verify_sign_in_text(self):
        sign_in_header = self.driver.find_element(*self.SIGN_IN_TEXT).text
        assert 'Sign-In' in sign_in_header, f'Incorrect header {sign_in_header}'