n = int(input())
li = []
for i in range(n):
    li.append(input().split(sep=','))
k = int(input())
for i in range(k):
    s = input()
    print(li[int(s[:s.index(',')])][int(s[s.index(',') + 1:])])
