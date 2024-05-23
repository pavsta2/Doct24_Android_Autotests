import pytest
import allure
from datetime import timedelta
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
        login_patient.fill_the_field('FNAME_FLD_ID', 'тест', 'ID')
        login_patient.fill_the_field('DBIRTH_FLD_ID', '26.02.1999', 'ID')
        login_patient.fill_the_field('EMAIL_FLD_ID', 'test@test.com', 'ID')

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
        login_patient.fill_the_field('FNAME_FLD_ID', 'тест', 'ID')
        login_patient.fill_the_field('DBIRTH_FLD_ID', '26.02.1999', 'ID')
        login_patient.fill_the_field('EMAIL_FLD_ID', 'test@test.com', 'ID')

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
        """Негативные проверки валидации фамилии по кол-ву символов"""
        if not login_patient.check_elem_is_visible('LNAME_FLD_ID', 'ID'):
            login_patient.click_element('PRFL_BTN_XP', 'XPATH')
            login_patient.click_element('PERS_DATA_BTN_ID', 'ID')

        login_patient.clear_element('LNAME_FLD_ID', 'ID')
        login_patient.fill_the_field('LNAME_FLD_ID', params['INPUT'], 'ID')
        login_patient.fill_the_field('FNAME_FLD_ID', 'тест', 'ID')
        login_patient.fill_the_field('DBIRTH_FLD_ID', '26.02.1999', 'ID')
        login_patient.fill_the_field('EMAIL_FLD_ID', 'test@test.com', 'ID')
        login_patient.click_element('SAVE_PTN_DATA_BTN_ID', 'ID')

        err_mess = login_patient.check_elem_is_visible('ER_MESS_LMANE_XP_MIN', 'XPATH')
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
        login_patient.fill_the_field('FNAME_FLD_ID', 'тест', 'ID')
        login_patient.fill_the_field('DBIRTH_FLD_ID', '26.02.1999', 'ID')
        login_patient.fill_the_field('EMAIL_FLD_ID', 'test@test.com', 'ID')
        login_patient.click_element('SAVE_PTN_DATA_BTN_ID', 'ID')

        err_mess = login_patient.check_elem_is_visible('ER_MESS_LMANE_XP_MAX', 'XPATH')
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
        login_patient.fill_the_field('FNAME_FLD_ID', 'тест', 'ID')
        login_patient.fill_the_field('DBIRTH_FLD_ID', '26.02.1999', 'ID')
        login_patient.fill_the_field('EMAIL_FLD_ID', 'test@test.com', 'ID')
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
        login_patient.fill_the_field('FNAME_FLD_ID', 'тест', 'ID')
        login_patient.fill_the_field('DBIRTH_FLD_ID', '26.02.1999', 'ID')
        login_patient.fill_the_field('EMAIL_FLD_ID', 'test@test.com', 'ID')
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
        login_patient.fill_the_field('LNAME_FLD_ID', 'тест', 'ID')
        login_patient.fill_the_field('DBIRTH_FLD_ID', '26.02.1999', 'ID')
        login_patient.fill_the_field('EMAIL_FLD_ID', 'test@test.com', 'ID')
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
        login_patient.fill_the_field('LNAME_FLD_ID', 'тест', 'ID')
        login_patient.fill_the_field('DBIRTH_FLD_ID', '26.02.1999', 'ID')
        login_patient.fill_the_field('EMAIL_FLD_ID', 'test@test.com', 'ID')
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
        login_patient.fill_the_field('LNAME_FLD_ID', 'тест', 'ID')
        login_patient.fill_the_field('DBIRTH_FLD_ID', '26.02.1999', 'ID')
        login_patient.fill_the_field('EMAIL_FLD_ID', 'test@test.com', 'ID')

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
        login_patient.fill_the_field('LNAME_FLD_ID', 'тест', 'ID')
        login_patient.fill_the_field('DBIRTH_FLD_ID', '26.02.1999', 'ID')
        login_patient.fill_the_field('EMAIL_FLD_ID', 'test@test.com', 'ID')

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
        login_patient.fill_the_field('LNAME_FLD_ID', 'тест', 'ID')
        login_patient.fill_the_field('DBIRTH_FLD_ID', '26.02.1999', 'ID')
        login_patient.fill_the_field('EMAIL_FLD_ID', 'test@test.com', 'ID')
        login_patient.click_element('SAVE_PTN_DATA_BTN_ID', 'ID')

        err_mess = login_patient.check_elem_is_visible('ER_MESS_FMANE_XP_SYMB', 'XPATH')
        assert err_mess, 'При вводе НЕвалидных данных НЕТ сообщения об ошибке'

    @allure.story('Негативные проверки возможности ввода в поле Имя кол-ва символов свыше допустимого')
    @pytest.mark.parametrize('params',
                             dtn.ALLNAME_FLD_MAX_LEN[0],
                             ids=dtn.ALLNAME_FLD_MAX_LEN[1])
    def test_fname_max_len_negot(self, login_patient, params):
        """Негативные проверки возможности ввода в поле Имя кол-ва символов свыше допустимого"""
        if not login_patient.check_elem_is_visible('FNAME_FLD_ID', 'ID'):
            login_patient.click_element('PRFL_BTN_XP', 'XPATH')
            login_patient.click_element('PERS_DATA_BTN_ID', 'ID')
        login_patient.clear_element('FNAME_FLD_ID', 'ID')
        login_patient.fill_the_field('FNAME_FLD_ID', params['INPUT'], 'ID')
        login_patient.fill_the_field('LNAME_FLD_ID', 'тест', 'ID')
        login_patient.fill_the_field('DBIRTH_FLD_ID', '26.02.1999', 'ID')
        login_patient.fill_the_field('EMAIL_FLD_ID', 'test@test.com', 'ID')
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
        login_patient.fill_the_field('LNAME_FLD_ID', 'тест', 'ID')
        login_patient.fill_the_field('DBIRTH_FLD_ID', '26.02.1999', 'ID')
        login_patient.fill_the_field('EMAIL_FLD_ID', 'test@test.com', 'ID')
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

        err_mess = login_patient.check_elem_is_visible('ER_MESS_FMANE_XP_SYMB', "XPATH")
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
        login_patient.fill_the_field('LNAME_FLD_ID', 'тест', 'ID')
        login_patient.fill_the_field('FNAME_FLD_ID', 'тест', 'ID')
        login_patient.fill_the_field('DBIRTH_FLD_ID', '26.02.1999', 'ID')
        login_patient.fill_the_field('EMAIL_FLD_ID', 'test@test.com', 'ID')
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
        login_patient.fill_the_field('LNAME_FLD_ID', 'тест', 'ID')
        login_patient.fill_the_field('FNAME_FLD_ID', 'тест', 'ID')
        login_patient.fill_the_field('DBIRTH_FLD_ID', '26.02.1999', 'ID')
        login_patient.fill_the_field('EMAIL_FLD_ID', 'test@test.com', 'ID')
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
        login_patient.fill_the_field('LNAME_FLD_ID', 'тест', 'ID')
        login_patient.fill_the_field('FNAME_FLD_ID', 'тест', 'ID')
        login_patient.fill_the_field('DBIRTH_FLD_ID', '26.02.1999', 'ID')
        login_patient.fill_the_field('EMAIL_FLD_ID', 'test@test.com', 'ID')

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
        login_patient.fill_the_field('LNAME_FLD_ID', 'тест', 'ID')
        login_patient.fill_the_field('FNAME_FLD_ID', 'тест', 'ID')
        login_patient.fill_the_field('DBIRTH_FLD_ID', '26.02.1999', 'ID')
        login_patient.fill_the_field('EMAIL_FLD_ID', 'test@test.com', 'ID')

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
        login_patient.fill_the_field('LNAME_FLD_ID', 'тест', 'ID')
        login_patient.fill_the_field('FNAME_FLD_ID', 'тест', 'ID')
        login_patient.fill_the_field('DBIRTH_FLD_ID', '26.02.1999', 'ID')
        login_patient.fill_the_field('EMAIL_FLD_ID', 'test@test.com', 'ID')
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
        login_patient.fill_the_field('LNAME_FLD_ID', 'тест', 'ID')
        login_patient.fill_the_field('FNAME_FLD_ID', 'тест', 'ID')
        login_patient.fill_the_field('DBIRTH_FLD_ID', '26.02.1999', 'ID')
        login_patient.fill_the_field('EMAIL_FLD_ID', 'test@test.com', 'ID')
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
        login_patient.fill_the_field('LNAME_FLD_ID', 'тест', 'ID')
        login_patient.fill_the_field('FNAME_FLD_ID', 'тест', 'ID')
        login_patient.fill_the_field('DBIRTH_FLD_ID', '26.02.1999', 'ID')
        login_patient.fill_the_field('EMAIL_FLD_ID', 'test@test.com', 'ID')
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
        login_patient.fill_the_field('LNAME_FLD_ID', 'тест', 'ID')
        login_patient.fill_the_field('FNAME_FLD_ID', 'тест', 'ID')
        login_patient.fill_the_field('DBIRTH_FLD_ID', '26.02.1999', 'ID')
        login_patient.fill_the_field('EMAIL_FLD_ID', 'test@test.com', 'ID')
        login_patient.click_element('SAVE_PTN_DATA_BTN_ID', 'ID')

        err_mess = login_patient.check_elem_is_visible('ER_MESS_PATRON_ID', 'ID')
        assert not err_mess, 'При сохранении незаполненного поля появляется сообщение об ошибке'


