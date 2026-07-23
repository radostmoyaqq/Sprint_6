import allure

from constants import BASE_URL, DZEN_URL_PART
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step("Open main page")
    def open_main_page(self):
        self.open(BASE_URL)
        self.accept_cookies()

    @allure.step("Accept cookies if banner is shown")
    def accept_cookies(self):
        try:
            self.click(MainPageLocators.COOKIE_BUTTON)
        except Exception:
            pass

    @allure.step("Open FAQ answer #{index}")
    def open_faq_answer(self, index):
        locator = MainPageLocators.faq_question(index)
        self.scroll_to(locator)
        self.click_with_js(locator)

    def get_faq_answer_text(self, index):
        return self.get_text(MainPageLocators.faq_answer(index))

    @allure.step("Click top order button")
    def click_top_order_button(self):
        self.click(MainPageLocators.TOP_ORDER_BUTTON)

    @allure.step("Click bottom order button")
    def click_bottom_order_button(self):
        self.scroll_to(MainPageLocators.BOTTOM_ORDER_BUTTON)
        self.click(MainPageLocators.BOTTOM_ORDER_BUTTON)

    @allure.step("Click Scooter logo")
    def click_scooter_logo(self):
        self.click(MainPageLocators.SCOOTER_LOGO)

    def is_main_page_opened(self):
        self.wait_for_url(BASE_URL)
        return self.current_url() == BASE_URL

    @allure.step("Click Yandex logo")
    def click_yandex_logo(self):
        old_handles = self.get_window_handles()
        self.click(MainPageLocators.YANDEX_LOGO)
        self.switch_to_new_window(old_handles)

    def is_dzen_page_opened(self):
        self.wait_for_url_part(DZEN_URL_PART)
        return DZEN_URL_PART in self.current_url()
