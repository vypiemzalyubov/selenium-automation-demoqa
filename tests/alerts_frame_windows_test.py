import time

import allure

from pages.alerts_frame_windows_page import (
    BrowserWindowsPage,
    AlertsPage,
    FramesPage,
    NestedFramesPage,
    ModalDialogsPage
) 
from utils.routes import UIRoutes


@allure.suite("Alerts, Frame & Windows")
class TestBrowserWindows:

    @allure.title("Checking the opening of a new tab")
    def test_new_tab(self):
        browser_windows_page = BrowserWindowsPage(self.driver, f"https://demoqa.com{UIRoutes.BROWSER_WINDOWS}")
        browser_windows_page.open()
        text_result = browser_windows_page.check_opened_interface("tab")
        assert text_result == "This is a sample page", \
            "the new tab has not opened or an incorrect tab has opened"

    @allure.title("Checking the opening of a new window")
    def test_new_window(self):
        browser_windows_page = BrowserWindowsPage(self.driver, f"https://demoqa.com{UIRoutes.BROWSER_WINDOWS}")
        browser_windows_page.open()
        text_result = browser_windows_page.check_opened_interface("window")
        assert text_result == "This is a sample page", \
            "the new window has not opened or an incorrect window has opened"


@allure.feature("Alerts Page")
class TestAlertsPage:

    @allure.title("Checking the opening of an alert")
    def test_see_alert(self):
        alert_page = AlertsPage(self.driver, f"https://demoqa.com{UIRoutes.ALERTS}")
        alert_page.open()
        alert_text = alert_page.check_see_alert()
        assert alert_text == "You clicked a button", \
            "Alert did not show up"

    @allure.title("Checking the opening of the alert after 5 seconds")
    def test_alert_appear_after_5_sec(self):
        alert_page = AlertsPage(self.driver, f"https://demoqa.com{UIRoutes.ALERTS}")
        alert_page.open()
        alert_text = alert_page.check_alert_appear_after_5_sec()
        assert alert_text == "This alert appeared after 5 seconds", \
            "Alert did not show up"

    @allure.title("Checking the acceptance of the alert")
    def test_accept_alert(self):
        alert_page = AlertsPage(self.driver, f"https://demoqa.com{UIRoutes.ALERTS}")
        alert_page.open()
        alert_text = alert_page.check_action_alert("accept")
        assert alert_text == "You selected Ok", \
            "Alert did not show up"

    @allure.title("Checking the dismission of the alert")
    def test_dismiss_alert(self):
        alert_page = AlertsPage(self.driver, f"https://demoqa.com{UIRoutes.ALERTS}")
        alert_page.open()
        alert_text = alert_page.check_action_alert("dismiss")
        assert alert_text == "You selected Cancel", \
            "Alert did not show up"

    @allure.title("Checking the opening of the alert with prompt")
    def test_prompt_alert(self):
        alert_page = AlertsPage(self.driver, f"https://demoqa.com{UIRoutes.ALERTS}")
        alert_page.open()
        text, alert_text = alert_page.check_prompt_alert()
        assert text in alert_text, \
            "Alert did not show up"


# @allure.feature("Frame Page")
# class TestFramesPage:

#     @allure.title("Check the page with frames")
#     def test_frames(self):
#         frame_page = FramesPage(self.driver, "https://demoqa.com/frames")
#         frame_page.open()
#         result_frame1 = frame_page.check_frame("frame1")
#         result_frame2 = frame_page.check_frame("frame2")
#         assert result_frame1 == ["This is a sample page", "500px", "350px"], "The frame does not exist"
#         assert result_frame2 == ["This is a sample page", "100px", "100px"], "The frame does not exist"

# @allure.feature("Nested Page")
# class TestNestedFramesPage:
#     @allure.title("Check the page with nested frames")
#     def test_nested_frames(self):
#         nested_frame_page = NestedFramesPage(self.driver, "https://demoqa.com/nestedframes")
#         nested_frame_page.open()
#         parent_text, child_text = nested_frame_page.check_nested_frame()
#         assert parent_text == "Parent frame", "Nested frame does not exist"
#         assert child_text == "Child Iframe", "Nested frame does not exist"


# @allure.feature("Modal Dialog Page")
# class TestModalDialogsPage:

#     @allure.title("Check the page with modal dialogs")
#     def test_modal_dialogs(self):
#         modal_dialogs_page = ModalDialogsPage(self.driver, "https://demoqa.com/modal-dialogs")
#         modal_dialogs_page.open()
#         small, large = modal_dialogs_page.check_modal_dialogs()
#         assert small[1] < large[1], "text from large dialog is less than text from small dialog"
#         assert small[0] == "Small Modal", "The header is not 'Small modal'"
#         assert large[0] == "Large Modal", "The header is not 'Large modal'"