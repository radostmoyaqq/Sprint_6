import allure

from data import BOTTOM_ORDER_DATA, TOP_ORDER_DATA
from pages.main_page import MainPage
from pages.order_page import OrderPage


@allure.feature("Order")
@allure.story("Positive order flow")
class TestOrder:
    def test_successful_order_from_top_button(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.open_main_page()
        main_page.click_top_order_button()

        order_page.fill_customer_form(
            TOP_ORDER_DATA["first_name"],
            TOP_ORDER_DATA["last_name"],
            TOP_ORDER_DATA["address"],
            TOP_ORDER_DATA["metro"],
            TOP_ORDER_DATA["phone"],
        )
        order_page.fill_rental_form(
            TOP_ORDER_DATA["date"],
            TOP_ORDER_DATA["period"],
            TOP_ORDER_DATA["color"],
            TOP_ORDER_DATA["comment"],
        )
        order_page.submit_order()

        assert order_page.is_success_modal_visible()

    def test_successful_order_from_bottom_button(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.open_main_page()
        main_page.click_bottom_order_button()

        order_page.fill_customer_form(
            BOTTOM_ORDER_DATA["first_name"],
            BOTTOM_ORDER_DATA["last_name"],
            BOTTOM_ORDER_DATA["address"],
            BOTTOM_ORDER_DATA["metro"],
            BOTTOM_ORDER_DATA["phone"],
        )
        order_page.fill_rental_form(
            BOTTOM_ORDER_DATA["date"],
            BOTTOM_ORDER_DATA["period"],
            BOTTOM_ORDER_DATA["color"],
            BOTTOM_ORDER_DATA["comment"],
        )
        order_page.submit_order()

        assert order_page.is_success_modal_visible()
