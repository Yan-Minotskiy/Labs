import random

n, count = 100000, 0
for i in range(n):
    x, y = random.random(), random.random()
    if y ** 2 + x ** 2 <= 1:
        count += 1
print(count / n * 4)
