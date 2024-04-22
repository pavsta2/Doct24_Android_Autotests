import pytest
import allure
import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException

from data_config.possit import data_test_possit as dtp
from data_config.negot import data_test_negot as dtn


@allure.feature('Проверки валидации поля Фамилия')
class TestLNameField:
    @allure.story('Позитивные проверки валидации фамилии по кол-ву символов')
    @pytest.mark.parametrize('params',
                            dtp.ALLNAME_FLD_LEN_POSSITIVE[0],
                            ids=dtp.ALLNAME_FLD_LEN_POSSITIVE[1])
    def test_lname_len_possit(self, login_patient, params):
        """Позитивные проверки валидации фамилии поо кол-ву символов"""
        if not login_patient.check_elem_is_visible('LNAME_FLD_ID', 'ID'):
            login_patient.click_element('PRFL_BTN_XP', 'XPATH')
            login_patient.click_element('PERS_DATA_BTN_ID', 'ID')

        login_patient.clear_element('LNAME_FLD_ID', 'ID')
        login_patient.fill_the_field('LNAME_FLD_ID',  params['INPUT'],'ID')
        login_patient.click_element('SAVE_PTN_DATA_BTN_ID', 'ID')

        err_mess = login_patient.check_elem_is_visible('ER_MESS_LMANE_XP_SYMB', 'XPATH')
        assert not err_mess, 'При вводе валидных данных появляется ошибка'

    @allure.story('Позитивные проверки валидации фамилии по типу символов')
    @pytest.mark.parametrize('params',
                             dtp.ALLNAME_FLD_SYMB_POSSITIVE[0],
                             ids=dtp.ALLNAME_FLD_SYMB_POSSITIVE[1])
    def test_lname_symb_possit(self, login_patient, params):
        """Позитивные проверки валидации фамилии по типу символов"""
        if not login_patient.check_elem_is_visible('LNAME_FLD_ID', 'ID'):
            login_patient.click_element('PRFL_BTN_XP', 'XPATH')
            login_patient.click_element('PERS_DATA_BTN_ID', 'ID')
        login_patient.clear_element('LNAME_FLD_ID', 'ID')
        login_patient.fill_the_field('LNAME_FLD_ID', params['INPUT'], 'ID')
        login_patient.click_element('SAVE_PTN_DATA_BTN_ID', 'ID')

        err_mess = login_patient.check_elem_is_visible('ER_MESS_LMANE_XP_SYMB', 'XPATH')
        assert not err_mess, 'При вводе валидных данных появляется ошибка'

    @allure.story('Позитивные проверки удаления пробелов в начале и в конце')
    @pytest.mark.parametrize('params',
                             dtp.ALLNAME_FLD_SPACE_DELETE[0],
                             ids=dtp.ALLNAME_FLD_SPACE_DELETE[1])
    def test_lname_space_del_possit(self, login_patient, params):
        """Позитивные проверки удаления пробелов в начале и в конце"""
        if not login_patient.check_elem_is_visible('LNAME_FLD_ID', 'ID'):
            login_patient.click_element('PRFL_BTN_XP', 'XPATH')
            login_patient.click_element('PERS_DATA_BTN_ID', 'ID')
        login_patient.clear_element('LNAME_FLD_ID', 'ID')
        login_patient.fill_the_field('LNAME_FLD_ID', params['INPUT'], 'ID')
        login_patient.fill_the_field('FNAME_FLD_ID', 'test', 'ID')
        login_patient.fill_the_field('DBIRTH_FLD_ID', '26.02.1999', 'ID')

        login_patient.click_element('SAVE_PTN_DATA_BTN_ID', 'ID')
        login_patient.click_element('PRFL_BTN_XP', 'XPATH')
        login_patient.click_element('PERS_DATA_BTN_ID', 'ID')

        field_fact_data = str(login_patient.get_elem_attr('LNAME_FLD_ID', 'ID', 'text'))
        assert field_fact_data == str(params['INPUT']).strip(), 'Пробелы не удаляются'

    @allure.story('Позитивные проверки сохранения данных в том регистре в каком ввел юзер')
    @pytest.mark.parametrize('params',
                             dtp.ALLNAME_FLD_TEXT_REGISTR[0],
                             ids=dtp.ALLNAME_FLD_TEXT_REGISTR[1])
    def test_lname_registr_input_possit(self, login_patient, params):
        """Позитивные проверки сохранения данных в том регистре в каком ввел юзер"""
        if not login_patient.check_elem_is_visible('LNAME_FLD_ID', 'ID'):
            login_patient.click_element('PRFL_BTN_XP', 'XPATH')
            login_patient.click_element('PERS_DATA_BTN_ID', 'ID')
        login_patient.clear_element('LNAME_FLD_ID', 'ID')
        login_patient.fill_the_field('LNAME_FLD_ID', params['INPUT'], 'ID')
        login_patient.fill_the_field('FNAME_FLD_ID', 'test', 'ID')
        login_patient.fill_the_field('DBIRTH_FLD_ID', '26.02.1999', 'ID')

        login_patient.click_element('SAVE_PTN_DATA_BTN_ID', 'ID')
        login_patient.click_element('PRFL_BTN_XP', 'XPATH')
        login_patient.click_element('PERS_DATA_BTN_ID', 'ID')

        field_fact_data = str(login_patient.get_elem_attr('LNAME_FLD_ID', 'ID', 'text'))
        assert field_fact_data == str(params['INPUT']), (f"Введенные данные сохраняются не том регистре, "
                                                         f"в каком ввел юзер, expected: {str(params['INPUT'])}, "
                                                         f"fact: {field_fact_data}")

    @allure.story('Негативные проверки валидации фамилии по кол-ву символов')
    @pytest.mark.parametrize('params',
                             dtn.ALLNAME_FLD_MIN_LEN[0],
                             ids=dtn.ALLNAME_FLD_MIN_LEN[1])
    def test_lname_min_len_negot(self, login_patient, params):
        """Негативные проверки валидации фамилии поо кол-ву символов"""
        if not login_patient.check_elem_is_visible('LNAME_FLD_ID', 'ID'):
            login_patient.click_element('PRFL_BTN_XP', 'XPATH')
            login_patient.click_element('PERS_DATA_BTN_ID', 'ID')

        login_patient.clear_element('LNAME_FLD_ID', 'ID')
        login_patient.fill_the_field('LNAME_FLD_ID', params['INPUT'], 'ID')
        login_patient.click_element('SAVE_PTN_DATA_BTN_ID', 'ID')

        err_mess = login_patient.check_elem_is_visible('ER_MESS_LMANE_XP_SYMB', 'XPATH')
        assert err_mess, 'При вводе НЕвалидных данных НЕТ сообщения об ошибке'

    @allure.story('Негативные проверки валидации фамилии по кол-ву символов')
    @pytest.mark.parametrize('params',
                             dtn.ALLNAME_FLD_MAX_LEN[0],
                             ids=dtn.ALLNAME_FLD_MAX_LEN[1])
    def test_lname_max_len_negot(self, login_patient, params):
        """Негативные проверки валидации фамилии поо кол-ву символов"""
        if not login_patient.check_elem_is_visible('LNAME_FLD_ID', 'ID'):
            login_patient.click_element('PRFL_BTN_XP', 'XPATH')
            login_patient.click_element('PERS_DATA_BTN_ID', 'ID')
        login_patient.clear_element('LNAME_FLD_ID', 'ID')
        login_patient.fill_the_field('LNAME_FLD_ID', params['INPUT'], 'ID')
        login_patient.click_element('SAVE_PTN_DATA_BTN_ID', 'ID')

        err_mess = login_patient.check_elem_is_visible('ER_MESS_LMANE_XP_SYMB', 'XPATH')
        assert err_mess, 'При вводе НЕвалидных данных НЕТ сообщения об ошибке'

    @allure.story('Негативные проверки валидации фамилии по типу символов')
    @pytest.mark.parametrize('params',
                             dtn.ALLNAME_FLD_SYMB[0],
                             ids=dtn.ALLNAME_FLD_SYMB[1])
    def test_lname_symb_negot(self, login_patient, params):
        """Негативные проверки валидации фамилии по типу символов"""
        if not login_patient.check_elem_is_visible('LNAME_FLD_ID', 'ID'):
            login_patient.click_element('PRFL_BTN_XP', 'XPATH')
            login_patient.click_element('PERS_DATA_BTN_ID', 'ID')
        login_patient.clear_element('LNAME_FLD_ID', 'ID')
        login_patient.fill_the_field('LNAME_FLD_ID', params['INPUT'], 'ID')
        login_patient.click_element('SAVE_PTN_DATA_BTN_ID', 'ID')

        err_mess = login_patient.check_elem_is_visible('ER_MESS_LMANE_XP_SYMB', 'XPATH')
        assert err_mess, 'При вводе НЕвалидных данных НЕТ сообщения об ошибке'

    @allure.story('Негативные проверки валидации на обязательность заполнения поля')
    def test_lname_mandotory_negot(self, login_patient):
        """Негативные проверки валидации на обязательность заполнения поля"""
        if not login_patient.check_elem_is_visible('LNAME_FLD_ID', 'ID'):
            login_patient.click_element('PRFL_BTN_XP', 'XPATH')
            login_patient.click_element('PERS_DATA_BTN_ID', 'ID')
        login_patient.clear_element('LNAME_FLD_ID', 'ID')
        login_patient.click_element('SAVE_PTN_DATA_BTN_ID', 'ID')

        err_mess = login_patient.check_elem_is_visible('ER_MESS_LMANE_XP_MNDTRY', 'XPATH')
        assert err_mess, 'При сохранении незаполненного поля НЕТ сообщения об ошибке'


