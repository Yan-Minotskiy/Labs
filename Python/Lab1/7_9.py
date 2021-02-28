while True:
    a, zn = int(input()), input()
    if zn == 'x' or zn == '!':
        if zn == 'x':
            print(a)
            break
        f = 1
        while a > 1:
            f *= a
            a -= 1
        print(f)
    else:
        b = int(input())
        if zn == '+':
            print(a + b)
        elif zn == '-':
            print(a - b)
        elif zn == '*':
            print(a * b)
        elif zn == '/':
            print(a // b)
        elif zn == '%':
            print(a % b)
