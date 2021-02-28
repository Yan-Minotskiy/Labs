n = int(input())
s = 0
c = 0
for i in range(n):
    iq = int(input())
    s += iq
    c = s / (i + 1)
    if iq > c:
        print('>')
    elif iq < c:
        print('<')
    else:
        print('0')
