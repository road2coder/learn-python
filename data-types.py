# 数字类型
zero: int = 0
pi: float = 3.14159265
com: complex = 1 - 1j
print(zero, zero, com)

# 布尔类型
flag: bool = True
print(flag)
flag = False
print(flag)

# 字符串
s: str = "hello"
print(s, len(s), f"{s} python")
print(f"pi ≈ {pi:.2f}")

# 列表
lst: list = [123, 321, "abc"]
print(lst)
lst.append("cba")
print(lst)
nums: list[int] = [123, 321]
numbers = [1, 2, 3, 4, 5]
print(numbers)
squares = [x**2 for x in numbers]
print(squares)
squares = list(map(lambda x: x**2, numbers))
print(squares)

# 元组
t: tuple[str, int] = ("Bob", 18)
print(t)

# 集合
ids: set[int] = {123, 31, 123}
print(ids)
print(ids, 321 in ids)
sexes = frozenset({"男", "女"})
print(sexes, "男" in sexes)

# 范围
r1: range = range(3, 5)
print(r1)
r2 = range(0, 9, 2)
for i in r2:
    print(i)
print(list(r2))

# 字典
person = {"name": "Bob", "age": 18}
print(person)
print(person["name"])  # 不存在会报错
person["sex"] = "男"
print(person)
