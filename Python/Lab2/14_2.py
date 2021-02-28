password_list = []
users_list = []
name_list = []
flag = False
while True:
    info = input()
    if info == '':
        break
    user = info[0:info.index(':')]
    name = ''
    password = ''
    count = 0
    k = 0
    for i in info:
        if count == 4 and k < info.index(','):
            name += i
        if count == 1 and i != ':':
            password += i
        if i == ':':
            count += 1
        k += 1
    users_list.append(user)
    password_list.append(password)
    name_list.append(name)
s = input()
usual_password = s.split(';')
k = 0
for p in password_list:
    if p in usual_password:
        print('To:', users_list[k])
        print(name_list[k], ', ваш пароль слишком простой, смените его.', sep='')
    k += 1
