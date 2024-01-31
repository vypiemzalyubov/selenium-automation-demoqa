import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--headless",
                     default="false",
                     help="headless options: 'true' or 'false'")


@pytest.fixture(scope="function", autouse=True)
def driver(request: pytest.FixtureRequest):
    chrome_option = Options()
    chrome_option.page_load_strategy = "eager"
    chrome_option.add_argument("--window-size=1920,1080")
    chrome_option.add_argument("--ignore-certificate-errors")
    chrome_option.add_argument("--no-sandbox")
    chrome_option.add_argument("--disable-dev-shm-usage")
    chrome_option.add_argument("--disable-blink-features=AutomationControlled")
    chrome_option.add_argument("--user-agent=Selenium")
    headless = request.config.getoption("--headless")
    if headless == "true":
        chrome_option.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_option)
    request.cls.driver = driver
    yield driver
    driver.quit()
