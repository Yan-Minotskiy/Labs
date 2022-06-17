"""
Задание 2
Дано выражение S = A*B*C, A,B,C – заданные целые числа. 
Вместо звёдочек подставить одну из арифметических операций +,-,*, чтобы S= 25. 
Вывести комбинации звёздочек.
"""


def get_comb(a, b, c, s):
    opers = ['+', '-', '*']
    comb = []
    for i in opers:
        for j in opers:
            if eval('a' + i + 'b' + j + 'c==' + str(s)):
                comb.append((i, j))
    return comb


print(get_comb(30, 5, 1, 25))
