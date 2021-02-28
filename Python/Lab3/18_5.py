def equation(a, b):
    x1, x2, y1, y2 = float(a[:a.index(';')]), float(b[:b.index(';')]), float(a[a.index(';') + 1:]), float(
        b[b.index(';') + 1:])
    if x2 - x1 == 0:
        k, c = 0, x2
    else:
        k = (y2 - y1) / (x2 - x1)
        c = y2 - k * x2
    if k == 0:
        print(c)
    else:
        print(k, c)
