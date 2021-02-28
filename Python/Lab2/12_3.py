n = int(input())
shop_list = []
for i in range(n):
    product = input()
    count = input()
    shop_list.append(product+' '+count)
print('\n'.join(shop_list[-1::-1]))
