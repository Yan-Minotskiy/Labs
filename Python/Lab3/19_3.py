def roots_of_quadratic_equation(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                return ["all"]
            else:
                return []
        else:
            return [-c / b]
    else:
        d = b * b - 4 * a * c
        if d > 0:
            return [(-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)]
        elif d == 0:
            return [-b / 2 * a]
        else:
            return []
