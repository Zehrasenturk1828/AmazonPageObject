from selenium.webdriver.common.by import By

CONTINUE_SHOPPING = (By.XPATH, "//button[@alt='Continue shopping']")
COOKIES_BUTTON = (By.ID, "sp-cc-accept")
HOME_PAGE_URL = "https://www.amazon.com/"
ACCOUNT_BUTTON = (By.XPATH, "//span[@id='nav-link-accountList-nav-line-1']")
DISMISS_DELIVER = (By.XPATH, "/html/body/div[1]/header/div/div[2]/div[2]/div/div[3]/span[1]/span/input")
SEARCH_INPUT = (By.XPATH, "/html/body/div[1]/header/div[1]/div[1]/div[2]/div/form/div[2]/div[1]/input")
SEARCH_KEYWORDS = "samsung"
SEARCH_RESULT_PAGE_CONFIRM = "//span[@class='a-color-state a-text-bold']"
SUBMIT_BUTTON = (By.ID, "nav-search-submit-button")