@allure.feature('Проверки поля Дата рождения')
class TestBirthField:
    @allure.story('Позитивная проверка открытия модального окна календаря и выбора 15 числа текущего месяца')
    def test_open_calendar(self, login_patient, unlogin_patient):
        """Позитивная проверка открытия модального окна календаря и выбора 15 числа текущего месяца"""
        login_patient.click_element('BTHDY_FLD_ID', 'ID')

        calendar = login_patient.check_elem_is_visible('CLNDR_VIEW_ID', 'ID')
        assert calendar, 'При клике на поле Даты рождения окно календаря не открывается'

        login_patient.click_element('15_TH_OF_CUR_MNTH_XP', 'XPATH')
        login_patient.click_element('CLDR_OK_BTN_ID', 'ID')

        field_data = login_patient.get_elem_attr('BTHDY_FLD_ID', 'ID', 'text')
        assert field_data == '15.' + login_patient.get_cur_month_digit_str() + '.2024', ('Фактическое содержание поля '
                                                                                       'не соответствует выбору')

    @allure.story('Позитивная проверка ввода даты рождения, при которой пациенту ровно 18 лет')
    def test_save_prfl_18_yrs_old(self, login_patient, unlogin_patient):
        """Позитивная проверка ввода даты рождения, при которой пациенту ровно 18 лет"""
        # получаем дату 18 лет назад от текущей
        birthdate_to_test = login_patient.get_date_18_years_ago().strftime("%d.%m.%Y")
        # заполняем поле даты рождения
        login_patient.fill_the_field('BTHDY_FLD_ID', birthdate_to_test, 'ID')
        # заполняем все обязат поля
        login_patient.fill_the_field('FNAME_FLD_ID', 'test', 'ID')
        login_patient.fill_the_field('LNAME_FLD_ID', 'test', 'ID')
        login_patient.fill_the_field('EMAIL_FLD_ID', 'test@test.com', 'ID')

        login_patient.click_element('SAVE_PTN_DATA_BTN_ID', 'ID')

        prfl_btn = login_patient.check_elem_is_visible('PRFL_BTN_XP', 'XPATH')
        assert prfl_btn, "Не удается сохранить профиль с датой рождения, при которой пациенту ровно 18 лет"

    @allure.story('Негативная проверка ввода даты рождения, при которой пациенту меньше 18 лет')
    def test_save_prfl_less_18_yrs_old(self, login_patient, unlogin_patient):
        """Негативная проверка ввода даты рождения, при которой пациенту меньше 18 лет"""
        if not login_patient.check_elem_is_visible('BTHDY_FLD_ID', 'ID'):
            login_patient.click_element('PRFL_BTN_XP', 'XPATH')
            login_patient.click_element('PERS_DATA_BTN_ID', 'ID')
        # получаем дату на 1 день раньше чем 18 лет назад от текущей
        birthdate_to_test = (login_patient.get_date_18_years_ago() + timedelta(days=1)).strftime("%d.%m.%Y")

        # заполняем поле даты рождения
        login_patient.fill_the_field('BTHDY_FLD_ID', birthdate_to_test, 'ID')
        # заполняем все обязат поля
        login_patient.fill_the_field('FNAME_FLD_ID', 'test', 'ID')
        login_patient.fill_the_field('LNAME_FLD_ID', 'test', 'ID')
        login_patient.fill_the_field('EMAIL_FLD_ID', 'test@test.com', 'ID')

        login_patient.click_element('SAVE_PTN_DATA_BTN_ID', 'ID')

        prfl_btn = login_patient.check_elem_is_visible('PRFL_BTN_XP', 'XPATH')
        assert not prfl_btn, "Можно сохранить профиль с датой рождения, при которой пациенту менее 18 лет"

    @allure.story('Негативная проверка ввода даты рождения ранее 1930 года')
    @pytest.mark.parametrize('params',
                             dtn.DBIRTH_FLD_UNVALID[0],
                             ids=dtn.DBIRTH_FLD_UNVALID[1])
    def test_save_prfl_less_1930(self, login_patient, unlogin_patient, params):
        """Негативная проверка ввода даты рождения ранее 1930 года"""
        if not login_patient.check_elem_is_visible('BTHDY_FLD_ID', 'ID'):
            login_patient.click_element('PRFL_BTN_XP', 'XPATH')
            login_patient.click_element('PERS_DATA_BTN_ID', 'ID')
        # заполняем поле даты рождения
        login_patient.fill_the_field('BTHDY_FLD_ID', params['INPUT'], 'ID')
        # заполняем все обязат поля
        login_patient.fill_the_field('FNAME_FLD_ID', 'test', 'ID')
        login_patient.fill_the_field('LNAME_FLD_ID', 'test', 'ID')
        login_patient.fill_the_field('EMAIL_FLD_ID', 'test@test.com', 'ID')

        login_patient.click_element('SAVE_PTN_DATA_BTN_ID', 'ID')

        prfl_btn = login_patient.check_elem_is_visible('PRFL_BTN_XP', 'XPATH')
        assert not prfl_btn, "Можно сохранить профиль с датой рождения ранее 1930 года"


