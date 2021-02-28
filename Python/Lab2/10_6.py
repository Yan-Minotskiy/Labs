s, x, xm = input(), 0, 0
way, = s[0]
for i in s[1:]:
    if i == '>':
        x += 1
        way = way[:x] + s[0] + way[x + 1:]
    elif i == '<':
        x -= 1
        way = way[:x] + s[0] + way[x + 1:]
    elif i == 'V':
        print(way)
        way = x * ' ' + s[0]
print(way)
