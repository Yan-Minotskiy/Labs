a = [int(input())]
buy, sell, i = 0, 0, 0
while a[i] != 0:
    i += 1
    a.append(int(input()))
    if a[i - 1] < a[i] and buy == 0:
        buy = a[i]
    if a[i - 1] > a[i] and buy != 0 and sell == 0:
        sell = a[i]
print(buy, sell, sell - buy)