@allure.feature('Проверки поля Email')
class TestEmailField:
    @allure.story('Позитивные проверки валидации поля Email на кол-во символов')
    @pytest.mark.parametrize('params',
                             dtp.EMAIL_FLD_LEN[0],
                             ids=dtp.EMAIL_FLD_LEN[1])
    def test_email_len_posit(self, login_patient, unlogin_patient, params):
        """Позитивные проверки валидации поля Email на кол-во символов"""
        if not login_patient.check_elem_is_visible('EMAIL_FLD_ID', 'ID'):
            login_patient.click_element('PRFL_BTN_XP', 'XPATH')
            login_patient.click_element('PERS_DATA_BTN_ID', 'ID')
        # заполняем поле даты рождения
        login_patient.fill_the_field('EMAIL_FLD_ID', params['INPUT'], 'ID')
        # заполняем все обязат поля
        login_patient.fill_the_field('FNAME_FLD_ID', 'test', 'ID')
        login_patient.fill_the_field('LNAME_FLD_ID', 'test', 'ID')
        login_patient.fill_the_field('BTHDY_FLD_ID', '26.02.1981', 'ID')

        login_patient.click_element('SAVE_PTN_DATA_BTN_ID', 'ID')
        err_mess = login_patient.check_elem_is_visible('ER_MESS_EMAIL_XP', 'XPATH')
        assert not err_mess, 'При сохранении валидных данных появляется сообщение об ошибке'

    @allure.story('Позитивные проверки валидации поля Email по типу символов')
    @pytest.mark.parametrize('params',
                             dtp.EMAIL_FLD_SYMB[0],
                             ids=dtp.EMAIL_FLD_SYMB[1])
    def test_email_symb_posit(self, login_patient, unlogin_patient, params):
        """Позитивные проверки валидации поля Email по типу символов"""
        if not login_patient.check_elem_is_visible('EMAIL_FLD_ID', 'ID'):
            login_patient.click_element('PRFL_BTN_XP', 'XPATH')
            login_patient.click_element('PERS_DATA_BTN_ID', 'ID')
        # заполняем поле даты рождения
        login_patient.fill_the_field('EMAIL_FLD_ID', params['INPUT'], 'ID')
        # заполняем все обязат поля
        login_patient.fill_the_field('FNAME_FLD_ID', 'test', 'ID')
        login_patient.fill_the_field('LNAME_FLD_ID', 'test', 'ID')
        login_patient.fill_the_field('BTHDY_FLD_ID', '26.02.1981', 'ID')

        login_patient.click_element('SAVE_PTN_DATA_BTN_ID', 'ID')
        err_mess = login_patient.check_elem_is_visible('ER_MESS_EMAIL_XP', 'XPATH')
        assert not err_mess, 'При сохранении валидных данных появляется сообщение об ошибке'

    @allure.story('Позитивные проверки удаления пробелов в начале и в конце')
    @pytest.mark.parametrize('params',
                             dtp.EMAIL_FLD_SPACE_DELETE[0],
                             ids=dtp.EMAIL_FLD_SPACE_DELETE[1])
    def test_email_space_del_possit(self, login_patient, params):
        """Позитивные проверки удаления пробелов в начале и в конце"""
        if not login_patient.check_elem_is_visible('EMAIL_FLD_ID', 'ID'):
            login_patient.click_element('PRFL_BTN_XP', 'XPATH')
            login_patient.click_element('PERS_DATA_BTN_ID', 'ID')
            # заполняем поле даты рождения
            login_patient.fill_the_field('EMAIL_FLD_ID', params['INPUT'], 'ID')
            # заполняем все обязат поля
            login_patient.fill_the_field('FNAME_FLD_ID', 'test', 'ID')
            login_patient.fill_the_field('LNAME_FLD_ID', 'test', 'ID')
            login_patient.fill_the_field('BTHDY_FLD_ID', '26.02.1981', 'ID')

        login_patient.click_element('SAVE_PTN_DATA_BTN_ID', 'ID')
        login_patient.click_element('PRFL_BTN_XP', 'XPATH')
        login_patient.click_element('PERS_DATA_BTN_ID', 'ID')

        field_fact_data = str(login_patient.get_elem_attr('EMAIL_FLD_ID', 'ID', 'text'))
        assert field_fact_data == str(params['INPUT']).strip(), 'Пробелы не удаляются'

    @allure.story('Негативные проверки валидации поля Email на мин кол-во символов')
    @pytest.mark.parametrize('params',
                             dtn.EMAIL_FLD_MIN_LEN[0],
                             ids=dtn.EMAIL_FLD_MIN_LEN[1])
    def test_email_min_len_negot(self, login_patient, unlogin_patient, params):
        """Негативные проверки валидации поля Email на мин кол-во символов"""
        if not login_patient.check_elem_is_visible('EMAIL_FLD_ID', 'ID'):
            login_patient.click_element('PRFL_BTN_XP', 'XPATH')
            login_patient.click_element('PERS_DATA_BTN_ID', 'ID')
        # заполняем поле даты рождения
        login_patient.fill_the_field('EMAIL_FLD_ID', params['INPUT'], 'ID')
        # заполняем все обязат поля
        login_patient.fill_the_field('FNAME_FLD_ID', 'test', 'ID')
        login_patient.fill_the_field('LNAME_FLD_ID', 'test', 'ID')
        login_patient.fill_the_field('BTHDY_FLD_ID', '26.02.1981', 'ID')

        login_patient.click_element('SAVE_PTN_DATA_BTN_ID', 'ID')
        err_mess = login_patient.check_elem_is_visible('ER_MESS_EMAIL_XP', 'XPATH')
        assert err_mess, 'При сохранении НЕвалидных данных НЕТ сообщения об ошибке'

    @allure.story('Негативные проверки валидации поля Email на макс кол-во символов')
    @pytest.mark.parametrize('params',
                             dtn.EMAIL_FLD_MAX_LEN[0],
                             ids=dtn.EMAIL_FLD_MAX_LEN[1])
    def test_email_max_len_negot(self, login_patient, unlogin_patient, params):
        """Негативные проверки валидации поля Email на макс кол-во символов"""
        if not login_patient.check_elem_is_visible('EMAIL_FLD_ID', 'ID'):
            login_patient.click_element('PRFL_BTN_XP', 'XPATH')
            login_patient.click_element('PERS_DATA_BTN_ID', 'ID')
        # заполняем поле даты рождения
        login_patient.fill_the_field('EMAIL_FLD_ID', params['INPUT'], 'ID')
        # заполняем все обязат поля
        login_patient.fill_the_field('FNAME_FLD_ID', 'test', 'ID')
        login_patient.fill_the_field('LNAME_FLD_ID', 'test', 'ID')
        login_patient.fill_the_field('BTHDY_FLD_ID', '26.02.1981', 'ID')

        login_patient.click_element('SAVE_PTN_DATA_BTN_ID', 'ID')
        err_mess = login_patient.check_elem_is_visible('ER_MESS_EMAIL_XP', 'XPATH')
        assert err_mess, 'При сохранении НЕвалидных данных НЕТ сообщения об ошибке'

    @allure.story('Негативные проверки валидации поля Email по маске')
    @pytest.mark.parametrize('params',
                             dtn.EMAIL_FLD_MASK[0],
                             ids=dtn.EMAIL_FLD_MASK[1])
    def test_email_mask_negot(self, login_patient, unlogin_patient, params):
        """Негативные проверки валидации поля Email по маске"""
        if not login_patient.check_elem_is_visible('EMAIL_FLD_ID', 'ID'):
            login_patient.click_element('PRFL_BTN_XP', 'XPATH')
            login_patient.click_element('PERS_DATA_BTN_ID', 'ID')
        # заполняем поле даты рождения
        login_patient.fill_the_field('EMAIL_FLD_ID', params['INPUT'], 'ID')
        # заполняем все обязат поля
        login_patient.fill_the_field('FNAME_FLD_ID', 'test', 'ID')
        login_patient.fill_the_field('LNAME_FLD_ID', 'test', 'ID')
        login_patient.fill_the_field('BTHDY_FLD_ID', '26.02.1981', 'ID')

        login_patient.click_element('SAVE_PTN_DATA_BTN_ID', 'ID')
        err_mess = login_patient.check_elem_is_visible('ER_MESS_EMAIL_XP', 'XPATH')
        assert err_mess, 'При сохранении НЕвалидных данных НЕТ сообщения об ошибке'


