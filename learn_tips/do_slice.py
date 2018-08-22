# 切片:
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# 取前3个元素，应该怎么做 --['Michael', 'Sarah', 'Tracy']
print([L[0], L[1], L[2]])
# 取前N个元素，也就是索引为0-(N-1)的元素，可以用循环： --['Michael', 'Sarah']
r = []
n = 2
for i in range(n):
  r.append(L[i])
print(r)
# 对这种经常取指定索引范围的操作，用循环十分繁琐，因此，Python提供了切片（Slice）操作符，能大大简化这种操作
# 对应上面的问题，取前3个元素，用一行代码就可以完成切片：--L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素。
print(L[0:3])
# 如果第一个索引是0，还可以省略
print(L[:3])


