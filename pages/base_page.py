import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    @allure.step("Open page: {url}")
    def open(self, url):
        self.driver.get(url)

    def find_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    @allure.step("Click element")
    def click(self, locator):
        self.find_clickable(locator).click()

    @allure.step("Type text")
    def type_text(self, locator, text):
        element = self.find_visible(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Scroll to element")
    def scroll_to(self, locator):
        element = self.find_visible(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        return element

    def get_text(self, locator):
        return self.find_visible(locator).text

    def current_url(self):
        return self.driver.current_url
