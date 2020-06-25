from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then

ORDERS_ICON = (By.ID, 'nav-orders')
SIGN_IN_TEXT = (By.XPATH, "//h1[@class='a-spacing-small']")


@when('Click on Orders icon')
def click_orders_icon(context):
    context.driver.find_element(*ORDERS_ICON).click()
    sleep(4)


@then('Logged out user sees Sign in page')
def verify_found_results_text(context):
    sign_in_header = context.driver.find_element(*SIGN_IN_TEXT).text
    assert 'Sign-In' in sign_in_header, f'Incorrect header {sign_in_header}'