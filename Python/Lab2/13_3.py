n = int(input())
li = [0]
for i in range(2, n+1):
    k = 0
    for j in range(len(li)):
        if li[j] == li[-1-j]:
            k += 1
    li.append(k)
for l in li:
    print(l)
