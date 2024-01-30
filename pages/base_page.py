import allure

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:

    def __init__(self, driver: WebDriver, page_url: str):
        self.driver = driver
        self.page_url = page_url
        self.wait = WebDriverWait(driver, timeout=10, poll_frequency=1)

    @allure.step("Open a browser")
    def open(self):
        self.driver.get(self.page_url)

    @allure.step("Find a visible element")
    def element_is_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Find visible elements")
    def elements_are_visible(self, locator):
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    @allure.step("Find a present element")
    def element_is_present(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))
     
    @allure.step("Find present elements")
    def elements_are_present(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    @allure.step("Find a not visible element")
    def element_is_not_visible(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    @allure.step("Find clickable elements")
    def element_is_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    @allure.step("Go to specified element")
    def go_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Switch to new window")
    def switch_to_window(self, window_number: int):
        self.driver.switch_to.window(self.driver.window_handles[window_number])

    @allure.step("Switch to alert")
    def switch_to_alert(self):
        return self.wait.until(EC.alert_is_present())

    @allure.step("Double click")
    def action_double_click(self, element):
        action = ActionChains(self.driver)
        action.double_click(element)
        action.perform()

    @allure.step("Right click")
    def action_right_click(self, element):
        action = ActionChains(self.driver)
        action.context_click(element)
        action.perform()

    @allure.step("Drag and drop by offset")
    def action_drag_and_drop_by_offset(self, element, x_coords, y_coords):
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(element, x_coords, y_coords)
        action.perform()

    @allure.step("Drag and drop element to element")
    def action_drag_and_drop_to_element(self, what, where):
        action = ActionChains(self.driver)
        action.drag_and_drop(what, where)
        action.perform()

    @allure.step("Move cursor to element")
    def action_move_to_element(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()

    @allure.step("Remove footer")
    def remove_footer(self):
        self.driver.execute_script("document.getElementsByTagName('footer')[0].remove();")
        self.driver.execute_script("document.getElementById('fixedban').style.display = 'none'")