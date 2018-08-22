import math
# 求绝对值的函数：
def my_abs(x):
  if x >= 0:
    return x
  else:
    return -x
print(my_abs(-99))

# math包
# pi
print(math.pi)
# 求平方根
print(math.sqrt(2))
# 定义计算x平方函数
def power(x):
  return x*x
print(power(5))
# 定义计算 x的n次方的函数
def powern(x,n):
  s = 1
  while n > 0:
    n = n-1
    s = s * x
  return s
print(powern(2,3))
