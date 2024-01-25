import random
import time

from pages.elements_page import ButtonsPage, CheckBoxPage, RadioButtonPage, TextBoxPage, WebTablePage


class TestTextBox:

    def test_text_box(self):
        text_box_page = TextBoxPage(self.driver, "https://demoqa.com/text-box")
        text_box_page.open()
        full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
        output_full_name, output_email, output_current_address, output_permanent_address = text_box_page.check_filled_form()
        assert full_name == output_full_name, "The full name does not match"
        assert email == output_email, "The email does not match"
        assert current_address == output_current_address, "The current address does not match"
        assert permanent_address == output_permanent_address, "The permanent address does not match"


class TestCheckBox:

    def test_check_box(self):
        check_box_page = CheckBoxPage(self.driver, "https://demoqa.com/checkbox")
        check_box_page.open()
        check_box_page.open_full_list()
        check_box_page.click_random_checkbox()
        input_checkbox = check_box_page.get_checked_checkboxes()
        output_result = check_box_page.get_output_result()
        assert input_checkbox == output_result, "Checkboxes have not been selected"


class TestRadioButton:

    def test_radio_button(self):
        radio_button_page = RadioButtonPage(self.driver, "https://demoqa.com/radio-button")
        radio_button_page.open()
        radio_button_page.click_on_the_radio_button("yes")
        output_yes = radio_button_page.get_output_result()
        radio_button_page.click_on_the_radio_button("impressive")
        output_impressive = radio_button_page.get_output_result()
        radio_button_page.click_on_the_radio_button("no")
        output_no = radio_button_page.get_output_result()
        assert output_yes == "Yes", "\"Yes\" has not been selected"
        assert output_impressive == "Impressive", "\"Impressive\" has not been selected"
        assert output_no != "No", "\"No\" has been selected, but it should not be"


class TestWebTable:

    def test_web_table_person(self):
        web_table_page = WebTablePage(self.driver, "https://demoqa.com/webtables")
        web_table_page.open()
        new_person = web_table_page.add_new_person()
        table_result = web_table_page.check_new_added_person()
        assert new_person in table_result, "The resulting table differs from the expected table"

    def test_web_table_search(self):
        web_table_page = WebTablePage(self.driver, "https://demoqa.com/webtables")
        web_table_page.open()
        key_word = web_table_page.add_new_person()[random.randint(0, 5)]
        time.sleep(5)
        web_table_page.search_some_person(key_word)
        time.sleep(5)
        table_result = web_table_page.check_search_person()
        assert key_word in table_result, "The person was not found in the table"

    def test_web_table_update_person_info(self):
        web_table_page = WebTablePage(self.driver, "https://demoqa.com/webtables")
        web_table_page.open()
        lastname = web_table_page.add_new_person()[1]
        web_table_page.search_some_person(lastname)
        age = web_table_page.update_person_info()
        row = web_table_page.check_search_person()
        assert age in row, "The person card has not been changed"

    def test_web_table_delete_person(self):
        web_table_page = WebTablePage(self.driver, "https://demoqa.com/webtables")
        web_table_page.open()
        email = web_table_page.add_new_person()[3]
        web_table_page.search_some_person(email)
        web_table_page.delete_person()
        text = web_table_page.check_deleted_person()
        assert text == "No rows found", "The person card has not been deleted"

    def test_web_table_change_count_row(self):
        web_table_page = WebTablePage(self.driver, "https://demoqa.com/webtables")
        web_table_page.open()
        count = web_table_page.select_rows_count()
        assert count == [5, 10, 20, 50, 100], "The number of rows in the table has not been changed or has not been chahged incorrectly"


class TestButtonPage:

    def test_different_click_on_the_buttons(self):
        button_page = ButtonsPage(self.driver, "https://demoqa.com/buttons")
        button_page.open()
        double = button_page.click_on_different_button("double")
        right = button_page.click_on_different_button("right")
        click = button_page.click_on_different_button("click")
        assert double == "You have done a double click", "The double click button was not pressed"
        assert right == "You have done a right click", "The right click button was not pressed"
        assert click == "Click Me", "The dynamic click button was not pressed"