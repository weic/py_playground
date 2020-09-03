#!/usr/bin/env python
#homework1
'''
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = a[1:8:2]
print('Question 1 answer is:', b)

c = a[::-2]
print('Question 2 answer is:', c)

d = a[0:4]
print('Question 3 answer is:', d)

e = a[3::-1]
print('Question 4 answer is:', e)
'''
#homework2

#homework3

list1=[
    'zero',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
]
num = input('Please input number here:')
new_number = []

for n in num:
    new_number.append(list1[int(n)])
print(' '.join(new_number))