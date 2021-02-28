def month_name(n, s):
    list_en_month = ['january', 'february', 'marсh', 'april', 'may', 'june', 'jule', 'august', 'september', 'november',
                     'december']
    list_ru_month = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь',
                     'ноябрь', 'декабрь']
    if s == 'en':
        return list_en_month[n - 1]
    elif s == 'ru':
        return list_ru_month[n - 1]
    else:
        return 'Error'
