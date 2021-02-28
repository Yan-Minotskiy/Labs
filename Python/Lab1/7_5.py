p, n, s, c = -1, 0, '', 0
while s != 'СТОП':
    s = input()
    n += 1
    if 'Кот' in s or 'кот' in s:
        c += 1
        if p == -1:
            p = n
print(c, p)
