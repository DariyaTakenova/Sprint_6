import pytest
import allure
from pages.main_page import MainPage
from data import BASE_URL


@allure.feature("FAQ")
class TestFAQ:

    @pytest.mark.parametrize("question_index", range(1, 9))  # если вопросов 8
    @allure.title("Проверка раскрытия вопроса FAQ и отображения ответа")
    def test_faq_answers_visible(self, driver, question_index):
        main = MainPage(driver)

        with allure.step("Открыть главную страницу"):
            main.open_main_page(BASE_URL)

        with allure.step(f"Клик по вопросу FAQ №{question_index}"):
            main.click_faq_question(question_index)

        with allure.step(f"Проверка отображения ответа на вопрос №{question_index}"):
            assert main.is_faq_answer_visible(question_index), \
                f"Ответ на вопрос {question_index} не отображается"
