import pytest
from pages.constants.homepage_constants import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.constants.productdetailspage_constants import *
@pytest.mark.usefixtures("setup")

class ProductDetailsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_add_to_list(self):
        addtolist = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(ADD_TO_LIST))
        addtolist.click()

    def click_view_list(self):
        view_list = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(VIEW_LIST))
        view_list.click()

    def get_product_name(self):
        product = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(PRODUCT_NAME))
        return product.text.strip()

