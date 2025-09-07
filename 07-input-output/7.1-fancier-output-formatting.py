import math
import json


# f-string

# 浮点数保留位数
print(f'π保留两位小数：{math.pi:.2f}')
# 使用最小宽度对齐
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
[print(f'{k:10}=>{v:10}') for k, v in table.items()]

# < 3.6 可以使用 format 函数实现

# 使用位置参数
print('π保留两位小数：{0:.2f}'.format(math.pi))
# 使用关键字参数
print('π保留两位小数：{pi:.2f}'.format(pi=math.pi))
# 0 - format 的第一个参数, [Jack] - 对应参数的 Jack 这个 key， :d 输出格式
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; Dcab: {0[Dcab]:d}'.format(table))
# 利用 ** 将 table 变为关键字参数
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))

# 更老的版本可以使用 format % values https://docs.python.org/zh-cn/3.13/library/stdtypes.html#old-string-formatting


# 文件操作

# 文件打开了就一定要关闭，所以很麻烦
f = None
try:
    f = open('pyproject.toml', 'r')
    data = f.read()
    print(data)
except FileNotFoundError:
    print('文件不存在！')
finally:
    # 如果文件成功打开，可以关闭文件
    if f is not None:
        f.close()

# 使用 with 可以让操作变得简单
with open('pyproject.toml', 'r', encoding='utf-8') as f:
    data = f.read()
    print(data)


# file通过实现 __enter__ 和 __exit__ 方法，自动获取资源，自己定义的对象也可以
class MyResource:
    def __enter__(self):
        print('获取资源')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('释放资源', exc_type, exc_val, exc_tb, end='\t')
        # 返回 True 会忽略异常
        return False


with MyResource() as r:
    print('使用资源')
    # raise Exception("测试异常")  # 异常会被传递出去


# 文件对象是可迭代的, 每次返回一行，存在非 ascii 字符时需要指定编码
with open('test.txt', 'r+', encoding='utf-8') as f:
    for line_number, line in enumerate(f, start=1):
        print(f'第 {line_number} 行: {line}', end='')
        f.write('这是在代码中写入的行\n')


# json 模块可以实现简单的序列化和反序列化
x = [1, 'simple', True]
print(json.dumps(x))
with open('test.json', 'r+', encoding='utf-8') as f:
    x = json.load(f)
    print(type(x))
