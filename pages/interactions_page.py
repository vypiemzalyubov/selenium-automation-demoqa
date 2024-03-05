import random
import re
import time

import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage
from utils.routes import UIRoutes


class SortablePage(BasePage):
    TAB_LIST = (By.CSS_SELECTOR, 'a[id="demo-tab-list"]')
    LIST_ITEM = (
        By.CSS_SELECTOR,
        'div[id="demo-tabpane-list"] div[class="list-group-item list-group-item-action"]',
    )

    TAB_GRID = (By.CSS_SELECTOR, 'a[id="demo-tab-grid"]')
    GRID_ITEM = (
        By.CSS_SELECTOR,
        'div[id="demo-tabpane-grid"] div[class="list-group-item list-group-item-action"]',
    )

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver, page=UIRoutes.SORTABLE)

    @allure.step('Change list or grid order')
    def change_order(self, tab_name: str) -> tuple[list[str], list[str]]:
        tabs = {
            'list': {'tab': self.TAB_LIST, 'item': self.LIST_ITEM},
            'grid': {'tab': self.TAB_GRID, 'item': self.GRID_ITEM},
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
    def _get_sortable_items(self, elements) -> list[str]:
        item_list = self.elements_are_visible(elements)
        return [item.text for item in item_list]


class SelectablePage(BasePage):
    TAB_LIST = (By.CSS_SELECTOR, "a[id='demo-tab-list']")
    LIST_ITEM = (
        By.CSS_SELECTOR,
        'ul[id="verticalListContainer"] li[class="mt-2 list-group-item list-group-item-action"]',
    )
    LIST_ITEM_ACTIVE = (
        By.CSS_SELECTOR,
        'ul[id="verticalListContainer"] li[class="mt-2 list-group-item active list-group-item-action"]',
    )

    TAB_GRID = (By.CSS_SELECTOR, 'a[id="demo-tab-grid"]')
    GRID_ITEM = (
        By.CSS_SELECTOR,
        'div[id="gridContainer"]  li[class="list-group-item list-group-item-action"]',
    )
    GRID_ITEM_ACTIVE = (
        By.CSS_SELECTOR,
        'div[id="gridContainer"]  li[class="list-group-item active list-group-item-action"]',
    )

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver, page=UIRoutes.SELECTABLE)

    @allure.step('Select list or grid item')
    def select_item(self, tab_name: str, count: str) -> int:
        tabs = {
            'list': {
                'tab': self.TAB_LIST,
                'item': self.LIST_ITEM,
                'active': self.LIST_ITEM_ACTIVE,
            },
            'grid': {
                'tab': self.TAB_GRID,
                'item': self.GRID_ITEM,
                'active': self.GRID_ITEM_ACTIVE,
            },
        }
        self.element_is_visible(tabs[tab_name]['tab']).click()
        self._click_selectable_item(tabs[tab_name]['item'], count)
        active_elements = self.elements_are_visible(tabs[tab_name]['active'])
        return len(active_elements)

    @allure.step('Click selectable item')
    def _click_selectable_item(self, elements: list[str], count: str) -> None:
        item_list = self.elements_are_visible(elements)
        if count == 'one':
            random.sample(item_list, k=1)[0].click()
        else:
            [item.click() for item in item_list]


