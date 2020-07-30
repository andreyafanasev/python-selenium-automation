import allure

bs_user = 'andreiafanasev1'
bs_pw = 'd1DmdqqMKTXypzLdxRkY'

from selenium import webdriver
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application
from features.logger import MyListener, logger


def browser_init(context, name):
    """
    :param context: Behave context
    """
    # context.driver = webdriver.Chrome(executable_path='/Users/andrei/Automation/python-selenium-automation/chromedriver')
    # context.driver = webdriver.Safari()
    # context.driver = webdriver.Firefox(executable_path='/Users/andrei/Automation/python-selenium-automation/geckodriver')

    """
    Headless mode
    """
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # context.driver = webdriver.Chrome(executable_path='/Users/andrei/Automation/python-selenium-automation/chromedriver', chrome_options=options)

    """
    EventFiringWebDriver
    """
    # context.driver = EventFiringWebDriver(webdriver.Chrome(executable_path='/Users/andrei/Automation/python-selenium-automation/chromedriver'), MyListener())

    """
    BrowserStack
    """

    desired_cap = {

        'os': 'Windows',
        'os_version': '10',
        'browser': 'Chrome',
        'browser_version': '80',
        'name': name

    }
    BROWSERSTACK_URL = f'http://{bs_user}:{bs_pw}@hub-cloud.browserstack.com/wd/hub'
    context.driver = webdriver.Remote(command_executor=BROWSERSTACK_URL, desired_capabilities=desired_cap)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.app = Application(context.driver)

    context.driver.wait = WebDriverWait(context.driver, 15)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    # logger.info(f'\nStarted scenario: {scenario.name}')
    browser_init(context, scenario.name)


def before_step(context, step):
    # logger.info(f'\nStarted step: {step.name}')
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()