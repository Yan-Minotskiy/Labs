s, n, c = input(), input(), input()
if n.isdigit() and c.isalpha():
    n = int(n)
    if len(c) > 1 or not (1 <= n <= len(s)):
        print('ОШИБКА')
    elif s[n - 1] == c:
        print('ДА')
    else:
        print('НЕТ')
else:
    print('ОШИБКА')

