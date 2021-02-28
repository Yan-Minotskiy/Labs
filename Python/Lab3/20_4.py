base = ['список имён']


def hello(name):
    print('Здравствуйте, ', name, '! Вашу карту ищут...', sep='')


def search_card(name):
    global base
    if name in base:
        print('Ваша карта с номером', base.index(name) + 1, 'найдена.')
    else:
        print('Ваша карта не найдена.')
