n, s = int(input()), input()
k = 0
for i in s:
    if ord('А') <= ord(i) <= ord('Я'):
        if ord('А') <= ord(i) + n <= ord('Я'):
            s = s[0:k] + chr(ord(i) + n) + s[k + 1:]
        else:
            s = s[0:k] + chr(ord(i) + n-32) + s[k + 1:]
    if ord('а') <= ord(i) <= ord('я'):
        if ord('а') <= ord(i) + n <= ord('я'):
            s = s[0:k] + chr(ord(i) + n) + s[k + 1:]
        else:
            s = s[0:k] + chr(ord(i) + n-32) + s[k + 1:]
    k += 1
print(s)
