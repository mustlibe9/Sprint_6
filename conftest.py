import allure
import pytest
import urls
from selenium import webdriver


@pytest.fixture
def driver():
    with allure.step("Запуск браузера и приложения"):
        driver = webdriver.Firefox()
        driver.get(urls.SCOOTER_ORDER_APP_URL)

    yield driver

    with allure.step("Закрытие браузера"):
        driver.quit()
