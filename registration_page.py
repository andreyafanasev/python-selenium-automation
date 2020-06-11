"""
Created by Andrei Afanasev
Home work 07/06/20
Find the most optimal locators for Create Account (Registration) page elements:


amazon_logo = (By.CSS_SELECTOR, ".a-icon-logo")
create_account_sign = (By.CSS_SELECTOR, "h1")
your_name_field = (By.ID, 'ap_customer_name')
email_field = (By.ID, 'ap_email')
password_field = (By.ID, 'ap_password')
password_massage = (By.XPATH, '//div[contains(@class, 'information-message')]/div[contains(@class, 'container')]/div[@class='a-alert-content']')
re_enter_password_field = (By.ID, 'ap_password_check')
create_account_button = (By.ID, 'continue')
condition_of_use_1 = (By.XPATH, '//a[contains(@href, 'condition_of_use')]')
privacy_notice_1 = (By.XPATH, '//div[@id='legalTextRow']/a[contains(@href, 'privacy_notice')]')
sign_in_link = (By.CSS_SELECTOR, "a[href*='signin']")

"""