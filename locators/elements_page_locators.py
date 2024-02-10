from selenium.webdriver.common.by import By


class TextBoxPageLocators:

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


class CheckBoxPageLocators:

    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, 'button[title="Expand all"]')
    ITEM_LIST = (By.CSS_SELECTOR, 'span[class="rct-title"]')
    CHECKED_ITEMS = (By.CSS_SELECTOR, 'svg[class="rct-icon rct-icon-check"]')
    TITLE_ITEM = './/ancestor::span[@class="rct-text"]'
    OUTPUT_RESULT = (By.CSS_SELECTOR, 'span[class="text-success"]')


class RadioButtonPageLocators:

    YES_RADIOBUTTON = (By.CSS_SELECTOR, 'label[class^="custom-control"][for="yesRadio"]')
    IMPRESSIVE_RADIOBUTTON = (By.CSS_SELECTOR, 'label[class^="custom-control"][for="impressiveRadio"]')
    NO_RADIOBUTTON = (By.CSS_SELECTOR, 'label[class^="custom-control"][for="noRadio"]')
    OUTPUT_RESULT = (By.CSS_SELECTOR, 'p span[class="text-success"]')


class WebTablePageLocators:

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


class ButtonsPageLocators:

    DOUBLE_BUTTON = (By.XPATH, '//button[text()="Double Click Me"]')
    RIGHT_CLICK_BUTTON = (By.XPATH, '//button[text()="Right Click Me"]')
    CLICK_ME_BUTTON = (By.XPATH, '//button[text()="Click Me"]')

    # result
    SUCCESS_DOUBLE = (By.XPATH, '//p[@id="doubleClickMessage"]')
    SUCCESS_RIGHT = (By.XPATH, '//p[@id="rightClickMessage"]')
    SUCCESS_CLICK_ME = (By.XPATH, '//p[@id="dynamicClickMessage"]')


class LinksPageLocators:

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


class UploadAndDownloadPageLocators:

    UPLOAD_FILE = (By.CSS_SELECTOR, 'input[id="uploadFile"]')
    UPLOADED_RESULT = (By.CSS_SELECTOR, 'p[id="uploadedFilePath"]')

    DOWNLOAD_FILE = (By.CSS_SELECTOR, 'a[id="downloadButton"]')


class DynamicPropertiesPageLocators:

    COLOR_CHANGE_BUTTON_BEFORE = (By.CSS_SELECTOR, 'button[id="colorChange"]')
    COLOR_CHANGE_BUTTON_AFTER = (By.CSS_SELECTOR, 'button[class*="text-danger"]')
    VISIBLE_AFTER_FIVE_SECONDS_BUTTON = (By.CSS_SELECTOR, 'button[id="visibleAfter"]')
    ENABLE_BUTTON = (By.CSS_SELECTOR, 'button[id="enableAfter"]')