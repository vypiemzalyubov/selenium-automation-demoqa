import base64
import os
import random

import allure
import requests

from selenium.common.exceptions import TimeoutException
from locators.elements_page_locators import (
    ButtonsPageLocators,
    CheckBoxPageLocators,
    DynamicPropertiesPageLocators,
    LinksPageLocators,
    RadioButtonPageLocators,
    TextBoxPageLocators,
    UploadAndDownloadPageLocators,
    WebTablePageLocators
) 
from pages.base_page import BasePage
from utils.generator import generated_file, generated_person


class TextBoxPage(BasePage):

    locators = TextBoxPageLocators()

    @allure.step("Fill in all fields")
    def fill_all_fields(self):
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address
        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.element_is_visible(self.locators.SUBMIT).click()
        return full_name, email, current_address, permanent_address

    @allure.step("Check filled form")
    def check_filled_form(self):
        full_name = self.element_is_present(self.locators.CREATED_FULLNAME).text.split(":")[1]
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(":")[1]
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(":")[1]
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADSRESS).text.split(":")[1]
        return full_name, email, current_address, permanent_address


class CheckBoxPage(BasePage):

    locators = CheckBoxPageLocators()

    @allure.step("Open full list")
    def open_full_list(self):
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    @allure.step("Click random items")
    def click_random_checkbox(self):
        item_list = self.elements_are_visible(self.locators.ITEM_LIST)
        count = 21
        while count != 0:
            item = item_list[random.randint(0, 16)]
            self.go_to_element(item)
            item.click()
            count -= 1

    @allure.step("Get checked checkbox")
    def get_checked_checkboxes(self):
        checked_list = self.elements_are_present(self.locators.CHECKED_ITEMS)
        data = [box.find_element("xpath", self.locators.TITLE_ITEM).text for box in checked_list]
        return str(data).replace(" ", "").replace("doc", "").replace(".", "").lower()

    @allure.step("Get output result")
    def get_output_result(self):
        result_list = self.elements_are_present(self.locators.OUTPUT_RESULT)
        data = [item.text for item in result_list]
        return str(data).replace(" ", "").lower()


class RadioButtonPage(BasePage):

    locators = RadioButtonPageLocators()

    @allure.step("Click on the radiobutton")
    def click_on_the_radio_button(self, choice):
        choices = {
            "yes": self.locators.YES_RADIOBUTTON,
            "impressive": self.locators.IMPRESSIVE_RADIOBUTTON,
            "no": self.locators.NO_RADIOBUTTON
        }
        self.element_is_visible(choices[choice]).click()

    @allure.step("Get output result")
    def get_output_result(self):
        return self.element_is_present(self.locators.OUTPUT_RESULT).text


class WebTablePage(BasePage):

    locators = WebTablePageLocators()

    @allure.step("Add new person")
    def add_new_person(self):
        count = 1
        while count != 0:
            person_info = next(generated_person())
            firstname = person_info.firstname
            lastname = person_info.lastname
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department
            self.element_is_visible(self.locators.ADD_BUTTON).click()
            self.element_is_visible(self.locators.FIRSTNAME_INPUT).send_keys(firstname)
            self.element_is_visible(self.locators.LASTNAME_INPUT).send_keys(lastname)
            self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(email)
            self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
            self.element_is_visible(self.locators.SALARY_INPUT).send_keys(salary)
            self.element_is_visible(self.locators.DEPARTMENT_INPUT).send_keys(department)
            self.element_is_visible(self.locators.SUBMIT).click()
            count -= 1
        return [firstname, lastname, str(age), email, str(salary), department]

    @allure.step("Check added people")
    def check_new_added_person(self):
        people_list = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        data = [item.text.splitlines() for item in people_list]
        return data

    @allure.step("Find some person")
    def search_some_person(self, key_word):
        self.element_is_visible(self.locators.SEARCH_INPUT).send_keys(key_word)

    @allure.step("Check found person")
    def check_search_person(self):
        delete_button = self.element_is_present(self.locators.DELETE_BUTTON)
        row = delete_button.find_element("xpath", self.locators.ROW_PARENT)
        return row.text.splitlines()

    @allure.step("Update person information")
    def update_person_info(self):
        person_info = next(generated_person())
        age = person_info.age
        self.element_is_visible(self.locators.UPDATE_BUTTON).click()
        self.element_is_visible(self.locators.AGE_INPUT).clear()
        self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
        self.element_is_visible(self.locators.SUBMIT).click()
        return str(age)

    @allure.step("Delete person")
    def delete_person(self):
        self.element_is_visible(self.locators.DELETE_BUTTON).click()

    @allure.step("Check deleted person")
    def check_deleted_person(self):
        return self.element_is_present(self.locators.NO_ROWS_FOUND).text

    @allure.step("Select up to some rows")
    def select_rows_count(self):
        self.remove_footer()
        count = [5, 10, 20, 50, 100]
        data = []
        for x in count:
            count_row_button = self.element_is_visible(self.locators.COUNT_ROW_LIST)
            self.go_to_element(count_row_button)
            count_row_button.click()
            self.element_is_visible(("xpath", f"//option[@value='{x}']")).click()
            data.append(self._check_count_rows())
        return data

    @allure.step("Check count rows")
    def _check_count_rows(self):
        list_rows = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        return len(list_rows)


