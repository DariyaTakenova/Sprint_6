import allure
from pages.main_page import MainPage
from locators import MainPageLocators
from data import BASE_URL
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.title("Проверка раскрытия вопросов FAQ и отображения ответов")
def test_faq_answers_visible(driver):
    main = MainPage(driver)

    with allure.step("Открыть главную страницу"):
        main.open_main_page(BASE_URL)

    faq_questions = main.get_faq_questions()

    for index, question in enumerate(faq_questions):
        with allure.step(f"Клик по вопросу FAQ №{index + 1}"):
            question.click()

        with allure.step(f"Проверка отображения ответа на вопрос №{index + 1}"):
            # Правильно формируем локатор для конкретного ответа
            answer_xpath = f"({MainPageLocators.FAQ_ANSWERS[1]})[{index + 1}]"
            answer_locator = (By.XPATH, answer_xpath)
            answer_element = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located(answer_locator)
            )
            assert answer_element.is_displayed(), f"Ответ на вопрос {index + 1} не отображается"
