m = int(input())
products = []
for i in range(m):
    products.append(input())
n = int(input())
recipes = []
recipes_products = []
for j in range(n):
    recipes.append(input())
    products_count = int(input())
    recipes_products.append([])
    for k in range(products_count):
        recipes_products[j].append(input())
count = 0
for recipe in recipes_products:
    flag = True
    for product in recipe:
        if product not in products:
            flag = False
            break
    if flag:
        print(recipes[count])
    count += 1
