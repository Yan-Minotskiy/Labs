m = int(input())
dishes = []
for i in range(m):
    dishes.append(input())
n = int(input())
for j in range(n):
    count = int(input())
    for k in range(count):
        dish = input()
        if dish in dishes:
            dishes.pop(dishes.index(dish))
print('\n'.join(dishes))
