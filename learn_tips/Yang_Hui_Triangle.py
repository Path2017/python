# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]

# 杨辉三角 line：行数:

def triangles(max):
    L = [1]
    n = 0
    while n < max:
        yield L
        L.append(0)
        L = [L[i - 1] + L[i] for i in range(len(L))]
        n = n + 1
    return 'finish'

tr = triangles(10)
while True:
  try:
    n = next(tr)
    print(n)
  except StopIteration as e:
    print('Generator return value:', e.value)
    break