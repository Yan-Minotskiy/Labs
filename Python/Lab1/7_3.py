count = int(input('Введте количество строк: '))
f = False
while count > 0:
    s = input()
    count -= 1
    if 'Кот' in s or 'кот' in s:
        f = True
if f:
    print('МЯУ')
else:
    print('Нет')
