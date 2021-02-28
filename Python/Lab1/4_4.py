x = input()
y = input()
if len(x) < 8:
    print('Короткий!')
elif '123' in x:
    print('Простой!')
elif x != y:
    print('Различаются!')
else:
    print('Ok')
