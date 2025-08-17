from selenium.webdriver.common.by import By

LISTPAGE_TITLE = (By.XPATH, "//*[@id='my-lists-tab']/a/div")
PRODUCT_NAME = (By.XPATH, "/html/body/div[2]/div[1]/div/div/div/div/div/div[2]/div[8]/div/div/ul/li[2]/span/div/div/div/div[2]/div[1]/div[3]/div[2]/h2")
DELETE_BUTTON = (By.XPATH, "//input[@name='submit.deleteItem']")