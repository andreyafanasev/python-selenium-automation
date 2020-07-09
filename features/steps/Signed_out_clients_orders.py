from behave import given, when, then


@when('Click on Orders icon')
def click_orders_icon(context):
    context.app.sign_in_page.click_orders()


@then('Logged out user sees Sign in page')
def verify_found_results_text(context):
    context.app.sign_in_page.verify_sign_in_text()