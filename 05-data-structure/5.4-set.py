fruits = {'apple', 'apple', 'orange', 'pear'}
print(fruits)  # 不会重复
print('apple' in fruits, 'banana' in fruits)
# 创建空集合，{} 用于创建空字典
empty_set = set()
a = set('abracadabra')  # {'a', 'r', 'b', 'c', 'd'}
b = set('alacazam')  # {'z', 'a', 'c', 'm', 'l'}
print(a - b)  # 存在于 a 中但不存在于 b 中的
print(a | b)  # 存在于 a 或 b 中、或同时存在于 a、b 中的
print(a & b)  # 同时存在于 a 和 b 中的
print(a ^ b)  # 存在于 a 或 b 中、但不同时存在于 a、b 中的

# 集合推导式
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)
