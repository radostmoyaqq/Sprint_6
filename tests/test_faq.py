import allure
import pytest

from pages.main_page import MainPage


FAQ_DATA = [
    (0, "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
    (1, "Пока что у нас так: один заказ — один самокат."),
    (2, "Допустим, вы оформляете заказ на 8 мая."),
    (3, "Только начиная с завтрашнего дня."),
    (4, "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку"),
    (5, "Самокат приезжает к вам с полной зарядкой."),
    (6, "Да, пока самокат не привезли."),
    (7, "Да, обязательно. Всем самокатов! И Москве, и Московской области."),
]


@allure.feature("Main page")
@allure.story("FAQ")
class TestFAQ:
    @pytest.mark.parametrize("question_index, expected_text", FAQ_DATA)
    def test_faq_answer_opens_after_click(self, driver, question_index, expected_text):
        main_page = MainPage(driver)
        main_page.open_main_page()

        main_page.open_faq_answer(question_index)

        assert expected_text in main_page.get_faq_answer_text(question_index)
