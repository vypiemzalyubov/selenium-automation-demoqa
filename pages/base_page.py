import allure

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from utils.logger import logger


class BasePage:

    def __init__(self, driver: WebDriver, page: str):
        self.driver = driver
        self.page = page
        self.wait = WebDriverWait(driver, timeout=10, poll_frequency=1)

    @allure.step("Open a browser")
    def open(self):
        logger.info(
            f"Opening page {self.page}"
        )
        self.driver.get(self.page)

    @allure.step("Find a visible element")
    def element_is_visible(self, locator):
        logger.info(
            f"{locator} - Check if this element is visible"
        )
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Find visible elements")
    def elements_are_visible(self, locator):
        logger.info(
            f"{locator} - Check if these elements are visible"
        )
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    @allure.step("Find a present element")
    def element_is_present(self, locator):
        logger.info(
            f"{locator} - Check if this element is present"
        )
        return self.wait.until(EC.presence_of_element_located(locator))

    @allure.step("Find present elements")
    def elements_are_present(self, locator):
        logger.info(
            f"{locator} - Check if these elements are present"
        )
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    @allure.step("Find a not visible element")
    def element_is_not_visible(self, locator):
        logger.info(
            f"{locator} - Check if this element is not visible"
        )
        return self.wait.until(EC.invisibility_of_element_located(locator))

    @allure.step("Find clickable elements")
    def element_is_clickable(self, locator):
        logger.info(
            f"{locator} - Check if this element is clickable"
        )
        return self.wait.until(EC.element_to_be_clickable(locator))

    @allure.step("Go to specified element")
    def go_to_element(self, element):
        logger.info(
            f"Scroll to element {element.accessible_name}"
        )
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Switch to new window")
    def switch_to_window(self, window_number: int):
        logger.info(
            f"Switch to the window with the number {window_number}"
        )
        self.driver.switch_to.window(self.driver.window_handles[window_number])

    @allure.step("Switch to alert")
    def switch_to_alert(self):
        logger.info(
            "Switch to alert"
        )
        return self.wait.until(EC.alert_is_present())

    @allure.step("Double click")
    def action_double_click(self, element):
        logger.info(
            f"Double click on an element {element}"
        )
        action = ActionChains(self.driver)
        action.double_click(element)
        action.perform()

    @allure.step("Right click")
    def action_right_click(self, element):
        logger.info(
            f"Right-click on an element {element}"
        )
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
        self.driver.execute_script(
            "document.getElementsByTagName('footer')[0].remove();")
        self.driver.execute_script(
            "document.getElementById('fixedban').style.display = 'none'")
