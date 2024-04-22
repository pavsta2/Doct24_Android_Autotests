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