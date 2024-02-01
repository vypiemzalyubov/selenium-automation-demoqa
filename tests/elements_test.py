import random

import allure
import pytest

from pages.elements_page import (
    ButtonsPage,
    CheckBoxPage,
    DynamicPropertiesPage,
    LinksPage,
    RadioButtonPage,
    TextBoxPage,
    UploadAndDownloadPage,
    WebTablePage
)


@allure.suite("Elements")
@allure.feature("Text Box Page")
class TestTextBox:

    @allure.title("Check TextBox")
    def test_text_box(self):
        text_box_page = TextBoxPage(self.driver)
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


@allure.suite("Elements")
@allure.feature("Check Box Page")
class TestCheckBox:

    @allure.title("Check CheckBox")
    def test_check_box(self):
        check_box_page = CheckBoxPage(self.driver)
        check_box_page.open()
        check_box_page.open_full_list()
        check_box_page.click_random_checkbox()
        input_checkbox = check_box_page.get_checked_checkboxes()
        output_result = check_box_page.get_output_result()
        assert input_checkbox == output_result, \
            "Checkboxes have not been selected"


@allure.suite("Elements")
@allure.feature("Radio Button Page")
class TestRadioButton:

    @allure.title("Check 'Yes' radio button")
    def test_yes_radio_button(self):
        radio_button_page = RadioButtonPage(self.driver)
        radio_button_page.open()
        radio_button_page.click_on_the_radio_button("yes")
        output_yes = radio_button_page.get_output_result()
        assert output_yes == "Yes", \
            "The radio button 'Yes' has not been selected"

    @allure.title("Check 'Impressive' radio button")
    def test_impressive_radio_button(self):
        radio_button_page = RadioButtonPage(self.driver)
        radio_button_page.open()
        radio_button_page.click_on_the_radio_button("impressive")
        output_impressive = radio_button_page.get_output_result()
        assert output_impressive == "Impressive", \
            "The radio button 'Impressive' has not been selected"

    @allure.title("Check 'No' radio button")
    @pytest.mark.xfail(reason="BUG-01: The radio button 'No' has not been selected")
    def test_no_radio_button(self):
        radio_button_page = RadioButtonPage(self.driver)
        radio_button_page.open()
        radio_button_page.click_on_the_radio_button("no")
        output_no = radio_button_page.get_output_result()
        assert output_no == "No", \
            "The radio button 'No' has not been selected"


@allure.suite("Elements")
@allure.feature("Web Tables Page")
class TestWebTable:

    @allure.title("Сheck to add a person to the table")
    def test_web_table_person(self):
        web_table_page = WebTablePage(self.driver)
        web_table_page.open()
        new_person = web_table_page.add_new_person()
        table_result = web_table_page.check_new_added_person()
        assert new_person in table_result, \
            "The resulting table differs from the expected table"

    @allure.title("Check human search in table")
    def test_web_table_search(self):
        web_table_page = WebTablePage(self.driver)
        web_table_page.open()
        key_word = web_table_page.add_new_person()[random.randint(0, 5)]
        web_table_page.search_some_person(key_word)
        table_result = web_table_page.check_search_person()
        assert key_word in table_result, \
            "The person was not found in the table"

    @allure.title("Checking to update the persons info in the table")
    def test_web_table_update_person_info(self):
        web_table_page = WebTablePage(self.driver)
        web_table_page.open()
        lastname = web_table_page.add_new_person()[1]
        web_table_page.search_some_person(lastname)
        age = web_table_page.update_person_info()
        row = web_table_page.check_search_person()
        assert age in row, \
            "The person card has not been changed"

    @allure.title("Checking to remove a person from the table")
    def test_web_table_delete_person(self):
        web_table_page = WebTablePage(self.driver)
        web_table_page.open()
        email = web_table_page.add_new_person()[3]
        web_table_page.search_some_person(email)
        web_table_page.delete_person()
        text = web_table_page.check_deleted_person()
        assert text == "No rows found", \
            "The person card has not been deleted"

    @allure.title("Check the change in the number of rows in the table")
    def test_web_table_change_count_row(self):
        web_table_page = WebTablePage(self.driver)
        web_table_page.open()
        count = web_table_page.select_rows_count()
        assert count == [5, 10, 20, 50, 100], \
            "The number of rows in the table has not been changed or has not been changed incorrectly"


