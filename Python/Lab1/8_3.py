bull, cow, calf = [1], [0], [0]
subsidy, cattle = int(input()), int(input())
s_s, s_c, k = subsidy, cattle, 0

while bull[k] < s_c and bull[k] * 20 < subsidy:
    subsidy -= 20 * bull[k]
    cattle -= bull[k]
    calf[k] = (10 * cattle - subsidy) // 5
    cow[k] = cattle - calf[k]
    if calf[k] > cattle and cow[k] < 0:
        bull[k] += 1
        continue
    else:
        bull.append(bull[k] + 1)
        cow.append(0)
        calf.append(0)
        k += 1
        subsidy = s_s
        cattle = s_c

for i in range(k):
    print(bull[i], ' ', cow[i], ' ', calf[i])
