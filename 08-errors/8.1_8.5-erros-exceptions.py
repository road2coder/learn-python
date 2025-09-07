# 语法错误（解析错误）: 比如这里少了一个冒号
# while True print('Hello Python')


# 执行时检测到的错误称为异常
# print(1 / 0) # ZeroDivisionError


# 使用 try except 处理异常
try:
    print(1 / 0)
except ZeroDivisionError:
    print('不可以除以0')

# except 通常需要指定异常类型:
# except Exception: 捕获所有 Exception 及 Exception 派生的异常
# except: 捕获所有异常，可能导致程序无法正常终止, 一般用于兜底日志记录
# except (RuntimeError, TypeError, NameError): 捕获 RuntimeError, TypeError, NameError 及其派生的异常
