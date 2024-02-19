import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--headless',
                     default='false',
                     help='Run tests in headless mode')
    parser.addoption('--window-size',
                     default='1920,1080',
                     help='Window size in format "width,height"')


@pytest.fixture(scope='function', autouse=True)
def driver(request: pytest.FixtureRequest):
    chrome_option = Options()
    chrome_option.page_load_strategy = 'eager'
    chrome_option.add_argument('--ignore-certificate-errors')
    chrome_option.add_argument('--no-sandbox')
    chrome_option.add_argument('--disable-dev-shm-usage')
    chrome_option.add_argument('--disable-blink-features=AutomationControlled')
    chrome_option.add_argument('--user-agent=Selenium')

    headless = request.config.getoption('--headless')
    if headless == 'true':
        chrome_option.add_argument('--headless')

    window_size = request.config.getoption('--window-size')
    if window_size == 'max':
        chrome_option.add_argument('--start-maximized')
    else:
        width, height = window_size.split(',')
        chrome_option.add_argument(f'--window-size={width},{height}')

    driver = webdriver.Chrome(options=chrome_option)
    request.cls.driver = driver
    yield driver
    driver.quit()
