n = [int(x) for x in input().split()]
print(n)
while (n[0] != 0) or (n[1] != 0) or (n[2] != 0):
    command = int(input())
    if command == 2:
        n[1] -= int(input())
    else:
        if command == 3:
            n[2] -= int(input())
        else:
            n[0] -= int(input())
    print(n[0], n[1], n[2])
