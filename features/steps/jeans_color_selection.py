from selenium.webdriver.common.by import By
from behave import given, then

COLOR_OPTIONS = (By.CSS_SELECTOR, "div#variation_color_name li")
SELECTED_COLOR = (By.CSS_SELECTOR, "div#variation_color_name span.selection")


@given('Open Amazon Jeans {productid} page')
def open_jeans_page(context, productid):
    context.driver.get(f'https://www.amazon.com/gp/product/{productid}/')


@then('Verify user can select through the jeans colors')
def verify_jeans_color_selection(context):
    expected_colors = ['Black', 'Blue Overdyed', 'Dark Wash', 'Indigo Wash', 'Light Wash', 'Medium Wash', 'Rinse', 'Vintage Light Wash']
    color_options = context.driver.find_elements(*COLOR_OPTIONS)


    for x in range(len(color_options)):
        color_options[x].click()
        selected_color_text = context.driver.find_element(*SELECTED_COLOR).text
        assert selected_color_text == expected_colors[x]