import allure

from pages.main_page import MainPage


@allure.feature("Header")
@allure.story("Logo navigation")
class TestLogo:
    def test_scooter_logo_opens_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_top_order_button()

        main_page.click_scooter_logo()

        assert main_page.is_main_page_opened()

    def test_yandex_logo_opens_dzen_in_new_window(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()

        main_page.click_yandex_logo()

        assert main_page.is_dzen_page_opened()
