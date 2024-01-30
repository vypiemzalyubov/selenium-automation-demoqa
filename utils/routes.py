from enum import Enum


class UIRoutes(str, Enum):
    TEXT_BOX = "/text-box"
    CHECKBOX = "/checkbox"
    RADIO_BUTTON = "/radio-button"
    WEB_TABLES = "/webtables"
    BUTTONS = "/buttons"
    LINKS = "/links"
    UPLOAD_DOWNLOAD = "/upload-download"
    DYNAMIC_PROPERTIES = "/dynamic-properties"
    FORM = "/automation-practice-form"
    BROWSER_WINDOWS = "/browser-windows"
    ALERTS = "/alerts"