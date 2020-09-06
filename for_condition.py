#! python3
#迭代 iteratable 

'''
for i in 'hello':
    print(i)


lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in lst1:
    print(i, i+10)

dic = {'hello':1, 'byebye':2, 'OK':3}
for k in dic:
    print(k, dic[k])

for k, v in dic.items():
    print(k, v)

import random

lst2 =[]
for i in range(100):
    a = random.randint(1, 10)
    lst2.append(a)
print(lst2)

dic2 = {}
for a in lst2:
    if a in dic2:
        dic2[a] += 1
    else:
        dic2[a] = 1
print(dic2)

#range define
r = range(4)
print(r)


r = range(4)
for i in r:
    print(i)

#print number in 100 can be dvided by 3
b = []
for i in range(100):
    if i % 3 == 0:
        b.append(i)
print(b)  

#or
#list(range(0, 100, 3))

#zip 2 lists
c = [1, 2, 3, 4, 5]
d = ['x', 'y', 'z', 'w', 'x']
r =[]
for i in range(len(c)):
    r.append(str(c[i]) + d[i])
print(r)

r2 = []
for c, d in zip(c, d):
    r2.append(str(c) + d)
print(r2)



#enumarate()
s = ['one', 'two', 'three', 'four', 'five', 'six']
print(list(enumerate(s)))


lst = []
for i in range(10):
    lst.append(i**2)
print(lst)
a = [i**2 for i in range(10)]
print(a)

b = [i for i in range(100) if i%3 == 0]
print(b)

'''
#count the number of letter appearances
a = 'This is a test sentence, please try it out.'
b = {}
for i in a:
    if i.isalpha():
        if i in b:
             b[i] += 1
        else:
            b[i] = 1
print(b)