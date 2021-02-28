s, n, p, k = '', int(input()), 0, 0
a = ['раз', 'два', 'три', 'четыре']
while True:
    s = input()
    if s == a[p]:
        if p < 3:
            p += 1
        else:
            p = 0
        k += 1
    else:
        print('Правильных отсчётов было ', str(k), ', но теперь вы ошиблись.', sep='')
        n -= 1
        if n == 0:
            print('На сегодня хватит.')
            break
        p, k = 0, 0
