"""
Задание 1
Дан двумерный массив n, m. 
Найти индексы всех различных пар элементов сумма которых больше чем 25.
"""

#функция для предотвращения двойных проверок
def exclusion_duplicates(ij, kl):
    i, j = ij
    k, l = kl
    if i < k:
        return True
    if i == k:
        return j < l
    return False


def find_index(array, sum_digit):
    n = len(array)
    m = len(array[0])
    comb = []
    for i in range(n):
        for j in range(m):
            for k in range(n):
                for l in range(m):
                    if exclusion_duplicates((i, j), (k, l)) and array[i][j] + array[k][l] > sum_digit:
                        comb.append(((i, j), (k, l)))
    return comb


# пример
print(find_index([[1, 1, 2, 3],
                  [23, 4, 3, 1],
                  [0, 1, 1, -8]], 25))
