# Тестовые данные для проверки позитивных сценариев
# Данные для полей Имя, Фамилия, Отчество (у них одинаковые требования)
ALLNAME_FLD_LEN_POSSITIVE = (
                        [
                            {'INPUT': 'ива'},
                            {'INPUT': 'ив'},
                            {'INPUT': 'ИвановскийИвановскийИвановскийИвановскийИвановски'},
                            {'INPUT': 'ИвановскийИвановскийИвановскийИвановскийИвановский'}
                        ],
                        [
                            '3 letters',
                            '2 letters',
                            '49 letters',
                            '50 letters',
                        ]
                       )
ALLNAME_FLD_SYMB_POSSITIVE = (
                        [
                            {'INPUT': 'Иванов'},
                            {'INPUT': 'Ivanov'},
                            {'INPUT': 'Иванов-Петров'},
                            {'INPUT': 'Ivanov-petrov'},
                            {'INPUT': 'Иванов Петров'},
                            {'INPUT': 'Ivanov Petrov'}],
                        [
                            'russian symbols',
                            'eng symbols',
                            'russian symbol and -',
                            'eng symbols and -',
                            'russian symbol and space',
                            'eng symbols and space'
                         ]
                        )
ALLNAME_FLD_SPACE_DELETE = (
                        [
                            {'INPUT': '  Иванов'},
                            {'INPUT': 'Иванов  '}
                        ],
                        [
                            'with left space',
                            'with right space'
                         ],
                        )

ALLNAME_FLD_TEXT_REGISTR = (
                        [
                            {'INPUT': 'ИвAнOв'}
                        ],
                        [
                            'wright textregistr field save'
                         ],
                        )

# Данные для поля E-mail
EMAIL_FLD_LEN = (
                        [
                            {'INPUT': 'i@f.ru'},
                            {'INPUT': 'i@fo.ru'},
                            {'INPUT': 'ivanofffffivanofffffivanofffffivanofffffivanofffffivanofffff@info.com'},
                            {'INPUT': 'ivanofffffivanofffffivanofffffivanofffffivanofffffivanofffff@infoo.com'},
                            {'INPUT': 'ivanofffffivanofffff@infoo.com'}
                        ],
                        [
                            '6 symbols',
                            '7 symbols',
                            '69 symbols',
                            '70 symbols',
                            '30 symbols'
                         ]
                        )

EMAIL_FLD_SYMB = (
                        [
                            {'INPUT': 'eng@domain.ru'},
                            {'INPUT': '1234@domain.ru'},
                            {'INPUT': '12-34@domain.ru'},
                            {'INPUT': '12_34@domain.ru'}
                        ],
                        [
                            'eng symbols as username in email',
                            'digits as username in email',
                            'dash (-) in email',
                            'underlining (_) in email'
                         ]
                        )

EMAIL_FLD_SPACE_DELETE = (
                        [
                            {'INPUT': '  mail@mail.ru'},
                            {'INPUT': 'mail@mail.ru  '}
                        ],
                        [
                            'with left space',
                            'with right space'
                         ],
                        )

# Данные для поиска города
CITY_FLD_SRCH = (
                        [
                            {'INPUT': ["Влад", "Владивосток", "Владикавказ", "Владимир"]},
                        ],
                        [
                            'Search for "vlad"'
                         ],
                        )

# Данные для поля Рост
HEIGHT_FLD = (
                        [
                            {'INPUT': '3'},
                            {'INPUT': '99'},
                            {'INPUT': '199'}
                        ],
                        [
                            '1 symbol',
                            '2 symbols',
                            '3 symbols'
                         ],
                        )

# Данные для поля Вес
WEIGHT_FLD = (
                        [
                            {'INPUT': '9'},
                            {'INPUT': '99'},
                            {'INPUT': '199'}
                        ],
                        [
                            '1 symbol',
                            '2 symbols',
                            '3 symbols'
                         ],
                        )

# Данные для поля Аллерген
ALLERGEN_FLD_LEN = (
                        [
                            {'INPUT': '12'},
                            {'INPUT': 'abc'},
                            {'INPUT': '12345qwer'},
                            {'INPUT': '12345qwert12345qwert12345qwert12345qwert12345qwer'},
                            {'INPUT': '12345qwert12345qwert12345qwert12345qwert12345qwert'},

                        ],
                        [
                            '2 symbol',
                            '3 symbols',
                            '10 symbols',
                            '49 symbols',
                            '50 symbols'
                         ],
                        )

