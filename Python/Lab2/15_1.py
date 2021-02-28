c = input()
s = input()
words = ' '.join(s.split()).split(' ')
for w in words:
    if c.lower() in w or c.upper() in w:
        print(w)
