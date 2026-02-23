import pytest
import allure
from pages.order_scooter_page import OrderScooterPage
from pages.home_page import HomePage
from input_test_data.order_scooter_data import ORDER_DATA, OrderStartButton


@allure.feature("Оформление заказа")
@allure.story("Позитивный сценарий заказа самоката")
class TestOrderScooter:

    @allure.title(
        "Успешное оформление заказа для пользователя {order.name} {order.surname}"
    )
    @allure.description(
        "Проверяем, что пользователь может успешно оформить заказ самоката "
        "с корректными данными."
    )
    @pytest.mark.parametrize("order", ORDER_DATA)
    def test_order_scooter_successful(self, driver, order):
        home_page = HomePage(driver)

        match order.start_button:
            case OrderStartButton.NAVIGATION_BUTTON:
                home_page.click_order_from_navigation_bar()
            case OrderStartButton.ROADMAP_FINISH_BUTTON:
                home_page.click_order_from_roadmap()
            case _:
                raise ValueError("Неизвестное значение стартовой кнопки заказ")

        order_page = OrderScooterPage(driver)
        assert order_page.make_order(order)
