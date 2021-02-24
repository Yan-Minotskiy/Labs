def m(li, p, q):
	X = list(map(lambda x: x[0], li))
	Y = list(map(lambda x: x[1], li))
	x_m = sum(X) / len(X)
	y_m = sum(Y) / len(Y)
	size = len(li)
	s = 0
	for i in range(size):
		s += ((X[i] - x_m) ** p) * ((Y[i] - y_m) ** q)
	return s / size
ex = [
[(2, 1), (5, 1), (5, 7)], #оригинальный треугольник
[(2, 7), (2, 1), (5, 7)], #повернутый на 180 градусов
[(2, 7), (5, 7), (5, 1)], #отраженный треугольник
[(3, 2), (6, 2), (6, 8)], #сдвинутый вправо и вверх
] 

def M1(points):
	return m(points, 2, 0) + m(points, 0, 2)

def M2(points):
	return (m(points, 2, 0) - m(points, 0, 2))**2 + 4*(m(points, 1, 1))**2

def M3(points):
	return (m(points, 3, 0) - 3*(m(points, 1, 2)))**2 + (3*(m(points, 2, 1))+ m(points, 0, 3))**2

def M4(points):
	return (m(points, 3, 0) + m(points, 1, 2)) ** 2 + (m(points, 2, 1) + m(points, 0, 3)) ** 2

def M5(points):
	return (m(points, 3, 0) - 3 * m(points, 1, 2)) * (m(points, 3, 0) + m(points, 1, 2)) * \
                  ((m(points, 3, 0) + m(points, 1, 2)) ** 2 - 3 * (m(points, 2, 1) + m(points, 0, 3))) + \
                  (3 * m(points, 2, 1) - m(points, 0, 3)) * (m(points, 2, 1) + m(points, 0, 3)) * \
                  (3 * (m(points, 3, 0) + m(points, 1, 2)) **
                   2 - (m(points, 2, 1) + m(points, 0, 3)) ** 2)

def M6(points):
	return (m(points, 2, 0) + m(points, 0, 2)) * \
                  ((m(points, 3, 0) + m(points, 1, 2)) ** 2 - (m(points, 2, 1) + m(points, 0, 3)) ** 2) + \
            4 * m(points, 1, 1) * (m(points, 3, 0) + m(points, 1, 2)) * \
            (m(points, 2, 1) + m(points, 0, 3))

def M7(points):
	return (3 * m(points, 2, 1) - m(points, 0, 3)) * (m(points, 3, 0) + m(points, 1, 2)) * \
                  ((m(points, 3, 0) + m(points, 1, 2)) ** 2 - 3 * (m(points, 2, 1) + m(points, 0, 3))) - \
                  (m(points, 3, 0) - 3 * m(points, 1, 2)) * (m(points, 2, 1) + m(points, 0, 3)) * \
                  (3 * (m(points, 3, 0) + m(points, 1, 2)) **
                   2 - (m(points, 2, 1) + m(points, 0, 3)) ** 2)


def test (func, examples):
	for i in examples:
		print(func(i))

test(M2, ex)
