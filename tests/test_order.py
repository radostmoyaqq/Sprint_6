import allure
import pytest

from pages.main_page import MainPage
from pages.order_page import OrderPage


ORDER_DATA = [
    (
        "top",
        {
            "first_name": "Иван",
            "last_name": "Петров",
            "address": "Москва, Ленина 1",
            "metro": "Сокольники",
            "phone": "+79991234567",
            "date": "25.07.2026",
            "period": "сутки",
            "color": "black",
            "comment": "Позвоните за час",
        },
    ),
    (
        "bottom",
        {
            "first_name": "Анна",
            "last_name": "Смирнова",
            "address": "Москва, Тверская 10",
            "metro": "Черкизовская",
            "phone": "+79997654321",
            "date": "26.07.2026",
            "period": "двое суток",
            "color": "grey",
            "comment": "Домофон не работает",
        },
    ),
]


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