@allure.feature('Проверки поля Город')
class TestCityField:
    @allure.story('Позитивная проверка перехода в режим поиска и работы поиска')
    @pytest.mark.parametrize('params',
                             dtp.CITY_FLD_SRCH[0],
                             ids=dtp.CITY_FLD_SRCH[1])
    def test_email_mask_negot(self, login_patient, unlogin_patient, params):
        """Позитивная проверка перехода в режим поиска города и работы поиска"""
        if not login_patient.check_elem_is_visible('EMAIL_FLD_ID', 'ID'):
            login_patient.click_element('PRFL_BTN_XP', 'XPATH')
            login_patient.click_element('PERS_DATA_BTN_ID', 'ID')
        login_patient.scroll_and_get_elem_obj()
        login_patient.click_element('CITY_FLD_ID', 'ID')

        # проверяем, что отображается поле поиска городов
        assert login_patient.check_elem_is_visible('CITY_SRCH_FLD_ID', 'ID')

        login_patient.fill_the_field('CITY_SRCH_FLD_ID', params['INPUT'][0], 'ID')

        # проверяем, что выводится 3 ожидаемых результата и не более этих трех
        assert login_patient.check_elem_is_visible('CITY_SRCH_RES_1_XP', 'XPATH'), \
            "В списке результатов поиска нет Владивостока"
        assert login_patient.check_elem_is_visible('CITY_SRCH_RES_2_XP', 'XPATH'), \
            "В списке результатов поиска нет Владикавказа"
        assert login_patient.check_elem_is_visible('CITY_SRCH_RES_3_XP', 'XPATH'), \
            "В списке результатов поиска нет Владимира"
        assert not login_patient.check_elem_is_visible('CITY_SRCH_RES_4_XP', 'XPATH'), \
            "В результатах поиска города более 3 строк"


