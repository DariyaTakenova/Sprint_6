import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import BASE_URL, ORDER_DATA_SETS


@allure.feature("Заказ самоката")
class TestOrderFlow:

    @pytest.mark.parametrize("order_data, click_method", [
        (ORDER_DATA_SETS[0], MainPage.click_top_order_button),
        (ORDER_DATA_SETS[1], MainPage.click_bottom_order_button_with_scroll),
    ])
    @allure.title("Проверка оформления заказа через верхнюю и нижнюю кнопку 'Заказать'")
    def test_order_flow(self, driver, order_data, click_method):
        main = MainPage(driver)
        order = OrderPage(driver)

        with allure.step("Открыть главную страницу"):
            main.open_main_page(BASE_URL)

        with allure.step("Нажать кнопку 'Заказать'"):
            click_method(main)

        with allure.step("Заполнить персональные данные"):
            order.fill_personal_info(order_data)

        with allure.step("Заполнить данные о самокате"):
            order.fill_scooter_info(order_data)

        with allure.step("Проверить успешное оформление заказа"):
            assert order.is_success_modal_visible()
