# 高级特性 - 生成器
# list
L = [x * x for x in range(10)]
print(L)

# 生成器
g = (x * x for x in range(10))
next(g)

for n in g:
  print(n)

# 斐波拉契数列（Fibonacci）除第一个和第二个数外，任意一个数都可由前两个数相加得到：
# 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
def fib(max):
  n,a,b = 0,0,1
  while n<max:
    print(b)
    a,b=b,a+b
    n=n+1
  return 'done'
fib(5)

# 注意，赋值语句：
# a, b = b, a + b
# 相当于：
# t = (b, a + b) # t是一个tuple
# a = t[0]
# b = t[1]









