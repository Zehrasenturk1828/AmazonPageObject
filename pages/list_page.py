import pytest
from selenium.common import TimeoutException

from pages.constants.homepage_constants import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.constants.searchresultpage_constants import *
from pages.constants.listpage_constants import *
@pytest.mark.usefixtures("setup")

class ListPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def verify_product(self):
        product_name = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(PRODUCT_NAME))
        return product_name.text.strip()

    def delete_product_from_list(self):
        delete_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(DELETE_BUTTON))
        delete_button.click()

    def load_page_with_refresh(self):
        self.driver.refresh()

    def is_product_removed(self, product_name):
        try:
            WebDriverWait(self.driver, 10).until_not(
                EC.presence_of_element_located((PRODUCT_NAME.text.strip()))
            )
            return True
        except:
            return False

