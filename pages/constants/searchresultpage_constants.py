from selenium.webdriver.common.by import By

TITLE = (By.XPATH, "/html/body/div[1]/div[1]/span/div/h1/div/div[1]/div/h2/span[3]")
PAGINATION_BUTTON_2 = (By.CSS_SELECTOR, "a[aria-label='Go to page 2']")
SELECTED_PAGINATION_2 = (By.CSS_SELECTOR, "span[aria-label='Page 2']")
FIND_PRODUCT = (By.CSS_SELECTOR, "[role=listitem] [data-component-type='s-product-image'] a")
