# Данные для негативных проверок

# Данные для полей Имя, Фамилия, Отчество
ALLNAME_FLD_MIN_LEN = (
                        [
                            {'INPUT': 's'}
                        ],
                        [
                            '1 letter'
                        ]
                       )

ALLNAME_FLD_MAX_LEN = (
                        [
                            {'INPUT': 'ИвановскийИвановскийИвановскийИвановскийИвановскийN'},
                            {'INPUT': 'ИвановскийИвановскийИвановскийИвановскийИвановскийИвановский'}
                        ],
                        [
                            '51 letters',
                            '60 letters'
                        ]
                       )

ALLNAME_FLD_SYMB = (
                        [
                            {'INPUT': '12345'},
                            {'INPUT': 'Иванов!'},
                            {'INPUT': 'Иванов@'},
                            {'INPUT': 'Иванов#'},
                            {'INPUT': 'Иванов$'},
                            {'INPUT': 'Иванов%'},
                            {'INPUT': 'Иванов^'},
                            {'INPUT': 'Иванов&'},
                            {'INPUT': 'Иванов*'},
                            {'INPUT': 'Иванов('},
                            {'INPUT': 'Иванов)'},
                            {'INPUT': 'Иванов_'},
                            {'INPUT': 'Иванов+'},
                            {'INPUT': 'Иванов='},
                        ],
                        [
                            'Digits',
                            'Symbol !',
                            'Symbol @',
                            'Symbol #',
                            'Symbol $',
                            'Symbol %',
                            'Symbol ^',
                            'Symbol &',
                            'Symbol *',
                            'Symbol (',
                            'Symbol )',
                            'Symbol _',
                            'Symbol +',
                            'Symbol =',
                        ]
                       )