class ResizablePage(BasePage):
    RESIZABLE_BOX_HANDLE = (
        By.CSS_SELECTOR,
        'div[class="constraint-area"] span[class="react-resizable-handle react-resizable-handle-se"]',
    )
    RESIZABLE_BOX = (By.CSS_SELECTOR, 'div[id="resizableBoxWithRestriction"]')
    RESIZABLE_HANDLE = (
        By.CSS_SELECTOR,
        'div[id="resizable"] span[class="react-resizable-handle react-resizable-handle-se"]',
    )
    RESIZABLE = (By.CSS_SELECTOR, 'div[id="resizable"]')

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver, page=UIRoutes.RESIZABLE)

    @allure.step('Change size resizable box')
    def change_size_resizable_box(self) -> tuple[tuple[str, str], tuple[str, str]]:
        self.action_drag_and_drop_by_offset(
            self.element_is_present(self.RESIZABLE_BOX_HANDLE), 400, 200
        )
        max_size = self._get_px_from_width_height(self._get_max_min_size(self.RESIZABLE_BOX))
        self.action_drag_and_drop_by_offset(
            self.element_is_present(self.RESIZABLE_BOX_HANDLE), -500, -300
        )
        min_size = self._get_px_from_width_height(self._get_max_min_size(self.RESIZABLE_BOX))
        return max_size, min_size

    @allure.step('Change size resizable')
    def change_size_resizable(self) -> tuple[tuple[str, str], tuple[str, str]]:
        self.action_drag_and_drop_by_offset(
            self.element_is_visible(self.RESIZABLE_HANDLE),
            random.randint(1, 300),
            random.randint(1, 300),
        )
        max_size = self._get_px_from_width_height(self._get_max_min_size(self.RESIZABLE))
        self.action_drag_and_drop_by_offset(
            self.element_is_visible(self.RESIZABLE_HANDLE),
            random.randint(-200, -1),
            random.randint(-200, -1),
        )
        min_size = self._get_px_from_width_height(self._get_max_min_size(self.RESIZABLE))
        return max_size, min_size

    @allure.step('Get pixel from width and height')
    def _get_px_from_width_height(self, value_of_size: str) -> tuple[str, str]:
        width = value_of_size.split(';')[0].split(':')[1].replace(' ', '')
        height = value_of_size.split(';')[1].split(':')[1].replace(' ', '')
        return width, height

    @allure.step('Get max and min size')
    def _get_max_min_size(self, element: WebElement) -> str:
        size = self.element_is_present(element)
        size_value = size.get_attribute('style')
        return size_value


class DroppablePage(BasePage):
    # simple
    SIMPLE_TAB = (By.CSS_SELECTOR, 'a[id="droppableExample-tab-simple"]')
    DRAG_ME_SIMPLE = (By.CSS_SELECTOR, 'div[id="draggable"]')
    DROP_HERE_SIMPLE = (By.CSS_SELECTOR, '#simpleDropContainer #droppable')

    # accept
    ACCEPT_TAB = (By.CSS_SELECTOR, 'a[id="droppableExample-tab-accept"]')
    ACCEPTABLE = (By.CSS_SELECTOR, 'div[id="acceptable"]')
    NOT_ACCEPTABLE = (By.CSS_SELECTOR, 'div[id="notAcceptable"]')
    DROP_HERE_ACCEPT = (By.CSS_SELECTOR, '#acceptDropContainer #droppable')

    # prevent Propogation
    PREVENT_TAB = (By.CSS_SELECTOR, 'a[id="droppableExample-tab-preventPropogation"]')
    NOT_GREEDY_DROP_BOX_TEXT = (By.CSS_SELECTOR, 'div[id="notGreedyDropBox"] p:nth-child(1)')
    NOT_GREEDY_INNER_BOX = (By.CSS_SELECTOR, 'div[id="notGreedyInnerDropBox"]')
    GREEDY_DROP_BOX_TEXT = (By.CSS_SELECTOR, 'div[id="greedyDropBox"] p:nth-child(1)')
    GREEDY_INNER_BOX = (By.CSS_SELECTOR, 'div[id="greedyDropBoxInner"]')
    DRAG_ME_PREVENT = (By.CSS_SELECTOR, '#ppDropContainer #dragBox')

    # revert Draggable
    REVERT_TAB = (By.CSS_SELECTOR, 'a[id="droppableExample-tab-revertable"]')
    WILL_REVERT = (By.CSS_SELECTOR, 'div[id="revertable"]')
    NOT_REVERT = (By.CSS_SELECTOR, 'div[id="notRevertable"]')
    DROP_HERE_REVERT = (By.CSS_SELECTOR, '#revertableDropContainer #droppable')

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver, page=UIRoutes.DROPPABLE)

    @allure.step('Drop simple div')
    def drop_simple(self) -> str:
        self.element_is_visible(self.SIMPLE_TAB).click()
        drag_div = self.element_is_visible(self.DRAG_ME_SIMPLE)
        drop_div = self.element_is_visible(self.DROP_HERE_SIMPLE)
        self.action_drag_and_drop_to_element(drag_div, drop_div)
        return drop_div.text

    @allure.step('Drop accept div')
    def drop_accept(self, accept: str) -> str:
        accepts = {
            'acceptable': self.ACCEPTABLE,
            'not_acceptable': self.NOT_ACCEPTABLE,
        }
        self.element_is_visible(self.ACCEPT_TAB).click()
        accept_div = self.element_is_visible(accepts[accept])
        drop_div = self.element_is_visible(self.DROP_HERE_ACCEPT)
        self.action_drag_and_drop_to_element(accept_div, drop_div)
        drop_text = drop_div.text
        return drop_text

    @allure.step('Drop prevent propogation div')
    def drop_prevent_propogation(self, propogation: str) -> tuple[str, str]:
        propogations = {
            'greedy': {
                'box': self.GREEDY_INNER_BOX,
                'text': self.GREEDY_DROP_BOX_TEXT,
            },
            'not_greedy': {
                'box': self.NOT_GREEDY_INNER_BOX,
                'text': self.NOT_GREEDY_DROP_BOX_TEXT,
            },
        }
        self.element_is_visible(self.PREVENT_TAB).click()
        drag_div = self.element_is_visible(self.DRAG_ME_PREVENT)
        inner_box = self.element_is_visible(propogations[propogation]['box'])
        self.action_drag_and_drop_to_element(drag_div, inner_box)
        outer_box_text = self.element_is_visible(propogations[propogation]['text']).text
        inner_box_text = inner_box.text
        return outer_box_text, inner_box_text

    @allure.step('Drag revert draggable div')
    def drop_revert_draggable(self, type_drag: str) -> tuple[str, str]:
        drags = {'will': self.WILL_REVERT, 'not_will': self.NOT_REVERT}
        self.element_is_visible(self.REVERT_TAB).click()
        revert = self.element_is_visible(drags[type_drag])
        drop_div = self.element_is_visible(self.DROP_HERE_REVERT)
        self.action_drag_and_drop_to_element(revert, drop_div)
        position_after_move = revert.get_attribute('style')
        time.sleep(1)
        position_after_revert = revert.get_attribute('style')
        return position_after_move, position_after_revert


