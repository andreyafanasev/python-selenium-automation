from selenium.webdriver.common.by import By
from behave import given, then

REGULAR_PRICE = (By.CSS_SELECTOR, "div#wfm-pmd_deals_section span.wfm-sales-item-card__regular-price")
SELECTED_PRODUCT = (By.CSS_SELECTOR, "div.a-section.a-padding-none ul.s-col-2 li")
PRODUCT_NAME = (By.CSS_SELECTOR, "div.a-section.a-padding-none ul.s-col-2 span.wfm-sales-item-card__product-name")


@given('Open Amazon wholefood page')
def open_amazon_wholefood(context):
    context.driver.get('https://www.amazon.com/wholefoodsdeals')

"""
@then('Verify every product on the page has a text "Regular"')
def check_product_name(context):
    selected_product = context.driver.find_elements(*SELECTED_PRODUCT)

    for i in range(len(selected_product) - 1): # - 1 because last item is link "to see more"
        assert 'Regular' in selected_product[i].text
"""

@then('Verify every product on the page has a text "Regular" and a product name')
def check_product_name(context):
    selected_product = context.driver.find_elements(*SELECTED_PRODUCT)

    for i in range(len(selected_product) - 1): # - 1 because last item is link "to see more"
        assert 'Regular' in selected_product[i].text

    for e in selected_product[:-2]:
        e.find_element(*PRODUCT_NAME)