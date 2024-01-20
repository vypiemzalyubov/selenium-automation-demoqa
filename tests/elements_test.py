import time
from pages.base_page import BasePage


def test(driver):
    page = BasePage(driver, "https://google.com")
    page.open()
    time.sleep(3)
