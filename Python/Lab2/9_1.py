m, n = int(input()), int(input())
list_library = []
yes_no_list = []
for i in range(m):
    list_library.append(input())
for j in range(n):
    book = input()
    if book in list_library:
        yes_no_list.append(True)
    else:
        yes_no_list.append(False)
for k in yes_no_list:
    if k:
        print('YES')
    else:
        print('NO')
