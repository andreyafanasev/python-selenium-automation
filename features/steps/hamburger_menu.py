from behave import given, when, then


@when('Click on hamburger menu')
def click_ham_menu(context):
    context.app.hamburger_menu_page.ham_menu()


@when('Click on Amazon Music menu item')
def click_amazon_music(context):
    context.app.hamburger_menu_page.amaz_music()


@then('{expected_item_count} menu items are present')
def verify_amount_of_items(context, expected_item_count):
    context.app.hamburger_menu_page.amount_of_items(expected_item_count)
