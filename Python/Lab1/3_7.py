x = int(input())
li = []
for i in range(3):
    li.append(x % 10)
    x //= 10
li.sort()
if (li[0] + li[2]) / 2 == li[1]:
    print('Вы ввели красивое число.')
else:
    print('Жаль, вы ввели обычное число.')
