import random
import re
import time
from typing import List, Tuple

import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from locators.interactions_page_locators import (
    SortablePageLocators,
    SelectablePageLocators,
    ResizablePageLocators,
    DroppablePageLocators,
    DraggablePageLocators
)
from pages.base_page import BasePage
from utils.routes import UIRoutes


class SortablePage(BasePage):
    locators = SortablePageLocators()

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver, page=UIRoutes.SORTABLE)

    @allure.step('Change list or grid order')
    def change_order(self, tab_name: str) -> Tuple[List[str], List[str]]:
        tabs = {
            'list': {
                'tab': self.locators.TAB_LIST,
                'item': self.locators.LIST_ITEM
            },
            'grid': {
                'tab': self.locators.TAB_GRID,
                'item': self.locators.GRID_ITEM
            }
        }
        self.element_is_visible(tabs[tab_name]['tab']).click()
        order_before = self._get_sortable_items(tabs[tab_name]['item'])
        item_list = random.sample(self.elements_are_visible(tabs[tab_name]['item']), k=2)
        item_what = item_list[0]
        item_where = item_list[1]
        self.action_drag_and_drop_to_element(item_what, item_where)
        order_after = self._get_sortable_items(tabs[tab_name]['item'])
        return order_before, order_after

    @allure.step('Get sortable items')
    def _get_sortable_items(self, elements) -> List[str]:
        item_list = self.elements_are_visible(elements)
        return [item.text for item in item_list]


class SelectablePage(BasePage):
    locators = SelectablePageLocators()

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver, page=UIRoutes.SELECTABLE)

    @allure.step('Select list or grid item')
    def select_item(self, tab_name: str, count: str) -> int:
        tabs = {
            'list': {
                'tab': self.locators.TAB_LIST,
                'item': self.locators.LIST_ITEM,
                'active': self.locators.LIST_ITEM_ACTIVE
            },
            'grid': {
                'tab': self.locators.TAB_GRID,
                'item': self.locators.GRID_ITEM,
                'active': self.locators.GRID_ITEM_ACTIVE
            }
        }
        self.element_is_visible(tabs[tab_name]['tab']).click()
        self._click_selectable_item(tabs[tab_name]['item'], count)
        active_elements = self.elements_are_visible(tabs[tab_name]['active'])
        return len(active_elements)

    @allure.step('Click selectable item')
    def _click_selectable_item(self, elements: List[str], count: str) -> None:
        item_list = self.elements_are_visible(elements)
        if count == 'one':
            random.sample(item_list, k=1)[0].click()
        else:
            [item.click() for item in item_list]


class ResizablePage(BasePage):
    locators = ResizablePageLocators()

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver, page=UIRoutes.RESIZABLE)

    @allure.step('Change size resizable box')
    def change_size_resizable_box(self) -> Tuple[Tuple[str, str], Tuple[str, str]]:
        self.action_drag_and_drop_by_offset(self.element_is_present(self.locators.RESIZABLE_BOX_HANDLE), 400, 200)
        max_size = self._get_px_from_width_height(self._get_max_min_size(self.locators.RESIZABLE_BOX))
        self.action_drag_and_drop_by_offset(self.element_is_present(self.locators.RESIZABLE_BOX_HANDLE), -500, -300)
        min_size = self._get_px_from_width_height(self._get_max_min_size(self.locators.RESIZABLE_BOX))
        return max_size, min_size

    @allure.step('Change size resizable')
    def change_size_resizable(self) -> Tuple[Tuple[str, str], Tuple[str, str]]:
        self.action_drag_and_drop_by_offset(self.element_is_visible(self.locators.RESIZABLE_HANDLE),
                                            random.randint(1, 300), random.randint(1, 300))
        max_size = self._get_px_from_width_height(self._get_max_min_size(self.locators.RESIZABLE))
        self.action_drag_and_drop_by_offset(self.element_is_visible(self.locators.RESIZABLE_HANDLE),
                                            random.randint(-200, -1), random.randint(-200, -1))
        min_size = self._get_px_from_width_height(self._get_max_min_size(self.locators.RESIZABLE))
        return max_size, min_size

    @allure.step('Get pixel from width and height')
    def _get_px_from_width_height(self, value_of_size: str) -> Tuple[str, str]:
        width = value_of_size.split(';')[0].split(':')[1].replace(' ', '')
        height = value_of_size.split(';')[1].split(':')[1].replace(' ', '')
        return width, height

    @allure.step('Get max and min size')
    def _get_max_min_size(self, element: WebElement) -> str:
        size = self.element_is_present(element)
        size_value = size.get_attribute('style')
        return size_value


