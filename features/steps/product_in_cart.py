"""
Created by Andrei Afanasev
Home work 06/11/20

"""


from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
SEARCH_SUBMIT = (By.XPATH, "//input[@value='Go']")
PRODUCT_IN_LIST = (By.XPATH, "//h2[contains(@class,'s-line-clamp')]/a[contains(@href, 'B07JMVN1LM')]")
CHOOSE_SIZE_LINK = (By.ID, 'dropdown_selected_size_name')
SIZE_LINK = (By.ID, 'size_name_2')
ADD_TO_CART = (By.ID, 'add-to-cart-button')
COUNTER_NUMBER = (By.ID, 'nav-cart-count')


@when('Click on product in list')
def click_product_field(context):
    context.driver.find_element(*PRODUCT_IN_LIST).click()
    sleep(4)


@when('Click on Choose the size button')
def click_product_size(context):
    context.driver.find_element(*CHOOSE_SIZE_LINK).click()
    sleep(2)


@when('Choose size')
def choose_product_size(context):
    context.driver.find_element(*SIZE_LINK).click()
    sleep(2)


@when('Click on Add to cart button')
def sdd_to_cart(context):
    context.driver.find_element(*ADD_TO_CART).click()
    sleep(4)


@then('Cart counter increased by 1')
def verify_cart_counter_increased(context):
    cart_counter = context.driver.find_element(*COUNTER_NUMBER).text
    assert '1' in cart_counter, f'Incorrect product in cart counter {cart_counter}'
