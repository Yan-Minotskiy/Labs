n = int(input())
s_list = []
for i in range(n):
    s = input()
    s = s.replace('%%', '')
    if not s.startswith('####'):
        s_list.append(s)
print('\n'.join(s_list))
