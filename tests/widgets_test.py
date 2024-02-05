import time

import allure

from pages.widgets_page import (
    AccordianPage, 
    AutoCompletePage, 
    DatePickerPage, 
    SliderPage, 
    ProgressBarPage, 
    TabsPage,
    ToolTipsPage, 
    MenuPage
)


@allure.suite("Widgets")
@allure.feature("Accordian Page")
class TestAccordianPage:

    @allure.title("Check accordian widget")
    def test_accordian(self):
        accordian_page = AccordianPage(self.driver)
        accordian_page.open()
        first_title, first_content = accordian_page.check_accordian("first")
        second_title, second_content = accordian_page.check_accordian("second")
        third_title, third_content = accordian_page.check_accordian("third")
        assert first_title == "What is Lorem Ipsum?" and first_content > 0, \
            "Incorrect title or missing text for first accordian"
        assert second_title == "Where does it come from?" and second_content > 0, \
            "Incorrect title or missing text for second accordian"
        assert third_title == "Why do we use it?" and third_content > 0, \
            "Incorrect title or missing text for third accordian"


@allure.suite("Widgets")
@allure.feature("Autocomplete page")
class TestAutoCompletePage:

    @allure.title("Check the autocomplete is filled")
    def test_fill_multi_autocomplete(self):
        autocomplete_page = AutoCompletePage(self.driver)
        autocomplete_page.open()
        colors = autocomplete_page.fill_input_multi()
        colors_result = autocomplete_page.check_color_in_multi()
        assert colors == colors_result, \
            "The added color is missing in the input"

    @allure.title("Check deletions from the multi autocomplete")
    def test_remove_value_from_multi(self):
        autocomplete_page = AutoCompletePage(self.driver)
        autocomplete_page.open()
        autocomplete_page.fill_input_multi()
        count_value_before, count_value_after = autocomplete_page.remove_value_from_multi()
        assert count_value_before != count_value_after, \
            "Value was not deleted"

    @allure.title("Check deletions from the multi autocomplete by cross")
    def test_remove_all_values_from_multi_by_cross(self):
        autocomplete_page = AutoCompletePage(self.driver)
        autocomplete_page.open()
        autocomplete_page.fill_input_multi()
        count_value = autocomplete_page.remove_all_values_from_multi()
        assert count_value == 0, \
            "Not all values have been deleted"

    @allure.title("Check deletions from the single autocomplete")
    def test_fill_single_autocomplete(self):
        autocomplete_page = AutoCompletePage(self.driver)
        autocomplete_page.open()
        color = autocomplete_page.fill_input_single()
        color_result = autocomplete_page.check_color_in_single()
        assert color == color_result, \
            "The added colors are missing in the input"


@allure.suite("Widgets")
@allure.feature("Date Picker Page")
class TestDatePickerPage:
        
    @allure.title("Check change date")
    def test_change_date(self):
        date_picker_page = DatePickerPage(self.driver)
        date_picker_page.open()
        value_date_before, value_date_after = date_picker_page.select_date()
        assert value_date_before != value_date_after, \
            "The date has not been changed"

    @allure.title("Check change date and time")
    def test_change_date_and_time(self):
        date_picker_page = DatePickerPage(self.driver)
        date_picker_page.open()
        value_date_before, value_date_after = date_picker_page.select_date_and_time()
        assert value_date_before != value_date_after, \
            "The date and time have not been changed"


@allure.suite("Widgets")
@allure.feature("Slider Page")
class TestSliderPage:
    
    @allure.title("Check moved slider")
    def test_slider(self):
        slider = SliderPage(self.driver)
        slider.open()
        before, after = slider.change_slider_value()
        assert before != after, \
            "The slider value has not been changed"


# @allure.suite("Widgets")
# @allure.feature("Progress Bar Page")
# class TestProgressBarPage:
#     @allure.title("Check changed progress bar")
#     def test_progress_bar(self):
#         progress_bar = ProgressBarPage(self.driver, "https://demoqa.com/progress-bar")
#         progress_bar.open()
#         before, after = progress_bar.change_progress_bar_value()
#         assert before != after, \
#             "The progress bar value has not been changed"


# @allure.suite("Widgets")
# @allure.feature("Test Tabs Page")
# class TestTabsPage:
#     @allure.title("Check switched tabs")
#     def test_tabs(self):
#         tabs = TabsPage(self.driver, "https://demoqa.com/tabs")
#         tabs.open()
#         what_button, what_content = tabs.check_tabs("what")
#         origin_button, origin_content = tabs.check_tabs("origin")
#         use_button, use_content = tabs.check_tabs("use")
#         more_button, more_content = tabs.check_tabs("more")
#         assert what_button == "What" and what_content != 0, \
#             "The tab 'what' was not pressed or the text is missing"
#         assert origin_button == "Origin" and origin_content != 0, \
#             "The tab 'origin' was not pressed or the text is missing"
#         assert use_button == "Use" and use_content != 0, \
#             "The tab 'use' was not pressed or the text is missing"
#         assert more_button == "More" and what_content != 0, \
#             "The tab 'more' was not pressed or the text is missing"


# @allure.suite("Widgets")
# @allure.feature("Tool Tips")
# class TestToolTips:
#     @allure.title("Check tool tips ")
#     def test_tool_tips(self):
#         tool_tips_page = ToolTipsPage(self.driver, "https://demoqa.com/tool-tips")
#         tool_tips_page.open()
#         button_text, field_text, contrary_text, section_text = tool_tips_page.check_tool_tips()
#         assert button_text == "You hovered over the Button", "hover missing or incorrect content"
#         assert field_text == "You hovered over the text field", "hover missing or incorrect content"
#         assert contrary_text == "You hovered over the Contrary", "hover missing or incorrect content"
#         assert section_text == "You hovered over the 1.10.32", "hover missing or incorrect content"


# @allure.suite("Widgets")
# @allure.feature("Menu Page")
# class TestMenuPage:
#     @allure.title("Check all of the menu items")
#     def test_menu_items(self):
#         menu_page = MenuPage(self.driver, "https://demoqa.com/menu")
#         menu_page.open()
#         data = menu_page.check_menu()
#         assert data == ["Main Item 1", "Main Item 2", "Sub Item", "Sub Item", "SUB SUB LIST »", "Sub Sub Item 1",
#                         "Sub Sub Item 2", "Main Item 3"], "menu items do not exist or have not been selected"