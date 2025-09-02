nums = [1, 99, 100, -3, -5]
print(nums)
del nums[0]
print(nums)
# 仅保留一个
del nums[1:]
print(nums)

fruits = {'apple', 'apple', 'orange', 'pear'}
# 可以删除整个变量
del fruits

person = {'name': 'Bob', 'age': 18}
del person['name']
print(person)
