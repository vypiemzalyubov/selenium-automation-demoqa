import base64
import os
import random
from typing import Any

import allure
import requests
from pydantic import EmailStr
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utils.generator import generated_file, generated_person
from utils.routes import UIRoutes


class TextBoxPage(BasePage):
    # form fields
    FULL_NAME = (By.CSS_SELECTOR, 'input[id="userName"]')
    EMAIL = (By.CSS_SELECTOR, 'input[id="userEmail"]')
    CURRENT_ADDRESS = (By.CSS_SELECTOR, 'textarea[id="currentAddress"]')
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, 'textarea[id="permanentAddress"]')
    SUBMIT = (By.CSS_SELECTOR, 'button[id="submit"]')
    
    # created form
    CREATED_FULLNAME = (By.CSS_SELECTOR, '#output #name')
    CREATED_EMAIL = (By.CSS_SELECTOR, '#output #email')
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, '#output #currentAddress')
    CREATED_PERMANENT_ADSRESS = (By.CSS_SELECTOR, '#output #permanentAddress')

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver, page=UIRoutes.TEXT_BOX)

    @allure.step('Fill in all fields')
    def fill_all_fields(self) -> tuple[str | None, EmailStr | None, str | None, str | None]:
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address
        self.element_is_visible(self.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.EMAIL).send_keys(email)
        self.element_is_visible(self.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.element_is_visible(self.SUBMIT).click()
        return full_name, email, current_address, permanent_address

    @allure.step('Check filled form')
    def check_filled_form(self) -> tuple[str, str, str, str]:
        full_name = self.element_is_present(self.CREATED_FULLNAME).text.split(':')[1]
        email = self.element_is_present(self.CREATED_EMAIL).text.split(':')[1]
        current_address = self.element_is_present(self.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_present(self.CREATED_PERMANENT_ADSRESS).text.split(':')[1]
        return full_name, email, current_address, permanent_address


class CheckBoxPage(BasePage):
    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, 'button[title="Expand all"]')
    ITEM_LIST = (By.CSS_SELECTOR, 'span[class="rct-title"]')
    CHECKED_ITEMS = (By.CSS_SELECTOR, 'svg[class="rct-icon rct-icon-check"]')
    TITLE_ITEM = './/ancestor::span[@class="rct-text"]'
    OUTPUT_RESULT = (By.CSS_SELECTOR, 'span[class="text-success"]')

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver, page=UIRoutes.CHECKBOX)

    @allure.step('Open full list')
    def open_full_list(self) -> None:
        self.element_is_visible(self.EXPAND_ALL_BUTTON).click()

    @allure.step('Click random items')
    def click_random_checkbox(self) -> None:
        item_list = self.elements_are_visible(self.ITEM_LIST)
        count = 21
        while count != 0:
            item = item_list[random.randint(0, 16)]
            self.go_to_element(item)
            item.click()
            count -= 1

    @allure.step('Get checked checkbox')
    def get_checked_checkboxes(self) -> str:
        checked_list = self.elements_are_present(self.CHECKED_ITEMS)
        data = [box.find_element('xpath', self.TITLE_ITEM).text for box in checked_list]
        return str(data).replace(' ', '').replace('doc', '').replace('.', '').lower()

    @allure.step('Get output result')
    def get_output_result(self) -> str:
        result_list = self.elements_are_present(self.OUTPUT_RESULT)
        data = [item.text for item in result_list]
        return str(data).replace(' ', '').lower()


class RadioButtonPage(BasePage):
    YES_RADIOBUTTON = (By.CSS_SELECTOR, 'label[class^="custom-control"][for="yesRadio"]')
    IMPRESSIVE_RADIOBUTTON = (
        By.CSS_SELECTOR,
        'label[class^="custom-control"][for="impressiveRadio"]',
    )
    NO_RADIOBUTTON = (By.CSS_SELECTOR, 'label[class^="custom-control"][for="noRadio"]')
    OUTPUT_RESULT = (By.CSS_SELECTOR, 'p span[class="text-success"]')

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver, page=UIRoutes.RADIO_BUTTON)

    @allure.step('Click on the radiobutton')
    def click_on_the_radio_button(self, choice) -> None:
        choices = {
            'yes': self.YES_RADIOBUTTON,
            'impressive': self.IMPRESSIVE_RADIOBUTTON,
            'no': self.NO_RADIOBUTTON,
        }
        self.element_is_visible(choices[choice]).click()

    @allure.step('Get output result')
    def get_output_result(self) -> str:
        return self.element_is_present(self.OUTPUT_RESULT).text


