# 递归函数 n! = 1 x 2 x 3 x ... x n
def fn(n):
  if n ==1:
    return 1
  else:
    return n*fn(n-1)
print(fn(5))