@allure.feature('Проверки загрузки фото на Аватар')
class TestAvatarUpload:
    def test_avatar_upld_possit(self, login_patient, unlogin_patient):
        """Позитивная проверка загрузки фото на аватар менее 2 мб"""
        img_randon_name = login_patient.get_randon_file_name(5)
        login_patient.push_photo('Images/img.jpg', f'/sdcard/{img_randon_name}.jpg')
        login_patient.click_element('AVTR_UPLD_BTN_ID', 'ID')
        login_patient.click_element('CHS_FROM_GAL_BTN_XP', 'XPATH')
        login_patient.click_element('UPLD_DIR_PHOTO_XP', 'XPATH')
        login_patient.click_element('PHOTO_TO_UPLD_XP', 'XPATH')

        login_patient.screen_shot('avatar_change_possitive.png')
        assert login_patient.check_elem_is_visible('AVTR_UPLD_BTN_ID', 'ID'), ('Фото аватара не '
                                                                               'добавляется успешно')

    def test_avatar_upld_negot(self, login_patient, unlogin_patient):
        """Неготивная проверка загрузки фото на аватар более 2 мб"""
        img_randon_name = login_patient.get_randon_file_name(5)
        login_patient.push_photo('Images/Big_img.jpeg', f'/sdcard/{img_randon_name}.jpg')
        login_patient.click_element('AVTR_UPLD_BTN_ID', 'ID')
        login_patient.click_element('CHS_FROM_GAL_BTN_XP', 'XPATH')
        login_patient.click_element('UPLD_DIR_PHOTO_XP', 'XPATH')
        login_patient.click_element('PHOTO_TO_UPLD_XP', 'XPATH')

        login_patient.screen_shot('avatar_change_negot.png')
        assert not login_patient.check_elem_is_visible('AVTR_UPLD_BTN_ID', 'ID'), ('Фото аватара '
                                                                                   'добавляется без сообщения об ошибке')


