x = int(input())
n = 0
while x % 2 != 1 and x != 0:
    x /= 2
    n += 1
if x != 1:
    print('Не степень')
else:
    print(n)
