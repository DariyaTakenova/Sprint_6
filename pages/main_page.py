from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Локаторы
    FAQ_QUESTION = lambda self, index: (By.ID, f"accordion__heading-{index-1}")
    FAQ_ANSWER = lambda self, index: (By.ID, f"accordion__panel-{index-1}")
    LOGO_SCOOTER = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    LOGO_YANDEX = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
    TOP_ORDER_BUTTON = (By.XPATH, "//button[text()='Заказать' and not(ancestor::div[contains(@class,'middle'))]]")
    BOTTOM_ORDER_BUTTON = (By.XPATH, "//button[text()='Заказать' and ancestor::div[contains(@class,'middle')]]")

    # Д
