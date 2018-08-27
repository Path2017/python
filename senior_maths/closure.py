# 闭包: 返回的函数在其定义内部引用了局部变量args，所以，当一个函数返回了一个函数后，其内部的局部变量还被新函数引用，所以，闭包用起来简单，实现起来可不容易
def count():
  fs = []
  for i in range(1, 4):
    def f():
      return i*i
    fs.append(f)
  return fs

f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())

# 上述函数方法 输出的结果均为9 应修改为以下方式
def count2():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
h1,h2,h3 = count2()
print(h1())
print(h2())
print(h3())
