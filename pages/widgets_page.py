import random
import time
from typing import List, Literal, Tuple

import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from utils.generator import generated_color, generated_date
from locators.widgets_page_locators import (
    AccordianPageLocators,
    AutoCompletePageLocators,
    DatePickerPageLocators,
    SliderPageLocators,
    ProgressBarPageLocators,
    TabsPageLocators,
    ToolTipsPageLocators,
    MenuPageLocators
)
from pages.base_page import BasePage
from utils.routes import UIRoutes


class AccordianPage(BasePage):

    locators = AccordianPageLocators()

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver, page=UIRoutes.ACCORDEAN)

    @allure.step('Check accordian widget')
    def check_accordian(self, accordian_number: str) -> list:
        accordian = {
            'first': {
                'title': self.locators.SECTION_FIRST,
                'content': self.locators.SECTION_CONTENT_FIRST
            },
            'second': {
                'title': self.locators.SECTION_SECOND,
                'content': self.locators.SECTION_CONTENT_SECOND
            },
            'third': {
                'title': self.locators.SECTION_THIRD,
                'content': self.locators.SECTION_CONTENT_THIRD
            },
        }
        section_title = self.element_is_visible(accordian[accordian_number]['title'])
        section_title.click()
        try:
            section_content = self.element_is_visible(accordian[accordian_number]['content']).text
            self._check_invisible_accordean(accordian_number)
        except TimeoutException:
            section_title.click()
            section_content = self.element_is_visible(accordian[accordian_number]['content']).text
            self._check_invisible_accordean(accordian_number)
        return [section_title.text, len(section_content)]

    def _check_invisible_accordean(self, accordian_number: str) -> None:
        if accordian_number == 'first':
            self.element_is_not_visible(self.locators.SECTION_CONTENT_SECOND)
            self.element_is_not_visible(self.locators.SECTION_CONTENT_THIRD)
        elif accordian_number == 'second':
            self.element_is_not_visible(self.locators.SECTION_CONTENT_FIRST)
            self.element_is_not_visible(self.locators.SECTION_CONTENT_THIRD)
        else:
            self.element_is_not_visible(self.locators.SECTION_CONTENT_FIRST)
            self.element_is_not_visible(self.locators.SECTION_CONTENT_SECOND)


class AutoCompletePage(BasePage):

    locators = AutoCompletePageLocators()

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver, page=UIRoutes.AUTO_COMPLETE)

    @allure.step('Fill multi autocomplete input')
    def fill_input_multi(self) -> List[str]:
        colors = random.sample(next(generated_color()).color_name, k=random.randint(2, 5))
        for color in colors:
            input_multi = self.element_is_clickable(self.locators.MULTI_INPUT)
            input_multi.send_keys(color)
            input_multi.send_keys(Keys.ENTER)
        return colors

    @allure.step('Remove value from multi autocomplete')
    def remove_value_from_multi(self) -> Tuple[int, int]:
        count_value_before = len(self.elements_are_present(self.locators.MULTI_VALUE))
        remove_button_list = self.elements_are_visible(self.locators.MULTI_VALUE_REMOVE)
        for value in remove_button_list:
            value.click()
            break
        count_value_after = len(self.elements_are_present(self.locators.MULTI_VALUE))
        return count_value_before, count_value_after

    @allure.step('Remove all values from multi autocomplete by cross')
    def remove_all_values_from_multi(self) -> Literal[0] | None:
        self.element_is_visible(self.locators.REMOVE_ALL_VALUES).click()
        try:
            self.element_is_not_visible(self.locators.MULTI_VALUE)
            return 0
        except TimeoutException as e:
            print(e)

    @allure.step('Check colors in multi autocomplete')
    def check_color_in_multi(self) -> List[str]:
        color_list = self.elements_are_present(self.locators.MULTI_VALUE)
        colors = []
        for color in color_list:
            colors.append(color.text)
        return colors

    @allure.step('Fill single autocomplete input')
    def fill_input_single(self) -> str:
        color = random.sample(next(generated_color()).color_name, k=1)
        input_single = self.element_is_clickable(self.locators.SINGLE_INPUT)
        input_single.send_keys(color)
        input_single.send_keys(Keys.ENTER)
        return color[0]

    @allure.step('Check color in single autocomplete')
    def check_color_in_single(self) -> str:
        color = self.element_is_visible(self.locators.SINGLE_VALUE)
        return color.text


class DatePickerPage(BasePage):

    locators = DatePickerPageLocators()

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver, page=UIRoutes.DATE_PICKER)

    @allure.step('Change date')
    def select_date(self) -> Tuple[str | None, str | None]:
        date = next(generated_date())
        input_date = self.element_is_visible(self.locators.DATE_INPUT)
        value_date_before = input_date.get_attribute('value')
        input_date.click()
        self.select_element_by_value(self.locators.DATE_SELECT_MONTH, date.month)
        self.select_element_by_value(self.locators.DATE_SELECT_YEAR, date.year)
        self._set_date_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
        value_date_after = input_date.get_attribute('value')
        return value_date_before, value_date_after

    @allure.step('Change select date and time')
    def select_date_and_time(self) -> Tuple[str | None, str | None]:
        date = next(generated_date())
        input_date = self.element_is_visible(self.locators.DATE_AND_TIME_INPUT)
        value_date_before = input_date.get_attribute('value')
        input_date.click()
        self.element_is_clickable(self.locators.DATE_AND_TIME_MONTH).click()
        self._set_date_item_from_list(self.locators.DATE_AND_TIME_MONTH_LIST, date.month)
        self.element_is_clickable(self.locators.DATE_AND_TIME_YEAR).click()
        self._set_date_item_from_list(self.locators.DATE_AND_TIME_YEAR_LIST, '2020')
        self._set_date_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
        self._set_date_item_from_list(self.locators.DATE_AND_TIME_TIME_LIST, date.time)
        input_date_after = self.element_is_visible(self.locators.DATE_AND_TIME_INPUT)
        value_date_after = input_date_after.get_attribute('value')
        return value_date_before, value_date_after

    @allure.step('Select date item from list')
    def _set_date_item_from_list(self, elements: List[WebElement], value: str) -> None:
        item_list = self.elements_are_present(elements)
        for item in item_list:
            if item.text == value:
                item.click()
                break


