import locators.base_page_locators as locators
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    DEFAULT_WAIT_TIMEOUT = 5

    def __init__(self, driver):
        self._driver = driver

    def _find_element(self, locator):
        return self._driver.find_element(*locator)

    def _switch_to_the_last_tab(self):
        last_window = self._driver.window_handles[-1]
        self._driver.switch_to.window(last_window)

    def _wait(self, timeout=DEFAULT_WAIT_TIMEOUT):
        return WebDriverWait(self._driver, timeout)

    def _wait_until_visible(self, locator):
        return self._wait().until(EC.visibility_of_element_located(locator))

    def _wait_until_url_contains(self, url_part):
        return self._wait().until(EC.url_contains(url_part))

    def _wait_until_element_on_page(self, elem_locator):
        return self._wait().until(EC.presence_of_element_located(elem_locator))

    def _wait_until_element_clickable(self, element):
        return self._wait().until(EC.element_to_be_clickable(element))

    def _wait_for_second_tab(self):
        return self._wait().until(EC.number_of_windows_to_be(2))

    def _scroll_to_element(self, element):
        self._driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )

    def _scroll_and_click(self, elem_locator):
        element = self._wait_until_element_on_page(elem_locator)
        self._scroll_to_element(element)
        self._wait_until_element_clickable(element).click()

    @allure.step("Проверка открытия новой вкладки с URL {expected_url}")
    def is_new_tab_opened_with_correct_url(self, expected_url):
        self._wait_for_second_tab()
        self._switch_to_the_last_tab()
        self._wait_until_url_contains(expected_url)
        return self.is_url_contains_part(expected_url)

    @allure.step("Проверка, что URL содержит {url_part}")
    def is_url_contains_part(self, url_part):
        return url_part in self._driver.current_url

    @allure.step("Кликнуть по логотипу 'Самокат'")
    def click_on_scooter_main_logo(self):
        self._find_element(locators.SCOOTER_LOGO_LOCATOR).click()

    @allure.step("Кликнуть по логотипу 'Яндекс'")
    def click_on_yandex_logo(self):
        self._find_element(locators.YANDEX_LOGO_LOCATOR).click()
