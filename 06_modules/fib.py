def fib(n: int):
    if n < 0:
        raise ValueError(f'无效的索引: {n}')
    a, b, i = 0, 1, 0
    while i < n:
        a, b, i = b, a + b, i + 1
    return a


print(__name__)
