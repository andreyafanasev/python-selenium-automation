from pages.base_page import Page
from selenium.webdriver.common.by import By


class SearchResults(Page):
    RESULTS_INFO_TEXT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")

    def verify_found_results_text(self, search_word: str):
        search_result_header = self.find_element(*self.RESULTS_INFO_TEXT).text
        assert search_word in search_result_header, f'Incorrect header {search_result_header}'
