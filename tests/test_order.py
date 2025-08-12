import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import BASE_URL, ORDER_DATA_SETS

@allure.feature("Заказ самоката")
@pytest.mark.parametrize("order_data, button_click", [
    (ORDER_DATA_SETS[0], "top"),
    (ORDER_DATA_SETS[1], "bottom"),
])
@allure.title("Проверка оформления заказа через верхнюю и нижнюю кнопку 'Заказать'")
def test_order_flow(driver, order_data, button_click):
    main = MainPage(driver)
    order = OrderPage(driver)

    with allure.step("Открыть главную страницу"):
        main.open_main_page(BASE_URL)

    if button_click == "top":
        with allure.step("Нажать верхнюю кнопку 'Заказать'"):
            main.click_top_order_button()
    else:
        with allure.step("Прокрутить до нижней кнопки и нажать 'Заказать'"):
            main.scroll_to_bottom_order_button()
            main.click_bottom_order_button()

    with allure.step("Заполнить персональные данные"):
        order.fill_personal_info(order_data)

    with allure.step("Заполнить данные о самокате"):
        order.fill_scooter_info(order_data)

    with allure.step("Проверить успешное оформление заказа"):
        assert order.is_success_modal_visible()
