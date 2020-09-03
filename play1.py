#!/usr/bin/env python


#this is a playground
'''
import math

print("Hello World!!!")

# Int, Float
# 变量 variable， 对象/object， 内置对象/Built-in objects

a_number = 3
b_string = "object"
print(a_number)
print(b_string)
a_number , b_string = b_string , a_number
print(a_number)
print(b_string)
#内置函数 Built-in function
print(type(3))
print(int(5.3333))
print(type(3.0))

a = 0.1
b = 0.2
a,b = b,a
c = round(a + b, 4)
print(c)

print(dir(math))

print(math.pi)
print(math.pow(2,4))
print(2 ** 4)

'''
# String
# 序列/sequence
import math
import sys
'''
print(sys.getdefaultencoding())
a = '200'
print(type('200'))
print('it\'s a new string')

a = 'this'
b = 'that'
c = (a + b) * 3
print(c)
print(len(c))
print('m' in c)


# String 索引/index  切片/slice
s = 'test_this_string'
print(len(s))
print(s[-11])
print(s[2])
print(s[2:7])
print(s[2: -4])
print(s[5: 9])
print(s[: 10: 2])
print(s[:10:-1])

a = input('this is where you input: ')
b = input('this is second you input:')
print(a)
print(b)
c = int(a) + int(b) + 10
print(c)

string = 'this is test'
print(string.index('st'))
string2 = string.split('i')
print(string2)

print('+'.join(string2))

string3 = 'This is an empty field {0}'
print(string3.format('test'))


# list
lst = []
print(type(lst))

lst1 = [1, 2, 3, 1.1234, 'test', []]
print(lst1)
lst2 = [2, 3, 3, 1.1234, 'test', []]
print(lst2)

print(len(lst1))
print(lst1[2])
print(lst1[-2])
print(type(lst1[-2]))
print(lst1[::2])
print(lst1[::-2])
print(lst1 + lst2)
print(lst2 * 2)
print('test' in lst1)

lst1 = [1, 2, 3, 4]
lst1[3] = 200
print(lst1)
print(id(lst1))

lst1.append('test')
print(lst1)

lst1.insert(1, 'hello')
print(lst1)
lst2 = ['a', 'b', 'c']
lst1.extend(lst2)
print(lst1) 
c = 'this'
lst1.extend(c)
print(lst1)

lst1 = ['a', 'b', 'c', 'd']
print(lst1)
lst1.pop(2)
print(lst1)
lst1.pop()
print(lst1)

lst2 = ['h', 'i', 'jk', 'l']
lst1.extend(lst2)
print(lst1)

lst1.sort()
print(lst1)
lst1.reverse()
print(lst1)

a = 'This is a test'
list(a)
print(list(a))
c = ''.join(list(a))
print(c)









# Tuple/元组

tpl = (1, 2, 3, 4, 5, 6, 7, 8, 9, 'this', 'that')
print(tpl)
print(type(tpl))

tpl2 = (-1, 2, 3, 4, 5, 6, 7, 8, 9, 'this', 'that')
a = (100,)
print(type(a))
b = (100)
print(type(b))
print(tpl.index('this'))

# different between tuple and list, element can't change type
# change tuple to list
lst1 = list(tpl2)
print(lst1)
lst1[0] = 100
print(lst1)
tpl2 = tuple(lst1)
print(tpl2)
print(tpl + tpl2)
tpl3 = tpl2 + tpl
print(tpl3)
print(tpl * 2)




# Dictionary
dic = {}
print(type(dic))

dic = {'a' : 1, 'b' : 2, 'c' : 3}
print(dic)
#help(dic)
#key and value, 键值对

dic1 = dict(y=100, x=200, z=300)
print(dic1)
dic1.pop('y')
print(dic1)
print(dic1['x'])
print(len(dic1))
dic1['z'] = 500
print(dic1)
del dic1['z']
print(dic1)

'''
# Dictionary methods
'''
a = dict([('x', 1), ('y', 2)])
print(a)
print(type(a))
print(a['x'])

#print(a.get('z'))
print(a.get('z'), 3)
print(a)

print(a.update([('o', 100), ('p', 200)]))
print(a)
print(a.pop('y'))
print(a)
print(a.popitem())
print(a)
del a['x']
print(a)


'''




# Set
'''
a = set([1, 2, 3, 4,100,300,2000,3000])
print(a)
print(type(a))

a2 = ['test', 100, 1000]
print(a2)

a.add('haha')
print(a)
a.pop()
print(a)
a.remove(100)
print(a)

lst = ['a', 'b', 'c']

print(lst.copy())

'''









