from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)  # Явные ожидания

    def open(self, url):
        """Открыть страницу по URL"""
        self.driver.get(url)

    def click(self, locator):
        """Кликнуть на элемент, когда он кликабелен"""
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def input_text(self, locator, text):
        """Ввести текст в поле ввода"""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_elements(self, locator):
        """Получить список элементов"""
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def get_element(self, locator):
        """Получить один элемент"""
        return self.wait.until(EC.presence_of_element_located(locator))

    def scroll_to_element(self, locator):
        """Прокрутить страницу до элемента"""
        element = self.get_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def wait_for_url(self, expected_url, timeout=10):
        """Ожидать, что текущий URL совпадет с expected_url"""
        self.wait.until(lambda d: d.current_url == expected_url)
