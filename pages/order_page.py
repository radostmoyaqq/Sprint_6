import allure

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    @allure.step("Fill customer form")
    def fill_customer_form(self, first_name, last_name, address, metro, phone):
        self.type_text(OrderPageLocators.FIRST_NAME_INPUT, first_name)
        self.type_text(OrderPageLocators.LAST_NAME_INPUT, last_name)
        self.type_text(OrderPageLocators.ADDRESS_INPUT, address)
        self.type_text(OrderPageLocators.METRO_INPUT, metro)
        self.click(OrderPageLocators.metro_station(metro))
        self.type_text(OrderPageLocators.PHONE_INPUT, phone)
        self.click(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Fill rental form")
    def fill_rental_form(self, date, period, color, comment):
        self.type_text(OrderPageLocators.DATE_INPUT, date)
        self.click_page_body(OrderPageLocators.BODY)
        self.click(OrderPageLocators.RENT_PERIOD_FIELD)
        self.click(OrderPageLocators.rent_period(period))
        self.click(OrderPageLocators.color_checkbox(color))
        self.type_text(OrderPageLocators.COMMENT_INPUT, comment)

    @allure.step("Submit order")
    def submit_order(self):
        self.click(OrderPageLocators.ORDER_BUTTON)
        self.click(OrderPageLocators.CONFIRM_ORDER_BUTTON)

    @allure.step("Check successful order modal is visible")
    def is_success_modal_visible(self):
        return self.find_visible(OrderPageLocators.SUCCESS_MODAL).is_displayed()
