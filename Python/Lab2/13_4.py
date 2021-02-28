s = int(input())
skill_first = []
for i in range(s):
    skill_first.append(int(input()))
skill_second = skill_first[:]
n = int(input())
for j in range(n):
    num_man = int(input())
    num_skill = int(input())
    develop = int(input())
    if num_man == 1:
        skill_first[num_skill] = skill_first[num_skill] + develop
    elif num_man == 2:
        skill_second[num_skill] = skill_second[num_skill] + develop
count = 0
for k in range(len(skill_first)):
    if skill_first[k] == skill_second[k]:
        count += 1
for l in skill_first:
    print(l, end=' ')
print()
for m in skill_second:
    print(m, end=' ')
print()
print(count)
