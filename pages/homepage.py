import pytest
from pages.constants.homepage_constants import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
@pytest.mark.usefixtures("setup")

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_continue_shopping_button(self):
        continue_shopping = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(CONTINUE_SHOPPING))
        continue_shopping.click()


    def load_homepage_with_refresh(self):
        self.driver.get(HOME_PAGE_URL)
        self.driver.refresh()

    def click_dismiss_shipping(self):
        dismiss_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(DISMISS_DELIVER))
        dismiss_button.click()

    def click_cookies(self):
        cookies_button = self.wait_element_visibility(COOKIES_BUTTON)
        cookies_button.click()

    def click_login_button(self):
        account_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(ACCOUNT_BUTTON))
        account_button.click()

    def send_keywords_to_search_input(self):
        search_input = self.wait_element_visibility(SEARCH_INPUT)
        search_input.send_keys(SEARCH_KEYWORDS)

    def click_submit_button(self):
        submit_button = self.wait_element_visibility(SUBMIT_BUTTON)
        submit_button.click()
