from behave import given, when, then


@when('Click on cart icon')
def click_on_cart_icon(context):
    context.app.empty_cart_page.click_cart_icon()


@then('User sees that cart is empty')
def verify_found_results_text(context):
    context.app.empty_cart_page.verify_empty_cart_text()