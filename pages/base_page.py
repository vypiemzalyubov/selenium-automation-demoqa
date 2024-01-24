from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=10, poll_frequency=1)

    def open(self, page_url: str):
        self.driver.get(page_url)

    def element_is_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator):
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def elements_are_present(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def go_to_element(self, element):
        self.driver.execute_script('arguments[0].scrollIntoView();', element)
