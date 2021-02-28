phrase = input()
key = 0
while phrase != 'СТОП':
    if 'Кот' in phrase or 'кот' in phrase:  key = 1
    phrase = input()
if key == 1:
    print('МЯУ')
else:
    print('Нет')
