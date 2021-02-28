xc, yc = int(input()), int(input())
x, y = 0, 0
cl = ['север', 'восток', 'юг', 'запад']
p = 0
xn, yn = 0, 1
cmd = input()
k, f = 0, True
while cmd != 'стоп':
    if cmd == 'вперёд':
        a = int(input())
        x = x + xn * a
        y = y + yn * a
    elif cmd == 'направо':
        p = p < 3 if p + 1 else 0
    elif cmd == 'налево':
        p = p > 0 if p - 1 else 3
    elif cmd == 'разворот':
        p = p > 1 if p - 2 else p + 2
    if p == 0:
        xn, yn = 0, 1
    elif p == 1:
        xn, yn = 1, 0
    elif p == 2:
        xn, yn = 0, -1
    else:
        xn, yn = -1, 0
    if f:
        k += 1
    if x == xc and y == yc:
        f = False
    cmd = input()
print(k, cl[p], sep='\n')