@allure.feature('Проверки валидации поля Рост')
class TestHeightField:
    @allure.story('Позитивные проверки валидации поля Рост по кол-ву символов')
    @pytest.mark.parametrize('params',
                            dtp.HEIGHT_FLD[0],
                            ids=dtp.HEIGHT_FLD[1])
    def test_height_len_possit(self, login_patient, params):
        """Позитивные проверки валидации поля Рост по кол-ву символов"""
        if login_patient.check_elem_is_visible('PRFL_BTN_XP', 'XPATH'):
            login_patient.click_element('PRFL_BTN_XP', 'XPATH')
            login_patient.click_element('MED_DATA_BTN_ID', 'ID')

        login_patient.click_element('CHNG_MED_DATA_BTN_ID', 'ID')
        login_patient.clear_element('HEIGHT_FLD_ID', 'ID')
        login_patient.fill_the_field('HEIGHT_FLD_ID', params['INPUT'], 'ID')
        login_patient.fill_the_field('WEIGHT_FLD_ID', '30', 'ID')
        login_patient.click_element('SAVE_PRMTR_BTN_ID', 'ID')

        assert login_patient.check_elem_is_visible('CHNG_MED_DATA_BTN_ID', 'ID'), \
            (f"данные роста не сохраняются, ошибка: "
             f"{login_patient.get_elem_attr('ER_MESS_HEIGHT_FLD_XP', 'XPATH', 'text')}")
        assert login_patient.get_elem_attr('HEIGHT_FLD_V_ID', 'ID', 'text') == params['INPUT'], \
            (f"данные роста сохраняются не так, как ввел юзер. Ожидаем ввод: {params['INPUT']},"
             f"фактический ввод: {login_patient.get_elem_attr('HEIGHT_FLD_V_ID', 'ID', 'text')}")

    @allure.story('Негативные проверки валидации поля Рост по кол-ву символов')
    @pytest.mark.parametrize('params',
                             dtn.HEIGHT_FLD_LEN[0],
                             ids=dtn.HEIGHT_FLD_LEN[1])
    def test_height_len_negot(self, login_patient, params):
        """Негативные проверки валидации поля Рост по кол-ву символов"""
        if login_patient.check_elem_is_visible('PRFL_BTN_XP', 'XPATH'):
            login_patient.click_element('PRFL_BTN_XP', 'XPATH')
            login_patient.click_element('MED_DATA_BTN_ID', 'ID')

        login_patient.click_element('CHNG_MED_DATA_BTN_ID', 'ID')
        login_patient.clear_element('HEIGHT_FLD_ID', 'ID')
        login_patient.fill_the_field('HEIGHT_FLD_ID', params['INPUT'], 'ID')
        login_patient.fill_the_field('WEIGHT_FLD_ID', '30', 'ID')
        login_patient.click_element('SAVE_PRMTR_BTN_ID', 'ID')

        assert login_patient.check_elem_is_visible('ER_MESS_HEIGHT_FLD_XP', 'XPATH'), \
            "При вводе невалидных данных ошибки не появляется"


