import platform

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeWebDriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.webdriver import WebDriver as FirefoxWebDriver
from selenium.webdriver.firefox.service import Service

from utils.driver.options import driver_options, headless_option, window_size_option


def driver_config(
    browser: str, headless: str, window_size: str
) -> ChromeWebDriver | FirefoxWebDriver:
    chrome_options = ChromeOptions()
    firefox_options = FirefoxOptions()

    match browser:
        case 'chrome':
            driver_options(chrome_options, browser)
            headless_option(chrome_options, headless)
            window_size_option(chrome_options, window_size, browser)
            driver = webdriver.Chrome(options=chrome_options)

        case 'firefox':
            driver_options(firefox_options, browser)
            headless_option(firefox_options, headless)
            window_size_option(firefox_options, window_size, browser)
            driver = webdriver.Firefox(options=firefox_options)
            # match platform.system():
            #     case 'Windows':
            #         driver = webdriver.Firefox(options=firefox_options)
            #     case _:
            #         service = Service('/snap/bin/geckodriver')
            #         driver = webdriver.Firefox(options=firefox_options, service=service)

    return driver
