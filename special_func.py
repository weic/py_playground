#! python3
# special function
# ----------------------------------------------------------------
# lambda / map / filter
# ----------------------------------------------------------------

# lambda

def add(x):
    x += 2
    return x
print(add(5))

lam = lambda x: x+2
print(lam(5))

# map
m = map(lambda x: x+2, range(10))
print(list(m))

lst1 = [1,2,3,4,5]
lst2 = [6,7,8,9,0]
lst3 = [7,8,9,2,1]

lst4 = [x+y+z for x,y,z in zip(lst1,lst2,lst3)]
print(lst4)

r = map(lambda x, y, z: x+y+z, lst1, lst2, lst3)
print(list(r))

#filter
n = range(-5, 5)
f = filter(lambda x: x>0, n)
print(list(f))

lst_a = ['apple', 'banana', 'cherry']
lst_b = ['orange', 'lemon', 'pineapple']

lst_new = map(lambda x, y: x + y, lst_a, lst_b)
print(list(lst_new))

#more practise hxxps://www.w3resource.com/python-exercises/lambda/index.php

# 1.Write a Python program to create a lambda function that adds 15 to a given 
# number passed in as an argument, also create a lambda function that multiplies 
# argument x with argument y and print the result

a = lambda x : x + 15
print(a(1))

b = lambda x,y : x * y
print(b(3, 4))

# 2. Write a Python program to create a function that takes one argument, and 
# that argument will be multiplied with an unknown given number.

def func_compute(n):
 return lambda x : x * n
result = func_compute(2)
print(result(3))
