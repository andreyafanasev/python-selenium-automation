from selenium.webdriver.common.by import By
from behave import given, then

COLOR_OPTIONS = (By.CSS_SELECTOR, "div#variation_color_name li")
SELECTED_COLOR = (By.CSS_SELECTOR, "div#variation_color_name span.selection")


@given('Open Amazon Dress {productid} page')
def open_dress_page(context, productid):
    context.driver.get(f'https://www.amazon.com/gp/product/{productid}/')


@then('Verify user can select through the colors')
def verify_color_selection(context):
    expected_colors = ['Emerald', 'Ivory', 'Navy']
    color_options = context.driver.find_elements(*COLOR_OPTIONS)
    print('OPTIONS: ', color_options)

    # for color in color_options:
    #     print('Color element: ', color)
    #     color.click()
    #     assert context.driver.find_element(*SELECTED_COLOR).text == expected_colors[color_options.index(color)]

    for x in range(len(color_options)):
        color_options[x].click()
        selected_color_text = context.driver.find_element(*SELECTED_COLOR).text
        assert selected_color_text == expected_colors[x]