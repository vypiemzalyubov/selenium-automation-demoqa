import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

from utils.logger import logger
from utils.settings import settings


class BasePage:
    def __init__(self, driver: WebDriver, page: str) -> None:
        self.driver = driver
        self.page = page
        self.base_page = settings.base_page
        self.wait = WebDriverWait(driver, timeout=15, poll_frequency=1)

    @allure.step('Open a browser')
    def open(self) -> None:
        logger.info(f'Opening page "{self.base_page}{self.page}"')
        self.driver.get(f'{self.base_page}{self.page}')

    @allure.step('Find a visible element')
    def element_is_visible(self, locator: tuple[str, str]) -> WebElement:
        logger.info(f'{locator} - Check if this element is visible')
        return self.wait.until(
            EC.visibility_of_element_located(locator),
            message=f'Cannot find element by locator {locator}',
        )

    @allure.step('Find visible elements')
    def elements_are_visible(self, locator: tuple[str, str]) -> list[WebElement]:
        logger.info(f'{locator} - Check if these elements are visible')
        return self.wait.until(
            EC.visibility_of_all_elements_located(locator),
            message=f'Cannot find elements by locator {locator}',
        )

    @allure.step('Find a present element')
    def element_is_present(self, locator: tuple[str, str]) -> WebElement:
        logger.info(f'{locator} - Check if this element is present')
        return self.wait.until(
            EC.presence_of_element_located(locator),
            message=f'Cannot find element by locator {locator}',
        )

    @allure.step('Find present elements')
    def elements_are_present(self, locator: tuple[str, str]) -> list[WebElement]:
        logger.info(f'{locator} - Check if these elements are present')
        return self.wait.until(
            EC.presence_of_all_elements_located(locator),
            message=f'Cannot find elements by locator {locator}',
        )

    @allure.step('Find a not visible element')
    def element_is_not_visible(self, locator: tuple[str, str]) -> bool | WebElement:
        logger.info(f'{locator} - Check if this element is not visible')
        return self.wait.until(
            EC.invisibility_of_element_located(locator),
            message=f'Element was found by locator {locator} but should not',
        )

    @allure.step('Find clickable elements')
    def element_is_clickable(self, locator: tuple[str, str]) -> WebElement:
        logger.info(f'{locator} - Check if this element is clickable')
        return self.wait.until(
            EC.element_to_be_clickable(locator), message=f'Cannot find element by locator {locator}'
        )

    @allure.step('Go to specified element')
    def go_to_element(self, element: WebElement) -> None:
        logger.info(f'Scroll to element "{element.tag_name}"')
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    @allure.step('Select element by text')
    def select_element_by_text(self, element: WebElement, text: str) -> None:
        logger.info(f'Select element "{element}" by text "{text}"')
        select = Select(self.element_is_present(element))
        select.select_by_visible_text(text)

    @allure.step('Select element by value')
    def select_element_by_value(self, element: WebElement, value: str) -> None:
        logger.info(f'Select element "{element}" by value "{value}"')
        select = Select(self.element_is_present(element))
        select.select_by_value(value)

    @allure.step('Switch to new window')
    def switch_to_window(self, window_number: int) -> None:
        logger.info(f'Switch to the window with the number "{window_number}"')
        self.driver.switch_to.window(self.driver.window_handles[window_number])

    @allure.step('Switch to alert')
    def switch_to_alert(self) -> None:
        logger.info('Switch to alert')
        return self.wait.until(EC.alert_is_present())

    @allure.step('Switch to frame')
    def switch_to_frame(self, frame) -> None:
        logger.info('Switch to frame')
        self.wait.until(EC.frame_to_be_available_and_switch_to_it(frame))

    @allure.step('Switch to default content')
    def switch_to_default_content(self) -> None:
        logger.info('Switch to default content')
        self.driver.switch_to.default_content()

    @allure.step('Double click')
    def action_double_click(self, element: WebElement) -> None:
        logger.info(f'Double click on an element "{element}"')
        action = ActionChains(self.driver)
        action.double_click(element)
        action.perform()

    @allure.step('Right click')
    def action_right_click(self, element: WebElement) -> None:
        logger.info(f'Right-click on an element "{element}"')
        action = ActionChains(self.driver)
        action.context_click(element)
        action.perform()

    @allure.step('Drag and drop element by offset')
    def action_drag_and_drop_by_offset(
        self, element: WebElement, x_coords: int, y_coords: int
    ) -> None:
        logger.info(
            f'Drag and drop an element "{element.tag_name}" by offset "{x_coords}" "{y_coords}"'
        )
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(element, x_coords, y_coords)
        action.perform()

    @allure.step('Drag and drop an element to another element')
    def action_drag_and_drop_to_element(self, what: WebElement, where: WebElement) -> None:
        logger.info(f'Drag and drop an element "{what.tag_name}" to element "{where.tag_name}"')
        action = ActionChains(self.driver)
        action.drag_and_drop(what, where)
        action.perform()

    @allure.step('Move cursor to element')
    def action_move_to_element(self, element: WebElement) -> None:
        logger.info(f'Move to element "{element.accessible_name}"')
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()

    @allure.step('Remove footer')
    def remove_footer(self) -> None:
        logger.info('Remove footer and fixedban')
        self.driver.execute_script('document.getElementsByTagName("footer")[0].remove();')
        self.driver.execute_script('document.getElementById("fixedban").style.display = "none"')
