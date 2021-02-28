n = int(input())
fifo = []
for i in range(n):
    s = input()
    if 'встал в очередь' in s or 'встала в очередь' in s:
        fifo.append(s[:s.find(' встал')])
    if 'будет за тобой' in s:
        f1 = s[8:s.find('!')]
        f2 = s[s.find('!')+2:s.find(' будет за тобой')]
        fifo = fifo[:fifo.index(f1)]+[f1]+[f2]+fifo[fifo.index(f1)+1:]
    if 'хватит тут стоять, пошли отсюда' in s:
        fifo.pop(fifo.index(s[:s.find(', хватит тут стоять, пошли отсюда')]))
print('\n'.join(fifo))
