import locators.base_page_locators as locators
import allure
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    WAIT_TIMEOUT = 3

    def __init__(self, driver):
        self.driver = driver

    def wait(self):
        return WebDriverWait(self.driver, self.WAIT_TIMEOUT)

    @allure.step("Кликнуть по логотипу 'Самокат'")
    def click_on_scooter_main_logo(self):
        self.driver.find_element(*locators.SCOOTER_LOGO_LOCATOR).click()

    @allure.step("Кликнуть по логотипу 'Яндекс'")
    def click_on_yandex_logo(self):
        self.driver.find_element(*locators.YANDEX_LOGO_LOCATOR).click()
