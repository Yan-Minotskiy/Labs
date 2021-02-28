n = int(input())
k = 0
for i in range(n):
    s=input()
    if 'кот' in s or 'Кот' in s:
        k = 1
if k == 1:
    print('МЯУ')
else:
    print('НЕТ')
