from selenium.webdriver.common.by import By

class MainPageLocators:
    FAQ_QUESTIONS = (By.XPATH, "//div[@data-accordion-component='AccordionItemButton']")
    FAQ_ANSWERS = (By.XPATH, "//div[@data-accordion-component='AccordionItemPanel']")
    TOP_ORDER_BUTTON = (By.XPATH, "//button[text()='Заказать' and ancestor::div[contains(@class, 'Header')]]")
    BOTTOM_ORDER_BUTTON = (By.XPATH, "//button[text()='Заказать' and ancestor::div[contains(@class, 'Home_Finish')]]")
    LOGO_SCOOTER = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    LOGO_YANDEX = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")

class OrderPageLocators:
    FIRST_NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_FIELD = (By.CLASS_NAME, "select-search__input")
    PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    DATE_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    SCOOTER_COLOR_BLACK = (By.ID, "black")
    SCOOTER_COLOR_GREY = (By.ID, "grey")
    COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Заказать' and not(@disabled)]")
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")
    SUCCESS_MODAL = (By.XPATH, "//div[contains(text(),'Заказ оформлен')]")