@allure.feature('Проверки валидации поля Вес')
class TestWeightField:
    @allure.story('Позитивные проверки валидации поля Вес по кол-ву символов')
    @pytest.mark.parametrize('params',
                            dtp.WEIGHT_FLD[0],
                            ids=dtp.WEIGHT_FLD[1])
    def test_weight_len_possit(self, login_patient, params):
        """Позитивные проверки валидации поля Вес по кол-ву символов"""
        if login_patient.check_elem_is_visible('PRFL_BTN_XP', 'XPATH'):
            login_patient.click_element('PRFL_BTN_XP', 'XPATH')
            login_patient.click_element('MED_DATA_BTN_ID', 'ID')

        login_patient.click_element('CHNG_MED_DATA_BTN_ID', 'ID')
        login_patient.clear_element('WEIGHT_FLD_ID', 'ID')
        login_patient.fill_the_field('WEIGHT_FLD_ID', params['INPUT'], 'ID')
        login_patient.fill_the_field('HEIGHT_FLD_ID', '150', 'ID')
        login_patient.click_element('SAVE_PRMTR_BTN_ID', 'ID')

        assert login_patient.check_elem_is_visible('CHNG_MED_DATA_BTN_ID', 'ID'), \
            (f"данные веса не сохраняются, ошибка: "
             f"{login_patient.get_elem_attr('ER_MESS_WEIGHT_FLD_XP', 'XPATH', 'text')}")
        assert login_patient.get_elem_attr('WEIGHT_FLD_V_ID', 'ID', 'text') == params['INPUT'], \
            (f"данные веса сохраняются не так, как ввел юзер. Ожидаем ввод: {params['INPUT']},"
             f"фактический ввод: {login_patient.get_elem_attr('WEIGHT_FLD_V_ID', 'ID', 'text')}")

    @allure.story('Негативные проверки валидации поля Вес по кол-ву символов')
    @pytest.mark.parametrize('params',
                             dtn.WEIGHT_FLD_LEN[0],
                             ids=dtn.WEIGHT_FLD_LEN[1])
    def test_weight_len_negot(self, login_patient, params):
        """Негативные проверки валидации поля Вес по кол-ву символов"""
        if login_patient.check_elem_is_visible('PRFL_BTN_XP', 'XPATH'):
            login_patient.click_element('PRFL_BTN_XP', 'XPATH')
            login_patient.click_element('MED_DATA_BTN_ID', 'ID')

        login_patient.click_element('CHNG_MED_DATA_BTN_ID', 'ID')
        login_patient.clear_element('WEIGHT_FLD_ID', 'ID')
        login_patient.fill_the_field('WEIGHT_FLD_ID', params['INPUT'], 'ID')
        login_patient.fill_the_field('HEIGHT_FLD_ID', '150', 'ID')
        login_patient.click_element('SAVE_PRMTR_BTN_ID', 'ID')

        assert login_patient.check_elem_is_visible('ER_MESS_WEIGHT_FLD_XP', 'XPATH'), \
            "При вводе невалидных данных ошибки не появляется"