class ButtonsPage(BasePage):

    locators = ButtonsPageLocators()

    @allure.step("Click on different  buttons")
    def click_on_different_button(self, type_click):
        if type_click == "double":
            self.action_double_click(self.element_is_visible(self.locators.DOUBLE_BUTTON))
            return self.check_clicked_on_the_button(self.locators.SUCCESS_DOUBLE)

        if type_click == "right":
            self.action_right_click(self.element_is_visible(self.locators.RIGHT_CLICK_BUTTON))
            return self.check_clicked_on_the_button(self.locators.SUCCESS_RIGHT)

        if type_click == "click":
            self.element_is_visible(self.locators.CLICK_ME_BUTTON).click()
            return self.check_clicked_on_the_button(self.locators.SUCCESS_CLICK_ME)

    @allure.step("Check clicked button")
    def check_clicked_on_the_button(self, element):
        return self.element_is_present(element).text


class LinksPage(BasePage):

    locators = LinksPageLocators()

    @allure.step("Check simple link")
    def check_new_tab_link(self, link_locator: str):
        locator_name = getattr(self.locators, link_locator)
        new_tab_link = self.element_is_visible(locator_name)
        link_href = new_tab_link.get_attribute('href')
        request = requests.get(link_href)
        if request.status_code == 200:
            new_tab_link.click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            current_url = self.driver.current_url
            return link_href, current_url
        else:
            return link_href, request.status_code

    @allure.step("Check broken link")
    def check_broken_link(self, link_locator: str):
        locator_name = getattr(self.locators, link_locator)
        broken_link = self.element_is_visible(locator_name).click()
        response_field = self.element_is_present(self.locators.RESPONSE_FIELD)
        return response_field.text


class UploadAndDownloadPage(BasePage):

    locators = UploadAndDownloadPageLocators()

    @allure.step("Upload file")
    def upload_file(self):
        file_name, path = generated_file()
        self.element_is_present(self.locators.UPLOAD_FILE).send_keys(path)
        os.remove(path)
        uploaded_text = self.element_is_present(self.locators.UPLOADED_RESULT).text
        return file_name.split('\\')[-1], uploaded_text.split('\\')[-1]

    @allure.step("Download file")
    def download_file(self):
        image_link = self.element_is_present(self.locators.DOWNLOAD_FILE).get_attribute("href")
        link_byte = base64.b64decode(image_link)
        path_name_file = fr"{os.getcwd()}\data\image_file{random.randint(0,999)}.jpg"
        with open(path_name_file, "wb+") as f:
            offset = link_byte.find(b"\xff\xd8")
            f.write(link_byte[offset:])
            check_file_exists = os.path.exists(path_name_file)
            f.close()
        os.remove(path_name_file)
        return check_file_exists


class DynamicPropertiesPage(BasePage):

    locators = DynamicPropertiesPageLocators()

    @allure.step("Check enable button")
    def check_enable_button(self):
        try:
            self.element_is_clickable(self.locators.ENABLE_BUTTON)
        except TimeoutException:
            return False
        return True

    @allure.step("Check changed of color")
    def check_changed_of_color(self):
        color_button_before = self.element_is_present(self.locators.COLOR_CHANGE_BUTTON_BEFORE)
        color_before = color_button_before.value_of_css_property("color")
        color_button_after = self.element_is_present(self.locators.COLOR_CHANGE_BUTTON_AFTER)
        color_after = color_button_after.value_of_css_property("color")
        return color_before, color_after

    @allure.step("Check appear of button")
    def check_appear_of_button(self):
        try:
            self.element_is_visible(self.locators.VISIBLE_AFTER_FIVE_SECONDS_BUTTON)
        except TimeoutException:
            return False
        return True
