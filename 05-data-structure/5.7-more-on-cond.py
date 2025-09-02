class MyCls:
    # def __bool__(self):
    #     return True
    def __len__(self):
        return 0


# 条件句可以用任何值（调用bool，优先调用 __bool__，然后调用 __len__）
myCls = MyCls()
if myCls:
    print('True')
else:
    print('False')


# in 和 not in 判断是否在集合中
print(2 in {1, 3, 5}, 2 not in {1, 3, 5})
# is 和 is not 判断是不是同一个对象
person = {'name': 'Lisa'}
person1 = person
print(person is person1, person is not person1)
# not 取反
print(not 2 > 3)

# 比较支持链式操作：a < b == c 校验 a 是否小于 b，且 b 是否等于 c
print(3 > 2 > 2, 3 > 2 and 2 > 2)

# and 和 or 是短路的，并且返回操作数
string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3 or print('111')  # print 不会执行
print(non_null)  # 'Trondheim'

# 序列是是可比较的：依次比较对应位置的元素，直到出结果或者其中一个序列结束（较短的视为更小）
print('ABC' < 'C' < 'Pascal' < 'Python')
