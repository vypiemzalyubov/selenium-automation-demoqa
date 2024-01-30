import allure

from pages.form_page import FormPage
from utils.routes import UIRoutes


@allure.suite("Forms")
class TestFormPage:

    @allure.title("Check form")
    def test_form(self):
        form_page = FormPage(self.driver, f"https://demoqa.com{UIRoutes.FORM}")
        form_page.open()
        person_info = form_page.fill_form_fields()
        result_info = form_page.form_result()
        assert [person_info.firstname + " " + person_info.lastname, person_info.email] == [result_info[0], result_info[1]], \
            "The form has not been filled"
