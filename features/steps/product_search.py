from behave import given, when, then
from time import sleep


@given('Open Amazon product {product_id} page')
def open_product(context, product_id):
    context.app.product_page.open_product(product_id)


@given('Open Amazon page')
def open_amazon(context):
    context.app.page.open_page()


@when('Search for {search_word}')
def input_search(context, search_word):
    context.app.top_nav_menu.search_word(search_word)


@then('Product results for {search_word} are shown')
def verify_found_results_text(context, search_word):
    context.app.search_results_page.verify_found_results_text(search_word)


@when('Select {alias} department')
def select_department(context, alias):
    context.app.top_nav_menu.select_department(alias)


@then('{selected_dep} department is selected')
def verify_selected_department(context, selected_dep):
    context.app.top_nav_menu.verify_selected_department(selected_dep)