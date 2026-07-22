import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class OrderPage(BasePage):
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
    SUCCESS_MODAL = (By.XPATH, ".//div[contains(@class, 'Order_ModalHeader') and contains(text(), 'Заказ оформлен')]")

    def metro_station(self, station):
        return By.XPATH, f".//div[contains(@class, 'select-search__select')]//div[text()='{station}']"

    def rent_period(self, period):
        return By.XPATH, f".//div[contains(@class, 'Dropdown-option') and text()='{period}']"

    def color_checkbox(self, color):
        return By.ID, color

    @allure.step("Fill customer form")
    def fill_customer_form(self, first_name, last_name, address, metro, phone):
        self.type_text(self.FIRST_NAME_INPUT, first_name)
        self.type_text(self.LAST_NAME_INPUT, last_name)
        self.type_text(self.ADDRESS_INPUT, address)
        self.type_text(self.METRO_INPUT, metro)
        self.click(self.metro_station(metro))
        self.type_text(self.PHONE_INPUT, phone)
        self.click(self.NEXT_BUTTON)

    @allure.step("Fill rental form")
    def fill_rental_form(self, date, period, color, comment):
        self.type_text(self.DATE_INPUT, date)
        self.driver.find_element(By.TAG_NAME, "body").click()
        self.click(self.RENT_PERIOD_FIELD)
        self.click(self.rent_period(period))
        self.click(self.color_checkbox(color))
        self.type_text(self.COMMENT_INPUT, comment)

    @allure.step("Submit order")
    def submit_order(self):
        self.click(self.ORDER_BUTTON)
        self.click(self.CONFIRM_ORDER_BUTTON)

    @allure.step("Check successful order modal is visible")
    def is_success_modal_visible(self):
        return self.wait.until(EC.visibility_of_element_located(self.SUCCESS_MODAL)).is_displayed()
