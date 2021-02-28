p, n, s = -1, 0, ''
while s != 'СТОП':
    s = input()
    n += 1
    if ('Кот' in s or 'кот' in s) and p == -1:
        p = n
print(p)
