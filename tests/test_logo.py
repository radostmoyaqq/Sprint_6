import allure
from selenium.webdriver.support import expected_conditions as EC

from pages.main_page import MainPage


@allure.feature("Header")
@allure.story("Logo navigation")
class TestLogo:
    def test_scooter_logo_opens_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_top_order_button()

        main_page.click_scooter_logo()

        main_page.wait.until(EC.url_to_be(MainPage.URL))
        assert driver.current_url == MainPage.URL

    def test_yandex_logo_opens_dzen_in_new_window(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()

        main_page.click_yandex_logo()

        main_page.wait.until(lambda browser: "dzen.ru" in browser.current_url)
        assert "dzen.ru" in driver.current_url
