s = input()
sn, k = s[0], 1
for i in s[1:]:
    if sn == i:
        k += 1
    else:
        print(k, sn)
        k, sn = 1, i
print(k, sn)
