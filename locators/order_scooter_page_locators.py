from selenium.webdriver.common.by import By

NAME_LOCATOR = (By.XPATH, "//input[contains(@placeholder, 'Имя')]")

SURNAME_LOCATOR = (By.XPATH, "//input[contains(@placeholder, 'Фамилия')]")

ADDRESS_LOCATOR = (By.XPATH, "//input[contains(@placeholder, 'Адрес')]")

SUBWAY_STATION_LOCATOR = (
    By.XPATH,
    "//input[contains(@placeholder, 'Станция метро')]",
)

PHONE_LOCATOR = (By.XPATH, "//input[contains(@placeholder, 'Телефон')]")

NEXT_BUTTON_LOCATOR = (By.XPATH, "//button[text()='Далее']")

ABOUT_RENT_HEADER_LOCATOR = (By.XPATH, "//div[text()='Про аренду']")

DELIVERY_DATE_LOCATOR = (
    By.XPATH,
    "//input[contains(@placeholder, 'Когда привезти самокат')]",
)

RENT_PERIOD_LOCATOR = (By.XPATH, "//div[text()='* Срок аренды']")

COMMENT_LOCATOR = (By.XPATH, "//input[contains(@placeholder, 'Комментарий')]")

FINISH_ORDER_BUTTON = (
    By.XPATH,
    "//div[contains(@class,'Order_Buttons')]//button[text()='Заказать']",
)

ORDER_CONFIRMATION_HEADER_LOCATOR = (
    By.XPATH,
    "//div[contains(@class, 'Order_ModalHeader')]",
)

ORDER_CONFIRMATION_BUTTON_LOCATOR = (By.XPATH, "//button[text()='Да']")

ORDER_DONE_HEADER_LOCATOR = (By.XPATH, "//div[text()='Заказ оформлен']")
