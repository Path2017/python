#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 第1行注释可以让这个文件直接在Unix/Linux/Mac上运行
# 第2行注释表示.py文件本身使用标准UTF-8编码

'a test module'
# 模块的文档注释 可利用 __doc__ 进行访问
__author__ = 'cris.liu'
import sys

def test():
  args = sys.argv
  if len(args) == 1:
    print('Hello World')
  elif len(args) == 2:
    print('Hello, %s!'%args[1])
  else:
    print('Too many arguments!')
if __name__ == '__main__':
  test()

# sys模块有一个argv变量，用list存储了命令行的所有参数。argv至少有一个元素，因为第一个参数永远是该.py文件的名称

print(__doc__)