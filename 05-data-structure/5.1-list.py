# 把列表当栈使用:
stack = list(range(10))
while stack:
    top = stack.pop()
    print(top)
# 列表当队列使用效率很低，使用 collections 的 deque


# 列表推导式
nums = range(1, 6)
squares = [num**2 for num in nums]
print(nums, squares)
# 等价于这个
squares = list(map(lambda x: x**2, nums))
print(nums, squares)
# 利用嵌套推导式打印九九乘法表
multi_table = [
    ' '.join([f'{i}×{j}={i * j}' for j in range(1, i + 1)]) for i in range(1, 10)
]
for line in multi_table:
    print(line)
