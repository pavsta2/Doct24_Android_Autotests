from Pages.profile_page import ProfilePage


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
    # поле Дата рождения
    'BTHDY_FLD_ID': 'com.doct24.doct24_android:id/patient_birthday',
    # окно календаря
    'CLNDR_VIEW_ID': 'android:id/month_view',
    # поле email
    'EMAIL_FLD_ID': 'com.doct24.doct24_android:id/patient_email',
    # поле Город
    'CITY_FLD_ID': 'com.doct24.doct24_android:id/patient_city',
    # поле поиска города
    'CITY_SRCH_FLD_ID': 'android:id/search_src_text',
    # поле результатов поиска Города
    'CITY_SRCH_RES_FLD_ID': 'com.doct24.doct24_android:id/cities_recyclerview',
    # локаторы списка результата поиска городов
    'CITY_SRCH_RES_1_XP': '//*[@resource-id="com.doct24.doct24_android:id/tv_title" and @text="Владивосток"]',
    'CITY_SRCH_RES_2_XP': '//*[@resource-id="com.doct24.doct24_android:id/tv_title" and @text="Владикавказ"]',
    'CITY_SRCH_RES_3_XP': '//*[@resource-id="com.doct24.doct24_android:id/tv_title" and @text="Владимир"]',
    'CITY_SRCH_RES_4_XP': '//*[@resource-id="com.doct24.doct24_android:id/cities_recyclerview"]/android.view.ViewGroup[4]',
    # поле Роста в Медицинских данных при редактировании
    'HEIGHT_FLD_ID': 'com.doct24.doct24_android:id/etHeight',
    # поле Роста в Медицинских данных при просмотре
    'HEIGHT_FLD_V_ID': 'com.doct24.doct24_android:id/tv_patient_height',
    # поле Роста в Медицинских данных при редактировании
    'WEIGHT_FLD_ID': 'com.doct24.doct24_android:id/etWeight',
    # поле Роста в Медицинских данных при просмотре
    'WEIGHT_FLD_V_ID': 'com.doct24.doct24_android:id/tv_patient_weight',
    # поле группы крови в Медицинских данных при редактировании
    'BLOOD_FLD_ID': 'com.doct24.doct24_android:id/etBloodType',
    # поле группы крови в Медицинских данных при просмотре
    'BLOOD_FLD_V_ID': 'com.doct24.doct24_android:id/tv_patient_blood_type',

    # кнопки
    # кнопка далее (авторизация)
    'NEXT_BTN_XP': '//*[@resource-id="com.doct24.doct24_android:id/reg_phone_next_button"]',
    'NEXT_2_BTN_XP': '//*[@resource-id="com.doct24.doct24_android:id/reg_code_next_button"]',
    # кнопка сохранения данных пациента
    'SAVE_PTN_DATA_BTN_ID': 'com.doct24.doct24_android:id/save_patient_button',
    # кнопка выбора 15 чиса текущего месяца на календаре
    '15_TH_OF_CUR_MNTH_XP': '//android.view.View[@content-desc="15 ' + ProfilePage.get_cur_month_rus_str() + ' 2024"]',
    # кнопка сохранения выбора даты календаря
    'CLDR_OK_BTN_ID': 'android:id/button1',
    # кнопка загрузки Аватара
    'AVTR_UPLD_BTN_ID': 'com.doct24.doct24_android:id/btn_change_profile_avatar',
    # кнопка "Выбрать из галереии" при загрузке аватара
    'CHS_FROM_GAL_BTN_XP': '//*[@resource-id="android:id/text1" and @text="Выбрать из галереи"]',
    # директория загруженных фото в смартфоне
    'UPLD_DIR_PHOTO_XP': '//android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]',
    # последнее загруженное фото внутри директории
    'PHOTO_TO_UPLD_XP': '//android.view.ViewGroup[@bounds="[0,493][264,757]"]',
    # кнопка Медицинские данные в Профиле
    'MED_DATA_BTN_ID': 'com.doct24.doct24_android:id/btn_medical_data',
    # кнопка Изменить в разделе Медицинские данные
    'CHNG_MED_DATA_BTN_ID': 'com.doct24.doct24_android:id/parametersEditButton',
    # кнопка сохранения Параметров Медицинских данныхс
    'SAVE_PRMTR_BTN_ID': 'com.doct24.doct24_android:id/saveParametresButton',

    # сообщения об ошибках
    # сообщение об ошибке валидации поля Фамилия
    'ER_MESS_LMANE_XP_SYMB': '//*[@resource-id="com.doct24.doct24_android:id/textinput_error" and '
                             '@text="Поле может содержать символы алфавита, пробел, дефис"]',
    # сообщение об ошибке НЕзаполненности Фамилии
    'ER_MESS_LMANE_XP_MNDTRY': '(//*[@resource-id="com.doct24.doct24_android:id/textinput_error"])[1]',
    # сообщение об ошибке минимальной длины Фамилии
    'ER_MESS_LMANE_XP_MIN': '//*[@resource-id="com.doct24.doct24_android:id/textinput_error" and '
                            '@text="В поле должно быть минимум 2 символа"]',
    # сообщение об ошибке максимальной длины Фамилии
    'ER_MESS_LMANE_XP_MAX': '//*[@resource-id="com.doct24.doct24_android:id/textinput_error" and '
                            '@text="В поле должно быть максимум 50 символов"]',
    # сообщение об ошибке валидации поля Имя
    'ER_MESS_FMANE_XP_SYMB': '//android.widget.TextView[@resource-id="com.doct24.doct24_android:id/textinput_error"]',
    # сообщение об ошибке валидации поля Отчество
    'ER_MESS_PATRON_ID': 'com.doct24.doct24_android:id/textinput_error',

    # сообщение об ошибке Незаполненности Имени
    'ER_MESS_FMANE_XP_MNDTRY': '//*[@resource-id="com.doct24.doct24_android:id/textinput_error" '
                               'and @text="Необходимо указать имя"]',
    # сообщение об ошибке валидации поля Email
    'ER_MESS_EMAIL_XP': '//*[@resource-id="com.doct24.doct24_android:id/textinput_error" and '
                        '@text="Укажите верный E-mail или оставьте поле пустым"]',
    # сообщения о доступе приложения
    'PERMIS_MESS_ID': 'com.android.permissioncontroller:id/permission_message',
    # сообщение об ошибке валидации поля Роста пациента
    'ER_MESS_HEIGHT_FLD_XP': '//android.widget.TextView[@bounds="[84,497][996,540]"]',
    # сообщение об ошибке валидации поля Веса пациента
    'ER_MESS_WEIGHT_FLD_XP': '//android.widget.TextView[@bounds="[84,712][996,755]"]',



    # кнопка профиль в меню
    'PRFL_BTN_XP': '(//*[@resource-id="com.doct24.doct24_android:id/navigation_bar_item_icon_view"])[4]',
    # кнопка Личные данные в Профиле
    'PERS_DATA_BTN_ID': 'com.doct24.doct24_android:id/btn_patient_data',
    # кнопка выхода из профиля
    'PRFL_EXT_BTN_ID': 'com.doct24.doct24_android:id/btn_quit_from_profile',
    # кнопка подждения выхода из профиля
    'PRFL_EXT_CONF_ID': 'com.doct24.doct24_android:id/dialogButtonAccept',
    # кнопка Разрешить при использовании приложения
    'FOREGRND_ONLY_BTN_ID': 'com.android.permissioncontroller:id/permission_allow_foreground_only_button',
    # кнопка разрешить
    'ALLOW_BTN_ID': 'com.android.permissioncontroller:id/permission_allow_button',

    # сообщения
    # приветствие на стартовом экране
    'HELLO_MSG_ID': 'com.doct24.doct24_android:id/user_greetings',
}

