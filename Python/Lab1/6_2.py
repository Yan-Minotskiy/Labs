space = int(input())
sign = 1
while space > 0:
    print(' ' * space + '*' * sign)
    sign += 2
    space -= 1
