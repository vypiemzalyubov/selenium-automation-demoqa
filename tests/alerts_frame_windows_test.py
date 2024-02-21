import allure
import pytest

from pages.alerts_frame_windows_page import (
    AlertsPage,
    BrowserWindowsPage,
    FramesPage,
    ModalDialogsPage,
    NestedFramesPage
)

pytestmark = allure.suite('Alerts, Frame & Windows')


@allure.feature('Browser Windows Page')
class TestBrowserWindows:

    @allure.title('Checking the opening of a new tab')
    def test_new_tab(self):
        browser_windows_page = BrowserWindowsPage(self.driver)
        browser_windows_page.open()
        text_result = browser_windows_page.check_opened_interface('tab')
        assert text_result == 'This is a sample page', \
            'the new tab has not opened or an incorrect tab has opened'

    @allure.title('Checking the opening of a new window')
    def test_new_window(self):
        browser_windows_page = BrowserWindowsPage(self.driver)
        browser_windows_page.open()
        text_result = browser_windows_page.check_opened_interface('window')
        assert text_result == 'This is a sample page', \
            'the new window has not opened or an incorrect window has opened'


@allure.feature('Alerts Page')
class TestAlertsPage:

    @allure.title('Checking the opening of an alert')
    def test_see_alert(self):
        alert_page = AlertsPage(self.driver)
        alert_page.open()
        alert_text = alert_page.check_see_alert()
        assert alert_text == 'You clicked a button', \
            'Alert did not show up'

    @allure.title('Checking the opening of the alert after 5 seconds')
    @pytest.mark.flaky(reruns=1, reruns_delay=1)
    def test_alert_appear_after_5_sec(self):
        alert_page = AlertsPage(self.driver)
        alert_page.open()
        alert_text = alert_page.check_alert_appear_after_5_sec()
        assert alert_text == 'This alert appeared after 5 seconds', \
            'Alert did not show up'

    @allure.title('Checking the acceptance of the alert')
    def test_accept_alert(self):
        alert_page = AlertsPage(self.driver)
        alert_page.open()
        alert_text = alert_page.check_action_alert('accept')
        assert alert_text == 'You selected Ok', \
            'Alert did not show up'

    @allure.title('Checking the dismission of the alert')
    def test_dismiss_alert(self):
        alert_page = AlertsPage(self.driver)
        alert_page.open()
        alert_text = alert_page.check_action_alert('dismiss')
        assert alert_text == 'You selected Cancel', \
            'Alert did not show up'

    @allure.title('Checking the opening of the alert with prompt')
    def test_prompt_alert(self):
        alert_page = AlertsPage(self.driver)
        alert_page.open()
        text, alert_text = alert_page.check_prompt_alert()
        assert text in alert_text, \
            'Alert did not show up'


@allure.feature('Frame Page')
class TestFramesPage:

    @allure.title('Check the page with frames')
    def test_frames(self):
        frame_page = FramesPage(self.driver)
        frame_page.open()
        result_frame1 = frame_page.check_frame('frame1')
        result_frame2 = frame_page.check_frame('frame2')
        assert result_frame1 == ['This is a sample page', '500px', '350px'], \
            'The frame does not exist'
        assert result_frame2 == ['This is a sample page', '100px', '100px'], \
            'The frame does not exist'


@allure.feature('Nested Page')
class TestNestedFramesPage:

    @allure.title('Check the page with nested frames')
    def test_nested_frames(self):
        nested_frame_page = NestedFramesPage(self.driver)
        nested_frame_page.open()
        parent_text, child_text = nested_frame_page.check_nested_frame()
        assert parent_text == 'Parent frame', \
            'Nested frame does not exist'
        assert child_text == 'Child Iframe', \
            'Nested frame does not exist'


@allure.feature('Modal Dialog Page')
class TestModalDialogsPage:

    @allure.title('Check the page with small modal dialogs')
    @pytest.mark.parametrize(
        'method',
        ['button', 'cross', 'overlay']
    )
    def test_small_modal_dialogs(self, method):
        modal_dialogs_page = ModalDialogsPage(self.driver)
        modal_dialogs_page.open()
        title_small, body_small_text = modal_dialogs_page.check_modal_dialogs('small', method)
        assert title_small == 'Small Modal', \
            'The header is not "Small modal"'
        assert 'This is a small modal' in body_small_text, \
            'Small modal body does not content "This is a small modal"'

    @allure.title('Check the page with large modal dialogs')
    @pytest.mark.flaky(reruns=1, reruns_delay=1)
    @pytest.mark.parametrize(
        'method',
        ['button', 'cross', 'overlay']
    )
    def test_large_modal_dialogs(self, method):
        modal_dialogs_page = ModalDialogsPage(self.driver)
        modal_dialogs_page.open()
        title_large, body_large_text = modal_dialogs_page.check_modal_dialogs('large', method)
        assert title_large == 'Large Modal', \
            'The header is not "Large Modal"'
        assert 'Lorem Ipsum' in body_large_text, \
            'Small modal body does not content "Lorem Ipsum"'
