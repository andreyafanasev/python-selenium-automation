from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then

CART_ICON = (By.CSS_SELECTOR, "a[href*='cart']")
CART_TEXT = (By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']/h2")

@when('Click on cart icon')
def click_on_cart_icon(context):
    context.driver.find_element(*CART_ICON).click()
    sleep(4)


@then('User sees that cart is empty')
def verify_found_results_text(context):
    cart_header = context.driver.find_element(*CART_TEXT).text
    assert 'Cart is empty' in cart_header, f'Incorrect header {cart_header}'