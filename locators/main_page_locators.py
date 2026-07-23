from selenium.webdriver.common.by import By


class MainPageLocators:
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
    SCOOTER_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
    TOP_ORDER_BUTTON = (
        By.XPATH,
        ".//button[contains(@class, 'Button_Button') and text()='Заказать']",
    )
    BOTTOM_ORDER_BUTTON = (
        By.XPATH,
        ".//div[contains(@class, 'Home_FinishButton')]/button[text()='Заказать']",
    )
    FAQ_ITEMS = (By.XPATH, ".//div[@class='accordion__item']")

    @staticmethod
    def faq_question(index):
        return By.ID, f"accordion__heading-{index}"

    @staticmethod
    def faq_answer(index):
        return By.ID, f"accordion__panel-{index}"
