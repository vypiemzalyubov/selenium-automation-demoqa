import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOption
from selenium.webdriver.firefox.options import Options as FirefoxOption


def pytest_addoption(parser):
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
def driver(request: pytest.FixtureRequest):
    chrome_options = ChromeOption()
    firefox_options = FirefoxOption()    
    
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
        
        driver = webdriver.Firefox(options=firefox_options)
    
    request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    alluredir = getattr(config.option, "allure_report_dir", None)
    if not alluredir:
        setattr(config.option, "allure_report_dir", "allure-results")
