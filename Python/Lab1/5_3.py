n = [int(input()), int(input())]
while (n[0] != 0) or (n[1] != 0):
    if int(input())-1:
        n[1] -= int(input())
    else:
        n[0] -= int(input())
    print(*n)
