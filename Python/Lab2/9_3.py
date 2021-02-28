n = int(input())
list_name = []
for i in range(n):
    list_name.append(input())
list_same_name = []
count = 0
for name in list_name:
    if list_name.count(name) > 1 and name not in list_same_name:
        count += list_name.count(name)
        list_same_name.append(name)
print(count)
