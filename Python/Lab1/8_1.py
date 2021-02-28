y = int(input())
x = int(input())
for i in range(x):
    for j in range(y):
        print((y - j) / (i + 1), end='\t')
    print()
