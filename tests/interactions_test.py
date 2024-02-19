import allure
import pytest

from pages.interactions_page import (
    SortablePage, 
    SelectablePage, 
    ResizablePage, 
    DroppablePage, 
    DraggablePage
)


@allure.suite('Interactions')
@allure.feature('Sortable Page')
class TestSortablePage:

    @allure.title('Check changed sortable list or grid')
    @pytest.mark.parametrize(
        'tab', 
        ['list', 'grid']
    )
    def test_sortable(self, driver, tab):
        sortable_page = SortablePage(driver)
        sortable_page.open()
        sortable_before, sortable_after = sortable_page.change_order(tab)
        assert sortable_before != sortable_after, \
            f'The order of the {tab} has not been changed'


@allure.suite('Interactions')
@allure.feature('Selectable Page')
class TestSelectablePage:

    @allure.title('Check changed selectable list or grid of a one item')
    @pytest.mark.parametrize(
        'tab,count', 
        [('list', 'one'), ('grid', 'one')]
    )    
    def test_selectable_one_item(self, driver, tab, count):
        selectable_page = SelectablePage(driver)
        selectable_page.open()
        item_length = selectable_page.select_item(tab, count)
        assert item_length == 1, \
            f'No elements were selected in {tab}'

    @allure.title('Check changed selectable list or grid of all items')
    @pytest.mark.parametrize(
        'tab,count,length', 
        [('list', 'all', 4), ('grid', 'all', 9)]
    )    
    def test_selectable_all_items(self, driver, tab, count, length):
        selectable_page = SelectablePage(driver)
        selectable_page.open()
        item_length = selectable_page.select_item(tab, count)
        assert item_length == length, \
            f'Not all elements were selected in {tab}'


@allure.suite('Interactions')
@allure.feature('Resizable Page')
class TestResizablePage:

    @allure.title('Check changed "Resizable box"')
    def test_resizable_box(self, driver):
        resizable_page = ResizablePage(driver)
        resizable_page.open()
        max_box, min_box = resizable_page.change_size_resizable_box()
        assert ('500px', '300px') == max_box, \
            'Maximum size not equal to "500px", "300px"'
        assert ('150px', '150px') == min_box, \
            'Minimum size not equal to "150px", "150px"'

    @allure.title('Check changed "Resizable"')
    def test_resizable(self, driver):
        resizable_page = ResizablePage(driver)
        resizable_page.open()
        max_resize, min_resize = resizable_page.change_size_resizable()
        assert min_resize != max_resize, \
            'Resizable has not been changed'


@allure.suite('Interactions')
@allure.feature('Droppable Page')
class TestDroppablePage:

    @allure.title('Check "Simple" droppable')
    def test_simple_droppable(self, driver):
        droppable_page = DroppablePage(driver)
        droppable_page.open()
        text = droppable_page.drop_simple()
        assert text == 'Dropped!', \
            'The elements has not been dropped'

    @allure.title('Check accebtable div in "Accept" droppable')
    def test_accept_droppable_accebtable(self, driver):
        droppable_page = DroppablePage(driver)
        droppable_page.open()
        accept_result = droppable_page.drop_accept('acceptable')
        assert accept_result == 'Dropped!', \
            'The dropped element has not been accepted'

    @allure.title('Check not accebtable div in "Accept" droppable')
    def test_accept_droppable_not_accebtable(self, driver):
        droppable_page = DroppablePage(driver)
        droppable_page.open()
        accept_result = droppable_page.drop_accept('not_acceptable')
        assert accept_result == 'Drop here', \
            'The dropped element has been accepted'

    @allure.title('Check not greedy box in "Prevent Propogation" droppable')
    def test_prevent_propogation_droppable_not_greedy(self, driver):
        droppable_page = DroppablePage(driver)
        droppable_page.open()
        outer_box_text, inner_box_text = droppable_page.drop_prevent_propogation('not_greedy')
        assert outer_box_text == 'Dropped!', \
            'The elements texts has not been changed'
        assert inner_box_text == 'Dropped!', \
            'The elements texts has not been changed'

    @allure.title('Check greedy box in "Prevent Propogation" droppable')
    def test_prevent_propogation_droppable_greedy(self, driver):
        droppable_page = DroppablePage(driver)
        droppable_page.open()
        outer_box_text, inner_box_text = droppable_page.drop_prevent_propogation('greedy')
        assert outer_box_text == 'Outer droppable', \
            'The elements texts has been changed'
        assert inner_box_text == 'Dropped!', \
            'The elements texts has not been changed'

    @allure.title('Check will revert in "Revert draggable" droppable')
    def test_will_revert_draggable_droppable(self, driver):
        droppable_page = DroppablePage(driver)
        droppable_page.open()
        position_after_move, position_after_revert = droppable_page.drop_revert_draggable('will')
        assert position_after_move != position_after_revert, \
            'The elements has not reverted'

    @allure.title('Check not will revert in "Revert draggable" droppable')
    def test_not_will_revert_draggable_droppable(self, driver):
        droppable_page = DroppablePage(driver)
        droppable_page.open()
        position_after_move, position_after_revert = droppable_page.drop_revert_draggable('not_will')
        assert position_after_move == position_after_revert, \
            'The elements has reverted'


@allure.suite('Interactions')
@allure.feature('Draggable Page')
class TestDraggablePage:
    
    @allure.title('Check simple draggable')
    def test_simple_draggable(self, driver):
        draggable_page = DraggablePage(driver, 'https://demoqa.com/dragabble')
        draggable_page.open()
        before, after = draggable_page.simple_drag_box()
        assert before != after, 'the position of the box has not been changed'

    @allure.title('Check axis restricted draggable')
    def test_axis_restricted_draggable(self, driver):
        draggable_page = DraggablePage(driver, 'https://demoqa.com/dragabble')
        draggable_page.open()
        top_x, left_x = draggable_page.axis_restricted_x()
        top_y, left_y = draggable_page.axis_restricted_y()
        assert top_x[0][0] == top_x[1][0] and int(
            top_x[1][0]) == 0, "box position has not changed or there has been a shift in the y-axis"
        assert left_x[0][0] != left_x[1][0] and int(
            left_x[1][0]) != 0, "box position has not changed or there has been a shift in the y-axis"
        assert top_y[0][0] != top_y[1][0] and int(
            top_y[1][0]) != 0, "box position has not changed or there has been a shift in the x-axis"
        assert left_y[0][0] == left_y[1][0] and int(
            left_y[1][0]) == 0, "box position has not changed or there has been a shift in the x-axis"
