import os

import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


@pytest.fixture
def driver():
    options = Options()
    if os.getenv("HEADLESS", "false").lower() == "true":
        options.add_argument("-headless")

    browser = webdriver.Firefox(options=options)
    browser.maximize_window()
    yield browser
    browser.quit()
