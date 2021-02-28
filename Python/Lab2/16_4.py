n = int(input())
price_list = [[]]
for i in range(1, n):
    price_list.append(input().split())
    if len(price_list[i]) != i:
        print('Ошибка ввода', price_list)
for j in range(len(price_list)):
    price_list[j] = [int(item) for item in price_list[j]]
a, b = input().split()
a, b = int(a), int(b)
if a > b:
    p = price_list[a][b]
else:
    p = price_list[b][a]
l = []

# не доделана
