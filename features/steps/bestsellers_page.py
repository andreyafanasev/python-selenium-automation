from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then


best_sellers_link = (By.XPATH, "//div[@id='nav-xshop']/a[1]")
# top_bar_links = (By.XPATH, "//div[@id='zg_header']//a")

@when ("Click on Best sellers link")
def best_seller(context):
    context.driver.find_element(*best_sellers_link).click()

@then ("Verify Amazon BestSellers page has {number} links")
def best_sellers_links(context, number):
    top_bar_links = context.driver.find_elements(By.XPATH, "//div[@id='zg_header']//a")
    assert len(top_bar_links) == int(number), f"expected {len(top_bar_links)} links, but got {number} links"