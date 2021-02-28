znak = "q"
first = 1
last = 1000
n = last // 2
count = 0
while znak != "=":
    print(n)
    znak = input()
    if znak == "<":
        first = n
        n = last - (last - first + 1) // 2
    if znak == ">":
        last = n
        n = first + (last - first + 1) // 2
    count += 1
print("Ваше загадонное число = ", n, count)
