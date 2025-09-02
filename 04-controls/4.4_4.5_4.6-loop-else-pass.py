# break 用于跳出当前循环
# continue 用于跳过循环的剩余部分，进入下一次迭代

# 循环中的 else: 如果循环正常执行完毕(没有遭遇 break) 提前退出，就会执行 else 的内容
nums = [1, 0, 3, 5, 7, 9]
for num in nums:
    if num % 2 == 0:
        print('nums 中有偶数')
        break
else:
    print('nums 中没有偶数')

# pass 用于占位，通常为了需要缩进的地方不报错
if True:
    pass
