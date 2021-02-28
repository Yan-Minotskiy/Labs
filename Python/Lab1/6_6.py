c = int(input())
s = 0
pi = 3.141592653589793
for i in range(1, c + 1):
    s += (1 / i ** 2)
itog = (pi ** 2) / s
print(itog)
