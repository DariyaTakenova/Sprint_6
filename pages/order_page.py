from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrderPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Локаторы
    FIRST_NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION = (By.CLASS_NAME, "select-search__input")
    PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    DELIVERY_DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_DROPDOWN = (By.CLASS_NAME, "Dropdown-placeholder")
    RENTAL_PERIOD_OPTION = lambda self, text: (By.XPATH, f"//div[@class='Dropdown-menu']//div[text()='{text}']")
    COLOR_CHECKBOX = lambda self, color: (By.ID, f"{color}")
    COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_CONFIRM_BUTTON = (By.XPATH, "//button[text()='Заказать' and ancestor::div[contains(@class,'Order_Buttons')]]")
    YES_BUTTON = (By.XPATH, "//button[text()='Да']")
    SUCCESS_MODAL = (By.CLASS_NAME, "Order_Modal__content")

    # Методы
    def fill_personal_info(self, data):
        self.wait.until(EC.element_to_be_clickable(self.FIRST_NAME)).send_keys(data["first_name"])
        self.driver.find_element(*self.LAST_NAME).send_keys(data["last_name"])
        self.driver.find_element(*self.ADDRESS).send_keys(data["address"])
        self.driver.find_element(*self.METRO_STATION).send_keys(data["metro"])
        self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[text()='{data['metro']}']"))).click()
        self.driver.find_element(*self.PHONE).send_keys(data["phone"])
        self.driver.find_element(*self.NEXT_BUTTON).click()

    def fill_scooter_info(self, data):
        self.driver.find_element(*self.DELIVERY_DATE).send_keys(data["date"])
        self.driver.find_element(*self.RENTAL_PERIOD_DROPDOWN).click()
        self.wait.until(EC.element_to_be_clickable(self.RENTAL_PERIOD_OPTION(data["rental_period"]))).click()
        self.driver.find_element(*self.COLOR_CHECKBOX(data["color"])).click()
        if data.get("comment"):
            self.driver.find_element(*self.COMMENT).send_keys(data["comment"])
        self.driver.find_element(*self.ORDER_CONFIRM_BUTTON).click()
        self.wait.until(EC.element_to_be_clickable(self.YES_BUTTON)).click()

    def is_success_modal_visible(self):
        return self.wait.until(EC.visibility_of_element_located(self.SUCCESS_MODAL)).is_displayed()
