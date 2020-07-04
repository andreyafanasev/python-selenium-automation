from selenium.webdriver.common.by import By
from behave import when, then, given
from selenium.webdriver.support import expected_conditions as EC

BLOG_LINK = (By.XPATH, "//*[contains(text(),'blog.aboutamazon.com')]")
BLOG_WEB_SITE = (By.CSS_SELECTOR, "h1.ArticlePage-headline")
BLOG_MENU_BUTTON = (By.CSS_SELECTOR, "button.ArticlePage-header-menuToggle")
CLOSE_MENU = (By.CSS_SELECTOR, "button.ArticlePage-header-menuClose")
NAVIGATION_MENU = (By.CSS_SELECTOR, "div.ArticlePage-navigation-heading")


@when('Store original windows')
def Store_original_windows(context):
    context.original_windows = context.driver.window_handles
    context.original_window = context.driver.current_window_handle

@when('Click on blog link “See daily updates at blog.aboutamazon.com”')
def click_on_blog_link(context):
    context.driver.find_element(*BLOG_LINK).click()

@when('Switch to the newly opened window')
def switch_to_new_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    current_windows = context.driver.window_handles
    context.driver.switch_to_window(current_windows[1])

@then('Amazon Blog is opened')
def amazon_blog_is_opened(context):
    context.driver.find_element(*BLOG_WEB_SITE)

@then('User can open and close Blog menu')
def open_and_close_blog_menu(context):
    context.driver.find_element(*BLOG_MENU_BUTTON).click()
    context.driver.wait.until(EC.presence_of_element_located(NAVIGATION_MENU))
    context.driver.find_element(*CLOSE_MENU).click()
    context.driver.wait.until(EC.invisibility_of_element(NAVIGATION_MENU))

@then('User can close new window and switch back to original')
def switch_back_to_original(context):
    context.driver.close()
    context.driver.switch_to_window(context.original_window)