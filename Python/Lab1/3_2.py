a = float(input())
b = float(input())
s = str(input())
if (b == 0 and s == '/') or (s != '+' and s != '-' and s != '*' and s != '/'):
    print('88888888')
else:
    if s == '+':
        print(a + b)
    elif s == '-':
        print(a - b)
    elif s == '*':
        print(a * b)
    elif s == '/':
        print(a / b)