# python math()函数

L = [1,2,3,4,5]
def f(x):
  return x*x

r = map(f,L)
# 结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list
sum = list(r)
print(sum)

# else
print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))