from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

WEBSITE_LINK = (By.XPATH, "//*[contains(text(), 'hungerpangnyc.com')]")
COMPANY_NAME = (By.XPATH, "//*[contains(text(), 'HUNGER PANG')]")

@given("Open a company's Yelp page")
def open_yelp(context):
    context.driver.get("https://www.yelp.com/biz/hunger-pang-brooklyn?osq=Restaurants")

@when("Click on a website link")
def click_link(context):
    context.original_windows = context.driver.window_handles
    print(context.original_windows)
    context.original_window = context.driver.current_window_handle
    print(context.original_window)
    context.driver.find_element(*WEBSITE_LINK).click()

@when("Switch to a new window")
def switch_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    current_windows = context.driver.window_handles
    print(current_windows)
    # context.driver.switch_to_window(current_window[1])
    for old_window in context.original_windows:
        current_windows.remove(old_window)
    print(current_windows)
    context.driver.switch_to_window(current_windows[0])

@then("The {company} website is open")
def verify_website_name(context, company):
    context.driver.find_element(*COMPANY_NAME)

@then("The user can close the new window and go to original one")
def close_window_and_go_back(context):
    context.driver.close()
    context.driver.switch_to_window(context.original_window)