@allure.feature('Проверки заполнения поля Группа крови пациента')
class TestBloodField:
    @allure.story('Позитивные проверки заполнения поля Группа крови пациента')
    def test_blood_fld_inp_possit(self, login_patient):
        """Позитивные проверки заполнения поля Группа крови пациента"""
        if login_patient.check_elem_is_visible('PRFL_BTN_XP', 'XPATH'):
            login_patient.click_element('PRFL_BTN_XP', 'XPATH')
            login_patient.click_element('MED_DATA_BTN_ID', 'ID')

        login_patient.click_element('CHNG_MED_DATA_BTN_ID', 'ID')
        login_patient.click_element('BLOOD_FLD_ID', 'ID')
        login_patient.tap_by_coordinates(120, 1155)
        login_patient.fill_the_field('WEIGHT_FLD_ID', '80', 'ID')
        login_patient.fill_the_field('HEIGHT_FLD_ID', '150', 'ID')
        login_patient.click_element('SAVE_PRMTR_BTN_ID', 'ID')

        assert login_patient.check_elem_is_visible('BLOOD_FLD_V_ID', 'ID'), \
            "данные группы крови не сохраняются"
        assert login_patient.get_elem_attr('BLOOD_FLD_V_ID', 'ID', 'text') == 'I-', \
            (f"данные группы крови сохраняются не так, как выбрал юзер. Ожидаем выбор 'I-',"
             f"фактический результат: {login_patient.get_elem_attr('BLOOD_FLD_V_ID', 'ID', 'text')}")







