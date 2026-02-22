import urls
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def scroll_and_click(driver, elem_locator):
    element = WebDriverWait(driver, 1).until(
        EC.presence_of_element_located(elem_locator)
    )
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    WebDriverWait(driver, 1).until(EC.element_to_be_clickable(element)).click()


def is_new_tab_opened_with_correct_url(driver, expected_url):
    WebDriverWait(driver, 3).until(EC.number_of_windows_to_be(2))
    new_window = driver.window_handles[-1]

    driver.switch_to.window(new_window)

    WebDriverWait(driver, 3).until(EC.url_contains(urls.YANDEX_DZEN_URL))
    return expected_url in driver.current_url
