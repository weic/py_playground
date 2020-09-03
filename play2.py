#!/usr/bin/env python

'''
print(type(True))

print(True == False)
print(False == False)

print(bool(1))

print(bool())

#boolem
# > < == != >= <= 

print(1 > 2)

a = (2 > 1) and (3 > 4)
print(a)

a, b, *c= 1, 2, 3, 4, 5
print(a)
print(b)
print(c)
'''
from math import pi
from random import randint
a = randint(1, 10)
print('This is randomly generated number:', a)
if a >= pi:
    ci = a * pi
    area = (a / 2) * (a / 2) * pi
    print('The length of circile is:', round(ci, 2))
    print('The area of circile is:', round(area, 2))
else:
    ci = 2 * a * pi
    area = a * a * pi
    print('The length of circile is:', round(ci, 2))
    print('The area of circile is:', round(area, 2))




