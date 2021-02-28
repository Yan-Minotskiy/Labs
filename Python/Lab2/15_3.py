s = input()
num = []
for c in s:
    num.append(s.count(c))
print(max(num))
