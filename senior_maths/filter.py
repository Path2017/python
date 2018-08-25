# filter 在一个list中，删掉偶数，只保留奇数，可以这么写
def is_odd(x):
    return x % 2 == 1
r = list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
print(r)

# 把一个序列中的空字符串删掉
# filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list
def not_empty(s):
  return s and s.strip()
sum = list(filter(not_empty,['A','B','',None,' ']))
print(sum)