@allure.suite("Elements")
@allure.feature("Buttons Page")
class TestButtonPage:

    @allure.title("Checking double click")
    def test_click_on_the_double_click_button(self):
        button_page = ButtonsPage(self.driver)
        button_page.open()
        double = button_page.click_on_different_button("double")
        assert double == "You have done a double click", \
            "The double click button was not pressed"

    @allure.title("Checking right click")
    def test_click_on_the_right_click_button(self):
        button_page = ButtonsPage(self.driver)
        button_page.open()
        right = button_page.click_on_different_button("right")
        assert right == "You have done a right click", \
            "The right click button was not pressed"

    @allure.title("Checking a click")
    def test_click_on_the_click_button(self):
        button_page = ButtonsPage(self.driver)
        button_page.open()
        click = button_page.click_on_different_button("click")
        assert click == "You have done a dynamic click", \
            "The dynamic click button was not pressed"


@allure.suite("Elements")
@allure.feature("Links Page")
class TestLinksPage:

    @allure.title("Checking the link for a new tab")
    @pytest.mark.parametrize(
        "locator_name",
        ["SIMPLE_LINK", "DYNAMIC_LINK"]
    )
    def test_check_new_tab_link(self, locator_name):
        links_page = LinksPage(self.driver)
        links_page.open()
        link_href, current_url = links_page.check_new_tab_link(locator_name)
        assert link_href == current_url, \
            f"The link is broken or url incorrect. Expected: {link_href}. Actual: {current_url}"

    @allure.title("Checking a broken link")
    @pytest.mark.parametrize(
        "locator_name",
        ["CREATED", "NO_CONTENT", "MOVED", "BAD_REQUEST", "UNAUTHORIZED", "FORBIDDEN", "NOT_FOUND"]
    )
    def test_check_broken_link(self, locator_name):
        links_page = LinksPage(self.driver)
        links_page.open()
        response_text = links_page.check_broken_link(locator_name)
        expected_word = locator_name.replace("_", " ").title()
        assert expected_word in response_text, \
            f"The expected word is missing from the response field. Expected: {expected_word}. Actual: {response_text}"


@allure.suite("Elements")
@allure.feature("Upload and Download Page")
class TestUploadAndDownload:

    @allure.title("Check upload file")
    def test_upload_file(self):
        upload_download_page = UploadAndDownloadPage(self.driver)
        upload_download_page.open()
        upload_download_page.upload_file()
        file_name, uploaded_text = upload_download_page.upload_file()
        assert file_name == uploaded_text, \
            "The file has not been uploaded"

    @allure.title("Check download file")
    def test_download_file(self):
        upload_download_page = UploadAndDownloadPage(self.driver)
        upload_download_page.open()
        check_file_exists = upload_download_page.download_file()
        assert check_file_exists is True, \
            "The file has not been downloaded"


@allure.suite("Elements")
@allure.feature("Dynamic Properties Page")
class TestDynamicPropertiesPage:

    @allure.title("Check enable button")
    def test_enable_button(self):
        dynamic_properties_page = DynamicPropertiesPage(self.driver)
        dynamic_properties_page.open()
        enable = dynamic_properties_page.check_enable_button()
        assert enable is True, \
            "Button did not enable after 5 seconds"

    @allure.title("Check change color button")
    def test_change_color_button(self):
        dynamic_properties_page = DynamicPropertiesPage(self.driver)
        dynamic_properties_page.open()
        color_before, color_after = dynamic_properties_page.check_changed_of_color()
        assert color_before != color_after, \
            "Color have not been changed"

    @allure.title("Check appear button")
    def test_appear_button(self):
        dynamic_properties_page = DynamicPropertiesPage(self.driver)
        dynamic_properties_page.open()
        appear = dynamic_properties_page.check_appear_of_button()
        assert appear is True, \
            "Button did not appear after 5 seconds"
