birthday_list = []
for i in range(int(input())):
    birthday_list.append(input().split())
for j in range(int(input())):
    m = input()
    for p in birthday_list:
        if p[2] == m:
            print(p[0], p[1], end=' ')
    print()
