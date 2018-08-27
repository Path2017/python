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