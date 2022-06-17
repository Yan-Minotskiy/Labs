"""
Задание №1.

Составить программу для определения, 
какое количество информации несет сообщение о том, 
что горит красный и желтый сигнал светофора, 
среднее количество информации о том, 
что загорелся любой из трех сигналов.
"""

import math

k = {
    'green': 108,
    'yellow': 4,
    'red': 16
}

# расчитывет вероятность наступления события
def get_p(color, color_dict):
    return color_dict[color] / sum(color_dict.values())

# находит количество информации, которое несёт сообщение, когда загорается определённый сигнал
def get_i(color, color_dict):
    return math.ceil(math.log2(1/get_p(color, color_dict)))

# возвращает среднее количество информации полученное при выборе любого из сигналов
def get_h(color_dict):
    return sum(get_p(item, color_dict) * get_i(item, color_dict) for item in color_dict.keys())

print(get_h(k))

