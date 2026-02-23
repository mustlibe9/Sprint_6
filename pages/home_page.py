import urls
import locators.home_page_locators as locators
import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):

    def _question_locator(self, index):
        return (By.ID, f"accordion__heading-{index}")

    def _answer_locator(self, index):
        return (By.XPATH, f"//div[@id='accordion__panel-{index}']//p")

    @allure.step("Кликнуть по вопросу {question_index}")
    def click_question(self, question_index):
        question_locator = self._question_locator(question_index)
        self._scroll_and_click(question_locator)

    @allure.step("Получить текст ответа {answer_index}")
    def get_answer_text(self, answer_index):
        answer_locator = self._answer_locator(answer_index)
        return self._wait_until_visible(answer_locator).text

    @allure.step("Кликнуть на вопрос и получить текст ответа")
    def get_answer_text_after_question_click(self, question_index):
        self.click_question(question_index)
        return self.get_answer_text(question_index)

    @allure.step("Нажать кнопку 'Заказать' в навигационной панели")
    def click_order_from_navigation_bar(self):
        self._find_element(locators.ORDER_NAVIGATION_BUTTON_LOCATOR).click()
        self.wait_order_url_active()

    @allure.step("Нажать кнопку 'Заказать' в нижнем блоке страницы")
    def click_order_from_roadmap(self):
        self._scroll_and_click(locators.ORDER_FINISH_BUTTON_LOCATOR)
        self.wait_order_url_active()

    @allure.step("Ожидание перехода на страницу заказа")
    def wait_order_url_active(self):
        self._wait_until_url_contains(urls.ORDER_PAGE_PATH)

    @allure.step("Проверить отображение главной страницы")
    def is_home_page_active(self):
        return self._wait_until_visible(locators.HOME_HEADER_LOCATOR)
