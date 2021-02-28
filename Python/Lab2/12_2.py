string = input()
n = int(string[0:3].replace(' ', ''))
total = int(string[4:])
su = 0
error_list = []
for i in range(n):
    s = input()
    price = int(s[0:6].replace(' ', ''))
    count = int(s[8:12])
    cost = int(s[13:])
    su += price * count
    if price * count != cost:
        error_list.append(i + 1)
print(total - su)
for j in error_list:
    print(j, end=' ')