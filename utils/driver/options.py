from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def driver_options(driver_options: ChromeOptions | FirefoxOptions, browser: str):
    match browser:
        case 'chrome':
            driver_options.add_argument('--ignore-certificate-errors')
            driver_options.add_argument('--no-sandbox')
            driver_options.add_argument('--disable-dev-shm-usage')
            driver_options.add_argument(
                '--disable-blink-features=AutomationControlled')
            driver_options.add_argument('--user-agent=Selenium')
            driver_options.page_load_strategy = 'eager'
        case 'firefox':
            driver_options.add_argument('--ignore-certificate-errors')
            driver_options.add_argument('--no-sandbox')
            driver_options.add_argument('--disable-dev-shm-usage')
            driver_options.page_load_strategy = 'eager'


def headless_option(driver_options: ChromeOptions | FirefoxOptions, headless: str):
    match headless:
        case 'true':
            driver_options.add_argument('--headless')


def window_size_option(driver_options: ChromeOptions | FirefoxOptions, window_size: str, browser: str):
    match window_size:
        case 'max':
            driver_options.add_argument('--start-maximized')
        case _:
            width, height = window_size.split(',')

            match browser:
                case 'chrome':
                    driver_options.add_argument(f'--window-size={width},{height}')
                case 'firefox':
                    driver_options.add_argument(f'--width={width}')
                    driver_options.add_argument(f'--height={height}')
