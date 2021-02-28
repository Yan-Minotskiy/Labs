n = int(input())
list_legion = []
list_kills = []
for i in range(n):
    list_legion.append(input())
    list_kills.append(i + 1)
k = int(input())
j = 1
while True:
    list_kills.pop(j - 1)
    print(list_legion[j - 1])
    if j + k <= n:
        j += k
    elif len(list_kills) != 0:
        j = list_kills[0]
    else:
        break
