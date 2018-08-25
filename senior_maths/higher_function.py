# 高阶函数
# 求绝对值 abs(-10)是函数调用，而abs是函数本身
num = abs(-10)
print(num)

# 变量可以指向函数
f = abs
num2 = f(-20)
print(num2)

# 传入函数 数值的绝对值相加:
def add(x, y, f):
    return f(x)+f(y)
print(add(4,-3,abs))
