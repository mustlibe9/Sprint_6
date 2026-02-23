import urls
import allure
from pages.home_page import HomePage


@allure.feature("Навигация по сайту")
class TestNavigationActions:

    @allure.story("Переход на страницу заказа")
    @allure.title("Переход на страницу заказа через кнопку в навигационной панели")
    def test_click_order_in_navigation_go_to_order(self, driver):
        home_page = HomePage(driver)
        home_page.click_order_from_navigation_bar()
        assert home_page.is_url_contains_part(urls.ORDER_PAGE_PATH)

    @allure.story("Переход на страницу заказа")
    @allure.title("Переход на страницу заказа через кнопку в блоке Roadmap")
    def test_click_order_in_roadmap_go_to_order(self, driver):
        home_page = HomePage(driver)
        home_page.click_order_from_roadmap()
        assert home_page.is_url_contains_part(urls.ORDER_PAGE_PATH)

    @allure.story("Возврат на главную страницу")
    @allure.title("Возврат на главную страницу по клику на логотип 'Самокат'")
    def test_go_to_home_page_after_click_scooter_logo(self, driver):
        home_page = HomePage(driver)
        home_page.click_order_from_navigation_bar()
        home_page.click_on_scooter_main_logo()
        assert home_page.is_home_page_active()

    @allure.story("Открытие внешней ссылки")
    @allure.title("Открытие новой вкладки при клике на логотип 'Яндекс'")
    @allure.link(urls.YANDEX_DZEN_URL, name="Ожидаемая ссылка Яндекс.Дзен")
    def test_new_yandex_tab_after_click_yandex_logo(self, driver):
        home_page = HomePage(driver)
        home_page.click_on_yandex_logo()
        assert home_page.is_new_tab_opened_with_correct_url(urls.YANDEX_DZEN_URL)