class WebTablePage(BasePage):
    # add person form
    ADD_BUTTON = (By.CSS_SELECTOR, 'button[id="addNewRecordButton"]')
    FIRSTNAME_INPUT = (By.CSS_SELECTOR, 'input[id="firstName"]')
    LASTNAME_INPUT = (By.CSS_SELECTOR, 'input[id="lastName"]')
    EMAIL_INPUT = (By.CSS_SELECTOR, 'input[id="userEmail"]')
    AGE_INPUT = (By.CSS_SELECTOR, 'input[id="age"]')
    SALARY_INPUT = (By.CSS_SELECTOR, 'input[id="salary"]')
    DEPARTMENT_INPUT = (By.CSS_SELECTOR, 'input[id="department"]')
    SUBMIT = (By.CSS_SELECTOR, 'button[id="submit"]')

    # table
    FULL_PEOPLE_LIST = (By.CSS_SELECTOR, 'div[class="rt-tr-group"]')
    SEARCH_INPUT = (By.CSS_SELECTOR, 'input[id="searchBox"]')
    DELETE_BUTTON = (By.CSS_SELECTOR, 'span[title="Delete"]')
    ROW_PARENT = './/ancestor::div[@class="rt-tr-group"]'
    NO_ROWS_FOUND = (By.CSS_SELECTOR, 'div[class="rt-noData"]')
    COUNT_ROW_LIST = (By.CSS_SELECTOR, 'select[aria-label="rows per page"]')

    # update
    UPDATE_BUTTON = (By.CSS_SELECTOR, 'span[title="Edit"]')

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver, page=UIRoutes.WEB_TABLES)

    @allure.step('Add new person')
    def add_new_person(self) -> list[str]:
        count = 1
        while count != 0:
            person_info = next(generated_person())
            firstname = person_info.firstname
            lastname = person_info.lastname
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department
            self.element_is_visible(self.ADD_BUTTON).click()
            self.element_is_visible(self.FIRSTNAME_INPUT).send_keys(firstname)
            self.element_is_visible(self.LASTNAME_INPUT).send_keys(lastname)
            self.element_is_visible(self.EMAIL_INPUT).send_keys(email)
            self.element_is_visible(self.AGE_INPUT).send_keys(age)
            self.element_is_visible(self.SALARY_INPUT).send_keys(salary)
            self.element_is_visible(self.DEPARTMENT_INPUT).send_keys(department)
            self.element_is_visible(self.SUBMIT).click()
            count -= 1
        return [firstname, lastname, str(age), email, str(salary), department]

    @allure.step('Check added people')
    def check_new_added_person(self) -> list[list[str]]:
        people_list = self.elements_are_present(self.FULL_PEOPLE_LIST)
        data = [item.text.splitlines() for item in people_list]
        return data

    @allure.step('Find some person')
    def search_some_person(self, key_word) -> None:
        self.element_is_visible(self.SEARCH_INPUT).send_keys(key_word)

    @allure.step('Check found person')
    def check_search_person(self) -> list[str]:
        delete_button = self.element_is_present(self.DELETE_BUTTON)
        row = delete_button.find_element('xpath', self.ROW_PARENT)
        return row.text.splitlines()

    @allure.step('Update person information')
    def update_person_info(self) -> str:
        person_info = next(generated_person())
        age = person_info.age
        self.element_is_visible(self.UPDATE_BUTTON).click()
        self.element_is_visible(self.AGE_INPUT).clear()
        self.element_is_visible(self.AGE_INPUT).send_keys(age)
        self.element_is_visible(self.SUBMIT).click()
        return str(age)

    @allure.step('Delete person')
    def delete_person(self) -> None:
        self.element_is_visible(self.DELETE_BUTTON).click()

    @allure.step('Check deleted person')
    def check_deleted_person(self) -> str:
        return self.element_is_present(self.NO_ROWS_FOUND).text

    @allure.step('Select up to some rows')
    def select_rows_count(self) -> list[str]:
        self.remove_footer()
        count = [5, 10, 20, 50, 100]
        data = []
        for x in count:
            count_row_button = self.element_is_visible(self.COUNT_ROW_LIST)
            self.go_to_element(count_row_button)
            count_row_button.click()
            self.element_is_visible(('xpath', f'//option[@value="{x}"]')).click()
            data.append(self._check_count_rows())
        return data

    @allure.step('Check count rows')
    def _check_count_rows(self) -> int:
        list_rows = self.elements_are_present(self.FULL_PEOPLE_LIST)
        return len(list_rows)


class ButtonsPage(BasePage):
    DOUBLE_BUTTON = (By.XPATH, '//button[text()="Double Click Me"]')
    RIGHT_CLICK_BUTTON = (By.XPATH, '//button[text()="Right Click Me"]')
    CLICK_ME_BUTTON = (By.XPATH, '//button[text()="Click Me"]')

    # result
    SUCCESS_DOUBLE = (By.XPATH, '//p[@id="doubleClickMessage"]')
    SUCCESS_RIGHT = (By.XPATH, '//p[@id="rightClickMessage"]')
    SUCCESS_CLICK_ME = (By.XPATH, '//p[@id="dynamicClickMessage"]')

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver, page=UIRoutes.BUTTONS)

    @allure.step('Click on different buttons')
    def click_on_different_button(self, type_click) -> str | None:
        if type_click == 'double':
            self.action_double_click(self.element_is_visible(self.DOUBLE_BUTTON))
            return self.check_clicked_on_the_button(self.SUCCESS_DOUBLE)

        if type_click == 'right':
            self.action_right_click(self.element_is_visible(self.RIGHT_CLICK_BUTTON))
            return self.check_clicked_on_the_button(self.SUCCESS_RIGHT)

        if type_click == 'click':
            self.element_is_visible(self.CLICK_ME_BUTTON).click()
            return self.check_clicked_on_the_button(self.SUCCESS_CLICK_ME)

    @allure.step('Check clicked button')
    def check_clicked_on_the_button(self, element) -> str:
        return self.element_is_present(element).text


