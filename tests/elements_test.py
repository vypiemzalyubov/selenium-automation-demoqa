import random

import pytest

from pages.elements_page import ButtonsPage, CheckBoxPage, DynamicPropertiesPage, LinksPage, RadioButtonPage, TextBoxPage, UploadAndDownloadPage, WebTablePage


class TestTextBox:

    def test_text_box(self):
        text_box_page = TextBoxPage(self.driver, "https://demoqa.com/text-box")
        text_box_page.open()
        full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
        output_full_name, output_email, output_current_address, output_permanent_address = text_box_page.check_filled_form()
        assert full_name == output_full_name, \
            "The full name does not match"
        assert email == output_email, \
            "The email does not match"
        assert current_address == output_current_address, \
            "The current address does not match"
        assert permanent_address == output_permanent_address, \
            "The permanent address does not match"


class TestCheckBox:

    def test_check_box(self):
        check_box_page = CheckBoxPage(self.driver, "https://demoqa.com/checkbox")
        check_box_page.open()
        check_box_page.open_full_list()
        check_box_page.click_random_checkbox()
        input_checkbox = check_box_page.get_checked_checkboxes()
        output_result = check_box_page.get_output_result()
        assert input_checkbox == output_result, \
            "Checkboxes have not been selected"


class TestRadioButton:

    def test_yes_radio_button(self):
        radio_button_page = RadioButtonPage(self.driver, "https://demoqa.com/radio-button")
        radio_button_page.open()
        radio_button_page.click_on_the_radio_button("yes")
        output_yes = radio_button_page.get_output_result()
        assert output_yes == "Yes", \
            "The radio button 'Yes' has not been selected"

    def test_impressive_radio_button(self):
        radio_button_page = RadioButtonPage(self.driver, "https://demoqa.com/radio-button")
        radio_button_page.open()
        radio_button_page.click_on_the_radio_button("impressive")
        output_impressive = radio_button_page.get_output_result()
        assert output_impressive == "Impressive", \
            "The radio button 'Impressive' has not been selected"

    @pytest.mark.xfail(reason="BUG-01: The radio button 'No' has not been selected")
    def test_no_radio_button(self):
        radio_button_page = RadioButtonPage(self.driver, "https://demoqa.com/radio-button")
        radio_button_page.open()
        radio_button_page.click_on_the_radio_button("no")
        output_no = radio_button_page.get_output_result()
        assert output_no == "No", \
            "The radio button 'No' has not been selected"

class TestWebTable:

    def test_web_table_person(self):
        web_table_page = WebTablePage(self.driver, "https://demoqa.com/webtables")
        web_table_page.open()
        new_person = web_table_page.add_new_person()
        table_result = web_table_page.check_new_added_person()
        assert new_person in table_result, \
            "The resulting table differs from the expected table"

    def test_web_table_search(self):
        web_table_page = WebTablePage(self.driver, "https://demoqa.com/webtables")
        web_table_page.open()
        key_word = web_table_page.add_new_person()[random.randint(0, 5)]
        web_table_page.search_some_person(key_word)
        table_result = web_table_page.check_search_person()
        assert key_word in table_result, \
            "The person was not found in the table"

    def test_web_table_update_person_info(self):
        web_table_page = WebTablePage(self.driver, "https://demoqa.com/webtables")
        web_table_page.open()
        lastname = web_table_page.add_new_person()[1]
        web_table_page.search_some_person(lastname)
        age = web_table_page.update_person_info()
        row = web_table_page.check_search_person()
        assert age in row, \
            "The person card has not been changed"

    def test_web_table_delete_person(self):
        web_table_page = WebTablePage(self.driver, "https://demoqa.com/webtables")
        web_table_page.open()
        email = web_table_page.add_new_person()[3]
        web_table_page.search_some_person(email)
        web_table_page.delete_person()
        text = web_table_page.check_deleted_person()
        assert text == "No rows found", \
            "The person card has not been deleted"

    def test_web_table_change_count_row(self):
        web_table_page = WebTablePage(self.driver, "https://demoqa.com/webtables")
        web_table_page.open()
        count = web_table_page.select_rows_count()
        assert count == [5, 10, 20, 50, 100], \
            "The number of rows in the table has not been changed or has not been changed incorrectly"


