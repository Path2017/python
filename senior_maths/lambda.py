# 匿名函数 lambda - [1, 4, 9, 16, 25, 36, 49, 64, 81]
print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

# 匿名函数lambda x: x * x实际上就是:
def f(x):
    return x * x

# 关键字lambda表示匿名函数，冒号前面的x表示函数参数
