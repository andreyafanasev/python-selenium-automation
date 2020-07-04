from selenium.webdriver.common.by import By
from behave import given, when, then

HEADER = (By.CSS_SELECTOR, "#zg_banner_text_wrapper")
TOP_LINKS = (By.CSS_SELECTOR, "#zg_header a")


@then('Verify user can click on top links on Bestsellers page, and they are open')
def top_links_open(context):
    top_bar_links = context.driver.find_elements(*TOP_LINKS)
    header_text = context.driver.find_element(*HEADER).text
    for i in range(len(top_bar_links)):
        top_bar_links[i].click()
        top_bar_links = context.driver.find_elements(*TOP_LINKS)
        assert top_bar_links[i].text in context.driver.find_element(*HEADER).text