ALLERGEN_FLD_SYMB = (
                        [
                            {'INPUT': '12'},
                            {'INPUT': 'Abc'},
                            {'INPUT': 'Абв'},
                            {'INPUT': "-.,:;!?\|/{}[]'“`#&$%@^*()+_< >"},
                            {'INPUT': '阪市立学鎰命'},
                            {'INPUT': 'ﷵ ﷵ ﷵ ﷵ'}
                        ],
                        [
                            'digits',
                            'eng letters',
                            'rus letters',
                            'not letters with space',
                            'hieroglyphs',
                            'arabic'
                         ],
                        )

# Данные для поля Реакция
REACTION_FLD_LEN = (
                        [
                            {'INPUT': '12'},
                            {'INPUT': 'abc'},
                            {'INPUT': '12345qwer'},
                            {'INPUT': '12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert'
                                      '12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert'
                                      '12345qwert12345qwert12345qwert12345qwer'},
                            {'INPUT': '12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert'
                                      '12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert'
                                      '12345qwert12345qwert12345qwert12345qwert'},

                        ],
                        [
                            '2 symbol',
                            '3 symbols',
                            '10 symbols',
                            '199 symbols',
                            '200 symbols'
                         ],
                        )

REACTION_FLD_SYMB = (
                        [
                            {'INPUT': '12'},
                            {'INPUT': 'Abc'},
                            {'INPUT': 'Абв'},
                            {'INPUT': "-.,:;!?\|/{}[]'“`#&$%@^*()+_< >"},
                            {'INPUT': '阪市立学鎰命'},
                            {'INPUT': 'ﷵ ﷵ ﷵ ﷵ'}
                        ],
                        [
                            'digits',
                            'eng letters',
                            'rus letters',
                            'not letters with space',
                            'hieroglyphs',
                            'arabic'
                         ],
                        )

# Данные для поля Операции
SURGERIES_FLD_LEN = (
                        [
                            {'INPUT': '12'},
                            {'INPUT': 'abc'},
                            {'INPUT': '12345qwer'},
                            {'INPUT': '12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert'
                                      '12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert'
                                      '12345qwert12345qwert12345qwert12345qwer'},
                            {'INPUT': '12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert'
                                      '12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert'
                                      '12345qwert12345qwert12345qwert12345qwert'},

                        ],
                        [
                            '2 symbol',
                            '3 symbols',
                            '10 symbols',
                            '199 symbols',
                            '200 symbols'
                         ],
                        )

SURGERIES_FLD_SYMB = (
                        [
                            {'INPUT': '12'},
                            {'INPUT': 'Abc'},
                            {'INPUT': 'Абв'},
                            {'INPUT': "-.,:;!?\|/{}[]'“`#&$%@^*()+_< >"},
                            {'INPUT': '阪市立学鎰命'},
                            {'INPUT': 'ﷵ ﷵ ﷵ ﷵ'}
                        ],
                        [
                            'digits',
                            'eng letters',
                            'rus letters',
                            'not letters with space',
                            'hieroglyphs',
                            'arabic'
                         ],
                        )

# Данные для поля Год операции
SURGERIE_YEAR_FLD = (
                        [
                            {'INPUT': '1950'},
                            {'INPUT': '2001'},
                            {'INPUT': '2024'}
                        ],
                        [
                            '1950 lowest border of range',
                            '2001 midle of range',
                            '2024 highest border of range'
                         ],
                        )

# Данные для поля Препарат
MEDICATION_FLD_LEN = (
                        [
                            {'INPUT': '12'},
                            {'INPUT': 'abc'},
                            {'INPUT': '12345qwer'},
                            {'INPUT': '12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345'
                                      'qwert12345qwert12345qwer'},
                            {'INPUT': '12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345'
                                      'qwert12345qwert12345qwert'},

                        ],
                        [
                            '2 symbol',
                            '3 symbols',
                            '10 symbols',
                            '99 symbols',
                            '100 symbols'
                         ],
                        )

