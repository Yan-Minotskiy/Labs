count, f, s = int(input()), False, ''
while count > 0:
    s = input()
    if 'Кот' in s or 'кот' in s:
        f = True
    if 'Пёс' in s or 'пёс' in s:
        f = False
    count -= 1
if f:
    print('МЯУ')
else:
    print('НЕТ')
