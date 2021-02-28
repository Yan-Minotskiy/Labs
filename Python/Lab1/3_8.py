x = int(input())
print(max(x % 10 + x % 100 // 10, x % 100 // 10 + x // 100), min(x % 10 + x % 100 // 10, x % 100 // 10 + x // 100),
      sep='')
