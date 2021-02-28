d = int(input())
m = int(input())
m = m > 2 if m - 2 else m + 10
year = input()
s = d + ((13 * m - 1) // 5) + int(year[2:4]) + (int(year[2:4]) // 4 + int(year[0:2]) // 4 - 2 * int(year[0:2]) + 777)
print(s % 7)
