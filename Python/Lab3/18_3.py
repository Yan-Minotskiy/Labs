def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def golden_ratio(x):
    print(fibonacci(x + 1) / fibonacci(x))

