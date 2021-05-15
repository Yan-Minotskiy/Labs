import random
from string import ascii_uppercase


def prima(W, city_labels = None):
    """
    Алгоритм Прима для нахождения сети дорог минимальной длины
    Дискретная алгебра, приложение 1
    """

    _ = float('inf')
    cities_count = len(W)

    # проверка на размерость таблицы связей
    for weights in W:
        assert len(weights) == cities_count

    # генерация имен городов
    if not city_labels:
        city_labels = [ascii_uppercase[x] for x in range(cities_count)]

    assert cities_count <= len(city_labels)

    # выбор начального города
    free_vertexes = list(range(len(city_labels)))

    starting_vertex = random.choice(free_vertexes)
    tied = [starting_vertex]
    free_vertexes.remove(starting_vertex)

    print('Started with %s' % city_labels[starting_vertex])

    road_length = 0

    a, b, c, d, e = (1, 1, 1, 2, 2) 

    # пока есть свободные вершины
    while free_vertexes:
        min_link = None  # соединение, образующее минимальный путь
        overall_min_path = _    # минимальный путь среди всех возможных

        # проход по всем уже связанным дорогой вершинам
        for current_vertex in tied:
            weights = W[current_vertex]   # связи текущей вершины с другими

            min_path = _
            free_vertex_min = current_vertex

            # проход по связанным городам
            for vertex in range(cities_count):
                vertex_path = weights[vertex]
                if vertex_path == 0:
                    continue

                if vertex in free_vertexes and vertex_path < min_path:
                    free_vertex_min = vertex
                    min_path = vertex_path

            if (
                free_vertex_min != current_vertex
                and overall_min_path > min_path
            ):
                min_link = (current_vertex, free_vertex_min)
                overall_min_path = min_path
        try:
            path_length = W[min_link[0]][min_link[1]]
        except TypeError:
            print('Unable to find path')
            return

        print('Connecting %s to %s [%s]' % (city_labels[min_link[0]], city_labels[min_link[1]], path_length))

        road_length += path_length
        free_vertexes.remove(min_link[1])
        tied.append(min_link[1])

    print('Road length: %s' % road_length)
    print(f'\nA - class {a}\nB - class {b}\nC - class {c}\nD - class {d}\nE - class {e}')

if __name__ == '__main__':

    _ = float('inf')

    W = [
        #A  B  C  D  E
        [0, 11, 9, 7, 8], # A
        [11, 0, 15, 14, 13], # B
        [9, 15, 0, 12, 14], # C
        [7, 14, 12, 0, 6], # D
        [8, 13, 14, 6, 0], # E
    ]

    prima(W)