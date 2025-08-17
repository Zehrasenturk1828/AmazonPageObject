import time

import pytest
from pages.homepage import *
from pages.loginpage import *
from pages.search_result_page import *
from pages.product_details_page import *
from pages.list_page import *
from tests.conftest import *
import softest

@pytest.mark.usefixtures("setup")
class TestCheckofProductAddtoWishlist(softest.TestCase):
    def test_check_of_product_add_to_basket(self):
        home_page = HomePage(self.driver)
        home_page.click_continue_shopping_button()
        home_page.load_homepage_with_refresh()
        self.assertEqual(HOME_PAGE_URL, home_page.get_URL(), "Amazon homepage didn't open.")
        home_page.click_dismiss_shipping()
        home_page.click_login_button()

        login_page = LoginPage(self.driver)
        login_page.send_email_to_input()
        login_page.click_continue_button()
        login_page.send_password_to_input()
        login_page.sign_in_button()
        self.assertEqual(LOGIN_PAGE_URL, login_page.get_URL(), "Amazon loginpage didn't open.")
        home_page.send_keywords_to_search_input()
        home_page.click_submit_button()

        search_result_page = SearchResultPage(self.driver)
        self.assertIn("samsung", search_result_page.verify_result_page(), "Result Page is wrong")
        search_result_page.click_second_page()
        search_result_page.verify_page_number()
        search_result_page.click_a_product()

        productdetailspage = ProductDetailsPage(self.driver)
        productdetailspagename = productdetailspage.get_product_name()
        productdetailspage.click_add_to_list()
        productdetailspage.click_view_list()

        listpage = ListPage(self.driver)
        listpage_pname = listpage.verify_product()
        self.assertEqual(productdetailspagename, listpage_pname, "Product is wrong")
        listpage.delete_product_from_list()
        listpage.load_page_with_refresh()
        listpage.is_product_removed(listpage_pname)








