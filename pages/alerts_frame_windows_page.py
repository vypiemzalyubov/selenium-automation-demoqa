import random

import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utils.routes import UIRoutes


class BrowserWindowsPage(BasePage):
    NEW_TAB_BUTTON = (By.CSS_SELECTOR, 'button[id="tabButton"]')
    NEW_WINDOW_BUTTON = (By.CSS_SELECTOR, 'button[id="windowButton"]')
    TITLE_NEW = (By.CSS_SELECTOR, 'h1[id="sampleHeading"]')

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver, page=UIRoutes.BROWSER_WINDOWS)

    @allure.step('Check opened new tab or window')
    def check_opened_interface(self, interface: str) -> str:
        available_intefaces = {
            'tab': self.NEW_TAB_BUTTON,
            'window': self.NEW_WINDOW_BUTTON,
        }
        self.element_is_visible(available_intefaces[interface]).click()
        self.switch_to_window(1)
        text_title = self.element_is_present(self.TITLE_NEW).text
        return text_title


class AlertsPage(BasePage):
    SEE_ALERT_BUTTON = (By.CSS_SELECTOR, 'button[id="alertButton"]')
    APPEAR_ALERT_AFTER_5_SEC_BUTTON = (By.CSS_SELECTOR, 'button[id="timerAlertButton"]')
    CONFIRM_BOX_ALERT_BUTTON = (By.CSS_SELECTOR, 'button[id="confirmButton"]')
    CONFIRM_RESULT = (By.CSS_SELECTOR, 'span[id="confirmResult"]')
    PROMPT_BOX_ALERT_BUTTON = (By.CSS_SELECTOR, 'button[id="promtButton"]')
    PROMPT_RESULT = (By.CSS_SELECTOR, 'span[id="promptResult"]')

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver, page=UIRoutes.ALERTS)

    @allure.step('Get text from alert')
    def check_see_alert(self) -> str:
        self.element_is_visible(self.SEE_ALERT_BUTTON).click()
        alert_text = self.switch_to_alert().text
        return alert_text

    @allure.step('Check alert appear after 5 sec')
    def check_alert_appear_after_5_sec(self) -> str:
        self.element_is_visible(self.APPEAR_ALERT_AFTER_5_SEC_BUTTON).click()
        alert_text = self.switch_to_alert().text
        return alert_text

    @allure.step('Check action with alert')
    def check_action_alert(self, action: str) -> str:
        self.element_is_visible(self.CONFIRM_BOX_ALERT_BUTTON).click()
        if action == 'accept':
            self.switch_to_alert().accept()
        else:
            self.switch_to_alert().dismiss()
        text_result = self.element_is_present(self.CONFIRM_RESULT).text
        return text_result

    @allure.step('Check prompt alert')
    def check_prompt_alert(self) -> tuple[str, str]:
        text = f'autotest{random.randint(0, 999)}'
        self.element_is_visible(self.PROMPT_BOX_ALERT_BUTTON).click()
        alert_window = self.switch_to_alert()
        alert_window.send_keys(text)
        alert_window.accept()
        text_result = self.element_is_present(self.PROMPT_RESULT).text
        return text, text_result


class FramesPage(BasePage):
    FIRST_FRAME = (By.CSS_SELECTOR, 'iframe[id="frame1"]')
    SECOND_FRAME = (By.CSS_SELECTOR, 'iframe[id="frame2"]')
    TITLE_FRAME = (By.CSS_SELECTOR, 'h1[id="sampleHeading"]')

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver, page=UIRoutes.FRAMES)

    @allure.step('Check frame')
    def check_frame(self, frame_number: str) -> list[str]:
        if frame_number == 'frame1':
            frame = self.element_is_present(self.FIRST_FRAME)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.switch_to_frame(frame)
            frame_text = self.element_is_present(self.TITLE_FRAME).text
            self.switch_to_default_content()
            return [frame_text, width, height]
        if frame_number == 'frame2':
            frame = self.element_is_present(self.SECOND_FRAME)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.switch_to_frame(frame)
            frame_text = self.element_is_present(self.TITLE_FRAME).text
            self.switch_to_default_content()
            return [frame_text, width, height]


class NestedFramesPage(BasePage):
    PARENT_FRAME = (By.CSS_SELECTOR, 'iframe[id="frame1"]')
    PARENT_TEXT = (By.CSS_SELECTOR, 'body')
    CHILD_FRAME = (By.CSS_SELECTOR, 'iframe[srcdoc="<p>Child Iframe</p>"]')
    CHILD_TEXT = (By.CSS_SELECTOR, 'p')

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver, page=UIRoutes.NESTED_FRAMES)

    @allure.step('Check nested frame')
    def check_nested_frame(self) -> tuple[str, str]:
        parent_frame = self.element_is_present(self.PARENT_FRAME)
        self.switch_to_frame(parent_frame)
        parent_text = self.element_is_present(self.PARENT_TEXT).text
        child_frame = self.element_is_present(self.CHILD_FRAME)
        self.switch_to_frame(child_frame)
        child_text = self.element_is_present(self.CHILD_TEXT).text
        return parent_text, child_text


class ModalDialogsPage(BasePage):
    SMALL_MODAL_BUTTON = (By.CSS_SELECTOR, 'button[id="showSmallModal"]')
    SMALL_MODAL_CLOSE_BUTTON = (By.CSS_SELECTOR, 'button[id="closeSmallModal"]')
    BODY_SMALL_MODAL = (By.CSS_SELECTOR, 'div[class="modal-body"]')
    TITLE_SMALL_MODAL = (By.CSS_SELECTOR, 'div[id="example-modal-sizes-title-sm"]')

    LARGE_MODAL_BUTTON = (By.CSS_SELECTOR, 'button[id="showLargeModal"]')
    LARGE_MODAL_CLOSE_BUTTON = (By.CSS_SELECTOR, 'button[id="closeLargeModal"]')
    BODY_LARGE_MODAL = (By.CSS_SELECTOR, 'div[class="modal-body"] p')
    TITLE_LARGE_MODAL = (By.CSS_SELECTOR, 'div[id="example-modal-sizes-title-lg"]')

    MODAL_CLOSE_CROSS = (By.CSS_SELECTOR, 'span[aria-hidden="true"]')
    CLOSE_OVERLAY = (By.CSS_SELECTOR, 'div[role="dialog"]')

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver, page=UIRoutes.MODAL_DIALOGS)

    @allure.step('Check modal dialogs')
    def check_modal_dialogs(self, size: str, method: str) -> tuple[str, str]:
        if size == 'small':
            self.element_is_visible(self.SMALL_MODAL_BUTTON).click()
            title_text = self.element_is_visible(self.TITLE_SMALL_MODAL).text
            body_text = self.element_is_visible(self.BODY_SMALL_MODAL).text
            self._closing_method(method, 'SMALL_MODAL_CLOSE_BUTTON')
            return title_text, body_text
        else:
            self.element_is_visible(self.LARGE_MODAL_BUTTON).click()
            title_text = self.element_is_visible(self.TITLE_LARGE_MODAL).text
            body_text = self.element_is_visible(self.BODY_LARGE_MODAL).text
            self._closing_method(method, 'LARGE_MODAL_CLOSE_BUTTON')
            return title_text, body_text

    def _closing_method(self, method: str, locator_name: str) -> None:
        locator = getattr(self, locator_name)
        if method == 'button':
            self.element_is_visible(locator).click()
        elif method == 'cross':
            self.element_is_visible(self.MODAL_CLOSE_CROSS).click()
        else:
            self.element_is_visible(self.CLOSE_OVERLAY).click()
