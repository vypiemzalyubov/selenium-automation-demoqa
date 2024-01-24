import random
import time

from selenium.webdriver.chrome.webdriver import WebDriver
from pages.elements_page import CheckBoxPage, RadioButtonPage, TextBoxPage, WebTablePage


class TestTextBox:

    def test_text_box(self, driver: WebDriver):
        text_box_page = TextBoxPage(driver)
        text_box_page.open("https://demoqa.com/text-box")
        full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
        output_full_name, output_email, output_current_address, output_permanent_address = text_box_page.check_filled_form()
        assert full_name == output_full_name, "The full name does not match"
        assert email == output_email, "The email does not match"
        assert current_address == output_current_address, "The current address does not match"
        assert permanent_address == output_permanent_address, "The permanent address does not match"


class TestCheckBox:

    def test_check_box(self, driver: WebDriver):
        check_box_page = CheckBoxPage(driver)
        check_box_page.open("https://demoqa.com/checkbox")
        check_box_page.open_full_list()
        check_box_page.click_random_checkbox()
        input_checkbox = check_box_page.get_checked_checkboxes()
        output_result = check_box_page.get_output_result()
        assert input_checkbox == output_result, "Checkboxes have not been selected"


class TestRadioButton:

    def test_radio_button(self, driver: WebDriver):
        radio_button_page = RadioButtonPage(driver)
        radio_button_page.open("https://demoqa.com/radio-button")
        radio_button_page.click_on_the_radio_button("yes")
        output_yes = radio_button_page.get_output_result()
        radio_button_page.click_on_the_radio_button("impressive")
        output_impressive = radio_button_page.get_output_result()
        radio_button_page.click_on_the_radio_button("no")
        output_no = radio_button_page.get_output_result()
        assert output_yes == "Yes", "\"Yes\" has not been selected"
        assert output_impressive == "Impressive", "\"Impressive\" has not been selected"
        assert output_no != "No", "\"No\" has been selected, but it should not be"


# class TestWebTable:

#     def test_web_table_person(self, driver: WebDriver):
#         web_table_page = WebTablePage(driver)
#         web_table_page.open("https://demoqa.com/webtables")
#         new_person = web_table_page.add_new_person()
#         table_result = web_table_page.check_new_added_person()
#         assert new_person in table_result

#     def test_web_table_search(self, driver: WebDriver):
#         web_table_page = WebTablePage(driver)
#         web_table_page.open("https://demoqa.com/webtables")
#         key_word = web_table_page.add_new_person()[random.randint(0, 5)]
#         web_table_page.search_some_person(key_word)
#         table_result = web_table_page.check_search_person()
#         assert key_word in table_result, "The person was not found in the table"

#     def test_web_table_update_person_info(self, driver: WebDriver):
#         web_table_page = WebTablePage(driver)
#         web_table_page.open("https://demoqa.com/webtables")
#         lastname = web_table_page.add_new_person()[1]
#         web_table_page.search_some_person(lastname)
#         age = web_table_page.update_person_info()
#         row = web_table_page.check_search_person()
#         assert age in row, "The person card has not been changed"

#     def test_web_table_delete_person(self, driver: WebDriver):
#         web_table_page = WebTablePage(driver)
#         web_table_page.open("https://demoqa.com/webtables")
#         email = web_table_page.add_new_person()[3]
#         web_table_page.search_some_person(email)
#         web_table_page.delete_person()
#         text = web_table_page.check_deleted_person()
#         assert text == 'No rows found'

#     def test_web_table_change_count_row(self, driver: WebDriver):
#         web_table_page = WebTablePage(driver)
#         web_table_page.open("https://demoqa.com/webtables")
#         web_table_page.remove_footer()
#         web_table_page.remove_fixedban()
#         count = web_table_page.select_up_to_some_rows()
#         assert count == [5, 10, 20, 50, 100], "The number of rows in the table has not been changed or has not been chahged incorrectly"
