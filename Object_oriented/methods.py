#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# methods - type()
# True
print(type(123) == int)
# True
print(type('123') == str)

# methods - isinstance()
# True
print(isinstance('a', str))
# True
print(isinstance(123, int))
# True
print(isinstance(b'a', bytes))

# methods - dir() 获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法
# ['__add__', '__class__',..., '__subclasshook__', 'capitalize', 'casefold',..., 'zfill']
print(dir('ABC'))