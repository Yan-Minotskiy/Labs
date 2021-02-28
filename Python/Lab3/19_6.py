def catalan(n):
    if n == 0:
        return 1
    s = 0
    for i in range(n):
        s += catalan(i) * catalan(n-i-1)
    return s
