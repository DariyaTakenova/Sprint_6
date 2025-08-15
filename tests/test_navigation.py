import allure
from pages.main_page import MainPage
from data import BASE_URL


@allure.feature("Навигация")
class TestNavigation:

    @allure.title("Проверка перехода по логотипу 'Самокат'")
    def test_logo_scooter_redirect(self, driver):
        main = MainPage(driver)

        with allure.step("Открыть главную страницу"):
            main.open_main_page(BASE_URL)

        with allure.step("Клик по логотипу 'Самокат'"):
            main.click_logo_scooter()

        assert main.is_redirect_to_main_page(BASE_URL)

    @allure.title("Проверка перехода по логотипу 'Яндекс'")
    def test_logo_yandex_redirect(self, driver):
        main = MainPage(driver)

        with allure.step("Открыть главную страницу"):
            main.open_main_page(BASE_URL)

        with allure.step("Клик по логотипу 'Яндекс'"):
            main.click_logo_yandex()

        assert main.is_redirect_to_yandex()
