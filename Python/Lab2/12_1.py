n = int(input())
allowed_list = []
for i in range(n):
    allowed_list.append(input())
m = int(input())
requests_list = []
for j in range(m):
    request = input()
    if request in allowed_list:
        requests_list.append(request)
print('\n'.join(requests_list))
