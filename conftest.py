import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
import time

from Pages.profile_page import ProfilePage
from Locators import locators_patient

driver = None

# Configure various connection information of the app
@pytest.fixture(scope='session')
def android_setting():
    des = {
        'automationName': 'appium',
        'platformName': 'Android',
        'platformVersion': '13.0', # Fill in the system version number of the android virtual machine/real machine
        'deviceName': 'autoschool10', # Fill in the device name of the Android virtual machine/real machine
        'appPackage': 'com.doct24.doct24_android', # Fill in the package name of the app under test
        'appActivity': 'com.doct24.doct24_android.view.MainActivity', # Fill in the entrance of the app under test
        'udid': 'emulator-5554', # Fill in the udid viewed through the command line adb devices
        'noReset': True, # Whether to reset APP
        'noSign': True, # Whether not to sign
        'unicodeKeyboard': True, # Whether to support Chinese input
        'resetKeyboard': True, # Whether to support resetting the keyboard
        'newCommandTimeout': 30 # Disconnect if no new command is sent for 30 seconds
    }
    return des


# Start the calculator app in Android system
@pytest.fixture(scope='session')
def start_app(android_setting):
    global driver
    driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', options=UiAutomator2Options().
                              load_capabilities(android_setting))
    yield driver
    driver.quit()


# Создаем фикстуру с областью видимости "session" для задания данных для авторизации
@pytest.fixture(scope="session", autouse=False)
def login_data():
    return {
        "PHONE": "9113459855",
        'CODE_1': '1',
        'CODE_2': '1',
        'CODE_3': '1',
        'CODE_4': '1'
    }

@pytest.fixture(scope="session", autouse=False)
def login_patient(start_app, login_data) -> ProfilePage:
    """Функция для заполнения поля при помощи клавиатуры смартфона"""
    prof_page = ProfilePage(start_app, locators_patient.locators)
    # выходим из профиля, если приложение уже авторизовано
    if prof_page.check_elem_is_visible('HELLO_MSG_ID', 'ID'):
        prof_page.click_element('PRFL_BTN_XP', 'XPATH')
        prof_page.click_element('PRFL_EXT_BTN_ID', 'ID')
        prof_page.click_element('PRFL_EXT_CONF_ID', 'ID')
        prof_page.click_element('PRFL_BTN_XP', 'XPATH')

    # создаем словарь кодов для взаимодействия с клавиатурой смартфона
    num = {'0': 7, '1': 8, '2': 9, '3': 10, '4': 11, '5': 12, '6': 13, '7': 14, '8': 15, '9': 16}
    field = prof_page.get_elem_obj('PHONE_FLD_XP', 'XPATH')
    field.click()
    # вводим номер телефона через системную клавиатуру андройда
    for i in login_data['PHONE']:
        start_app.press_keycode(num[i])
    prof_page.click_element('NEXT_BTN_XP', 'XPATH')
    prof_page.fill_the_field('CODE_1_FLD_ID', login_data['CODE_1'], 'ID')
    prof_page.fill_the_field('CODE_2_FLD_ID', login_data['CODE_2'], 'ID')
    prof_page.fill_the_field('CODE_3_FLD_ID', login_data['CODE_3'], 'ID')
    prof_page.fill_the_field('CODE_4_FLD_ID', login_data['CODE_4'], 'ID')
    prof_page.click_element('NEXT_2_BTN_XP', 'XPATH')
    return prof_page


@pytest.fixture(scope="session", autouse=False)
def unlogin_patient(login_patient):
    """Функция для разлогинивания, если приложение авторизовано, и для выдачи разрешения приложению"""
    if not login_patient.check_elem_is_visible('PATRON_FLD_ID', 'ID'):
        login_patient.click_element('PRFL_BTN_XP', 'XPATH')
        login_patient.click_element('PERS_DATA_BTN_ID', 'ID')

    if login_patient.check_elem_is_visible('PERMIS_MESS_ID', 'ID'):
        login_patient.click_element('FOREGRND_ONLY_BTN_ID', 'ID')
        login_patient.click_element('FOREGRND_ONLY_BTN_ID', 'ID')
        login_patient.click_element('ALLOW_BTN_ID', 'ID')
        login_patient.click_element('ALLOW_BTN_ID', 'ID')
