from pages.base_page import Page
from pages.top_nav_menu import TopNavMenu
from pages.search_results_page import SearchResults
from pages.sign_in_page import SignIn
from pages.empty_cart_page import EmptyCart
from pages.hamburger_menu_page import HamburgerMenu
from pages.product_page import Product


class Application:

    def __init__(self, driver):
        self.driver = driver

        self.page = Page(self.driver)
        self.top_nav_menu = TopNavMenu(self.driver)
        self.search_results_page = SearchResults(self.driver)
        self.sign_in_page = SignIn(self.driver)
        self.empty_cart_page = EmptyCart(self.driver)
        self.hamburger_menu_page = HamburgerMenu(self.driver)
        self.product_page = Product(self.driver)