@allure.feature('Проверки валидации поля Имя')
class TestFNameField:
    @allure.story('Позитивные проверки валидации Имени по кол-ву символов')
    @pytest.mark.parametrize('params',
                            dtp.ALLNAME_FLD_LEN_POSSITIVE[0],
                            ids=dtp.ALLNAME_FLD_LEN_POSSITIVE[1])
    def test_fname_len_possit(self, login_patient, params):
        """Позитивные проверки валидации Имени по кол-ву символо"""
        if not login_patient.check_elem_is_visible('FNAME_FLD_ID', 'ID'):
            login_patient.click_element('PRFL_BTN_XP', 'XPATH')
            login_patient.click_element('PERS_DATA_BTN_ID', 'ID')

        login_patient.clear_element('FNAME_FLD_ID', 'ID')
        login_patient.fill_the_field('FNAME_FLD_ID',  params['INPUT'],'ID')
        login_patient.click_element('SAVE_PTN_DATA_BTN_ID', 'ID')

        err_mess = login_patient.check_elem_is_visible('ER_MESS_FMANE_XP_SYMB', 'XPATH')
        assert not err_mess, 'При вводе валидных данных появляется ошибка'

    @allure.story('Позитивные проверки валидации имени по типу символов')
    @pytest.mark.parametrize('params',
                             dtp.ALLNAME_FLD_SYMB_POSSITIVE[0],
                             ids=dtp.ALLNAME_FLD_SYMB_POSSITIVE[1])
    def test_fname_symb_possit(self, login_patient, params):
        """Позитивные проверки валидации имени по типу символов"""
        if not login_patient.check_elem_is_visible('FNAME_FLD_ID', 'ID'):
            login_patient.click_element('PRFL_BTN_XP', 'XPATH')
            login_patient.click_element('PERS_DATA_BTN_ID', 'ID')
        login_patient.clear_element('FNAME_FLD_ID', 'ID')
        login_patient.fill_the_field('FNAME_FLD_ID', params['INPUT'], 'ID')
        login_patient.click_element('SAVE_PTN_DATA_BTN_ID', 'ID')

        err_mess = login_patient.check_elem_is_visible('ER_MESS_FMANE_XP_SYMB', 'XPATH')
        assert not err_mess, 'При вводе валидных данных появляется ошибка'

    @allure.story('Позитивные проверки удаления пробелов в начале и в конце')
    @pytest.mark.parametrize('params',
                             dtp.ALLNAME_FLD_SPACE_DELETE[0],
                             ids=dtp.ALLNAME_FLD_SPACE_DELETE[1])
    def test_fname_space_del_possit(self, login_patient, params):
        """Позитивные проверки удаления пробелов в начале и в конце"""
        if not login_patient.check_elem_is_visible('FNAME_FLD_ID', 'ID'):
            login_patient.click_element('PRFL_BTN_XP', 'XPATH')
            login_patient.click_element('PERS_DATA_BTN_ID', 'ID')
        login_patient.clear_element('FNAME_FLD_ID', 'ID')
        login_patient.fill_the_field('FNAME_FLD_ID', params['INPUT'], 'ID')
        login_patient.fill_the_field('LNAME_FLD_ID', 'test', 'ID')
        login_patient.fill_the_field('DBIRTH_FLD_ID', '26.02.1999', 'ID')

        login_patient.click_element('SAVE_PTN_DATA_BTN_ID', 'ID')
        login_patient.click_element('PRFL_BTN_XP', 'XPATH')
        login_patient.click_element('PERS_DATA_BTN_ID', 'ID')

        field_fact_data = str(login_patient.get_elem_attr('FNAME_FLD_ID', 'ID', 'text'))
        assert field_fact_data == str(params['INPUT']).strip(), 'Пробелы не удаляются'

    @allure.story('Позитивные проверки сохранения данных в том регистре в каком ввел юзер')
    @pytest.mark.parametrize('params',
                             dtp.ALLNAME_FLD_TEXT_REGISTR[0],
                             ids=dtp.ALLNAME_FLD_TEXT_REGISTR[1])
    def test_fname_registr_input_possit(self, login_patient, params):
        """Позитивные проверки сохранения данных в том регистре в каком ввел юзер"""
        if not login_patient.check_elem_is_visible('FNAME_FLD_ID', 'ID'):
            login_patient.click_element('PRFL_BTN_XP', 'XPATH')
            login_patient.click_element('PERS_DATA_BTN_ID', 'ID')
        login_patient.clear_element('FNAME_FLD_ID', 'ID')
        login_patient.fill_the_field('FNAME_FLD_ID', params['INPUT'], 'ID')
        login_patient.fill_the_field('LNAME_FLD_ID', 'test', 'ID')
        login_patient.fill_the_field('DBIRTH_FLD_ID', '26.02.1999', 'ID')

        login_patient.click_element('SAVE_PTN_DATA_BTN_ID', 'ID')
        login_patient.click_element('PRFL_BTN_XP', 'XPATH')
        login_patient.click_element('PERS_DATA_BTN_ID', 'ID')

        field_fact_data = str(login_patient.get_elem_attr('FNAME_FLD_ID', 'ID', 'text'))
        assert field_fact_data == str(params['INPUT']), (f"Введенные данные сохраняются не том регистре, "
                                                         f"в каком ввел юзер, expected: {str(params['INPUT'])}, "
                                                         f"fact: {field_fact_data}")

    @allure.story('Негативные проверки валидации Имени по мин кол-ву символов')
    @pytest.mark.parametrize('params',
                             dtn.ALLNAME_FLD_MIN_LEN[0],
                             ids=dtn.ALLNAME_FLD_MIN_LEN[1])
    def test_fname_min_len_negot(self, login_patient, params):
        """Негативные проверки валидации Имени по мин кол-ву символов"""
        if not login_patient.check_elem_is_visible('FNAME_FLD_ID', 'ID'):
            login_patient.click_element('PRFL_BTN_XP', 'XPATH')
            login_patient.click_element('PERS_DATA_BTN_ID', 'ID')

        login_patient.clear_element('FNAME_FLD_ID', 'ID')
        login_patient.fill_the_field('FNAME_FLD_ID', params['INPUT'], 'ID')
        login_patient.click_element('SAVE_PTN_DATA_BTN_ID', 'ID')

        err_mess = login_patient.check_elem_is_visible('ER_MESS_FMANE_XP_SYMB', 'XPATH')
        assert err_mess, 'При вводе НЕвалидных данных НЕТ сообщения об ошибке'

    @allure.story('Негативные проверки валидации Имени по макс кол-ву символов')
    @pytest.mark.parametrize('params',
                             dtn.ALLNAME_FLD_MAX_LEN[0],
                             ids=dtn.ALLNAME_FLD_MAX_LEN[1])
    def test_fname_max_len_negot(self, login_patient, params):
        """Негативные проверки валидации Имени по макс кол-ву символов"""
        if not login_patient.check_elem_is_visible('FNAME_FLD_ID', 'ID'):
            login_patient.click_element('PRFL_BTN_XP', 'XPATH')
            login_patient.click_element('PERS_DATA_BTN_ID', 'ID')
        login_patient.clear_element('FNAME_FLD_ID', 'ID')
        login_patient.fill_the_field('FNAME_FLD_ID', params['INPUT'], 'ID')
        login_patient.click_element('SAVE_PTN_DATA_BTN_ID', 'ID')

        err_mess = login_patient.check_elem_is_visible('ER_MESS_FMANE_XP_SYMB', 'XPATH')
        assert err_mess, 'При вводе НЕвалидных данных НЕТ сообщения об ошибке'

    @allure.story('Негативные проверки валидации Имени по типу символов')
    @pytest.mark.parametrize('params',
                             dtn.ALLNAME_FLD_SYMB[0],
                             ids=dtn.ALLNAME_FLD_SYMB[1])
    def test_fname_symb_negot(self, login_patient, params):
        """Негативные проверки валидации Имени по типу символов"""
        if not login_patient.check_elem_is_visible('FNAME_FLD_ID', 'ID'):
            login_patient.click_element('PRFL_BTN_XP', 'XPATH')
            login_patient.click_element('PERS_DATA_BTN_ID', 'ID')
        login_patient.clear_element('FNAME_FLD_ID', 'ID')
        login_patient.fill_the_field('FNAME_FLD_ID', params['INPUT'], 'ID')
        login_patient.click_element('SAVE_PTN_DATA_BTN_ID', 'ID')

        err_mess = login_patient.check_elem_is_visible('ER_MESS_FMANE_XP_SYMB', 'XPATH')
        assert err_mess, 'При вводе НЕвалидных данных НЕТ сообщения об ошибке'

    @allure.story('Негативные проверки валидации на обязательность заполнения поля')
    def test_fname_mandotory_negot(self, login_patient):
        """Негативные проверки валидации на обязательность заполнения поля"""
        if not login_patient.check_elem_is_visible('FNAME_FLD_ID', 'ID'):
            login_patient.click_element('PRFL_BTN_XP', 'XPATH')
            login_patient.click_element('PERS_DATA_BTN_ID', 'ID')
        login_patient.clear_element('FNAME_FLD_ID', 'ID')
        login_patient.click_element('SAVE_PTN_DATA_BTN_ID', 'ID')

        err_mess = login_patient.check_elem_is_visible('ER_MESS_FMANE_XP_MNDTRY', 'XPATH')
        assert err_mess, 'При сохранении незаполненного поля НЕТ сообщения об ошибке'


