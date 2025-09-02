tel = {'jack': 4098, 'sape': 4139}
print(tel)
# 添加/修改
tel['lisa'] = 1166
print(tel)
# 删除 key
del tel['sape']
print(tel)
print('jack' in tel, 'bob' in tel, 'bob' not in tel)

# 从列表构建字典
grades = dict([('Lisa', 100), ('Bob', 98), ('Lucas', 59)])
print(grades)

# 从关键字参数构建
grades = dict(Lisa=100, Bob=98)
print(grades)

# 从推导式构建
squares = {x: x**2 for x in range(1, 5)}
print(squares)