class SliderPage(BasePage):

    locators = SliderPageLocators()

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver, page=UIRoutes.SLIDER)

    @allure.step('Change slider value')
    def change_slider_value(self) -> Tuple[str | None, str | None]:
        value_before = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')
        slider_input = self.element_is_visible(self.locators.INPUT_SLIDER)
        self.action_drag_and_drop_by_offset(slider_input, random.randint(1, 100), 0)
        value_after = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')
        return value_before, value_after


class ProgressBarPage(BasePage):

    locators = ProgressBarPageLocators()

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver, page=UIRoutes.PROGRESS_BAR)

    @allure.step('Change progress bar value')
    def change_progress_bar_value(self) -> Tuple[str | None, str | None]:
        value_before = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).get_attribute('aria-valuenow')
        progress_bar_button = self.element_is_clickable(self.locators.PROGRESS_BAR_BUTTON)
        progress_bar_button.click()
        time.sleep(random.randint(4, 6))
        progress_bar_button.click()
        value_after = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).get_attribute('aria-valuenow')
        return value_before, value_after

    @allure.step('Change progress bar value')
    def change_full_progress_bar(self, reset: str = None) -> Tuple[str | None, str | None]:
        value_before = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).get_attribute('aria-valuenow')
        progress_bar_button = self.element_is_clickable(self.locators.PROGRESS_BAR_BUTTON)
        progress_bar_button.click()
        reset_button = self.element_is_clickable(self.locators.RESET_BUTTON)
        if reset:
            reset_button.click()
            value_after = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).get_attribute('aria-valuenow')
        else:
            value_after = self.element_is_present(self.locators.PROGRESS_BAR_SUCCESS_VALUE).get_attribute('aria-valuenow')
        return value_before, value_after


class TabsPage(BasePage):

    locators = TabsPageLocators()

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver, page=UIRoutes.TABS)

    @allure.step('Check tabs')
    def check_tabs(self, tab_name: str) -> Tuple[str, int]:
        tabs = {
            'what': {
                'title': self.locators.TABS_WHAT,
                'content': self.locators.TABS_WHAT_CONTENT
            },
            'origin': {
                'title': self.locators.TABS_ORIGIN,
                'content': self.locators.TABS_ORIGIN_CONTENT
            },
            'use': {
                'title': self.locators.TABS_USE,
                'content': self.locators.TABS_USE_CONTENT
            },
            'more': {
                'title': self.locators.TABS_MORE,
                'content': self.locators.TABS_MORE_CONTENT
            },
        }
        button = self.element_is_visible(tabs[tab_name]['title'])
        button.click()
        content = self.element_is_visible(tabs[tab_name]['content']).text
        return button.text, len(content)


class ToolTipsPage(BasePage):

    locators = ToolTipsPageLocators()

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver, page=UIRoutes.TOOL_TIPS)

    @allure.step('Check tool tip')
    def check_tool_tips(self, tool_tip: str) -> str:
        tool_tips = {
            'button': {
                'locator': self.locators.BUTTON,
                'hover': self.locators.TOOL_TIP_BUTTON
            },
            'field': {
                'locator': self.locators.FIELD,
                'hover': self.locators.TOOL_TIP_FIELD
            },
            'contrary': {
                'locator': self.locators.CONTRARY_LINK,
                'hover': self.locators.TOOL_TIP_CONTRARY
            },
            'section': {
                'locator': self.locators.SECTION_LINK,
                'hover': self.locators.TOOL_TIP_SECTION
            }                                    
        }
        tool_tip_text = self._get_text_from_tool_tips(tool_tips[tool_tip]['locator'], tool_tips[tool_tip]['hover'])
        return tool_tip_text

    @allure.step('Get text from tool tip')
    def _get_text_from_tool_tips(self, hover_element: Tuple[str, str], hover_text: Tuple[str, str]) -> str:
        element = self.element_is_present(hover_element)
        self.action_move_to_element(element)
        self.element_is_visible(hover_text)
        tool_tip_text = self.element_is_visible(self.locators.TOOL_TIPS_INNERS)
        text = tool_tip_text.text
        return text

class MenuPage(BasePage):

    locators = MenuPageLocators()

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver, page=UIRoutes.MENU)

    @allure.step('Check menu item')
    def check_menu(self):
        menu_item_list = self.elements_are_present(self.locators.MENU_ITEM_LIST)
        data = []
        for item in menu_item_list:
            self.action_move_to_element(item)
            data.append(item.text)
        return data