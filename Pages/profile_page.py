import time, datetime
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
import base64
import string
import random
from selenium.webdriver.common.action_chains import ActionChains


class ProfilePage:
    def __init__(self, driver, locators):
        self.driver = driver
        self.locators = locators

    def get_wait(self) -> WebDriverWait:
        """Функция для получения объекта WebDriverWait"""
        wait = WebDriverWait(driver=self.driver, timeout=10, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                                 NoSuchElementException])
        return wait

    def click_element(self, field_locator: str, find_meth: str) -> None:
        """Функция кликает элемент"""
        field = None
        wait = self.get_wait()
        if find_meth == 'XPATH':
            field = wait.until(lambda x: x.find_element(AppiumBy.XPATH, value=self.locators[field_locator]))
            # field = self.driver.find_element(by=AppiumBy.XPATH, value=self.locators[field_locator])
        elif find_meth == 'ID':
            field = wait.until(lambda x: x.find_element(AppiumBy.ID, value=self.locators[field_locator]))
            # field = self.driver.find_element(by=AppiumBy.ID, value=self.locators[field_locator])
        elif find_meth == 'IND':
            field = wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR, self.locators[field_locator]))
        elif find_meth == 'CLS':
            field = wait.until(lambda x: x.find_element(AppiumBy.CLASS_NAME, value=self.locators[field_locator]))
        field.click()

    def clear_element(self, field_locator: str, find_meth: str) -> None:
        """Функция очищает элемент"""
        field = None
        wait = self.get_wait()
        if find_meth == 'XPATH':
            field = wait.until(lambda x: x.find_element(AppiumBy.XPATH, value=self.locators[field_locator]))
            # field = self.driver.find_element(by=AppiumBy.XPATH, value=self.locators[field_locator])
        elif find_meth == 'ID':
            field = wait.until(lambda x: x.find_element(AppiumBy.ID, value=self.locators[field_locator]))
            # field = self.driver.find_element(by=AppiumBy.ID, value=self.locators[field_locator])
        field.clear()

    def fill_the_field(self, field_locator: str, data: str, find_meth: str) -> None:
        """Функция заполняет текстовое поле"""
        field = None
        wait = self.get_wait()
        if find_meth == 'XPATH':
            field = wait.until(lambda x: x.find_element(AppiumBy.XPATH, value=self.locators[field_locator]))
            # field = self.driver.find_element(by=AppiumBy.XPATH, value=self.locators[field_locator])
        elif find_meth == 'ID':
            field = wait.until(lambda x: x.find_element(AppiumBy.ID, value=self.locators[field_locator]))
            # field = self.driver.find_element(by=AppiumBy.ID, value=self.locators[field_locator])
        field.send_keys(data)

    def get_elem_attr(self, field_locator: str, find_meth: str, attr: str) -> str:
        """Функция возвращает атрибут элемента"""
        elem = None
        wait = self.get_wait()
        if find_meth == 'XPATH':
            elem = wait.until(lambda x: x.find_element(AppiumBy.XPATH, value=self.locators[field_locator]))
            # elem = self.driver.find_element(by=AppiumBy.XPATH, value=self.locators[field_locator])
        elif find_meth == 'ID':
            elem = wait.until(lambda x: x.find_element(AppiumBy.ID, value=self.locators[field_locator]))
            # elem = self.driver.find_element(by=AppiumBy.ID, value=self.locators[field_locator])
        return elem.get_attribute(attr)

    def get_elem_obj(self, field_locator: str, find_meth: str):
        """Функция возвращает объект элемента"""
        wait = self.get_wait()
        if find_meth == 'XPATH':
            try:
                elem = wait.until(lambda x: x.find_element(AppiumBy.XPATH, value=self.locators[field_locator]))
                # elem = self.driver.find_element(by=AppiumBy.XPATH, value=self.locators[field_locator])
            except NoSuchElementException:
                return False
            return elem
        elif find_meth == 'ID':
            try:
                elem = wait.until(lambda x: x.find_element(AppiumBy.ID, value=self.locators[field_locator]))
                # elem = self.driver.find_element(by=AppiumBy.ID, value=self.locators[field_locator])
            except NoSuchElementException:
                return False
            return elem

    def get_elems_obj(self, field_locator: str, find_meth: str):
        """Функция возвращает итерируемый объект с элементами"""
        wait = self.get_wait()
        if find_meth == 'XPATH':
            try:
                elems = wait.until(lambda x: x.find_elements(AppiumBy.XPATH, value=self.locators[field_locator]))
                # elem = self.driver.find_element(by=AppiumBy.XPATH, value=self.locators[field_locator])
            except NoSuchElementException:
                return False
            return elems
        elif find_meth == 'ID':
            try:
                elems = wait.until(lambda x: x.find_elements(AppiumBy.ID, value=self.locators[field_locator]))
                # elem = self.driver.find_element(by=AppiumBy.ID, value=self.locators[field_locator])
            except NoSuchElementException:
                return False
            return elems

    def check_elem_is_visible(self, field_locator: str, find_meth: str):
        """Функция возвращает объект элемента"""
        # wait = self.get_wait()
        time.sleep(1)
        if find_meth == 'XPATH':
            try:
                # wait.until(lambda x: x.find_element(AppiumBy.XPATH, value=self.locators[field_locator]))
                time.sleep(3)
                self.driver.find_element(by=AppiumBy.XPATH, value=self.locators[field_locator])
            except NoSuchElementException:
                return False
            return True
        elif find_meth == 'ID':
            try:
                # wait.until(lambda x: x.find_element(AppiumBy.ID, value=self.locators[field_locator]))
                time.sleep(3)
                self.driver.find_element(by=AppiumBy.ID, value=self.locators[field_locator])
            except NoSuchElementException:
                return False
            return True

    @staticmethod
    def get_cur_month_rus_str() -> str:
        """Метод получения текущего месяца в род падеже в виде строки"""
        month_dict = {
            1: 'января',
            2: 'февраля',
            3: "марта",
            4: "апреля",
            5: "мая",
            6: "июня",
            7: "июля",
            8: "августа",
            9: "сентября",
            10: "октября",
            11: "ноября",
            12: "декабря"
        }
        current_month = datetime.datetime.now().month
        return month_dict[current_month]

    @staticmethod
    def get_cur_month_digit_str() -> str:
        """Метод получения текущего месяца двузначным числом в виде строки"""
        current_month = datetime.datetime.now().month
        if current_month < 10:
            res = '0'+str(current_month)
        else:
            res = str(current_month)
        return res

    @staticmethod
    def get_date_18_years_ago():
        """Функция для получения даты 18 лет назад от текущей"""
        present_date = datetime.datetime.now().strftime("%d/%m/%Y")
        present_y = int(present_date[-4:])
        eigtheen_y_ago = present_y - 18
        date_eighteen_y_ago = datetime.datetime(eigtheen_y_ago, int(present_date[3:5]), int(present_date[:2]))

        return date_eighteen_y_ago

    def scroll_and_get_elem_obj(self):
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().resourceId'
                                                               '("com.doct24.doct24_android:id/layout_personal_data")).'
                                                               'scrollIntoView(new UiSelector().text("Город"))')

    def push_photo(self, from_path: str, dest_path: str):
        with open(from_path, 'rb') as image:
            img = image.read()
        self.driver.push_file(dest_path, base64.b64encode(img).decode('utf-8'))

    def screen_shot(self, file_name: str):
        self.driver.get_screenshot_as_file(f"Screenshots/{file_name}")

    @staticmethod
    def get_randon_file_name(n: int):
        img_randon_name = ''.join(random.choices(string.ascii_letters, k=n))
        return img_randon_name

    def tap_by_coordinates(self, x: int, y: int):
        TouchAction(self.driver).tap(None, x, y, 1).perform()






