from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


ORDERS_ICON = (By.ID, 'nav-orders')
SIGN_IN_TEXT = (By.XPATH, "//h1[@class='a-spacing-small']")


@When('Click on Orders icon')
def click_orders_icon(context):
    context.driver.find_element(*ORDERS_ICON).click()
    sleep(4)

@Then('Logged out user sees Sign in page')
def verify_found_results_text(context):
    Sign_in_header = context.driver.find_element(*SIGN_IN_TEXT).text
    assert 'Sign-In' in Sign_in_header, f'Incorrect header {Sign_in_header}'