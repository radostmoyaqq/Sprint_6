import allure
import pytest

from data import FAQ_DATA
from pages.main_page import MainPage


@allure.feature("Main page")
@allure.story("FAQ")
class TestFAQ:
    @pytest.mark.parametrize("question_index, expected_text", FAQ_DATA)
    def test_faq_answer_opens_after_click(self, driver, question_index, expected_text):
        main_page = MainPage(driver)
        main_page.open_main_page()

        main_page.open_faq_answer(question_index)

        assert expected_text in main_page.get_faq_answer_text(question_index)
