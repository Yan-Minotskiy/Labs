import statistics

n = int(input())
stat = []
med = []
mod = []
for i in range(n):
    s = input()
    num = s.split()
    num = [int(j) for j in num]
    for nu in num:
        stat.append(nu)
    med.append(statistics.median(num))
    mod.append(statistics.mode(num))
med_med = statistics.median(med)
mod_mod = statistics.mode(mod)
med = [str(k) for k in med]
mod = [str(l) for l in mod]
print(' '.join(med))
print(' '.join(mod))
print(med_med)
print(mod_mod)
print(statistics.median(stat))
print(statistics.mode(stat))
