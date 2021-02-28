pile1 = int(input('Введите количество камней в 1 кучке (целое число): '))
pile2 = int(input('Введите количество камней во 2 кучке (целое число): '))
a = -1
while pile1 < 0 or pile1 == 0 or pile2 < 0 or pile2 == 0:
    print('Ошибка. Введите значения больше 0')
    pile1 = int(input())
    pile2 = int(input())
else:
    while pile1 > 0 or pile2 > 0:
        if a == 1:
            b = 0
            while b < 1 or b > 2:
                b = int(input('Введите номер кучки: '))
            c = 0
            if b == 1:
                pile = pile1
            elif b == 2:
                pile = pile2
            while c > pile or c < 1:
                c = int(input('Введите количестово: '))
        elif a == -1:
            if pile1 - pile2 != 0:
                if pile1 - pile2 > 0:
                    b = 1
                elif pile1 - pile2 < 0:
                    b = 2
                c = abs(pile1 - pile2)
            else:
                b = 1
                c = 1
        if b == 1:
            pile1 -= c
        elif b == 2:
            pile2 -= c
        print(pile1, pile2)
        a = -a
    if a == -1:
        print('ПОЛЬЗОВАТЕЛЬ выиграл')
    elif a == 1:
        print('КОМПЬЮТЕР выиграл')