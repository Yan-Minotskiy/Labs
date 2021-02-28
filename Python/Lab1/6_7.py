n = int(input())
s = 0
for i in range(n):
    if i % 2 == 0:
        s += int(input())
    else:
        s -= int(input())
print(s)