MEDICATION_FLD_SYMB = (
                        [
                            {'INPUT': '12'},
                            {'INPUT': 'Abc'},
                            {'INPUT': 'Абв'},
                            {'INPUT': "-.,:;!?\|/{}[]'“`#&$%@^*()+_< >"},
                            {'INPUT': '阪市立学鎰命'},
                            {'INPUT': 'ﷵ ﷵ ﷵ ﷵ'}
                        ],
                        [
                            'digits',
                            'eng letters',
                            'rus letters',
                            'not letters with space',
                            'hieroglyphs',
                            'arabic'
                         ],
                        )

# Данные для поля Дозировка
DOSAGE_FLD_LEN = (
                        [
                            {'INPUT': '12'},
                            {'INPUT': 'abc'},
                            {'INPUT': '12345qwer'},
                            {'INPUT': '12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345'
                                      'qwert12345qwert12345qwer'},
                            {'INPUT': '12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345'
                                      'qwert12345qwert12345qwert'},

                        ],
                        [
                            '2 symbol',
                            '3 symbols',
                            '10 symbols',
                            '99 symbols',
                            '100 symbols'
                         ],
                        )

DASAGE_FLD_SYMB = (
                        [
                            {'INPUT': '12'},
                            {'INPUT': 'Abc'},
                            {'INPUT': 'Абв'},
                            {'INPUT': "-.,:;!?\|/{}[]'“`#&$%@^*()+_< >"},
                            {'INPUT': '阪市立学鎰命'},
                            {'INPUT': 'ﷵ ﷵ ﷵ ﷵ'}
                        ],
                        [
                            'digits',
                            'eng letters',
                            'rus letters',
                            'not letters with space',
                            'hieroglyphs',
                            'arabic'
                         ],
                        )

# Данные для поля Периодичность приема
FREQ_OF_TKNG_FLD_LEN = (
                        [
                            {'INPUT': '12'},
                            {'INPUT': 'abc'},
                            {'INPUT': '12345qwer'},
                            {'INPUT': '12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345'
                                      'qwert12345qwert12345qwer'},
                            {'INPUT': '12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345'
                                      'qwert12345qwert12345qwert'},

                        ],
                        [
                            '2 symbol',
                            '3 symbols',
                            '10 symbols',
                            '99 symbols',
                            '100 symbols'
                         ],
                        )

FREQ_OF_TKNG_FLD_SYMB = (
                        [
                            {'INPUT': '12'},
                            {'INPUT': 'Abc'},
                            {'INPUT': 'Абв'},
                            {'INPUT': "-.,:;!?\|/{}[]'“`#&$%@^*()+_< >"},
                            {'INPUT': '阪市立学鎰命'},
                            {'INPUT': 'ﷵ ﷵ ﷵ ﷵ'}
                        ],
                        [
                            'digits',
                            'eng letters',
                            'rus letters',
                            'not letters with space',
                            'hieroglyphs',
                            'arabic'
                         ],
                        )

# Данные для поля Хронические заболевания
CHRON_DES_FLD_LEN = (
                        [
                            {'INPUT': '12'},
                            {'INPUT': 'abc'},
                            {'INPUT': '12345qwer'},
                            {'INPUT': '12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345'
                                      'qwert12345qwert12345qwer'},
                            {'INPUT': '12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345qwert12345'
                                      'qwert12345qwert12345qwert'},

                        ],
                        [
                            '2 symbol',
                            '3 symbols',
                            '10 symbols',
                            '99 symbols',
                            '100 symbols'
                         ],
                        )

CHRON_DES_FLD_SYMB = (
                        [
                            {'INPUT': '12'},
                            {'INPUT': 'Abc'},
                            {'INPUT': 'Абв'},
                            {'INPUT': "-.,:;!?\|/{}[]'“`#&$%@^*()+_< >"},
                            {'INPUT': '阪市立学鎰命'},
                            {'INPUT': 'ﷵ ﷵ ﷵ ﷵ'}
                        ],
                        [
                            'digits',
                            'eng letters',
                            'rus letters',
                            'not letters with space',
                            'hieroglyphs',
                            'arabic'
                         ],
                        )

# Данные для поля Год обнаружения
CHRON_DISC_YEAR_FLD = (
                        [
                            {'INPUT': '1950'},
                            {'INPUT': '2001'},
                            {'INPUT': '2024'}
                        ],
                        [
                            '1950 lowest border of range',
                            '2001 midle of range',
                            '2024 highest border of range'
                         ],
                        )