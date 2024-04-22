locators = {
    # поля ввода
    # поле ввода номера телефона при авторизации
    'PHONE_FLD_XP': '//*[@resource-id="com.doct24.doct24_android:id/phone_number_field"]',
    # поля ввода кода
    'CODE_1_FLD_ID': 'com.doct24.doct24_android:id/reg_code_edit_text_1',
    'CODE_2_FLD_ID': 'com.doct24.doct24_android:id/reg_code_edit_text_2',
    'CODE_3_FLD_ID': 'com.doct24.doct24_android:id/reg_code_edit_text_3',
    'CODE_4_FLD_ID': 'com.doct24.doct24_android:id/reg_code_edit_text_4',
    # поле ввода фамилии
    'LNAME_FLD_ID': 'com.doct24.doct24_android:id/patient_surname',
    # поле ввода имени
    'FNAME_FLD_ID': 'com.doct24.doct24_android:id/patient_name',
    # поле ввода отчества
    'PATRON_FLD_ID': 'com.doct24.doct24_android:id/patient_patronymic',
    # поле ввода даты рождения
    'DBIRTH_FLD_ID': 'com.doct24.doct24_android:id/patient_birthday',


    # кнопки
    # кнопка далее (авторизация)
    'NEXT_BTN_XP': '//*[@resource-id="com.doct24.doct24_android:id/reg_phone_next_button"]',
    'NEXT_2_BTN_XP': '//*[@resource-id="com.doct24.doct24_android:id/reg_code_next_button"]',
    # кнопка сохранения данных пациента
    'SAVE_PTN_DATA_BTN_ID': 'com.doct24.doct24_android:id/save_patient_button',

    # сообщения об ошибках
    'ER_MESS_LMANE_XP_SYMB': '//*[@resource-id="com.doct24.doct24_android:id/textinput_error" '
                             'and @text="Недопустимо применение символов в Фамилии"]',
    'ER_MESS_FMANE_XP_SYMB': '//*[@resource-id="com.doct24.doct24_android:id/textinput_error" '
                             'and @text="Недопустимо применение символов в Имени"]',
    'ER_MESS_PATRON_XP_SYMB': '//*[@resource-id="com.doct24.doct24_android:id/textinput_error" '
                              'and @text="Недопустимо применение символов в Отчестве"]',
    'ER_MESS_PATRON_ID': 'com.doct24.doct24_android:id/textinput_error',
    'ER_MESS_LMANE_XP_MNDTRY': '//*[@resource-id="com.doct24.doct24_android:id/textinput_error" '
                               'and @text="Необходимо указать фамилию"]',
    'ER_MESS_FMANE_XP_MNDTRY': '//*[@resource-id="com.doct24.doct24_android:id/textinput_error" '
                               'and @text="Необходимо указать имя"]',



    # кнопка профиль в меню
    'PRFL_BTN_XP': '(//*[@resource-id="com.doct24.doct24_android:id/navigation_bar_item_icon_view"])[4]',
    # кнопка Личные данные в Профиле
    'PERS_DATA_BTN_ID': 'com.doct24.doct24_android:id/btn_patient_data',
    # кнопка выхода из профиля
    'PRFL_EXT_BTN_ID': 'com.doct24.doct24_android:id/btn_quit_from_profile',
    # кнопка подждения выхода из профиля
    'PRFL_EXT_CONF_ID': 'com.doct24.doct24_android:id/dialogButtonAccept',

    # сообщения
    # приветствие на стартовом экране
    'HELLO_MSG_ID': 'com.doct24.doct24_android:id/user_greetings',
}