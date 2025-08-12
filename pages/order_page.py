import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from locators import OrderPageLocators

class OrderPage(BasePage):

    @allure.step("Заполнить персональные данные")
    def fill_personal_info(self, data):
        self.input_text(OrderPageLocators.FIRST_NAME, data["first_name"])
        self.input_text(OrderPageLocators.LAST_NAME, data["last_name"])
        self.input_text(OrderPageLocators.ADDRESS, data["address"])

        self.click(OrderPageLocators.METRO_FIELD)

        # Выбрать станцию метро из списка
        metro_option = (By.XPATH, f"//div[contains(@class, 'select-search__select')]//div[text()='{data['metro']}']")
        self.wait.until(EC.element_to_be_clickable(metro_option)).click()

        self.input_text(OrderPageLocators.PHONE, data["phone"])
        self.click(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Заполнить данные о самокате")
    def fill_scooter_info(self, data):
        self.input_text(OrderPageLocators.DATE_FIELD, data["date"])
        # Выбираем цвет чёрный (можно расширить, если надо)
        self.click(OrderPageLocators.SCOOTER_COLOR_BLACK)
        self.input_text(OrderPageLocators.COMMENT, data["comment"])
        self.click(OrderPageLocators.ORDER_BUTTON)
        self.click(OrderPageLocators.CONFIRM_BUTTON)

    @allure.step("Проверить, что модальное окно с подтверждением заказа отображается")
    def is_success_modal_visible(self):
        return "Заказ оформлен" in self.get_element(OrderPageLocators.SUCCESS_MODAL).text
