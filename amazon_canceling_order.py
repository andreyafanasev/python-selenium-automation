from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome(executable_path='/Users/andrei/Automation/python-selenium-automation/chromedriver')
driver.maximize_window()

# open the page
driver.get('https://www.amazon.com/gp/help/customer/display.html')
driver.implicitly_wait(4)

input_field = driver.find_element(By.ID, 'helpsearch')
input_field.clear()
input_field.send_keys('Cancel order')


search_icon = driver.find_element(By.ID, 'helpSearchSubmit')
search_icon.click()

text = driver.find_element(By.XPATH, "//p[@class='a-color-secondary']/b").text

assert text == 'Cancel order', f'Incorrect text {text}.'

driver.quit()
