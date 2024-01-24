from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver: WebDriver, page_url: str):
        self.driver = driver
        self.page_url = page_url
        self.wait = WebDriverWait(driver, timeout=10, poll_frequency=1)

    def open(self):
        self.driver.get(self.page_url)

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

    def remove_footer(self):
        self.driver.execute_script("document.getElementsByTagName('footer')[0].remove();")

    def remove_fixedban(self):
        self.driver.execute_script("document.getElementById('fixedban').style.display = 'none'")
