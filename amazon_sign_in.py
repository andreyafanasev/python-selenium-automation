from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

amazon_logo = (By.XPATH, '//i[@aria-label='Amazon']')
email_field = (By.XPATH, '//input[@type='email']')
continue_button = (By.ID, 'continue')
need_help_button = (By.XPATH, '//span[@class='a-expander-prompt']')
forgot_password = (By.ID, 'auth-fpp-link-bottom')
other_issue = (By.ID, 'ap-other-signin-issues-link')
create_acc = (By.ID, 'createAccountSubmit')
conditions_of_use = (By.XPATH, '//div[@class='a-section a-spacing-small a-text-center a-size-mini']/a[contains(@href, '508088')]')
privacy_notice = (By.XPATH, '//div[@class='a-section a-spacing-small a-text-center a-size-mini']/a[contains(@href, '468496')]')
