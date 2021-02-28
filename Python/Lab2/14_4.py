s = input()
num = s.split()
n = [int(i) for i in num]
print('*' * (len(n) + 2))
for i in range(max(n)):
    print('*', end='')
    for j in n:
        if j >= len(n) - i:
            print('*', end='')
        else:
            print(' ', end='')
    print('*')
print('*' * (len(n) + 2))
