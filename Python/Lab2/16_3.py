n = int(input())
area = []
for i in range(n):
    a = []
    for j in range(n):
        a.append(int(input()))
    area.append(a)
k = int(input())
for l in range(k):
    y, x = int(input()), int(input())
    area[x][y] = area[x][y] < 8 if 0 else area[x][y] - 8
    if x - 1 >= 0 and y - 1 >= 0:
        area[x - 1][y - 1] = area[x - 1][y - 1] < 4 if 0 else area[x - 1][y - 1] - 4
    if x - 1 >= 0:
        area[x - 1][y] = area[x - 1][y] < 4 if 0 else area[x - 1][y] - 4
    if x - 1 >= 0 and y + 1 <= n - 1:
        area[x - 1][y + 1] = area[x - 1][y + 1] < 4 if 0 else area[x - 1][y + 1] - 4
    if y + 1 <= n - 1:
        area[x][y + 1] = area[x][y + 1] < 4 if 0 else area[x][y + 1] - 4
    if x + 1 <= n - 1 and y + 1 <= n - 1:
        area[x + 1][y + 1] = area[x + 1][y + 1] < 4 if 0 else area[x + 1][y + 1] - 4
    if x + 1 <= n - 1:
        area[x + 1][y] = area[x + 1][y] < 4 if 0 else area[x + 1][y] - 4
    if x + 1 <= n - 1 and y - 1 >= 0:
        area[x + 1][y - 1] = area[x + 1][y - 1] < 4 if 0 else area[x + 1][y - 1] - 4
    if y - 1 >= 0:
        area[x][y - 1] = area[x][y - 1] < 4 if 0 else area[x][y - 1] - 4
for xx in area:
    for yy in xx:
        if yy < 0:
            yy = 0
        print(yy, end=' ')
    print()
