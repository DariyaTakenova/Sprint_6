import allure
from .base_page import BasePage
from locators import MainPageLocators

class MainPage(BasePage):

    @allure.step("Открыть главную страницу")
    def open_main_page(self, url):
        self.open(url)

    @allure.step("Клик по верхней кнопке 'Заказать'")
    def click_top_order_button(self):
        self.click(MainPageLocators.TOP_ORDER_BUTTON)

    @allure.step("Клик по нижней кнопке 'Заказать'")
    def click_bottom_order_button(self):
        self.click(MainPageLocators.BOTTOM_ORDER_BUTTON)

    @allure.step("Прокрутить страницу до нижней кнопки 'Заказать'")
    def scroll_to_bottom_order_button(self):
        self.scroll_to_element(MainPageLocators.BOTTOM_ORDER_BUTTON)

    @allure.step("Получение списка вопросов FAQ")
    def get_faq_questions(self):
        return self.get_elements(MainPageLocators.FAQ_QUESTIONS)

    @allure.step("Получение списка ответов FAQ")
    def get_faq_answers(self):
        return self.get_elements(MainPageLocators.FAQ_ANSWERS)

    @allure.step("Клик по логотипу 'Самокат'")
    def click_logo_scooter(self):
        self.click(MainPageLocators.LOGO_SCOOTER)

    @allure.step("Клик по логотипу 'Яндекс'")
    def click_logo_yandex(self):
        self.click(MainPageLocators.LOGO_YANDEX)
