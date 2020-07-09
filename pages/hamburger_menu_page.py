from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class HamburgerMenu(Page):

    HAM_MENU = (By.ID, 'nav-hamburger-menu')
    AMAZON_MUSIC_MENU_ITEM = (By.XPATH, "//ul[contains(@class, 'hmenu-visible')]//div[contains(text(), 'Amazon Music')]")
    AMAZON_MUSIC_MENU_ITEM_RESULTS = (By.CSS_SELECTOR, "ul.hmenu-visible a:not(.hmenu-back-button)")

    def ham_menu(self):
        self.driver.find_element(*self.HAM_MENU).click()

    def amaz_music(self):
        self.driver.wait.until(EC.element_to_be_clickable(self.AMAZON_MUSIC_MENU_ITEM)).click()

    def amount_of_items(self, expected_item_count):
        expected_item_count = int(expected_item_count)
        self.driver.wait.until(EC.visibility_of_all_elements_located(self.AMAZON_MUSIC_MENU_ITEM_RESULTS))
        actual = len(self.driver.find_elements(*self.AMAZON_MUSIC_MENU_ITEM_RESULTS))
        assert expected_item_count == actual, f'Expected {expected_item_count} items, but got {actual} items'