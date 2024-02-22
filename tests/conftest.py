from datetime import datetime
import platform
from typing import Generator

import allure
from allure_commons.types import AttachmentType
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeWebDriver
from selenium.webdriver.firefox.webdriver import WebDriver as FirefoxWebDriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service


def pytest_addoption(parser) -> None:
    parser.addoption('--headless',
                     default='false',
                     help='Run tests in headless mode')
    parser.addoption('--browser',
                     default='chrome',
                     help='Choose browser: Chrome or Firefox')
    parser.addoption('--window-size',
                     default='1920,1080',
                     help='Window size in format "width,height"')


@pytest.fixture(scope='function', autouse=True)
def driver(request: pytest.FixtureRequest) -> Generator[ChromeWebDriver | FirefoxWebDriver | None, None, None]:
    chrome_options = ChromeOptions()
    firefox_options = FirefoxOptions()

    browser = request.config.getoption('--browser')
    headless = request.config.getoption('--headless')
    window_size = request.config.getoption('--window-size')

    if browser == 'chrome':
        if headless == 'true':
            chrome_options.add_argument('--headless')
        if window_size == 'max':
            chrome_options.add_argument('--start-maximized')
        else:
            width, height = window_size.split(',')
            chrome_options.add_argument(f'--window-size={width},{height}')

        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        chrome_options.add_argument('--user-agent=Selenium')
        chrome_options.page_load_strategy = 'eager'

        driver = webdriver.Chrome(options=chrome_options)

    elif browser == 'firefox':
        if headless == 'true':
            firefox_options.add_argument('--headless')
        if window_size == 'max':
            firefox_options.add_argument('--start-maximized')
        else:
            width, height = window_size.split(',')
            firefox_options.add_argument(f'--width={width}')
            firefox_options.add_argument(f'--height={height}')

        firefox_options.add_argument('--ignore-certificate-errors')
        firefox_options.add_argument('--no-sandbox')
        firefox_options.add_argument('--disable-dev-shm-usage')
        firefox_options.page_load_strategy = 'eager'

        if platform.system() == 'Windows':
            driver = webdriver.Firefox(options=firefox_options)
        else:
            service = Service('/snap/bin/geckodriver')
            driver = webdriver.Firefox(options=firefox_options, service=service)

    request.cls.driver = driver
    yield driver
    allure.attach(body=driver.get_screenshot_as_png(),
                  name=f"Screenshot {datetime.today()}",
                  attachment_type=AttachmentType.PNG)
    driver.quit()


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config) -> None:
    alluredir = getattr(config.option, 'allure_report_dir', None)
    if not alluredir:
        setattr(config.option, 'allure_report_dir', 'allure-results')
