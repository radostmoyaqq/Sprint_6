from selenium.webdriver.common.by import By


class OrderPageLocators:
    FIRST_NAME_INPUT = (By.XPATH, ".//input[@placeholder='* Имя']")
    LAST_NAME_INPUT = (By.XPATH, ".//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH, ".//input[@placeholder='* Станция метро']")
    PHONE_INPUT = (By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, ".//button[text()='Далее']")
    DATE_INPUT = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")
    RENT_PERIOD_FIELD = (By.CLASS_NAME, "Dropdown-placeholder")
    COMMENT_INPUT = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (
        By.XPATH,
        ".//div[contains(@class, 'Order_Buttons')]/button[text()='Заказать']",
    )
    CONFIRM_ORDER_BUTTON = (By.XPATH, ".//button[text()='Да']")
    SUCCESS_MODAL = (
        By.XPATH,
        ".//div[contains(@class, 'Order_ModalHeader') and contains(text(), 'Заказ оформлен')]",
    )
    BODY = (By.TAG_NAME, "body")

    @staticmethod
    def metro_station(station):
        return By.XPATH, f".//div[contains(@class, 'select-search__select')]//div[text()='{station}']"

    @staticmethod
    def rent_period(period):
        return By.XPATH, f".//div[contains(@class, 'Dropdown-option') and text()='{period}']"

    @staticmethod
    def color_checkbox(color):
        return By.ID, color
