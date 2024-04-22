import time, datetime
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait


class ProfilePage:

    def __init__(self, driver, locators):
        self.driver = driver
        self.locators = locators

    def get_wait(self) -> WebDriverWait:
        """Функция для получения объекта WebDriverWait"""
        wait = WebDriverWait(driver=self.driver, timeout=3, poll_frequency=1,
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

    def check_elem_is_visible(self, field_locator: str, find_meth: str):
        """Функция возвращает объект элемента"""
        # wait = self.get_wait()
        time.sleep(1)
        if find_meth == 'XPATH':
            try:
                # wait.until(lambda x: x.find_element(AppiumBy.XPATH, value=self.locators[field_locator]))
                self.driver.find_element(by=AppiumBy.XPATH, value=self.locators[field_locator])
            except NoSuchElementException:
                return False
            return True
        elif find_meth == 'ID':
            try:
                # wait.until(lambda x: x.find_element(AppiumBy.ID, value=self.locators[field_locator]))
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

