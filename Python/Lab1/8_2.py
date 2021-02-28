x = int(input())
y = int(input())
s = input()
for i in range(x):
    for j in range(y):
        if i == 0 or j == 0 or i == x - 1 or j == y - 1:
            print(s, end='')
        else:
            print(end=' ')
    print()
