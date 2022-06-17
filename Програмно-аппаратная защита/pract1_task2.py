"""
Задание №2

Составить программу, которая кодирует строку любой длины, 
составляет кодовый словарь и выводит закодированное сообщение.
"""

import math

# извлекает из строки алфавит уникальных символов
def get_alpha(s):
    return list(set(s))

# расчитывает необходимое количество бит для кодирования алфавита из n символов
def shennon(n):
    return math.ceil(math.log2(n))

# получает словарь - кодовую таблицу в двоичной системе для символов из строки s
def get_alphabet(s):
    alpha_list = get_alpha(s)
    r = shennon(len(alpha_list))
    return {alpha_list[x]: str(bin(x))[2:].zfill(r) for x in range(len(alpha_list))}


s = input()
print(get_alphabet(s))
