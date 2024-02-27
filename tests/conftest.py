from datetime import datetime
from collections.abc import Generator

import allure
from allure_commons.types import AttachmentType
import pytest
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeWebDriver
from selenium.webdriver.firefox.webdriver import WebDriver as FirefoxWebDriver

from utils.driver.driver import driver_config


def pytest_addoption(parser) -> None:
    parser.addoption('--headless', default='false', help='Run tests in headless mode')
    parser.addoption('--browser', default='chrome', help='Choose browser: Chrome or Firefox')
    parser.addoption(
        '--window-size', default='1920,1080', help='Window size in format "width,height"'
    )


@pytest.fixture(scope='function', autouse=True)
def driver(
    request: pytest.FixtureRequest,
) -> Generator[ChromeWebDriver | FirefoxWebDriver, None, None]:
    driver = driver_config(
        request.config.getoption('--browser'),
        request.config.getoption('--headless'),
        request.config.getoption('--window-size'),
    )
    request.cls.driver = driver
    yield driver
    allure.attach(
        body=driver.get_screenshot_as_png(),
        name=f'Screenshot {datetime.today()}',
        attachment_type=AttachmentType.PNG,
    )
    driver.quit()


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config) -> None:
    alluredir = getattr(config.option, 'allure_report_dir', None)
    if not alluredir:
        setattr(config.option, 'allure_report_dir', 'allure-results')
