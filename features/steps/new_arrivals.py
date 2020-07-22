from behave import when, then
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


SIGN_IN_TOOLTIP = (By.ID, 'nav-signin-tooltip')


@when('Hover over New Arrivals link')
def hover_over_new_arrivals(context):
    context.driver.wait.until(EC.invisibility_of_element(SIGN_IN_TOOLTIP))
    context.app.product_page.hover_over_new_arrivals()

@then('Verify that the deals are shown')
def verify_deals_are_shown(context):
    context.app.product_page.verify_deals_are_shown()