class DroppablePage(BasePage):
    locators = DroppablePageLocators()

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver, page=UIRoutes.DROPPABLE)

    @allure.step('Drop simple div')
    def drop_simple(self) -> str:
        self.element_is_visible(self.locators.SIMPLE_TAB).click()
        drag_div = self.element_is_visible(self.locators.DRAG_ME_SIMPLE)
        drop_div = self.element_is_visible(self.locators.DROP_HERE_SIMPLE)
        self.action_drag_and_drop_to_element(drag_div, drop_div)
        return drop_div.text

    @allure.step('Drop accept div')
    def drop_accept(self, accept: str) -> str:
        accepts = {
            "acceptable": self.locators.ACCEPTABLE,
            "not_acceptable": self.locators.NOT_ACCEPTABLE
        }
        self.element_is_visible(self.locators.ACCEPT_TAB).click()
        accept_div = self.element_is_visible(accepts[accept])
        drop_div = self.element_is_visible(self.locators.DROP_HERE_ACCEPT)
        self.action_drag_and_drop_to_element(accept_div, drop_div)
        drop_text = drop_div.text
        return drop_text

    @allure.step('Drop prevent propogation div')
    def drop_prevent_propogation(self, propogation: str) -> Tuple[str, str]:
        propogations = {
            'greedy': {
                'box': self.locators.GREEDY_INNER_BOX,
                'text': self.locators.GREEDY_DROP_BOX_TEXT
            },
            'not_greedy': {
                'box': self.locators.NOT_GREEDY_INNER_BOX,
                'text': self.locators.NOT_GREEDY_DROP_BOX_TEXT
            }
        }
        self.element_is_visible(self.locators.PREVENT_TAB).click()
        drag_div = self.element_is_visible(self.locators.DRAG_ME_PREVENT)
        inner_box = self.element_is_visible(propogations[propogation]['box'])
        self.action_drag_and_drop_to_element(drag_div, inner_box)
        outer_box_text = self.element_is_visible(propogations[propogation]['text']).text
        inner_box_text = inner_box.text
        return outer_box_text, inner_box_text

    @allure.step('Drag revert draggable div')
    def drop_revert_draggable(self, type_drag: str) -> Tuple[str, str]:
        drags = {
            'will': self.locators.WILL_REVERT,
            'not_will': self.locators.NOT_REVERT
        }
        self.element_is_visible(self.locators.REVERT_TAB).click()
        revert = self.element_is_visible(drags[type_drag])
        drop_div = self.element_is_visible(self.locators.DROP_HERE_REVERT)
        self.action_drag_and_drop_to_element(revert, drop_div)
        position_after_move = revert.get_attribute('style')
        time.sleep(1)
        position_after_revert = revert.get_attribute('style')
        return position_after_move, position_after_revert


class DragabblePage(BasePage):
    locators = DraggablePageLocators()

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver, page=UIRoutes.DRAGABBLE)

    @allure.step('Simple drag and drop')
    def simple_drag_box(self) -> Tuple[str, str]:
        self.element_is_visible(self.locators.SIMPLE_TAB).click()
        drag_div = self.element_is_visible(self.locators.DRAG_ME)
        position_before, position_after = self._get_before_and_after_position(drag_div)
        return position_before, position_after

    @allure.step('Drag axis restricted element')
    def drag_axis_restricted(self, type_only: str) -> Tuple[str, str, str, str]:
        only = {
            'only_x': self.locators.ONLY_X,
            'only_y': self.locators.ONLY_Y
        }
        self.element_is_visible(self.locators.AXIS_TAB).click()
        only_element = self.element_is_visible(only[type_only])
        position_before, position_after = self._get_before_and_after_position(only_element)
        top_before = self._get_top_position(position_before)
        top_after = self._get_top_position(position_after)
        left_before = self._get_left_position(position_before)
        left_after = self._get_left_position(position_after)
        return top_before[0], top_after[0], left_before[0], left_after[0]

    @allure.step('Get before and after positions')
    def _get_before_and_after_position(self, drag_element: WebElement) -> Tuple[str, str]:
        self.action_drag_and_drop_by_offset(drag_element, random.randint(0, 50), random.randint(0, 50))
        before_position = drag_element.get_attribute('style')
        self.action_drag_and_drop_by_offset(drag_element, random.randint(0, 50), random.randint(0, 50))
        after_position = drag_element.get_attribute('style')
        return before_position, after_position

    @allure.step('Get top position')
    def _get_top_position(self, positions: str) -> List[str]:
        return re.findall(r"[0-9]+", positions.split(';')[2])

    @allure.step('Get left position')
    def _get_left_position(self, positions: str) -> List[str]:
        return re.findall(r"[0-9]+", positions.split(';')[1])
