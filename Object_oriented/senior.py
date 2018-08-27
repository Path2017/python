#!usr/bin/env python3
# -*- coding: utf-8 -*-
class Student(object):
  def __init__(self):
    pass
s = Student()
s.name = "Cris"
print(s.name)

# 从其他类中调用定义的方法:
from mytypeclass import myStudent
b = myStudent('type',20)
b.print_score()
