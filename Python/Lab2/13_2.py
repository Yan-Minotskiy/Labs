n = int(input())
digits = []
for i in range(n):
    digits.append(int(input()))
digits.sort(reverse=True)
for j in digits:
    print(j)
