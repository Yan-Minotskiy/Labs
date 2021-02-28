login = input()
email = input()
if '@' not in login and '@' in email:
    print('OK')
elif '@' in login:
    print('Некорректный логин')
    if '@' not in email:
        print('Некорректный адрес')