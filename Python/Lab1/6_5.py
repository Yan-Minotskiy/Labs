num, denum = 0, 1
for i in range(int(input())):
    a, b = int(input()), int(input())
    num = num * b + a * denum
    denum *= b
x, y = num, denum
while y > 0:
    x, y = y, x % y
print(num // x, '/', denum // x, sep='')
