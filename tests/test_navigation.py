# test_navigation.py
import allure
from pages.main_page import MainPage
from locators import MainPageLocators
from data import BASE_URL
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.title("Проверка перехода по логотипу 'Самокат'")
def test_logo_scooter_redirect(driver):
    main = MainPage(driver)
    main.open_main_page(BASE_URL)

    with allure.step("Клик по логотипу 'Самокат'"):
        main.click_logo_scooter()

    WebDriverWait(driver, 5).until(lambda d: d.current_url == BASE_URL)
    assert driver.current_url == BASE_URL

@allure.title("Проверка перехода по логотипу 'Яндекс'")
def test_logo_yandex_redirect(driver):
    main = MainPage(driver)
    main.open_main_page(BASE_URL)

    with allure.step("Клик по логотипу 'Яндекс'"):
        main.click_logo_yandex()

    driver.switch_to.window(driver.window_handles[-1])
    WebDriverWait(driver, 5).until(EC.url_contains("dzen.ru"))
    assert "dzen.ru" in driver.current_url
