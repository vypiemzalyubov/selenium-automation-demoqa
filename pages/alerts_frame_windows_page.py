import random
import time
from typing import List, Tuple

import allure
from selenium.webdriver.chrome.webdriver import WebDriver

from locators.alerts_frame_windows_locators import (
    BrowserWindowsPageLocators,
    AlertsPageLocators,
    FramesPageLocators,
    NestedFramesPageLocators,
    ModalDialogsPageLocators
)
from pages.base_page import BasePage
from utils.routes import UIRoutes


class BrowserWindowsPage(BasePage):

    locators = BrowserWindowsPageLocators()

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver, page=UIRoutes.BROWSER_WINDOWS)

    @allure.step('Check opened new tab or window')
    def check_opened_interface(self, interface: str) -> str:
        available_intefaces = {
            'tab': self.locators.NEW_TAB_BUTTON,
            'window': self.locators.NEW_WINDOW_BUTTON
        }
        self.element_is_visible(available_intefaces[interface]).click()
        self.switch_to_window(1)
        text_title = self.element_is_present(self.locators.TITLE_NEW).text
        return text_title


class AlertsPage(BasePage):

    locators = AlertsPageLocators()

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver, page=UIRoutes.ALERTS)

    @allure.step('Get text from alert')
    def check_see_alert(self) -> str:
        self.element_is_visible(self.locators.SEE_ALERT_BUTTON).click()
        alert_text = self.switch_to_alert().text
        return alert_text

    @allure.step('Check alert appear after 5 sec')
    def check_alert_appear_after_5_sec(self) -> str:
        self.element_is_visible(self.locators.APPEAR_ALERT_AFTER_5_SEC_BUTTON).click()
        alert_text = self.switch_to_alert().text
        return alert_text

    @allure.step('Check action with alert')
    def check_action_alert(self, action: str) -> str:
        self.element_is_visible(self.locators.CONFIRM_BOX_ALERT_BUTTON).click()
        if action == 'accept':
            self.switch_to_alert().accept()
        else:
            self.switch_to_alert().dismiss()
        text_result = self.element_is_present(self.locators.CONFIRM_RESULT).text
        return text_result

    @allure.step('Check prompt alert')
    def check_prompt_alert(self) -> Tuple[str, str]:
        text = f'autotest{random.randint(0, 999)}'
        self.element_is_visible(self.locators.PROMPT_BOX_ALERT_BUTTON).click()
        alert_window = self.switch_to_alert()
        alert_window.send_keys(text)
        alert_window.accept()
        text_result = self.element_is_present(self.locators.PROMPT_RESULT).text
        return text, text_result


class FramesPage(BasePage):

    locators = FramesPageLocators()

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver, page=UIRoutes.FRAMES)

    @allure.step('Check frame')
    def check_frame(self, frame_number: str) -> List[str]:
        if frame_number == 'frame1':
            frame = self.element_is_present(self.locators.FIRST_FRAME)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.switch_to_frame(frame)
            frame_text = self.element_is_present(self.locators.TITLE_FRAME).text
            self.switch_to_default_content()
            return [frame_text, width, height]
        if frame_number == 'frame2':
            frame = self.element_is_present(self.locators.SECOND_FRAME)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.switch_to_frame(frame)
            frame_text = self.element_is_present(self.locators.TITLE_FRAME).text
            self.switch_to_default_content()
            return [frame_text, width, height]


class NestedFramesPage(BasePage):

    locators = NestedFramesPageLocators()

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver, page=UIRoutes.NESTED_FRAMES)

    @allure.step('Check nested frame')
    def check_nested_frame(self) -> Tuple[str, str]:
        parent_frame = self.element_is_present(self.locators.PARENT_FRAME)
        self.switch_to_frame(parent_frame)
        parent_text = self.element_is_present(self.locators.PARENT_TEXT).text
        child_frame = self.element_is_present(self.locators.CHILD_FRAME)
        self.switch_to_frame(child_frame)
        child_text = self.element_is_present(self.locators.CHILD_TEXT).text
        return parent_text, child_text


class ModalDialogsPage(BasePage):

    locators = ModalDialogsPageLocators()

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver, page=UIRoutes.MODAL_DIALOGS)

    @allure.step('Check modal dialogs')
    def check_modal_dialogs(self, size: str, method: str) -> Tuple[str, str]:
        if size == 'small':
            self.element_is_visible(self.locators.SMALL_MODAL_BUTTON).click()
            title_text = self.element_is_visible(self.locators.TITLE_SMALL_MODAL).text
            body_text = self.element_is_visible(self.locators.BODY_SMALL_MODAL).text
            self._closing_method(method, 'SMALL_MODAL_CLOSE_BUTTON')
            return title_text, body_text
        else:
            self.element_is_visible(self.locators.LARGE_MODAL_BUTTON).click()
            title_text = self.element_is_visible(self.locators.TITLE_LARGE_MODAL).text
            body_text = self.element_is_visible(self.locators.BODY_LARGE_MODAL).text
            self._closing_method(method, 'LARGE_MODAL_CLOSE_BUTTON')
            return title_text, body_text

    def _closing_method(self, method: str, locator_name: str) -> None:
        locator = getattr(self.locators, locator_name)
        if method == 'button':
            self.element_is_visible(locator).click()
        elif method == 'cross':
            self.element_is_visible(self.locators.MODAL_CLOSE_CROSS).click()
        else:
            self.element_is_visible(self.locators.CLOSE_OVERLAY).click()
