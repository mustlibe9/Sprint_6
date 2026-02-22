import allure
import pytest
from pages.home_page import HomePage
from input_test_data.important_questions_data import ANSWERS


@allure.feature("Главная страница")
@allure.story("Блок 'Вопросы о важном'")
class TestImportantQuestions:

    @allure.title("Проверка ответа на вопрос №{question_index}")
    @allure.description(
        "Проверяем, что при клике на вопрос на определенной позиции раскрывается корректный текст ответа"
    )
    @pytest.mark.parametrize("question_index, expected_answer_text", ANSWERS)
    def test_click_question_get_answer(
        self, driver, question_index, expected_answer_text
    ):
        question_page = HomePage(driver)
        answer_text = question_page.get_answer_text_after_question_click(question_index)
        assert answer_text == expected_answer_text
