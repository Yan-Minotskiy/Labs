n = int(input())
li = []
for i in range(n):
    li.append(input())
k = int(input())
for j in range(k):
    count = int(input())
    nl = []
    for p in range(count):
        nl.append(li[int(input())-1])
    li = nl
print(*li[:], sep='\n')
