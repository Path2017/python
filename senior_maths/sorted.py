# sorted 排序算法

# Python内置的sorted()函数就可以对list进行排序 [-21, -12, 5, 9, 36]
print(sorted([36, 5, -12, 9, -21]))
# sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序
# [5, 9, -12, -21, 36]
print(sorted([36, 5, -12, 9, -21], key=abs))
# 字符串排序 ['Credit', 'Zoo', 'about', 'bob']
print(sorted(['bob', 'about', 'Zoo', 'Credit']))
# 给sorted传入key函数，即可实现忽略大小写的排序 ['about', 'bob', 'Credit', 'Zoo']
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
# 要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True ['Zoo', 'Credit', 'bob', 'about']
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))