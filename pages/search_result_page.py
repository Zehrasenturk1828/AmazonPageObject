import pytest
from pages.constants.homepage_constants import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.constants.searchresultpage_constants import *
@pytest.mark.usefixtures("setup")

class SearchResultPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def verify_result_page(self):
        title = self.wait_element_presence(TITLE)
        return title.text

    def click_second_page(self):
        second_page = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(PAGINATION_BUTTON_2))
        second_page.click()

    def verify_page_number(self):
        nav_button = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(SELECTED_PAGINATION_2))
        return nav_button.text

    def click_a_product(self):
        products = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(FIND_PRODUCT))
        products[2].click()




