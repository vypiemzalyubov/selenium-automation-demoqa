import allure
import pytest

from pages.interactions_page import (
    DragabblePage,
    DroppablePage,
    ResizablePage,
    SelectablePage,
    SortablePage,
)

pytestmark = allure.suite('Interactions')


@allure.feature('Sortable Page')
class TestSortablePage:
    @allure.title('Check changed sortable list or grid')
    @pytest.mark.parametrize('tab', ['list', 'grid'])
    def test_sortable(self, tab):
        sortable_page = SortablePage(self.driver)
        sortable_page.open()
        sortable_before, sortable_after = sortable_page.change_order(tab)
        assert sortable_before != sortable_after, f'The order of the {tab} has not been changed'


@allure.feature('Selectable Page')
class TestSelectablePage:
    @allure.title('Check changed selectable list or grid of a one item')
    @pytest.mark.parametrize('tab,count', [('list', 'one'), ('grid', 'one')])
    def test_selectable_one_item(self, tab, count):
        selectable_page = SelectablePage(self.driver)
        selectable_page.open()
        item_length = selectable_page.select_item(tab, count)
        assert item_length == 1, f'No elements were selected in {tab}'

    @allure.title('Check changed selectable list or grid of all items')
    @pytest.mark.parametrize('tab,count,length', [('list', 'all', 4), ('grid', 'all', 9)])
    def test_selectable_all_items(self, tab, count, length):
        selectable_page = SelectablePage(self.driver)
        selectable_page.open()
        item_length = selectable_page.select_item(tab, count)
        assert item_length == length, f'Not all elements were selected in {tab}'


@allure.feature('Resizable Page')
class TestResizablePage:
    @allure.title('Check changed "Resizable box"')
    @pytest.mark.flaky(reruns=1, reruns_delay=1)
    def test_resizable_box(self):
        resizable_page = ResizablePage(self.driver)
        resizable_page.open()
        max_box, min_box = resizable_page.change_size_resizable_box()
        assert ('500px', '300px') == max_box, 'Maximum size not equal to "500px", "300px"'
        assert ('150px', '150px') == min_box, 'Minimum size not equal to "150px", "150px"'

    @allure.title('Check changed "Resizable"')
    def test_resizable(self):
        resizable_page = ResizablePage(self.driver)
        resizable_page.open()
        max_resize, min_resize = resizable_page.change_size_resizable()
        assert min_resize != max_resize, 'Resizable has not been changed'


@allure.feature('Droppable Page')
class TestDroppablePage:
    @allure.title('Check "Simple" droppable')
    def test_simple_droppable(self):
        droppable_page = DroppablePage(self.driver)
        droppable_page.open()
        text = droppable_page.drop_simple()
        assert text == 'Dropped!', 'The elements has not been dropped'

    @allure.title('Check accebtable div in "Accept" droppable')
    def test_accept_droppable_accebtable(self):
        droppable_page = DroppablePage(self.driver)
        droppable_page.open()
        accept_result = droppable_page.drop_accept('acceptable')
        assert accept_result == 'Dropped!', 'The dropped element has not been accepted'

    @allure.title('Check not accebtable div in "Accept" droppable')
    def test_accept_droppable_not_accebtable(self):
        droppable_page = DroppablePage(self.driver)
        droppable_page.open()
        accept_result = droppable_page.drop_accept('not_acceptable')
        assert accept_result == 'Drop here', 'The dropped element has been accepted'

    @allure.title('Check not greedy box in "Prevent Propogation" droppable')
    @pytest.mark.flaky(reruns=1, reruns_delay=1)
    def test_prevent_propogation_droppable_not_greedy(self):
        droppable_page = DroppablePage(self.driver)
        droppable_page.open()
        outer_box_text, inner_box_text = droppable_page.drop_prevent_propogation('not_greedy')
        assert outer_box_text == 'Dropped!', 'The elements texts has not been changed'
        assert inner_box_text == 'Dropped!', 'The elements texts has not been changed'

    @allure.title('Check greedy box in "Prevent Propogation" droppable')
    @pytest.mark.flaky(reruns=1, reruns_delay=1)
    def test_prevent_propogation_droppable_greedy(self):
        droppable_page = DroppablePage(self.driver)
        droppable_page.open()
        outer_box_text, inner_box_text = droppable_page.drop_prevent_propogation('greedy')
        assert outer_box_text == 'Outer droppable', 'The elements texts has been changed'
        assert inner_box_text == 'Dropped!', 'The elements texts has not been changed'

    @allure.title('Check will revert in "Revert draggable" droppable')
    def test_will_revert_draggable_droppable(self):
        droppable_page = DroppablePage(self.driver)
        droppable_page.open()
        position_after_move, position_after_revert = droppable_page.drop_revert_draggable('will')
        assert position_after_move != position_after_revert, 'The elements has not reverted'

    @allure.title('Check not will revert in "Revert draggable" droppable')
    def test_not_will_revert_draggable_droppable(self):
        droppable_page = DroppablePage(self.driver)
        droppable_page.open()
        position_after_move, position_after_revert = droppable_page.drop_revert_draggable(
            'not_will'
        )
        assert position_after_move == position_after_revert, 'The elements has reverted'


@allure.feature('Dragabble Page')
class TestDragabblePage:
    @allure.title('Check "Simple" dragabble')
    def test_simple_dragabble(self):
        dragabble_page = DragabblePage(self.driver)
        dragabble_page.open()
        before, after = dragabble_page.simple_drag_box()
        assert before != after, 'The position of the box has not been changed'

    @allure.title('Check Only X in "Axis Restricted" dragabble')
    @pytest.mark.flaky(reruns=1, reruns_delay=1)
    def test_axis_restricted_dragabble_only_x(self):
        dragabble_page = DragabblePage(self.driver)
        dragabble_page.open()
        top_before, top_after, left_before, left_after = dragabble_page.drag_axis_restricted(
            'only_x'
        )
        assert (
            top_before == top_after and int(top_after) == 0
        ), 'Box position has not changed or there has been a shift in the y-axis'
        assert (
            left_before != left_after and int(left_before) != 0
        ), 'Box position has not changed or there has been a shift in the y-axis'

    @allure.title('Check Only Y in "Axis Restricted" dragabble')
    @pytest.mark.flaky(reruns=1, reruns_delay=1)
    def test_axis_restricted_dragabble_only_y(self):
        dragabble_page = DragabblePage(self.driver)
        dragabble_page.open()
        top_before, top_after, left_before, left_after = dragabble_page.drag_axis_restricted(
            'only_y'
        )
        assert (
            top_before != top_after and top_after != 0
        ), 'Box position has not changed or there has been a shift in the x-axis'
        assert (
            left_before == left_after and int(left_after) == 0
        ), 'Box position has not changed or there has been a shift in the x-axis'
