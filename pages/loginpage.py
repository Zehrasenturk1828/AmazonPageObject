import pytest
from pages.constants.homepage_constants import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.constants.loginpage_constants import *


@pytest.mark.usefixtures("setup")
class LoginPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def send_email_to_input(self):
        email_input = self.wait_element_visibility(EMAIL_INPUT)
        email_input.send_keys(EMAIL)

    def click_continue_button(self):
        submit_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(CONTINUE_BUTTON))
        submit_button.click()

    def send_password_to_input(self):
        password_input = self.wait_element_visibility(PASSWORD_INPUT)
        password_input.send_keys(PASSWORD)

    def sign_in_button(self):
        signin_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(SIGN_IN_BUTTON))
        signin_button.click()