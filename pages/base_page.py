import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)  # Явные ожидания

    @allure.step("Открыть страницу: {url}")
    def open(self, url):
        """Открыть страницу по URL"""
        self.driver.get(url)

    @allure.step("Кликнуть по элементу: {locator}")
    def click(self, locator):
        """Кликнуть на элемент, когда он кликабелен"""
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    @allure.step("Ввести текст '{text}' в поле: {locator}")
    def input_text(self, locator, text):
        """Ввести текст в поле ввода"""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    @allure.step("Получить список элементов: {locator}")
    def get_elements(self, locator):
        """Получить список элементов"""
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    @allure.step("Получить элемент: {locator}")
    def get_element(self, locator):
        """Получить один элемент"""
        return self.wait.until(EC.presence_of_element_located(locator))

    @allure.step("Прокрутить страницу до элемента: {locator}")
    def scroll_to_element(self, locator):
        """Прокрутить страницу до элемента"""
        element = self.get_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    @allure.step("Ожидать переход на URL: {expected_url}")
    def wait_for_url(self, expected_url, timeout=10):
        """Ожидать, что текущий URL совпадет с expected_url"""
        self.wait.until(lambda d: d.current_url == expected_url)