class TestButtonPage:

    def test_click_on_the_double_click_button(self):
        button_page = ButtonsPage(self.driver, "https://demoqa.com/buttons")
        button_page.open()
        double = button_page.click_on_different_button("double")
        assert double == "You have done a double click", \
            "The double click button was not pressed"

    def test_click_on_the_right_click_button(self):
        button_page = ButtonsPage(self.driver, "https://demoqa.com/buttons")
        button_page.open()
        right = button_page.click_on_different_button("right")
        assert right == "You have done a right click", \
            "The right click button was not pressed"

    def test_click_on_the_click_button(self):
        button_page = ButtonsPage(self.driver, "https://demoqa.com/buttons")
        button_page.open()
        click = button_page.click_on_different_button("click")
        assert click == "You have done a dynamic click", \
            "The dynamic click button was not pressed"


class TestLinksPage:

    @pytest.mark.parametrize("link_locator",
                             ["SIMPLE_LINK", "DYNAMIC_LINK"])
    def test_check_new_tab_link(self, link_locator):
        links_page = LinksPage(self.driver, "https://demoqa.com/links")
        links_page.open()
        link_href, current_url = links_page.check_new_tab_link(link_locator)
        assert link_href == current_url, \
            f"The link is broken or url incorrect. Expected: {link_href}. Actual: {current_url}"

    @pytest.mark.parametrize("link_locator",
                             ["CREATED", "NO_CONTENT", "MOVED",
                              "BAD_REQUEST", "UNAUTHORIZED", "FORBIDDEN", "NOT_FOUND"])
    def test_check_broken_link(self, link_locator):
        links_page = LinksPage(self.driver, "https://demoqa.com/links")
        links_page.open()
        response_text = links_page.check_broken_link(link_locator)
        expected_word = link_locator.replace("_", " ").title()
        assert expected_word in response_text, \
            f"The expected word is missing from the response field. Expected: {expected_word}. Actual: {response_text}"
        

class TestUploadAndDownload:

    def test_upload_file(self):
        upload_download_page = UploadAndDownloadPage(self.driver, "https://demoqa.com/upload-download")
        upload_download_page.open()
        upload_download_page.upload_file()
        file_name, uploaded_text = upload_download_page.upload_file()
        assert file_name == uploaded_text, \
            "The file has not been uploaded"

    def test_download_file(self):
        upload_download_page = UploadAndDownloadPage(self.driver, "https://demoqa.com/upload-download")
        upload_download_page.open()
        check_file_exists = upload_download_page.download_file()
        assert check_file_exists is True, \
            "The file has not been downloaded"
        

class TestDynamicPropertiesPage:

    def test_enable_button(self):
        dynamic_properties_page = DynamicPropertiesPage(self.driver, "https://demoqa.com/dynamic-properties")
        dynamic_properties_page.open()
        enable = dynamic_properties_page.check_enable_button()
        assert enable is True, \
            "Button did not enable after 5 seconds"

    def test_change_color_button(self):
        dynamic_properties_page = DynamicPropertiesPage(self.driver, "https://demoqa.com/dynamic-properties")
        dynamic_properties_page.open()
        color_before, color_after = dynamic_properties_page.check_changed_of_color()
        assert color_before != color_after, \
            "Color have not been changed"

    def test_appear_button(self):
        dynamic_properties_page = DynamicPropertiesPage(self.driver, "https://demoqa.com/dynamic-properties")
        dynamic_properties_page.open()
        appear = dynamic_properties_page.check_appear_of_button()
        assert appear is True, \
            "Button did not appear after 5 seconds"