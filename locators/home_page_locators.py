from selenium.webdriver.common.by import By

HOME_HEADER_LOCATOR = (By.XPATH, "//div[contains(@class, 'Home_Header')]")

ORDER_NAVIGATION_BUTTON_LOCATOR = (
    By.XPATH,
    "//div[contains(@class, 'Header_Nav')]//button[contains(text(), 'Заказать')]",
)

ORDER_FINISH_BUTTON_LOCATOR = (
    By.XPATH,
    "//div[contains(@class, 'FinishButton')]//button[contains(text(), 'Заказать')]",
)
