print('Как дела?')
ans = input()
if 'хорош' in ans and 'не' not in ans and '?' not in ans:
    print('Отлично, у меня тоже все хорошо!')
elif 'плох' in ans and 'не' not in ans and '?' not in ans:
    print('Ничего, скоро всё наладится.')
else:
    print('Я вас решительно не понимаю.')
