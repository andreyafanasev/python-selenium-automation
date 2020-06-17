from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then


@then ("The number of items is equal to {number}")
def count_items(contex, number):
    # one_element = contex.driver.find_element(By.CSS_SELECTOR, "div[data-component-type='s-search-result']")
    # print(one_element)
    search_result = contex.driver.find_elements(By.CSS_SELECTOR, "div[data-component-type='s-search-result']")
    assert len(search_result) == int(number), f"Expected {number}, but got {len(search_result)}"
    # print(search_result)
    # print(len(search_result))