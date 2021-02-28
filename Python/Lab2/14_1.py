n = int(input())
li_1 = []
for i in range(n):
    a = input()
    if 'лук' not in a:
        li_1.append(a)
print(', '.join(li_1))
