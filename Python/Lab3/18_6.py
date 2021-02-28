def line(s, t):
    if '+' in s:
        equation = float(s[:s.index('x')]) * float(t[:t.index(';')]) + float(s[s.index('+') + 1:])
    else:
        k = s[s.find('x'):]
        equation = float(s[:s.find('x')]) * float(t[:t.find(';')]) + float(k[k.find('-'):])
    if float(t[t.find(';') + 1:]) == equation:
        print(True)
    else:
        print(False)