@allure.feature('Проверки валидации поля Отчество')
class TestPatronField:
    @allure.story('Позитивные проверки валидации Отчества по кол-ву символов')
    @pytest.mark.parametrize('params',
                            dtp.ALLNAME_FLD_LEN_POSSITIVE[0],
                            ids=dtp.ALLNAME_FLD_LEN_POSSITIVE[1])
    def test_patron_len_possit(self, login_patient, params):
        """Позитивные проверки валидации Отчества по кол-ву символов"""
        if not login_patient.check_elem_is_visible('PATRON_FLD_ID', 'ID'):
            login_patient.click_element('PRFL_BTN_XP', 'XPATH')
            login_patient.click_element('PERS_DATA_BTN_ID', 'ID')

        login_patient.clear_element('PATRON_FLD_ID', 'ID')
        login_patient.fill_the_field('PATRON_FLD_ID',  params['INPUT'],'ID')
        login_patient.click_element('SAVE_PTN_DATA_BTN_ID', 'ID')

        err_mess = login_patient.check_elem_is_visible('ER_MESS_PATRON_XP_SYMB', 'XPATH')
        assert not err_mess, 'При вводе валидных данных появляется ошибка'

    @allure.story('Позитивные проверки валидации Отчества по типу символов')
    @pytest.mark.parametrize('params',
                             dtp.ALLNAME_FLD_SYMB_POSSITIVE[0],
                             ids=dtp.ALLNAME_FLD_SYMB_POSSITIVE[1])
    def test_patron_symb_possit(self, login_patient, params):
        """Позитивные проверки валидации Отчества по типу символов"""
        if not login_patient.check_elem_is_visible('PATRON_FLD_ID', 'ID'):
            login_patient.click_element('PRFL_BTN_XP', 'XPATH')
            login_patient.click_element('PERS_DATA_BTN_ID', 'ID')
        login_patient.clear_element('PATRON_FLD_ID', 'ID')
        login_patient.fill_the_field('PATRON_FLD_ID', params['INPUT'], 'ID')
        login_patient.click_element('SAVE_PTN_DATA_BTN_ID', 'ID')

        err_mess = login_patient.check_elem_is_visible('ER_MESS_PATRON_XP_SYMB', 'XPATH')
        assert not err_mess, 'При вводе валидных данных появляется ошибка'

    @allure.story('Позитивные проверки удаления пробелов в начале и в конце')
    @pytest.mark.parametrize('params',
                             dtp.ALLNAME_FLD_SPACE_DELETE[0],
                             ids=dtp.ALLNAME_FLD_SPACE_DELETE[1])
    def test_patron_space_del_possit(self, login_patient, params):
        """Позитивные проверки удаления пробелов в начале и в конце"""
        if not login_patient.check_elem_is_visible('PATRON_FLD_ID', 'ID'):
            login_patient.click_element('PRFL_BTN_XP', 'XPATH')
            login_patient.click_element('PERS_DATA_BTN_ID', 'ID')
        login_patient.clear_element('PATRON_FLD_ID', 'ID')
        login_patient.fill_the_field('PATRON_FLD_ID', params['INPUT'], 'ID')
        login_patient.fill_the_field('FNAME_FLD_ID', 'test', 'ID')
        login_patient.fill_the_field('LNAME_FLD_ID', 'test', 'ID')
        login_patient.fill_the_field('DBIRTH_FLD_ID', '26.02.1999', 'ID')

        login_patient.click_element('SAVE_PTN_DATA_BTN_ID', 'ID')
        login_patient.click_element('PRFL_BTN_XP', 'XPATH')
        login_patient.click_element('PERS_DATA_BTN_ID', 'ID')

        field_fact_data = str(login_patient.get_elem_attr('PATRON_FLD_ID', 'ID', 'text'))
        assert field_fact_data == str(params['INPUT']).strip(), 'Пробелы не удаляются'

    @allure.story('Позитивные проверки сохранения данных в том регистре в каком ввел юзер')
    @pytest.mark.parametrize('params',
                             dtp.ALLNAME_FLD_TEXT_REGISTR[0],
                             ids=dtp.ALLNAME_FLD_TEXT_REGISTR[1])
    def test_patron_registr_input_possit(self, login_patient, params):
        """Позитивные проверки сохранения данных в том регистре в каком ввел юзер"""
        if not login_patient.check_elem_is_visible('PATRON_FLD_ID', 'ID'):
            login_patient.click_element('PRFL_BTN_XP', 'XPATH')
            login_patient.click_element('PERS_DATA_BTN_ID', 'ID')
        login_patient.clear_element('PATRON_FLD_ID', 'ID')
        login_patient.fill_the_field('PATRON_FLD_ID', params['INPUT'], 'ID')
        login_patient.fill_the_field('FNAME_FLD_ID', 'test', 'ID')
        login_patient.fill_the_field('LNAME_FLD_ID', 'test', 'ID')
        login_patient.fill_the_field('DBIRTH_FLD_ID', '26.02.1999', 'ID')

        login_patient.click_element('SAVE_PTN_DATA_BTN_ID', 'ID')
        login_patient.click_element('PRFL_BTN_XP', 'XPATH')
        login_patient.click_element('PERS_DATA_BTN_ID', 'ID')

        field_fact_data = str(login_patient.get_elem_attr('PATRON_FLD_ID', 'ID', 'text'))
        assert field_fact_data == str(params['INPUT']), (f"Введенные данные сохраняются не том регистре, "
                                                         f"в каком ввел юзер, expected: {str(params['INPUT'])}, "
                                                         f"fact: {field_fact_data}")

    @allure.story('Негативные проверки валидации Отчества по мин кол-ву символов')
    @pytest.mark.parametrize('params',
                             dtn.ALLNAME_FLD_MIN_LEN[0],
                             ids=dtn.ALLNAME_FLD_MIN_LEN[1])
    def test_patron_min_len_negot(self, login_patient, params):
        """Негативные проверки валидации Отчества по мин кол-ву символов"""
        if not login_patient.check_elem_is_visible('PATRON_FLD_ID', 'ID'):
            login_patient.click_element('PRFL_BTN_XP', 'XPATH')
            login_patient.click_element('PERS_DATA_BTN_ID', 'ID')

        login_patient.clear_element('PATRON_FLD_ID', 'ID')
        login_patient.fill_the_field('PATRON_FLD_ID', params['INPUT'], 'ID')
        login_patient.click_element('SAVE_PTN_DATA_BTN_ID', 'ID')

        err_mess = login_patient.check_elem_is_visible('ER_MESS_PATRON_XP_SYMB', 'XPATH')
        assert err_mess, 'При вводе НЕвалидных данных НЕТ сообщения об ошибке'

    @allure.story('Негативные проверки валидации Отчества по макс кол-ву символов')
    @pytest.mark.parametrize('params',
                             dtn.ALLNAME_FLD_MAX_LEN[0],
                             ids=dtn.ALLNAME_FLD_MAX_LEN[1])
    def test_patron_max_len_negot(self, login_patient, params):
        """Негативные проверки валидации Отчества по макс кол-ву символов"""
        if not login_patient.check_elem_is_visible('PATRON_FLD_ID', 'ID'):
            login_patient.click_element('PRFL_BTN_XP', 'XPATH')
            login_patient.click_element('PERS_DATA_BTN_ID', 'ID')
        login_patient.clear_element('PATRON_FLD_ID', 'ID')
        login_patient.fill_the_field('PATRON_FLD_ID', params['INPUT'], 'ID')
        login_patient.click_element('SAVE_PTN_DATA_BTN_ID', 'ID')

        err_mess = login_patient.check_elem_is_visible('ER_MESS_PATRON_XP_SYMB', 'XPATH')
        assert err_mess, 'При вводе НЕвалидных данных НЕТ сообщения об ошибке'

    @allure.story('Негативные проверки валидации Отчества по типу символов')
    @pytest.mark.parametrize('params',
                             dtn.ALLNAME_FLD_SYMB[0],
                             ids=dtn.ALLNAME_FLD_SYMB[1])
    def test_patron_symb_negot(self, login_patient, params):
        """Негативные проверки валидации Отчества по типу символов"""
        if not login_patient.check_elem_is_visible('PATRON_FLD_ID', 'ID'):
            login_patient.click_element('PRFL_BTN_XP', 'XPATH')
            login_patient.click_element('PERS_DATA_BTN_ID', 'ID')
        login_patient.clear_element('PATRON_FLD_ID', 'ID')
        login_patient.fill_the_field('PATRON_FLD_ID', params['INPUT'], 'ID')
        login_patient.click_element('SAVE_PTN_DATA_BTN_ID', 'ID')

        err_mess = login_patient.check_elem_is_visible('ER_MESS_PATRON_XP_SYMB', 'XPATH')
        assert err_mess, 'При вводе НЕвалидных данных НЕТ сообщения об ошибке'

    @allure.story('Позитивная проверка валидации на НЕобязательность заполнения поля')
    def test_patron_mandotory_possit(self, login_patient):
        """Позитивная проверка валидации на НЕобязательность заполнения поля"""
        if not login_patient.check_elem_is_visible('PATRON_FLD_ID', 'ID'):
            login_patient.click_element('PRFL_BTN_XP', 'XPATH')
            login_patient.click_element('PERS_DATA_BTN_ID', 'ID')
        login_patient.clear_element('PATRON_FLD_ID', 'ID')
        login_patient.click_element('SAVE_PTN_DATA_BTN_ID', 'ID')

        err_mess = login_patient.check_elem_is_visible('ER_MESS_PATRON_ID', 'ID')
        assert not err_mess, 'При сохранении незаполненного поля появляется сообщение об ошибке'

