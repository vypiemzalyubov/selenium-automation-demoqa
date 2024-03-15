import os
import random

import allure
from selenium.webdriver import Keys
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from models.models import Person
from pages.base_page import BasePage
from utils.generator import generated_file, generated_person, generated_subject
from utils.routes import UIRoutes


class FormPage(BasePage):
    # registration form
    FIRST_NAME = (By.CSS_SELECTOR, '#firstName')
    LAST_NAME = (By.CSS_SELECTOR, '#lastName')
    EMAIL = (By.CSS_SELECTOR, '#userEmail')
    GENDER = (
        By.CSS_SELECTOR,
        f'div[class*="custom-control"] label[for="gender-radio-{random.randint(1, 3)}"]',
    )
    MOBILE = (By.CSS_SELECTOR, 'input[id="userNumber"]')
    DATE_OF_BIRTH = (By.CSS_SELECTOR, '#dateOfBirthInput')
    SUBJECT = (By.CSS_SELECTOR, 'input[id="subjectsInput"]')
    HOBBIES = (
        By.CSS_SELECTOR,
        f'div[class*="custom-control"] label[for="hobbies-checkbox-{random.randint(1, 3)}"]',
    )
    FILE_INPUT = (By.CSS_SELECTOR, 'input[id="uploadPicture"]')
    CURRENT_ADDRESS = (By.CSS_SELECTOR, '#currentAddress')
    SELECT_STATE = (By.CSS_SELECTOR, 'div[id="state"]')
    STATE_INPUT = (By.CSS_SELECTOR, f'#react-select-3-option-{random.randint(0, 3)}')
    SELECT_CITY = (By.CSS_SELECTOR, 'div[id="city"]')
    CITY_INPUT = (By.CSS_SELECTOR, 'input[id="react-select-4-input"]')
    SUBMIT = (By.CSS_SELECTOR, '#submit')

    # table result
    RESULT_TABLE = (By.XPATH, '//div[@class="table-responsive"]//td[2]')

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver, page=UIRoutes.FORM)

    @allure.step('Fill in all fields')
    def fill_form_fields(self) -> Person:
        person = next(generated_person())
        file_name, path = generated_file()
        subject = generated_subject()
        self.remove_footer()
        self.element_is_visible(self.FIRST_NAME).send_keys(person.firstname)
        self.element_is_visible(self.LAST_NAME).send_keys(person.lastname)
        self.element_is_visible(self.EMAIL).send_keys(person.email)
        self.element_is_visible(self.GENDER).click()
        self.element_is_visible(self.MOBILE).send_keys(person.mobile)
        self.element_is_visible(self.SUBJECT).send_keys(subject)
        self.element_is_visible(self.SUBJECT).send_keys(Keys.RETURN)
        self.element_is_visible(self.HOBBIES).click()
        self.element_is_present(self.FILE_INPUT).send_keys(path)
        os.remove(path)
        self.element_is_visible(self.CURRENT_ADDRESS).send_keys(person.current_address)
        self.element_is_visible(self.SELECT_STATE).click()
        self.element_is_visible(self.STATE_INPUT).click()
        self.element_is_visible(self.SELECT_CITY).click()
        self.element_is_visible(self.CITY_INPUT).send_keys(Keys.RETURN)
        self.element_is_visible(self.SUBMIT).click()
        return person

    @allure.step('Get form result')
    def form_result(self) -> list[str]:
        result_list = self.elements_are_visible(self.RESULT_TABLE)
        data = []
        for item in result_list:
            self.go_to_element(item)
            data.append(item.text)
        return data
