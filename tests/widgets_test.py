import time
import allure
import pytest

from pages.widgets_page import (
    AccordianPage,
    AutoCompletePage,
    DatePickerPage,
    MenuPage,
    ProgressBarPage,
    SelectMenuPage,
    SliderPage,
    TabsPage,
    ToolTipsPage
)


@allure.suite('Widgets')
@allure.feature('Accordian Page')
class TestAccordianPage:

    @allure.title('Check accordian widget')
    def test_accordian(self):
        accordian_page = AccordianPage(self.driver)
        accordian_page.open()
        first_title, first_content = accordian_page.check_accordian('first')
        second_title, second_content = accordian_page.check_accordian('second')
        third_title, third_content = accordian_page.check_accordian('third')
        assert first_title == 'What is Lorem Ipsum?' and first_content > 0, \
            'Incorrect title or missing text for first accordian'
        assert second_title == 'Where does it come from?' and second_content > 0, \
            'Incorrect title or missing text for second accordian'
        assert third_title == 'Why do we use it?' and third_content > 0, \
            'Incorrect title or missing text for third accordian'


@allure.suite('Widgets')
@allure.feature('Autocomplete page')
class TestAutoCompletePage:

    @allure.title('Check the autocomplete is filled')
    def test_fill_multi_autocomplete(self):
        autocomplete_page = AutoCompletePage(self.driver)
        autocomplete_page.open()
        colors = autocomplete_page.fill_input_multi()
        colors_result = autocomplete_page.check_color_in_multi()
        assert colors == colors_result, \
            'The added color is missing in the input'

    @allure.title('Check deletions from the multi autocomplete')
    def test_remove_value_from_multi(self):
        autocomplete_page = AutoCompletePage(self.driver)
        autocomplete_page.open()
        autocomplete_page.fill_input_multi()
        count_value_before, count_value_after = autocomplete_page.remove_value_from_multi()
        assert count_value_before != count_value_after, \
            'Value was not deleted'

    @allure.title('Check deletions from the multi autocomplete by cross')
    def test_remove_all_values_from_multi_by_cross(self):
        autocomplete_page = AutoCompletePage(self.driver)
        autocomplete_page.open()
        autocomplete_page.fill_input_multi()
        count_value = autocomplete_page.remove_all_values_from_multi()
        assert count_value == 0, \
            'Not all values have been deleted'

    @allure.title('Check deletions from the single autocomplete')
    def test_fill_single_autocomplete(self):
        autocomplete_page = AutoCompletePage(self.driver)
        autocomplete_page.open()
        color = autocomplete_page.fill_input_single()
        color_result = autocomplete_page.check_color_in_single()
        assert color == color_result, \
            'The added colors are missing in the input'


@allure.suite('Widgets')
@allure.feature('Date Picker Page')
class TestDatePickerPage:

    @allure.title('Check change date')
    def test_change_date(self):
        date_picker_page = DatePickerPage(self.driver)
        date_picker_page.open()
        value_date_before, value_date_after = date_picker_page.select_date()
        assert value_date_before != value_date_after, \
            'The date has not been changed'

    @allure.title('Check change date and time')
    def test_change_date_and_time(self):
        date_picker_page = DatePickerPage(self.driver)
        date_picker_page.open()
        value_date_before, value_date_after = date_picker_page.select_date_and_time()
        assert value_date_before != value_date_after, \
            'The date and time have not been changed'


@allure.suite('Widgets')
@allure.feature('Slider Page')
class TestSliderPage:

    @allure.title('Check moved slider')
    def test_slider(self):
        slider = SliderPage(self.driver)
        slider.open()
        before, after = slider.change_slider_value()
        assert before != after, \
            'The slider value has not been changed'


@allure.suite('Widgets')
@allure.feature('Progress Bar Page')
class TestProgressBarPage:

    @allure.title('Check changed progress bar')
    def test_progress_bar(self):
        progress_bar = ProgressBarPage(self.driver)
        progress_bar.open()
        before, after = progress_bar.change_progress_bar_value()
        assert before != after, \
            'The progress bar value has not been changed'

    @allure.title('Check full progress bar')
    def test_full_progress_bar(self):
        progress_bar = ProgressBarPage(self.driver)
        progress_bar.open()
        before, after = progress_bar.change_full_progress_bar()
        assert before != after, \
            'The progress bar value has not been changed'
        assert int(after) == 100, \
            'The progress bar value is not equal to 100'

    @allure.title('Check progress bar after reset')
    def test_reset_progress_bar(self):
        progress_bar = ProgressBarPage(self.driver)
        progress_bar.open()
        before, after = progress_bar.change_full_progress_bar('reset')
        assert before == after, \
            'The progress bar value has not been changed after pressing "Reset"'


@allure.suite('Widgets')
@allure.feature('Tabs Page')
class TestTabsPage:

    @allure.title('Check switched tabs')
    @pytest.mark.parametrize(
        'tab_name',
        [
            pytest.param('what'),
            pytest.param('origin'),
            pytest.param('use'),
            pytest.param('more', marks=pytest.mark.xfail(
                reason='BUG-02: The "More" tab is not clickable'))
        ]
    )
    def test_tabs(self, tab_name):
        tabs = TabsPage(self.driver)
        tabs.open()
        button_text, content = tabs.check_tabs(tab_name)
        assert button_text.lower() == tab_name and content != 0, \
            f'The tab "{tab_name}" was not pressed or the text is missing'


@allure.suite('Widgets')
@allure.feature('Tool Tips')
class TestToolTips:

    @allure.title('Check tool tips')
    @pytest.mark.parametrize(
        'tool_tip, expected_hover',
        [
            ('button', 'You hovered over the Button'),
            ('field', 'You hovered over the text field'),
            ('contrary', 'You hovered over the Contrary'),
            ('section', 'You hovered over the 1.10.32')
        ]
    )
    def test_tool_tips(self, tool_tip, expected_hover):
        tool_tips_page = ToolTipsPage(self.driver)
        tool_tips_page.open()
        tool_tip_text = tool_tips_page.check_tool_tips(tool_tip)
        assert tool_tip_text == expected_hover, \
            'Hover missing or incorrect content'

@allure.suite('Widgets')
@allure.feature('Menu Page')
class TestMenuPage:

    @allure.title('Check all of the menu items')
    def test_menu_items(self):
        menu_page = MenuPage(self.driver)
        menu_page.open()
        data = menu_page.check_menu()
        assert data == [
            'Main Item 1', 'Main Item 2', 'Sub Item',
            'Sub Item', 'SUB SUB LIST »', 'Sub Sub Item 1',
            'Sub Sub Item 2', 'Main Item 3'
        ], \
            'Menu items do not exist or have not been selected'


@allure.suite('Widgets')
@allure.feature('Select Menu Page')
class TestSelectMenuPage:

    @allure.title('Check "Select Value" dropdown')
    def test_check_select_value_dropdown(self):
        select_menu_page = SelectMenuPage(self.driver)
        select_menu_page.open()
        option_value, actual_value = select_menu_page.check_dropdown()
        assert option_value == actual_value, \
            "The value in dropdown has not changed"