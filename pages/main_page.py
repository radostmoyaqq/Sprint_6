import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class MainPage(BasePage):
    URL = "https://qa-scooter.praktikum-services.ru/"

    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
    SCOOTER_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
    TOP_ORDER_BUTTON = (By.XPATH, ".//button[contains(@class, 'Button_Button') and text()='Заказать']")
    BOTTOM_ORDER_BUTTON = (
        By.XPATH,
        ".//div[contains(@class, 'Home_FinishButton')]/button[text()='Заказать']",
    )
    FAQ_ITEMS = (By.XPATH, ".//div[@class='accordion__item']")

    def faq_question(self, index):
        return By.ID, f"accordion__heading-{index}"

    def faq_answer(self, index):
        return By.ID, f"accordion__panel-{index}"

    @allure.step("Open main page")
    def open_main_page(self):
        self.open(self.URL)
        self.accept_cookies()

    @allure.step("Accept cookies if banner is shown")
    def accept_cookies(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.COOKIE_BUTTON)).click()
        except Exception:
            pass

    @allure.step("Open FAQ answer #{index}")
    def open_faq_answer(self, index):
        locator = self.faq_question(index)
        self.scroll_to(locator)
        self.click(locator)

    def get_faq_answer_text(self, index):
        return self.get_text(self.faq_answer(index))

    @allure.step("Click top order button")
    def click_top_order_button(self):
        self.click(self.TOP_ORDER_BUTTON)

    @allure.step("Click bottom order button")
    def click_bottom_order_button(self):
        self.scroll_to(self.BOTTOM_ORDER_BUTTON)
        self.click(self.BOTTOM_ORDER_BUTTON)

    @allure.step("Click Scooter logo")
    def click_scooter_logo(self):
        self.click(self.SCOOTER_LOGO)

    @allure.step("Click Yandex logo")
    def click_yandex_logo(self):
        old_handles = self.driver.window_handles
        self.click(self.YANDEX_LOGO)
        self.wait.until(EC.new_window_is_opened(old_handles))
        new_handle = [handle for handle in self.driver.window_handles if handle not in old_handles][0]
        self.driver.switch_to.window(new_handle)
