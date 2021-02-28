s = input()
li = s[s.index('?') + 1:].split('&')
d = dict()
for i in li:
    a = i.split('=')
    d[a[0]] = a[1]
k = input()
print(d.get(k))
