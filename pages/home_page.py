import urls
import locators.home_page_locators as locators
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import scroll_and_click
from pages.base_page import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def _question_locator(self, index):
        return (By.ID, f"accordion__heading-{index}")

    def _answer_locator(self, index):
        return (By.XPATH, f"//div[@id='accordion__panel-{index}']//p")

    @allure.step("Кликнуть по вопросу {question_index}")
    def click_question(self, question_index):
        question_locator = self._question_locator(question_index)
        scroll_and_click(self.driver, question_locator)

    @allure.step("Получить текст ответа {answer_index}")
    def get_answer_text(self, answer_index):
        return (
            self.wait()
            .until(EC.visibility_of_element_located(self._answer_locator(answer_index)))
            .text
        )

    @allure.step("Кликнуть на вопрос и получить текст ответа")
    def get_answer_text_after_question_click(self, question_index):
        self.click_question(question_index)
        return self.get_answer_text(question_index)

    @allure.step("Нажать кнопку 'Заказать' в навигационной панели")
    def click_order_from_navigation_bar(self):
        self.driver.find_element(*locators.ORDER_NAVIGATION_BUTTON_LOCATOR).click()
        self.wait_order_url_active()

    @allure.step("Нажать кнопку 'Заказать' в нижнем блоке страницы")
    def click_order_from_roadmap(self):
        scroll_and_click(self.driver, locators.ORDER_FINISH_BUTTON_LOCATOR)
        self.wait_order_url_active()

    @allure.step("Ожидание перехода на страницу заказа")
    def wait_order_url_active(self):
        self.wait().until(EC.url_contains(urls.ORDER_PAGE_PATH))

    @allure.step("Проверить отображение главной страницы")
    def is_home_page_active(self):
        return self.wait().until(
            EC.visibility_of_element_located(locators.HOME_HEADER_LOCATOR)
        )
