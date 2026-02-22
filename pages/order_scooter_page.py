import locators.order_scooter_page_locators as locators
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys


class OrderScooterPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def _subway_station_option_locator(self, station_name):
        return (By.XPATH, f"//div[text()='{station_name}']")

    def _rent_period_option_locator(self, rent_period_name):
        return (By.XPATH, f"//div[text()='{rent_period_name}']")

    def _color_option_locator(self, color_name):
        return (By.ID, color_name)

    @allure.step("Ввести имя: {name}")
    def enter_name(self, name):
        self.driver.find_element(*locators.NAME_LOCATOR).send_keys(name)

    @allure.step("Ввести фамилию: {surname}")
    def enter_surname(self, surname):
        self.driver.find_element(*locators.SURNAME_LOCATOR).send_keys(surname)

    @allure.step("Ввести адрес: {address}")
    def enter_address(self, address):
        self.driver.find_element(*locators.ADDRESS_LOCATOR).send_keys(address)

    @allure.step("Выбрать станцию метро: {station_name}")
    def choose_subway_station(self, station_name):
        element = self.driver.find_element(*locators.SUBWAY_STATION_LOCATOR)
        element.click()
        element.send_keys(station_name)
        WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(
                self._subway_station_option_locator(station_name)
            )
        ).click()

    @allure.step("Ввести телефон: {phone}")
    def enter_phone(self, phone):
        self.driver.find_element(*locators.PHONE_LOCATOR).send_keys(phone)

    @allure.step("Нажать кнопку 'Далее'")
    def push_next_button(self):
        self.driver.find_element(*locators.NEXT_BUTTON_LOCATOR).click()
        self.wait().until(
            EC.visibility_of_element_located(locators.ABOUT_RENT_HEADER_LOCATOR)
        )

    @allure.step("Ввести дату доставки: {date}")
    def enter_delivery_date(self, date):
        element = self.driver.find_element(*locators.DELIVERY_DATE_LOCATOR)
        element.send_keys(date)
        element.send_keys(Keys.ESCAPE)

    @allure.step("Выбрать срок аренды: {rent_period_name}")
    def choose_rent_period(self, rent_period_name):
        self.driver.find_element(*locators.RENT_PERIOD_LOCATOR).click()
        option_locator = self._rent_period_option_locator(rent_period_name)
        self.wait().until(
            EC.visibility_of_element_located(option_locator)
        ).click()

    @allure.step("Выбрать цвета: {colors_ids}")
    def choose_colors(self, colors_ids):
        for id in colors_ids:
            self.driver.find_element(*self._color_option_locator(id)).click()

    @allure.step("Ввести комментарий: {comment}")
    def enter_comment(self, comment):
        self.driver.find_element(*locators.COMMENT_LOCATOR).send_keys(comment)

    @allure.step("Нажать кнопку 'Заказать'")
    def push_order_button(self):
        self.driver.find_element(*locators.FINISH_ORDER_BUTTON).click()
        self.wait().until(
            EC.visibility_of_element_located(locators.ORDER_CONFIRMATION_HEADER_LOCATOR)
        )

    @allure.step("Подтвердить заказ")
    def complete_order(self):
        self.driver.find_element(*locators.ORDER_CONFIRMATION_BUTTON_LOCATOR).click()
        element = self.wait().until(
            EC.visibility_of_element_located(locators.ORDER_DONE_HEADER_LOCATOR)
        )
        return element.is_displayed()

    @allure.step("Полностью оформить заказ")
    def make_order(self, order):
        self.enter_name(order.name)
        self.enter_surname(order.surname)
        self.enter_address(order.address)
        self.choose_subway_station(order.subway)
        self.enter_phone(order.phone)
        self.push_next_button()
        self.enter_delivery_date(order.delivery_date)
        self.choose_rent_period(order.rent_period)
        self.choose_colors(order.colors)
        self.enter_comment(order.comment)
        self.push_order_button()
        return self.complete_order()
