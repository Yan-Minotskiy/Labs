n = int(input())
li = []
for it in range(n):
    li.append(input())
res = []
for l in li:
    i = 0
    try:
        while True:
            if l[i] != ' ':
                break
            res.append(l[i])
            i += 1
        while True:
            if l[i] == "'":
                res.append(l[i])
                i += 1
                while True:
                    if l[i] == '\\':
                        res.append(l[i])
                        i += 1
                        res.append(l[i])
                        i += 1
                        continue
                    if l[i] == "'":
                        res.append(l[i])
                        i += 1
                        break
                    res.append(l[i])
                    i += 1
                continue
            if l[i] == ' ':
                res.append(l[i])
                i += 1
                while l[i] == ' ':
                    i += 1
                continue
            if l[i] == '#':
                break
            res.append(l[i])
            i += 1
    except IndexError:
        pass
    res.append('\n')
print(''.join(res))