class DragabblePage(BasePage):
    # simple
    SIMPLE_TAB = (By.CSS_SELECTOR, 'a[id="draggableExample-tab-simple"]')
    DRAG_ME = (By.CSS_SELECTOR, 'div[id="draggableExample-tabpane-simple"] div[id="dragBox"]')

    # axis Restricted
    AXIS_TAB = (By.CSS_SELECTOR, 'a[id="draggableExample-tab-axisRestriction"]')
    ONLY_X = (By.CSS_SELECTOR, 'div[id="restrictedX"]')
    ONLY_Y = (By.CSS_SELECTOR, 'div[id="restrictedY"]')

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver, page=UIRoutes.DRAGABBLE)

    @allure.step('Simple drag and drop')
    def simple_drag_box(self) -> tuple[str, str]:
        self.element_is_visible(self.SIMPLE_TAB).click()
        drag_div = self.element_is_visible(self.DRAG_ME)
        position_before, position_after = self._get_before_and_after_position(drag_div)
        return position_before, position_after

    @allure.step('Drag axis restricted element')
    def drag_axis_restricted(self, type_only: str) -> tuple[str, str, str, str]:
        only = {'only_x': self.ONLY_X, 'only_y': self.ONLY_Y}
        self.element_is_visible(self.AXIS_TAB).click()
        only_element = self.element_is_visible(only[type_only])
        position_before, position_after = self._get_before_and_after_position(only_element)
        top_before = self._get_top_position(position_before)
        top_after = self._get_top_position(position_after)
        left_before = self._get_left_position(position_before)
        left_after = self._get_left_position(position_after)
        return top_before[0], top_after[0], left_before[0], left_after[0]

    @allure.step('Get before and after positions')
    def _get_before_and_after_position(self, drag_element: WebElement) -> tuple[str, str]:
        self.action_drag_and_drop_by_offset(
            drag_element, random.randint(0, 50), random.randint(0, 50)
        )
        before_position = drag_element.get_attribute('style')
        self.action_drag_and_drop_by_offset(
            drag_element, random.randint(0, 50), random.randint(0, 50)
        )
        after_position = drag_element.get_attribute('style')
        return before_position, after_position

    @allure.step('Get top position')
    def _get_top_position(self, positions: str) -> list[str]:
        return re.findall(r'[0-9]+', positions.split(';')[2])

    @allure.step('Get left position')
    def _get_left_position(self, positions: str) -> list[str]:
        return re.findall(r'[0-9]+', positions.split(';')[1])
