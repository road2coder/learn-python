# 使用 dict.items 提取字典的 key 和对应的 value
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(f'{k} -> {v}')

# 使用 enumerate 方法提取序列的索引和对应的值
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(f'{i} -> {v}')

# 使用 zip 函数操作多个序列
names = ['Lisa', 'Bob', 'Lucas']
ages = [22, 19, 18]
sexes = ['female', 'male', 'female']
for name, age, sex in zip(names, ages, sexes):
    print(f'{name} -- {age} -- {sex}')

# 此外，可以使用 reversed、sorted 获取反转、排序过后的序列，使用 set 可以去重
