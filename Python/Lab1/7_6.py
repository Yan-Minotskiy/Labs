xc, yc, x, y, s, n, g, f = int(input()), int(input()), 0, 0, '', 0, 0, True
while True:
    s = input()
    if xc == x and yc == y and f:
        f = False
    if f:
        n += 1
    if s == 'стоп':
        break
    g = int(input())
    if s == 'север':
        y += g
        continue
    if s == 'юг':
        y -= g
        continue
    if s == 'восток':
        x += g
        continue
    if s == 'запад':
        x -= g
        continue
print(n)