class LinksPage(BasePage):
    # new tab
    SIMPLE_LINK = (By.XPATH, '//a[@id="simpleLink"]')
    DYNAMIC_LINK = (By.XPATH, '//a[@id="dynamicLink"]')

    # 4xx
    CREATED = (By.XPATH, '//a[@id="created"]')
    NO_CONTENT = (By.XPATH, '//a[@id="no-content"]')
    MOVED = (By.XPATH, '//a[@id="moved"]')
    BAD_REQUEST = (By.XPATH, '//a[@id="bad-request"]')
    UNAUTHORIZED = (By.XPATH, '//a[@id="unauthorized"]')
    FORBIDDEN = (By.XPATH, '//a[@id="forbidden"]')
    NOT_FOUND = (By.XPATH, '//a[@id="invalid-url"]')

    # response field
    RESPONSE_FIELD = (By.XPATH, '//p[@id="linkResponse"]')

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver, page=UIRoutes.LINKS)

    @allure.step('Check simple link')
    def check_new_tab_link(
        self, locator_name: str
    ) -> tuple[str | None, str] | tuple[str | None, int]:
        locator = getattr(self, locator_name)
        new_tab_link = self.element_is_visible(locator)
        link_href = new_tab_link.get_attribute('href')
        request = requests.get(link_href)
        if request.status_code == 200:
            new_tab_link.click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            current_url = self.driver.current_url
            return link_href, current_url
        else:
            return link_href, request.status_code

    @allure.step('Check broken link')
    def check_broken_link(self, locator_name: str) -> str:
        locator = getattr(self, locator_name)
        self.element_is_visible(locator).click()
        response_field = self.element_is_present(self.RESPONSE_FIELD)
        return response_field.text


class UploadAndDownloadPage(BasePage):
    UPLOAD_FILE = (By.CSS_SELECTOR, 'input[id="uploadFile"]')
    UPLOADED_RESULT = (By.CSS_SELECTOR, 'p[id="uploadedFilePath"]')
    DOWNLOAD_FILE = (By.CSS_SELECTOR, 'a[id="downloadButton"]')

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver, page=UIRoutes.UPLOAD_DOWNLOAD)

    @allure.step('Upload file')
    def upload_file(self) -> tuple[str | Any, str]:
        file_name, path = generated_file()
        self.element_is_present(self.UPLOAD_FILE).send_keys(path)
        os.remove(path)
        uploaded_text = self.element_is_present(self.UPLOADED_RESULT).text
        return file_name.split('\\')[-1], uploaded_text.split('\\')[-1]

    @allure.step('Download file')
    def download_file(self) -> bool:
        image_link = self.element_is_present(self.DOWNLOAD_FILE).get_attribute('href')
        link_byte = base64.b64decode(image_link)
        path_name_file = rf'{os.getcwd()}\utils\image_file{random.randint(0, 999)}.jpg'
        with open(path_name_file, 'wb+') as f:
            offset = link_byte.find(b'\xff\xd8')
            f.write(link_byte[offset:])
            check_file_exists = os.path.exists(path_name_file)
            f.close()
        os.remove(path_name_file)
        return check_file_exists


class DynamicPropertiesPage(BasePage):
    COLOR_CHANGE_BUTTON_BEFORE = (By.CSS_SELECTOR, 'button[id="colorChange"]')
    COLOR_CHANGE_BUTTON_AFTER = (By.CSS_SELECTOR, 'button[class*="text-danger"]')
    VISIBLE_AFTER_FIVE_SECONDS_BUTTON = (By.CSS_SELECTOR, 'button[id="visibleAfter"]')
    ENABLE_BUTTON = (By.CSS_SELECTOR, 'button[id="enableAfter"]')

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver, page=UIRoutes.DYNAMIC_PROPERTIES)

    @allure.step('Check enable button')
    def check_enable_button(self) -> bool:
        try:
            self.element_is_clickable(self.ENABLE_BUTTON)
        except TimeoutException:
            return False
        return True

    @allure.step('Check changed of color')
    def check_changed_of_color(self) -> tuple[str, str]:
        color_button_before = self.element_is_present(self.COLOR_CHANGE_BUTTON_BEFORE)
        color_before = color_button_before.value_of_css_property('color')
        color_button_after = self.element_is_present(self.COLOR_CHANGE_BUTTON_AFTER)
        color_after = color_button_after.value_of_css_property('color')
        return color_before, color_after

    @allure.step('Check appear of button')
    def check_appear_of_button(self) -> bool:
        try:
            self.element_is_visible(self.VISIBLE_AFTER_FIVE_SECONDS_BUTTON)
        except TimeoutException:
            return False
        return True
