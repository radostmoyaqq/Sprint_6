import allure
import pytest

from data import ORDER_DATA
from pages.main_page import MainPage
from pages.order_page import OrderPage


@allure.feature("Order")
@allure.story("Positive order flow")
class TestOrder:
    @pytest.mark.parametrize("entry_point, order_data", ORDER_DATA)
    def test_successful_order_from_different_entry_points(self, driver, entry_point, order_data):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.open_main_page()

        if entry_point == "top":
            main_page.click_top_order_button()
        else:
            main_page.click_bottom_order_button()

        order_page.fill_customer_form(
            order_data["first_name"],
            order_data["last_name"],
            order_data["address"],
            order_data["metro"],
            order_data["phone"],
        )
        order_page.fill_rental_form(
            order_data["date"],
            order_data["period"],
            order_data["color"],
            order_data["comment"],
        )
        order_page.submit_order()

        assert order_page.is_success_modal_visible()
