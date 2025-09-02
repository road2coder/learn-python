# 定义函数


# 斐波那契数列  0-based
from typing import Any, Sequence


def fib(n: int):
    if n < 0:
        raise ValueError(f'无效的索引: {n}')
    a, b, i = 0, 1, 0
    while i < n:
        a, b, i = b, a + b, i + 1
    return a


for i in range(0, 10):
    print(fib(i))


# 默认参数
def join(lst: Sequence[Any], sep='-'):
    result = ''
    for item in lst:
        if result != '':
            result += sep
        result += str(item)
    return result


lst = ['2022', '12', '07']
# 关键字参数
print(join(lst), join(lst, sep='/'))


# 特殊参数: / 前的是仅位置参数， / 和 * 之间的是位置或关键字参数， * 后面的是仅关键字参数
def foo(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
    print(pos1, pos2, pos_or_kwd, kwd1, kwd2)


foo('p1', 'p2', pos_or_kwd='234', kwd1='kwd1', kwd2='kwd2')
foo('p1', 'p2', '234', kwd1='kwd1', kwd2='kwd2')


# *posArgs 接收位置参数(元组)
def bar(*posArgs):
    print(posArgs)


# **kwdArgs 接收关键字参数(字典)
def boo(**kwdArgs):
    print(kwdArgs)


# 可以混合使用， *posArgs 必须在 **kwdArgs 前面
def mixed(*posArgs, **kwdArgs):
    print(posArgs, kwdArgs)


bar(1, 2, 3)
boo(name='abc', age=18)
# 传参时也要求位置参数在关键字参数前面
mixed('hello', 123, name='Bob', age=21)


# 任意数量的参数
def concat(*args, sep='-'):
    return sep.join(args)


print(concat('Hello', 'Python', sep=' '))


# 解包位置参数
def bar1(p1, p2):
    print(p1, p2)


# 解包位置参数
def boo1(name, age):
    print(name, age)


bar1(*(1, 2))
boo1(**{'name': 'Bob', 'age': 18})
