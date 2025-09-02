# range 生成等差数列 range(start, end, step) 含 start 不含 end
for i in range(5):
    print(i)

print(list(range(5)))
print(list(range(0, 10, 3)))
print(list(range(10, 0, -3)))

# 类似于 enumerate 的效果
words = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(words)):
    print(i, words[i])
for i, word in enumerate(words):
    print(i, word)
